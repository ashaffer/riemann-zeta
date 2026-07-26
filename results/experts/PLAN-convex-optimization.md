# PLAN — Convex optimization (SDP / SOS / moment problems / duality)

*Independent consultant plan, prepared 2026-07-26 without reading other experts' PLAN files.
All repo numbers quoted below match `results/RESULTS.md`; all new numbers were measured
this session with the repo's own instruments (`src/spectral_margins.py` builder, spectral
Legendre basis) plus ~200 lines of scratch numpy/scipy. Every new eigenvalue computation
below was anchored to a repo EXPECTED value before use (L = 2.485, m = 24:
3.8688156e-10 against the documented 3.86882e-10; L = 1.75, m = 20: 3.17791e-5 against
the documented ladder).*

## 1. Reformulation.

Fix L > 0, a = L/4, and let Q_L, λ(L) be as in `THEOREMS.md`. Everything below rests on
one change of variables: Q_L is **linear in the autocorrelation**. With ψ_φ(u) = ∫φφ(·+u),

  Q_L(φ) = ⟨𝔴_L, ψ_φ⟩,

where 𝔴_L is the *truncated Weil distribution* on (−L/2, L/2): the even distribution whose
pairing with an even ψ ∈ C_c(−L/2, L/2) is (repo ledger normalization, `PROGRAM.md` §6,
x-space kernel of §2.14)

  ⟨𝔴_L, ψ⟩ = (ψ₀(¼) − log π)·ψ(0) + 2∫₀^{L/2}[ψ(0) − ψ(u)] w(u) du + 2ψ(0)∫_{L/2}^∞ w
             + 2∫_{−L/2}^{L/2} ψ(u) cosh(u/2) du  −  Σ_{n<e^{L/2}} 2Λ(n)n^{−1/2} ψ(log n),

w(u) = e^{−u/2}/(1−e^{−2u}). (The pole term is the cosh density because
h(±i/2) = ∫ψ(u)e^{±u/2}du for h = |φ̂|²; the prime term is a finite set of atoms at
±log n; truncation is exact on window-supported ψ.)

Two cones on the window (both classical; Carathéodory–Toeplitz in continuous time):

- **𝒦_L (Boas–Kac cone):** even positive-definite functions/distributions on ℝ *supported in*
  [−L/2, L/2], i.e. mixtures of autocorrelations ψ_φ, supp φ ⊂ [−a, a] (Boas–Kac 1945:
  every PD function supported in [−L/2, L/2] factors as one autocorrelation from [−a, a]).
- **𝒦*_L (Krein cone):** even distributions μ on (−L/2, L/2) whose Toeplitz kernel μ(x−y)
  is PSD on C_c^∞(−a, a). This is the dual cone of 𝒦_L, and 𝒦_L ⊊ 𝒦*_L|window: the gap is
  exactly *Krein-extendable* (PD on the interval; Krein 1940: always extendable to PD on ℝ)
  versus *extendable by zero* (Boas–Kac). Membership 𝔴_L ∈ 𝒦*_L is verbatim Q_L ⪰ 0.

Then:

- **Primal conic LP:** λ(L) = min{ ⟨𝔴_L, χ⟩ : χ ∈ 𝒦_L, χ(0) = 1 }. (Extreme points of the
  section are single autocorrelations; a linear objective attains its min there — this is
  why the sphere-minimization and the convex problem over PSD trace-one operators agree.)
- **Dual:** λ(L) = sup{ β : 𝔴_L − βδ₀ ∈ 𝒦*_L }. By Krein extension + Bochner(–Schwartz),
  𝔴_L − βδ₀ ∈ 𝒦*_L should be equivalent to the existence of a **positive even tempered
  measure σ on ℝ** ("dual witness") with

    ⟨𝔴_L − βδ₀, ψ⟩ = (1/2π)∫ ψ̂(t) dσ(t)  for all admissible ψ on the window.

  A witness is a **positive quadrature rule reproducing the truncated Weil data**. Under RH
  the explicit formula says σ₀ = Σ_γ δ_γ (ordinates with both signs; weight 2 per positive
  ordinate in the E(t)-parametrization below) is a witness at β = 0 *for every L
  simultaneously* — the zero measure itself is the universal dual optimal. Conversely,
  witness existence at β = 0 for all L is Weil positivity, i.e. RH.

