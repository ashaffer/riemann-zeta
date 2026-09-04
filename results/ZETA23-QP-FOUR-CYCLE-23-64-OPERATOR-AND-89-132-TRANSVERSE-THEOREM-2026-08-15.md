# QP four-cycle: `23/64` operator and `89/132` transverse theorem

**Date:** 2026-08-15  
**Verdict:** splitting directly by the product of the first two relation-
lattice minima removes the short-relation union loss.  For the truncated
actual prime-power carry matrix and every complex vector `z`,

```text
|Q_nd(z)|<<D^(23/16)q^o(1)||z||_2^4.              (0.1)
```

Consequently

```text
||A_z||_op<<D^(23/64)q^o(1)||z||_2.               (0.2)
```

The proved smooth band-pass and Schwartz-tail transfer then gives the
full-shell transverse exponent

```text
1/2+(23/64)*(16/33)=89/132.                        (0.3)
```

This strictly improves the preceding `D^(16/11)` fourth trace,
`D^(4/11)` operator, and `491/726` transverse exponent.  It still does not
prove the four-cycle target `D^(1+o(1))`, quarter-power operator, QP, or a
uniform strip.

The proof uses two already established geometric facts for a fixed color:

1. a universal nonparabolic slice gives `m(C)<<1+D/lambda2`;
2. if the short two-plane slice is parabolic, all parallel slices share one
   primitive rank-one direction, allowing the weighted height split.

No enumeration of all short invertible relation vectors is needed.

---

## 1. Setup and slice inputs

Normalize `||z||_2=1`.  For an all-distinct color matrix `C`, write

```text
Lambda_C={E in Z^4:w_C dot E=0},
lambda1<=lambda2<=lambda3,
P=lambda1 lambda2.                                  (1.1)
```

The lattice has determinant `asymp q`, so

```text
lambda1 lambda2 lambda3asympq.                     (1.2)
```

The determinant-layer color estimate is

```text
sum_C w_z(C)<<Dq^o(1).                             (1.3)
```

Choose a reduced basis `V1,V2,V3`.  Product matrices for one color obey a
ternary affine quadric equation in that basis.  The determinant form
restricted to `Lambda_C` is nondegenerate because its polar normal is
`adj(K)^T`, whose determinant is the nonzero color determinant.

The universal constant-shear slice theorem therefore gives

```text
m(C)<< (1+D/lambda2)q^o(1).                        (1.4)
```

Alternatively, slice first in the `V3` coordinate.  The number of parallel
slices is

```text
K_C:=1+D/lambda3
 <<1+D P/q.                                        (1.5)
```

Let

```text
Q_12(x,y)=det(xV1+yV2).                            (1.6)
```

If its discriminant is nonzero, every slice is a nonparabolic binary conic
and has `q^o(1)` actual points.  Hence

```text
m(C)<<K_Cq^o(1).                                   (1.7)
```

If its discriminant is zero but it is not identically zero, all slices have
one common primitive rank-one direction `e`, of height `h`.  Their total
multiplicity satisfies

```text
m_e(C)<<K_C(1+sqrt(D/h))q^o(1).                    (1.8)
```

The relation `e` kills the color matrix.  For every fixed primitive
rank-one relation,

```text
sum_(C:e kills C) w_z(C)<<sqrt(D)q^o(1),           (1.9)
```

and there are `H^2q^o(1)` such directions of height at most `H`.  If
`Q_12` vanishes identically, a fixed slice has at most one actual point and
(1.7) applies.

These slice statements do not require a lower bound on `lambda1`; this is
the observation that makes the new global split possible.

---

## 2. High two-minimum product

Set

```text
T=D^(9/8).                                         (2.1)
```

First suppose `P>=T`.  Since `lambda1<=lambda2`,

```text
lambda2>=sqrt(P)>=D^(9/16).                        (2.2)
```

The universal slice bound (1.4) gives

```text
m(C)<<D/lambda2*q^o(1)
     <<D^(7/16)q^o(1).                             (2.3)
```

Combining (2.3) with (1.3),

