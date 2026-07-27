# PLAN — Harmonic analysis seat (exponential systems, sampling, de Branges spaces, prolate theory)

Independent expert plan, prepared 2026-07-26. Inputs read: README.md, PROGRAM.md
§2.14–2.18/§3/§4, THEOREMS.md, ENVELOPE.md, results/RESULTS.md; plus the two
measurement reports results/agent-prior-art.md (§3 transcriptions of
Landau–Widom 1980, Fuchs 1964, Widom 1964, Bonami–Karoui 2017, and the
supercritical-Vandermonde literature — cited from there below) and
results/agent-law-theory.md (measurement report; the capacity/marginal/
deformation data). No other expert's PLAN file was read. Deliverable: lemmas
only; all proposed computations are designs for the numerics seats.

Notation (locked to the repo ledger). a = L/4, I = [−a, a] (|I| = L/2 = 2a);
φ̂(r) = ∫φ e^{−irx}dx; type(φ̂) ≤ a for φ ∈ L²(I). Λ_sm = smooth staircase
{±t_k : N_sm(t_k) = k − 1/2}, N_sm(T) = (T/2π)ln(T/2πe) + 7/8. Nyquist
crossing T* = 2π e^{2a}; **capacity height T_cap = eT* = 2π e^{2a+1}** (where
the cumulative zero budget of a type-a function is exhausted: N_sm(T) ≤ (a/π)T
iff T ≤ eT*(1+o(1))). E := −ln λ. Measured (repo + law-theory sharpening):
E(L) = −A + b e^{2a}(2a + c₀) with (A, b, c₀) = (11.13, 1.509, 5.04)
(spread A 11.1–11.8, b 1.39–1.51, c₀ 5.0–5.7), equivalently
E + A = b[N(T*) + μ D(T*)], μ = c₀ + 1, D(T) = (a/π)T − N(T).

---

## 1. Reformulation.

**(R1) The object is a lower frame bound at graded density — conditionally.**
Under RH, λ(L) = min{2Σ_{γ>0}|φ̂(γ)|² : ‖φ‖_{L²(I)} = 1} — the smallest
eigenvalue of the concentration operator T_L = P_I (Σ_{t∈Λ} e_t ⊗ e_t) P_I,
Λ = {±γ}. Everything my field can prove lives here or on model sequences Λ.
The classical frame theory (Beurling; Landau, Acta Math. 117 (1967);
Ortega-Cerdà–Seip, Ann. of Math. 155 (2002); Seip, *Interpolation and Sampling
in Spaces of Analytic Functions*, AMS 2004) gives positivity of each fixed-L
margin after thinning (as ENVELOPE.md already notes) but no rates; the rate is
the program's object.

**(R2) The margin is a discreteness effect, not a concentration effect.** The
law-theory report proves the calibration (its §2.1, a two-line Poisson-summation
theorem worth recording as a lemma): an arithmetic progression of spacing
s₀ ≤ π/a is an exact tight frame (λ = 2π/s₀, zero cost), and s₀ > π/a has an
exact infinite-dimensional kernel. And its §2.0: replacing the zero *sum* by
the density *integral* makes λ order one. So: **all exponential smallness is
the sum-vs-integral gap** — φ̂ vanishes *at* the points and lives *between*
them — and every functional built from smoothed/bulk prolate asymptotics
(Fuchs, LW plunge, Widom mode counting) fails structurally (law-theory §2.2).
The correct territory is: zero sets and canonical products of Paley–Wiener
functions, Turán-type lower bounds, Beurling–Malliavin majorants, and the
clustered-node Vandermonde literature (agent-prior-art.md §3.3: Batenkov–
Demanet–Goldman–Yomdin, SIMAX 2020; Kunis–Nagel 2020/2021). This kills the
naive version of the "derive b from Landau–Widom" hope and redirects it: the
LW/BK constants survive, but in the *marginal* law (R4), not the bulk.

**(R3) Unconditional operator reading (for reference; the only unconditional
frame).** Q_L = P_I[Ψ(D) + Pole − X_L]P_I with Ψ(D) the Fourier multiplier
with symbol Re ψ(1/4 + ir/2) − ln π (two-sidedly log-controlled by THEOREMS.md
Lemma A), Pole a rank-≤2 term, and X_L = Σ_{n<e^{2a}} Λ(n) n^{−1/2}
(S_{ln n} + S_{−ln n}) a bounded almost-periodic Toeplitz/shift sum,
‖X_L‖ ≤ 2Σ_{n<e^{2a}}Λ(n)n^{−1/2} ≍ 4e^{a}. The margin e^{−E} sits ~30 decades
below what operator-norm perturbation theory can see in this splitting; that
asymmetry is restated honestly in §5.

**(R4) The two structural laws now in evidence, in harmonic-analysis terms.**
(i) *Capacity*: the marginal worth of a zero at height t is supported on
[0, eT*] — exactly the Levinson/Jensen zero-capacity height of PW_a against
N_sm. (ii) *Marginal law*: f(t) = ln λ(full)/λ(minus t) ≈ (π²/2)·ln(eT*/t) for
t ≲ 0.6 eT* (measured to 1–4%), with (π²/2) precisely the Landau–Widom/
Bonami–Karoui exponent unit (LW: JMAA 77 (1980) 469–481, count
(2c/π) + (1/π²)ln((1−ε)/ε)ln c; BK: ACHA 42 (2017) 1–20, profile
λ_n ~ ½exp(−π²(n+½)/2 ∫dt/(tE(t)²)); transcriptions in agent-prior-art.md
§3.2), softened near the endpoint consistently with a (eT*−t)^{3/2}
turning-point exponent; and E is *not* additive over zeros (~20% interaction).
My lemma set below is re-aimed at exactly these two laws plus the two-sided
envelope shape; the bulk constant b is demoted to a research-grade target.

---

## 2. Lemma candidates.

### Lemma H1 (Capacity dichotomy: eT* is the exact vanishing horizon).