So the program's three measured objects have exact convex-duality names: the **envelope**
is the value function of a conic LP; the **keyhole** is complementary slackness (at
β = λ(L), every witness is supported in the zero set of φ̂*, and the measured node set of
φ̂* is the zeros); **UPT** is the statement that the arithmetic trajectory L ↦ 𝔴_L stays in
the moving cone 𝒦*_L — a *positive-completion problem* (§2, Lemma CO-3). In the Galerkin
compression the frame matrices are E(t) = Re[v̂(t)v̂(t)^H], v̂_k(t) = 2a·n_k(−i)^k j_k(ta)
(spherical Bessel, orthonormal Legendre), the compression is a truncated matrix moment
problem (Curto–Fialkow), and the repo's LDL^T/interval-Cholesky certificates are exact
rational SOS certificates — proof objects in Lasserre–Parrilo's sense (Lasserre 2001;
Parrilo 2000, 2003; Nesterov 2000 for squared functional systems).

## 2. Lemma candidates

### Lemma CO-1 (Krein–Weil duality: dual witnesses are positive quadratures at the zeros)

**(a) Statement.** For every L > 0 and β ∈ ℝ: λ(L) ≥ β ⟺ there exists a positive even
tempered measure σ on ℝ, of at most (T log T)-growth, with
(1/2π)∫ψ̂ dσ = ⟨𝔴_L − βδ₀, ψ⟩ for all even ψ ∈ C_c^∞(−L/2, L/2). Moreover:
(i) the witness set Σ_L(β) is convex and weak-* closed, nonempty iff β ≤ λ(L), and its
extreme points can be taken discrete (canonical extensions: atoms at zeros of an entire
function of exponential type a from the associated de Branges chain; Krein–Nudelman 1977,
Akhiezer 1965 Addenda, de Branges 1968);
(ii) complementary slackness: at β = λ(L), every σ ∈ Σ_L(λ) is supported in
{t : φ̂*(t) = 0} for every minimizer φ*;
(iii) RH ⟺ Σ_L(0) ≠ ∅ for all L, with the universal witness σ₀ = Σ_γ δ_γ.
The finite-m Galerkin statement is a truncated matrix moment problem: Q_L(m) − βG is a
moment matrix for the family E(t), and flat extensions (Curto–Fialkow 1996) give finitely
atomic witnesses with ≤ rank atoms.

**(b) Proof strategy.** Direction "witness ⟹ PSD" is one line (evaluate on ψ_φ). For the
converse: mollify 𝔴_L − βδ₀ by a Fejér kernel (stays PD on a shrunken window), apply
Krein's interval-extension theorem for continuous PD functions, remove the mollification
by weak-* compactness with a uniform local mass bound (test against windowed Fejér
squares), then Bochner. The ε-loss of window is repaired using the repo's own **Glide
Theorem** (λ is continuous in L, `THEOREMS.md` Thm 1) — take L' ↑ L. Growth control of σ
from Lemma A(iv)'s two-sided log bound on the archimedean symbol. Extremal/discrete
witnesses via Krein–Nudelman's canonical-extension theory (Nevanlinna parametrization of
all extensions; the two "Friedrichs/Krein-corner" extensions are atomic).

**(c) Hardest missing step.** The distributional Krein extension with *atoms approaching
the window edge* (the newest prime sits at log n → L/2⁻): mollification is most lossy
exactly there, and the Glide modulus (log 1/h)^{−1/2} is weak. Secondary: certifying the
(T log T)-growth (Riemann–von Mangoldt density) of some witness, not just temperedness.

**(d) Difficulty.** Medium. Assembly of classical results (Krein 1940; Boas–Kac 1945;
Krein–Nudelman 1977; Gelfand–Vilenkin vol. 4; Sasvári 1994 for the extension-problem
literature) with one genuinely delicate boundary argument. Priority risk: this cone
picture may substantially overlap Suzuki's screw-function formulation (arXiv:2606.09096) —
diligence before any novelty claim.

