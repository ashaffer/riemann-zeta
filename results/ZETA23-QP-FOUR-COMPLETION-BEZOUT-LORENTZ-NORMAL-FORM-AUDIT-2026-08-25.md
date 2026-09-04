# QP four completion: Bezout--Lorentz normal form and its exact limit

**Date:** 2026-08-25  
**Verdict:** the unimodular Bezout-token normal form is exact and useful, but
its Gram identities do **not** force the desired `O(D q^o(1))` occupied-cell
bound.  They factor into the original coordinate products.  The two hard
diamonds retain exactly the selected two-inverse condition and supply no
third independent constraint.  Thus the sharp four-cycle bound remains open.

## 1. Exact unimodular chart

Fix a primitive anchor `gamma=(c,C)` and choose integers `u,v` with

```text
c*u-C*v=1.                                               (1.1)
```

For a centre `p=(b,B)` and partner `eta=(d,E)`, put

```text
delta=c*b-C*B,                 h=C*d-c*E.
```

There are unique integers `n,m` such that

```text
b=u*delta-C*n,                 B=v*delta-c*n,
d=-v*h+c*m,                    E=-u*h+C*m.              (1.2)
```

Both changes of variables have determinant `+-1`.  Write

```text
P=(delta,n),       Q=(h,m),       Q0=(0,1),
K=(-2uv, cu+Cv; cu+Cv, -2cC).                           (1.3)
```

Then exactly

```text
det K=-1,
det(P,Q)=delta*m-n*h=b*d-B*E,
P^T K Q=b*d+B*E,
P^T K Q0=b*c+B*C.                                      (1.4)
```

The two windows on an edge with row `y`, product sum `S`, and product
difference `T` are equivalent to one hard diamond:

```text
max(|4y(S+T)-q^3|,|4y(S-T)-q^3|)
 =|4yS-q^3|+4y|T| <=qD.                                (1.5)
```

Consequently the anchored and middle edges are represented without loss by

```text
|4a(P^T K Q0)-q^3|+4a|det(P,Q0)| <=qD,
|4x(P^T K Q )-q^3|+4x|det(P,Q )| <=qD.                 (1.6)
```

## 2. The complete Gram multiplication law

Put

```text
S0=b*c+B*C,       L=C*d+c*E,
S =b*d+B*E,       kappa=b*d-B*E.
```

The determinant-minus-one Gram identity gives the two exact equations

```text
2cC*S     =S0*L+delta*h,
2cC*kappa=S0*h+delta*L.                                (2.1)
```

Equivalently,

```text
(S0+delta)(L+h)=2cC(S+kappa),
(S0-delta)(L-h)=2cC(S-kappa).                          (2.2)
```

This is a clean Lorentz multiplication law.  It is also the precise reason
the Gram step creates no new counting condition: `(2.2)` factors as

```text
(2bc)(2Cd)=2cC(2bd),
(2BC)(2cE)=2cC(2BE).                                  (2.3)
```

Thus the putative new congruences modulo `2cC` are identities inherited from
the already known factors.  In particular,

```text
S0*L == -delta*h          (mod 2cC)                    (2.4)
```

does not imply `delta*h=0`, even though `|delta*h|<<D^2<q`.

## 3. Literal actual-prime no-go to small-remainder vanishing

Use the certified seven-prime fixture with

```text
m=2,934,091,       q=5,868,182,       D=1,912,
gamma=(m+18,m+12),
p    =(m,m+6),
eta  =(m+12,m+6),
a=m-18,             x=m-12.                            (3.1)
```

Both hard diamonds in `(1.6)` hold, every displayed coordinate is prime,
and `D^2<q`.  Nevertheless

```text
delta=-72,        h=36,        kappa=-36,
delta*h=-2592 !=0.                                      (3.2)
```

Hence neither actual primality, the two hard diamonds, nor the inequality
`D^2<q` turns the mixed Gram remainder into zero.

## 4. Why Bezout or resultant elimination stops here

For fixed `(c,C,u,v)`, the maps in `(1.2)` are unimodular bijections

```text
Z^2_(delta,n) <-> Z^2_(b,B),
Z^2_(h,m)     <-> Z^2_(d,E).                           (4.1)
```

Therefore `(delta,n,h,m)` are algebraically free before the inequalities and
actual-node masks are imposed.  All identities in Section 2 hold identically
on this four-dimensional affine space.  In particular their elimination
ideal in `Z[delta,h]` is zero: Gram/Bezout algebra cannot place the occupied
`(delta,h)` cells on a fixed curve or on finitely many curves.

The missing information is analytic/arithmetic rather than algebraic.  The
first diamond selects the physical `P` tokens.  For every selected `P`, the
second diamond asks whether the reciprocal value

```text
q^3/(4 P^T K Q)                                         (4.2)
```

lands within `O(D/q)` of an **actual prime-power row** simultaneously with
the two factorizations in `(2.3)`.  There is no hard diamond on `(L,h)`.
Adding one would be an extra edge absent from an NDS chain.  The required
theorem is still the mask-sensitive, fixed-anchor two-inverse estimate

```text
#{(P,Q): first diamond for some actual a,
          second diamond for some actual x}
   <<D q^o(1).                                           (4.3)
```

The map from a chain to `(delta,h)` is injective, so `(4.3)` is exactly the
occupied-cell/NDS theorem, not a consequence already contained in the
normal form.

## 5. Verification and binary status

```text
src/qp_four_completion_bezout_normal_form.py
src/test_qp_four_completion_bezout_normal_form.py
lean/weilcert/QPFourCompletionBezoutNormalForm.lean
```

Python replays the all-prime chain, both hard diamonds, and all factorisations.
Lean certifies the reconstruction, middle determinant, `det K=-1`, both
Lorentz identities, both factorisations, and the nonzero fixture remainder.

```text
unimodular Bezout reconstruction:                    PROVED;
middle determinant delta*m-n*h:                      PROVED;
symmetric Gram matrix has determinant -1:            PROVED;
hard-window pair equals one hard diamond:             PROVED;
Lorentz multiplication and factorisations:            PROVED;
D^2<q forces delta*h=0:                               FALSE;
Gram identities add a third physical diamond:         FALSE;
Bezout/resultant algebra alone compresses D^2 cells:  FALSE AS A METHOD;
mask-sensitive two-inverse occupied-cell theorem:      OPEN;
sharp four-cycle bound:                                NOT PROVED.
```

## 6. Affine-chart follow-up

The subsequent Hessian audit proves that every fixed transverse affine token
chart (`det(V,W)!=0`) has `O(D log D)` cells from the determinant strip alone.
For parallel directions, the radial Hessian is nondegenerate unless the
common token direction is `K`-null, in which case it is exactly a coordinate
tangent ruling.  The non-null parallel chart is `O(D)` once its physical row
is locked to the stationary affine law.  Automatic actual-prime row locking
and global Carleson summation across up to `O(D^2)` directions remain open.

See
`ZETA23-QP-AFFINE-TOKEN-TRANSVERSE-STRIP-AND-PARALLEL-HESSIAN-AUDIT-2026-08-25.md`.
