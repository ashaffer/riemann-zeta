# An empirical envelope law for the margins of the truncated Weil quadratic form

**Draft note for comment — not yet distributed.** Prepared July 25, 2026, from the
instrumented research program in this repository (see `README.md`, `PROGRAM.md`).
Contact: [to be filled by the repository owner].

## Summary

Let Q_L denote the Weil quadratic form of ζ (pole + archimedean − prime-power
terms, in the normalization of the certified ledger in `PROGRAM.md` §6, equal
under RH to 2Σ_{γ>0}|φ̂(γ)|²) restricted to real test functions φ supported in
[−L/4, L/4], with the prime sum truncated at e^{L/2} — on such φ the truncation
is exact, so positivity of Q_L for all L is Weil's criterion. Write λ_min(L) for
the infimum of Q_L(φ)/‖φ‖₂², i.e. the lower frame bound of the exponential
system at the zero ordinates over an interval of length L/2.

Computing λ_min(L) in a spectral (Legendre) Galerkin basis in extended precision
— with the archimedean term evaluated by an exact x-space kernel rather than
numerical quadrature in r — we measure, across the support windows of the prime
powers 2, 3, 4, 5, 7 and twenty-five orders of magnitude:

1. **A smooth envelope law.** With T*(L) = 2πe^{L/2} (the height at which the
   zero-counting density reaches the Nyquist density of the support),
   **ln λ_min(L) ≈ 10.2 − 1.755 · e^{L/2} (L/2 + 4.0)**,
   i.e. the exponent is proportional to (T*/2π)(ln(T*/2π) + 4). The three
   constants were fit on the window interiors of 2, 3, 4(=2²), 5; the law then
   (a) interpolated an unfitted point (L = 2.30: predicted 1.03e−8, measured
   9.72e−9), (b) reproduced the threshold-approach band (L = 2.1942: predicted
   6.0e−8, measured 5.77e−8), and (c) extrapolated to the p = 7 window (forecast
   1.3e−30, logged before the deep runs; measured upper bound 2.79e−30, still
   descending toward it).

2. **No knife-edge at prime-power thresholds.** At operator level the margin
   does **not** collapse as L ↑ 2 log 3: the spectral values flatten to
   ≈ 5.77e−8 (basis drift 0.35% between m = 48 and 64), on the envelope law.
   The "zero-slack at thresholds, λ ∝ d^κ" phenomenology previously measured in
   a hat (P1 finite-element) basis — including by us — is the hat basis's own
   convergence transient, not a property of the form. A fine grid across the
   threshold makes this vivid: L = 2log3 − 0.001 → +0.001 moves the margin
   5.638e−8 → 5.486e−8, ratio 0.973 measured against 0.968 from the law's local
   slope — the margin *glides* through the prime's arrival. The deficit/rescue
   structure (archimedean-plus-pole alone fails past each threshold and the
   newest prime restores positivity) is untouched; what dissolves is the local
   knife-edge picture of the full form's margin.

2b. **The law is density, not arithmetic — and the zeros are maximally rigid.**
   Since the form equals the frame form of exponentials at the zero ordinates,
   we recomputed the frame bound with the ordinates replaced by (i) the smooth
   Riemann–von Mangoldt staircase N(γ_k) = k − 1/2 (correct density, perfectly
   rigid, no arithmetic) and (ii) Poisson arrivals through the same density.
   At equal truncation (Γ_cut = 420, m = 48): true / smooth / Poisson =
   2.690e−10 / 2.751e−10 / 2.90e−12 at L = 2.485; 2.714e−15 / 3.176e−15 /
   2.97e−17 at L = 2.996; 9.91e−22 / 1.58e−22 / 8.95e−23 at L = 3.555. The
   smooth staircase matches the true zeros within truncation uncertainty; the
   Poisson model costs 1.5–2 orders; all three share the decay slope. So the
   envelope's decay constant is a functional of the counting function alone
   (prolate/Landau–Widom territory), local statistics enter only the offset,
   and the true zeros sit at the maximally-rigid offset — at frame-bound level
   the zeta zeros behave like a perfectly rigid sequence.
   [Update, July 26 IAS panel: the "Poisson costs 1.5–2 orders" figure is a
   one-seed number of which roughly half is that seed's realized charge
   (worth-weighted deficiency); at Poisson amplitude no affine law exists
   (extreme-value crossover past sup|δN| ≈ 2). A charge-matched rerun
   protocol, jointly pre-registered by two seats, is in
   results/ias/IAS-SYNTHESIS.md §7; this claim should be quoted with the
   decomposition until that rerun replaces it.]

