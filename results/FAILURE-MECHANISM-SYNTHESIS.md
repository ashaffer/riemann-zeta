# Failure-mechanism synthesis: coherence without mass

Status: regrouping after the theta, cyclotomic, entropy, random-sieve,
non-Hilbert, and additive--multiplicative audits; 2026-08-01.

## 1. The common adversary

A hypothetical off-line zero `rho=beta+i gamma`, `beta>1/2`, is globally
decisive but locally small.

- Its normalized summatory bias is of scale `X^(beta-1)`, which tends to zero.
- Its primewise Mellin amplitudes have size `p^(-beta)`, and

  `sum_p p^(-2 beta) < infinity`.

- Its contribution can therefore be finite-energy, zero-density, or invisible
  to normalized local statistics while still producing a pole through coherent
  global analytic accumulation.

This is not incidental.  The critical line `beta=1/2` is exactly the
square-summability threshold for the local prime amplitudes.  An off-line zero
on the right lies in the regime where quadratic localization regards its tail
as harmless.

The program repeatedly tried to convert this **coherence without mass** into
coercivity, entropy, density, or a uniform spectral gap.  That conversion was
the shared point of failure.

## 2. The fidelity--amplification--closure trilemma

Every attempted mechanism needed three properties.

1. **Fidelity:** preserve the hypothetical zero, including its Mellin phase and
   the completed functional equation.
2. **Amplification:** turn one exceptional zero into a positive gap, extensive
   entropy, positive density, or another contradiction visible to available
   estimates.
3. **Closure:** survive the infinite support, prime, zero, or theta limit
   without inserting the desired conclusion as a uniform bound.

The failed paths achieved at most two.

### Fidelity plus closure, without amplification

- Fixed finite prime exclusions preserve the pole exactly.
- Positive-density random sieves preserve it through a nonzero analytic Euler
  multiplier.
- Coordinate changes among Weil, Suzuki, Birman--Schwinger, collar, and CCM
  descriptions preserve the possible radical.

But the signal remains a common finite-energy mode.  Random branch entropy
diverges while the pole multiplier has finite `L2`--indeed, under honest local
absolute convergence, finite `L1`--variation.  No contradiction scales with
the number of branches.

### Fidelity plus amplification, without closure

- Finite Weil windows have positive certified margins.
- Finite theta truncations and finite determinant models can be controlled on
  bounded ranges.
- Primorial branching creates many formal descendants.

At the global limit, the margin collapses, channel density vanishes, or a
boundary defect takes over.  For theta truncations the first surviving odd
boundary jet forces an eventually negative Laguerre tail.  Infinite modular
cancellation is not a small correction; it is what removes every such tail.

### Amplification plus closure, without fidelity

- Squaring or four-point alignment turns Möbius signs into `mu^2` and erases
  the Mellin resonance.
- Absolute values, variance, and ordinary entropy discard the phase coherence
  that made the pole possible.
- Centered or Wick-renormalized Euler products generate large endpoint
  variation, but can coexist with arbitrary prescribed poles and are no longer
  unrenormalized Möbius restrictions.
- A formal gamma determinant has the right spectrum, but the proposed
  `THR(Z)` object loses that spectrum after complexification.

These mechanisms produce strong structure, but not structure attached to the
actual completed zeta function.

## 3. Four information-loss operations

The trilemma manifested through four recurring operations.

### Local decomposition destroys completion

The completed object contains essential cross terms.

- Individual theta summands have the wrong high-frequency Laguerre sign; the
  `n=1,n=2` cross term repairs it at the first tested failure.
- Finite-prime cyclotomic data do not natively contain the archimedean gamma
  ladder.
- Prime and archimedean Weil blocks are individually indefinite in the wrong
  way; completion supplies the decisive cancellation.

Local pieces are not independently positive objects waiting to be summed.

### Truncation creates a boundary adversary