**(e) Numerical stress test — EXECUTED (the charged dual-measure extraction).**
At L = 2.485, m = 24 orthonormal Legendre (λ = 3.8688156e-10, repo-anchored;
T*(L) = 2πe^{L/2} = 21.77, so exactly two zeros are sub-Nyquist):

- *Keyhole/slackness (nodes of φ̂\*)*: deep nodes measured at 14.1340, 21.0220, 25.0120,
  30.4680, 33.0920 against true 14.1347, 21.0220, 25.0109, 30.4249, 32.9351 — 3–4 decimal
  agreement at and below ~25, degrading above T*, and **no spurious node below 14** at
  relative depth < 0.05 (the hat-basis spurious nodes 7.640/13.655 of `results/RESULTS.md`
  are absent in the spectral basis at this L).
- *Direct witness*: R_N = Q − 2Σ_{k≤N}E(γ_k) over the first N true zeros stays PSD to
  float precision for N = 10, 20, 40, 60, 80 (λ_min(R_N) ≥ −1.04e-14, i.e. numerical
  zero at ‖Q‖ ≈ 7); the zero measure with weight exactly 2 per positive ordinate
  reproduces the Galerkin Weil matrix, remainder = positive tail (‖R_80‖_F = 4.16).
- *Blind extraction*: nonnegative least squares (Lawson–Hanson NNLS) of Q against 2,500
  frame matrices E(t) on the grid t ∈ [0, 50], step 0.02, **with no zero information
  supplied**, returns as its two leading in-band clusters: centroid **14.079, weight
  2.047** and centroid **20.556, weight 1.606** — the RH-predicted atoms (weight 2 at
  14.135; the 21.022 atom sits at the band edge T* = 21.77 and is pulled/split, weight
  deficit consistent with edge leakage into the 23.76 cluster). Total spurious weight
  below t = 12 is 0.106 (≈ 5% of one atom: clusters 0.051 at t≈2.6, 0.055 at t≈7.8).
  Above T* the atoms smear (super-resolution fails past Nyquist, as it must).
- *Slackness caveat, stated honestly*: at residual 7.14 (tail-dominated) the β = λ and
  β = 0 fits coincide; the complementary-slackness sum Σw|φ̂*(t)|² = 3.1e-2 is not
  resolved against λ = 3.9e-10 by a grid witness. The decisive slackness data is the
  node-zero coincidence above.
Proposed follow-ups: repeat blindly at L = 2.996, m = 32 (Prediction P1); push the R_N
test to mpmath (dps 30) to lower the PSD floor from −1e-14 toward −1e-25.

### Lemma CO-2 (Certificate Depth Law: entry precision = envelope, sharp constant ‖v‖₁²)

**(a) Statement.** Let Q be the Galerkin matrix at (L, m), λ = λ_min(Q) with spectral gap
g = λ₂ − λ₁ ≫ λ, v the unit minimizer. Define δ*(Q) = max{δ : every symmetric M with
|M − Q|_∞ ≤ δ entrywise is PSD}. Then

  δ*(Q) = λ / ‖v‖₁² + O(λ²/g)   (‖v‖₁ the vector 1-norm; λ/m ≤ δ* ≤ λ always),

and consequently any certificate in the repo's Theorem-2 format (kernel-verified
positivity of an entrywise δ-ball around a published rational matrix, `lean/weilcert`)
exists iff δ < δ*, hence requires entry precision

  digits(L) ≈ A(L) + log₁₀‖v‖₁²,  A(L) = [1.755·e^{L/2}(L/2+4) − 10.2]/ln 10,

conditional on the measured envelope (unconditional version with log₁₀(1/λ(L,m)) in place
of A). Via N(T*) = (T*/2π)(ln(T*/2π) − 1) + 7/8 the marginal cost is
1.755·(ln x + 5)/(ln x)·(1/ln 10) digits per resolved zero (x = T*/2π), → **0.762 digits
per zero** asymptotically; total certificate bit-size Θ(m²·digits(L)). Companion negative
part: no *density-built* preconditioner bounds the relative certificate — see (e).

**(b) Proof strategy.** Exact extremal perturbation Δ = −δ·sign(vv^T) plus first-order
eigenvalue perturbation with gap control gives the two-sided estimate for δ*; the digit
consequence is arithmetic. For "‖v‖₁² = O(1) uniformly in (L, m)" (needed so the constant
never degrades to the trivial λ/m): derive minimizer flatness from the repo's Lemma B/C
non-concentration machinery (log-weighted energy bounds).

