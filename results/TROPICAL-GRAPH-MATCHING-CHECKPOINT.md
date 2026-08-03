# Tropical graph matching checkpoint

Status: naive graphic-matroid mechanism falsified, 2026-07-31.

## Proposed mechanism

In a localized nonnegative hat basis, the prime part of the Weil matrix is a
matrix `P` with nonnegative entries.  With

`D = diag(P * 1)`

there is an exact decomposition

`Q = (D-P) + ((Q+P)-D)`.

The first term is the weighted Laplacian of the prime-shift graph and is
positive semidefinite.  If the residual `R=(Q+P)-D` were positive on the form
domain (or on the two moment constraints), ordinary graph potential theory,
chip firing, and the Lorentzian spanning-tree polynomial would give a
non-circular positivity mechanism.

## Test

The script `src/tropical_graph_residual.py` assembles the normalization-audited
hat Galerkin form and reports the generalized minimum of the residual.  A
representative run is

```text
python3 src/tropical_graph_residual.py --dimension 31
```

with output:

| support | minimum Weil Ritz value | minimum residual value |
|---:|---:|---:|
| 1.750 | 3.96e-5 | -0.455 |
| 2.485 | 3.15e-6 | -1.255 |
| 2.996 | 2.51e-6 | -1.900 |
| 3.555 | 1.37e-6 | -2.983 |

The graph Laplacian minimum is zero to floating-point error, as it must be.
The hat-space Weil values are only coarse Ritz upper bounds and are not used
as precise margin estimates here.  The residual obstruction is order one and
grows with support, so it is not a resolution artifact near the tiny Weil
ground margin.

## Meaning

The prime-shift graph by itself does not carry the needed Hodge inequality.
The actual small positive Weil form arises from a large cancellation between
the graph degree term and an indefinite archimedean/pole residual.  Ordinary
chip-firing or a graphic-matroid basis polynomial sees the Laplacian but not
this cancellation.

There is also a structural obstruction to the most obvious gain-graph repair.
Label the edge `x -> x+log(n)` by the multiplicative gain `n`.  These gains are
ratios of vertex potentials `exp(x+log(n))/exp(x)`, so the gain around every
closed cycle is one.  The associated frame matroid therefore reduces to the
ordinary graphic matroid and adds no new Hodge data.

This kills the naive claim that modern Lorentzian theory can simply be applied
to the prime adjacency graph.  It does not kill the full characteristic-one
Riemann--Roch route: a successful object would have to incorporate the
archimedean place, pole divisor, and relative trace in its incidence algebra
before invoking Hodge--Riemann.  Merely declaring their completed intersection
polynomial Lorentzian would be equivalent to the desired Weil signature and
would be circular.

## Surviving finite target

The remaining non-circular geometric question is narrower:

> Is there a combinatorially defined relative Chow ring for the pair
> `(adele classes, ideles)` whose degree map gives `Tr_X-Tr_Y`, and whose
> Frobenius divisor pairing reproduces the archimedean/pole residual as well as
> the prime graph?

This is materially closer to Connes--Consani's stated missing intersection
theory than the original finite-prime Lorentzian proposal.  It is not presently
a fail-fast target; constructing the relative degree map is the main theorem.
