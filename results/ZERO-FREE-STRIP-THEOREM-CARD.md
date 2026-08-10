# Zero-free strip theorem card

## Status

This document specifies a target theorem and its exact dependency split. It is
not a proof of a zero-free strip and does not assert the required arithmetic
moment estimate.

## Target

Prove that there is a constant `eta > 0` such that every nontrivial zero
`rho = beta + i gamma` of the Riemann zeta function satisfies

```text
eta <= beta <= 1 - eta.
```

The symmetry `rho -> 1 - conjugate rho` means it is enough to prove the upper
bound `beta <= 1 - eta` with the same uniform `eta`.

## Fixed-window displacement parameter

Let

```text
Delta = sup_rho |Re(rho) - 1/2|,
```

where the supremum ranges over nontrivial zeta zeros. A bound

```text
Delta <= 1/2 - eta
```

is exactly the desired closed strip.

The Lean module `RHBridge.FixedWindowStripReduction` formalizes this elementary
last step without importing the Guinand--Weil or Weil-criterion axioms.

## Full-frequency completed moment gate

Fix a moment power `p >= 2`. The analytic fixed-window program is intended to
construct a completed local transform `F_N(t)` such that its full-frequency
moment

```text
U_p(N) = integral_R |F_N(t)|^p dt
```

has exponential rate `p * Delta` after the normalization used by the completed
microblock. The desired arithmetic input is a power saving

```text
U_p(N) <= C_epsilon * N^(p/2 - kappa + epsilon)
```

for every `epsilon > 0`, for some fixed `kappa > 0`, uniformly for all
sufficiently large `N`.

Provided both statements are proved with matching normalization, exponent
comparison gives

```text
p * Delta <= p/2 - kappa,
Delta <= 1/2 - kappa/p,
```

and hence the uniform zero-free strip

```text
kappa/p <= Re(rho) <= 1 - kappa/p.
```

For `p = 4`, the strip width is `eta = kappa/4`. The numerical helper
`src/r71_fixed_strip_moment_probe.py` records the same exponent ledger but is
explicitly diagnostic only.

## Required theorem split

A valid proof must establish the following components independently.

### A. Analytic detector theorem

Prove that the completed fixed-window transform has full-frequency moment
exponent at least `p * Delta`. This requires an exact explicit formula,
normal convergence or a justified symmetric limiting procedure, and a
non-cancellation argument at every off-line zero. No zero-free strip may be
assumed in this step.

### B. Arithmetic moment theorem

Prove the power-saving upper bound for the completed transform directly from
its arithmetic coefficients. This is the genuinely new input. It must include
all continuum/centering terms and all multiplicative collisions; independent
random-phase or finite-height numerical comparators are not substitutes.

### C. Exponent comparison

Deduce the strip from A and B. This is elementary and is the part formalized in
`RHBridge.FixedWindowStripReduction`.

## Non-circularity requirements

The arithmetic theorem may use unconditional published results if each is
stated in an explicit literature-boundary file with precise normalization and
source. It may not use:

- RH or an equivalent all-support Weil-positivity statement;
- a pre-existing fixed zero-free strip;
- the target moment estimate itself under another name;
- a zero-side identity outside the test class for which convergence has been
  proved;
- a finite-range fit as an asymptotic bound.

## Falsification gates

Before attempting a large proof, test these necessary conditions.

1. The completed center term is retained with its sign and normalization.
2. Boundary microblocks and multiplicative-product collisions are included.
3. The detector lower bound survives multiple zeros and zeros sharing a real
   part.
4. Every interchange of zero sums, integrals, limits, and moments has a stated
   convergence theorem.
5. The power saving is uniform in all smoothing, truncation, and localization
   parameters that are later optimized.

## Milestones

1. Kernel-check the compact-support autocorrelation cutoff and the abstract
   strip reduction.
2. Prove the detector theorem for one fixed smooth window.
3. State the completed fourth-moment estimate with all constants and
   quantifiers.
4. Import only genuinely published analytic-number-theory inputs through the
   consolidated trust boundary.
5. Prove any positive `kappa`; this yields a genuine fixed strip.
6. Improve `kappa`, or prove a family approaching `p/2`, to narrow the strip
   toward the critical line.

## Current open statement

The present project does not yet prove component B. Any claim of a uniform
zero-free strip must therefore remain conditional until the completed
full-frequency moment saving is established and its normalization is matched
to component A.