**(a) Statement.** Fix the staircase Λ_sm (the same statements for any Λ with
|N_Λ − N_sm| ≤ R carry R only in the o(1)'s). Let a > 0, φ ∈ L²(I)\{0},
F = φ̂ (entire, exponential type ≤ a).

 (i) [Hard horizon — exact vanishing.] For every δ > 0 there is a₀(δ): for
 a ≥ a₀, if F vanishes at every point of Λ_sm ∩ [0, (1+δ)eT*], then φ = 0.

 (ii) [Effective horizon — smallness forces effective zeros.] There are
 absolute C, c > 0 such that: if ‖φ‖₂ = 1 and Σ_{t∈Λ}|F(t)|² = e^{−E} with
 E ≥ C a e^{2a}, then for T ∈ [T*, (1−δ)eT*] the function F has at least
 N_sm(T) − C(aT)/E·(...) — in the clean form: at least N_sm(T)(1 − o(1)) —
 zeros in [0, T]·(1 + small complex neighborhood), i.e. the smallness at the
 staircase points below capacity is realized by genuine zeros nearby.

 (iii) [Tail is asymptotically free.] E_{Λ}(a) ≤ E_{Λ∩[0,eT*]}((1−ρ(a))a) + C a
 with ρ(a) → 0 — deleting the entire supercritical tail changes the exponent
 only by the cost of a vanishing fraction of support. (Aspirational sharp
 form: E_Λ = E_{Λ∩[0,eT*]} + O(a).)

**(b) Proof strategy.** (i) is classical bookkeeping: a nonzero F ∈ PW_a has
real-zero density at most a/π in the Polya/Levinson sense (Levinson, *Gap and
Density Theorems*, AMS Colloq. 26 (1940); Koosis, *The Logarithmic Integral*),
while N_sm((1+δ)eT*) = (a/π)·(1+δ)eT*·(1 + ln(1+δ)/(2a+1)) exceeds the budget
for a ≥ a₀(δ); Jensen's formula on disks |z| ≤ T with the L²-normalization
controlling ln max|F| ≤ aT + O(ln a) closes it with explicit constants.
(ii) is a quantitative Rouché/Turán step: partition [T*, T] into blocks
carrying ~m := ⌈ln T⌉ staircase points each; on a block where F has fewer than
(1−η)m zeros, the Turán lemma of Nazarov (St. Petersburg Math. J. 5 (1994);
also the Turán-type estimates in Havin–Jöricke, *The Uncertainty Principle in
Harmonic Analysis*) bounds min-over-the-block from below by
(block width/spread)^{power} × sup, contradicting |F(t_k)|² ≤ e^{−E} once E
exceeds the stated threshold; summing blocks gives the count. (iii) upper
construction: take the head-minimizer φ_h on the slightly shorter interval
(1−ρ)a, multiply its transform by a Beurling–Malliavin corrector of type ρa
built for the admissible majorant w(t) = (E/2 + ln t)·1_{t>eT*} — the
log-integral ∫w/(1+t²) ≈ E/(2eT*) = b(2a+c₀)/(4πe) + o(1) is *linear in a*,
so the BM density it consumes is a constant fraction ρ∞ of a; quantitative BM
as in Makarov–Poltoratski (Beurling–Malliavin theory for Toeplitz kernels,
Invent. Math. 180 (2010); and *Meromorphic inner functions, Toeplitz kernels
and the uncertainty principle*, in Perspectives in Analysis, 2005).

**(c) Hardest missing step.** In (ii): Turán–Nazarov constants degrade with
the number of block zeros as (spread)^{#zeros}; keeping the loss per block at
O(m ln m) — so the total stays o(E) rather than O(E) — needs the graded local
near-AP structure of the staircase (locally equal spacing), i.e. a Turán
lemma with *lattice-adapted* constants. In (iii): making ρ(a) → 0 (the naive
BM budget gives only ρ = const, hence a constant-factor loss in the exponent);
the fix must let the tail-damping ride on the head product's own decay — this
is where the measured 20% non-additivity lives.

**(d) Difficulty.** (i): days. (ii): weeks–months. (iii) with ρ = const:
weeks; with ρ(a) → 0: months.

**(e) Numerical stress test first.** (1) Verify the horizon at *fixed a*
against basis effects: recompute RUN-4-style worths at L = 2.485 for zeros at
t = 59.2·(1 ± 0.1) with doubled Gcut and m — worth beyond eT* should stay
< 0.05 (already measured out to γ = 746; the test is the (1+δ)-window).
(2) Zero-tracking: compute the true-form minimizer's φ̂ on [0, 1.2eT*] at
L = 2.485 (m = 64) and count its real zeros against N_sm(T) — H1(ii) predicts
the count tracks N_sm(T) up to T ≈ (1−δ)eT* and stalls at ≈ (a/π)T beyond;
the keyhole data (RESULTS.md, nodes at the zeros with two extra non-zero
nodes at 7.64, 13.655) is a partial confirmation at L = 3.2 and this makes it
quantitative.

### Lemma H2 (The marginal law is a rank-two identity plus a one-point
profile bound; the π²/2 as a lattice-defect potential).

**(a) Statement.** Fix Λ (staircase), t₀ ∈ Λ ∩ (0, (1−δ)eT*], and let Q, Q₋ be
the frame forms with and without ±t₀; v_c, v_s ∈ L²(I) the cosine/sine
components of e_{t₀} on I; λ = λ_min(Q), λ₋ = λ_min(Q₋) with normalized
eigenvector ψ₋, spectral gap g₋ = λ₂(Q₋) − λ₋.

 (i) [Exact removal identity, unconditional in the model.] λ is the smallest
 root of the 2×2 secular equation det(I − 2 G(λ)) = 0,
 G(λ)_{ij} = ⟨v_i, (Q₋ − λ)^{−1} v_j⟩, i, j ∈ {c, s}; consequently, whenever
 2(|⟨ψ₋, v_c⟩|² + |⟨ψ₋, v_s⟩|²) =: 2|ψ̂₋(t₀)|²_pair ≤ g₋/4,

  ln(1 + 2|ψ̂₋(t₀)|²_pair/λ₋) − C·(2|ψ̂₋(t₀)|²_pair/g₋)
   ≤ f(t₀) := ln(λ/λ₋) ≤ ln(1 + 2⟨v, (Q₋ − λ₋)^{−1}v⟩-form bound),

 i.e. the measured worth f(t₀) equals ln(1 + 2|ψ̂₋(t₀)|²/λ₋) up to explicit
 gap-controlled corrections. (All quantities computable in the existing
 pipeline.)

 (ii) [Defect-profile bound — the actual content of (π²/2)ln(eT*/t₀).] The
 constrained minimizer's transform at its freed frequency satisfies

  |ψ̂₋(t₀)|² / λ₋ = (eT*/t₀)^{π²/2 + o(1)},  t₀ ≤ (1−δ)eT*, a → ∞.

 Equivalently (via (i)): f(t₀) = (π²/2)(1+o(1)) ln(eT*/t₀). Target two-sided
 version: exponent in [π²/2 − ε(δ), π²/2 + ε(δ)].

**(b) Proof strategy.** (i) is finite-dimensional spectral perturbation
(Schur complement on the rank-two update; eigenvalue interlacing supplies the
unconditional two-sidedness) — an exercise, but the *right* exercise: it
converts the measured marginal law into a pointwise statement about one
extremal function, which is what canonical-product methods can reach.
(ii): ψ̂₋ vanishes (effectively, by H1(ii)) at all of Λ below capacity except
t₀ — an entire function of type a with a *lattice defect*. Write
ψ̂₋ = (z² − t₀²)^{-free} × canonical product over the constrained set × BM
window; the ratio |ψ̂₋(t₀)|²/λ₋ is then a ratio of logarithmic potentials:
the potential of the defect lattice minus the full lattice, evaluated at t₀.
For a locally arithmetic lattice of spacing s(t) = π/(local density), deleting
one point lets the function rise mid-gap by the classical factor: the model
computation sin(πx/s)/(π(x−t₀)/s)-type gives ln-gain = ∫_{t₀}^{eT*}
[potential mismatch density] dt; the mismatch density for the *graded*
staircase is where π²/2 must come from — the same integral that produces the
(1/π²)ln((1−ε)/ε) ln c term in Landau–Widom's counting and BK's π²/2 unit.
The BK profile is the flat-density instance; the lemma is its slowly-varying
generalization evaluated in the *defect* (rank-one) direction rather than in
the bulk (which is what fails per law-theory §2.2).

**(c) Hardest missing step.** The mid-range plateau: proving the potential
mismatch integrates to exactly (π²/2)ln(eT*/t₀) — with the constant, not just
the shape — requires the local-to-global gluing of gap potentials with errors
summable over ~e^{2a} gaps; the known BK two-sided bounds (their Cor. 3,
A(n,c)-corridor) are for the flat case and their corridor is too wide for the
constant; a new equilibrium-measure computation for the graded lattice with
one defect is needed. Non-additivity (20%) warns: the o(1) in (ii) is *not*
uniform in simultaneous deletions — the lemma must stay strictly marginal.

**(d) Difficulty.** (i): days. (ii): months (constant included); the shape
(f ≍ ln(eT*/t₀) with π²/2 in a corridor [4, 6]): weeks.

**(e) Numerical stress test first.** The decisive same-day test of (i): at
L = 2.485, delete γ at t₀ = 20.7 (staircase), compute ψ₋, λ₋, g₋ in the
existing law-theory frame builder, and check
f(t₀) = ln(1 + 2|ψ̂₋(t₀)|²_pair/λ₋) to the gap-correction accuracy — this
validates the whole rank-two mechanism before any asymptotics are attempted.
Then profile: |ψ̂₋(t₀)|²/λ₋ vs (eT*/t₀)^{π²/2} at the nine measured (t, L)
combinations. If (i) fails at the 20% level, the gap assumption is bad and
the secular equation must be solved directly — still finite-dimensional.

### Lemma H3 (Two-sided envelope sandwich: canonical-product upper bound with
shared suppression; Jensen–Turán lower bound).

