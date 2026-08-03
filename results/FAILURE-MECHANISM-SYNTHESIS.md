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
