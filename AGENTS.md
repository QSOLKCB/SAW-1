# AGENTS.md — SAW-1 Editing Contract

## Priority order

1. Preserve artifact provenance and hashes.
2. Preserve the chronology `paper < reference < song < documented observation` for the original SAW-1 chain.
3. Keep exact claims separate from analogies, author reports, conditional claims, and explanatory hypotheses.
4. Keep private source and audio outside the repository.
5. Prefer compact mathematical documentation over framework or tooling bloat.

## Non-negotiable statements

- The paper v2 date is **25 June 2026**.
- The reference MP3 was created at **2026-07-27T09:24:54.574Z**.
- The final song MP3 was created at **2026-07-27T10:15:19Z**.
- The two audio creations are separated by **3024.426 seconds**.
- The exact original correspondence is `parse("Three beats to two") = (3,2)`.
- The paper's proposed spacetime signature is `(3,2)`.
- The original correspondence is semantic and retrospective, not causal or retrocausal.
- `(2,3)` and `(3,2)` are different ordered pairs.
- Coordinate exchange `tau(a,b)=(b,a)` maps `(2,3)` exactly to `(3,2)` and is an involution.
- The Cybernetic God `(2,3)` antecedent is currently an **author-reported candidate** until transcript-level evidence is committed or independently archived.
- Lean proves the pair algebra only; it does not prove lyric provenance, psychology, authorship, causation, or historical independence.

## Source boundary

`E8-Chakra-Vortexmouth-Lab-v1.0.0(1).zip` is private closed-source material. Do not add its source files to this repository. Equations already extracted into the formal note may be maintained, but do not reconstruct or publish the application code.

The MP3 files are evidence artifacts and are not committed. Validate supplied local files against `artifacts/manifest.json` before deriving new measurements.

## Physics boundary

Describe Marco Pettini's work as a proposal, hypothesis, or model. Do not state that a second time dimension has been discovered. Distinguish results proved within the adopted ansatz from unrestricted physical uniqueness claims.

Physics, mathematics, determinism, sonification, E8, triality, and related language are established parts of the author's creative background. Generic thematic overlap must not be promoted to an exact correspondence.

## Creative-intent boundary

Author-reported influence and intent may be recorded when explicitly labelled as such. In particular:

- `God` in the author's music is intentionally open to interpretation and is not to be rewritten as a required religious figure;
- `His bassline is law` may be documented as an ordinary deterministic/superdeterministic creative reading, not as a physics theorem;
- the reported creative lineage from `God Is a DJ`, `Cybernetic God`, and related works is context, not proof of causal exclusivity;
- ordinary parallel or convergent human thinking is an admissible **non-exotic explanatory possibility** for nearby motifs such as `(2,3)` and `(3,2)`, not a case-level sufficient explanation.

## Cognitive-mechanism boundary

Memory-science concepts may be used only as **general explanatory possibilities**, never as retrospective diagnosis or proof of the author's mental state.

Literature-backed background concepts include:

- implicit memory;
- source monitoring and source-attribution uncertainty;
- pattern completion, used only as a bounded cue/reconstruction analogy.

Repository-defined or adapted explanatory language includes:

- associative reconstruction;
- source-uncertain self-retrieval;
- qualified `cryptomnesia-like self-retrieval`;
- parallel or convergent reconstruction.

Do not describe repository-defined or adapted language as an established mechanism merely because related literature exists.

Required wording discipline:

- Prefer **`associative reconstruction with uncertain source attribution`** as the umbrella phrase.
- Do not diagnose a `source-monitoring failure` from the music; say `source-attribution uncertainty` when discussing the possibility.
- `Cryptomnesia` is usually discussed as inadvertent plagiarism. When the candidate source is the author's own earlier work, do not call the case plagiarism. Use `cryptomnesia-like self-retrieval` only as an explicitly qualified analogy, not as a literature-established self-reuse mechanism.
- Do not claim that the author has `photographic memory`, `eidetic memory`, exceptional memory, amnesia, or any other memory phenotype or disorder.
- Do not infer a specific brain region, hippocampal event, or neurological mechanism from a lyric.
- Do not convert memory-science background into evidence that the Cybernetic God antecedent exists; lyric provenance still requires artifact evidence.
- A schematic retrieval arrow may be used in prose or equations, but it must be labelled possible/unobserved and must never be encoded as a Lean theorem or axiom.
- Do not attach an unverified date or year to a candidate memory/motif state. Use an undated label such as `M_candidate` unless the date itself is independently classified and supported.
- Describe cognitive mechanisms as **compatible or available explanatory possibilities**, not as sufficient explanations of the lyric.

The cognitive-mechanism reference note is `analysis/COGNITIVE_MECHANISMS.md`.

## Audio boundary

The private lab has deterministic seeded synthesis properties within its implementation. The attached reference and final song MP3s identify themselves as Suno-generated. Never collapse those two provenance layers into a claim that the MP3s are deterministic lab renders.

## Lean boundary

Lean 4 is permitted only for compact propositions that are genuinely mathematical and independently checkable from explicit definitions in this repository.

Current permitted proof scope:

- coordinate swap;
- involution of coordinate swap;
- inequality of `(2,3)` and `(3,2)` as ordered pairs;
- equality after one coordinate swap;
- same-orbit-under-swap statements.

Do not encode author reports, publication dates, search-engine findings, lyric authorship, psychological explanations, or cognitive mechanisms as axioms merely to obtain a theorem.

## Editing style

- Use UTF-8 Markdown and LaTeX-compatible equations.
- Use ISO 8601 UTC timestamps.
- Use SHA-256 in lowercase hexadecimal.
- Avoid dependencies unless they directly improve reproducibility.
- Keep the Lean surface deliberately small and pinned.
- Do not write bloat.