3. **Conductor universality.** For real primitive Dirichlet characters the same
   measurement (pole-free, ψ((1±1)/4… per parity, conductor term log(q/π))
   gives envelopes whose decay rate is governed by the family Nyquist height
   **T*_χ(L) = (2π/q) e^{L/2}** (density (1/2π)log(qT/2π) reaching Nyquist):
   measured d ln λ / d(e^{L/2}/q) ≈ −11.2…−12.3 for q = 3, 5, 7 (both parities)
   against −10.7…−11.6 for ζ — the same constant within current convergence
   bias, which is one-sided (all deep values are Rayleigh–Ritz upper bounds).
   Conductor, parity, and the pole appear only in the offset, not the rate.

4. **Certified rungs.** The measurements are backed by interval-arithmetic
   certificates (exact-rational basis integrals; Bernoulli-series kernel with
   rigorous tails; interval Cholesky lower bounds and interval Rayleigh upper
   bounds; mpmath.iv, 220-bit endpoints): two-sided enclosures of Galerkin
   minima including
   ζ, L = 7/4, hat m = 41: (3.77497970e−5, 3.77497984e−5];
   ζ, L = 497/200, Legendre m = 24: (3.86870e−10, 3.86881560e−10];
   ζ, L = 749/250, Legendre m = 48: (4.34600e−15, 4.34621580e−15];
   ζ, L = 711/200, Legendre m = 40: (1.79970e−20, 1.79972291e−20];
   χ₋₇, L = 101/25, hat m = 41: (1.57558810e−3, 1.57558821e−3];
   χ₋₇, L = 5, Legendre m = 40: (7.56900e−7, 7.56991097e−7] —
   certified positivity of truncated Weil forms across fifteen orders of
   magnitude, including two family windows.

5. **Out-of-fit tests, summarized.** Interpolation at L = 2.30 (6%); the
   threshold band and glide (4% and the 0.973-vs-0.968 crossing); extrapolation
   to the p = 7 window (forecast 1.3e−30 logged first; measured ≤ 2.79e−30,
   descending); extrapolation into the n = 8 window at L = 4.25 (predicted
   2.2e−35; measured 7.52e−35 → 5.55e−35 at m = 96 → 112, descending toward
   it); and extrapolation into the n = 9 window at L = 4.50 (predicted 1.7e−41;
   measured ≤ 1.24e−40 at m = 112, not yet converged) — the law holds over ~35
   orders of magnitude everywhere we have looked. Both deep extrapolations sit
   above the law and descend toward it with basis size; convergence bias
   explains this, but a mild upward bend of the true envelope beyond L ≈ 4.2 is
   not yet excluded. Figure: `results/figures/envelope_law.png`.

## Why this may interest the positivity program

- **For the CCM finite criterion** (Connes–Consani–Moscovici, arXiv:2310.18423;
  Connes–Consani, Selecta 2021): the uniform-transfer normalization must divide
  out precisely the envelope above. In particular a naive per-window margin
  bound λ_min ≥ c·dist(L, ∂W_p)^κ is not supported at operator level — there is
  no threshold-local structure to normalize against, only the global envelope.
- **For finite-cutoff certification** (arXiv:2607.02828): the law quantifies how
  fast the certifiable margin closes as support grows — the certification
  budget must beat exp(−1.755·(T*/2π)(ln(T*/2π)+4)); our certified rungs at
  1e−15 and 1e−20 indicate what interval arithmetic can already reach.
- **For object candidates** (Track E sense): any spectral realization of the
  missing positivity-bearing operator must reproduce (i) the envelope constant
  b ≈ 1.755 (in the (T*/2π)ln T* normalization), (ii) the offset's dependence
  on pole/parity/conductor, and (iii) the universality in T*_χ across the
  family. The natural theoretical comparison is Landau–Widom-type asymptotics
  for prolate/Toeplitz eigenvalue plunges; whether b and the +4.0 offset are
  derivable from Sonin-space asymptotics is, to us, the sharpest question this
  data poses.

## Proved companions (added same day)

Two statements graduated from measurement to proof; see `THEOREMS.md`:
(1) the **Glide Theorem** — the operator margin λ(L) is non-increasing and
continuous with explicit modulus across prime-power thresholds (so the
absence of a knife-edge is a theorem, not only a measurement); its engine is
the elementary two-sided bound ψ(¼) + ½log(1+4r²) ≤ Re ψ(¼+ir/2) ≤ same + 8.
(2) a **machine-checked window of Weil positivity**: a Lean 4 kernel-verified
certificate (axioms propext/Classical.choice/Quot.sound only) that the
truncated Weil form at L = 497/200 is strictly positive on an explicit
12-dimensional Legendre test space — both primes 2 and 3 participating —
modulo a Bridge Proposition proved by interval arithmetic with stated trust
base. We believe this is the first formally verified statement in the
Weil-positivity program.

## The sharpened, invariant form of the law (added July 26, derivation campaign)

A dedicated derivation-and-discrimination campaign (results/agent-law-theory.md)
upgraded the law in three ways. (1) **Invariant parameterization**: staircase
deformations break the fit degeneracy and select
  ln λ_min = −A + b·[ N(T*) + μ·D(T*) ],   b ≈ 1.51,  μ ≈ 6.0–6.7,
with N the counting function at the Nyquist height and D the Nyquist-deficit
mass; this single pair of constants fits both the 25-point deformed-staircase
family and the true-ζ ladder (rms 0.026), strictly better than the
(10.2, 1.755, 4.0) chart above, whose parameters are degenerate on the fitted
window; β-linearity of the exponent is verified to 1% and IS the conductor
universality. (2) **Mechanism**: bulk prolate/Landau–Widom functionals
provably cannot produce the law — replacing the zero sum by its density
integral makes λ order one, so the exponential smallness is a pure
DISCRETENESS effect; sub-Nyquist constant-density sequences cost nothing
(exact tight-frame calibration), and the ζ margin is a chirp effect.
(3) **The marginal law**: removing a single zero at height t is worth exactly
(π²/2)·ln(eT*/t) in the exponent — the Bonami–Karoui constant, measured to
1–4% across nine (t, L) points — supported up to the capacity height e·T*,
with ~20% non-additive interactions. The bulk constants (b, μ) resisted
derivation; the marginal law and the capacity endpoint e·T* are the
best-supported provable targets (four are recorded in the campaign report).

## The deep-window correction: the 4π cap (added July 26, deep-window campaign)

The deep-window campaign (results/agent-deep-windows.md; ladders to m = 176 at
L = 4.25–5.50, every rung a Rayleigh–Ritz upper bound with monotone nested
bases) settles the bend question flagged in the caveats: **the mid-range law
above is pre-asymptotic, and the decay rate saturates**. The measured facts:

- The converged deep limits (L = 4.25, 4.50, 4.60, 4.75; the last
  blind-predicted to 0.4% before its refinement rungs ran) sit systematically
  ABOVE every 3-parameter refit — a bend, not a refit problem.
- The deep data select the prolate (Fuchs) form
    **ln λ_min ≈ A′ − 4π·e^{L/2} + p·(L/2)**,   p ≈ 4.5–6.5,
  with the decay rate per unit c = e^{L/2} measured at 4π to 0.4–1.3% three
  independent ways (free fit 12.729, constrained 12.521, pairwise secant
  slopes 12.42–12.58 against 4π = 12.566).
- The onset is exactly computable: the mid-range law's local slope
  1.755(L/2+5) crosses 4π at **L = 4.32**, precisely where deviations begin.
  Below that the three-constant chart stands as fitted; above it the rate is
  capped at the universal prolate rate.
- Stopping-height readout (the differential-geometry protocol): abrupt
  saturation is EXCLUDED (level test), and the scalar shape test favors the
  smooth-cap hypothesis — the measured secant slopes lie on 4π and 3–6% below
  both drift alternatives, with bias headroom ≤ 0.5%.
- Consistency: all eleven measured stopping heights lie strictly inside the
  two proved-target horizons (e·T*, e²·T*), margins ≥ 0.14 in w = ln(T_s/T*).

**This resolves the Connes/Groskin discrepancy below** — see the updated
paragraph there — and is the reading this note now recommends: the
(L/2 + 4) log-factor is a faithful mid-range description (all validations in
the Summary stand on their windows), and the asymptotic decay rate is 4π per
unit e^{L/2}, matching the frontier's prolate asymptotics.

## Prior art and repositioning (added after the July 26 literature sweep)

The sweep (results/agent-prior-art.md) found that the qualitative shape of the
decay is anticipated by the frontier itself: Connes (arXiv:2602.04022, §6.4)
describes the truncated form's smallest eigenvalue as decaying "exponential of
exponential" and plots it against an explicit prolate comparator (numerically
identified in our sweep as Fuchs's 1964 theorem at n = 4); Connes–Consani's
2021 zeta-cycles paper computes a deep value (2.389e−48 at their λ² = 11)
lying essentially on our envelope; Groskin (arXiv:2605.20224) tabulates
λ_min to 1e−334 across sixteen cutoffs with an extrapolation matching
Connes's prediction. What remains, to our knowledge, THIS note's own: the
support-normalized three-constant law with its (L/2 + 4) log-correction and
out-of-sample validations; the Dirichlet-family universality in T*_χ (no
corpus paper treats families); the staircase/Poisson mechanism experiment
(the law is a functional of the counting function at maximal rigidity); the
Glide Theorem's effective modulus and monotonicity (qualitative continuity is
Bombieri 2000/2003, proved by Suzuki arXiv:2606.09096 Thm 1.3); and the
kernel-checked certificates. **The c = 100 discrepancy is RESOLVED (July 26,
deep-window campaign):** the naive extrapolation of the mid-range chart gave
log₁₀ λ ≈ −656 against Connes/Groskin's ≈ −530; with the measured 4π cap
(previous section) the corrected law predicts −527.7 to −529.0 at c = 100 —
agreement to ~0.5% of the exponent, resolving the tension as option (ii) of
results/agent-prior-art.md §7.2 (the log-factor was mid-range only). Our
envelope now extrapolates onto the frontier's prolate asymptotics; what
remains ours is the mid-range form, the onset point L ≈ 4.32, the family
universality, the mechanism experiment, and the certificates.