**(c) Hardest missing step.** Unconditional lower bounds on 1/λ(L) (that *is* the envelope
derivation — M3); and the uniform ‖v‖₁² = O(1) bound. The rest is elementary.

**(d) Difficulty.** Core claim: easy (worth writing down because it is *sharp* and it
retargets Track A/B budgeting). Flatness bound: medium. Envelope input: conditional.

**(e) Numerical stress test — EXECUTED.**
- Adversarial flip at L = 2.485, m = 24: bisected δ* = 1.2695e-10 against predicted
  λ/‖v‖₁² = 1.2730e-10 — **ratio 0.997**. (‖v‖₁² = 3.039; the naive Weyl bound λ/m =
  1.6e-11 is 8× pessimistic.)
- Cross-window: (L, m, λ, ‖v‖₁², λ/‖v‖₁²) = (1.75, 20, 3.1779e-5, 2.352, 1.351e-5);
  (2.485, 24, 3.8688e-10, 3.039, 1.273e-10); (2.996, 32, 6.4501e-15, 3.511, 1.837e-15).
  Measured digits(L) = 4.87 / 9.90 / 14.74 against A(L) + log₁₀‖v‖₁² = 4.86 / 9.90 / 14.86:
  the depth law tracks the envelope to ≤ 0.13 digits across ten orders. ‖v‖₁² is drifting
  slowly (2.35 → 3.51), not growing with m.
- *Preconditioning negative result*: against the smooth Riemann–von Mangoldt staircase
  frame F_s (80 model ordinates, `model_zeros` construction), the relative margin at
  L = 2.485 is λ_min(Q, F_s) = **2.646e-5**, not O(1) — while the control against the true-
  zero frame gives λ_min(Q, F_true) = 1.0000. Mechanism: the Q-minimizer nearly attains it
  (ratio 2.652e-5) because |φ̂*(γ₁^smooth = 14.521)|² = 7.2e-6 — the two forms' keyholes
  sit at different points. **The envelope divides out of the value, not of the form**
  (sharpening §2.17: value-law is density-functional, form-equivalence is arithmetic):
  any bounded-size relative/denominator certificate family must encode the true zeros to
  sub-mean-spacing accuracy. This numerically disfavors the optimistic Track B reading
  (bounded per-window certificates after a density-only normalization).

### Lemma CO-3 (UPT as a positive completion problem: the arithmetic point rides the cone boundary)

**(a) Statement.** For a symmetric direction M, the set {x : λ_min(Q_L + (x−x₀)M) ≥ 0} is
a closed interval (concavity of λ_min over affine families). For the canonical directions
of the Weil data — prime-power atom weights w_n (arithmetic value w_n* = −2Λ(n)n^{−1/2})
and pole coefficient ρ (arithmetic value 1) — define the feasibility intervals I_n(L),
I_pole(L) (Galerkin versions are outer approximations, shrinking in m). Then:
(i) RH ⟺ for every L, the arithmetic point lies in every interval (equivalently: the
completion of window-L data across the next threshold by the *arithmetic* atom weight
stays in the Krein cone — the Nevanlinna/Schur-parameter step of the Krein extension
theory stays contractive; Krein–Nudelman; Arov–Dym);
(ii) near-endpoint distance = envelope transfer: dist(arith, ∂I) = λ(L)/|⟨M⟩_{φ*}| + O(λ²),
where ⟨M⟩_{φ*} is the minimizer expectation — for prime directions this is exactly
ψ_{φ*}(log n), i.e. **the repo's §2.11 mechanism law is the envelope theorem (Danskin) of
this conic program**, and the repo's Lemma E (edge suppression of ψ near thresholds)
predicts wide tolerance for newly-entered primes, collapsing as they move interior;
(iii) hence every structural constant of the explicit formula is pinned with tolerance → 0
on the envelope schedule: the arithmetic trajectory rides the boundary of the positivity
cone (the convex-geometric form of §2.12's safety-factor → 1).

**(b) Proof strategy.** Interval structure and (ii): elementary (concavity + Danskin +
gap). Equivalence (i): exhaustion over L, Glide continuity, and Lemma CO-1's witness
language for the completion reading. The *content* — lower bounds on endpoint distances
uniform in the threshold index — is the renormalized transfer lemma itself; the lemma's
value is that it isolates scalar trajectories w_n^±(L), ρ^±(L) that are **certifiable at
every finite L by the repo's interval-Cholesky machinery** (each endpoint is itself an
eigenvalue problem): a new certified "rigidity ledger" for Track A.

