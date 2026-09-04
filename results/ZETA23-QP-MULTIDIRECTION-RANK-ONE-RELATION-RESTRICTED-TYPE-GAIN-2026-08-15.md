# QP four-cycle: aggregate short rank-one relations

**Date:** 2026-08-15  
**Verdict:** summing the fixed-relation `sqrt(D)` estimate direction by
direction is not sharp.  If each color matrix is assigned to at most
`q^o(1)` primitive rank-one relations and all assigned relations have height
at most `H`, then

```text
sum_e sum_(C assigned to e) |z_c11 z_c12 z_c21 z_c22|
  <<min(D,H sqrt(D))q^o(1)||z||_2^4.                (0.1)
```

The new part is the `H sqrt(D)` bound.  It combines triple uniqueness of a
small-determinant color matrix with unequal pointwise caps in the usual
fixed-rank-one hyperbola proof.  At the critical height `H=D^(1/4)`, (0.1)
is `D^(3/4)`, saving `D^(1/4)` over the determinant-layer mass `D`.

For the low-covolume parabolic branch, this improves the high/low chart
split from `D^(11/8)` to

```text
Q_low-P,parabolic(z)<<D^(5/4)q^o(1)||z||_2^4.      (0.2)
```

This does not improve the current global `D^(11/8)` theorem: its high-`P`
balanced branch has relation height above `sqrt(D)`, where (0.1) reverts to
the determinant-layer bound.

---

## 1. Assigned relation form

For a primitive rank-one matrix `e`, let `A_e` be any assigned subset of
the color matrices satisfying

```text
e dot (c11,-c12,-c21,c22)=0,
0<|c11*c22-c12*c21|<<D.                            (1.1)
```

Assume every color matrix occurs in at most `L=q^o(1)` of the sets `A_e`,
and that the assigned relations come from nonconstant active parabolic
charts.  This is the exact form needed below: the inverse theorem and
small-slope rigidity give only `q^o(1)` charts/directions per fixed color in
the high-multiplicity range.

All four components in the primitive factorization `e=r s^T` are nonzero
in this assigned sector.  This is not an implicit division assumption.  The
previous parabolic normal-form lemma proves it directly: if, for example,
`r1=0`, then `a1` is fixed, while two distinct values of either `b_j` change
`8*a1*b_j*c_1j` by order `q^2`, larger than the active width `O(qD)` because
`D=o(q)`.  Both columns, and then the second row, are fixed, contradicting a
nonconstant chart.  The other zero-component cases are symmetric.  In the
height range `H<=sqrt(D)` used for the gain, the equivalent determinant-gap
argument says that a zero tangent component forces the complementary factor
to have size `>>q/H>D`, outside `0<|det C|<<D`.  Thus zero-component relation
sectors contribute no high chart here; the already proved tangent/repeated
sectors cover their lower-multiplicity remnants.

Define the positive four-linear form

```text
T_H(f1,f2,f3,f4)
 =sum_(height(e)<=H) sum_(C in A_e)
    f1(c11)f2(c12)f3(c21)f4(c22).                  (1.2)
```

It is enough first to prove a restricted estimate for normalized
indicators `fi=1_Ai/sqrt(Ni)`.

---

## 2. Triple uniqueness

Fix any three entries of `C`.  The fourth belongs to an interval of length

```text
O(D/q)<1,                                          (2.1)
```

because all colors are comparable with `q` and `D=o(q)`.  Thus there is at
most one integral fourth entry.  Sort the four support sizes as

```text
N1<=N2<=N3<=N4.                                    (2.2)
```

Allowing the assignment multiplicity `L`, triple uniqueness gives

```text
T_H(f1,f2,f3,f4)
 <<L sqrt(N1*N2*N3/N4).                            (2.3)
```

Call the square root on the right `X`.

---

## 3. The fixed-relation estimate with unequal caps

Write `e=r s^T`, with all components nonzero as checked in Section 1.  The
proved fixed-relation parametrization gives two
integer gaps `h,l` with

```text
det C=h*l.                                         (3.1)
```

