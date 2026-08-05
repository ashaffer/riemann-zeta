# Manuscript briefs

Status: editorial plans, 2026-08-05.  These are not submitted manuscripts.
Each brief states the smallest defensible paper, its theorem spine, and the
condition that should kill or postpone it.

## 1. Correction to the phase coupling in a hybrid joint limit theorem

**Recommended form:** coordinated correction or corrigendum, not a competing
paper if author coordination is possible.

**Provisional abstract.**  We identify a coordinate-inversion mismatch in the
joint limiting law of a hybrid universality theorem.  The empirical coordinate
`p^(i tau)` enters a smoothed Dirichlet polynomial with inverse powers, so its
Haar pushforward couples the random Dirichlet series to the conjugated finite
torus coordinate.  A one-prime mixed moment distinguishes the corrected law
from the stated same-phase law.  We give the corresponding edits to the weak-
convergence argument and repair a separate compact-open tail estimate.  The
marginal law, product support, and qualitative universality consequences are
unchanged.

**Theorem spine.**

1. Exact finite-polynomial Haar pushforward with coordinate inversion.
2. One-prime mixed-moment separation.
3. Passage of the witness to the full law.
4. Corrected joint-limit theorem.
5. Compact-open tail repair on an exhaustion by compact subsets.
6. Corollary audit: statements that survive unchanged and statements whose
   joint coupling changes.

**Evidence:**
[`results/ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`](../results/ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md).

**Release gate:** a line-by-line check against the source PDF and private
communication with the author.  If a newer version already repairs the issue,
replace the manuscript by an acknowledgement/provenance note.

## 2. An anchored Jensen bound for prescribed Paley--Wiener zeros

**Recommended form:** short analytic theorem plus machine-checked companion.

**Provisional abstract.**  Let a unit-norm function be supported on a finite
interval and suppose its Fourier--Laplace transform has a quantitatively
nonvanishing low-frequency anchor.  If a symmetric prescribed frequency set
obeys a Riemann--von Mangoldt-type lower counting law and the transform vanishes
on its initial segment with the prescribed multiplicities, Jensen's formula
gives an explicit upper bound on the vanishing horizon.  We also bound the
remaining Jensen mass of unprescribed zeros.  The abstract theorem and its
global-order formulation are formalized in Lean.

**Theorem spine.**

1. Entirety and exponential type from finite-interval `L2` support.
2. Layer-cake identity for the prescribed zero count.
3. Integrated staircase lower bound.
4. Recentered Jensen formula with a zero-free selected radius.
5. Pair-product lower bound for symmetric prescribed zeros.
6. Explicit monotone crossing and Hard Horizon theorem.
7. Residual Jensen-mass or “zero desert” corollary.
8. Necessity of the anchor via a finite-head vanishing construction.

