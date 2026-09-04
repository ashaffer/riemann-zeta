# QP weighted triangles: diffuse-bin square gain and cross-Gram multiplicity gate

**Date:** 2026-08-24  
**Verdict:** the factor-two-bin refinement is valid.  If the coefficient
support has size `M`, the randomized residual-block fourth moment is

```text
O(Delta min(1,Delta/M)) ||z||2^4.                    (0.1)
```

There is also an exact packet-safe deterministic criterion: if `mu` is the
largest number of nonzero cross-block wedge atoms landing in one matrix
cell, then

```text
||sum_I A_I(z)||S4^4
 <<(1+mu) Delta min(1,Delta/M) ||z||2^4.             (0.2)
```

At the critical diffuse support `M=D^(15/8)` and `Delta<=D`, a violation of
the desired `O(D)` bound therefore forces `mu>=D^(7/8-o(1))`.  This is a
substantially stronger inverse conclusion than merely finding a mildly
large cross-Gram.

The tangent/Hankel integer fixture has `mu=L` and attains equality in the
entrywise multiplicity estimate.  Thus (0.2) is the correct combinatorial
gate, but bounding `mu` without first extracting coherent tangent packets
is impossible in the integer product-window model.  The actual-prime
inverse theorem remains open.

No sharp four-cycle theorem is proved here.

## 1. Scope of the triangle theorem

Let the all-distinct edges be partitioned into residual classes of diameter
less than `8 min(S)`, and write

```text
M_e(i,j)=z_k,  M_e(i,k)=z_j,  M_e(j,k)=z_i,
A_I=sum_(e in I) M_e.                                (1.1)
```

On the actual shell the required hypotheses are valid:

1. If two distinct fine-window triples shared two nodes, their residuals
   would differ by at least `8 min(S)^2`, whereas two residuals in the full
   window differ by at most `2qD`.  The active scale has
   `8 min(S)^2>2qD`, so the all-distinct hypergraph is globally linear.
2. If two triples in one short class share `p`, their residual difference is
   `8p(xy-x'y')`.  Its absolute value is below `8p`, so `xy=x'y'`.
   Unique factorization, together with the fact that the ratio-`e^.4<2`
   shell contains at most one power of each prime base, makes the two
   unordered triples equal.  Hence every class is a vertex matching.

Repeated-node triples are not a simple three-uniform linear hypergraph and
must remain in their already separated sector.  Arbitrary integer shells do
not inherit the unique-factorization matching conclusion; the tangent
fixture below is checked directly.

## 2. Complex Rademacher pairing is sound

For complex symmetric, not necessarily Hermitian, matrices `A_I`, put

```text
R=sum_I A_I^*A_I,                 L=sum_I A_I A_I^*,
C=sum_(I,J) tr((A_I^*A_J)^2),     U=sum_I ||A_I||S4^4.
```

The exact real-Rademacher pairing identity is

```text
E ||sum_I epsilon_I A_I||S4^4
 =||R||HS^2+||L||HS^2+C-2U.                          (2.1)
```

No reality assumption on `z` is needed.  For every complex matrix `B`,

```text
|tr(B^2)|<=||B||HS^2,                                (2.2)
```

and summing (2.2) with `B=A_I^*A_J` gives `|C|<=||L||HS^2`.
Thus

```text
E ||sum_I epsilon_I A_I||S4^4
 <=||R||HS^2+2||L||HS^2.                             (2.3)
```

This verifies both the complex phases and the constant `42` in the coarse
bound `14 Delta+2(14 Delta)`.

## 3. Refined factor-two square theorem

Assume `z` has `M` nonzero entries and their absolute values differ by at
most a factor two.  Put `s=||z||2`.  Then

```text
max_u |z_u|^2 <=4s^2/M.                              (3.1)
```

For a pivot `p`, define

```text
d_e(p)=sum_(u in e, u!=p)|z_u|^2,
S_p=sum_(e contains p)d_e(p).                        (3.2)
```

Global linearity makes all complementary vertices in (3.2) distinct.
There are at most `2 Delta` of them.  Hence

```text
S_p<=min(1,8Delta/M)s^2,                              (3.3)
sum_p S_p=2 sum_e sum_(u in e)|z_u|^2
         <=2Delta s^2.                               (3.4)
```

The cross-edge portion of either square function is exactly

```text
sum_p sum_(e!=f; e,f contain p)d_e(p)d_f(p)
 <=sum_p S_p^2
 <=16 Delta min(1,Delta/M)s^4.                       (3.5)
```

For one edge there is the sharper exact self identity

```text
||M_e^*M_e||HS^2
 =2(sum_(u in e)|z_u|^2)^2.                          (3.6)
```

Using (3.1), the self sum is at most

```text
24 Delta min(1,Delta/M)s^4.                          (3.7)
```

Therefore

```text
||R||HS^2, ||L||HS^2
 <=40 Delta min(1,Delta/M)s^4,                       (3.8)

E ||sum_I epsilon_I A_I||S4^4
 <=120 Delta min(1,Delta/M)s^4.                      (3.9)
```