The four components of `r,s` may be taken nonzero.  Indeed, in the gain
range `height(e)<=H<=sqrt(D)`, a zero component makes the color relation
an equality between two distinct shell prime powers with coprime
coefficients of size at most `H`.  Clearing that equality forces the
complementary determinant factor to have size `>>q/H>D`, contradicting
`0<|det C|<<D`.  This is the zero-component case of the previously proved
nonzero-direction lemma for parabolic charts.

Its four matching energies `P_h,Q_h,R_l,S_l` obey

```text
sum P_h,sum Q_h,sum R_l,sum S_l<=1.                (3.2)
```

For normalized indicators on supports of sizes `Ni,Nj`, every matching has
at most `min(Ni,Nj)` edges.  Hence its energy is at most

```text
1/max(Ni,Nj).                                      (3.3)
```

The standard two Cauchy--Schwarz proof puts

```text
a_h=(P_h Q_h)^(1/4),       b_l=(R_l S_l)^(1/4),
||a||_2,||b||_2<=1.                                (3.4)
```

If `||a||_infinity<=A` and `||b||_infinity<=B`, a dyadic rectangle
`|h|~U,|l|~V`, `UV<<D`, contributes at most

```text
min(sqrt(U),U*A)*min(sqrt(V),V*B)
 <<min(sqrt(D),D*A*B).                             (3.5)
```

Across the two perfect matchings in (3.3), the product of the four maxima is
at least

```text
N2*N3*N4^2.                                        (3.6)
```

Therefore one fixed relation contributes at most

```text
D/((N2*N3)^(1/4)*N4^(1/2)) q^o(1).                (3.7)
```

There are `H^2 q^o(1)` primitive rank-one directions of height at most
`H`.  Unioning (3.7) gives

```text
Y=H^2*D/((N2*N3)^(1/4)*N4^(1/2)) q^o(1).          (3.8)
```

---

## 4. Interpolation of the two counts

We claim

```text
min(X,Y)<=H sqrt(D).                               (4.1)
```

If `X<=H sqrt(D)`, this is immediate.  Otherwise

```text
N1*N2*N3>H^2*D*N4.                                (4.2)
```

Since `N1<=N4`, equation (4.2) implies

```text
N2*N3>H^2*D.                                      (4.3)
```

Also `X<=N4`, so `N4>H sqrt(D)`.  Multiplying the square roots of these two
strict inequalities gives

```text
(N2*N3)^(1/4)*N4^(1/2)>H sqrt(D),                 (4.4)
```

and (3.8) gives `Y<H sqrt(D)`.  This proves the restricted estimate.

A positive restricted four-linear estimate at exponents `(2,2,2,2)`
extends to arbitrary vectors with their `ell^(2,1)` Lorentz norms.
The color universe has polynomial size in `q`, and

```text
||f||_(2,1)<<sqrt(log q)||f||_2.                  (4.5)
```

The four logarithmic losses are `q^o(1)`.  This proves the new branch of
(0.1); the `D` branch is the existing determinant-layer theorem.

---

## 5. Consequence for low-`P` parabolic charts

In the low-covolume branch the slice count is `K=O(1)`.  Split charts at
length `M`.  Low charts cost

```text
M*D*q^o(1).                                        (5.1)
```

A chart longer than `M` has primitive quadratic direction height

```text
h<<H:=D/M^2.                                       (5.2)
```

On a dyadic height block `h~J`, chart length is at most `sqrt(D/J)`.  By
(0.1), the assigned color mass of all directions in that block is at most
`J sqrt(D)q^o(1)`.  Thus all high charts cost

```text
sum_(J<=H) sqrt(D/J)*J*sqrt(D)
 <<D*sqrt(H)q^o(1)
 =D^(3/2)/M*q^o(1).                               (5.3)
```

Balancing (5.1) and (5.3) at `M=D^(1/4)` proves (0.2).

```text
aggregate rank-one relation mass H*sqrt(D):         PROVED;
low-P parabolic completed mass D^(5/4):              PROVED;
high-P balanced branch improvement:                  NOT OBTAINED;
global D^(11/8) exponent improvement:                 NO;
full four-cycle bound:                                OPEN.
```

The two finite inequalities are replayed in
`src/qp_four_cycle_multidirection_relation.py` and its test module.
