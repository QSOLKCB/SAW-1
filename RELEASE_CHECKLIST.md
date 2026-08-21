# SAW-1 v1.2.1 Release Checklist

## Reserved record

- [x] Reserve Zenodo DOI `10.5281/zenodo.22045037` for the v1.2.1 record.
- [x] Record the reserved DOI as **reserved, not yet published** in `zenodo-import/ZENODO_V1_2_1_RESERVED_RECORD.json`.
- [x] Preserve the existing related-works text and append v1.2.1 information in `zenodo-import/RELATED_IDENTIFIERS_NOTE.md`.
- [x] Prepare `zenodo-import/ZENODO_V1_2_1_METADATA_COPY_PASTE.txt` with Resource type, Title, Description, Notes, and Keywords.

## Pre-merge validation

- [ ] Resolve all substantive PR review threads.
- [ ] Obtain a fresh adversarial Codex review of the final candidate head.
- [ ] Run `python scripts/validate_metadata.py` and confirm the original v1.0.0 artifact chronology still passes.
- [ ] Run `python -O scripts/validate_metadata.py`.
- [ ] Run Python utility compilation.
- [ ] Run the pinned Lean 4 `lake build` and confirm the coordinate-swap proof passes.
- [ ] Confirm `SAW1/PairSwap.lean` contains only explicit pair algebra and no song/author/physics semantic constants.
- [ ] Confirm `FORMALIZATION_1_2_1.md`, README, README4AI, cognitive note, corpus note, references, and changelog agree on all evidence classes.
- [ ] Confirm the Cybernetic God `(2,3)` antecedent is still labelled author-reported pending transcript-level capture.
- [ ] Confirm no unverified date is attached to the candidate motif/memory state.

## Version and metadata boundary

- [ ] Confirm `lakefile.lean` says `1.2.1`.
- [ ] Confirm README and README4AI identify `1.2.1` as the target/current development release.
- [ ] Confirm DOI `10.5281/zenodo.22045037` is labelled **reserved, not yet published** everywhere before Zenodo publication.
- [ ] Keep the published v1.0.0 DOI `10.5281/zenodo.21984110` attached to the existing v1.0.0 archival record.
- [ ] Do not silently rewrite the existing related-identifiers note; use the additive v1.2.1 section.

`CITATION.cff` and `.zenodo.json` currently preserve the canonical published-v1.0.0 metadata. If the v1.2.1 Zenodo workflow is performed manually using the prepared copy-paste metadata, they may remain historical v1.0.0 metadata with the release-state distinction documented in README/README4AI. If they are intentionally promoted to v1.2.1 metadata before release, update the metadata validator in the same reviewed change so CI does not encode contradictory version expectations.

## Release

- [ ] Merge the validated pull request into `main`.
- [ ] Confirm the merge commit is the intended v1.2.1 source state.
- [ ] Create Git tag `v1.2.1` from that validated commit.
- [ ] Create GitHub release `SAW-1 v1.2.1 — Spooky Action at Work`.
- [ ] Use `CHANGELOG.md` as the release-note basis.
- [ ] Publish the prepared Zenodo record for DOI `10.5281/zenodo.22045037`.
- [ ] Verify the Zenodo resource type is **Publication / Technical note**.
- [ ] Verify creator is **Slade, Trent — QSOL-IMC**.
- [ ] Verify the record licence applies to the technical note/repository metadata and not to excluded audio/private source/third-party material.
- [ ] Verify the repository URL is recorded in Zenodo's dedicated Repository URL field.
- [ ] Verify the related identifier includes `arXiv:2606.12457` and that the contextual note preserves the supplied references.
- [ ] Verify the published Zenodo record resolves at `https://doi.org/10.5281/zenodo.22045037`.

## Post-publication

- [ ] Change any `reserved-not-published` statements for DOI `10.5281/zenodo.22045037` to the accurate published state in a metadata-only follow-up if needed.
- [ ] Record the final v1.2.1 Git tag, release commit, and publication date in the reserved-record JSON or its published successor.
- [ ] Re-run CI after any post-publication metadata-only update.
