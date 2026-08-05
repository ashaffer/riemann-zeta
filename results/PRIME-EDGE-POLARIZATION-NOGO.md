# Prime-edge polarization cost and no-go gate

Status: the optimal local Gram cost is a Lean theorem; the displayed
zeta-residual failure is presently a floating-point falsifier rather than an
analytic or interval-certified theorem, 2026-08-05.  A fully nonlocal
completed polarization remains open.

Roadmap note: the nonlocal Mobius/Poisson lift proposed at the end was pursued
in later audits.  Its pure mixed-pairing gate is formalized in
[`GlobalMobiusCancellation.lean`](../lean/rhbridge/RHBridge/GlobalMobiusCancellation.lean);
no positive completed factorization resulted.

## Exact polarization

For a prime-power translation `T_h`, `h = log n`, the negative autocorrelation
cross term has the elementary completion

`w ||f-T_h f||^2 = w||f||^2 + w||T_h f||^2
                     - 2w Re <f,T_h f>`.

Thus the prime term can be embedded in a positive weighted graph Laplacian, at
the cost of one diagonal copy of `w` at each endpoint.  The completed Weil
form then splits exactly as

`Q = (prime graph Laplacian) + (pole + archimedean - graph degree)`.

This is the tropical graph residual previously tested in
`src/tropical_graph_residual.py`.

## New optimality theorem

The graph-degree cost is unavoidable, not an artifact of choosing difference
squares.  If vectors `u,v` in any real Hilbert space reproduce cross mass
`<u,v>=w>=0`, positivity gives

`0 <= ||u-v||^2 = ||u||^2 + ||v||^2 - 2w`.

Hence their total endpoint diagonal cost is at least `2w`.  Equality is attained
by `u=v` with norm squared `w`, exactly the difference-square construction.
Splitting an edge among arbitrarily many auxiliary Gram coordinates changes
neither the statement nor the bound: take `u` and `v` to be the direct sums of
all endpoint vectors.

The identity, Hilbert-space lower bound, scalar rank-one version, and sharpness
are kernel-checked in `RHBridge.PrimeEdgePolarization`.  They use no RH or zeta
axiom.

## Independent residual check

Running

```text
python3 src/tropical_graph_residual.py --dimension 31
```

gives

| support | minimum Weil Ritz value | minimum residual | minimum graph Laplacian |
|---:|---:|---:|---:|
| 1.750 | 3.96e-5 | -0.455 | -1.3e-18 |
| 2.485 | 3.15e-6 | -1.255 | -9.7e-18 |
| 2.996 | 2.51e-6 | -1.900 | 4.7e-17 |
| 3.555 | 1.37e-6 | -2.983 | -6.7e-17 |

The observed residual failure is order one and grows with support, so it is a
strong and numerically stable falsifier rather than a tiny-margin effect.  The
table is nevertheless ordinary floating-point evidence, not a proof that the
continuum residual has a negative direction.

## Exact scope and remaining certificate

The exact theorem rules out lowering the endpoint diagonal cost for a
decomposition which:

1. assigns Gram channels independently to each prime-power edge;
2. reproduces that edge's negative autocorrelation cross coefficient; and
3. asks the pole/archimedean diagonal to pay the resulting endpoint costs.

It includes unequal endpoint weights, higher-rank auxiliary spaces, multiple
squares per edge, and direct sums over places.  To turn that optimality result
into a zeta-specific no-go theorem, one must additionally prove—analytically
or by a frozen outward-rounded certificate—that the resulting
pole/archimedean-minus-degree residual has a negative direction.  The table
above has not yet discharged that obligation.

Even after that witness is certified, the result would **not** rule out a
factorization with essential cross-couplings between
distinct primes and the archimedean channel.  Such couplings can redistribute
diagonal mass by interference, but they must cancel all unwanted cross terms
in the final explicit formula.  Producing that cancellation is new content;
declaring the completed Weil operator to have a square root is circular.

## Surviving target

Seek an explicitly defined nonlocal transform `U`, derived before any
positivity claim from Poisson/co-Poisson or an adelic incidence relation, such
that

`Q(f,g) = <Uf,Ug>`

on the arithmetic smooth core.  The next fail-fast gate is an exact
off-diagonal cancellation identity: when `U` is expanded by places, all
prime-prime and prime-archimedean cross terms absent from Guinand--Weil must
cancel algebraically.  If that identity cannot be obtained without using the
zero-side form or an RH-equivalent positive kernel, the global Gram path is
also circular.
