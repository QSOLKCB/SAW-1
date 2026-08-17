#!/usr/bin/env python3
"""SAW-1 fixed-window spectral probe. Requires NumPy, ffmpeg, and ffprobe."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "artifacts" / "manifest.json"
SR = 48_000
WINDOW = 2.0


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_expected_hashes(manifest_path: Path) -> dict[str, str]:
    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)

    artifacts = {artifact["id"]: artifact for artifact in manifest["artifacts"]}
    expected: dict[str, str] = {}
    for artifact_id in ("reference-track", "industrial-metal-god"):
        try:
            expected[artifact_id] = artifacts[artifact_id]["sha256"]
        except KeyError as exc:
            raise ValueError(
                f"manifest is missing canonical SHA-256 for {artifact_id}"
            ) from exc
    return expected


def decode(path: Path) -> np.ndarray:
    command = [
        "ffmpeg", "-v", "error", "-i", str(path),
        "-f", "f32le", "-ac", "1", "-ar", str(SR), "-",
    ]
    return np.frombuffer(
        subprocess.run(command, check=True, capture_output=True).stdout,
        dtype=np.float32,
    ).copy()


def measure(samples: np.ndarray, centre: float) -> dict[str, float]:
    length = int(WINDOW * SR)
    start = max(0, int(centre * SR) - length // 2)
    end = min(samples.size, start + length)
    start = max(0, end - length)
    values = samples[start:end].astype(np.float64, copy=False)
    if values.size < length:
        values = np.pad(values, (0, length - values.size))

    spectrum = np.abs(np.fft.rfft(values * np.hanning(length)))
    frequency = np.fft.rfftfreq(length, 1 / SR)
    power = spectrum**2
    power[0] = 0
    total = power.sum()
    centroid = np.sum(frequency * power) / total
    bandwidth = np.sqrt(np.sum((frequency - centroid) ** 2 * power) / total)
    rolloff = frequency[np.searchsorted(np.cumsum(power), 0.85 * total)]
    mask = (frequency >= 20) & (frequency <= 12_000)
    dominant = frequency[mask][np.argmax(power[mask])]

    return {
        "centre_seconds": centre,
        "rms": round(float(np.sqrt(np.mean(values**2))), 6),
        "dominant_hz": round(float(dominant), 3),
        "power_centroid_hz": round(float(centroid), 3),
        "rolloff_85_hz": round(float(rolloff), 3),
        "bandwidth_hz": round(float(bandwidth), 3),
    }


def analyse(
    path: Path,
    centres: list[float],
    *,
    artifact_id: str,
    expected_sha256: str,
) -> dict:
    actual_sha256 = sha256(path)
    if actual_sha256 != expected_sha256:
        raise ValueError(
            f"{artifact_id} SHA-256 mismatch for {path}: "
            f"expected {expected_sha256}, got {actual_sha256}"
        )

    samples = decode(path)
    return {
        "artifact_id": artifact_id,
        "file": {
            "name": path.name,
            "bytes": path.stat().st_size,
            "sha256": actual_sha256,
        },
        "decode": {
            "sample_rate_hz": SR,
            "channels": 1,
            "duration_seconds": round(samples.size / SR, 6),
        },
        "method": {
            "window": "2-second Hann",
            "spectrum": "power = abs(rfft(x*hann))**2",
        },
        "windows": [measure(samples, centre) for centre in centres],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("reference", type=Path)
    parser.add_argument("song", type=Path)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="artifact manifest containing canonical evidence hashes",
    )
    args = parser.parse_args()
    for path in (args.reference, args.song, args.manifest):
        if not path.is_file():
            parser.error(f"file not found: {path}")

    try:
        expected = load_expected_hashes(args.manifest)
        result = {
            "schema": "qsol-imc-saw-1-audio-probe/1",
            "reference": analyse(
                args.reference,
                [15.0, 45.0, 75.0],
                artifact_id="reference-track",
                expected_sha256=expected["reference-track"],
            ),
            "song": analyse(
                args.song,
                [30.0, 90.0, 150.0, 210.0],
                artifact_id="industrial-metal-god",
                expected_sha256=expected["industrial-metal-god"],
            ),
        }
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        parser.error(str(exc))

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
