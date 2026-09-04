# QP four-cycle: middle-slice conic dichotomy

**Date:** 2026-08-15  
**Verdict:** the rank-three slice range that appears beyond the old critical
relation cutoff can be controlled.  Let

```text
R_crit=q/D^2=D^(1/16+o(1)),
R_crit<R,
lambda1>=R,
lambda1*lambda2<RD.                               (0.1)
```

For the colors in (0.1), slicing the fixed-color ternary rank-one quadric
along its third reduced lattice coordinate gives:

```text
nondegenerate binary restriction:
    Q_middle,ndeg<<D(1+R/R_crit)q^o(1);            (0.2)

degenerate binary restriction:
    Q_middle,deg<<D^(11/8)(1+R/R_crit)q^o(1).      (0.3)
```

At `R=D^(1/11)`, these are respectively

```text
D^(181/176+o(1)),             D^(247/176+o(1)).   (0.4)
```

Both are smaller than `D^(16/11)`.

This report proves the **middle slice range**.  The raw broad-range lattice
count by itself still contains

```text
D^3/q=D/R_crit,                                    (0.5)
```

which is larger than `D/R` once `R>R_crit`.  The subsequent universal direct
quadric-slice theorem removes that term and combines this middle result into
the global `D^(16/11)` fourth-trace and `D^(4/11)` operator theorem; see
`ZETA23-QP-FOUR-CYCLE-FOUR-ELEVENTHS-OPERATOR-AND-491-726-TRANSVERSE-THEOREM-2026-08-15.md`.

---

## 1. Ternary quadric coordinates

Fix a color matrix `C` and one completion product matrix `P0`.  Let

```text
Lambda_C={E in Z^4:w_C dot E=0}
```

and choose a reduced integral basis `V1,V2,V3` with

```text
||Vi||asymp lambda_i,             lambda1<=lambda2<=lambda3. (1.1)
```

Every other completion has

```text
P(x,y,t)=P0+xV1+yV2+tV3,
det P(x,y,t)=0.                                   (1.2)
```

The product box of side `O(D)` gives

```text
|x|<<D/lambda1,   |y|<<D/lambda2,
|t|<<D/lambda3.                                  (1.3)
```

Minkowski's second theorem and (0.1) imply

```text
lambda3>>q/(lambda1 lambda2)>q/(RD),
K:=1+D/lambda3
 <<1+RD^2/q
 =1+R/R_crit.                                     (1.4)
```

Thus only `Kq^o(1)` parallel `t` slices can occur.

The quadratic part in `(x,y)` is independent of `t`:

```text
Q(x,y)=det(xV1+yV2)
      =a x^2+bxy+c y^2.                            (1.5)
```

---

## 2. Nondegenerate restriction

Suppose

```text
b^2-4ac!=0.                                       (2.1)
```

For each fixed `t`, the equation in `(x,y)` is a nonparabolic binary conic.
For an affine equation

```text
a x^2+bxy+c y^2+d x+e y+f=0,
Delta=b^2-4ac!=0,
```

assume first that `c!=0` and put

```text
Y=2cy+bx+e,       p=be-2cd,       q0=e^2-4cf,
X=Delta*x+p.
```

Direct completion of squares gives

```text
X^2-Delta*Y^2=p^2-Delta*q0.                       (2.2)
```

The change only imposes congruence restrictions.  A nonzero right side in
(2.2) has `q^o(1)` solutions by the divisor/ideal count and the logarithmic
number of units of polynomial height.  If the right side is zero and
`Delta` is nonsquare, only `X=Y=0` is integral; if `Delta` is square, the
equation is a union of rational lines.  The case `c=0` is the same after
swapping variables or direct factorization.  Thus every irreducible slice
has `q^o(1)` integral points uniformly.  A singular/reducible slice is a union of at
most two lines; every such line contains at most one actual completion,
because the difference of two points on a component has rank one, which is
excluded for a nonzero all-distinct same-color completion difference.

It follows from (1.4) that

```text
m(C)<<Kq^o(1).                                     (2.3)
```

Multiplying by the determinant-layer color mass
`sum_C w_z(C)<<Dq^o(1)` proves (0.2).

---

## 3. Degenerate restriction and its common direction

Suppose `Q` is nonzero and

```text
b^2-4ac=0.                                        (3.1)
```

An integral binary quadratic of rank one has the exact form

```text
Q(x,y)=g(alpha*x+beta*y)^2,                        (3.2)
```

where `g` is a nonzero integer and `(alpha,beta)` is primitive.  Indeed the
linear factor is rational by (3.1); after making it primitive integral, the
integrality of all three coefficients forces its scalar to be integral.

The repeated direction at infinity is therefore the primitive matrix
direction of

```text
e0=beta V1-alpha V2.                               (3.3)
```

After dividing its entry gcd, call the resulting primitive rank-one matrix
`e` and put `h=||e||_infinity`.  Since

```text
|alpha|sqrt(|g|)<<lambda1,
|beta|sqrt(|g|)<<lambda2,                          (3.4)
```

one has

```text
lambda1<<h<<lambda1 lambda2.                       (3.5)
```