Finite support introduces collars, odd boundary jets, zero tails, or
determinant normalization defects.  These are not technical remainders: as the
interior margin collapses, the boundary term becomes the whole problem.

### Averaging erases the exceptional phase

Density-one zero statistics, almost-all short intervals, entropy, and `L2`
Walsh energy are designed to ignore sparse or finite-energy exceptions.  One
off-line zero is precisely such an exception in their native normalization.

### Universal inequalities absorb RH

When a bound was strengthened enough to survive the collapsing scale, it
became equivalent to Weil positivity, square-root Mertens cancellation,
positive-definiteness of the derived theta kernel, or compact-local
identification with xi.  The final uniform constant was not scaffolding; it
was the theorem.

## 4. What was missed ex ante

The earlier admission rule asked whether a path was sensitive to one
exceptional zero.  That was insufficient.  Many constructions *retain* the
zero algebraically but place it in a topology where its normalized signal
vanishes.

The missing question was:

> In what topology does the exceptional zero have nonvanishing size, and is
> the proposed contradiction theorem actually continuous in that topology?

For every failed analytic route, the answers were mismatched:

- the zero was visible in meromorphic continuation but the estimate lived in
  `L2`;
- it was visible in an all-shifts aggregate but the theorem controlled each
  correlation only relative to length `N`;
- it was visible after infinite modular completion but the proof worked
  termwise or at finite support;
- it was visible as a determinant spectrum but positivity of the pairing was
  absent.

This topology mismatch is the broadest reusable diagnosis.

## 5. Revised admission rule

A new path should not enter the portfolio until it specifies all six items.

1. **Exceptional-zero carrier:** the exact object changed by one off-line
   zero.
2. **Native topology:** the norm, order, index, or topology in which that
   change is bounded away from zero.
3. **Completion compatibility:** why gamma, pole, and all infinite cross terms
   are native rather than repaired afterward.
4. **Amplifier:** an independent theorem converting that carrier into a
   contradiction without averaging away its phase.
5. **Closed limit:** a proof that the amplifier survives the global limit at
   the same scale.
6. **Countermodel separation:** a model with arbitrary Euler-product poles,
   generic self-adjoint spectra, or finite-window positivity must fail at least
   one stated hypothesis for a transparent reason.

Merely preserving a pole, producing many branches, proving finite positivity,
or finding another equivalent quadratic form no longer qualifies.

## 6. What kind of mechanism could still work

The synthesis does not identify a proof, but it sharply restricts viable
mechanisms.  A successor must detect **coherent phase rather than mass** and
must be native to the completed global object.  Plausible forms are:

- a quantized or integer-valued invariant that one off-line quartet cannot
  cancel, unlike ordinary signed spectral flow;
- an exact order or monotonicity law for the completed theta/xi object, not for
  its summands, whose strictness is insensitive to small amplitude;
- a genuine arithmetic polarization or duality pairing whose positivity is
  independently geometric and whose spectrum is completed zeta;
- a phase-sensitive nonlinear invariant with a closed global limit and a
  countermodel theorem excluding flexible Helson-type Euler products.

All are difficult because each asks for new structure, not a sharper estimate
on an existing RH-equivalent certificate.  That is nevertheless the correct
Bayesian conclusion: further work on density, generic `L2` positivity,
finite-window gaps, or local Euler assembly is unlikely to pay.

## 7. Compressed lesson

The failed paths were not unrelated bad guesses.  They all encountered the
same boundary:

> RH is not resisting because the exceptional signal is too complicated; it
> is resisting because the signal is globally phase-coherent while being
> locally square-summable, asymptotically negligible, and removable by every
> averaging operation we know how to control.

The next path must preserve completion and phase from the start, and its
notion of size cannot be ordinary mass, density, or quadratic energy.

## 8. Mobius density follow-up: a singular Euler-factor endpoint