**(a) Statement.** For the staircase Λ_sm (and any R-rigid Λ, R entering only
the constants), there exist explicit 0 < b₁ ≤ b₂ and c₁, c₂ such that for
a ≥ a₀:

  b₁ · a e^{2a} · (1 − C/ln a) ≤ E(a) ≤ b₂ · e^{2a}(2a + c₂),

i.e. the exponent is ≍ a e^{2a} two-sidedly, with the upper bound carrying the
measured (2a + c₀) *shape*. Rigidity clause: if |N_Λ − N_sm| ≤ R then E moves
by at most C·R·a (offset-only — the theorem form of "rigidity enters the
offset"; the Poisson comparator, with R ~ √(local N), is consistent with its
measured 1.5–2 decade cost).

**(b) Proof strategy.** *Upper (= law-theory target P4):* test function
φ̂ = W(z) · Π_{t∈Λ, t ≤ (1−δ)eT*} (1 − z²/t²), W a prolate-type window using
the residual type budget; ‖φ‖ and the surviving Σ|φ̂(t)|² over t > (1−δ)eT*
are controlled by the logarithmic potential U(r) = ∫₀^{(1−δ)eT*}
ln|1 − r²/t²| dN_sm(t), an explicit closed-form integral for the rvM density
(this is the potential of the *full* product, so zero–zero interactions — the
measured 20% — are automatically included; per-zero accounting is provably an
overshoot and is not used). The stationary-phase reading is the law-theory
§2.4 chirp: the product's argument approximates π N_sm(r), so this ansatz and
the chirp are the same object; the potential computation prices its failure.
*Lower:* any competitor F = φ̂ of type ≤ a with Σ|F(t)|² = e^{−E}: by H1(ii)
F must have ~N_sm(T) zeros through T ≤ (1−δ)eT*; Jensen caps the total count;
the surplus needed in [T*, (1−δ)eT*] against the budget already spent below T*
forces, via Nazarov–Turán block estimates on dyadic-in-ln(t/T*) blocks, either
more zeros than type allows or |F| ≥ e^{−E_block} somewhere on the staircase,
whence E ≤ Σ E_block with Σ E_block ≍ a e^{2a}·(constants). Prior art for the
finite-section shadow of this argument: the σ_min lower bounds of
Batenkov–Demanet–Goldman–Yomdin (SIMAX 2020) and the single-exponential
cluster bounds of Kunis–Nagel (LAA 2020; ACHA 2021), which give the
worst-case-cluster version with an n ln n loss.