The numerical constants are explicit and intentionally unoptimized.  The
power gain in (3.9) is the important point.  With `M=D^(15/8)` and
`Delta<=D`, its right side is `O(D^(1/8))s^4`.

## 4. Exact cross-Gram multiplicity theorem

Write

```text
H=sum_(I!=J) A_I^*A_J.                               (4.1)
```

If edges `e` and `f` meet at `p`, their contribution to (4.1) is the wedge
whose `(u,v)` entry is

```text
conj(M_e(p,u)) M_f(p,v),
u in e-{p}, v in f-{p}.                              (4.2)
```

Its squared Hilbert--Schmidt norm is `d_e(p)d_f(p)`.  Decompose every wedge
further into its scalar matrix-cell atoms, and let

```text
mu=max_(u,v) #{nonzero scalar wedge atoms landing at (u,v)}.             (4.3)
```

Entrywise Cauchy--Schwarz gives the exact packet-safe estimate

```text
||H||HS^2
 <=mu sum_(ordered wedges) d_e(p)d_f(p).              (4.4)
```

Without a factor-two hypothesis, the atomic energy is at most
`2Delta s^4`; with it, (3.5) improves this to
`16Delta min(1,Delta/M)s^4`.  Since

```text
(sum_I A_I)^*(sum_I A_I)=R+H,                        (4.5)
```

we obtain

```text
||sum_I A_I||S4^4
 <=2||R||HS^2+2||H||HS^2
 <=(80+32mu) Delta min(1,Delta/M)s^4.                (4.6)
```

In the unbinned case the original `14Delta` square estimate similarly gives

```text
||sum_I A_I||S4^4 <=(28+4mu)Delta s^4.               (4.7)
```

Thus at `M=D^(15/8)`, any `D^(1+o(1))s^4` excess over (4.6) requires

```text
mu>=D^(7/8-o(1)).                                    (4.8)
```

The inverse problem has become concrete: classify matrix cells carrying
nearly `D` compatible two-edge product walks.

## 5. The tangent packet saturates the multiplicity loss

Take

```text
a_i=m+i,  b_j=m+2L+j,  c_ij=m-2L-i-j,  q=2m,
1<=i,j<=L,  m>48L^3,  D=100L^2.                      (5.1)
```

Width-`q` classes are the exact levels of

```text
Q(i,2L+j)=i^2+i(2L+j)+(2L+j)^2,                      (5.2)
```

and direct monotonicity on rows, columns, and anti-diagonals proves that
every level is a vertex matching.  Put flat normalized coefficients on the
`2L-1` color nodes and zero on the row and column nodes.  Then

```text
all-plus fourth power =2L^4/(2L-1)^2,
Rademacher average    =2L^2/(2L-1).                  (5.3)
```

For the cross Gram, each off-diagonal row-row or column-column output cell
receives exactly `L` equal wedge atoms.  Hence

```text
mu=L,
atomic energy =2L^2(L-1)/(2L-1)^2,
||H||HS^2     =2L^3(L-1)/(2L-1)^2
              =mu * atomic energy.                  (5.4)
```

So (4.4) is exactly saturated, including its power of `mu`.  Residual
ordering, matching structure, and product conservation alone cannot improve
it.  The obstruction must be recognized and merged as a coherent
affine/Hankel packet.

## 6. Why a standard Carleson theorem does not remove the signs

The residual index is an order, but the matrices `A_I` are neither
martingale differences nor operators with disjoint Fourier supports.
Hilbert--Schmidt orthogonality controls only the second moment.  At fourth
order the common-pivot walks (4.2) couple different intervals.  Scalar
Carleson--Hunt and Rademacher--Menshov theorems do not bound a fixed all-plus
endpoint in this noncommutative geometry, and the ordered fixture (5.1)
exhibits the missing coherent endpoint explicitly.

The viable route is therefore an arithmetic inverse theorem:

```text
large mu
  => Carleson-packed rational tangent/Hankel packets
     + a remainder with mu=q^o(1).                   (6.1)
```

The merged-packet estimate handles the first term, while (4.6) handles the
second.  Proving (6.1) on the actual prime-power mask is the remaining new
step.

## 7. Binary status

```text
complex weighted Rademacher constant 42:                 VERIFIED;
actual all-distinct hypergraph linearity:                 VERIFIED;
actual short residual classes are matchings:              VERIFIED;
factor-two randomized gain D min(1,D/M):                  PROVED;
cross-Gram output-multiplicity criterion:                 PROVED;
tangent fixture saturates multiplicity Cauchy--Schwarz:    PROVED;
standard order/Carleson theorem removes all signs:         FALSE as stated;
large-multiplicity actual-prime inverse theorem:           OPEN;
sharp four-cycle theorem:                                  NOT PROVED.
```

Executable replay:

```text
src/qp_weighted_triangle_unconditionality_hostile.py
src/test_qp_weighted_triangle_unconditionality_hostile.py
```
