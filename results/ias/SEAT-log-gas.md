# SEAT: log-gas / Coulomb gases and rigidity (statistical physics)

Round 1, 2026-07-26. Independence rule observed: no other `results/ias/SEAT-*.md`
was read. Sources: PROGRAM.md §§2.14–2.20, ENVELOPE.md, results/RESULTS.md,
THEOREMS.md, RH-LEMMA-MAP.md, results/experts/SYNTHESIS.md (incl. errata + §5
kill list), results/agent-law-theory.md (+ its `law_core.py`, reused here),
PLAN-harmonic-analysis.md and PLAN-number-theory.md / PLAN-differential-geometry.md
(only their pre-registered GUE-point bands, quoted in §5), src/ instruments.

Honesty tiers used throughout: THEOREM / COMPUTED / CONJECTURE / SPECULATION.

---

## §0 Seat card

Toolkit: 1D log-gases and Sine_β (DLR, screening, Leblé–Serfaty energies);
number variance and hyperuniformity classes (Torquato I/II/III); number
rigidity and tolerance of point processes (Ghosh, Ghosh–Peres, DHLM);
extreme-value statistics of log-correlated fields (FHK, GMC, freezing);
deficiency/hole probabilities (Jancovici–Lebowitz–Manificat, sine-kernel gap
determinants); Landau–Widom / Bonami–Karoui plunge spectra as the price list
of deficiencies. One sentence on this program: λ(L) is a *hyperuniformity
meter read at the capacity boundary*, and the repo has already measured its
linear-response kernel — the marginal law — without naming it that.

---

## §1 Translation into this seat's language

### 1.1 Two different electrostatics are in play; the repo's data separates them

A recurring confusion risk (and the reason "bulk prolate is dead" [SYNTHESIS
K2] coexists happily with "π²/2 is Landau–Widom" [T4]): there are two distinct
energy functionals here.

- **(i) The deterministic frame electrostatics.** λ(L) = lower frame bound of
  {e^{iγx}} on [−L/4, L/4] is a *variational, quenched* quantity of one fixed
  configuration. Its price list — worth (π²/2)·ln(eT*/t) per deleted point,
  capacity endpoint eT*, balayage identity D-surplus = deficit mass [SYNTHESIS
  errata 3] — is prolate/Landau–Widom spectral theory. It knows nothing about
  ensembles. The coefficient π²/2 is a property of the *functional*, not of
  any gas: deleting a point from a Sine_β sample changes the frame form
  identically for every β.
- **(ii) The ensemble electrostatics of the configuration.** Which
  configurations occur (Poisson, Sine₂, ζ) is governed by the point process —
  DLR equations, screening, number variance. The measured rigid/Poisson/true
  comparison (§2.17, model_zeros.py) is electrostatics (ii) *filtered through*
  the linear response of electrostatics (i).

The taxonomy question of the seat seed — "where do the ζ ordinates sit?" — is
a question about (ii); the frame-bound cost functional is (i). Their
composition is computed exactly in §1.3 below.

### 1.2 The deficiency functional: the repo's marginal law is a linear-response kernel

Write N_Γ(t) for the counting function of a configuration Γ, N̂(t) for the
Riemann–von Mangoldt staircase's, δN = N_Γ − N̂, X = e·T* the capacity height.
The measured marginal law [law-theory RUN 4: worth (π²/2)ln(eT*/t) to 1–4%,
support exactly [0, eT*]] linearizes, for any configuration of the same
density, to

  **ΔE ≡ E[Γ] − E[rigid] ≈ (π²/2) · J[Γ],
  J[Γ] := −∫₀^X δN(t) d ln t = Σ_{γ̂<X} ln(X/γ̂) − Σ_{γ<X} ln(X/γ).**  (LR)

Checks that this is the right reading (all against existing repo numbers):
a deleted point at t gives δN = −1 on [t, X), hence ΔE = +(π²/2)ln(X/t) — the
marginal law verbatim; a displaced point gives the differential form
(π²/2)·δt/t — exactly NT-2's displacement license; the insertion sign and the
~20% concavity (insertions worth ~0.8× deletions [RUN 4(iv)]) bound the
second-order term. (LR) is COMPUTED-tier as a reading of RUN 4; its ensemble
consequences are CONJECTURE until §5's test.

**In log coordinates u = ln t the worth is linear: f = (π²/2)(u_X − u).** A
hole is a unit charge on a string of constant tension π²/2 anchored at the
capacity boundary. This is the balayage identity's energy reading: the
deficiency's screening cloud is spread on [T*, eT*] (NT Round-2 exact
identity), and the energy is tension × conformal distance. (Tier: the tension
picture is an intuition pump, §3.1; the identity it repackages is proved.)

### 1.3 The frame-bound cost as a functional of the variance profile (seed (a) answered)

Take Γ random, stationary in unfolded coordinates, density matched. Then (LR)
gives ⟨ΔE⟩ ≈ concavity/adaptation bias ≥ 0 (second order, small when
|δN| ≲ 1), and the realization-to-realization statistics are governed by

  **Var(ΔE) = (π²/2)² ∫₀^X∫₀^X Cov(δN(s), δN(t)) d ln s d ln t.**  (VAR)

This is the *number-variance kernel read through the weight d ln t on
[0, eT*]* — a low-frequency window: in the stationary-spectral representation
Var(ΔE) ∝ ∫ S̄(k)|ŵ(k)|² dk with w(t) = 1_{[t₀,X]}/t, whose transform
concentrates at |k| ≲ 1/t₀ ≈ 0.07 at L = 2.485. **The frame bound is a
hyperuniformity meter: it integrates the structure factor at k → 0.**
Consequences, per class:

- **Poisson** (non-hyperuniform, S̄(0) = ρ): Cov(δN(s), δN(t)) = N̂(min), so
  Var J = ∫₀^X ln²(X/s) ρ(s) ds ≈ **5.4** at L = 2.485 (quadrature in §5) —
  σ(ΔE)_lin ≈ (π²/2)·2.3 ≈ **11.5 nats**. Fluctuation-dominated AND
  bias-dominated (see §5 P5): the measured 4.5-nat cost is, on this reading,
  mostly the one-sided concavity bias — deficits cost more than surpluses
  save — not a typical linear draw.
- **Sine₂ / GUE** (hyperuniform class II: Var N(0,u] = (1/π²)(ln 2πu + γ + 1)
  + o(1), structure factor S̄(k) = |k|/2π for |k| ≤ 2π): the counting field
  keeps a *shared low-k mode* — Cov(δN(0,u], δN(0,v]) → ½Var N(0,u] for
  v ≫ u, the two-edge CLT structure — so (VAR) does NOT average out over the
  window: hand quadrature gives Var J ≈ 0.4–0.9, i.e. σ(ΔE)_lin ≈ 3–4.7
  nats. **Prediction: Sine₂ samples have a small mean cost but a LARGE
  realization spread** — the seat's distinctive, falsifiable claim (§5 P2).
- **ζ ordinates**: see next.

### 1.4 Where the ζ ordinates sit: saturated class II ≈ effective class I, with a spectral gap at ln 2

Locally (unfolded, window ≪ correlation scale) the ordinates are Sine₂
[Montgomery 1973; Odlyzko 1987]. But the number variance of ζ zeros in a
window of W mean spacings at height T follows GUE only up to W ~ ln T and
then **saturates** at Var ≈ (2/π²)(ln ln T + const) [Berry, Nonlinearity 1
(1988) 399 — semiclassical, prime-driven; consistent with Selberg's theorem
Var S(T) ~ (1/2π²) ln ln T, Selberg 1944]. The frame functional (VAR)
integrates over ~1.5 e-folds of height — i.e. over the FULL window of
N(T*) ≈ e^ℓ points — squarely in the **saturation regime**. At the measured
heights (eT* ≈ 59–100), Var S ≈ 0.06–0.07: an order of magnitude below the
Sine₂ window variance at the same count (≈ 0.5–0.6).

Sharper, and provable-shaped (LG-2 below): under the explicit formula the
fluctuation field is a prime sum, S(t) ≈ −(1/π)Σ Λ(n) n^{−1/2} sin(t ln n)/ln n
+ (tails): **the ζ deficiency field has NO Fourier content at wavenumbers
below ln 2 ≈ 0.693.** The functional's window ŵ concentrates at k ≲ 1/t₀ ≈
0.07 ≪ ln 2. The overlap is the tail of ŵ at the prime lines:

  J[ζ] ≈ −(1/π) Σ_n Λ(n) n^{−1/2} (ln n)^{−1} · Im ŵ(ln n),
  |ŵ(ln n)| ≲ 2/(t₀ ln n),

an absolutely convergent prime sum of size ~0.03–0.05 at L = 2.485, hence
|ΔE(ζ vs rigid)| ≲ 0.2 nats. Measured: 0.023 (L = 2.485), 0.157 (L = 2.996)
[model_zeros EXPECTED]. **This is why the true zeros sit at the
maximally-rigid offset: the Weil frame functional is a low-pass filter with
cutoff far below the lowest prime frequency, and Berry saturation is exactly
the statement that ζ's counting noise lives entirely at and above the prime
frequencies.** In hyperuniformity language: the ordinates are class II
asymptotically but *effectively class I (bounded variance) for any functional
supported below k = ln 2* — and the Weil form is such a functional. It also
predicts the L = 3.555 factor-6.3 anomaly (SYNTHESIS Q3) must die at large
Gcut: nothing in the low-k budget can sustain 1.84 nats. (Tier: COMPUTED
reading + CONJECTURE quantification; lemma form in §2.)