**(c) Hardest missing step.** The lower bound's per-block constant: generic
Turán/Vandermonde methods give exponent ≍ n ln n (here a e^{2a}·ln), one ln
too many; removing it needs the equilibrium (equally-spaced-locally) structure
— the same lattice-adapted Turán lemma as H1(c). Matching b₁ = b₂ (deriving
b = 1.51 ± .06) is beyond this lemma: law-theory's §2.2 shows every bulk
assignment fails, so the constant must come out of the defect/potential
calculus (H2's machinery integrated over the lattice) — kept out of scope
here deliberately.

**(d) Difficulty.** Upper with explicit (b₂, c₂): weeks–months (the potential
integral is elementary; the window/tail bookkeeping is BM-quantitative).
Lower at a e^{2a}·(1 − C/ln a): months. Matching constants: research-program.

**(e) Numerical stress test first.** Implement the upper-bound ansatz
literally (product × prolate window; the law-theory exact-Bessel builder
evaluates it) at L = 2.485, 2.996: record E_ansatz vs measured E (21.8, 33.1)
and vs the law's (2a + c₀)-shape; scan δ ∈ [0.02, 0.3] — H3 predicts an
interior optimum δ* (the turning-point standoff), and E_ansatz/E → const as L
grows. If E_ansatz misses by a *growing factor*, the chirp/product picture is
wrong and the upper strategy needs redesign — cheapest possible kill test for
the whole H1–H3 mechanism.

### Lemma H4 (Structure: exact dilation covariance; the Krein/de Branges home;
the capacity edge as a turning point).

**(a) Statement.** Three parts, in increasing depth.

 (i) [Dilation covariance — exact.] For every β > 0:
 λ_{a, βΛ} = β^{−1} λ_{βa, Λ}. (One change of variables; verified numerically
 in the repo to 2×10⁻¹⁵.) Combined with the measured β-linearity of E + A at
 fixed a, this pins the two-variable structure E(a; β) and *derives the
 conductor-universality shape* T*_χ = (2π/q)e^{2a}: for real characters the
 zero density is the β = 1/q member of the same family, so one decay constant
 in T*_χ with conductor in the offset is forced, not empirical.

 (ii) [Screw-function bridge — identity level.] With g the Krein screw
 function of ζ in Suzuki's normalization (arXiv:2606.09096), the truncated
 Weil form Q_L is, after the ledger's normalization, the [0, 2a]-section
 quadratic form of the Krein kernel G(t, s) = g(t−s) − g(t) − g(−s) + g(0),
 and λ(L) is comparable to λ_min of that section with explicit Jacobian
 factors. Hence the certified 35-decade ladder *is* a measurement of the
 degeneration rate of the Krein-positivity sections of g_ζ, and the envelope
 constants (A, b, c₀) are spectral data of the (conjectural) canonical system
 behind g_ζ (Krein; de Branges, *Hilbert Spaces of Entire Functions*, 1968;
 Romanov, Canonical systems and de Branges spaces, arXiv:1408.6022).

 (iii) [Turning-point reading of the capacity edge.] For the canonical system
 with spectral measure Σδ_{±t_k} (staircase), the Weyl/WKB turning point of
 the transfer matrix at spectral parameter t sits at the support coordinate
 x*(t) = π N'_sm(t) = ½ ln(t/2π); the support edge x = a maps to T*, and the
 defect-worth profile of H2 acquires an Airy zone at the capacity edge —
 predicting the measured (eT* − t)^{3/2} softening and, quantitatively, that
 the softened zone *narrows in relative terms* as a grows (see Prediction P2).

**(b) Proof strategy.** (i): substitution x → βx in the frame form; the
β-linearity of E + A is then a one-parameter statement about the staircase
family alone. (ii): integration by parts twice against the ledger identities
of PROGRAM.md §6; the only care is Suzuki's normalization dictionary — this
is bookkeeping, and one numerical cross-check at L = 2.485 against the
pipeline settles the Jacobian. (iii): Liouville–Green analysis of the
canonical system with slowly varying point-mass density; the Airy model at
the turning point is standard for strings with regular density; the content
is transporting it to the *inverse* side (measure given, Hamiltonian
asymptotic) — Gesztesy–Simon A-amplitude / continuum-limit tools are the
plausible route for the leading order.

**(c) Hardest missing step.** (iii): rigorous inverse-spectral asymptotics —
the direct WKB is classical, the inverse direction (from N_sm to H(x) with
error control) is not; and for the *true* zeros this is the Hilbert–Pólya
object itself, which is exactly why only the staircase version is proposed.

**(d) Difficulty.** (i): days. (ii): days–weeks (dictionary risk only).
(iii): months for the staircase Airy-zone statement; research-program for
anything finer.

**(e) Numerical stress test first.** (ii): evaluate the screw-kernel section
numerically at one L and match λ(L) with the claimed Jacobian before writing
the proof. (iii): the edge-narrowing experiment of Prediction P2 below —
if the softened zone's relative width does not shrink with L, drop (iii) and
keep (i)–(ii).

---

## 3. Predictions.

**P1 (minimizer contribution profile — tests H1+H3 in the true form).** For
the true-zeta minimizer at L = 2.485 (T* = 21.8, eT* = 59.2; existing m = 48
spectral minimizer suffices), the per-zero shares 2|φ̂(γ_j)|²/λ satisfy:
(i) Σ over γ ≤ T* is < 10% (the covered zeros: γ₁ = 14.13, γ₂ = 21.02);
(ii) Σ over γ ∈ (T*, eT*] is the plurality — > 45%;
(iii) the single largest share sits at γ ∈ (0.6·eT*, 1.3·eT*) = (35, 77).
Falsifier: shares spread ~uniformly in γ, or dominated by γ₁, γ₂. (Consistency
anchor: 2Σ_{first 60}|φ̂(γ)|² = 3.10e−10 of λ = 3.596e−10 — 86% below
γ₆₀ = 163 — is compatible; P1 sharpens it below one capacity height.)