## Caveats (stated plainly)

- Every λ_min is a Rayleigh–Ritz **upper bound**; deep-window values at the
  largest supports are still descending in basis size (convergence status is
  tabulated per point in `results/RESULTS.md`). Slopes therefore carry a
  one-sided bias, small in the windows used for the fit.
- The law is phenomenological: three constants, five windows, no error model.
  It DOES bend beyond L ≈ 4.3 — measured, not hypothetical (see the 4π-cap
  section); use the mid-range chart only below the crossover.
- The spectral/hp values trust mpmath's floating arithmetic and quadrature-free
  exact integrals at 50 digits; the certificates trust mpmath.iv enclosures.
  The float pipeline, the extended-precision hat pipeline, the spectral
  pipeline, the explicit-formula zero-side inequality, and the interval
  certificates are five layers of internally independent validation; the
  two-sided Guinand–Weil oracle is certified to 1e−29.
- The zeros' lower Beurling density is infinite, so strict positivity of every
  fixed-L margin under RH is classical (Beurling sampling after thinning); the
  content of the measurement is the quantitative envelope, not positivity
  itself.

## Reproduction

Everything is reproducible from the repository in minutes to hours on a laptop:
`src/oracle.py` (certification gate), `src/spectral_margins.py` (the ladder),
`src/certified_margins.py` and `src/certified_spectral.py` (the certificates),
with EXPECTED values inline. Python 3 + numpy + mpmath (+ gmpy2 recommended).

