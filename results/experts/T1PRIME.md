# T1′ — The Hard Horizon Theorem (anchored Jensen bound at e²T*)

Paper-grade write-up of the panel's #1 target, corrected form (SYNTHESIS errata;
the original T1(i) at eT* is on the kill list — see §1.4). Author seat: harmonic
analysis. Date: 2026-07-26. Status: **complete proof at referee level for
Theorem 1 and Corollary 2; Corollary 1 (ζ) complete modulo two classical
citations with explicit constants (NT Lemma R1), which are quoted verbatim.**
Every numbered estimate is verified numerically in Appendix V (script + output).
Lean decomposition and mathlib gap-map in §6, against the repo's local mathlib
snapshot `520045ab14` (2026-07-23, `lean/glide/lake-manifest.json`).

---

## 0. The result in one box

Let a > 0, I = [−a, a], and let F = φ̂ be the Fourier–Laplace transform of a
unit-norm φ ∈ L²(I). Let Λ = {±t_k} be a symmetric multiset of frequencies
whose counting function is at most R below the Riemann–von Mangoldt staircase
N̂(T) = (T/2π)ln(T/2πe) + 7/8. **If F vanishes on Λ up to height T̃, and F is
anchored (Hypothesis A: |F(x₀)| ≥ e^{−κa} at some |x₀| ≤ 2π), then**

  ln(T̃/2π) ≤ 2a + 2 + ε*,   ε* = [(κ + 4 + 2/π)a + ½ln(2a) + 2R(2a+1)] / (2(e^{2a+2} − R)).

In the program's units (T* = 2πe^{2a} the Nyquist-crossing height): **an
anchored test function can dodge the staircase at most to e²T*·e^{ε*}, and
ε* is exponentially small in the support.** For the true zeta ordinates the
same bound holds **unconditionally** (no RH) with R given by Trudgian's
explicit S(T) bound (Corollary 1). Beyond the vanishing horizon the function
has almost no zeros left anywhere — a quantitative zero desert (Corollary 2).

The companion (variational) horizon at e·T* — where the zero-count budget
D(T) = (a/π)T − N̂(T) crosses zero (D(eT*) = −7/8 exactly; Lemma 0) and where
the measured single-zero worth support ends — is NOT claimed as a hard
horizon; a nonzero F vanishing on any finite head always exists (§1.4). The
two-horizon structure was confirmed against eleven measured stopping heights
in results/agent-deep-windows.md: all in T_s/T* ∈ [3.14, 3.41] ⊂ (e, e²) (§5).

Notation. τ := ln(T̃/2π); T* := 2πe^{2a}; N̂(T) := (T/2π)ln(T/2πe) + 7/8;
N_Λ(T) := #{k : t_k ≤ T} counted with multiplicity; all logs natural.

---

## 1. Setting, hypotheses, statements

### 1.1 Standing assumptions

(S1) a > 0; φ ∈ L²(ℝ) with supp φ ⊆ [−a, a] and ‖φ‖₂ = 1;
   F(z) := ∫_{−a}^{a} φ(x) e^{−izx} dx.

(S2) Λ = {±t_k}_{k≥1} a symmetric multiset, 2π < t_1 ≤ t_2 ≤ …, with counting
   function N_Λ (multiplicity counted), satisfying the one-sided rigidity

     N_Λ(T) ≥ N̂(T) − R  for all T ∈ [2πe, T̃],   with 0 ≤ R ≤ e^{2a+1}.

(S3) [vanishing] For every k with t_k ≤ T̃: F vanishes at +t_k and at −t_k,
   each to order ≥ the multiplicity of t_k in Λ.

**Hypothesis A (anchor).** There exist x₀ ∈ ℝ and κ ≥ 0 with

  |x₀| ≤ 2π  and  |F(x₀)| ≥ e^{−κa}.

Remarks on Hypothesis A. (i) It is not removable: without a condition of this
kind no hard horizon exists at any height (§1.4, construction; its normalized
version has |F| = e^{−huge} throughout [−2π, 2π] because its L²-mass sits
above T̃). (ii) It is verified by design, with explicit κ, for every
test-function competitor used in the upper-bound constructions of the
envelope program (H3/T5: those transforms are Θ(1) at low frequency before
normalization). (iii) For actual near-minimizers of the frame form it is a
measured-but-unproved property; its proof is the lattice-adapted Turán wall
(§4, Gap 1).

### 1.2 Main theorem

**Theorem 1 (hard horizon at e²T*).** Assume (S1), (S2), (S3) and
Hypothesis A. Then

  τ = ln(T̃/2π) ≤ 2a + 2 + ε*,
  ε* := max( 0, [B + 2R(2a+1)] / (2(e^{2a+2} − R)) ),
  B := (κ + 4 + 2/π)·a + ½ln(2a).

Equivalently T̃ ≤ e^{2+ε*}·T*. (Numerically: with (R, κ) = (½, 1) —
staircase rigidity, unit anchor — ε* = 0.124, 0.117, 0.106, 0.083, 0.044,
0.014 at a = 0.4375, 0.621, 0.749, 1, 1.5, 2.25; Appendix V5.)

**Lemma 0 (count horizon; calculus identity, for the record).** With
D(T) := (a/π)T − N̂(T): D′(T) = (1/2π)ln(T*/T), so D increases on (0, T*],
decreases after, and D(eT*) = −7/8 exactly; the unique positive zero of D is
at eT*(1 − θ) with 0 < θ < 7π/(4a·eT*)·(1/2π)⁻¹-scale, i.e. eT*(1 − O(e^{−2a})).
[Verified V6. This is the height at which the vanishing budget is exhausted
on AVERAGE; it bounds where dodging is variationally worthwhile, not where it
is possible.]

### 1.3 Corollaries

**Corollary 1 (true zeta ordinates; unconditional).** Let a ≥ 7/16. Let Λ_ζ
be the multiset {±γ : ζ(β + iγ) = 0, γ > 0, β ∈ (0,1)}, each ordinate with
the multiplicity of the corresponding zero. Assume (S1), Hypothesis A, and
that F vanishes at ±γ to order ≥ mult(γ) for every ordinate γ ≤ T̃. Then

  ln(T̃/2π) ≤ 2a + 2 + ε*_ζ,  ε*_ζ := [B + 2·D₀(2πe^{2a+3})·(2a+1)] / (2(e^{2a+2} − D₀(2πe^{2a+3}))),