**(c) Hardest missing step.** Any unconditional lower bound on dist(arith, ∂I) that beats
recomputing λ(L) — i.e. an inequality flowing from the arithmetic side (prime sums) to the
interval geometry rather than through the eigenvalue. This is where the actual RH
difficulty now sits, undisguised.

**(d) Difficulty.** Statement + (ii): easy-medium, publishable as a precise reframing with
measured constants. (i)-with-rates: RH-hard, and says so.

**(e) Numerical stress test — EXECUTED** (L = 2.485, m = 24; outer/Galerkin intervals):
- Minimizer expectations: ψ_{φ*}(log 2) = +0.025236; ψ_{φ*}(log 3) = +3.05e-6 (the prime 3
  entered at L = 2.197 and is still edge-suppressed — Lemma E in action); pole quadratic
  ⟨P⟩_{φ*} = +1.345091.
- Prime-2 weight: I₂ = [−0.980258159, −0.980257475] around w₂* = −0.980258143: gaps
  −1.532e-8 / +6.685e-7; first-order prediction λ/|ψ*(log 2)| = 1.533e-8 matches the near
  gap to 0.1%. **The Connes–Consani 10⁻³ arithmetic rigidity is refined, in the weight
  coordinate at L = 2.485, to 1.5×10⁻⁸** (true rigidity is tighter: outer bound).
- Prime-3 weight: I₃ = [−1.268690, −1.267964] around w₃* = −1.268568: gaps −1.214e-4 /
  +6.039e-4, against first-order 1.268e-4 (4%; second-order visible). Newly-entered prime
  ⟹ 10⁴× wider tolerance than prime 2, exactly as (ii)+Lemma E predict.
- Pole coefficient: I_pole = [1 − 2.876e-10, 1 + 6.045e-6]; the lower gap equals
  λ/⟨P⟩_{φ*} = 2.876e-10 to all printed digits. **Window positivity at L = 2.485 already
  pins the residue of ζ's pole from below to 3 parts in 10¹⁰.** The upper endpoint is an
  odd-parity event — see CO-4, where it is reproduced independently to 7 digits.
Follow-up: Prediction P3; certified endpoints via `certified_spectral` (proposed).

### Lemma CO-4 (the pole is parity-split rank-(1,1); the odd sector is one scalar inequality)

**(a) Statement.** In any parity-respecting basis the pole matrix is exactly
2cc^T ⊕ (−2ss^T) on the even/odd blocks (c, s = moments of cosh(x/2), sinh(x/2)): the pole
*helps* the even sector by a PSD rank-one and *drains* the odd sector by a NSD rank-one.
Writing Q^odd = T^odd − 2ss^T (T^odd = arch − primes, odd block, T^odd ≻ 0 in the measured
range), Sherman–Morrison gives: Q^odd ⪰ 0 ⟺ θ(L) := 2s^T(T^odd)^{−1}s ≤ 1. Hence
(i) the full margin is carried by the even block iff λ^even ≤ λ^odd (measured true at all
three windows), so certificates can halve dimension;
(ii) odd-sector Weil positivity for all L reduces to the one-parameter scalar family
θ(L) ≤ 1 — an RH-necessary inequality: a certified θ(L₀) > 1 at any L₀ would *disprove*
RH (a new one-scalar-per-L disproof channel for Track D);
(iii) the upper endpoint of CO-3's pole interval is ρ⁺ = 1/θ(L) exactly.

**(b) Proof strategy.** The parity split is a two-line computation (v_± = c ± s). The
Sherman–Morrison equivalence is standard rank-one theory. The analytic work is the
asymptotics of θ(L) = 1 − ε(L): express θ under RH via the zero-frame
(θ < 1 automatic), and unconditionally as a quotient of explicit quadratic forms in the
sinh vector against the arch-minus-primes resolvent — a concrete special-function target,
far more tractable-looking than an operator inequality.