**P2 (capacity-edge scaling — discriminates fixed profile vs turning point,
tests H4(iii)).** Law-theory measured the half-worth point of the marginal
profile at u½ := t/T* ≈ 2.0 at both L = 2.485 and L = 2.996 (ratios 0.50 and
0.56 at u ≈ 2.0). Airy/turning-point scaling predicts the softened zone's
relative width shrinks like (a·eT*)^{−2/3}: between L = 2.485 and L = 3.4
that is a factor ≈ 0.6, moving u½ to ≈ e − 0.6(e − 2.0) ≈ 2.29. Prediction:
at L = 3.4 (T* = 34.4, eT* = 93.6), u½ ∈ [2.2, 2.5]; the fixed-profile
alternative predicts u½ ≈ 2.0 ± 0.1. Four RUN-4-style surgeries at
t/T* ∈ {1.8, 2.0, 2.2, 2.4} decide. If u½ stays at 2.0, H4(iii) is dead
(H4(i)–(ii) unaffected).

**P3 (rank-two closure — tests H2(i) with zero new theory).** At L = 2.485,
staircase, t₀ = 20.7: the measured worth ΔE = 5.277 must satisfy
e^{ΔE} − 1 = 2|ψ̂₋(t₀)|²_pair/λ₋ within the gap correction — predicted
agreement within 25% (the bottom-of-spectrum gaps in the repo's cascade data
are factors 5–30, so the correction term is subdominant but not negligible).
Falsifier at >40% forces the full secular-equation treatment and would mean
the marginal law is a many-eigenvector effect — which would also undercut the
perturbative route to π²/2.

(A cautionary non-prediction, recorded deliberately: the repo's fitted
b = 1.755 agrees with 2 ln j₀ = 1.75530 (j₀ the first zero of J₀) to four
digits — and the law-theory deformation data shows 1.755 was a degenerate-fit
parameter, with the invariant value b = 1.51 ± 0.06. The coincidence is dead
on arrival; it is kept here as the program's cleanest example of four-digit
numerology manufactured by a parameter-degenerate fit.)

---

## 4. Interfaces.

**Needs.**
- *From number theory:* rigidity budgets for the true zeros — unconditional
  Backlund-type |N(T) − N_sm(T)| ≤ C ln T, RH-conditional
  S(T) = O(ln T/ln ln T) (Littlewood), and Selberg-moment "typical S(T)" on
  windows [0, eT*] — these set the R in H1/H3's rigidity clauses and hence
  how the staircase lemmas transfer to ζ (offset shift ≤ C·R·a). Also any
  unconditional zero-gap information relevant to thinning below T*.
- *From numerical analysis:* the five stress tests of §2(e) and the three
  predictions — all runnable in the existing law-theory frame builder
  (exact-Bessel overlaps) at ≤ RUN-4 cost; plus certified Gcut-extrapolation
  discipline for anything quoted as evidence.
- *From differential geometry / canonical systems:* H4(iii)'s inverse-WKB —
  the Hamiltonian asymptotics for the staircase measure and the Airy-zone
  matching constants.

**Offers / compositions.**
- *With convex optimization (dual witnesses):* H3's canonical-product × window
  ansatz is an explicit primal family; composition: "H3 ansatz + rational
  rounding + interval Rayleigh = certified upper rungs at L = 5–6" — exactly
  the discriminating depth for the envelope-vs-Fuchs divergence flagged in
  agent-prior-art.md §7.2 (>15 decades by e^{L/2} ≈ 16–20). Conversely, SOS
  dual certificates should factor approximately as |chirp product|²; I predict
  the certificate's Cholesky profile concentrates its bandwidth at the
  x ↔ ½ln(r/2π) stationary-phase pairing — a checkable structural prior for
  Track B's certificate mining.
- *With number theory:* H2's defect-potential calculus generalizes verbatim
  to the Dirichlet staircases (density ln(qT/2π)/2π); composition with H4(i):
  a proved marginal law is automatically conductor-uniform — one lemma covers
  the family ledger's habitat.
- *With canonical systems:* H4(ii) hands them the exact spectral-measure
  object; composition: "H4(ii) bridge + their Hamiltonian asymptotics =
  (A, b, c₀) as WKB invariants" — the only visible route to the constants
  after the bulk-functional failure.
- *Standing offer:* the law-theory §2.1 AP dichotomy (tight frame vs exact
  kernel at s₀ = π/a) is a complete two-page Poisson-summation proof away
  from being a recorded lemma; I can draft it for THEOREMS.md as the exact
  calibration anchor of the whole model program. Likewise Lemma A-style
  uniform archimedean log-control extends to all GL(1) archimedean factors
  (parity shifts ψ(3/4)), giving family-uniform constants for anyone's
  lemmas.

---

## 5. Honest assessment.

The strongest objection to this program: **everything above quantifies the
frame form, which is the RH-conditional face of Q_L (or an unconditional
statement about model sequences).** The unconditional operator (R3) differs
from the frame picture precisely when RH fails, and the margin sits ~30
decades below what operator-norm perturbation of the P_I[Ψ(D) − X_L]P_I
splitting can resolve — the arithmetic cancellation that makes UPT true (if
it is true) is invisible to every tool proposed here. Proved in full, H1–H4
would: turn the envelope into a theorem for the density class, fix the
normalization N_p that UPT must divide out (the program's own stated need
after §2.15), constrain every Hilbert–Pólya candidate through its counting
function and rigidity class, and derive the family universality — but they
would not prove positivity of anything unconditional. That is a real and
possibly permanent ceiling of this seat.