The later residue-to-density audit sharpens rather than overturns this
diagnosis.  Pintz's oscillation theorem shows that a single zero already
forces `x^beta` Mertens peaks in every log window of width
`O((log log x)^(3/2))`; the signal is substantially less sparse than this
report originally assumed.  But even resonance on every large scale cannot
support the proposed generic pretentious inverse theorem.

Indeed, `f_z(n)=mu(n)^2 z^omega(n)` has exactly squarefree support and, for
every fixed `z!=-1`, Selberg--Delange gives an every-scale mean of order
`x(log x)^(Re z-1)`, larger than every `x^beta`, `beta<1`.  Its pretentious
distance still diverges.  At the exact Mobius point `z=-1`, the coefficient
`1/Gamma(z)` vanishes and the Dirichlet series becomes `1/zeta(s)`.  The
exceptional-zero signal is therefore not merely low-mass: it sits at a
nonuniform, beyond-all-logarithmic-order endpoint of the local Euler-factor
family.

This supplies a stricter admission test for future inverse arguments.  They
must remain valid at the exact arithmetic endpoint while transparently
failing for every fixed nearby `z`, rather than rely only on the magnitude or
density of large partial sums.

## 9. Two-wave orthogonal follow-up

The later thermodynamic, model-theoretic, tropical, transport, fractal,
ultraproduct, automorphic, fugacity, and boundary-matching audits did not add a
fifth basic failure mechanism.  They sharpened the same four-part basis:

1. topology mismatch;
2. failure to include completion before imposing order;
3. an exact identity or detector with no independent exclusion engine; and
4. a limit theorem which already contains RH.

Three exact examples make the synthesis unusually concrete.

- Reciprocal polynomials with identical ordinary tropical data can have all
  roots on the unit circle or a reciprocal pair off it.  Valuation data erase
  the decisive phase.
- A zeta factor can be replicated through Rankin--Selberg convolutions only on
  the contragredient diagonal, exactly where fixed-partner family independence
  is lost.
- The odd-squarefree boundary exchange graph can pair opposite Mobius signs,
  but once a matching saturates the smaller parity class its deficiency is
  `|M(N)|` tautologically.  The graph does not estimate the imbalance.

The squarefree fugacity polynomial adds a useful quantitative distinction.
Hurwitz half-plane stability would give only a linear Mertens bound.  The
needed theorem is an accumulated root-displacement estimate of logarithmic
size.  Qualitative location and quantitative cancellation must not be
conflated.

An abstract continuity lemma packages the remote-zero versions of these
failures.  If a carrier `Phi` sends a divisor with an inserted off-line quartet
at height `T` back to the baseline carrier as `T -> infinity`, then every
finite collection of continuous inequalities having strict baseline margins
also accepts that quartet for all large `T`.  On an admissible class containing
these synthetic divisors, such a carrier can characterize critical-line
containment only through an infinite family with collapsing margins or a
discontinuous/quantized invariant.  A zeta-specific theorem may instead
exclude the perturbations by independent arithmetic.  Finite-moment cones,
bounded-resolution metrics, and fixed strict certificates are instances of
this lemma.

The full audit, exact finite gates, and next self-prompts are recorded in
`results/TWO-WAVE-ORTHOGONAL-FAIL-FAST-2026-08.md`.

## 10. Boundary-exchange follow-up: locality fails before parity enters

The deterministic `p <-> qr` collar experiment adds a more sharply delimited
negative result.  It is not merely that maximum matching repackages `M(N)`.
Several attempts to prescribe the pairing before counting signs fail for an
unsigned reason.

- Every fixed dictionary with summable endpoint-cylinder weights leaves a
  positive-density family with no applicable template.  This includes every
  bounded-incidence dictionary of finite prime-set substitutions, of any
  arity, that flips Mobius sign and preserves the collar.
- Requiring the three changed primes to stay within a bounded dyadic range
  forces all of them into a fixed finite set, again leaving positive density.
