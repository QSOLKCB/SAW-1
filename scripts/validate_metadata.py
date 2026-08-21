#!/usr/bin/env python3
"""Validate SAW-1 release metadata without private artifacts."""

from __future__ import annotations

import json
import re
from datetime import date, datetime, time, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SHA256 = re.compile(r"^[0-9a-f]{64}$")
EXPECTED_PAPER_DATE = "2026-06-25"
EXPECTED_DOCUMENTATION_DATE = "2026-08-18"
EXPECTED_ZENODO_VERSION = "1.2.1"
EXPECTED_ZENODO_PUBLICATION_DATE = "2026-08-21"
EXPECTED_TIMESTAMPS = {
    "reference-track": "2026-07-27T09:24:54.574Z",
    "industrial-metal-god": "2026-07-27T10:15:19Z",
}
EXPECTED_HASHES = {
    "source-lab-private-archive": "6b12eb900de306cc179c94860e614abd291a629d91b5fe8d04989253194abe0a",
    "reference-track": "109ffa7a2254b14f5b98f1a11f599880b3a44669b5d919ac0ba3984d16162583",
    "industrial-metal-god": "7be48bec0f090d25b9353a1767c37164e926d186fccb5686e622c703cfa6de8a",
}
EXPECTED_ARTIFACT_IDS = {
    "source-lab-private-archive",
    "reference-track",
    "industrial-metal-god",
    "pettini-arxiv-v2",
    "hossenfelder-video",
}
EXPECTED_RELATIONS = (
    (
        "source-lab-private-archive",
        "supplies-symbolic-and-receiver-basis-for",
        "reference-track",
        "provenance-bounded",
    ),
    (
        "reference-track",
        "user-reported-cover-reference-for",
        "industrial-metal-god",
        "user-supplied",
    ),
    (
        "industrial-metal-god",
        "contains-exact-semantic-correspondence-with",
        "pettini-arxiv-v2",
        "exact-for-ordered-pair-3-2",
    ),
    (
        "hossenfelder-video",
        "prompted-later-recognition-of",
        "industrial-metal-god",
        "documented-observation",
    ),
)


def load_json(relative: str) -> Any:
    with (ROOT / relative).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_utc(value: str, artifact_id: str) -> datetime:
    require(value.endswith("Z"), f"{artifact_id} createdUtc must end with Z")
    try:
        parsed = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
    except ValueError as exc:
        raise ValueError(f"invalid createdUtc for {artifact_id}: {value}") from exc
    require(parsed.utcoffset() is not None, f"{artifact_id} createdUtc must be timezone-aware")
    return parsed


def parse_canonical_date(value: Any, label: str, expected: str) -> date:
    require(value == expected, f"canonical {label} changed: expected {expected}, got {value}")
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"invalid {label}: {value}") from exc
    require(parsed.isoformat() == value, f"{label} must use canonical YYYY-MM-DD syntax")
    return parsed


def main() -> None:
    manifest = load_json("artifacts/manifest.json")
    zenodo = load_json(".zenodo.json")

    require(
        manifest.get("schema") == "qsol-imc-saw-1-artifact-manifest/1",
        "unexpected artifact manifest schema",
    )
    project = manifest.get("project", {})
    require(project.get("id") == "SAW-1", "unexpected project ID")
    require(project.get("version") == "1.0.0", "unexpected manifest project version")
    require(
        zenodo.get("version") == EXPECTED_ZENODO_VERSION,
        f"unexpected Zenodo version: expected {EXPECTED_ZENODO_VERSION}",
    )
    require(
        zenodo.get("publication_type") == "technicalnote",
        "Zenodo publication_type must be technicalnote",
    )

    documentation_date = parse_canonical_date(
        project.get("publicationDate"),
        "project publicationDate",
        EXPECTED_DOCUMENTATION_DATE,
    )
    require(
        zenodo.get("publication_date") == EXPECTED_ZENODO_PUBLICATION_DATE,
        "Zenodo publication_date differs from published v1.2.1 release date",
    )

    artifacts = manifest.get("artifacts")
    require(isinstance(artifacts, list), "manifest artifacts must be a list")

    by_id: dict[str, dict[str, Any]] = {}
    for artifact in artifacts:
        require(isinstance(artifact, dict), "each artifact must be an object")
        artifact_id = artifact.get("id")
        require(isinstance(artifact_id, str), "every artifact must have a string ID")
        require(artifact_id not in by_id, f"duplicate artifact ID: {artifact_id}")
        by_id[artifact_id] = artifact

        if "sha256" in artifact:
            digest = artifact["sha256"]
            require(
                isinstance(digest, str) and SHA256.fullmatch(digest) is not None,
                f"invalid SHA-256 syntax for {artifact_id}",
            )

    require(set(by_id) == EXPECTED_ARTIFACT_IDS, "artifact ID set differs from canonical manifest")

    for artifact_id, expected_hash in EXPECTED_HASHES.items():
        require(
            by_id[artifact_id].get("sha256") == expected_hash,
            f"canonical SHA-256 changed for {artifact_id}",
        )

    paper_date = parse_canonical_date(
        by_id["pettini-arxiv-v2"].get("date"),
        "pettini-arxiv-v2 date",
        EXPECTED_PAPER_DATE,
    )

    parsed_times: dict[str, datetime] = {}
    for artifact_id, expected_timestamp in EXPECTED_TIMESTAMPS.items():
        actual_timestamp = by_id[artifact_id].get("createdUtc")
        require(
            actual_timestamp == expected_timestamp,
            f"canonical createdUtc changed for {artifact_id}: "
            f"expected {expected_timestamp}, got {actual_timestamp}",
        )
        parsed_times[artifact_id] = parse_utc(expected_timestamp, artifact_id)

    paper_time = datetime.combine(paper_date, time.min, tzinfo=timezone.utc)
    reference_time = parsed_times["reference-track"]
    song_time = parsed_times["industrial-metal-god"]
    documentation_time = datetime.combine(
        documentation_date,
        time.min,
        tzinfo=timezone.utc,
    )
    require(
        paper_time < reference_time < song_time < documentation_time,
        "canonical chronology must satisfy paper < reference < song < documentation",
    )
    require(
        abs((song_time - reference_time).total_seconds() - 3024.426) < 0.001,
        "reference-to-song interval is not 3024.426 seconds",
    )

    relations = manifest.get("relations")
    require(isinstance(relations, list), "manifest relations must be a list")
    actual_relations: list[tuple[str, str, str, str]] = []
    seen_relations: set[tuple[str, str, str, str]] = set()
    required_relation_fields = {"subject", "predicate", "object", "strength"}
    for relation in relations:
        require(isinstance(relation, dict), "each relation must be an object")
        require(
            set(relation) == required_relation_fields,
            "each relation must contain exactly subject, predicate, object, and strength",
        )
        subject = relation["subject"]
        predicate = relation["predicate"]
        object_id = relation["object"]
        strength = relation["strength"]
        require(subject in by_id, f"unknown relation subject: {subject}")
        require(object_id in by_id, f"unknown relation object: {object_id}")
        require(isinstance(predicate, str), "relation predicate must be a string")
        require(isinstance(strength, str), "relation strength must be a string")
        relation_key = (subject, predicate, object_id, strength)
        require(relation_key not in seen_relations, f"duplicate relation: {relation_key}")
        seen_relations.add(relation_key)
        actual_relations.append(relation_key)

    require(
        tuple(actual_relations) == EXPECTED_RELATIONS,
        "complete relation sequence differs from canonical manifest",
    )

    print("SAW-1 metadata validation passed")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"SAW-1 metadata validation failed: {exc}") from exc