Secondary risks, stated plainly. (1) The lower-bound technology (Turán–
Nazarov/Vandermonde) may stall at a e^{2a}·ln — a publishable sandwich with a
log gap, not the law. (2) H2's π²/2 could be a mid-range plateau the way
1.755 was a degenerate fit; the constant is measured at 9 points over one
decade of ln(eT*/t) — the defect-potential derivation must *predict* the
next decade, not fit it. (3) The 20% non-additivity is the elephant: my
potential-theoretic accounting is additive at leading order, and if the
interaction term grows with a rather than staying at a fixed fraction, the
entire per-defect calculus caps at an upper-bound tool. (4) H4(iii) may be
this seat's version of the recurring failure mode PROGRAM.md warns about —
restating the hard object (the true Hamiltonian) in more elegant coordinates
and mistaking the restatement for progress; it is scoped to the staircase
measure for exactly that reason.

---

## Round 2 — honing (harmonic analysis)

Written after reading SYNTHESIS.md and the cited sections of
PLAN-differential-geometry.md and PLAN-number-theory.md (independence rule
lifted by the coordinator). One correction below is substantive and is owed
to this seat's own Round-1 error.

### (a) Response to the merged statement T1 (accept/restate): RESTATE — T1(i)
as written is FALSE, and the error is mine.

SYNTHESIS §3, T1(i) reads: "for a ≥ a₀, F cannot vanish on all of
Λ_sm ∩ [0, (1+δ)eT*]" — copied from my H1(a)(i). **This statement is false
for every finite horizon, at eT* or anywhere else**, by an explicit
construction:

> **Counterexample (kills T1(i)/H1(i) as literally stated).** Let T̃ > 0 be
> arbitrary, K = #(Λ_sm ∩ (0, T̃]), P(z) = Π_{k≤K}(1 − z²/t_k²) (degree 2K,
> exponential type 0), and ĥ(z) = (sin(az/M)/(az/M))^M with M = 2K + 2 (type
> exactly a, |ĥ(x)| ≤ min(1, (M/(a|x|))^M)). Then F = P·ĥ is entire of type
> ≤ a, F ∈ L²(ℝ) (|F(x)| = O(|x|^{−2})), so by Paley–Wiener F = φ̂ with
> 0 ≠ φ ∈ L²[−a, a], and F vanishes on all of Λ_sm ∩ [−T̃, T̃]. A finite set
> of linear conditions never forces φ = 0.

What is true — and what the three seats actually measured — is a
**two-horizon** structure, which DG's own plan already had right (DG-2(a)2–3:
"dodges ordinates only while aT/π ≥ N(T), i.e. up to at most e·T*"; "cannot
vanish on the quantiles beyond e²T*" — the Jensen budget): the synthesis
merged my mislabeled "hard horizon" with DG's count horizon and attached the
hard claim to the wrong height. Restated target, proposed as the corrected
T1:

> **T1′ (Two-Horizon Capacity Theorem).** Let Λ be symmetric with
> |#(Λ∩(0,T]) − N_sm(T)| ≤ R for all T. Then:
> (i) [count horizon eT* — variational] D(T) = (a/π)T − N_sm(T) has its
> unique positive zero at eT*·(1 − O(e^{−2a})), is positive before and
> negative after (calculus identity; D(eT*) = −7/8 exactly). Consequently
> any F ∈ PW_a vanishing on Λ ∩ (0, T̃] with T̃ > eT* carries real-zero
> EXCESS n_F(T̃) ≥ 2N(T̃) > (2a/π)T̃ — possible only by borrowing zeros
> against a subsequent zero desert (quantified in (b), Corollary 2); the
> MINIMIZER does not borrow: its worth support ends at eT* (law-theory
> RUN 4) and its node census saturates the budget (DG-2(e)). The
> worth-support half is a theorem-target of type H1(iii)/T4, months.
> (ii) [hard horizon e²T* — anchored Jensen; days] Under the anchor
> hypothesis (H3) below, F ∈ PW_a, ‖φ‖₂ = 1, vanishing on Λ ∩ [−T̃, T̃]
> forces ln(T̃/2π) ≤ 2a + 2 + ε(a) with ε explicit (proof in (b)). Without
> an anchor/mass-location hypothesis no hard horizon exists at ANY height
> (the counterexample above, normalized, pushes its L²-mass beyond T̃).
> (iii) [tail-freeness] as in H1(a)(iii), unchanged.

Consistency checks the corrected form passes and the old form fails:
DG's measured stopping heights T_s = 3.03–3.39·T* and C4's saturation value
e^{w∞} = 3.59·T* lie BETWEEN the horizons e·T* = 2.72T* and e²T* = 7.39T* —
the minimizer descends past eT* (no hard wall there) yet never approaches
e²T*. The law-theory worth endpoint (≈ eT*) and DG's Jensen ceiling
(52.7e^{ℓ} = 2π(e²+1)e^{ℓ}, from the e²-horizon) both sit exactly where T1′
puts them. Ownership note: the corrected hard horizon (ii) is DG's DG-2(a)3
upper bound; my contribution is the explicit-constant proof, the anchor
hypothesis made explicit, and the counterexample showing it is necessary.
NT's role is unchanged (constants for the R-clause; corollary below).

### (b) Fullest proof sketch of the days-scale part (corrected): the hard
horizon at e²T*, with explicit constants.

**Theorem (anchored hard horizon).** Let a ≥ 1/2, and let Λ = {±t_k} with
t_1 ≥ 2π satisfy the rigidity bound |#(Λ ∩ (0,T]) − N_sm(T)| ≤ R for all
T > 0. Let φ ∈ L²(ℝ), supp φ ⊂ [−a, a], ‖φ‖₂ = 1, F = φ̂. Assume:
 (H2) F(t) = 0 for every t ∈ Λ ∩ [−T̃, T̃], where T̃ = 2πe^{τ}, τ ≥ 2a + 2;
 (H3) [anchor] there is x₀ with |x₀| ≤ 2π and |F(x₀)| ≥ e^{−κa}.
