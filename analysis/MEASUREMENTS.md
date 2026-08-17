# Audio Measurements

## Method

The measurements below use the supplied MP3 files, decoded by FFmpeg to:

- mono float32;
- 48,000 samples per second;
- fixed two-second Hann windows.

For magnitude spectrum \(X_t(f)\), power is:

\[
P_t(f)=|X_t(f)|^2.
\]

The power-weighted spectral centroid is:

\[
\mu_f(t)=\frac{\sum_f fP_t(f)}{\sum_fP_t(f)}.
\]

The 85% roll-off \(r_{0.85}(t)\) is the lowest frequency satisfying:

\[
\sum_{f\le r_{0.85}}P_t(f)
\ge
0.85\sum_fP_t(f).
\]

The dominant bin is the maximum-power FFT bin between 20 Hz and 12 kHz.

## Reference track

Artifact SHA-256:

```text
109ffa7a2254b14f5b98f1a11f599880b3a44669b5d919ac0ba3984d16162583
```

| Centre | RMS | Dominant | Centroid | 85% roll-off | Bandwidth |
|---:|---:|---:|---:|---:|---:|
| 15 s | 0.2026 | 481.5 Hz | 448.4 Hz | 482.0 Hz | 94.7 Hz |
| 45 s | 0.2026 | 481.5 Hz | 475.8 Hz | 482.0 Hz | 109.7 Hz |
| 75 s | 0.2411 | 481.5 Hz | 618.6 Hz | 853.0 Hz | 229.9 Hz |

Interpretation:

- the dominant bin remains stable near 481.5 Hz;
- the centroid and bandwidth increase substantially late in the track;
- the 85% roll-off rises from 482 Hz to 853 Hz;
- RMS also rises in the late window.

This is consistent with a static ground tone plus increasing high-frequency resonance and saturation.

## Final song spot checks

Artifact SHA-256:

```text
7be48bec0f090d25b9353a1767c37164e926d186fccb5686e622c703cfa6de8a
```

| Centre | RMS | Dominant | Centroid | 85% roll-off |
|---:|---:|---:|---:|---:|
| 30 s | 0.2325 | 88.0 Hz | 1126.1 Hz | 2439.0 Hz |
| 90 s | 0.1825 | 113.5 Hz | 2759.6 Hz | 6056.5 Hz |
| 150 s | 0.2861 | 58.5 Hz | 632.3 Hz | 641.5 Hz |
| 210 s | 0.2866 | 60.5 Hz | 716.5 Hz | 1344.5 Hz |

These values show section-dependent expansion and contraction of the industrial spectrum. They do not establish a deterministic spectral mapping from the reference track.

## Reproduction warning

Lossy decoder implementations may differ slightly. The canonical evidence is the SHA-256 of each original MP3. Measurement tolerances should therefore be treated as descriptive rather than byte-level invariants.