- One-shot lexicographic selectors collapse large common-core fibers: prime
  and semiprime families make the exception count at least
  `N/log N` or `N log log N/log N`, and fixed palettes can fail on a linear
  family.

These obstructions precede the sieve parity problem: they count vertices that
cannot be paired or collide without using the sign imbalance at all.  Their
common cause is **local supply versus global exclusivity**.  A scale-compatible
edge is easy to find for one factor set, but many vertices see the same target;
resolving those collisions requires an `N`-dependent multiscale allocation
with history.  Once that history is admitted, the only surviving simple rule
is a global sequential greedy, and no unsigned sublinear defect estimate is
known.  Thus the experiment has located the exact point at which a local
combinatorial explanation ends and Mertens-scale global allocation begins.

The proof and guarded scouts are in
`results/MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`.

## 11. Conditioned Bagchi follow-up: continuation is not a tail limit

The fixed-prime-conditioned recurrence branch is now pruned more sharply than
the original rare-event comparison suggested.  For each fixed cutoff, the
de-Eulerized Bagchi limit is a large-prime random Euler product.  It is an
exponential of a holomorphic random series and is therefore zero-free in the
half-critical strip.  If the deterministic continued remainder inherits an
off-line zeta zero, its Rouche neighborhood is disjoint from that support.
The desired relative conditional frequency is exactly zero, not merely too
small for Chebyshev subtraction.

The Helson calibration makes the locality failure explicit.  Helson zeta
functions can have prescribed strip zeros after continuation, and any finite
set of their prime phases can then be reset exactly to `1` by a finite
zero-free Euler multiplier without changing the divisor.  Thus finite-prime
Haar independence, ordinary Euler-tail concentration, and meromorphic
continuation coexist with arbitrary off-line zeros.

This is another instance of completion preceding localization, but with a
new exact formulation:

> Analytic continuation through `Re(s)=1` is not the locally uniform limit of
> the ordinary zero-free Euler tails on a zero-containing compact.

Rouche proves a positive boundary separation from every such tail.  The only
logical survivor is a diagonal shrinking-target regime in which the prime
cutoff grows with the translation height; it abandons the fixed-block Bagchi
limit and would need a zeta-specific zero-bearing small-ball theorem.  The
quantitative gate is recorded in
`results/BAGCHI-CONDITIONED-TAIL-NOGO-2026-08.md`.

The joint phase convention used there has also been checked at theorem and
proof level.  With the empirical coordinate `p^(i tau)`, the random finite
coordinate must be conjugated relative to the random Euler phase.  This
corrects the exact coupling in Endo's arXiv:2410.17575v1 while preserving its
product support and qualitative universality consequences.  The one-prime
witness and a second compact-open support repair are in
`results/ENDO-HYBRID-JOINT-LIMIT-CORRECTION-2026-08.md`; neither correction
changes the fixed-cutoff no-go above.

## 12. Greedy matching follow-up: allocation is not imbalance

The value-ordered boundary greedy has now passed its intended fail-fast audit.
Its blocker DAG is exact, but its unmatched count decomposes as

```text
R_g(N)=|M(N)|+2D_g(N),
```

where `D_g` is the smaller-side allocation defect.  Alternating paths and
Hall expansion address only `D_g`.  At every retained checkpoint through
`N=200000`, disjoint length-three paths eliminate all of `D_g` and leave
exactly `|M(N)|`.

This also merges two supposedly different branches.  If `Q_N(z)` enumerates
the collar by number of prime factors, every matched edge contributes
`z^r(1+z)`, so

```text
Q_N(z)=(1+z)A_N(z)+U_N(z),
U_N(-1)=M(N),                 U_N(1)=R_g(N).
```

