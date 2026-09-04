# QP four-cycle: `4/11` operator and `491/726` transverse theorem

**Date:** 2026-08-15  
**Verdict:** the short-relation decomposition can be pushed past the old
critical cutoff by slicing the fixed-color rank-one quadric directly.  For
the truncated actual prime-power carry matrix and every complex vector `z`,
the all-distinct completed four-cycle mass satisfies

```text
|Q_nd(z)|<<D^(16/11)q^o(1)||z||_2^4.              (0.1)
```

Consequently

```text
||A_z||_op<<D^(4/11)q^o(1)||z||_2.                (0.2)
```

Through the already proved smooth band-pass and Schwartz-tail transfer, the
full-shell transverse exponent becomes

```text
1/2+(4/11)*(16/33)=491/726.                        (0.3)
```

This improves the preceding `D^(47/128)` operator theorem.  It remains
strictly weaker than the four-cycle target `D^(1+o(1))`, quarter-power
operator, and transverse exponent `41/66`; none of those is asserted.

The new broad lemma is a universal conic slice bound

```text
m(C)<<1+D/lambda2(C)                               (0.4)
```

for every fixed all-distinct color.  It removes the cubic
`D^3/q` lattice-volume term.  The only range not handled by (0.4) at the
optimized cutoff is a thin middle branch; the common-direction parabolic
height theorem controls that branch at a smaller exponent.

---

## 1. Inherited inputs

Normalize `||z||_2=1`.  For an all-distinct oriented color matrix `C`, put

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|,
Lambda_C={E in Z^4:w_C dot E=0},
lambda1<=lambda2<=lambda3.                         (1.1)
```

The earlier reports prove:

1. `det Lambda_C asymp q` and
   `lambda1 lambda2 lambda3 asymp q`.
2. Every product difference lies in an `O(D)` box in `Lambda_C`.
3. Every fixed nonzero `(C,E)` has only `q^o(1)` ordered realizations.
4. Uniformly, `m(C)<<sqrt(D)q^o(1)`.
5. The determinant-layer color mass is

   ```text
   sum_C w_z(C)<<Dq^o(1).                           (1.2)
   ```

6. For a fixed relation `e` of height at most `R`,

   ```text
   sum_(C:e kills C) w_z(C)<<R sqrt(D)q^o(1).       (1.3)
   ```

7. In the middle slice range

   ```text
   lambda1>=R,              lambda1 lambda2<RD,     (1.4)
   ```

   the nondegenerate and degenerate binary restrictions contribute

   ```text
   Q_mid,ndeg<<D(1+R/Rcrit)q^o(1),
   Q_mid,deg <<D^(11/8)(1+R/Rcrit)q^o(1),           (1.5)

   Rcrit=q/D^2=D^(1/16+o(1)).                       (1.6)
   ```

Repeated-node and permutation sectors have `O(Dq^o(1))` mass.

---

## 2. Nondegeneracy of the ternary determinant form

Fix a color and one completion product matrix `P0`.  Every other product
matrix is

```text
P=P0+E,                      E in Lambda_C,          (2.1)
```

and satisfies `det P=0`.  Let

```text
q_2(E)=det E,
B(E,F)=q_2(E+F)-q_2(E)-q_2(F).                     (2.2)
```

The determinant form is nondegenerate on the four-dimensional matrix
space.  Its restriction to the three-dimensional hyperplane `Lambda_C`
is also nondegenerate.  Here is the exact check.

Write the signed color matrix as

```text
K=(c11,-c12;-c21,c22),          det K=det C=k!=0.  (2.3)
```

There is a matrix `N=adj(K)^T` such that

```text
B(N,E)=w_C dot E.                                    (2.4)
```

Thus `Lambda_C` is the `B`-orthogonal hyperplane to `N`.  A restriction of
a nondegenerate bilinear form to `N^perp` is degenerate exactly when
`B(N,N)=0`.  But

```text
B(N,N)=2 det N=2 det K=2k!=0.                      (2.5)
```

Therefore `q_2|Lambda_C` is a nondegenerate ternary quadratic form.

---

## 3. A universal direct quadric-slice bound

Choose a reduced integral basis `v1,v2,v3` of `Lambda_C`, with
`||vi||asymp lambda_i`.  In these coordinates the completion equation is

```text
F(n1,n2,n3)=det(P0+n1v1+n2v2+n3v3)=0.             (3.1)
```

Reduced-basis coordinate control gives

```text
|ni|<<1+D/lambda_i.                                (3.2)
```

For an integer `t`, put

```text
u_t=v2+t v3,
delta(t)=B(v1,u_t)^2-4q_2(v1)q_2(u_t).             (3.3)
```

The polynomial `delta(t)` has degree at most two and is not identically
zero.  If `q_2(v1)!=0` and it vanished identically, then on
`span(v2,v3)` one would have

```text
q_2(u)=B(v1,u)^2/(4q_2(v1)),                       (3.4)
```

so the Schur complement of the `v1` entry would vanish and the ternary form
would be degenerate.  If `q_2(v1)=0`, identical vanishing would give
`B(v1,v2)=B(v1,v3)=0`; together with `B(v1,v1)=0`, this would make `v1` a
radical vector.  Both contradict Section 2.

Hence at least one

```text
t in {0,1,2}                                      (3.5)
```

has `delta(t)!=0`.  Use the unimodular basis

```text
(v1,u_t,v3).                                       (3.6)