Then
 τ ≤ 2a + 2 + ε, ε := [κa + ½ln(2a) + (2R + C₀)(2a + 3) + (2a+3)²]·e^{−(2a+2)},
with C₀ ≤ 10 absolute. (At a = 1.5, R = 3: ε ≤ 0.31; ε = O(a²e^{−2a}) → 0.
At the measured a = 0.62 the bound is vacuous-to-weak (ε ≈ 1.1) — this is an
asymptotic theorem, honest about its onset.)

**Proof sketch, every invocation named.**

*Step 0 (normalization and the two classical inputs).* By Paley–Wiener
(Boas, *Entire Functions*, Academic Press 1954, Theorem 6.8.1), F is entire
of exponential type ≤ a, and by Cauchy–Schwarz on [−a, a]:
 |F(z)| ≤ ‖φ‖₁ e^{a|Im z|} ≤ √(2a)·e^{a|Im z|}.  (0.1)
Jensen's formula (Boas §1.2; Levin, *Distribution of Zeros of Entire
Functions*, AMS Transl. 1964, Ch. I): for G entire, G(0) ≠ 0, R_J > 0:
 ∫₀^{R_J} n_G(s)/s ds = (1/2π)∫₀^{2π} ln|G(R_J e^{iθ})| dθ − ln|G(0)|. (0.2)

*Step 1 (recenter at the anchor).* Set G(z) = F(x₀ + z); G(0) = F(x₀) ≠ 0 by
(H3). Every point ±t_k with t_k ≤ T̃ is a zero of G at distance
|±t_k − x₀| ≤ t_k + 2π. Take R_J = T̃ + 2π. Then, keeping only the known
zeros (n_G counts all zeros in |z| ≤ s; each known zero at distance d
contributes ln(R_J/d) ≥ ln(R_J/(t_k + 2π))):
 ∫₀^{R_J} n_G(s)/s ds ≥ 2 Σ_{t_k ≤ T̃} ln( R_J / (t_k + 2π) ).  (1.1)

*Step 2 (circle bound).* By (0.1), since |Im(x₀ + R_J e^{iθ})| = R_J|sin θ|
and (1/2π)∫₀^{2π}|sin θ|dθ = 2/π:
 (1/2π)∫ ln|G(R_J e^{iθ})|dθ ≤ ½ln(2a) + (2/π) a R_J.  (2.1)

*Step 3 (the rvM Jensen mass — exact closed form).* Write the sum in (1.1)
against the smooth density and control the two replacements:
 (3a) shift removal: ln((t_k+2π)/t_k) ≤ 2π/t_k, and Σ_{t_k ≤ T̃} 1/t_k ≤
 ∫₀^{T̃} dN_sm/s + R/t₁ ≤ τ²/(4π) + C; total loss ≤ τ²/2 + C′.
 (3b) rigidity removal: replacing the sum over Λ by ∫₀^{T̃}ln(T̃/s)dN_sm(s)
 costs ≤ 2R·sup_s ln(T̃/s) ≤ 2Rτ by summation by parts against the monotone
 weight ln(T̃/s) (both endpoints controlled; the weight vanishes at s = T̃).
 (3c) the exact integral: with s = 2πe^u, dN_sm = (1/2π)ln(s/2π)ds = u e^u du:
  2∫ln(T̃/s)dN_sm = 2∫₀^{τ} u(τ − u)e^u du = 2[e^{τ}(τ − 2) + τ + 2],
 an identity (verified symbolically and numerically this session; it is
 DG-2(a)3's (R/π)(ln(R/2π) − 2) plus the lower-order terms). The nonexistent
 staircase points below t₁ = 2π·e^{0.81}-ish that the integral invents cost
 ≤ 2∫₀^{u₁}u(τ−u)e^u du ≤ 2u₁²e^{u₁}τ ≤ C₁τ, absorbed into C₀.

*Step 4 (assemble and conclude).* Chain (1.1) ≤ (0.2) = (2.1) − ln|G(0)|,
apply (H3), and use R_J = T̃ + 2π ≤ T̃(1 + e^{−τ+1}):
 2e^{τ}(τ − 2) ≤ (2/π)aT̃ + κa + ½ln(2a) + 2Rτ + τ² + C₀τ
and (2/π)aT̃ = 4a e^{τ}, so
 2e^{τ}(τ − 2 − 2a) ≤ κa + ½ln(2a) + τ² + (2R + C₀)τ.
If τ ≥ 2a + 2 + ε the left side is ≥ 2e^{2a+2}ε; solve for ε. ∎

**Corollary 1 (true zeta ordinates, unconditional).** For Λ = the true
ordinates {±γ}: R may be replaced by the running bound R_S(T̃) =
0.112 ln T̃ + 0.278 ln ln T̃ + 2.510 (Trudgian's |S(T)| bound, the citable
form in PLAN-number-theory §NT-2/interfaces; Backlund's classical version
suffices for the shape). Then 2R_S τ ≤ Cτ² and the same conclusion holds
with (2a+3)² promoted to C(2a+3)². **The hard horizon at e²T* is
unconditional for ζ** — no RH, no staircase model.

**Corollary 2 (the zero desert — quantitative borrowing).** If F ∈ PW_a,
anchored as in (H3), vanishes on Λ ∩ (0, T̃] with T̃ = 2πe^{2a+1+s},
s ∈ (0, 1), then for every ρ ≥ τ = 2a+1+s, the Jensen mass of ALL OTHER
zeros of F in |z − x₀| ≤ 2πe^{ρ} is at most
 Slack(ρ) = 4a e^{ρ} − 2e^{τ}[(τ−2) + (ρ−τ)(τ−1)] + κa + O(τ²),
which at ρ = τ equals 4ae^{τ}[1 − (s−1+2e^{−...})/2a·…] — explicitly: the
function has essentially NO zero budget left in the annulus
2πe^{τ} ≤ |z| ≤ 2πe^{ρ*} where ρ* solves Slack(ρ*) = 0-margin. Every zero
dodged beyond eT* is borrowed against a desert above T̃. This is the
statement DG's node census can test directly (their measured census already
shows ≤ 0.8 nodes in [59, 70] at L = 2.485 after the stop — consistent).

