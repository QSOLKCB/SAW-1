# SAW-1 v1.0.0 Release Checklist

- [ ] Merge the release pull request into `main`.
- [ ] Confirm the repository is enabled in the Zenodo GitHub integration.
- [ ] Run `python scripts/validate_metadata.py` on `main`.
- [ ] Confirm `CITATION.cff` and `.zenodo.json` both say `1.0.0`.
- [ ] Confirm the three evidence hashes in `artifacts/manifest.json` match the local files.
- [ ] Create Git tag `v1.0.0` from the validated `main` commit.
- [ ] Create the GitHub release titled `SAW-1 v1.0.0 — Spooky Action at Work`.
- [ ] Use `CHANGELOG.md` as the release-note basis.
- [ ] Wait for Zenodo to archive the release.
- [ ] Verify the Zenodo record type is **Publication / Technical note**.
- [ ] Verify creator is **Slade, Trent — QSOL-IMC**.
- [ ] Verify the record licence applies to the technical note, not the excluded audio/private source.
- [ ] Add the minted DOI to `CITATION.cff`, `.zenodo.json`, and the README badge in a metadata-only follow-up release.
