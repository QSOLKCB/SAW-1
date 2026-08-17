#!/usr/bin/env python3
"""Validate SAW-1 release metadata without private artifacts."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def load_json(relative: str):
    with (ROOT / relative).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    manifest = load_json("artifacts/manifest.json")
    zenodo = load_json(".zenodo.json")

    assert manifest["schema"] == "qsol-imc-saw-1-artifact-manifest/1"
    assert manifest["project"]["version"] == "1.0.0"
    assert zenodo["version"] == "1.0.0"
    assert zenodo["publication_type"] == "technicalnote"

    times = []
    identifiers = set()
    for artifact in manifest["artifacts"]:
        artifact_id = artifact["id"]
        assert artifact_id not in identifiers, artifact_id
        identifiers.add(artifact_id)
        if "sha256" in artifact:
            assert SHA256.fullmatch(artifact["sha256"]), artifact_id
        if "createdUtc" in artifact:
            times.append(
                datetime.fromisoformat(artifact["createdUtc"].replace("Z", "+00:00"))
            )

    assert len(times) == 2
    assert abs((max(times) - min(times)).total_seconds() - 3024.426) < 0.001

    for relation in manifest["relations"]:
        assert relation["subject"] in identifiers
        assert relation["object"] in identifiers

    print("SAW-1 metadata validation passed")


if __name__ == "__main__":
    main()