**(c) Hardest missing step.** θ(L) < 1 for all L unconditionally is (at least) odd-sector
Weil positivity — RH-adjacent. The honest finite goal is a certified θ-ladder and its
measured law ε(L), which is new phenomenology either way.

**(d) Difficulty.** Algebra: trivial (verified). θ-ladder instrument: easy. ε(L)
asymptotics: medium-hard.

**(e) Numerical stress test — EXECUTED** (L = 2.485, m = 24 unless noted):
- Rank-(1,1) split exact: pole even-block eigenvalues [−5.8e-17, +2.566] and odd-block
  [−8.148e-2, +9.9e-17]; ‖P^odd + 2ss^T‖_F = 1.6e-16.
- θ = 0.9999939548; 1 − θ = 6.045e-6 = ρ⁺ − 1 of CO-3 (independent computations agree to
  7 digits). Odd cascade of the drain: λ^odd(T) = 1.100e-3 → λ^odd(Q) = 1.494e-7.
- Parity margins (even | odd): L = 1.75, m = 20: 3.178e-5 | 4.010e-3; L = 2.485, m = 24:
  3.869e-10 | 1.494e-7; L = 2.996, m = 32: 6.450e-15 | 4.893e-12. The envelope is the
  even sector; the odd margin runs 10²–10³ above (roughly the envelope displaced by
  ΔL ≈ 0.4). Without the pole the even block is *hugely* negative at L = 2.485 (−2.519):
  the pole's even rank-one does O(1) rescue work while its odd rank-one operates at
  6e-6 slack from criticality — zero-slack in yet another coordinate.

## 3. Predictions

**P1 (dual quadrature at the next window; blind).** Repeating the NNLS extraction at
L = 2.996, m = 32, grid step 0.02 (T* = 28.11, three sub-Nyquist zeros): leading clusters
with centroids within 0.05 of 14.135, within 0.15 of 21.022, within 0.6 of 25.011;
weights 2.0 ± 0.15, 2.0 ± 0.4, and in [1, 3] respectively; total weight below t = 12
under 0.15. Nodes of φ̂* within 5e-3 of the first three zeros. Falsified by any missing/
misplaced (≥ 0.5) cluster or ≥ 0.5 spurious low-t weight.