Rigidity/tolerance taxonomy (the seed's checklist), with citations
(post-2015 attributions from memory — details UNVERIFIED where marked):

- **Number rigidity**: Sine₂ is number-rigid — the count in a bounded
  interval is a.s. determined by the exterior configuration [Ghosh, PTRF 163
  (2015); UNVERIFIED volume/page]. Sine_β for all β: Chhaibi–Najnudel
  [arXiv:1804.xxxx, UNVERIFIED]; via canonical DLR: Dereudre–Hardy–Leblé–
  Maïda, Ann. Probab. 49 (2021). The ζ ordinates, conjecturally in the same
  local class, are *more* than number-rigid at accessible heights: the count
  is pinned to N̂ within ±~0.3 (saturation), not just exterior-measurable.
- **Tolerance**: given the count, positions in an interval are mutually
  absolutely continuous with Lebesgue (Ghosh–Peres-type tolerance; proved for
  Ginibre/GEF [Duke 166 (2017)], expected for Sine₂). The frame functional
  prices exactly along this split: **counts enter at (π²/2)ln(X/t) per unit —
  the rigid degrees of freedom carry the exponent; positions enter only
  differentially, (π²/2)dt/t — the tolerant degrees of freedom are soft.**
  λ(L) is, quite literally, a rigidity meter.
- **Completeness connection** (this seat's favorite prior-art item for the
  program): Ghosh's Sine₂ theorem is about *completeness of the random
  exponentials {e^{iγx}} at critical density* — the qualitative, ensemble
  version of exactly this repo's frame bound. The program's λ(L) ladder is a
  quantitative, quenched, super-critical version of that circle of results
  [Ghosh 2015; earlier: Lyons–Steif for discrete; UNVERIFIED scope]. Worth a
  citation in ENVELOPE.md's next revision.
- **Deficiency probabilities close the loop** (§3.2): for Sine₂ the
  probability of an n-point deficit in an interval is a sine-kernel Fredholm
  determinant — a product over the SAME Landau–Widom prolate spectrum that
  prices the frame-cost of that deficit. The gas and the frame use one
  currency; des Cloizeaux–Mehta / Dyson asymptotics apply to both sides.

### 1.5 What this seat says the envelope constants are and are not

The mid-range envelope E = −A + b[N(T*) + μD(T*)] is a *quenched chirp
action* — electrostatics (i) only; K2 (bulk prolate death) says its constants
are not a smoothed-density functional, and law-theory §2.0 localizes all the
smallness in the sum-vs-integral (discreteness) gap. From this seat that is
the statement: **λ's exponent is the energy of the maximally-rigid
(zero-temperature, β = ∞) configuration of the constrained density; finite-
temperature (β = 2) and infinite-temperature (Poisson) configurations pay
fluctuation costs given by (VAR), not different bulk laws.** Hence the clean
prediction structure: one deterministic envelope + ensemble-dependent offset
DISTRIBUTIONS (not offset constants). The repo's phrase "local statistics
enter only the offset" should be sharpened to "…enter only the offset's
*distribution*; rigid and ζ share the offset because both have sub-critical
fluctuations at the functional's wavenumbers."

---

## §2 Lemma / conjecture candidates

### LG-1 (Displacement–response identity; the differential marginal law)

**Statement.** Let Λ be the rigid staircase, Λ_s the configuration with the
single point at height t moved to t + s (s = o(t)). Then
E(Λ_s) − E(Λ) = (π²/2)·(s/t)·(1 + o(1)) for t ≤ (1−δ)eT*, uniformly on
compacts of the window scale; more generally d E/dγ_j = −(π²/2)/γ_j·(1+o(1))
along any monotone rearrangement with sup-displacement o(spacing).
**Route.** Hellmann–Feynman on the frame form (dλ/dγ_j = 2 d/dγ_j
|φ̂_min(γ_j)|², plus near-vanishing of φ̂_min at staircase points below the
stopping height — the latter is Groskin-validated pipeline fact) + HA's H2
rank-two secular identity for the error term. Alternatively: difference of
two marginal worths f(t) − f(t+s) with the close-pair interaction bounded by
the H2 gap corrections.
**Effort.** Weeks, mostly bookkeeping on top of T4(i). **Interfaces.** Gives
NT-2's displacement lemma its sharp constant; is the derivative form of T3;
feeds LG-3. **Kill.** §5 P3: if the CUE ensemble's ΔE does not regress on
(π²/2)J with slope ~[0.6, 1.05], the identity is not uniform enough to be a
lemma (and T3's sharp form inherits the problem).

### LG-2 (Spectral-gap rigidity: ζ pays nothing, unconditionally-shaped)

**Statement.** For every L (both fixed and growing slowly), the ζ-vs-rigid
offset obeys |E_ζ(L) − E_rigid(L)| ≤ (π²/2)|∫_{t₀}^{eT*} S(t) d ln t| + C·
(sup_{[t₀, eT*]}|S|)² + truncation, and the integral is an absolutely
convergent prime sum ≤ C′/t₀ via |ŵ_{t₀,X}(ln n)| ≤ 2/(t₀ ln n): the
deficiency functional lives strictly below the lowest prime frequency ln 2.
Inputs: smoothed explicit formula for S(t); Selberg/Trudgian moments for the
quadratic term.
**Route.** Days–weeks; classical. The only delicate point is the same
second-order control as LG-1.
**Effort.** Small. **Interfaces.** Upgrades §2.17's "density, not arithmetic"
to a theorem for ζ specifically (T3 gives the general transfer; LG-2 gives
the ζ constant an explicit prime-sum form); predicts Q3's factor 6.3 is
truncation (a falsifiable corollary: at Gcut → ∞, |offset(L=3.555)| ≤ 0.5
nats); explains the below-GUE small-gap counts' harmlessness. **Kill.** Q3's
escalation experiment sustaining the 6.3× excess kills the quadratic-term
bound (and with it the claim that saturation controls the offset at growing
L).

### LG-3 (The ensemble law: cost distribution as a functional of the structure factor)

**Statement.** For a stationary (unfolded) point process Γ of unit density
pushed through N̂^{-1}, with structure factor S̄(k): as L grows,
(a) ΔE = (π²/2)J[Γ] + B[Γ], with ⟨B⟩ ≍ κ·⟨f·Var_loc δN⟩ ≥ 0 (concavity/
adaptation bias, κ ≈ 0.1 from RUN 4(iv)'s 20% asymmetry) and B = o(J) when
sup|δN| = o(1)·... (small-fluctuation regime);
(b) Var(ΔE) = (π²/2)²∬ Cov(δN, δN) d ln s d ln t → the k → 0 window of S̄;
class II processes keep a non-decaying shared mode and have Var(ΔE) ≍ V_edge·
ln²(X/t₀)-type growth; Poisson has Var(ΔE) ≍ (π²/2)²∫ln²(X/s)ρ ds ≍ N(X);
(c) consequently the ensemble-cost hierarchy rigid ≈ ζ ≪ Sine₂-typical ≪
Poisson-typical is a hierarchy of *low-k spectral mass*, with Sine₂'s
geometric-mean cost O(1) in nats but spread Θ(√ln N(X)).
**Route.** (LR) + Campbell/spectral formulas; second order via H2. The §5
experiment is the designed validation.
**Effort.** Weeks for the model statement; months to make (a)'s error term
honest. **Interfaces.** T3's ensemble refinement; the Hilbert–Pólya
constraint table (Track E) gains a *distributional* row: any candidate
operator's ordinate ensemble must have vanishing low-k spectral mass —
i.e. hyperuniform with structure-factor gap or saturation — or it would NOT
reproduce the measured rigid-offset envelope. **Kill.** §5 P1/P2 both
failing (mean large or spread absent) kills (a)/(b) respectively.

### LG-4 (Pair-defect interaction: Fisher–Hartwig merging vs screening sharing)

**Statement.** W(t₁, t₂) := ΔE(both deleted) − ΔE(t₁) − ΔE(t₂) satisfies:
(i) at contact (adjacent staircase points), W > 0 — merging defects
superadditively (FH exponent heuristic: charges add before squaring);
(ii) at separations ≥ ~3 spacings, W < 0 with |W| a decreasing function of
separation (two screened holes share the infimum: the minimizer cannot fully
exploit both) — the mechanism behind the measured global ~20% subadditivity
[RUN 4(v), K7];
(iii) |W| → 0 as separation → e-fold scale.
**Route.** Rank-4 secular determinant (H2 machinery, two pairs); the
function-field pilot C1 gives the solvable calibration.
**Effort.** Measurement: same-day (§5 P6). Model proof: weeks. **Interfaces.**
T4/T5's shared-suppression design (the upper-bound construction must build in
exactly this W); C1. **Kill.** If W(adjacent) < 0 the FH-merging clause dies
(screening-sharing then holds at all ranges — simpler, also useful); if
W(far) > 0 the whole subadditivity reading of K7 is miscredited.

---

## §3 Intuition pumps (SPECULATION, labeled)

### 3.1 The string picture

SPECULATION (repackaging proved facts). In u = ln(t/2π), the deficiency
worth is linear with tension π²/2, anchored at u_cap = ℓ + 1: a hole is a
quark on a string to the capacity boundary; the balayage identity (surplus on
[T*, eT*] = deficit mass) is the string's flux tube made of displaced
counting measure; the (eT* − t)^{3/2} edge softening is the string going
slack at the anchor (free-boundary/Airy zone — HA-P2/C3 own the exponent).
Pair superadditivity at contact (LG-4(i)) = string joining; far subadditivity
= two strings competing for one anchor. If the free-boundary seat derives the
3/2 from an obstacle problem, the tension constant and the anchor position
should come out of the SAME calculation — that is the consistency check that
the string is real structure and not decoration.

### 3.2 The gas and the frame use one currency

SPECULATION with a computable core. For Sine₂, P(n-point deficit in an
interval of scaled length c) is a sine-kernel Fredholm minor — a polynomial
in the SAME prolate eigenvalues λ_j(c) whose plunge prices the frame-cost of
that deficit (Landau–Widom). So "cost of realizing a fluctuation" (gas) and
"value of exploiting it" (frame) are dual functions of one spectrum. A
Varadhan-type tradeoff sup_n [frame-value(n) − realization-cost(n)] would
give the *annealed* frame bound of the Sine₂ ensemble — computable now from
des Cloizeaux–Mehta/Dyson asymptotics, and testable against the low tail of
§5's CUE ensemble. If the annealed optimum is dominated by n = O(1) deficits
at the lowest heights, that explains why the measured spread (P2) is of the
same order as single-point worths.

### 3.3 FHK / glassy landscape (seed (d))

SPECULATION. −ln λ is not itself the max of a log-correlated field, but the
*fluctuation part* of the near-null subspace is FHK-adjacent: the minimizer
must choose where to spend its vanishing budget against the field δN, i.e.
E ≈ E_chirp − max over strategies of a linear functional of a (for Sine₂)
log-correlated field — an extreme-value problem of FHK type [Fyodorov–Hiary–
Keating PRL 108 (2012) 170601; leading order proved for ζ max on short
intervals, Arguin–Belius–Bourgade–Radziwiłł–Soundararajan CPAM 2019; ζ-as-GMC:
Saksman–Webb AoP 2020]. Two concrete echoes in the repo's data: (a) the
cascade / near-degenerate Rayleigh ladder (§2.12–2.13, staircase convergence
of low modes) is the "many near-optimal strategies" signature of a shallow
glassy landscape; (b) the stopping-height drift-then-saturation w(L) ↑ w∞ =
1.2785 (C4) has the shape of a freezing transition — the optimizer's standoff
position pins at a boundary exactly when the mid-range slope crosses the
universal 4π (L ≈ 4.32). A cheap residual test exists: the true-ζ envelope
residuals at the five windows should correlate with the computable prime-sum
J[ζ](L) of §1.4; the measured residuals (±0.02–0.04 [law-theory §3.5]) are
already at the size (π²/2)J[ζ] predicts. If someone extends the window count,
this is the first place quenched "arithmetic disorder" would show as
log-periodic structure around the envelope.

### 3.4 β as a knob nobody has turned

SPECULATION, testable someday. Sine_β number variance scales like
(2/π²β)·ln [Valkó–Virág circle; UNVERIFIED constant]. Under LG-3, the
frame-cost spread of Sine_β samples scales like √(2/β) × the Sine₂ value,
while the *mean* cost stays O(1): β interpolates Poisson (β → 0, spread and
bias blow up) → GUE (β = 2) → rigid (β = ∞, spread → 0 at rate... the
crystallization limit). A three-point β-scan (β = 1, 2, 4 via G/C/S-ensembles)
would measure the exponent of the spread law and pin the (VAR) kernel with no
new theory. If the program ever needs to *prove* that only maximal rigidity
is compatible with the measured envelope offset, the β-scan is the data that
turns "the zeros are at the rigid offset" into "the zeros are at the β = ∞
offset of a one-parameter family" — a much stronger Track-E constraint.

---

## §4 Cross-seat bets (ranked by confidence)

1. **free-boundary** (conf. 0.8): the capacity endpoint eT*, the balayage
   identity, and the (eT*−t)^{3/2} marginal-worth softening all come out of
   ONE obstacle problem for the deficiency measure in u = ln t coordinates;
   the 3/2 is the generic free-boundary/contact exponent. Bet: they write the
   obstacle problem whose contact set ends at eT* within Round 2, and the
   string tension π²/2 appears as their Lagrange multiplier.
2. **riemann-hilbert** (conf. 0.7): the marginal-law constant π²/2 is
   derivable by their machinery as the Bonami–Karoui/LW exponent unit (T4's
   route), AND the full distribution of the Sine₂ frame cost (my §5 P2) is in
   principle a Fredholm/Painlevé-V computation with one FH singularity — if
   they confirm the spread scale ~3–4 nats analytically, LG-3(b) graduates to
   THEOREM-track in the model.
3. **quantum-chaos** (conf. 0.65): Berry's saturation formula (with its prime
   sum) quantitatively reproduces the ζ-vs-rigid offsets measured at all
   L ≤ 4 (|offset| ≤ 0.3 nats), i.e. their Var_sat(T) plugged into (VAR)
   matches LG-2's prime-sum bound term by term — the two seats' formulas
   should be literally the same object through the explicit formula.
4. **quasicrystal** (conf. 0.45): the rigid staircase is bounded-remainder-
   like and they will connect λ_rigid to crystalline-measure/model-set frame
   theory (Matei–Meyer line); the sharp statement worth wanting from them:
   the ζ ordinate set, though not Meyer, is "effectively bounded-remainder
   below wavenumber ln 2" — same gap as §1.4, in their language.
5. **renormalization** (conf. 0.3, SPECULATION-grade): the L ≈ 4.32 crossover
   (mid-range law → 4π cap; w(L) freezing at 1.2785) is a freezing transition
   of a log-correlated optimization in the FHK universality class, and RG on
   the transfer operator of the chirp map x ↦ r(x) = 2πe^{2x} reproduces the
   drift equation e^w(w−1) = (b/2π)(ℓ+c₀) − 1 [SYNTHESIS §2(iii)].

---

## §5 PRE-REGISTERED TEST: the GUE/Sine₂ point (Q6, executed with this seat's numbers)

Everything in §5.1–5.3 was written and locked BEFORE any run. The script is
`results/ias/log-gas/cue_frame_test.py`; raw output
`results/ias/log-gas/cue_frame_test.jsonl` + `run.log`.

### 5.1 Design (matches model_zeros.py EXPECTED protocol exactly)

L = 2.485, m = 48, orthonormal Legendre frame form (law_core.lam_min_frame,
dps 50), first KT = 180 points of each configuration (the EXPECTED table's
protocol), T* = 2πe^{L/2} = 21.77, X = eT* = 59.17. Reference: rigid
staircase (expect λ = 2.75124e-10); regression anchors: Poisson seed 7
(expect 2.89509e-12), true zeros from cache (expect 2.68972e-10), single
worth f(γ̂₂ ≈ 20.65) ≈ 5.28 [RUN 4]. CUE model: eigenangles of an N = 256
Haar-unitary (Mezzadri QR), sorted, u_k = Nθ_k/2π, first 180 pushed through
N̂^{-1} (same Newton as poisson_zeros) — a Sine₂ window at unit density,
correct-density chirp via N̂^{-1}, exactly DG-P3/NT-P2's proposed sampler.
Anchored variant: u ↦ u − u₁ + ½ (first point pinned to the staircase's
first quantile — kills the window-phase/edge mode). Poisson seeds 7–11.
Pair surgeries on the staircase: singles {2}, {3}, {5}, {8}; pairs (2,3)
adjacent, (2,5) mid, (2,8) far. For every configuration the script also
reports J (exact sum form of (LR)) and sup|δN| on [0, X].

Budget: ≤ 30 CPU-min, 1 worker, sequential, wall-clock guard.

### 5.2 Derivation of the numbers (hand quadratures, locked)

Var J(Poisson) = ∫₀^X ln²(X/s)ρ(s)ds ≈ 5.4 (script recomputes exactly) →
σ_lin = (π²/2)√5.4 ≈ 11.5 nats. Var J(Sine₂ window): (VAR) with the CUE/sine
covariance Cov(N(0,u], N(0,v]) = ½[V(u)+V(v)−V(|u−v|)], V(x) =
min(x, (ln 2πx + 1.577)/π²): hand value ≈ 0.7, honest band 0.4–0.9 →
σ_lin ≈ 3.1–4.7 nats; with ~15% concavity compression → predicted measured
spread ≈ 3.3 nats. Bias: κ ≈ 0.1 of ⟨f·Var_loc⟩: Poisson +3.2 ± 1.5; CUE
+0.4 ± 0.4 (+ adaptation ≲ 0.3).

### 5.3 LOCKED PREDICTIONS

- **P1 (headline, the seed's number).** Free-CUE ensemble mean (10 seeds):
  ⟨ΔE⟩ = **+0.7 nats**, acceptance band **[−0.5, +2.2]**. In λ: geometric
  mean λ_CUE ≈ 0.5 × λ_rigid — GUE/Sine₂ costs ~**0.3 orders of magnitude**
  against Poisson's measured 2.0 orders. (Consistent with NT-P2's central
  band; the disagreement is P2.)
- **P2 (the seat's distinctive claim).** Realization spread sd(ΔE) =
  **3.3 nats**, band **[2.0, 5.0]**. Corollaries: **≥5 of 10** free-CUE seeds
  land OUTSIDE DG-P3's window λ ∈ [3e-11, 3e-10]; **≥2 of 10** seeds have
  |ΔE| > 4 nats. (DG-P3 and NT-P2 read as predicting concentration inside
  ~±1–2 nats; this seat predicts the class-II shared mode makes single
  realizations scatter by ±1.5 orders. Maximum variance, as commissioned.)
- **P3 (mechanism).** Across free-CUE seeds: corr(ΔE, (π²/2)J) ≥ **0.85**;
  OLS slope ∈ **[0.6, 1.05]**; intercept ∈ **[0, +1.5]**.
- **P4 (anchoring).** sd(free)/sd(anchored) ∈ **[1.3, 2.5]** — removing the
  first-point phase removes a large coherent share of (VAR).
- **P5 (Poisson is bias-dominated).** Mean over 5 Poisson seeds ∈
  **[+1.5, +6.5]**; ≥4/5 positive; for each seed with J > 0, ΔE ≤ (π²/2)J + 2
  (concavity compresses, never amplifies); regression slope of ΔE on
  (π²/2)J over Poisson seeds < 0.85.
- **P6 (pairs, LG-4).** W(2,3) > 0, in [+10%, +70%] of min(f₂, f₃);
  W(2,5) < 0 in [−30%, −2%] of min(f₂, f₅); W(2,8) < 0 with |W(2,8)| <
  |W(2,5)|.
- **P7 (ζ spectral gap, free rider).** (π²/2)·J[true zeros] ∈ [−0.35, +0.35]
  and within 0.3 nats of the measured true-vs-rigid offset (+0.023).

### 5.4 RESULTS (appended after the run — predicted vs measured)

Run: 2026-07-26, 29 frame builds, 11 s wall, 1 worker
(`results/ias/log-gas/run.log`, `cue_frame_test.jsonl`). All three regression
anchors reproduced to printed digits: rigid 2.7512367e-10 (expect 2.75124e-10),
true 2.6897153e-10 (expect 2.68972e-10), Poisson-7 2.8950901e-12 (expect
2.89509e-12). Exact quadrature Var J(Poisson) = 5.73 (hand estimate 5.4).

Free-CUE ensemble, 10 seeds (ΔE in nats vs rigid; (π²/2)J from the realized
configuration):

| seed | λ | ΔE | (π²/2)J | seed | λ | ΔE | (π²/2)J |
|---|---|---|---|---|---|---|---|
| 1 | 1.64e-07 | −6.39 | −7.32 | 6 | 3.16e-12 | +4.47 | +3.98 |
| 2 | 4.25e-10 | −0.43 | −0.76 | 7 | 4.09e-11 | +1.91 | +1.31 |
| 3 | 6.37e-09 | −3.14 | −4.36 | 8 | 7.72e-08 | −5.64 | −5.35 |
| 4 | 1.87e-08 | −4.22 | −4.88 | 9 | 1.38e-10 | +0.69 | +0.28 |
| 5 | 4.02e-11 | +1.92 | +1.94 | 10 | 3.61e-09 | −2.57 | −3.96 |

**Scorecard (verdicts against the locked bands):**

- **P1: FAIL** (honestly scored). Measured mean ΔE = **−1.34** (SE 1.14) vs
  locked band [−0.5, +2.2]. Decomposition shows why: the per-seed bias
  ΔE − (π²/2)J has mean **+0.57 ± 0.16**, positive in 8/10 seeds — exactly
  the predicted concavity/adaptation bias (+0.4–0.7) — but the 10-seed draw
  of J itself came out at −1.9 (a ~1.6 SE fluctuation of a mean-zero
  statistic with the predicted large variance). The mean-cost *mechanism*
  is confirmed; the locked point estimate was overtaken by exactly the
  realization scatter this seat predicted in P2. N = 10 cannot resolve a
  +0.6-nat bias under a 3.6-nat spread; that is itself the finding.
- **P2: PASS, dead center** — the seat's distinctive claim. sd(ΔE) =
  **3.60** vs predicted 3.3, band [2.0, 5.0]. Sample Var J = 0.575, inside
  the locked hand-quadrature band [0.4, 0.9]. Corollaries: **7/10** seeds
  outside DG-P3's λ-window (locked: ≥5); **9/10** outside NT-P2's; **4**
  seeds with |ΔE| > 4 (locked: ≥2). Realizations span λ = 3.2e-12 to
  1.6e-07 — **4.7 orders of magnitude across ten Sine₂ samples.** "λ_GUE"
  is not a number; it is a distribution, and its spread is the class-II
  shared low-k mode. Directly confirmed: corr(u₁, ΔE) = **0.945** — the
  window phase (first-point position) alone explains ~89% of the variance.
- **P3: PASS, emphatically.** corr(ΔE, (π²/2)J) = **0.991** (locked ≥0.85);
  OLS slope **0.954** (locked [0.6, 1.05]); intercept **+0.48** (locked
  [0, 1.5]). The linear-response law (LR) with the repo's marginal-law
  kernel predicts individual Sine₂ frame costs to ~½ nat across a 12-nat
  range, from the configuration alone, with no eigensolve.
- **P4: PASS.** sd(free)/sd(anchored) = **2.43** (locked [1.3, 2.5]);
  anchored ensemble: mean +0.23, sd 1.48, bias +0.43. Pinning one point
  removes ~83% of the variance — the shared edge mode is the spread.
- **P5: PARTIAL — and the failure is the most instructive number of the
  run.** Mean over 5 Poisson seeds **+6.38** (locked [1.5, 6.5]: pass, at
  the edge); 4/5 positive (pass); regression slope 0.76 < 0.85 (pass). The
  per-seed concavity cap ΔE ≤ (π²/2)J + 2 **FAILED in 4/4 applicable
  seeds**: excesses +2.7, +6.0, +4.3, +3.7 nats (and +9.6 on the surplus
  seed 11). At Poisson amplitude the cost sits systematically ABOVE linear
  response, with intercept +5.5: I had put the saturation on the wrong
  side. Measured structure: **deficit-side amplification, surplus-side
  saturation** — seed 8 has balanced J ≈ +0.3 but supD = 4 and pays +6.3;
  seed 11 has a huge surplus (J-linear says −11.9) but recovers only −2.3.
  The infimum prices the *worst local deficit*, and surpluses elsewhere do
  not refund it. So the cost functional is J-linear only for sup|δN| ≲ 2
  (CUE regime, r = 0.99) and crosses over to an extreme-value functional of
  the deficiency field beyond — the quantitative content of seed (d)'s
  FHK question, measured.
- **P6: PARTIAL → LG-4 clause (ii)/(iii) REFUTED.** Singles reproduce the
  marginal law (f₂ = 5.31 vs LR 5.19; f₅ = 2.78 vs 2.79; f₈ = 0.78 vs 1.46
  — ratio 0.53 at u ≈ 2.0, matching RUN 4's independent edge-softening
  measurement 0.50 on a different instrument). Pairs: W(2,3) = **+0.52**
  (+12% of the smaller worth — inside the locked [+10%, +70%]: contact
  clause (i) PASSES), but W(2,5) = **+0.61** and W(2,8) = **+0.84**:
  positive and GROWING with separation toward the capacity edge. The
  screening-sharing negative regime does not exist at pair level at this L.
  Revised reading in §6.
- **P7: PASS.** (π²/2)J[ζ] = **−0.071** (locked |·| ≤ 0.35), within 0.094
  of the measured true-vs-rigid offset +0.023. The ζ configuration's
  deficiency functional is ~50× smaller than the typical Sine₂ draw —
  the spectral-gap/saturation mechanism of §1.4 in one number.

**Headline answer to the seed-(a) question** (as measured, replacing P1's
failed point form): relative to the rigid staircase at L = 2.485, GUE/Sine₂
ordinates cost **+0.5 nats in systematic bias (the concavity/adaptation
term, +0.57 ± 0.16 measured against the locked +0.4–0.7) and ±3.6 nats
(±1.6 orders) per realization**, against Poisson's ≈ +5.5-nat bias with
±7-nat scatter, and ζ's ≈ 0 ± 0.1. The correct invariant is not "the GUE
offset" but the pair (bias, Var J), and Var J is the number-variance kernel
of the ensemble read through d ln t on [0, eT*] — hyperuniformity class
enters exactly there.

---

## §6 Post-run addendum: revisions the measurements force

1. **LG-3 upgraded and corrected.** Clause (a) splits by regime:
   ΔE = (π²/2)J + B with B ≈ +0.5 ± 0.5 for sup|δN| ≲ 2 (measured r = 0.99,
   slope 0.95); for sup|δN| ≳ 3 the functional crosses over to
   extreme-value form — cost ≈ (π²/2)·(worth of the worst local deficiency
   configuration), surpluses non-refunding. The Poisson block is the
   measurement of the crossover. This one-sidedness is the finite-|δN|
   face of the infimum and belongs in any T3-adjacent transfer statement:
   **transfer bounds must be stated in terms of one-sided (deficit)
   discrepancy, not |N₁ − N₂|** — a sup-deficit hypothesis is both
   necessary (Poisson data) and sufficient-looking (CUE data).
2. **LG-4 restated (pair law).** Measured: W > 0 at all tested separations,
   growing toward the capacity edge (+12%, +22%, then +108% when the outer
   point sits in the softened zone u ≈ 2). Physics reading: deleting a
   point dilates the effective capacity budget (balayage has one fewer
   charge to place — worth ≈ (π²/2)·Δu_cap ≈ +0.2–0.3), and un-softens the
   edge zone for the second deletion (f₈'s deficit 1.46 − 0.78 = 0.69 of
   softening is recovered almost exactly in W(2,8) = 0.84). The K7 global
   subadditivity is therefore a MANY-body (deletion-density) effect, not
   pairwise screening-sharing. Corrected conjecture: W(t₁, t₂) =
   capacity-dilation term + edge-rehardening term ≥ 0, with subadditivity
   appearing only at finite deletion density (fraction of the staircase
   removed) — testable by triple/quadruple surgeries at fixed density.
   T5's "shared suppression" design should share at density level, not
   pair level.
3. **The Q6 adjudication this run supplies** (for the coordinator): DG-P3
   and NT-P2 asked whether λ_GUE lands between smooth and Poisson. Answer:
   its geometric mean does (bias +0.5), but individual realizations do not
   concentrate — 7/10 and 9/10 fall outside the respective locked windows,
   with scatter ±1.6 orders driven by the window phase (corr(u₁, ΔE) =
   0.945). The DG-3 discrepancy-Lipschitz mechanism survives (costs track
   the realized discrepancy, r = 0.99); only the "GUE = one number between
   the two" reading dies. Recommended restatement for the Track-E
   constraint table: a Hilbert–Pólya candidate must produce ordinates whose
   deficiency field has (i) vanishing low-k spectral mass on [0, ln 2)
   (saturation/spectral gap — ζ's measured J = −0.014 in unfolded units)
   and (ii) sup-deficit ≲ 1 at all heights; Sine₂ sampling fails (i)
   realization-wise, Poisson fails both.
4. **What would change this seat's mind.** If the anchored-CUE spread had
   NOT dropped (P4), the edge-mode reading of the spread would be wrong; it
   dropped by 2.43×. If J had not predicted per-seed costs (P3), the whole
   linear-response frame of §1 would be dead; it predicts them to ½ nat.
   The remaining soft spot is the second-order/bias term: +0.5 ± 0.5 is
   measured, not derived — its derivation (concavity of the secular
   equation, H2 machinery) is the natural next analytic step and belongs
   to T4's owner with this seat consulting.
5. **Follow-ups worth one afternoon each**: (i) repeat the free-CUE block
   at L = 2.996 to test the predicted growth of Var J with ln N(T*)
   (class-II signature: Var J up by ≈ (1/π²)ln-factor; a flat Var J would
   instead indicate the weight w d ln t, not the process, dominates);
   (ii) the β-scan of §3.4 (β = 1, 4 via tridiagonal β-ensembles): LG-3
   predicts spread ∝ √(2/β) at fixed bias; (iii) triple surgeries at fixed
   spacing to locate the onset of many-body subadditivity (revision 2);
   (iv) an anchored-CUE run with TWO pinned points (u₁ and the point
   nearest T*) — if the residual 1.5-nat spread halves again, the spread
   is entirely a boundary-mode ledger, and T3's exceptional-set analysis
   can be restricted to edge neighborhoods.

---

## Round 2 — colloquium (log-gas)

2026-07-26, after reading all eight Round-1 seat files + COLLOQUIUM-BRIEF.md.
Honesty tiers as before. New numerics pre-registered in §R2.5 BEFORE running;
§R2.5's script and raw output live in `results/ias/log-gas/`.

**The headline fact of the round for this seat**: quantum-chaos and log-gas
ran the SAME experiment independently (CUE ordinates through N̂^{-1}, L =
2.485, m = 48, K = 180 — their §5, my §5) with different unfolding/anchoring
conventions and different derivations, and measured the SAME affine law.
Dictionary: their I_w = (π²/2)∫ΔN(t)dt/t is exactly **−(π²/2)·J** in my
notation, and their Δ = −ΔE. Their regression Δ = 0.96·I_w − 0.66 (12 seeds,
anchored) IS my ΔE = 0.954·(π²/2)J + 0.484 (10 seeds, free): slopes 0.96 vs
0.95, intercepts 0.66 vs 0.48 (consistent at ~1σ; pooled with my anchored
block, B = 0.55 ± 0.10, 28 CUE samples total). An independent replication at
the 1%-slope level, before either seat saw the other's file. COMPUTED.

### R2.1 Bet responses (every bet placed on this seat)

**(a) Renormalization §4-3 + P1 (b = 3/2 ⟺ screening constant 3/π²).**
ACCEPTED as an assignment, QUARANTINED as an identification (their own K5
posture — concur). Three audit notes before the computation is attempted:
(i) *Reference-functional ambiguity is real but their numerology survives
it*: the full additive integral of the marginal law over all staircase
points below capacity is Σf → (π²/2)·e·e^ℓ(ℓ−1), so the asymptotic
screening fraction against THAT reference is b/((π²/2)e) = 0.1126, and
their b = 3/2 claim is equivalently 3/(π²e) = 0.1118 — same claim, the
capacity e-fold absorbed; against the in-band 13-zero sum at L = 2.485 the
fraction is ≈ 0.83 (law-theory's 20% overshoot). Any derivation must state
its reference or the "screening constant" is convention.
(ii) *Sign structure constraint from data*: my §5.4-P6 pairs (W > 0 at all
separations, growing toward the capacity edge) + their own block-spin
dressing (+17%/+26%, positive curvature) say short-range interactions are
SUPERadditive; the ~9× asymptotic reduction from the additive integral to
the measured E must therefore be a MANY-BODY/density effect (my §6.2), not
pairwise screening. A screened-equilibrium computation that models pairwise
negative interactions will get the sign of the dressing wrong and should be
rejected at the G(t₀) gate (see M-2, §R2.3).
(iii) Kill band pre-committed: if the equilibrium computation of M-2 returns
screening fraction outside [0.09, 0.13] of the full additive reference
(equivalently b outside [1.2, 1.75]), b = 3/2 dies; if it returns a value
inside law-theory's invariant band [1.39, 1.51] but off 3/2, the numerology
dies and the computation stands. Tier: CONJECTURE, computation owned by
this seat inside M-2.

**(b) Riemann–Hilbert §4-2 (fluctuation free energy; GUE within ~1 nat;
A′(ζ) − A′(staircase) → 0).** SETTLED IN DISTRIBUTIONAL FORM, and their
form of the kernel is exactly right: my (VAR) weight d ln t is (marginal
worth)′ dt/(π²/2) — i.e. their "number-variance kernel against the squared
g-function derivative" is (VAR) verbatim. Verdict on the wager: WON on the
geometric mean (bias B = 0.55 ± 0.10 ≈ their "~1 nat"), RESTATED for
realizations (sd 3.6 nats; single Sine₂ samples are NOT within 1 nat of
anything). Their A′-question is my LG-2: I commit the L-uniform prime-sum
bound |offset(ζ vs staircase)| ≤ (π²/2)Σ_n Λ(n)π^{-1}n^{-1/2}(ln n)^{-1}|ŵ_L(ln n)|
+ O(sup S²) — bounded uniformly in L — so A′(ζ) = A′(staircase) up to
≤ O(0.3) nats. On their RH-1(ii) p ∈ {9/2, π²/2}: one SPECULATION-grade
remark from my field — if the L ≈ 4.32 crossover is a freezing transition
(FHK class), frozen-phase log-coefficients generically shift by
3/4-type increments; p need not equal either clean candidate. Flagged only
so the L = 5.5 discriminator is read with that third possibility in mind.

**(c) Quantum-chaos B2 (three parts).** (i) Number-variance functional:
CONFIRMED and MERGED — see the replication note above and M-1 below; their
post-hoc sign lesson (frame form = sum of positive rank-ones, surplus
raises λ) is the same sign convention my (LR) carried from RUN 4, now
stated jointly. (ii) The L = 4.32 crossover as third-order
pulled-to-pushed: CO-SIGNED from this seat's side — boundary saturation of
a constrained log-gas is the Majumdar–Schehr third-order class (Majumdar–
Schehr, J. Stat. Mech. (2014) P01012, review), and C4's w-saturation IS
condensation of the dodging strategy on the wall; my only rider is that
the classification claim inherits Q1's "bend confirmed" premise. (iii)
π²/2 as single-charge extraction energy: ownership ACCEPTED jointly with
HA/T4; the free-boundary seat's G(t₀) finite sum (their FB-1) is the
cheapest adjudicator of whether the worth is a bare potential gap, and I
endorse running it before any asymptotics (minutes; it is M-2's gate).

**(d) Free-boundary §4-2.** Their Poisson pricing bet ("LIL of the
discrepancy, 4.5 nats within factor 2") resolves as: ensemble mean +6.4 ±
3.1 (5 seeds) vs their 4.5 — inside factor 2 — but the mechanism is charge
+ extreme-value, not LIL-of-|δN|: at Poisson amplitude the functional
crosses over from ⟨δN, w⟩ to worst-local-deficit (my §5.4-P5, QC's
Poisson decomposition; reconciliation in §R2.2/C-6). Their T3 bet: the
DHLM/rigidity offer stands for the ensemble version; for the DETERMINISTIC
worst case the constant is now essentially known — see M-1's corollary:
magic-functions' measured phase-transport bound 6.64 (their §5.1, D = 1,
ℓ = 1.2425) equals κ·(π²/2)·ln(eT*/t₀) = 6.59 to 1%. Their λ_GUE band
clause dies in realization form (7/10 seeds outside) — as does everyone's.

**(e) Quasicrystal §4-3 (OCP ordering; Q6 within ~2 nats of smooth).**
Mean/bias form: CONFIRMED (ordering true ≈ smooth < GUE < Poisson holds
for geometric means / intrinsic terms: 0 ≈ 0.1 < 0.55 < ~5). Realization
form: DEAD (sd 3.6). Their phason-stiffness pump (IP-2) survives with one
amendment from my data: the stiffness of an ENSEMBLE member is a random
variable dominated by the window-phase mode; "zeta at the zero-temperature
perfectly ordered point" should be sharpened to "zeta at the CHARGE-NEUTRAL
point" (I_w ≈ 0.07–0.11, β_eff = 0.5034) — see C-1, where their taxonomy's
chirp column and my low-pass functional are reconciled quantitatively.

**(f) Proof-theory B3 (extractability of the defect computation).**
ACCEPTED. The rank-two secular identity + Riemann-sum layer of the
π²/2 derivation is finite-dimensional linear algebra plus explicit
integrals — no compactness anticipated, consistent with their metatheorem
reading. Honest caveat for their ledger: the second-order term B (the
bias, 0.55 ± 0.10 for unit-variance clouds, ≈ 0.1 for near-rigid, and
NON-affine at Poisson amplitude) is currently measured-only; the
extractive layer covers the first-order law. Their certification lane is
welcome the day T4(i) lands on paper.

### R2.2 Adjudications

**C-1 (mine to own): the rigidity trichotomy is ONE scalar plus ONE
uniformity mechanism — equivalent per-L, NOT equivalent as statements.**
The exact dictionary:

  I_w(L) = −(π²/2)·J(L)  [identical functional; QC's t₀-cutoff and my
  0-cutoff agree since δN ≡ 0 below the first point];
  β_eff(L) − 1/2 = −J(L)/S(L) + O(B/((π²/2)S)),
  S(L) = Σ_{t_k ≤ eT*} 1/(t_k N̂′(t_k)) [MF's transport sum; their
  measured d ln λ/dβ = (π²/2)S at 2.5–4.5% is (LR) along the pure-phase
  direction].

Numerical check of the dictionary on the existing data (COMPUTED): MF's
β_eff − 1/2 = 0.0034 ⇒ (π²/2)S·0.0034 = 0.029 vs their measured λ-gap
0.028 at m = 24; QC's I_w(ζ) = +0.07 at L = 2.485 vs my (π²/2)J(ζ) =
−0.071 — sign conventions opposite, magnitudes identical to the printed
digit, two independent implementations. So: **worth-weighted charge
neutrality (QC) and midpoint effective phase (MF) are the same scalar
statement at each L — one is the other in different units.** The spectral
gap (LG) is strictly stronger: it bounds the WHOLE deficiency spectrum
below ln 2, hence forces |J(L)| small SIMULTANEOUSLY for every window —
neutrality at all L with one mechanism. Converse false: a configuration
with a low-frequency mode (k₀ < ln 2) phase-tuned at one window is
charge-neutral/midpoint-phase THERE but not elsewhere. That separating
example is now built and run — §R2.5 — and behaves exactly as the
trichotomy demands. One more structural remark worth recording: even the
staircase-sawtooth mismatch between N_ζ and N̂ lives at local frequencies
2πρ(t) = ln(t/2π) ≥ 0.80 > ln 2 on the measured windows, so the ENTIRE
ζ-deficiency spectrum (S(t) primes + sawtooth) clears the functional's
low-pass band — the gap statement is clean, not merely S(t)-leading-order.
**Panel answer: prove-equivalent verdict = "equivalent per-L (exact
dictionary above), inequivalent as uniformity claims; LG ⟹ (QC ⟺ MF) ∀L;
separator exhibited."** The Track-E constraint table should carry the
uniform statement (spectral gap / saturation), not the per-L scalar.

**C-5 (Q3 factor 6.3): co-signed dead as a rigidity/charge effect, with
the death certificate amended.** QC's I_w(true, 3.555) = +0.11 vs +1.84
needed, residual > 3× their scatter; my LG-2 predicts |offset| ≤ ~0.4
nats uniformly. Both verdicts are first-order; the formal death of the
ANOMALY (as opposed to its explanation) still requires the SYNTHESIS Q3
settling run (Gcut = 840/1680/3360, m = 64, both sequences — law-theory's
exact-Bessel builder makes this cheap). Pre-registered joint prediction
(LG+QC agree): the true-vs-smooth gap at L = 3.555 collapses to
|ΔE| ≤ 0.4 nats as Gcut → ∞. If it survives above 1 nat converged, LG-2's
quadratic-term bound is wrong AND the charge decomposition misses a
second-order arithmetic term — both seats' §2 candidates take damage, and
that outcome would be genuinely interesting (first visible arithmetic
beyond density+neutrality). Either way Q3 stops being folklore.

**C-6 (Poisson diligence; reconciling "above linear response" with the
charge decomposition; ENVELOPE §2b protocol).** Reconciliation first, since
the brief flags an apparent conflict: there is none — the two seats
measured the same nonlinearity from two sides. QC's "intrinsic Poisson
cost −2.0 to −2.7" is a slope-1 residual on ONE seed (7); my "+5.5
intercept" is an OLS artifact of forcing an affine law through 5 seeds
whose slope-1 residuals are +2.7, +6.0, +4.3, +3.7, +9.6 — NOT a constant.
Conclusion both seats now co-sign: **at sup|δN| ≳ 2–3 no affine law in J
exists; the cost functional crosses over to extreme-value form (worst
local deficit priced by the marginal law; surpluses non-refunding).**
"Intrinsic Poisson cost" is only well-defined charge-matched. Joint
protocol for ENVELOPE.md §2b (pre-registered numbers, run owned by QC + LG):
  (1) ≥ 12 Poisson seeds at L = 2.485 and 2.996, KT = 180, m = 48;
      report per-seed (λ, ΔE, (π²/2)J, supD).
  (2) Charge-matched intrinsic cost := mean ΔE over seeds with
      |(π²/2)J| ≤ 0.5. PREDICTION: +3.5 ± 1.5 nats at L = 2.485 (between
      QC's one-seed 2.0–2.7 and my OLS 5.5); ensemble sd ≥ 4 nats.
  (3) §2b text replaces "Poisson costs 1.5–2 orders" with: "Poisson:
      charge-matched intrinsic cost ≈ 1–2 orders; single samples scatter
      by ±2–3 orders; the recorded 2-order number is one seed of which
      roughly half is realized charge (I_w = −1.9)."
  (4) The ζ row gets stated as measured: I_w(ζ) = +0.07…+0.11 across
      L = 2.485/2.996/3.555 — worth-neutral to 0.1 nats — with the
      saturation/spectral-gap mechanism cited for uniformity.

**C-7 (ensemble ≠ number: the distributional restatement of DG-P3/NT-P2).**
Drafted for the prior panel's ledger (replaces both point predictions):

> For point processes Γ of RvM density pushed through N̂^{-1}, at
> (L, K, m) = (2.485, 180, 48): ln λ_Γ − ln λ_stair = −κ·(π²/2)J[Γ] − B[Γ]
> + ε, with κ = 0.95 ± 0.03 (two independent measurements), J the
> worth-weighted charge of the realized configuration (mean 0, variance =
> the number-variance kernel integrated against d ln t ⊗ d ln t on
> [0, eT*]²), B ≥ 0 the local-statistics bias (CUE: 0.55 ± 0.10; ζ: ≈ 0.1;
> Poisson: not affine — extreme-value regime), residual sd ≈ 0.5 nats
> valid for sup|δN| ≲ 2. Consequently λ_GUE is a DISTRIBUTION: geometric
> mean ≈ λ_stair·e^{−B}, free-window realization sd 3.6 nats; the old
> bands hold only for the charge-matched median (measured: every one of
> 28 CUE samples stayed ≥ 2.9 nats above the recorded Poisson value, so
> DG-P3's kill clause "λ_GUE at Poisson offset" remains safely un-fired).

**C-2 (one line, since I hold no w∞ claim):** this seat endorses the
cluster's statement via the constrained-gas reading — wall-condensation
transitions of log-gases are generically third order (Majumdar–Schehr
class), which is QC-4's clause and is consistent with C-11's "one
universal E-normalized profile across the crossover".

**C-4 (chirp trichotomy, reconciliation requested by the brief):** the
quasicrystal two-scale result and my low-pass functional agree
quantitatively through one sentence: **the worth potential f(t) =
(π²/2)ln(eT*/t) is the integral of the weight d ln t that only a GRADED
density creates; at constant density the capacity structure degenerates,
f ≡ 0 (their measured zero/polynomial toll; AG's π²/2-absent), and all
that remains of aperiodicity is small-divisor conditioning.** So "the
chirp owns the super-exponential toll" (QC seat), "grading is the marginal
operator generating the logs" (renormalization), and "the deficiency
functional has nonzero weight only under grading" (this seat) are one
statement in three dialects. Co-signed.

### R2.3 Merges (two, with division of labor)

**M-1 — The Deficiency-Response Law (LG + QC + MF + HA; PT certifies).**
Merged statement: for symmetric configurations of RvM density with
sup_{[0, e²T*]}|δN| ≤ 2: |ln λ[Γ](L) − ln λ[stair](L) + κ(π²/2)J[Γ, L] +
B[Γ]| ≤ ε, with κ = 1 + o(1) (measured 0.95–0.96; the deficit from 1 is
edge-softening of the worth kernel), B the concavity/adaptation bias
(second-order, ∝ local variance), and J the worth-weighted charge.
Beyond sup|δN| ≈ 2: extreme-value form (deficit-side sup-pricing,
surplus saturation) — hypothesis must be ONE-SIDED (deficit) discrepancy.
Corollary (hand to DG for T3): the deterministic transfer constant in the
LR regime is C = κ(π²/2)ln(eT*/t₀) per unit sup-discrepancy — which
predicts magic-functions' measured phase-transport bound 6.64 as
0.95·(π²/2)·ln(59.17/14.52) = 6.59 (1%). Division: HA owns the rank-two
secular engine (T4(i)); QC owns the semiclassical kernel derivation
(their QC-3 per-cell slope); MF owns the exactly-solvable phase direction
(β-dial); LG owns the second-order/bias term and the ensemble layer
(VAR); PT referees extraction. First deliverables: the L = 2.996/3.555
replication battery (§R2.6) and the QC-3 slope measurement on stored
deep vectors. Kill: intercept drift with L beyond ±0.3 (QC's
pre-registered falsifier) kills the B-is-local claim; slope off [0.85,
1.05] at L = 2.996 kills κ = 1 + o(1).

**M-2 — The screened deficit energy = the mid-range constants (LG + FB +
renorm; RH-seat consumes).** Target: compute the constrained-equilibrium
(screened) energy of the deficit profile ln(1/u)du against the
super-Nyquist conductor with capacity endpoint, and test whether it
reproduces E + A = b·e^ℓ(ℓ + c₀) with DERIVED (b, c₀) — adjudicating
renormalization's b = 3/2 ⟺ 3/π² and their "crossover amplitude"
classification (their §1.4 table: if b is trajectory data, the
computation must be global — I accept that constraint). Division: FB owns
the constrained-sweep formulation (their FB-1 IS the setup) and the
G(t₀) entry gate (minutes, run FIRST); LG owns the equilibrium/screening
computation and the many-body correction structure (constrained by my
W > 0 pair data and renorm's +17/+26% dressing — pairwise-attractive
screening ansätze are pre-refuted); renorm owns the crossover/trajectory
integration and the 4π-cap matching; RH-seat consumes the result as the
A′-normalization input. Gate: if G(t₀) misses the RUN-4 worths by a
growing factor, the potential-gap reading dies and M-2 reverts to
phenomenology (recorded in advance, per FB's own kill).

### R2.4 Updates to Round-1 claims

1. **LG-1/LG-3 STRENGTHENED**: independent QC replication (slope 0.96 vs
   0.954; N = 28 pooled; B = 0.55 ± 0.10). The affine law is now
   double-measured under two conventions. LG-3(a)'s bias clause upgraded:
   B is configuration-class-dependent (ζ ≈ 0.1, CUE ≈ 0.55, Poisson
   non-affine) — this was implicit; now explicit.
2. **LG-4′ AMENDED (again, constructively)**: renormalization's block-spin
   dressing (+17%/+26%, net positive curvature +0.044) is a third
   independent confirmation of short-range SUPERadditivity, joining my
   W > 0 pairs and QC's Poisson amplification. All three seats' data now
   agree: second order is one-sidedly positive; screening-sharing is
   many-body only.
3. **§6.3 Track-E row AMENDED** per MF's β-dial finding (their §5.1 item
   3, which I co-sign): the zeros are NOT in-class λ-maximizers (pure
   phase beats them; the class optimum is bang-bang at the boundary).
   The correct invariant is charge neutrality at every L (equivalently
   the spectral gap / Berry saturation), NOT extremality of λ. Any
   "zeros as extremizers of the frame bound" story is dead; my Round-1
   wording "maximally-rigid offset" survives only as "worth-neutral
   offset".
4. **Anchored-spread bookkeeping**: QC's anchored ensemble has sd 1.92
   (12 seeds) vs my 1.48 (6 seeds) — statistically consistent; recorded
   jointly as the interior-mode floor ≈ 1.5–1.9 nats that anchoring does
   not remove.
5. **No new kills of Round-1 claims**; P1's failure and P5/P6's partials
   stand as scored, now with mechanisms assigned (C-6, LG-4′).

### R2.5 Pre-registered separator run (the C-1 payoff experiment)

**Design (locked before running).** Base: smooth staircase, KT = 180,
m = 48, dps 50, harness of §5.1 (anchors already validated). Two
deterministic displacement fields applied to points k ≥ 3 (first two
points pinned to keep N̂^{-1} well-defined), displacements in unfolded
coordinate u_k → u_k + A sin(k₀ t_k + φ):
- **SEP** (gap-violating slow mode): k₀ ∈ {0.08, 0.10, 0.12} — the first
  value whose tuned configuration passes the J-structure gates below
  (deterministic selection, no eigensolves consulted); A = 0.9; φ = φ*
  solving J(L₁ = 2.485) = 0 (discrete J, exact sum).
- **CTRL** (gap-respecting mode): k₀ = 0.8 > ln 2; A = 0.25 (monotonicity
  bound ρ/k₀ at the low edge); φ tuned at L₁ identically.
Evaluate both at L ∈ {2.485, 2.996, 3.555}; rebuild smooth anchors at the
two new L (EXPECTED: 3.17610e-15, 1.57685e-22). Eight eigensolves, ≈ 1 min.
All J values are printed BEFORE any eigensolve.

**Locked predictions.**
- P-R2-A (structure gates, deterministic): |(π²/2)J_SEP(L₁)| ≤ 0.05;
  |(π²/2)J_SEP(L₃)| ≥ 1.0; |(π²/2)J_CTRL(L)| ≤ 0.4 at all three L.
- P-R2-B (the law on coherent fields): for all six (config, L) pairs,
  |ΔE − (π²/2)J| ≤ 0.3 + 0.3·|(π²/2)J| (coherent fields carry dressing-
  scale, not CUE-scale, bias).
- P-R2-C (the C-1 separation): SEP's |ΔE(L₃) − ΔE(L₁)| ≥ 0.8 (neutrality
  at one window does NOT transfer); CTRL's |ΔE(L₃) − ΔE(L₁)| ≤ 0.5
  (gap-respecting ⇒ uniform near-neutrality) — the trichotomy's converse
  failure and the gap's sufficiency, in two numbers.

**Results (appended after the run, unedited above this line).** Scripts and
raw logs: `separator_test.py/.log`, `separator_verify.log`. Interruption
note: this seat was killed mid-session by a credit outage after locking
§R2.1–R2.6 and before executing; the locked design was run unchanged on
resume. One DESIGN-stage amendment, made before any eigensolve and logged
in the script header: the locked A = 0.9 could not reach the
|(π²/2)J(L₃)| ≥ 1.0 gate at any k₀ (max 0.77 — deterministic arithmetic;
P-R2-A therefore FAILED AS LOCKED); since J is linear in A to first order,
A was raised to 1.8 (inside the monotonicity bound and the sup|δN| ≤ 2
domain), after which the gates pass: SEP (k₀ = 0.10, φ = 2.7419):
(π²/2)J = −0.000 / −0.090 / −1.560 at L = 2.485/2.996/3.555; CTRL
(k₀ = 0.8, A = 0.25): +0.000 / +0.005 / +0.009. One ordering crossing at
the pinned junction (configuration sorted; supD = 2; multiset semantics).
Smooth anchors reproduced EXPECTED at all three L to printed digits.

**Basis discipline proved essential (COMPUTED, the run's third finding):**
structured coherent configurations converge much slower than random ones.
m-ladder of ΔE = E_cfg − E_smooth (common-basis differences):

| config, L | m=48 | m=64 | m=80 | verdict |
|---|---|---|---|---|
| SEP, 2.485 | −0.31 | −0.22 | — | stable |
| SEP, 2.996 | +2.71 | +2.75 | +2.78 | stable |
| SEP, 3.555 | −0.08 | +3.17 | +3.18 | m=48 was a transient; converged +3.2 |
| CTRL, 2.485 | +0.08 | +0.09 | — | stable |
| CTRL, 2.996 | +0.23 | — | — | (small) |
| CTRL, 3.555 | −1.74 | +0.22 | — | m=48 was a transient; converged +0.2 |

**Scorecard (against the locked bands):**
- **P-R2-A**: FAILED as locked (amplitude too small to reach the gate);
  PASSED under the labeled deterministic-stage amendment. Informative
  content of the failure: tuned neutrality at one window constrains the
  achievable cross-window charge more strongly than my hand estimate — the
  shared [t₀, X₁] segment carries most of the weight at ALL three L.
- **P-R2-B**: CTRL PASSES at every L at converged basis (+0.09/+0.23/+0.22
  against ≈ 0 predictions). SEP: L₁ PASSES (−0.22, band ±0.30); L₂ **HARD
  FAIL** (+2.78 vs −0.09 ± 0.33, basis-stable); L₃ **HARD FAIL WITH WRONG
  SIGN** (+3.18 vs −1.56 ± 0.77: the 1.5-nat surplus is not merely
  uncollected — the mode costs +3.2 nats).
- **P-R2-C**: CTRL PASSES (m-corrected: |ΔE(L₃) − ΔE(L₁)| = 0.13 ≤ 0.5 —
  gap-respecting ⇒ uniform near-neutrality, as predicted). SEP: the number
  (3.40 ≥ 0.8) passes but by the WRONG MECHANISM (coherent-mode cost, not
  charge collection) — scored **FAILED AS INTENDED**.

**Findings (what the failures teach; all COMPUTED unless tiered):**

F1. **The affine charge law has a COHERENCE boundary, inside sup|δN| ≤ 2.**
A single narrowband low-frequency displacement mode (k₀ = 0.10 ≪ ln 2,
sup|δN| = 1.8) violates ΔE ≈ (π²/2)J by +2.9 (L₂) and +4.7 (L₃) nats,
always toward COST, swamping its own charge term — while the same
functional predicts random broadband fields to r = 0.991 (Round 1), slow
monotone transport to 2.5–4.5% (MF's dial), and block dipoles to 17–26%
(renormalization). The law's domain is therefore NOT parameterized by
sup|δN| alone: **incoherent/broadband fields and monotone transports obey
it; adversarial coherent narrowband fields do not.** Consequence for the
merges: QC's M-A draft ("for configurations with sup|δN| ≤ 2 …") and my
own M-1 statement are REFUTED AS WRITTEN by this run — the hypothesis must
exclude coherent sub-ln 2 modes (or bound gross transport), see the
amendment block below. T3's worst-case form survives untouched: measured
+3.2 sits inside DG-3's C₀·ℓ·(D+1) budget (≈ 12 at L₃, D = 2).

F2. **The C-1 separation is sharper than designed.** SEP is charge-neutral
at L₁ AND nearly neutral at L₂ (J = −0.09), yet costs +2.8 there: per-L
charge neutrality (equivalently midpoint effective phase) is NOT a
sufficient statistic even at its own window once coherent low-k modes
exist. The designed first-order separator (charge breaking at L₃) was
overwhelmed by a second-order coherent cost — separating MORE than
intended: the spectral-gap statement is stronger than per-L neutrality not
merely as a uniformity claim but as a validity-domain claim. ζ passes the
strong test (no sub-ln 2 coherent modes exist for it at all); ensemble
samples and adversarial fields require the full gap hypothesis before
"neutral ⇒ rigid-equivalent" may be used at any window.

F3. **Basis warning (practical, for every seat running configuration
tests):** structured/coherent configurations at m = 48 can be off by 3+
nats and even carry the wrong sign (table above; CTRL L₃ swung −1.74 →
+0.22). Single-rung m = 48 readings of structured configs are unreliable
below |ΔE| ≈ 2; random (CUE/Poisson) configs showed no such transients
(two-builder cross-checks, Round 1). All ensemble work in the C-6/R2.6
battery inherits an m-ladder requirement at L ≥ 3.
   Caveat on F1's localization: SEP's realized field includes a
half-spacing 3-point cluster at the worth-heavy bottom (the sorted
junction); the +2.8 may be concentrated there rather than spread along the
mode. This does not rescue the sup|δN| hypothesis (the cluster IS part of
a field with sup|δN| ≤ 2), but the R2.6 battery includes the
disambiguation variant (pin k ≤ 5, retune, remeasure).

F4. SPECULATION (one sentence, for the riemann-hilbert seat): a coherent
δN mode at frequency k₀ enters the frame operator like one added
almost-periodic line at lag k₀ in their AP-symbol picture (RH-4(ii)'s
"one-frequency symbol update") — which is exactly why its effect is
ledger-like (sign and size set by minimizer structure at lag k₀), not
charge-like; their machinery, not (LR), is the right price list for
coherent modes.

**Post-run amendment block (explicit, replacing nothing silently):**
1. M-1's hypothesis is amended from "sup_{[0,e²T*]}|δN| ≤ 2" to:
   "sup|δN| ≤ 2 AND the displacement field is incoherent (random with
   correlation length ≲ one spacing) or monotone-transport; coherent
   narrowband components below ln 2 excluded" — with F1 as the recorded
   counterexample forcing the clause. QC's M-A statement needs the same
   clause; flagged to their seat via this block.
2. C-1 verdict extended (jointly with QC's R2.2, which landed while this
   seat was interrupted): QC's charge-matched Sine₂ example separates
   midpoint-phase from charge-neutrality at second order (their
   β_eff ≈ 0.433 computation — the intrinsic term leaks into β_eff);
   my SEP example separates both per-L scalars from the gap statement at
   the level of validity domains. Two complementary separators, one
   verdict: the trichotomy is one first-order scalar per L, plus an
   intrinsic local-statistics term, plus a uniformity/coherence mechanism
   that only the spectral-gap statement captures — and ζ is the
   configuration that passes all three tests simultaneously.
3. The replication table of §R2.1 stands confirmed by QC's own R2.1
   (slopes 0.96/0.954, ζ charge +0.073/+0.071, and their sampler's
   x₁-pinning explaining the 1.92-vs-3.60 spread difference — their
   acknowledgment matches my Round-1 P4 reading).
4. C-6 harmonization: QC's R2.2 protocol (their steps 1–7: both builders,
   both samplers, free+anchored splits, charge-matched median AND
   intercept reported separately) is adopted as the joint protocol; my
   §R2.2-C-6 prediction bands ride along unchanged (my charge-matched
   Poisson central +3.5 ± 1.5 vs their 2.0–3.2 — overlapping but distinct
   centers, BOTH now on record; the run adjudicates between us). Per F3,
   the protocol gains one line: m-ladder verification at any |Δ| < 2
   reading for L ≥ 3.

### R2.6 Next action (single, sized)

**The three-L ensemble battery** (joint with QC; this seat owns; the M-1
first deliverable and the C-6 protocol in one run): 12 CUE + 12 Poisson
seeds at L = 2.996 and L = 3.555 (KT = 180, m = 48; law_core builder),
reporting per-seed (λ, ΔE, (π²/2)J, supD). Tests, all pre-committed:
QC's left-on-the-table falsifier (CUE intercept stays in [−0.9, −0.3]
across L, else M-1's B-is-local dies); the class-II variance signature
(Var J grows by the predicted low-k integral factor ≈ 1.2–1.5 from
L = 2.485 to 2.996 — flat Var J means the weight, not the process,
dominates); the charge-matched Poisson intrinsic cost (+3.5 ± 1.5 at
L = 2.485-calibration, L-trend reported); and Q3 support at L = 3.555
(ensemble context for the true-zero point). Size: ~50 eigensolves ≈ 30–45
min compute at current load + half a day of writeup. Deliverable: the
ENVELOPE.md §2b replacement text with measured decompositions, and M-1's
empirical constants at three windows.

**Post-run addendum to the next action (after §R2.5's findings and QC's
R2, one merged run):** the battery is now the JOINT C-6 protocol (QC R2.2
steps 1–7 adopted verbatim) plus three riders from this seat: (i) the
m-ladder requirement of F3 for every structured or L ≥ 3 reading; (ii) the
SEP disambiguation variant of F1 (pin k ≤ 5, retune φ, remeasure at
m = 48/64/80 — localizes the coherent-mode cost: cluster vs extended
mode; 6 eigensolves); (iii) the Var-J growth discriminator and my Poisson
band (+3.5 ± 1.5) vs QC's (2.0–3.2) adjudication, both pre-registered.
Combined size: ~85 eigensolves ≈ 45–60 min compute, one worker, one
session including analysis and the §2b rewrite draft.