```

If the old coordinates are `(n1,n2,n3)`, the new third coordinate is

```text
s=n3-t n2.                                         (3.7)
```

Equations (3.2) and `lambda2<=lambda3` show that `s` takes at most

```text
O(1+D/lambda2)                                    (3.8)
```

integer values.  For each fixed `s`, equation (3.1) is a binary affine
conic whose quadratic part on `span(v1,u_t)` has nonzero discriminant.

An irreducible slice completes squares to a nonzero binary norm equation
and has `q^o(1)` integral points in its polynomial-size box.  A singular or
reducible slice is a union of at most two rational lines.  Each line has at
most one actual completion: the difference of two points on a component
has determinant zero, whereas every nonzero same-color actual completion
difference has nonzero determinant.

This proves the promised universal bound

```text
m(C)<< (1+D/lambda2)q^o(1).                        (3.9)
```

It is important that (3.7), rather than the length of `u_t`, controls the
number of slices.  Although `u_t` may have size comparable with `lambda3`,
the constant shear in (3.6) makes the slice index range only on the
`lambda2` scale.

---

## 4. Relation cutoff and the short branch

Choose

```text
R=D^(1/11).                                        (4.1)
```

If `lambda1(C)<R`, choose a nonzero primitive relation
`e in Lambda_C` of height at most `R`.  There are `O(R^4)` possible
relation vectors.  Equation (1.3) and a union bound give

```text
sum_(lambda1<R) w_z(C)
 <<R^5 sqrt(D)q^o(1).                              (4.2)
```

Multiplying by the uniform completion bound `sqrt(D)` gives

```text
Q_short<<D R^5q^o(1)=D^(16/11)q^o(1).             (4.3)
```

---

## 5. Long broad branch

Suppose

```text
lambda1>=R,                 lambda1 lambda2>=RD.   (5.1)
```

Since `lambda1<=lambda2`,

```text
lambda2>=sqrt(RD).                                  (5.2)
```

The direct slice bound (3.9) therefore gives

```text
m(C)<<sqrt(D/R)q^o(1).                             (5.3)
```

Together with (1.2),

```text
Q_broad
 <<D sqrt(D/R)q^o(1)
 =D^(3/2)R^(-1/2)q^o(1)
 =D^(16/11)q^o(1).                                (5.4)
```

This is the step that legitimately removes the formerly dominant cubic
lattice-volume term `D^3/q`.

---

## 6. Long middle branch

It remains to consider

```text
lambda1>=R,                 lambda1 lambda2<RD.    (6.1)
```

Apply (1.5).  From (1.6) and (4.1),

```text
R/Rcrit
 =D^(1/11-1/16+o(1))
 =D^(5/176+o(1)).                                  (6.2)
```

Thus

```text
Q_mid,ndeg<<D^(181/176+o(1)),
Q_mid,deg <<D^(247/176+o(1)).                      (6.3)
```

Both are smaller than `D^(16/11)`:

```text
181/176<16/11,                 247/176<16/11.     (6.4)
```

Equations (4.3), (5.4), and (6.3), plus the repeated/permutation sectors,
prove (0.1).

---

## 7. Operator and transverse consequences

The exact fourth trace satisfies

```text
||A_z||_op^4
 <=tr((A_z^*A_z)^2)
 <=2D+|Q_nd(z)|.                                   (7.1)
```

Taking fourth roots of (0.1) proves (0.2).  The smooth transverse kernel
contains all cubic orientations, and the already proved Schwartz
truncation/tail transfer converts an operator exponent `theta` according to

```text
transverse exponent=1/2+theta*(2-A),
A=50/33,                    2-A=16/33.             (7.2)
```

With `theta=4/11`,

```text
1/2+(4/11)*(16/33)
 =1/2+64/363
 =491/726.                                          (7.3)
```

For comparison,

```text
4/11<47/128,
491/726<179/264.                                   (7.4)
```

```text
universal fixed-color slice bound m(C)<<D/lambda2: PROVED;
short relation branch D^(16/11):                   PROVED;
long broad branch D^(16/11):                       PROVED;
long middle branch o(D^(16/11)):                   PROVED;
absolute fourth trace D^(16/11+o):                 PROVED;
carry operator D^(4/11+o):                         PROVED;
transverse exponent 491/726 via smooth transfer:   PROVED;
full four-cycle D^(1+o):                           OPEN;
quarter-power operator / 41/66:                    OPEN;
QP or a uniform strip:                             NOT CLAIMED.
```