**Boxed gaps (what is NOT proved above).**
> **Gap 1 (the anchor).** (H3) is a hypothesis. It holds for every
> construction-competitor used in H3/T5 (their transforms are O(1) at low
> frequency by design) and is MEASURED for minimizers (low-band mass
> ~O(1)); but for a general near-minimizer it is not yet a theorem. Removing
> it needs a lower bound on sup_{|x| ≤ X} |F| with ln X = o(a)·... for
> mass-localized F — a Remez/Turán-type input, i.e. exactly the
> lattice-adapted Turán wall of H1(c)/T1(ii). Anchor placed at |x₀| ≤ 2π is
> essential to the constant: anchoring at |x₀| ~ T* costs an extra
> O(a²·e^{... }) drift in the horizon (computed this session; the loss is
> x₀·Σ1/t_k).
> **Gap 2 (sharpness of e²).** The theorem is one-sided. Whether anchored
> vanishing IS possible up to (1−δ)e²T* (i.e., e² is the true anchored
> horizon, not just Jensen's reach) requires a construction with mass held
> low — expected from the P·ĥ family with ĥ retuned, not yet done.
> **Gap 3 (onset).** ε(a) < 1 only for a ≳ 1.2 (L ≳ 4.8); in the currently
> measured window the theorem constrains nothing. Its value is structural
> (it caps DG's stopping height and C4's w∞ forever: e^{w} ≤ e²) — not
> numerical.
> **Gap 4 (local counts).** Nothing above bounds n_F(T) at a SINGLE T
> sharply (Jensen on disks localizes only at cost e: n(T) ≲ (2e/π)aT); the
> minimizer's O(log)-sharp node budget claimed in DG-2(a)2 needs more than
> Jensen — flagged to DG rather than assumed.

### (c) Does composite C3 (capacity in the de Branges chain) strengthen or
complicate this route?

Strengthens — with one mandatory correction and one dependency warning. The
correction: C3(i) inherits T1(i)'s falsity verbatim (a chain element
vanishing on the finite head always exists); C3 must be restated on the
two-horizon basis, with the Weyl-disk exhaustion claim (C3(ii)) attached to
e²T* under an anchor-type hypothesis, while eT* enters as the count/worth
horizon. Done so, the chain genuinely adds what raw Paley–Wiener cannot:
(1) a *mechanism* that distinguishes the horizons — in canonical-system
coordinates the type budget is the chain parameter via the Krein–de Branges
exact-type formula (type of E_x = ∫₀^x √(det H), Romanov arXiv:1408.6022),
and the passage oscillatory → hyperbolic (turning point) is the variational
stop at T_s ∈ (eT*, e²T*), while harmonic-measure/Jensen exhaustion is the
absolute wall at e²T* — two different geometric quantities, which is exactly
why the heights differ; (2) the Airy layer at the standoff is the P2/Q7
experiment unchanged, now pinned to T_s rather than eT* (my P2's u½-numbers
need no revision — they already bracket the measured standoff); (3) the
isometric embedding H(E) ⊂ L²(μ) is the right frame for the worth-support
half of T1′(i). The complications: the chain/PW norm equivalence (DG-1.1)
is harmless at log scale, but the ANCHOR does not transport through norm
equivalence (it is a point evaluation) — it becomes a reproducing-kernel
lower bound at low spectral parameter, one extra lemma; and C3 depends on
DG-1's normal form actually being constructed for μ_sm, which my PW proof
does not need. Recommendation: keep the Paley–Wiener proof of (b) as the
primary artifact (it is self-contained and Lean-adjacent in structure —
Jensen + explicit integrals + two classical bounds), let C3 be the
structural home it lands in, and let the chain version carry the turning-
point/Airy refinements that PW methods cannot state.

---

## Round 3 — status (T1′ taken to paper grade)

2026-07-26, per coordinator assignment. Deliverable:
**results/experts/T1PRIME.md** — complete referee-level proof of the Hard
Horizon Theorem (anchored Jensen at e²T*), superseding Round 2(b)'s sketch.
Deltas against the sketch worth recording here:

1. **Constants sharpened, onset caveat withdrawn.** Two proof improvements
   (the ±t_k pair-product bound, which eliminates the anchor-shift loss
   entirely, and a Fubini/layer-cake identity replacing the summation-by-
   parts bookkeeping) shrink ε from the sketch's O(a²)e^{−2a} with large
   prefactor to ε* = [B + 2R(2a+1)]/(2(e^{2a+2} − R)): numerically 0.117 at
   a = 0.62 with (R, κ) = (½, 1), and ε*_ζ ≤ 0.57 at every program window.
   The Round-2 claim "vacuous below a ≈ 1.2" is withdrawn — the theorem
   bites at all measured supports, unconditionally for ζ (Trudgian R = D₀
   via NT's Lemma R1, cross-checked to their printed digits).
2. **Gap disposition:** Gap 1 (anchor) → formal Hypothesis A, open for
   minimizers (the lattice-Turán wall), κ-calibration task assigned; Gap 2
   (sharpness of e²) → stated conjecture with construction route; Gap 3
   (onset) → resolved; Gap 4 (local counts) → open, unneeded, still with DG.
3. **Lean path is short:** local mathlib (@520045ab14) already has Jensen's
   formula (`AnalyticOnNhd.circleAverage_log_norm`) and Jensen's inequality
   (`AnalyticOnNhd.sum_divisor_le`); the staircase Theorem 1 + Corollary 2
   decompose into ~10 lemmas of ≤ a few days each (~2–3 weeks total); only
   the ζ-corollary is blocked (no formalized RvM/S(T) anywhere — months,
   external). Full gap-map in T1PRIME.md §7.
4. **Data:** the eleven deep-windows stopping heights all sit strictly
   inside (e·T*, e²·T*) with ≥ 0.14 margin (consistency, not proof — the
   variational horizon remains a months-scale target via T4/H1(iii)).