with D₀(T) := 0.112 ln T + 0.278 ln ln T + 2.517 (NT Lemma R1; Trudgian 2014
+ the theta-expansion remainder). No zero-location hypothesis is used: R1
counts all nontrivial zeros, on or off the line. Numerically ε*_ζ = 0.57,
0.46, 0.39, 0.28, 0.14, 0.045 at a = 0.4375 … 2.25: **the hard cap for ζ is
≤ 13.1·T* at L = 1.75, tightening to ≤ 7.7·T* at L = 9** (Appendix V5).

**Corollary 2 (zero desert).** Assume the hypotheses of Theorem 1 with
τ = 2a + 1 + s, s ∈ (0, 1]. For ρ′ ≥ τ let ρ = ρ(ρ′) be any radius in
[2πe^{ρ′} + 2π, 2πe^{ρ′} + 2π + 1] such that G(z) = F(x₀ + z) has no zeros
of modulus ρ (such ρ exists), and let Other(ρ′) be the Jensen mass
Σ m_w·ln(ρ/|w − x₀|) over the zeros w of F with |w − x₀| < ρ other than the
prescribed ones. Then

  Other(ρ′) ≤ Φ(ρ′) := 4a e^{ρ′} − 2e^{τ}[(τ−2) + (ρ′−τ)(τ−1)] + 2R(ρ′−1) + B′,
  B′ := (κ + 4 + 2/π)a + ½ln(2a),

and consequently the number of non-prescribed zeros of F within distance
2πe^{ρ′} of x₀ is at most Φ(ρ′ + ln 2)/ln 2. In particular at ρ′ = τ:
Φ(τ) = 2e^{τ}(1 − s) + 2R(τ−1) + B′ — as s ↑ 1 the entire foreign-zero
budget inside radius T̃ collapses to O(a + Rτ): **every ordinate dodged past
eT* is borrowed against a zero desert.** (This is the statement DG's node
census tests; their measured ≤ 0.8 nodes in [59, 70] at L = 2.485 after the
stop is consistent.)

### 1.4 What was corrected, and the counterexample (for the record)

The Round-1/merged statement ("F ∈ PW_a cannot vanish on Λ_sm ∩ [0, (1+δ)eT*]
for a large") is FALSE: with K = N_Λ(T̃), P(z) = Π_{k≤K}(1 − z²/t_k²) and
ĥ(z) = (sin(az/M)/(az/M))^M, M = 2K + 2, the function F = P·ĥ is entire of
exponential type ≤ a, lies in L²(ℝ) (|F(x)| = O(|x|^{−2})), is the transform
of a nonzero φ ∈ L²[−a, a] (Paley–Wiener), and vanishes on Λ ∩ [−T̃, T̃] —
for EVERY T̃. A finite system of linear conditions has nonzero solutions.
What Theorem 1 shows is that beyond e²T*·e^{ε*} every such F fails
Hypothesis A: its transform is uniformly exponentially small on [−2π, 2π]
after normalization (mass forced above the vanished head, where in the frame
form the supercritical constraints consume it — which is why the horizon is
invisible to the value E(a) and hard for anchored functions). The two-horizon
reading reconciles all measurements: worth support ends at eT* (law-theory
RUN 4), node budgets saturate aT/π (DG census), stopping heights sit in
(e, e²) (deep-windows, §5), and nothing vanishes-with-anchor past e²T*.

---

## 2. Lean-sized lemmas and complete proofs

Throughout, G(z) := F(x₀ + z).

**Lemma L1 (entirety and growth).** Under (S1), F is entire, and for all
ξ, η ∈ ℝ:
  |F(ξ + iη)| ≤ √(2a) · e^{a|η|}.   (L1.1)

*Proof.* Entirety: the integrand φ(x)e^{−izx} is entire in z for a.e. x and
locally dominated by |φ(x)|e^{a|Im z|} ∈ L¹[−a, a] (Cauchy–Schwarz: ‖φ‖₁ ≤
√(2a)‖φ‖₂ = √(2a)); differentiation under the integral sign (or Morera +
Fubini) gives holomorphy on ℂ. Growth: by Cauchy–Schwarz,
|F(ξ+iη)|² ≤ ‖φ‖₂² · ∫_{−a}^{a} |e^{−i(ξ+iη)x}|² dx = ∫_{−a}^{a} e^{2ηx} dx
= sinh(2aη)/η (η ≠ 0). For y > 0, sinh y ≤ y e^{y} (equivalent to
1 − e^{−2y} ≤ 2y, i.e. 1 − e^{−u} ≤ u); hence sinh(2a|η|)/|η| ≤ 2a e^{2a|η|},
and |F|² ≤ 2a e^{2a|η|}. At η = 0, |F| ≤ ‖φ‖₁ ≤ √(2a) directly. ∎

**Lemma L2 (Fubini/layer-cake identity).** For any finite multiset
{t_k} ⊂ (0, ∞) with counting function N and any T ≥ t_1:
  Σ_{t_k ≤ T} ln(T/t_k) = ∫₀^{T} N(s) ds/s.   (L2.1)

*Proof.* ln(T/t_k) = ∫_{t_k}^{T} ds/s. Sum over the (finitely many) k with
t_k ≤ T and interchange sum and integral (all terms nonnegative; Tonelli):
Σ_k ∫₀^T 1_{[t_k, T]}(s) ds/s = ∫₀^T #{k : t_k ≤ s} ds/s. ∎  [Verified to
1.6e−29 on the 40-point staircase, V2.]

**Lemma L3 (the rvM Jensen mass — closed form).** For T̃ = 2πe^{τ}, τ ≥ 1:
  ∫_{2πe}^{T̃} N̂(s) ds/s = e^{τ}(τ − 2) + (7/8)(τ − 1) + e.   (L3.1)