The initial even/odd factor-`2` cancellation gives the same decomposition of
the squarefree fugacity polynomial.  Thus matching and fugacity displacement
both expose the singular `z=-1` endpoint; neither controls it merely by
removing positive multiples of `1+z`.  Complete-bipartite core fibers explain
why dense blockers, terminal residuals, and excellent matching efficiency do
not constrain the majority imbalance.  The detailed proof and memory-bounded
certificates are in
`results/MOBIUS-GREEDY-DEPENDENCY-VERDICT-2026-08.md`.

## 13. Global-trace follow-up: duality is not positive polarization

The finite two-prime cohomological toy closes another recurring escape hatch.
The connected Euler logarithm correctly produces pure prime-power von
Mangoldt terms and removes mixed composites, but a connected character with
no mixed monomials is additive across its place variables.  In a finite
equivariant Hilbert complex, an invariant positive metric then orthogonalizes
the distinct place weights.  Honest trace data split as a direct sum;
supertrace cancellation can hide mixed states but supplies no positivity.

The decisive distinction has an exact `2x2` form.  An off-line pair
`1/2+-a` preserves the alternating functional-equation pairing for every
`a`, yet for `a!=0` it admits no positive metric satisfying the Hodge adjoint
law.  In general,

```text
there exists G>0 with A*G+GA=G
```

if and only if `A` is diagonalizable with spectrum already on
`Re(s)=1/2`.  Choosing the metric after seeing the generator is therefore the
finite critical-line assertion itself.  This unifies several prior failures:
functional equations, signed trace identities, and connected cancellation
are equality structures; the positive polarization is independent order
data.

The finite equivariant class is pruned, not the infinite semilocal program.
A revival needs a canonical metric on the coupled all-place object, defined
without zeros or the Weil-form spectrum and compatible as places are added.
The proof, exact `{infinity,3,5}` fixture, Lean countermodel, and positive
control are in
`results/GLOBAL-TRACE-POLARIZATION-FINITE-GATE-2026-08.md`.

## 14. Quantized-phase follow-up: the integer exists on the zero side only

The last proposed escape from remote-defect continuity was an integer-valued
completed phase.  It separates two issues that had previously been conflated.

On the divisor side, the construction works.  The shifted phase
`P(x-ia)/P(x+ia)` has winding equal to the number of roots in the horizontal
strip, so one simple functional-equation quartet changes the whole-line
winding by four.  This confirms the intuition that a quantized invariant
cannot fade merely because the quartet is moved to high ordinate.

What fails is the zero-independent arithmetic realization.  Every natural
finite-prime loop is contractible.  The literal two-sided shifted Euler
product is not bounded in mean square, while the functional-equation-
normalized unit phase has only a `B^2` limit below `Re(s)=1`.  That weak limit
has no winding class and cannot retain a finite or zero-density divisor.
Uniform convergence, which would preserve the index, begins only in the
ordinary Euler half-plane and yields the trivial class.  Contour continuation
does retain the integer, but then computes the zero divisor directly.

This adds a fifth reusable failure mechanism to the earlier four:

> **index/topology incompatibility.**  Finite arithmetic approximants may be
> continuously trivial even when the analytically continued target has a
> nontrivial divisor.  The weak topology in which the approximants converge
> need not support the target's integer invariant, while strengthening the
> topology demands exactly the missing global continuation theorem.

The point is stronger than the generic observation that Euler products fail
below `Re(s)=1`: the exact finite-torus norms identify which of two natural
phase normalizations fails existence and which loses topology.  Together
with the remote-quartet lemma, this gives a clean trilemma between weak mean
closure, uniform/Fredholm closure, and divisor counting.

The only honest survivor is no longer “find a phase.”  It is to exhibit a
specific completion-native equivariant or semifinite relative index with an
arithmetic representative, non-density sensitivity, and independent
all-place summability.  Existing generalized-Nevanlinna inertia, localized
Weil Morse index, Burnol scattering degree, and signed spectral flow do not
meet all three conditions.  The complete audit is in
`results/QUANTIZED-PHASE-INDEX-VERDICT-2026-08.md`.
