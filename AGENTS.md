# AGENTS.md — SAW-1 Editing Contract

## Priority order

1. Preserve artifact provenance and hashes.
2. Preserve the chronology `paper < reference < song < documented observation`.
3. Keep exact claims separate from analogies.
4. Keep private source and audio outside the repository.
5. Prefer compact mathematical documentation over framework or tooling bloat.

## Non-negotiable statements

- The paper v2 date is **25 June 2026**.
- The reference MP3 was created at **2026-07-27T09:24:54.574Z**.
- The final song MP3 was created at **2026-07-27T10:15:19Z**.
- The two audio creations are separated by **3024.426 seconds**.
- The exact correspondence is `parse("Three beats to two") = (3,2)`.
- The paper's proposed spacetime signature is `(3,2)`.
- The correspondence is semantic and retrospective, not causal or retrocausal.

## Source boundary

`E8-Chakra-Vortexmouth-Lab-v1.0.0(1).zip` is private closed-source material. Do not add its source files to this repository. Equations already extracted into the formal note may be maintained, but do not reconstruct or publish the application code.

The MP3 files are evidence artifacts and are not committed. Validate supplied local files against `artifacts/manifest.json` before deriving new measurements.

## Physics boundary

Describe Marco Pettini's work as a proposal, hypothesis, or model. Do not state that a second time dimension has been discovered. Distinguish results proved within the adopted ansatz from unrestricted physical uniqueness claims.

## Audio boundary

The private lab has deterministic seeded synthesis properties within its implementation. The attached reference and final song MP3s identify themselves as Suno-generated. Never collapse those two provenance layers into a claim that the MP3s are deterministic lab renders.

## Editing style

- Use UTF-8 Markdown and LaTeX-compatible equations.
- Use ISO 8601 UTC timestamps.
- Use SHA-256 in lowercase hexadecimal.
- Avoid dependencies unless they directly improve reproducibility.
- Do not add Lean, Coq, Isabelle, or another proof assistant unless a future version explicitly changes scope.
- Do not write bloat.
