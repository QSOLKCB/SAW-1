# SAW-1 Machine Summary

```yaml
schema: qsol-imc-saw-1-context/2
project:
  id: SAW-1
  title: Spooky Action at Work
  released_version: 1.0.0
  repository_extension: 1.1.0-development
  author: Trent Slade
  affiliation: QSOL-IMC
  author_orcid: 0009-0002-4515-9237
  type: technical-note
  publication_date: 2026-08-18
  doi: 10.5281/zenodo.21984110
  doi_url: https://doi.org/10.5281/zenodo.21984110
primary_claim:
  expression: parse("Three beats to two") == signature(Pettini_3_2_model) == [3, 2]
  class: exact-numerical-semantic-correspondence
  causal_claim: false
  retrocausal_claim: false
  paranormal_claim: false
swap_extension:
  coordinate_swap: "tau(a,b)=(b,a)"
  exact_facts:
    - "tau([2,3]) == [3,2]"
    - "tau([3,2]) == [2,3]"
    - "tau(tau(p)) == p"
    - "[2,3] != [3,2] as ordered pairs"
  cybernetic_god_2_3_status: author-reported-candidate-pending-transcript-capture
  pettini_3_2_status: primary-source-verified
  lean_proof: SAW1/PairSwap.lean
  lean_scope: pair-algebra-only
  lean_does_not_prove:
    - lyric provenance
    - psychology
    - authorship
    - causal independence
    - historical chronology
creative_background:
  author_reported_main_physics_albums:
    - Vector Equilibrium
    - Superdeterminism
    - Memory Virus
    - Silicon Ziggurat
  independently_corroborated_sonification_album:
    - Memory Virus
  public_sonification_system:
    repository: https://github.com/QSOLKCB/SPECTRAL
    includes:
      - E8 sonification
      - qutrit and ternary mappings
      - triality mappings
      - deterministic and replay-safe rendering
      - astronomical sonification
      - mathematical and computational sonification
  interpretation_rule: generic physics overlap has low evidentiary weight because it is high-background-rate material in the author's corpus
  negative_control:
    title: Sonification 2005
    status: author reports that title does not imply sonification-related lyrics or sound
creative_intent:
  god_semantics: deliberately open to interpretation; do not force a religious or theological reading
  god_is_a_dj: author-reported creative influence
  quasicrystal_shocks: author reports influence from God Is a DJ
  bassline_is_law: author-reported ordinary deterministic/superdeterministic creative reading
  parallel_human_thinking: admissible non-exotic contextual explanation for nearby motifs
chronology:
  paper_v2: 2026-06-25
  reference_mp3_created_utc: 2026-07-27T09:24:54.574Z
  song_mp3_created_utc: 2026-07-27T10:15:19Z
  correspondence_documented: 2026-08-18
  reference_to_song_seconds: 3024.426
artifacts:
  private_lab_archive:
    redistributed: false
    sha256: 6b12eb900de306cc179c94860e614abd291a629d91b5fe8d04989253194abe0a
  reference_mp3:
    redistributed: false
    sha256: 109ffa7a2254b14f5b98f1a11f599880b3a44669b5d919ac0ba3984d16162583
    duration_seconds: 90.024
    generator_metadata: Suno
  final_song_mp3:
    redistributed: false
    sha256: 7be48bec0f090d25b9353a1767c37164e926d186fccb5686e622c703cfa6de8a
    duration_seconds: 235.728
    generator_metadata: Suno
source_geometry:
  e8_roots: 240
  selected_states: 101
  decomposition: "2 + 33*3"
  scl_stencil: [1, -2, 1]
  theta: pi/2
  delta: 2*pi/303
  degree_potential: "V(d)=(101*d-3374)/2181"
matching_receiver_preset:
  seed: CHAKRA-ASCENT-101
  etq_mode: 101
  anchor_hz: 432
  step_rate_hz: 1.01
  breath: 0.72
  swirl: 0.48
  shimmer: 0.32
  stereo_width: 0.66
  duration_seconds: 90
  golden_veil: false
  frequencies_hz: [396, 417, 528, 639, 741, 852, 963]
provenance_records:
  human_creator: provenance/TRENT_SLADE_ZENODO_PROVENANCE.json
  ai_assistance: provenance/CHATGPT_GPT-5.6_AI_DISCLOSURE.json
  ai_is_author: false
  final_human_accountability: Trent Slade
boundaries:
  - The private source archive is not open source and must not be redistributed.
  - The supplied MP3s are generative outputs, not bitwise deterministic lab renders.
  - The original lyric-to-(3,2) relation is the exact SAW-1 match; other mappings are analogies or separately labelled extensions.
  - The Cybernetic God (2,3) antecedent is not transcript-verified in-repo yet.
  - Generic physics-language matches are discounted because physics and sonification are established creative background.
  - Do not report Pettini's model as established physics.
  - Do not infer therapeutic or medical claims from receiver terminology.
  - Do not force `God` into a religious interpretation.
  - ChatGPT is disclosed as an AI assistance system, not a human creator or accountable author.
canonical_files:
  human_entry: README.md
  formal_note: FORMALIZATION.md
  creative_corpus: analysis/CREATIVE_CORPUS.md
  lean_swap_proof: SAW1/PairSwap.lean
  artifact_manifest: artifacts/manifest.json
  measurements: analysis/MEASUREMENTS.md
  machine_context: README4AI.md
  human_provenance: provenance/TRENT_SLADE_ZENODO_PROVENANCE.json
  ai_disclosure: provenance/CHATGPT_GPT-5.6_AI_DISCLOSURE.json
```