*Proof.* N̂(s)/s = (1/2π)ln(s/2πe) + (7/8)/s. An antiderivative of the first
term is (1/2π)·s·(ln(s/2πe) − 1); evaluating: at s = T̃ it is e^{τ}(τ − 2),
at s = 2πe it is e·(0 − 1) = −e. The second term integrates to
(7/8)ln(T̃/2πe) = (7/8)(τ − 1). ∎  [Verified to 1e−29 at three τ, V1.]

**Lemma L4 (rigidity transfer).** Under (S2), for T̃ = 2πe^{τ}, τ ≥ 1:
  ∫₀^{T̃} N_Λ(s) ds/s ≥ e^{τ}(τ−2) + (7/8)(τ−1) + e − R(τ−1).   (L4.1)

*Proof.* N_Λ ≥ 0 on [0, 2πe) (drop that range); on [2πe, T̃],
N_Λ(s) ≥ N̂(s) − R pointwise by (S2), and ∫_{2πe}^{T̃} R ds/s = R(τ−1);
apply L3. ∎  [Staircase check with R = ½: slack +1.139 ≥ 0 at τ(t₄₀), V2.]

**Lemma L5 (Jensen's formula, radius selection).** Let G be entire with
G(0) ≠ 0, and let J = [T̃ + 2π, T̃ + 2π + 1]. There exists ρ ∈ J such that G
has no zeros on |z| = ρ, and for any such ρ:
  Σ_{z_j : |z_j| < ρ} m_j·ln(ρ/|z_j|) = (1/2π)∫₀^{2π} ln|G(ρe^{iθ})| dθ − ln|G(0)|,  (L5.1)
the sum over the zeros z_j of G with multiplicities m_j.

*Proof.* G ≢ 0 (G(0) ≠ 0), so the zeros of G are isolated, hence finitely
many in any compact disk, hence their moduli form a countable set; J is
uncountable, so a valid ρ exists. (L5.1) is Jensen's formula: Rudin, *Real
and Complex Analysis*, 3rd ed., Theorem 15.18; Boas, *Entire Functions*,
Academic Press 1954, §1.2; Levin, *Distribution of Zeros of Entire
Functions*, AMS 1964, Ch. I §5. (Mathlib's `AnalyticOnNhd.circleAverage_log_norm`
is this statement with the closed-ball divisor; boundary zeros contribute
ln(ρ/ρ) = 0 there, so the selection step is optional in the formal version.)
∎  [Verified to 2e−30 on F = P·ĥ recentered at x₀ = 2, V3.]

**Lemma L6 (circle bound).** Under (S1) and |x₀| ≤ 2π, for every ρ ∈ J:
  (1/2π)∫₀^{2π} ln|G(ρe^{iθ})| dθ ≤ ½ln(2a) + (2/π)aρ
   ≤ ½ln(2a) + 4a e^{τ} + (4 + 2/π)a.   (L6.1)

*Proof.* |G(ρe^{iθ})| = |F(x₀ + ρe^{iθ})| ≤ √(2a)·e^{aρ|sin θ|} by (L1.1)
(the imaginary part of x₀ + ρe^{iθ} is ρ sin θ). Average over θ using
(1/2π)∫₀^{2π}|sin θ| dθ = 2/π. Finally ρ ≤ T̃ + 2π + 1 gives
(2/π)aρ ≤ 4a e^{τ} + (2/π)(2π + 1)a = 4a e^{τ} + (4 + 2/π)a. ∎
[Verified on the normalized P·ĥ example: 2.72 ≤ 12.87, V4.]

**Lemma L7 (prescribed mass; the pair-product bound).** Under (S2), (S3),
|x₀| ≤ 2π < t_1, and ρ ≥ T̃ + 2π: all prescribed zeros ±t_k (t_k ≤ T̃) of G
(as zeros of G they sit at ±t_k − x₀) lie in |z| < ρ, and their total Jensen
mass in (L5.1) is at least
  Σ_{t_k ≤ T̃} m_k · ln( ρ² / (t_k² − x₀²) ) ≥ 2 Σ_{t_k ≤ T̃} m_k·ln(T̃/t_k)
   = 2∫₀^{T̃} N_Λ(s) ds/s.   (L7.1)
Moreover every other zero of G in |z| < ρ contributes ≥ 0 to (L5.1).

*Proof.* Distances from the center: |±t_k − x₀| ≤ t_k + 2π ≤ T̃ + 2π ≤ ρ, so
the prescribed zeros are in the (closed) disk; with the selection of L5 none
is on the boundary, so all are interior. For the pair at ±t_k:
ln(ρ/|t_k − x₀|) + ln(ρ/|t_k + x₀|) = ln(ρ²/|t_k² − x₀²|), and since
|x₀| ≤ 2π < t_1 ≤ t_k, |t_k² − x₀²| = t_k² − x₀² ≤ t_k²; hence the pair mass
is ≥ ln(ρ²/t_k²) = 2ln(ρ/t_k) ≥ 2ln(T̃/t_k) ≥ 0. Orders ≥ m_k give the
multiplicity factor. The final identity is L2. Any other interior zero has
|z_j| < ρ, so ln(ρ/|z_j|) > 0. ∎  [Pair bound verified pointwise, V3.]

**Lemma L8 (monotone crossing).** For 0 ≤ R < e^{2a+2}, the function
h(τ) := 2e^{τ}(τ − 2 − 2a) − 2R(τ − 1) is strictly increasing on
[2a + 2, ∞), and with ε* as in Theorem 1 (case ε* > 0):
  h(2a + 2 + ε*) ≥ B.   (L8.1)

*Proof.* h′(τ) = 2e^{τ}(τ − 1 − 2a) − 2R ≥ 2e^{2a+2}·1 − 2R > 0 for
τ ≥ 2a + 2. And h(2a+2+ε) = 2e^{2a+2+ε}ε − 2R(2a+1+ε) ≥ 2e^{2a+2}ε −
2Rε − 2R(2a+1) = 2ε(e^{2a+2} − R) − 2R(2a+1); at ε = ε* this equals
B + 2R(2a+1) − 2R(2a+1) = B. ∎  [Monotonicity spot-checked, V5.]

---

## 3. Proof of Theorem 1

If τ < 2a + 2 there is nothing to prove; assume τ ≥ 2a + 2. Apply L5 to
G(z) = F(x₀ + z) (G entire by L1; G(0) = F(x₀) ≠ 0 by Hypothesis A) with a
radius ρ ∈ [T̃ + 2π, T̃ + 2π + 1] avoiding zero-moduli. Chain the lemmas:

  2[e^{τ}(τ−2) + (7/8)(τ−1) + e − R(τ−1)]
    ≤ 2∫₀^{T̃} N_Λ(s) ds/s            [L4]
    ≤ Σ_prescribed (pair masses)       [L7, eq. (L7.1)]
    ≤ Σ_{all zeros of G in |z|<ρ} m_j ln(ρ/|z_j|)   [L7, last clause]
    = (1/2π)∫₀^{2π} ln|G(ρe^{iθ})|dθ − ln|F(x₀)|    [L5]
    ≤ ½ln(2a) + 4a e^{τ} + (4 + 2/π)a + κa.         [L6 + Hypothesis A]

Discard the favorable terms 2·[(7/8)(τ−1) + e] ≥ 0 on the left and rearrange:

  h(τ) = 2e^{τ}(τ − 2 − 2a) − 2R(τ−1) ≤ (κ + 4 + 2/π)a + ½ln(2a) = B.

If ε* = 0 (i.e. B ≤ −2R(2a+1)): h(2a+2) = −2R(2a+1) ≥ B, and h is strictly
increasing (L8), so h(τ) > B for every τ > 2a+2 — contradiction; hence
τ ≤ 2a + 2. If ε* > 0: by L8, h(2a+2+ε*) ≥ B ≥ h(τ) and h is strictly
increasing on [2a+2, ∞), hence τ ≤ 2a + 2 + ε*. ∎

Hypothesis audit: (S2) was used only through L4 (one-sided, only on
[2πe, T̃]); R ≤ e^{2a+1} guarantees R < e^{2a+2} in L8 and makes the
denominator ≥ 2e^{2a+2}(1 − e^{−1}) > 0. Hypothesis A was used exactly once,
as −ln|G(0)| ≤ κa. No Plancherel, no completeness theory, no density
theorems: the proof is Jensen + calculus.

---

## 4. Proofs of the corollaries

### 4.1 Corollary 1 (true zeta ordinates, unconditional)

**Inputs, quoted verbatim from PLAN-number-theory.md Round 2(b) (the NT
seat's constants-explicit licenses).**

> **Lemma R1 (counting license — unconditional, constants explicit).** For
> all T ≥ e: |N_ζ(T) − N̂(T)| ≤ S₀(T) + 1/(48πT) + ε₃(T) ≤ S₀(T) + 0.007
> =: D₀(T), where S₀(T) = 0.112 log T + 0.278 log log T + 2.510. Sources:
> |S(T)| ≤ S₀(T) for T ≥ e is Trudgian, *An improved upper bound for the
> argument of the Riemann zeta-function on the critical line II*, J. Number
> Theory 134 (2014), 280–292, Theorem 1; the remainder is the standard theta
> expansion (Edwards, *Riemann's Zeta Function*, §6.5).

Here N_ζ(T) is the number of nontrivial zeros with ordinate in (0, T],
counted with multiplicity, regardless of real part — R1 is unconditional.

*Proof of Corollary 1.* Λ_ζ satisfies (S2) with any R ≥ sup_{T ≤ T̃} D₀(T)
= D₀(T̃) (D₀ increasing); t_1 = γ₁ = 14.1347… > 2π (classical; e.g. the
repo's certified zero list). Two-step application of Theorem 1:

Step 1 (a-priori cap). Suppose T̃ > 2πe^{2a+3} =: T̃′. Then F vanishes on
Λ_ζ up to T̃′ a fortiori, and Theorem 1 applies with horizon T̃′ and
R = D₀(T̃′) (which is ≤ e^{2a+1} for a ≥ 7/16: D₀(2πe^{2a+3}) ≤ 4.2 for
a ≤ 2.25, growing only logarithmically, while e^{2a+1} ≥ 6.5). The
conclusion reads 2a + 3 = ln(T̃′/2π) ≤ 2a + 2 + ε*, i.e. ε* ≥ 1. But
ε* < 1 for every a ≥ 7/16 (with κ = 1), by the following elementary
estimate. Using ln x ≤ x/e: R = D₀(2πe^{2a+3}) = 0.112(2a + 4.838) +
0.278·ln(2a + 4.838) + 2.517 ≤ 0.43a + 3.56; and ln(2a) ≤ 2a − 1 gives
½ln(2a) ≤ a − ½. Hence the numerator of ε* satisfies
B + 2R(2a+1) ≤ 5.64a + (a − ½) + (4a+2)(0.43a + 3.56)
= 1.72a² + 21.74a + 6.62 ≤ 1.72a² + 21.8a + 6.7, while the denominator is
2(e^{2a+2} − R) ≥ 2e^{2a+2} − 8.5. At a = 7/16 the inequality
1.72a² + 21.8a + 6.7 < 2e^{2a+2} − 8.5 reads 16.6 < 27.0 ✓, and it
persists for all larger a: the right side's derivative 4e^{2a+2} ≥ 70.9
exceeds the left side's 3.44a + 21.8 at a = 7/16 (23.3 < 70.9), and the
gap only widens (exponential vs linear). Contradiction; hence
T̃ ≤ 2πe^{2a+3}. (Appendix V5 lists the actual ε*_ζ values, 0.57 → 0.045
across the program range — comfortably below the crude bound.)

Step 2 (main application). Now R := D₀(2πe^{2a+3}) ≥ D₀(T̃) is a valid
rigidity constant on all of [2πe, T̃]; Theorem 1 gives
τ ≤ 2a + 2 + ε*_ζ with the stated ε*_ζ. ∎

*Remarks.* (i) Multiplicity: hypothesis (S3) asks F to vanish at ±γ to the
order of the zero. If all zeros in the window are simple — verified for all
zeros to height 3·10¹² (Platt–Trudgian, Bull. LMS 53 (2021), 792–797; NT's
scope note: this covers every support with 2a + 2 + ε* ≤ ln(3·10¹²/2π), i.e.
L ≤ ~49) — plain vanishing at the distinct ordinates suffices in the entire
range this program will ever measure. (ii) The statement is about the
ordinate multiset, which is defined without RH; no zero-location input
enters anywhere. (iii) For κ: the corollary is typically applied to
competitor functions where κ is known by construction; see §5 (Gap 1) for
the minimizer case.

### 4.2 Corollary 2 (zero desert)

*Proof.* The radius ρ exists by the countability argument of L5. Run the
Theorem-1 chain at radius ρ, keeping the other-zeros term instead of
discarding it. Jensen (L5) splits the zero sum into prescribed and other:

  Other(ρ′) = (1/2π)∫ln|G(ρe^{iθ})|dθ − ln|F(x₀)| − Σ_prescribed
   ≤ [½ln(2a) + (2/π)aρ] + κa − Σ_prescribed.        (4.2.1)

For the prescribed mass at this larger radius, the pair-product bound (L7,
with ρ ≥ 2πe^{ρ′} in place of T̃ inside the logarithm) gives, for every
t_k ≤ T̃, pair mass ≥ 2 ln(2πe^{ρ′}/t_k) = 2ln(T̃/t_k) + 2(ρ′ − τ); summing
with multiplicity and using L2, L4 and
N_Λ(T̃) ≥ N̂(T̃) − R = e^{τ}(τ−1) + 7/8 − R:

  Σ_prescribed ≥ 2[e^{τ}(τ−2) − R(τ−1)] + 2(ρ′−τ)[e^{τ}(τ−1) − R]  (4.2.2)

(the favorable 7/8- and e-terms are again discarded). Since
(2/π)aρ ≤ (2/π)a(2πe^{ρ′} + 2π + 1) = 4a e^{ρ′} + (4 + 2/π)a, combining
(4.2.1)–(4.2.2) yields Other(ρ′) ≤ Φ(ρ′) as stated.

Counting version: let w be a non-prescribed zero with |w − x₀| ≤ 2πe^{ρ′}.
At the enlarged parameter ρ′ + ln 2 the selected radius satisfies
ρ(ρ′ + ln 2) ≥ 2πe^{ρ′}·2 + 2π, so w contributes to Other(ρ′ + ln 2) at
least ln((4πe^{ρ′} + 2π)/(2πe^{ρ′})) = ln(2 + e^{−ρ′}) > ln 2, and every
other term of Other(ρ′ + ln 2) is ≥ 0. Hence
#{such zeros} ≤ Other(ρ′ + ln 2)/ln 2 ≤ Φ(ρ′ + ln 2)/ln 2. ∎

---

## 5. Disposition of the four Round-2 boxed gaps

**Gap 1 (the anchor) → formal Hypothesis A; partially discharged; remainder
open.** Discharged: for every construction-competitor in the T5/H3 program
(canonical-product × window ansätze), κ is explicit by design. Open: that
near-minimizers of the frame form satisfy Hypothesis A with κ = O(1). This
is exactly the lattice-adapted Turán wall (SYNTHESIS T1(ii)/T5 "hardest
step") and is stated here as the standing open problem of this document.
Assigned numerical calibration (NA seat, cheap): evaluate max_{|x| ≤ 2π}
|φ̂_min(x)| on the stored minimizers at L = 1.75/2.485/2.996; report
κ_eff = −ln(·)/a. Prediction (falsifiable): κ_eff ≤ 2 across the ladder.

**Gap 2 (sharpness of e²) → open, now stated as a conjecture.** Conjecture:
for every δ > 0 and a ≥ a₀(δ) there is an anchored F (κ = O(1)) vanishing
on Λ_sm through T̃ = e^{2−δ}·T*. Route: the P·ĥ family with ĥ replaced by a
Beurling–Malliavin window shaped to hold Θ(1) of the L²-mass below T*;
the Jensen books balance up to e²T*, so only the mass location obstructs.
Not proved here; Corollary 2's pinch (Φ(τ) ↓ O(a + Rτ) as s ↑ 1) is the
quantitative reason the construction gets hard near the horizon.

**Gap 3 (onset) → RESOLVED, Round-2 statement withdrawn.** The Round-2
sketch estimated ε < 1 only for a ≳ 1.2. The two sharpenings in this
write-up (the pair-product bound L7 eliminating the anchor-shift loss; the
Fubini identity L2 eliminating the τ² bookkeeping) give ε* = 0.12 already at
a = 0.62 with (R, κ) = (½, 1), and ε*_ζ ≤ 0.57 at every program window down
to L = 1.75 (V5). The theorem now bites at all measured supports: hard caps
13.1·T* → 7.7·T* across L = 1.75 → 9 for ζ itself, unconditionally.

**Gap 4 (sharp local zero counts) → open, not needed here.** Nothing in
this document bounds n_F(T) at a single T sharply (disk-Jensen localizes
only at cost e). DG-2(a)2's O(log)-sharp node budget for minimizers still
needs a tool beyond Jensen; unchanged flag to the DG seat.

---

## 6. Data consistency (evidence, not proof)

The deep-windows final report (results/agent-deep-windows.md, "The T1′
two-horizon consistency test — PASS") measured the stopping height w_E2(L)
(T_s = e^{w}T*) at eleven supports L = 1.75 … 5.50:

  w = 1.1437, 1.1647, 1.1803, 1.1970, 1.2087, 1.2136, 1.2192, 1.2211,
      1.2243, 1.2282, 1.1861 (last row unconverged, verdict U at L = 5.0,
      plunge at 5.5; A-band moves w by ≤ 0.008).

All eleven lie strictly inside (1, 2): margins ≥ +0.1437 to the count
horizon and ≥ +0.7718 to the hard horizon; in height units T_s/T* ∈
[3.14, 3.41] ⊂ (e, e²) = (2.718, 7.389) [V7]. The bend verdict from the same
report — decay rate saturating at the prolate rate 4π per unit e^{L/2} past
L ≈ 4.32, i.e. w → w∞ = 1.2785, e^{w∞} = 3.59 — also sits strictly inside
the horizons forever; the corrected T1′ is compatible with the resolved
Connes/Groskin normalization at c = 100 (log₁₀λ ≈ −528 vs −530).

Honest caveats. (i) Consistency is not proof: the w-test confronts the
TWO-HORIZON PICTURE, of which Theorem 1 proves only the hard side; the
variational side (T_s > e·T*, worth support ending at eT*) is measured and
is a months-scale target (T4/H1(iii)), not a theorem. (ii) The measured
stopping heights are properties of MINIMIZERS, whose anchor status is
exactly Gap 1: Theorem 1 constrains them today only modulo Hypothesis A.
(iii) ε* is small but not zero at the measured supports: the proved caps
(e.g. ≤ 11.7·T* at L = 2.485 for ζ, ≤ 8.9·T* with staircase R = ½) are
comfortably above the measured T_s ≈ 3.2·T* — the theorem excludes deep
dodging, it does not predict the stopping height. Deriving T_s (the
standoff ≈ 3.6T*) is C4's obstacle problem, not this document.

---

## 7. Lean decomposition and mathlib gap-map

Terminal criterion: kernel-checked. Decomposition follows §2–§4; each item
is sized at ≤ a few days of formalization by one person familiar with
mathlib analysis. Names checked against the LOCAL snapshot
`lean/glide/.lake/packages/mathlib` @ `520045ab14` (2026-07-23); names may
drift upstream.

| # | Statement | Mathlib status (checked locally) | Est. |
|---|---|---|---|
| L1 | F entire + √(2a)e^{a·|Im z|} growth | Differentiation under ∫: `intervalIntegral.hasDerivAt_integral_of_dominated_loc_of_lip` (or Morera route `Complex.differentiable_of_...`); differentiable-everywhere ⟹ analytic: `Differentiable.analyticOnNhd`. C–S: `MeasureTheory.inner_mul_le_norm_mul_norm`/`Memℒp` API. sinh y ≤ y·e^y: 5-line calc (`Real.sinh_eq`, `Real.add_one_le_exp`). No Paley–Wiener needed (easy direction only). | 2–4 d |
| L2 | Σ ln(T/t_k) = ∫₀^T N/s | Direct: finite sum, `MeasureTheory.integral_finset_sum` + indicator Tonelli (`MeasureTheory.lintegral_finset_sum`); alternatively `Mathlib/NumberTheory/AbelSummation.lean` (`sum_mul_eq_sub_sub_integral_mul`). | 1–2 d |
| L3 | rvM closed form (L3.1) | `intervalIntegral.integral_log` exists; FTC `intervalIntegral.integral_eq_sub_of_hasDerivAt`. Pure calculus. | 1 d |
| L4 | rigidity transfer | Pointwise integrand inequality + `intervalIntegral.integral_mono_on`; trivial on top of L2/L3. | ½ d |
| L5 | Jensen + radius selection | **PRESENT**: `AnalyticOnNhd.circleAverage_log_norm` (Mathlib/Analysis/Complex/JensenFormula.lean) — Jensen at center c, radius R, divisor sum over the closed ball; boundary zeros contribute 0, so radius selection is OPTIONAL in Lean. Zero-finiteness: `(divisor …).finiteSupport` in the same file. Also available: `AnalyticOnNhd.sum_divisor_le` (Jensen's inequality) and the ValueDistribution/ Nevanlinna folder. Work = instantiation + divisor ≥ prescribed multiset (`AnalyticOnNhd.divisor_apply`, `analyticOrderAt` ≥ m at a prescribed zero). | 2–3 d |
| L6 | circle average bound | `circleAverage` API (same file family); ∫₀^{2π}|sin| = 4: `integral_sin` on quarters. | 1 d |
| L7 | pair-product + positivity | Algebra + `Real.log` monotonicity; multiplicity via divisor as in L5. | 1 d |
| L8 | monotone crossing | `StrictMonoOn` via `strictMonoOn_of_deriv_pos`; explicit evaluation. | ½ d |
| Thm 1 | assembly | Chain of L4→L7→L5→L6; bookkeeping. | 1–2 d |
| Cor 2 | desert | Re-run of the chain keeping the remainder term. | 1–2 d |
| Cor 1 | ζ instantiation | **BLOCKED — the one far item.** Needs formalized RvM with explicit constants (R1: Trudgian 2014 + theta expansion). Local mathlib has `riemannZeta`, zeros as a set, functional equation (Loeffler–Stoll corpus) but NO zero-counting asymptotics; PrimeNumberTheoremAnd (per prior-art §4) has no explicit-formula/N(T) statement either. Formalizing R1 is a standalone multi-month project (Backlund-style argument principle + explicit θ(T) bounds). Note: Theorem 1 + Corollary 2 for the STAIRCASE need zero arithmetic input and are fully unblocked. | months (external) |

Estimated unblocked total: ~2–3 weeks single-person for Theorem 1 + Corollary
2 kernel-checked over the staircase — a realistic next Lean artifact after
`weil_window_positive`, and the first ANALYTIC (non-finite-dimensional)
statement of the program to be formalized. Recommended order: L3, L8, L2,
L4 (pure calculus, zero risk) → L1, L6 → L5, L7 → assembly.

---

## Appendix V — verification script and output (program standard)

Script (`verify_t1prime.py`, run 2026-07-26, mpmath dps 30; also archived in
the session scratchpad). Checks: V1 = (L3.1); V2 = (L2.1) + (L4.1) on the
true staircase with R = ½; V3 = (L5.1) + (L7.1) pair bound on a concrete
F = P·ĥ recentered at x₀ = 2; V4 = (L6.1) on the normalized F; V5 = ε*
table for Theorem 1 and Corollary 1 (with the NT cross-check D₀(e²T*) =
3.476 at ℓ = 0.875, matching PLAN-number-theory to all printed digits) and
L8 monotonicity; V6 = Lemma 0's D(eT*) = −7/8; V7 = the §6 w-data margins.

```python
"""verify_t1prime.py -- numerical verification of every numbered estimate in T1PRIME.md.
Run: python3 verify_t1prime.py   (mpmath only; ~1 min)"""
import mpmath as mp
mp.mp.dps = 30
pi = mp.pi

def Nhat(T):          # smooth counting function
    return (T/(2*pi))*mp.log(T/(2*pi*mp.e)) + mp.mpf(7)/8

def staircase(K):     # t_k solving Nhat(t_k) = k - 1/2, Newton
    out, g = [], mp.mpf(14)
    for k in range(1, K+1):
        target = k - mp.mpf('0.5') - mp.mpf('0.875')
        for _ in range(80):
            f  = g/(2*pi)*mp.log(g/(2*pi*mp.e)) - target
            fp = mp.log(g/(2*pi))/(2*pi)
            g -= f/fp
            if abs(f/fp) < mp.mpf('1e-25'): break
        out.append(+g); g += 2*pi/mp.log(g/(2*pi))
    return out

print("== (V1) closed form: int_{2pi e}^{Ttil} Nhat(s)/s ds = e^tau(tau-2)+(7/8)(tau-1)+e")
for tau in (mp.mpf('2.0'), mp.mpf('3.2425'), mp.mpf('4.5')):
    Ttil = 2*pi*mp.e**tau
    lhs  = mp.quad(lambda s: Nhat(s)/s, [2*pi*mp.e, Ttil])
    rhs  = mp.e**tau*(tau-2) + mp.mpf(7)/8*(tau-1) + mp.e
    print("  tau=%s  lhs=%s rhs=%s  diff=%.1e" % (tau, mp.nstr(lhs,12), mp.nstr(rhs,12), float(abs(lhs-rhs))))

print("== (V2) Fubini identity + staircase lower bound (R=1/2), Ttil = t_40 + 0.3")
ts = staircase(60); Ttil = ts[39] + mp.mpf('0.3'); tau = mp.log(Ttil/(2*pi))
S  = sum(mp.log(Ttil/t) for t in ts if t <= Ttil)
# exact piecewise evaluation of int_0^Ttil N(s)/s ds  (N constant = k on [t_k, t_{k+1}))
pts = [t for t in ts if t <= Ttil] + [Ttil]
I   = sum(k*mp.log(pts[k]/pts[k-1]) for k in range(1, len(pts)))
low = mp.e**tau*(tau-2) + mp.mpf(7)/8*(tau-1) + mp.e - mp.mpf('0.5')*(tau-1)
print("  sum=%s  int N/s=%s  (identity diff=%.1e);  lower bd=%s  sum-lb=%+.4f (must be >=0)"
      % (mp.nstr(S,10), mp.nstr(I,10), float(abs(S-I)), mp.nstr(low,10), float(S-low)))

print("== (V3) Jensen's formula, recentered, on F = P * sinc^M (a=0.62125, K=3, M=8)")
a  = mp.mpf('2.485')/4; K = 3; M = 8
tk = ts[:K]
def F(z):
    z = mp.mpf(z) if isinstance(z,(int,float)) else z
    P = mp.mpf(1)
    for t in tk: P *= (1 - z*z/(t*t))
    w = a*z/M
    s = 1 if abs(w)<mp.mpf('1e-12') else mp.sin(w)/w
    return P * s**M
x0 = mp.mpf(2); Ttest = tk[-1] + mp.mpf('0.5'); rho = Ttest + 2*pi
zeros_in = [t - x0 for t in tk] + [-t - x0 for t in tk]        # distances from center
zsum = sum(mp.log(rho/abs(d)) for d in zeros_in)
circ = mp.quad(lambda th: mp.log(abs(F(x0 + rho*mp.exp(1j*th)))), [0, pi/2, pi, 3*pi/2, 2*pi])/(2*pi)
jenL = zsum + mp.log(abs(F(x0)))
print("  circleAvg ln|F| = %s ; zero-sum + ln|F(x0)| = %s ; diff = %.1e"
      % (mp.nstr(circ,12), mp.nstr(jenL,12), float(abs(circ-jenL))))
pairs_ok = all(mp.log(rho*rho/(t*t - x0*x0)) >= 2*mp.log(Ttest/t) - mp.mpf('1e-25') for t in tk)
print("  pair-product bound ln(rho^2/(t^2-x0^2)) >= 2 ln(Ttil/t): %s" % pairs_ok)

print("== (V4) circle bound for the NORMALIZED F: mean ln|F_n| <= (1/2)ln(2a) + (2/pi)a rho")
brk = [40.45*j for j in range(1,25)]
nrm2 = 2*mp.quad(lambda x: abs(F(x))**2, [0] + brk + [1500]) / (2*pi)   # ||phi||^2
Fn_circ = circ - mp.log(mp.sqrt(nrm2))
bound   = mp.mpf('0.5')*mp.log(2*a) + (2/pi)*a*rho
print("  ||phi||_2^2 = %s ; mean ln|F_n| = %s <= %s : %s"
      % (mp.nstr(nrm2,8), mp.nstr(Fn_circ,8), mp.nstr(bound,8), Fn_circ <= bound))

print("== (V5) h monotone on [2a+2,inf) and eps* table  eps*=[B+2R(2a+1)]/(2(e^{2a+2}-R))")
def epsstar(a,R,kap):
    B = (kap + 4 + 2/pi)*a + mp.mpf('0.5')*mp.log(2*a)
    return (B + 2*R*(2*a+1))/(2*(mp.e**(2*a+2) - R))
def D0(T):  # NT Lemma R1: Trudgian S0 + 0.007
    return mp.mpf('0.112')*mp.log(T) + mp.mpf('0.278')*mp.log(mp.log(T)) + mp.mpf('2.517')
print("  NT cross-check D0(e^2 T*) at l=0.875: %s (NT quotes 3.476)" % mp.nstr(D0(2*pi*mp.e**(mp.mpf('0.875')+2)),4))
for aa in ('0.4375','0.62125','0.749','1.0','1.5','2.25'):
    aa = mp.mpf(aa)
    Rz = D0(2*pi*mp.e**(2*aa+3))                       # zeta corollary, a-priori window
    print("  a=%s  L=%s : eps*(R=1/2,k=1)=%s  eps*(R=D0=%s,k=1)=%s  hard cap e^{2+eps*}T* = %s T*"
          % (mp.nstr(aa,4), mp.nstr(4*aa,4), mp.nstr(epsstar(aa,mp.mpf('0.5'),1),3),
             mp.nstr(Rz,4), mp.nstr(epsstar(aa,Rz,1),3),
             mp.nstr(mp.e**(2+epsstar(aa,Rz,1)),4)))
for aa in (mp.mpf('0.62125'), mp.mpf('1.5')):
    taus = [2*aa+2+k*mp.mpf('0.3') for k in range(4)]
    hs = [2*mp.e**t*(t-2-2*aa) - 2*mp.mpf('0.5')*(t-1) for t in taus]
    print("  h increasing at a=%s: %s" % (mp.nstr(aa,4), all(hs[i]<hs[i+1] for i in range(3))))

print("== (V6) D(eT*) = -7/8 exactly (D = (a/pi)T - Nhat)")
for aa in (mp.mpf('0.62125'), mp.mpf('1.126')):
    eTs = 2*pi*mp.e**(2*aa+1)
    print("  a=%s: D(eT*) = %s" % (mp.nstr(aa,5), mp.nstr((aa/pi)*eTs - Nhat(eTs), 8)))

print("== (V7) deep-windows w-data vs the two horizons (consistency, not proof)")
w = [1.1437,1.1647,1.1803,1.1970,1.2087,1.2136,1.2192,1.2211,1.2243,1.2282,1.1861]
print("  all in (1,2): %s ; min margin to e-horizon: %+0.4f ; to e^2-horizon: %+0.4f"
      % (all(1 < x < 2 for x in w), min(x-1 for x in w), min(2-x for x in w)))
print("  T_s/T* range: [%.3f, %.3f] inside (e, e^2) = (2.718, 7.389)"
      % (mp.e**min(w), mp.e**max(w)))
```

Output (verbatim, 2026-07-26):

```
== (V1) closed form: int_{2pi e}^{Ttil} Nhat(s)/s ds = e^tau(tau-2)+(7/8)(tau-1)+e
  tau=2.0  lhs=3.59328182846 rhs=3.59328182846  diff=3.9e-31
  tau=3.2425  lhs=36.485531948 rhs=36.485531948  diff=6.3e-30
  tau=4.5  lhs=230.82361008 rhs=230.82361008  diff=2.5e-29
== (V2) Fubini identity + staircase lower bound (R=1/2), Ttil = t_40 + 0.3
  sum=23.74989324  int N/s=23.74989324  (identity diff=1.6e-29);  lower bd=22.61077342  sum-lb=+1.1391 (must be >=0)
== (V3) Jensen's formula, recentered, on F = P * sinc^M (a=0.62125, K=3, M=8)
  circleAvg ln|F| = 2.92972068601 ; zero-sum + ln|F(x0)| = 2.92972068601 ; diff = 2.0e-30
  pair-product bound ln(rho^2/(t^2-x0^2)) >= 2 ln(Ttil/t): True
== (V4) circle bound for the NORMALIZED F: mean ln|F_n| <= (1/2)ln(2a) + (2/pi)a rho
  ||phi||_2^2 = 1.5079609 ; mean ln|F_n| = 2.7243415 <= 12.873667 : True
== (V5) h monotone on [2a+2,inf) and eps* table  eps*=[B+2R(2a+1)]/(2(e^{2a+2}-R))
  NT cross-check D0(e^2 T*) at l=0.875: 3.476 (NT quotes 3.476)
  a=0.4375  L=1.75 : eps*(R=1/2,k=1)=0.124  eps*(R=D0=3.641,k=1)=0.57  hard cap e^{2+eps*}T* = 13.07 T*
  a=0.6212  L=2.485 : eps*(R=1/2,k=1)=0.117  eps*(R=D0=3.7,k=1)=0.461  hard cap e^{2+eps*}T* = 11.72 T*
  a=0.749  L=2.996 : eps*(R=1/2,k=1)=0.106  eps*(R=D0=3.74,k=1)=0.394  hard cap e^{2+eps*}T* = 10.96 T*
  a=1.0  L=4.0 : eps*(R=1/2,k=1)=0.083  eps*(R=D0=3.817,k=1)=0.284  hard cap e^{2+eps*}T* = 9.82 T*
  a=1.5  L=6.0 : eps*(R=1/2,k=1)=0.044  eps*(R=D0=3.967,k=1)=0.141  hard cap e^{2+eps*}T* = 8.508 T*
  a=2.25  L=9.0 : eps*(R=1/2,k=1)=0.0142  eps*(R=D0=4.184,k=1)=0.045  hard cap e^{2+eps*}T* = 7.729 T*
  h increasing at a=0.6212: True
  h increasing at a=1.5: True
== (V6) D(eT*) = -7/8 exactly (D = (a/pi)T - Nhat)
  a=0.62125: D(eT*) = -0.875
  a=1.126: D(eT*) = -0.875
== (V7) deep-windows w-data vs the two horizons (consistency, not proof)
  all in (1,2): True ; min margin to e-horizon: +0.1437 ; to e^2-horizon: +0.7718
  T_s/T* range: [3.138, 3.415] inside (e, e^2) = (2.718, 7.389)
```

Notes on V-coverage. V2's staircase satisfies (S2) with R = ½ (N̂(t_k) =
k − ½ implies |N_Λ − N̂| ≤ ½), and the +1.1391 slack over the lower bound
(L4.1) is the discarded (7/8)(τ−1) + e minus discreteness — positive as
required. V3's test function has its sinc zeros at |z| = 40.45k, outside
the Jensen disk |z − 2| ≤ 31.8, so the prescribed six zeros are the complete
zero set in the disk — Jensen closes to 2e−30, confirming (L5.1) exactly in
the recentered form used in the proof. V4 confirms (L6.1) with 10 nats to
spare at this tiny example. V5's D₀ cross-check ties this document's
Corollary-1 constants to PLAN-number-theory's independently computed values.



---

## Coordinator's correction (2026-07-26, IAS panel, C-11/free-boundary R2)

The §6 data-consistency section compares the theorem's horizons against the
measured stopping heights w ∈ [1.144, 1.228]. The IAS panel's vector-level
measurements show those eleven values are ACTION heights (where the
minimizer's exponent budget is spent), not VANISHING heights: actual
node-to-zero registration terminates at ≈ 1.9·T* (w ≈ 0.64) at every tested
window. The theorem itself is untouched (and kernel-checked); the correct
data test of the Hard Horizon is that REGISTRATION heights stay below the
hard horizon — satisfied with room to spare — while the action heights test
the variational (eT*) story instead. §6's language should be read with that
substitution; a redraft is queued with the owning seat.