---

## Draft cover email (short form — to be edited/sent by the repository owner)

Subject: Measured envelope law for truncated Weil-form margins (numerical note)

Dear Professors Connes, Consani, Moscovici [/ Dr. Groskin / Prof. Suzuki],

While instrumenting the truncated Weil quadratic form numerically (hat and
Legendre Galerkin bases, an exact x-space archimedean kernel, and interval-
arithmetic certificates), we measured the minimal eigenvalue across the support
windows of the prime powers 2 through 8 and find that the margins follow a
single smooth envelope, ln λ_min ≈ 10.2 − 1.755·e^{L/2}(L/2 + 4), spanning ~30
orders of magnitude — with no threshold-local collapse (the d^κ behaviour we
and others measured in hat bases appears to be a basis transient; the margin
glides through 2 log 3 exactly on the law's slope), and with the same decay
constant for real Dirichlet characters once the height is rescaled to
T*_χ = (2π/q)e^{L/2}. Replacing the true ordinates by the smooth Riemann–von
Mangoldt staircase reproduces the margins within truncation uncertainty, while
Poisson statistics cost 1.5–2 orders: the decay constant appears to be a
functional of the counting function alone, with the true zeros sitting at the
maximally-rigid offset. Two-sided interval certificates back the ladder down
to the 1e−20 scale. The attached note summarizes the measurements, their
validations, and the caveats; the repository reproducing every number is
public. We would value any indication of (a) prior art we have missed, and
(b) whether b ≈ 1.755 and the +4.0 offset are derivable from Sonin-space/
prolate (Landau–Widom) asymptotics with the Riemann–von Mangoldt density —
the smooth-staircase result suggests they must be.

With respect and thanks, [name]
