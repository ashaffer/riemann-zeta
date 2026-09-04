# QP carrier: residual-block triangle matchings and the expander gate

**Date:** 2026-08-24  
**Verdict:** a new exact mask-preserving decomposition is proved, but it does
not by itself prove the sharp four-cycle estimate.

Partition the physical residuals

```text
rho(a,b,c)=8abc-q^3,             |rho|<=qD
```

into intervals shorter than eight times the smallest shell node.  Every
block is a vertex-disjoint union of actual three-prime edges.  Thus the
`q^2` packet decomposition has a completely physical interpretation as an
ordered family of triangle matchings.

The missing theorem is now an expansion statement for the **sum** of these
matchings.  Matching structure alone is insufficient: a resolvable Steiner
triple system is an exact abstract family of triangle matchings whose union
has a large nonconstant or component mode.  Consequently the desired gain
must use how the block index is tied to the integer product `abc`, not merely
pair uniqueness, residual orthogonality, or noncommutative square functions.

## 1. Exact short-block lemma

Let `S` be the actual prime-power shell, put `p0=min(S)`, and let `I` be a
half-open interval of length

```text
L<8p0.                                                   (1.1)
```

Suppose two unordered shell triples `E={a,b,c}` and `E'={a',b',c'}` have
residuals in `I`.  If they share a shell node `p`, write

```text
abc=p*m,              a'b'c'=p*m'.                     (1.2)
```

Then

```text
|rho(E)-rho(E')|=8p|m-m'|<L<8p.                        (1.3)
```

Since `m-m'` is an integer, (1.3) forces `m=m'`.  Unique factorization and
the one-power-per-prime-base property of the project shell then imply that
`E=E'` as multisets.  Hence distinct triples in one block share no vertex.

### Theorem 1 (physical triangle-matching decomposition)

For every partition of `[-qD,qD]` into intervals satisfying (1.1), the
actual factorization hypergraph in each interval is a disjoint union of
three-vertex edges.  Equivalently, its weighted carry matrix is block
diagonal with one `3 x 3` weighted block per retained integer product.

The theorem retains every part of the physical mask.  There is no box
completion, modular alias, translated window, or loss of the common
carrier.

At the project shell `p0` is a fixed positive multiple of `q`, so blocks of
length `q` are legal.  There are `O(D)` such blocks.  These are exactly the
additive fibres `rho=qv+u` which appeared in the conductor-`q^2` audit.

## 2. Relation with the `q^2` vector square problem

Write `A_v(z)` for the weighted adjacency matrix of the triples in residual
block `v`.  The full physical carry matrix is

```text
A_z=sum_v A_v(z).                                      (2.1)
```

Every `A_v(z)` is a direct sum of weighted triangle matrices.  In
particular, its rows do not compete inside one residual block.  All
nontrivial covariance therefore comes from

```text
A_v(z)^* A_w(z),              v != w.                  (2.2)
```

This is the physical version of the `K_eta(t-s)` cross-Gram in the hybrid
character--Mellin formulation.  A successful GPT-7-style theorem would
have to prove an almost-orthogonality or coefficient-dependent polar
decomposition for the ordered family `(A_v)_v`, uniformly after the
admissible tangent/parabolic incidence masks are inserted.

## 3. Why a generic matching square function is false

The affine plane over `F_3` is a Steiner triple system on nine points.  Its
twelve lines split into four parallel classes, each class consisting of
three vertex-disjoint triples.  Thus it has exactly the local structure of
Theorem 1.

For the flat normalized vector `z_i=1/3`, however, its weighted adjacency is

```text
A_z=(J-I)/3.                                            (3.1)
```

It has a singular value `8/3`, and its fourth Schatten trace is much larger
than the vertex hyperedge degree `4`.  Larger resolvable Steiner systems
give the corresponding asymptotic obstruction.  Therefore no inequality
using only

```text
each residual block is a matching,
the blocks have disjoint edge supports,
each pair occurs at most once
```

can prove the sharp four-cycle bound.

The arithmetic feature absent from the Steiner model is

```text
v=floor((8abc-q^3)/q).                                  (3.2)
```

In particular, if two blocks contain triples sharing `p`, their block
separation records the small integer difference of the complementary
products.  Exploiting this simultaneous ordering at all vertices is exactly
the selected shifted-semiprime/two-inverse dispersion problem.

## 4. Binary ledger

```text
physical residual blocks of length q are triangle matchings: PROVED;
within-block covariance obstruction:                         REMOVED;
generic matching-family square function:                     FALSE;
arithmetic ordered-block expansion:                          OPEN;
post-peeling mask-stable version:                             OPEN;
new unconditional fourth-trace exponent:                     NONE;
sharp four-cycle bound:                                       NOT PROVED.
```

The exact finite replay is

```text
src/qp_residual_block_triangle_matching.py
src/test_qp_residual_block_triangle_matching.py
```