**Prior-art boundary.**  The proof mechanism is classical Jensen plus
Paley--Wiener growth.  Related point-normalized Jensen constraints occur in
[Brevig--Chirre--Ortega-Cerda--Seip](https://arxiv.org/abs/2210.13922), and
[Burnol](https://arxiv.org/abs/1008.0617) studies Paley--Wiener spaces with
prescribed zeros.  The explicit bound and Riemann--von Mangoldt-density
specialization appear plausibly new as stated after a targeted search; this is
not yet a priority claim, and `e^2` is not claimed sharp or intrinsic.

**Evidence:**
[`results/experts/T1PRIME.md`](../results/experts/T1PRIME.md) and
[`lean/glide/Glide/HardHorizon.lean`](../lean/glide/Glide/HardHorizon.lean).

**Claim boundary:** the abstract theorem does not require RH.  A zeta
specialization additionally needs an explicit all-zero counting estimate and
the stated anchor; it must not be described as a zero-free theorem for zeta.
The stronger paper-side zero-desert extraction must also be distinguished from
the selected-radius/raw-bound theorem currently checked by Lean.  Compare the
zeta constants with [Bellotti--Wong's current explicit zero-count estimate](https://arxiv.org/abs/2412.15470)
before release.

**Release gate:** independent review of the Jensen divisor bookkeeping,
constants, anchor normalization, and novelty relative to density theorems for
Paley--Wiener zero sets.  Use the neutral title above rather than “Hard
Horizon.”

## 3. A verified local positivity theorem for an arithmetic Weil form

**Recommended form:** formalized-mathematics/computer-assisted case study.

**Provisional abstract.**  We define a compact-support arithmetic Weil
quadratic form on its logarithmically weighted Fourier domain and prove that at
`a=7/16` its active prime-power set is exactly `{2}`.  Lean identifies this
general definition with a previously certified time-domain form and checks a
strict full-domain lower bound from an exact rational certificate and analytic
error estimates.  Separate interval computations establish larger local
support endpoints under a documented FLINT-Arb and analytic trust base.  The
formal development exposes, rather than assumes silently, the Guinand--Weil
zero-side formula needed to reinterpret the form as a sum over zeros.

**Theorem spine.**

1. Logarithmic form domain and its linear closure.
2. Finite active-prime-power set and shell decomposition.
3. Exact specialization at `a=7/16`.
4. Generic exact certificate soundness.
5. Finite/complement/cross two-block transfer.
6. Strict lower bound for every nonzero vector in the form domain.
7. Explicit assumption boundary for the zero-side equality.

**Evidence:**
[`results/CONSOLIDATED-LEDGER-AND-ORTHOGONAL-RESET-2026-08.md`](../results/CONSOLIDATED-LEDGER-AND-ORTHOGONAL-RESET-2026-08.md),
[`THEOREMS.md`](../THEOREMS.md), and the `GeneralZetaWeilForm` audit.

**Release gate:** one clean, pinned reproduction environment; certificate
hashes; a dependency diagram separating exact Lean theorems, generated
rational data, interval computations, and literature assumptions.

**Mandatory nonclaim:** this is not a proof of the Guinand--Weil equality in
Lean, all-support positivity, or RH.

## 4. Lean infrastructure for explicit-formula analysis

**Recommended form:** a sequence of mathlib contributions.  Consider a
formalization paper only after enough pieces have been upstreamed to tell one
coherent story.

**Package A: simple poles and contours.**

- simultaneous removal of finitely many simple principal parts;
- an entire remainder;
- circle residue sums;
- rectangle-boundary formulas and gluing.

Potential contribution: the finite simultaneous simple-principal-part
regularization layer may complement mathlib's active isolated-singularity and
rectangle-residue work.  Coordinate with the authors of mathlib PRs #29588
and #39232 before extracting it; do not claim the rectangle theorem or the
first formal residue theorem as new.

**Package B: digamma and the Gauss vertical kernel.**

- the general two-point digamma series;
- the complex derivative bridge;
- the positive vertical-line integral;
- logarithmic bounds needed by the archimedean Weil multiplier.

**Package C: Hilbert-space approximation and certificates.**

- complete normalized Legendre bases on arbitrary intervals;
- Parseval and exact projection error;
- plane-wave coefficients and tail estimates;
- exact perturbative `LDL^T` positivity;
- optimal scalar two-block coercivity.

**Package D: small harmonic-analysis units.**

- autocorrelation Plancherel/Wiener--Khinchin;
- compact-support Fourier--Laplace entirety and exponential type;
- a quantitative two-sided smooth cutoff.

**Evidence and extraction order:** [`lean/UPSTREAMING.md`](../lean/UPSTREAMING.md).

**Release gate:** rebase each unit on current mathlib; use destination
namespaces; eliminate compatibility wrappers; minimize imports; run linters;
provide actual authorship and provenance.

## 5. Static local exchanges cannot cancel the Mobius collar

**Recommended form:** modest combinatorics/experimental-number-theory note
after independent review of the expanded density argument.

**Provisional abstract.**  We study sign-reversing exchanges between
squarefree integers in a dyadic boundary collar.  Any fixed scale-compatible
dictionary whose template weights are summable leaves a positive-density set
of collar vertices avoiding both support-pattern cylinders for every
template, and hence on which no exchange applies.  Bounded prime incidence
implies the summability hypothesis, and the argument extends to finite
prime-set hypertemplates.  Additional examples show collision obstructions
for several one-shot selectors.  Consequently, any local matching mechanism
capable of near-complete Mobius cancellation must be scale-adaptive, have
unbounded incidence, or retain global matching state.

**Theorem spine.**

1. Exact dyadic collar identity for `M(N)`.
2. Product divisibility law on odd squarefree integers.
3. Finite-prefix conditioning lemma.
4. Uniform template-tail density lemma with an explicit error.
5. Positive-density static-dictionary theorem.
6. Bounded-incidence and hypertemplate corollaries.
7. Explicit scope counterexamples: adaptive/greedy survivors are outside the
   theorem.

**Evidence:**
[`results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`](../results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md).

**Release gate:** independently check the new quantitative density lemma and
its countable-tail bound.  Retain scripts and checksums for every “first
counterexample” assertion.  Compare the tail argument with
Davenport--Erdos-type convergent-multiple-set results.

## 6. Topology loss in finite Euler-phase approximations

**Recommended form:** scoped obstruction paper after the analytic core is
formalized or independently refereed.

**Provisional abstract.**  We compare two natural finite-prime phase models
for detecting an off-critical functional-equation quartet.  A shifted
completed phase has the expected winding jump, but this is an
argument-principle zero count.  At finite cutoff both Euler phase models are
null-homotopic.  The literal two-sided quotient is unbounded in Besicovitch
`B^2`, while the functional-equation-normalized right phase converges in
`B^2` but fails to converge uniformly in the critical strip.  Thus `B^2`
convergence alone supplies no invertible continuous symbol carrying ordinary
winding, whereas uniform symbol convergence is unavailable from these finite
Euler products.  No claim is made about a separately constructed Calkin,
semifinite, or Fredholm-pair topology.

**Theorem spine.**

1. Remote-quartet compact-open invisibility and real-axis positivity.
2. Shifted polynomial phase winding.
3. Finite local null-homotopy.
4. Exact local `L2` norm and divergence of the literal quotient.
5. Exact `B^2` Cauchy formula for the normalized right phase.
6. Kronecker-alignment proof of nonuniform convergence for `0<a<=1/2`.
7. Precisely scoped trilemma for these two models.

**Evidence:**
[`results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`](../results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md) and
[`lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGo.lean`](../lean/rhbridge/RHBridge/QuantizedPhaseIndexNoGo.lean).

**Release gate:** formalize or independently check items 2, 4, 5, and 6.
Review against global scattering, hybrid Euler--Hadamard, and adelic trace
constructions.  The title and theorem must refer to the two studied phase
models, not every conceivable arithmetic index.

## 7. Fixed-place indefiniteness and the trace/polarization split

**Recommended form:** combine as one obstruction note only if editorial
compression produces a single theorem narrative.

**Provisional abstract.**  We show that the pole-zero quadratic form obtained
from any fixed finite set of Euler places is indefinite on sufficiently large
compact supports: broad rescaled test functions concentrate at the negative
zero-frequency value, while the archimedean multiplier becomes positive at
high frequency.  Finite algebraic models further show why one faithful
positive trace in the stated positive-contraction/log-determinant architecture
cannot both reproduce pure Euler moments, delete all mixed terms, and supply
the positive polarization.  The results isolate a structural
requirement of a cohomological RH program: the signed Lefschetz trace and the
positive metric must be distinct pieces of data.

**Theorem spine.**

1. Exact finite-place multiplier and `M_P(0)<0`.
2. Pole-killing broad-bump construction.
3. Rayleigh quotient convergence to `M_P(0)`.
4. High-frequency positivity and full indefiniteness.
5. Positive finite-trace saturation lemma.
6. Cayley--Hamilton obstruction for finite commuting invertible models.
7. Independent compact-place-torus action and invariant-metric assumptions
   stated as hypotheses, not consequences of an adelic quotient.
8. Explicit survivor class: infinite connected trace plus a separate
   polarization is not ruled out.

**Evidence:**
[`results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`](../results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md) and
[`results/TWO-PRIME-INFINITY-FAIL-FAST.md`](../results/TWO-PRIME-INFINITY-FAIL-FAST.md).

**Release gate:** write full conventional proofs of the broad-bump limit and
finite trace hypotheses; remove philosophical material not used by a theorem;
conduct a novelty comparison with semilocal explicit-formula/scattering work.

## 8. Editorial kill rule

A proposed paper is postponed if, after compression, its main theorem is one
of the following:

- a known equivalence to RH in new notation;
- a numerical pattern without a certified tail;
- an elementary lemma whose interest comes only from an aspirational RH
  interpretation;
- a Lean implication whose decisive premise is a project-specific axiom;
- a “universal no-go” supported by only two model families;
- a local result whose abstract or title implies global zeta-zero control.

This rule is intentionally stricter than the rule for retaining useful work in
the repository.