```text
Q_(P>=T)<<D^(23/16)q^o(1).                        (2.4)
```

---

## 3. Low two-minimum product: nondegenerate slices

Now suppose `P<T`.  At the project scale

```text
q=D^(33/16+o(1)).                                  (3.1)
```

Equations (1.5), (2.1), and (3.1) give the uniform slice cap

```text
K_C<<K_0:=1+DT/q
          <<D^(1/16+o(1)).                         (3.2)
```

If (1.6) has nonzero discriminant, use (1.7) and (1.3):

```text
Q_(P<T,nondeg)<<D K_0 q^o(1)
              <<D^(17/16+o(1)).                   (3.3)
```

This is much smaller than (0.1).

---

## 4. Low two-minimum product: common parabolic direction

It remains to sum the degenerate case of (1.8).  The additive `K_C` term in
(1.8), summed using (1.3), costs only `DK_0`, already covered by (3.3).
Retain `K_0 sqrt(D/h)`.

Split the **total multi-slice multiplicity** assigned to a color's common
direction at a threshold `M`.  The low-multiplicity part contributes

```text
Q_low<<M Dq^o(1).                                  (4.1)
```

If the square-root part of (1.8) exceeds `M`, then

```text
h<<H:=D K_0^2/M^2.                                 (4.2)
```

For a dyadic height block, combine (1.8), the fixed-direction color mass
(1.9), and the `H^2` direction count.  This gives

```text
Q_high
 <<K_0 D H^(3/2)q^o(1)
 =D^(5/2)K_0^4 M^(-3)q^o(1).                     (4.3)
```

Balance (4.1) and (4.3):

```text
M=D^(3/8)K_0,
Q_(P<T,deg)<<D^(11/8)K_0q^o(1).                  (4.4)
```

At this optimizer,

```text
H=D^(1/4),                                         (4.5)
```

so every invocation of (1.9) lies safely below the prime-power shell scale.
Using (3.2) in (4.4),

```text
Q_(P<T,deg)<<D^(11/8+1/16+o(1))
            =D^(23/16+o(1)).                      (4.6)
```

Equations (2.4), (3.3), and (4.6), together with the already closed
repeated-node/permutation sectors, prove (0.1).

---

## 5. Why `T=D^(9/8)` is the balanced cutoff

Write `T=D^tau`.  The high-product contribution from (1.4) has exponent

```text
2-tau/2.                                          (5.1)
```

For `tau>=17/16`, the low-product slice count has exponent
`tau-17/16`, so the degenerate height sum has exponent

```text
11/8+tau-17/16=5/16+tau.                          (5.2)
```

Balancing (5.1)--(5.2) gives

```text
2-tau/2=5/16+tau,
tau=9/8,
common exponent=23/16.                            (5.3)
```

Thus the cutoff in (2.1) is the optimizer of the proved two estimates, not
an arbitrary choice.

---

## 6. Operator and transverse consequences

The exact fourth trace obeys

```text
||A_z||_op^4
 <=tr((A_z^*A_z)^2)
 <=2D+|Q_nd(z)|.                                   (6.1)
```

Taking fourth roots of (0.1) proves (0.2).  The existing smooth
Schwartz-tail transfer uses

```text
transverse exponent=1/2+theta*(16/33).             (6.2)
```

With `theta=23/64`,

```text
1/2+(23/64)*(16/33)
 =1/2+23/132
 =89/132.                                          (6.3)
```

The improvements are strict:

```text
23/64<4/11,                    89/132<491/726.     (6.4)
```

```text
universal fixed-color slice bound:                 PROVED;
low-P nondegenerate mass D^(17/16+o):              PROVED;
low-P common-direction mass D^(23/16+o):           PROVED;
high-P mass D^(23/16+o):                           PROVED;
absolute fourth trace D^(23/16+o):                 PROVED;
carry operator D^(23/64+o):                        PROVED;
transverse exponent 89/132 via smooth transfer:    PROVED;
full four-cycle D^(1+o):                           OPEN;
quarter-power operator / 41/66:                    OPEN;
QP or a uniform strip:                             NOT CLAIMED.
```
