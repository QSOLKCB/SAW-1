# SAW-1 Formalization

## Spooky Action at Work

**Author:** Trent Slade · QSOL-IMC  
**Version:** 1.0.0 · **Date:** 18 August 2026

## 1. Claim

SAW-1 documents an artistic production chain and a later-discovered semantic correspondence. It does **not** claim prophecy, retrocausality, paranormal transfer, physical entanglement between artifacts, or experimental confirmation of a second time dimension.

Let:

\[
Z=\text{private ETQ-informed sonification lab},\quad
R=\text{reference track},\quad
M=\textit{Industrial Metal God},
\]

\[
P=\text{Pettini's proposed }(3,2)\text{-dimensional model},\quad
V=\text{Hossenfelder's explanatory video}.
\]

The evidence-bounded chain is:

\[
Z\xrightarrow{\rho}B
\xrightarrow{\mathcal G_1(\xi_1)}R
\xrightarrow{\mathcal G_2(\Pi,L,\xi_2)}M
\xrightarrow{\mathcal O(P,V)}C.
\]

Here \(\rho\) is the private creative receiver, \(B\) its settings/brief/reference design, \(\mathcal G_1\) and \(\mathcal G_2\) are generative processes, and \(C\) is the documented correspondence. Both supplied MP3s identify themselves as Suno-created, so neither is claimed to be a bitwise deterministic render of the private lab.

## 2. Chronology

\[
t_P=\text{2026-06-25},\quad
t_R=\text{2026-07-27T09:24:54.574Z},
\]

\[
t_M=\text{2026-07-27T10:15:19Z},\quad
t_C=\text{2026-08-18}.
\]

Therefore:

\[
t_P<t_R<t_M<t_C.
\]

The reference-to-song interval is:

\[
\Delta t_{R\to M}=3024.426\ \mathrm{s}
=50\ \mathrm{min}\ 24.426\ \mathrm{s}.
\]

The paper predates the music. The formalized event is the **later recognition** of the match.

## 3. ETQ-101 source layer

The private source defines:

\[
N=101=2+33\times3,
\]

with two selected singlets, thirty-three three-state blocks, and a broader 240-root E8 visual/projection source.

The three-state stencil and phase constants are:

\[
S=(1,-2,1),\qquad
\Theta=\frac{\pi}{2},\qquad
\delta=\frac{2\pi}{303}.
\]

For graph degree \(d_j\), the exact potential is:

\[
V_j=\frac{101d_j-3374}{2181}.
\]

For non-singlet basis index \(j\ge2\):

\[
m_j=\left\lfloor\frac{j-2}{3}\right\rfloor,
\qquad q_j=(j-2)\bmod3,
\]

\[
\operatorname{MIDI}(j)=14+33q_j+m_j.
\]

The singlets use MIDI identifiers 13 and 113. In the receiver implementation their missing qutrit and orbit values fall back to zero. Define the total receiver indices:

\[
\bar q_j=
\begin{cases}
0,&j\in\{0,1\},\\
q_j,&j\ge2,
\end{cases}
\qquad
\bar m_j=
\begin{cases}
0,&j\in\{0,1\},\\
m_j,&j\ge2.
\end{cases}
\]

Thus the two singlets use \(S_{\bar q_j}=S_0=1\) and orbit phase \(\bar m_j=0\). These definitions make the event and frequency laws total over all 101 basis indices.

These equations define symbolic structure only. They do not establish medical, therapeutic, or physical claims for the receiver's creative terminology.

## 4. Matching `CHAKRA-ASCENT-101` preset

The canonical source preset matching the supplied reference name has:

\[
\begin{aligned}
\text{seed}&=\texttt{CHAKRA-ASCENT-101},\\
\text{ETQ mode}&=101,\\
A&=432\ \mathrm{Hz},\\
r&=1.01\ \mathrm{s}^{-1},\\
b&=0.72,\quad s=0.48,\quad \sigma=0.32,\quad w=0.66,\\
T&=90\ \mathrm{s},\quad g=0.
\end{aligned}
\]

The seven authored receiver frequencies are:

\[
F=(396,417,528,639,741,852,963)\ \mathrm{Hz},
\]

with level \(a_k=0.86\) for each voice.

No exported project JSON accompanied the evidence files, so these are the **canonical matching preset values**, not proof that every control remained unchanged.

## 5. Event and frequency laws

The event and basis indices are:

\[
e(t)=\lfloor rt\rfloor,
\qquad
j(t)=e(t)\bmod101.
\]

For every event, including the singlets:

\[
\Phi_j=\frac{2\pi\bar q_j}{3}-\Theta S_{\bar q_j}.
\]

The general ETQ-303 receiver adds an external fibre term \(f\delta\), but the matching preset uses ETQ-101, so \(f=0\).

The receiver's cents displacement is:

\[
c_j=11V_j+2.2S_{\bar q_j}+5.5G_j.
\]

Because the matching preset disables the golden veil:

\[
G_j=0,
\qquad
\boxed{c_j=11V_j+2.2S_{\bar q_j}}.
\]

In particular, for the singlets:

\[
c_0=11V_0+2.2,
\qquad
c_1=11V_1+2.2.
\]

The receiver's octave-folding operator is the deterministic map

\[
\operatorname{fold}:\mathbb R_{>0}\rightarrow[80,1400]\ \mathrm{Hz}
\]

defined by

\[
\operatorname{fold}(f)=
\begin{cases}
2^{n(f)}f,&0<f<80,\\
f,&80\le f\le1400,\\
2^{-m(f)}f,&f>1400,
\end{cases}
\]

where

\[
n(f)=\min\{n\in\mathbb N_0:2^nf\ge80\},
\qquad
m(f)=\min\{m\in\mathbb N_0:2^{-m}f\le1400\}.
\]

This is the mathematical form of the receiver implementation, which repeatedly doubles frequencies below 80 Hz and halves frequencies above 1400 Hz. Every authored preset frequency already lies in the pass band, so

\[
\operatorname{fold}(F_k)=F_k
\qquad(k=0,\ldots,6).
\]

Voice \(k\) therefore receives the total frequency law:

\[
f_k(t)=\operatorname{fold}(F_k)2^{c_{j(t)}/1200}
=F_k2^{c_{j(t)}/1200},
\qquad j(t)\in\{0,\ldots,100\}.
\]

## 6. Ascent envelope and receiver field

For voice \(k\in\{0,\ldots,6\}\):

\[
J(t)=\frac{7t}{T},
\qquad
D_k(t)=\left|J(t)-\left(k+\frac12\right)\right|,
\]

\[
Q_k(t)=1-\operatorname{smoothstep}(0.35,1.25,D_k(t)),
\]

\[
E_k(t)=a_k\max(0.06+0.12a_k,Q_k(t)).
\]

A principal voice has the weighted structure:

\[
X_k(t)=0.8\sin\phi_k(t)
+0.16\sigma\sin\psi_k(t)
+0.055\sigma\sin(2.003\phi_k(t)+\bar m_j\delta).
\]

Ignoring stereo gains, the field is:

\[
Y(t)=\sum_{k=0}^{6}E_k(t)H(t)X_k(t)+A_0(t)+N(t)+V_0(t),
\]

where \(H\) is a slow breath envelope, \(A_0\) the anchor drone, \(N\) seeded filtered noise, and \(V_0\) the Vortexmouth contribution.

## 7. Generative boundary

The supplied durations are:

\[
\operatorname{duration}(R)=90.024\ \mathrm{s},
\qquad
\operatorname{duration}(M)=235.728\ \mathrm{s}.
\]

The final song is modeled conservatively as:

\[
M=\mathcal G_2(R,\Pi,L;\xi_2),
\]

not as a known deterministic waveform transform.

The defensible artistic correspondences are:

\[
\begin{aligned}
\text{continuous drone}&\rightsquigarrow\text{bass/guitar pedal law},\\
\text{metallic resonance}&\rightsquigarrow\text{factory percussion and distortion},\\
\text{rising upper spectrum}&\rightsquigarrow\text{crystalline metallic overtones},\\
\text{ETQ events}&\rightsquigarrow\text{machine-like sectional articulation}.
\end{aligned}
\]

The symbol \(\rightsquigarrow\) denotes artistic interpretation, not waveform identity.

## 8. Measured reference behaviour

For a two-second Hann window and power spectrum \(P_t(f)\), define:

\[
\mu_f(t)=\frac{\sum_f fP_t(f)}{\sum_fP_t(f)}.
\]

Measured reference values are:

| Centre | Dominant bin | Power centroid | 85% roll-off |
|---:|---:|---:|---:|
| 15 s | 481.5 Hz | 448.4 Hz | 482.0 Hz |
| 45 s | 481.5 Hz | 475.8 Hz | 482.0 Hz |
| 75 s | 481.5 Hz | 618.6 Hz | 853.0 Hz |

Thus:

\[
\mu_f(75)-\mu_f(15)\approx170.2\ \mathrm{Hz}>0.
\]

The stable dominant component plus expanding upper spectrum matches the described drone-and-resonance structure. These measurements apply to the generated MP3, not a private direct PCM render.

## 9. The exact \((3,2)\) correspondence

Let the lyric feature be:

\[
\lambda=\text{“Three beats to two”}.
\]

Define its ordered-pair parser:

\[
\nu(\lambda)=(3,2).
\]

Pettini's proposed spacetime has signature:

\[
\operatorname{sig}(P)=(3,2).
\]

Therefore:

\[
\boxed{\nu(\lambda)=\operatorname{sig}(P)=(3,2)}.
\]

This is the single exact correspondence. Other lyric mappings are analogies:

| Lyric | Physics-side reading | Class |
|---|---|---|
| His bassline is law | geometry constrains dynamics within the adopted ansatz | analogy |
| Three beats to two | three space dimensions, two time dimensions | **exact** |
| The pattern snaps and locks | deterministic collapse at fixed contextual microstate | analogy |
| He built the whole map | enlarged five-dimensional spacetime | analogy |
| One low note and the universe clicks | equal-ordinary-time projected reach | analogy |

## 10. Semantic-collapse joke

The lyric's available readings may be written metaphorically as:

\[
|\Psi_L\rangle
=\alpha|\text{industrial polyrhythm}\rangle
+\beta|\text{dimensional signature}\rangle.
\]

The later comparison acts as an interpretive operator:

\[
\widehat{\mathcal O}_{P,V}|\Psi_L\rangle
\longrightarrow|\text{Spooky Action at Work}\rangle.
\]

This is a joke in semantic feature space, not a physical quantum state.

## 11. Evidential result

Let:

\[
H_0=\text{post hoc recognition without an established causal channel},
\]

\[
H_1=\text{causal foreknowledge or retrocausal transfer}.
\]

The record \(E\) establishes the chronology and the exact ordered-pair equality. It is compatible with \(H_0\), but the record does not establish cognitive independence: the paper predates the music, and the available evidence cannot exclude unrecorded ordinary prior exposure. Nor does the record provide evidence sufficient to establish \(H_1\).

Formally:

\[
\operatorname{Consistent}(E,H_0)=\mathrm{true},
\qquad
E\not\Rightarrow H_0,
\qquad
E\not\Rightarrow H_1.
\]

The bounded evidential conclusion is therefore:

\[
\boxed{
C=\text{documented production chronology}
+\text{delayed observation}
+\text{an unusually precise }(3,2)\text{ match}
}.
\]

No probability of coincidence or causal independence is assigned.

## 12. Proposition SAW-1

If a lyric contains “Three beats to two,” parsed as the ordered musical relation \((3,2)\), and a separately authored physical proposal has dimensional signature \((3,2)\), then the two semantic objects share the same ordered pair.

### Proof

\[
\text{three}\mapsto3,
\qquad
\text{two}\mapsto2,
\]

so:

\[
\nu(\text{“Three beats to two”})=(3,2).
\]

By definition:

\[
\operatorname{sig}(P)=(3,2).
\]

Therefore:

\[
\nu(\lambda)=\operatorname{sig}(P).
\qquad\square
\]

The formal result is equality of the ordered pair across two semantic domains. It does not, by itself, establish how the lyric author did or did not encounter the physics proposal.

\[
\boxed{\text{His bassline is law.}}
\]
