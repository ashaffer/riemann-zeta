# Random-sieve Walsh-energy barrier

Status: the random-sieve density survives, but entropy amplification of the
pole is pruned, 2026-08-01.

Retain the setup of `RANDOM-SIEVE-RESONANCE-CAPACITY.md`.  For independent
prime selectors `X_p` and a hypothetical zero `rho=beta+i gamma`, the pole
residue is multiplied by

`R = product_p r_p^(X_p)`, where `r_p=(1-p^(-rho))^(-1)`.

For large `p`,

`r_p-1 = p^(-rho) + O(p^(-2 beta))`.

If `theta_p=P(X_p=1)`, the normalized one-prime variance is therefore

`theta_p(1-theta_p)|r_p-1|^2 = O(theta_p p^(-2 beta))`.

But `beta>1/2`, so even without sparsifying,

`sum_p theta_p p^(-2 beta) <= sum_p p^(-2 beta) < infinity`.

Standard product-martingale or Walsh-basis calculations then imply:

1. whenever the mean product is defined and nonzero, the normalized residue
   multiplier has finite total `L2` variation;
2. its Walsh coefficients have summable squared mass;
3. the Walsh energy involving primes above `y` tends to zero as `y->infinity`.

For the selector `theta_p=p^(-a)` with `1-beta<a<1`, these conclusions hold
alongside divergent selector entropy

`H_y ~ a sum_(p<=y) p^(-a) log p -> infinity`.

Thus the new prime decisions add entropy but asymptotically no orthogonal pole
energy.  The pole survives on almost every positive-density sieve, but it
survives as essentially the same finite-energy common mode rather than as
independent information replicated across branches.

## Generality of the obstruction

This failure is not caused by the particular choice `theta_p=p^(-a)`.  For
every independent selector with probabilities at most one, the pole increment
is square-summable solely because an off-line zero still has `beta>1/2`.
Consequently no Hilbert-space, variance, mutual-information-at-small-bias, or
ordinary Walsh-energy argument can extract extensive information from these
Euler residue fluctuations.

For a *dense formal* prime tree the critical non-Hilbert exponent would be
`r=1/beta<2`.  But an honest sparse sieve whose Euler multiplier converges
absolutely near `rho` has increments in `ell^1`, so even this endpoint is
finite.  Dense centered products can recover divergent endpoint variation,
but then cease to be positive-density Möbius restrictions and can coexist
with arbitrary prescribed poles.  See `NONHILBERT-ENDPOINT-AUDIT.md`.

## Verdict

The random-sieve construction is a valid new propagation theorem and a useful
description of why ordinary density was the wrong first measure.  Its proposed
use as an entropy contradiction nevertheless fails: divergent branch entropy
and pole information decouple.  The natural non-Hilbert endpoint also fails
the subsequent audit; changing probability weights cannot repair it.