The lower bound uses `e in Lambda_C` and the definition of `lambda1`; the
upper bound follows directly from (3.3)--(3.4).  Every parallel slice in
(1.2) has the same repeated direction `e`.

If `Q` vanishes identically, every vector in `span(V1,V2)` is rank one.
Then a fixed `t` slice contains at most one actual completion, so (2.3)
already applies.  Hence only the rank-one case (3.2) remains.

---

## 4. Multi-slice parabolic height split

On a fixed `t` slice, use a unimodular change
`u=alpha*x+beta*y`, with complementary coordinate `v`.  Its equation is

```text
B_t*v=-g*u^2-A_t*u-C_t.                            (4.1)
```

If `B_t=0`, there are at most two line components, already closed above.
Otherwise split the quadratic congruence in `u mod B_t` by
`gcd(u,B_t)`.  There are only `q^o(1)` divisor classes; after the gcd is
fixed, the primitive quadratic congruence has `q^o(1)` roots.  This also
handles the apparent `p^(j/2)` family of roots of `u^2=0 mod p^j`: their
common `p`-power is part of the fixed gcd class, rather than a polynomial
number of separate charts.

On each resulting arithmetic progression, reparametrize by `n`.  The matrix
polynomial `M_t(n)` is integer-valued, so

```text
2M_(t,2)=Delta_n^2 M_t(n) in Mat_2(Z).             (4.2)
```

Its quadratic coefficient is parallel to the repeated direction `e`, which
is independent of `t`.  Primitivity therefore gives
`2M_(t,2)=g_t e` for a nonzero integer `g_t`, and some entry has leading
coefficient at least `h/2`.  The product box gives

```text
# points on one slice<<1+sqrt(D/h).                 (4.3)
```

All coefficients and resultants in (4.1) have polynomial size uniformly in
the slice index, so the congruence cover costs only `q^o(1)` per slice.

Summing (4.3) over (1.4), the total multiplicity assigned to this common
direction obeys

```text
m_e(C)<<K(1+sqrt(D/h))q^o(1).                      (4.4)
```

The harmless `K` term is already bounded by (0.2); retain the square-root
term below.

Split the total `m_e(C)`, not the individual slices, at a threshold `M`.
The low part contributes

```text
Q_low<<MDq^o(1).                                   (4.5)
```

If the square-root part of (4.4) exceeds `M`, then

```text
h<<H:=D K^2/M^2.                                   (4.6)
```

There are `X^2q^o(1)` primitive rank-one directions of height at most `X`.
For each fixed direction the rank-one short-relation theorem gives color
mass at most `sqrt(D)q^o(1)`.  Dyadically summing (4.4) over directions of
height at most `H` yields

```text
 Q_high
 <<K D H^(3/2)q^o(1)
 =D^(5/2)K^4 M^(-3)q^o(1).                        (4.7)
```

Balance (4.5) and (4.7):

```text
M=D^(3/8)K,
Q_middle,deg<<D^(11/8)Kq^o(1).                    (4.8)
```

At this optimizer, `H=D^(1/4)`, independently of `K`, so every fixed-
relation invocation is safely below the prime-power shell scale.  Equations
(1.4) and (4.8) prove (0.3).

For `R=D^(1/11)` and `R_crit=D^(1/16)`,

```text
R/R_crit=D^(1/11-1/16)=D^(5/176),                 (4.9)
```

which gives (0.4).

---

## 5. Why raw lattice counting was insufficient, and its resolution

When `lambda1*lambda2>=RD`, the successive-minima expansion gives

```text
#(Lambda_C intersect O(D)-box)
 <<D/R+D^3/q
 =D/R+D/R_crit.                                    (5.1)
```

At the old cutoff `R=R_crit`, the two terms coincide.  For every larger
cutoff the cubic term dominates.  Balanced admissible minima

```text
lambda1asymplambda2asymplambda3asympq^(1/3)
```

lie in the broad range at `R=D^(1/11)` and have exactly the exponent in the
cubic lattice-volume term.  The fixed-`(C,E)` theorem converts (5.1) only to
the old pointwise plateau `m(C)<<sqrt(D/R_crit)q^o(1)`.

The universal direct quadric-slice theorem supplies the missing replacement
without counting secant vectors.  The determinant form restricted to
`Lambda_C` is a nondegenerate ternary quadratic form.  A constant shear
chooses a nonparabolic binary section while leaving only
`O(1+D/lambda2)` parallel slices.  Hence, in the broad range,

```text
m(C)<<1+D/lambda2<<sqrt(D/R)q^o(1),                (5.2)
```

which removes (5.1)'s cubic term and completes the global theorem cited in
the verdict.

```text
middle nondegenerate slice bound (0.2):             PROVED;
middle common-direction degenerate bound (0.3):     PROVED;
middle range at R=D^(1/11) below D^(16/11):         PROVED;
broad cubic term removed by subsequent slice bound: PROVED;
global fourth trace D^(16/11):                      PROVED;
global operator D^(4/11), transverse 491/726:       PROVED;
full four-cycle bound:                               OPEN.
```
