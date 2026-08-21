# SAW-1 v1.2.1 Release Checklist

## Published record

- [x] GitHub tag `v1.2.1` exists and points to release commit `829c0db54b26071daf0e0ad0c9fc33891d9acfd4`.
- [x] GitHub release `SAW-1 v1.2.1 — Spooky Action at Work` is published.
- [x] Zenodo DOI `10.5281/zenodo.22045037` is published for v1.2.1.
- [x] The previous v1.0.0 DOI `10.5281/zenodo.21984110` remains preserved as the earlier archival version.
- [x] Resource type is **Publication / Technical note**.
- [x] Creator is **Slade, Trent — QSOL-IMC**.
- [x] Related-work text preserves the supplied human-facing contextual version labels separately from canonical machine release state.

## Post-publication metadata alignment

- [x] Promote `CITATION.cff` to version `1.2.1` and DOI `10.5281/zenodo.22045037`.
- [x] Promote `.zenodo.json` to version `1.2.1` with the published v1.2.1 release date and archival metadata.
- [x] Replace the reserved DOI helper with `zenodo-import/ZENODO_V1_2_1_PUBLISHED_RECORD.json`.
- [x] Record GitHub tag, release URL, release commit, publication date, preferred citation, and prior-version DOI in the published-record JSON.
- [x] Update README and README4AI from `reserved-not-published` to published v1.2.1 state.
- [x] Update `REFERENCES.md`, `CHANGELOG.md`, related-identifiers text, and Zenodo copy-paste metadata to the published DOI state.
- [x] Update `scripts/validate_metadata.py` to validate v1.2.1 Zenodo metadata while preserving the immutable v1.0.0 artifact chronology and hashes.
- [ ] Confirm the post-publication metadata PR passes canonical Python validation, optimized Python validation, Python utility compilation, and pinned Lean `lake build` on the exact final head.

## Evidence and theorem boundaries retained

- [x] `SAW1/PairSwap.lean` contains explicit pair algebra only and no song/author/physics semantic constants.
- [x] The Cybernetic God `(2,3)` antecedent remains author-reported pending transcript-level capture.
- [x] No unverified date is attached to the candidate motif/memory state.
- [x] Memory-science background remains possibility-level rather than case proof.
- [x] `cryptomnesia-like self-retrieval` remains a qualified repository analogy rather than a literature-established self-reuse mechanism.
- [x] Coordinate swap remains a mathematical transformation, not an explanation of lyric production.

## Canonical published identifiers

Current published record:

```text
Version: 1.2.1
DOI: 10.5281/zenodo.22045037
GitHub release: https://github.com/QSOLKCB/SAW-1/releases/tag/v1.2.1
Release commit: 829c0db54b26071daf0e0ad0c9fc33891d9acfd4
```

Earlier published record:

```text
Version: 1.0.0
DOI: 10.5281/zenodo.21984110
```