**P2 (certificate depth, both directions, against the repo's own Lean format).**
(a) The `lean/weilcert` window (L = 497/200, m = 12, λ(m=12) = 7.5308e-8): the entrywise
ball radius can be widened from the published 1e-20 to δ* ∈ [1.5e-8, 5e-8] (prediction:
‖v‖₁²(m=12) ∈ [1.5, 5]) — about **12 orders of magnitude of unused headroom** — and the
same integer-congruence machinery still certifies it.
(b) The identical format at (L = 711/200, m = 40, certified λ ∈ (1.79970, 1.79972291]e-20)
**fails at δ = 1e-20**: predicted δ* = λ/‖v‖₁² = (4.6 ± 0.8)e-21 < 1e-20 (prediction
‖v‖₁²(L=3.555, m=40) = 3.9 ± 0.6, extrapolating the measured 2.35 → 3.04 → 3.51 drift).
Checkable in minutes: the T4 sign-matrix M = Q − 1e-20·sign(vv^T) should have λ_min < 0.
If instead ‖v‖₁² < 1.8 the format survives and P2(b) is falsified.

**P3 (interval pinch trajectory).** At L = 2.996, m = 32: the prime-3 near-endpoint gap
becomes λ/|ψ_{φ*}(log 3)| with |ψ_{φ*}(log 3)| ∈ [0.01, 0.12] (prime 3 now interior), i.e.
gap ∈ [5e-14, 6e-13] — a collapse by 8–9 orders from the measured 1.2e-4 at L = 2.485;
the pole lower gap = λ^even/⟨P⟩ ∈ [3e-15, 5e-15]; and 1 − θ(2.996) ∈ [3e-10, 3e-8].
Falsified if the gaps miss these windows by more than one order.

## 4. Interfaces

**Needs from harmonic analysis (extremal problems).** (i) The M3 target in dual clothing:
asymptotics of the Krein/de Branges chain for the archimedean-plus-pole symbol
(Landau–Widom 1980 / Slepian plunge theory) to *derive* b ≈ 1.755 and the +4.0 offset —
the canonical extremal witnesses' atoms are zeros of type-a de Branges functions, and I
supply their measured finite-L shadows. (ii) Beurling–Selberg technology (Vaaler 1985;
Carneiro–Littmann; Carneiro–Chandee–Milinovich's Guinand–Weil extremal functions) to
*construct* explicit positive witnesses σ_L with certified deficiency β > 0: an analytic
lower-bound route to λ(L) that would compete with Galerkin from the dual side.
**Composition to run:** "Krein-chain asymptotics for the Weil symbol" (HA × CO).

**Needs from computer science (certificate size).** Rational rounding/compression of
certificates (Peyrl–Parrilo 2008; LLL for simultaneous approximation) applied to the
depth law's budget A(L); and a proof-complexity formalization in which CO-2 is a lower
bound. Offer in return: **dual-certificate compression** — a witness (quadrature) is
O(N(T*)) numbers versus O(m²) for the primal LDL^T at the same window, and CO-1(e) shows
the atoms are recoverable blind. **Composition:** "quadrature witnesses as proof objects"
(CS × CO), feeding Track B's mining with the Curto–Fialkow flat-extension rank as the
per-window certificate rank (which should increment exactly on the repo's measured Weyl
staircase).

**Needs from number theory.** (i) Whether the residue pinch (3e-10 at L = 2.485, CO-3) and
the CC-rigidity refinement have known explicit-formula proofs. (ii) Beurling generalized
prime systems (Diamond–Montgomery–Vorhauer): systems matching N(T)-density but violating
RH-analogues would calibrate exactly how much of the interval ledger is density versus
arithmetic — my form-level preconditioning failure (λ_rel = 2.6e-5, CO-2e) is the first
data point that the *form* needs arithmetic even where the *value* does not.
**Composition:** "Beurling stress test of the rigidity ledger" (NT × CO), also a
falsification channel: a Beurling system passing all finite intervals would expose the
lemma family's blind spot.

## 5. Honest assessment

The strongest objection to this program is that its duality is *exact*, and exactness cuts
both ways: every reformulation above (witness existence, interval membership, θ ≤ 1) is RH
re-encoded without loss, so no relaxation gap is being exploited anywhere. Convex
optimization earns its keep when a relaxation is tight-but-easier; here the "relaxation"
is the theorem. Concretely: (1) the quantitative content has been relocated into
asymptotics of Krein chains for a nonclassical symbol — the same wall CCM's Sonin-space
program already faces, in different notation; I have moved the wall's coordinates, not its
thickness. (2) The measured boundary-riding (safety factor → 1, intervals pinching on the
envelope schedule, θ within 6e-6 of criticality) means the feasibility problems become
ill-conditioned exactly as fast as the margins decay: the convex geometry *measures* the
ride with new precision but supplies no mechanism for *why* arithmetic tracks the
boundary — which is the entire question. (3) My own depth law is bad news for the track I
was recruited to serve: raw certificate size grows ~0.76 digits per resolved zero, so
Track B's hoped-for bounded per-window certificates do not exist in the naive format, and
the natural repair (divide out the envelope by a density-built preconditioner) is killed
at form level by the measured λ_rel = 2.6e-5 — bounded relative certificates would need
the true zeros to sub-spacing accuracy, a circularity of the highest order. (4) The
witness extractions inherit the keyhole caveat (`PROGRAM.md` §2.13, Groskin
arXiv:2605.20224): their success is partially forced by the explicit-formula identity;
the blind NNLS weights (2.047 against the predicted 2) are genuine out-of-sample structure
but of validated-pipeline kind, not discovery. If the collaboration round cannot convert
the Krein-chain/witness picture into one derivable asymptotic — b and the +4.0 offset —
then this plan's lasting output is instrumentation: sharp certificate budgeting (CO-2),
a certified rigidity ledger and a residue pinch (CO-3), a halved certificate dimension
and a new scalar disproof channel (CO-4). Excellent instrumentation, on the measured side
of the wall.
