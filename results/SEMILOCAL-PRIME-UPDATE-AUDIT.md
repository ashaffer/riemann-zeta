# Semilocal one-prime update audit

Status: monotone Sonin compression and positive prime-update Schur complement
are falsified; semilocal stability survives only as an isomorphism, 2026-08-01.

## 1. Exact semilocal transport

For a finite set of places `S` containing infinity, Connes--Consani--Moscovici
construct the semilocal Sonin space and prove that

`theta_S : Sonin_lambda(R) -> Sonin_lambda(X_S)`

is a Hilbertian isomorphism.  For one added prime `p`, Mellin coordinates are
multiplied by the inverse Euler factor

`1-p^(-1/2-is)`,

while the cyclic spectral measure is multiplied by

`w_p(s)=|L_p(1/2+is)|^2`

`      =1/(1+p^(-1)-2p^(-1/2) cos(s log p))`.

This proves stability of the Sonin *space*.  It does not give a nesting of
orthogonal projections in one fixed metric, because both the realization and
the cyclic measure change.

## 2. Ambient Loewner obstruction

Writing `q=p^(-1/2)`, one has

`w_p(0)=1/(1-q)^2 > 1`,

`w_p(pi/log p)=1/(1+q)^2 < 1`.

Thus the Radon--Nikodym derivative crosses one during every Euler period.  The
new multiplication metric is neither above nor below the old metric.  Lean
proves this exact sign change in
`RHBridge.SemilocalPrimeWeight.localWeight_crosses_one` without zeta or RH
axioms.

Any proposed Loewner inequality between the full multiplication operators is
therefore false.  Localizing spectral vectors near the two phase arcs gives
both signs.

## 3. Natural moment-filtration test

One might hope that restriction to the cyclic/prolate filtration repairs the
sign.  The script `src/semilocal_prime_metric_scan.py` tests the canonical
even-monomial Gram spaces for the archimedean measure

`|Gamma(1/4+i s/2)|^2 ds`

and its one-prime update.  It reports generalized eigenvalues of
`G_(infinity,p)-G_infinity` relative to `G_infinity`.

Representative results are

| prime | dimension | minimum update | maximum update |
|---:|---:|---:|---:|
| 2 | 2 | `-0.205` | `6.95` |
| 2 | 4 | `-0.554` | `7.43` |
| 3 | 2 | `-0.191` | `2.87` |
| 3 | 4 | `-0.358` | `3.10` |
| 5 | 3 | `-0.210` | `1.39` |
| 7 | 3 | `-0.054` | `0.93` |

The update is already indefinite in the smallest natural spaces for `p=2,3`
and becomes indefinite by dimension three for `p=5,7`.  This is not a
high-frequency or vanishing-margin phenomenon.

## 4. Schur-complement consequence

Because the Sonin spaces are isomorphic rather than nested and their
transported metrics have an indefinite difference, there is no canonical
positive block

`new compression = old compression + positive prime block`.

Correspondingly, a positive Schur complement for “adjoining one place” cannot
be obtained from the natural cyclic filtration.  Any such complement would
need additional off-diagonal correction terms mixing the prime with the
archimedean channel; positivity of that corrected block is the semilocal Weil
problem, not a consequence of space stability.

## 5. Verdict

The requested monotone semilocal trace comparison fails both necessary gates:

1. the exact local-factor metric is not Loewner ordered;
2. its canonical finite moment compressions are indefinite.

The 2023 stability theorem is still highly relevant: it says adjoining primes
does not change the abstract Sonin space.  But all arithmetic difficulty moves
into the transported metric and scaling action, precisely where the signed
Euler oscillation occurs.

This prunes monotone prime-by-prime extension.  A surviving semilocal approach
must exploit cancellation across a **complete collection of places or Euler
phases**, rather than demand positivity from each update.  The next testable
object is an averaged or paired update whose Radon--Nikodym multiplier is
pointwise at least one after including the functional-equation partner.  If no
nontrivial finite pairing has this property, only the irreducibly global
completion remains.

Primary source: Connes--Consani--Moscovici,
*Zeta zeros and prolate wave operators*,
<https://arxiv.org/abs/2310.18423>, especially Propositions 4.6--4.7 and
Theorem 4.6.
