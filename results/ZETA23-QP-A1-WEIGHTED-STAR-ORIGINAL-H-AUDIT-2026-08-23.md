# QP final parabolic face: original-`H` weighted-star audit

**Date:** 2026-08-23  
**Verdict:** the inverse-square-root fixed-determinant star has bounded
operator norm, but it does not act directly on the original color-pair
coefficients.  The missing `sqrt(K)` is already present in the exact
row-pair/color-pair incidence `H`, before completion multiplicities are
grouped by color and before gap tokens are refined.  An `A=1` packet is a
two-column common-neighbour block.  Pulling either fixed column coefficient
to its `K` line directions has norm `sqrt(K)`, and common-column diagonal
subtraction leaves the resulting off-diagonal codegree unchanged.

Thus the proposed weighted Schur insertion is **conditional** on a new
actual-mask high-tail theorem.  It is not obtained by reorienting the
existing `H` identity, pair uniqueness, or the current gap-token bounds.

## 1. The exact expression before colorwise grouping

Let `p=(a1,a2)` be an ordered row pair and let
`rho=(c1,c2)` be an ordered color pair.  If one carrier `b` supports both
triples, put

```text
h(p,rho)=conj(kappa(a1,b,c1))*kappa(a2,b,c2).
```

Pair uniqueness makes `b=b(p,rho)` unique.  With

```text
xi_(c1,c2)=conj(z_c1)*z_c2,
```

the original incidence identity is

```text
G_p=(H xi)_p=sum_rho h(p,rho) xi_rho.                (1.1)
```

The common-column diagonal is exactly the sum of the squared individual
summands in (1.1).  Therefore

```text
Q_nd
 =sum_p sum_(rho!=sigma)
    h(p,rho) conj(h(p,sigma))
    xi_rho conj(xi_sigma).                           (1.2)
```

For

```text
rho=(x,zeta),       sigma=(y,w),
```

one summand of (1.2) is the original four-edge rectangle

```text
conj(kappa(a1,b1,x))*kappa(a2,b1,zeta)
*kappa(a1,b2,y)*conj(kappa(a2,b2,w))
*conj(z_x)*z_zeta*z_y*conj(z_w).                    (1.3)
```

No color-completion multiplicity has been introduced in (1.2)--(1.3).

## 2. What an `A=1` line is inside `H`

For a parabolic color rectangle use integral carrier coordinates

```text
U^T K V=(0,theta;eta,gamma0),
a=U(u,alpha),       b=V(v,beta).
```

At the final face the extremal line data can be written

```text
alpha=theta*c,      beta=eta*c*B,
A=1,                B~K,
B*(u+gamma0*c)+v=C0.                                (2.1)
```

One maximal line is consequently

```text
u=u0+t,             v=v0-B*t.                       (2.2)
```

Along (2.2), the row-pair vertex `p(t)=U(u0+t,alpha)` changes, but the two
right vertices

```text
rho=(x,zeta),       sigma=(y,w)                     (2.3)
```

do not.  If the occupied interval has length `ell_B`, then (2.2) supplies
`ell_B` distinct rows of `H` on which the same two columns coexist.
Pair uniqueness says that different `B`-lines cannot use the same row with
the same two fixed columns: each of the two row-pair/color-pair incidences
already fixes its carrier.  It makes the row sets disjoint; it does not
reduce their union.

The curvature bound is

```text
ell_B <<sqrt(D/(B*H)).                               (2.4)
```

Hence `K` saturated directions produce

```text
N=sum_(B~K) ell_B
  ~sqrt(D/H) sum_(B~K) B^(-1/2)
  ~sqrt(D/H)*sqrt(K).                               (2.5)
```

## 3. The copy norm in the weighted determinant operator

On one fixed-level star define

```text
T e_B=B^(-1/2)e_0,             B~K.                 (3.1)
```

Then

```text
||T||=(sum_(B~K) 1/B)^(1/2)<<1.                     (3.2)
```

But the base endpoint `sigma` is the same for every `B`.  Its actual lift is

```text
J e_sigma=sum_(B~K)e_B,       ||J e_sigma||=sqrt(K). (3.3)
```

Compressing (3.1) back to the two base color-pair endpoints gives exactly

```text
<e_0,T J e_sigma>=sum_(B~K)B^(-1/2)~sqrt(K).        (3.4)
```

Transposing the orientation only moves `J` to the other endpoint.  The
large multiplier belongs to the column-carrier progression in one
orientation and to the row of the transposed incidence in the other, while
the same two color-pair endpoints remain fixed.  Thus no top--bottom versus
left--right choice removes (3.3).

Varying `C0` in (2.1) is harmless for (3.2): one may take the direct sum of
the fixed-level operators.  It is also irrelevant to the obstruction,
because (3.3) occurs inside each fixed `C0` block.

## 4. Exact two-column Gram packet

The support packet behind (2.5) is the `N`-by-two all-one matrix

```text
H_packet=(1 1)
         (1 1)
          ...                                      (4.1)
```

with `N=sum_B ell_B` rows.  Therefore

```text
H_packet^* H_packet=N*(1 1;1 1).                   (4.2)
```

The common-column diagonal removes `N` times the identity and leaves

```text
N*(0 1;1 0),                                       (4.3)
```

whose norm is `N`.  For the equal unit pair
`xi=(1,1)/sqrt(2)`, the diagonal-subtracted quadratic form equals `N`.
The factorization constraint `xi=conj(z) tensor z` does not kill it: choose
four distinct colors and put `z=1/2` on them.  Then the two pair
coefficients are both `1/4`, and (1.2) contributes `N/8>0`.

This packet is compatible with pair uniqueness.  Give every row in (4.1)
its unique two carriers and use the four triples displayed in (1.3);
different rows use different row-pair/carrier incidences.  It can also be
placed on the integral pencil (2.1) by taking disjoint `u` intervals for
different `B`.  This is an exact incidence/integer-chart obstruction, not
an actual-prime QP construction: simultaneous prime powers and all four
product windows are the unresolved mask.

## 5. Final exponent ledger

At

```text
(e,t,r,s,g)=(21/32,11/32,23/64,3/64,0)
```

the relevant powers of `D` are

```text
relation mass                              45/64,
H=R*S                                      26/64,
# B-lines = K                              20/64,
one line length sqrt(D/(B*H))               9/64,
all common neighbours K*ell_B              29/64.
```

Equivalently,

```text
sqrt(D/H)                                  19/64,
sum_(B~K) B^(-1/2)                         10/64.
```

The original `H` packet therefore reproduces

```text
45/64+29/64=74/64=37/32.                   (5.1)
```

The conditional weighted-Schur proof would replace the last `10/64` by
zero and give

```text
45/64+19/64=1.                             (5.2)
```

Equation (3.3) is exactly the missing `10/64`.

## 6. Binary status

```text
original-H formula before color grouping:             EXACT;
A=1 lines keep the same two H columns:                EXACT;
weighted fixed-level star norm O(1):                  PROVED;
endpoint lift norm sqrt(K):                           PROVED, SHARP;
common-column diagonal removes the star:              FALSE;
row/column or top/bottom reorientation removes copy:  FALSE;
pair uniqueness makes the lift contractive:           FALSE;
actual-prime mask forces subpower B multiplicity:      OPEN;
sharp final-face bound from present ingredients:       NOT PROVED.
```

Finite replay:

```bash
PYTHONPATH=src pytest -q src/test_qp_a1_weighted_star_h_audit.py
```
