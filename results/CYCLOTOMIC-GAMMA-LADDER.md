# Cyclotomic reconnaissance: the archimedean gamma ladder

Status: exact determinant match; cohomological realization open, 2026-08-01.

## Exact calculation

Let `A_s` have the formal one-sided spectrum

`s, s+2, s+4, ...`.

Its spectral zeta function is

`zeta_A(w) = sum_(n>=0) (s+2n)^(-w)`

`          = 2^(-w) HurwitzZeta(w,s/2)`.

Using the classical values

`HurwitzZeta(0,a)=1/2-a`,

`HurwitzZeta'(0,a)=log Gamma(a)-(1/2)log(2pi)`,

gives the zeta-regularized determinant

`det_zeta(A_s) = exp(-zeta_A'(0))`

`              = 2^(1/2-s/2) sqrt(2pi) / Gamma(s/2)`.

Consequently

`pi^(-s/2) Gamma(s/2)`

` = det_zeta(A_s)^(-1) * 2 sqrt(pi) (2pi)^(-s/2)`.

The discrepancy is only the elementary exponential normalization allowed in a
regularized determinant.  The script `src/archimedean_gamma_determinant.py`
checks the differentiated Hurwitz-zeta definition against the closed form at
complex points to about 50 decimal digits.

## Why this matters

Degree-two periodicity is fundamental in Hochschild and cyclotomic homology.
Real topological Hochschild homology `THR` supplies genuine `C2`-equivariant
data and is defined for `Z` and for schemes with involution.  Thus the spacing
of the gamma factor is exactly the spacing one would expect from a connective
degree-two homotopy ladder.

This is the first concrete evidence for the portfolio's proposed
archimedean-cyclotomic bridge.  It is stronger than observing that gamma is a
regularized product: the required grading agrees with the native periodicity
of the candidate cohomology theory.

## The immediate obstruction

Periodic topological cyclic homology typically has a *bi-infinite* periodicity
generator.  A symmetric two-sided ladder produces sine-type determinants, not
the one-sided gamma factor.  The calculation therefore identifies the precise
next gate:

> Does the connective filtration, real fixed-point structure, or a canonical
> t-structure on `THR/TC(Z)` select the one-sided degree-two ladder in a way
> compatible with cyclotomic Frobenius?

Choosing the positive half by hand would merely insert the gamma factor.  It
must arise functorially from connectivity, a boundary condition, or the real
place.

## Minimal completed cohomology specification

A viable object for `Spec Z` must provide:

1. finite-prime cyclotomic Frobenius and the Euler closed-orbit factors;
2. the above one-sided archimedean ladder;
3. finite degree-zero and degree-two modes accounting for the factors `s` and
   `s-1`;
4. a determinant identity for completed zeta, with no factor defined using its
   zeros;
5. a positive duality pairing on the middle object with
   `Theta^*+Theta=1`.

Items 1--4 identify the spectrum.  Item 5 would force every middle eigenvalue
to have real part `1/2` and hence prove RH.  The determinant calculation above
advances item 2 only; it does not supply item 5.

## Bayesian update

The cyclotomic route remains extremely difficult, but its archimedean gate is
now a concrete construction problem rather than a vague analogy.  The prior
for obtaining a meaningful new cohomological model should increase modestly;
the prior for a complete RH proof should not materially change until a
positive polarization appears.
