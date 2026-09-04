# QP four-cycle: three-eighths operator and `45/66` transverse theorem

**Date:** 2026-08-15  
**Verdict:** the newly proved fixed-color classification has an immediate
global consequence even without the full four-cycle estimate.  Uniformly
for `||z||_2=1`, the truncated prime-power carry matrix satisfies

```text
||A_z||_op << D^(3/8) q^o(1).                       (0.1)
```

This improves the previous coefficient-uniform `D^(1/2)` Schur scale by
the fixed power `D^(1/8)`.  In the existing transverse transfer, where a
carry operator exponent `theta` contributes `theta*(16/33)` above the
generic `1/2`, (0.1) changes the full-shell exponent from

```text
49/66 = 1/2+(1/2)*(16/33)
```

to

```text
45/66 = 15/22 = 1/2+(3/8)*(16/33).                 (0.2)
```

The desired four-cycle theorem would give `D^(1/4)` and `41/66`; neither
is asserted here.  The result is an unconditional intermediate power
saving obtained from the completed fixed-color classification.

---

## 1. Input: the uniform square-root completion theorem

For an oriented all-distinct color matrix

```text
C=(c11,c12;c21,c22),                                (1.1)
```

let `m(C)` be its number of actual carrier completions.  The successive-
minima/conic dichotomy and the fixed-secant nonparabolic theorem together
give

```text
m(C) << D^(1/2) q^o(1).                             (1.2)
```

Here is the short proof, included to make the dependency exact.

* If the first two minima of the common-level `E` lattice have product
  at least a fixed multiple of `D`, that lattice has `O(D)` vectors in the
  length-`D` box.  Every nonzero realized fixed `(C,E)` has multiplicity
  `q^o(1)`, by the nonparabolic norm-conic theorem.  Hence
  `m(C)(m(C)-1)<<D q^o(1)`.
* Otherwise every short difference lies in one rational rank-two plane.
  The product matrices lie on the plane conic `det(P0+xV1+yV2)=0`.
  Pila's uniform conic bound gives `D^(1/2)q^o(1)` points in the irreducible
  case, while the reducible lines contain only `O(1)` actual completions by
  the nonzero-determinant difference lemma.

Thus (1.2) holds in both branches.  It is sharp for full-integer geometry:
the translation tangent family has `m(C)asymp sqrt(D)`.  No pointwise
improvement of (1.2) is used below.

---

## 2. Absolute fourth trace

Put

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|.                  (2.1)
```

The exact determinant/residual theorem proved that every nondegenerate
actual rectangle has

```text
1<=|det C|<<D,                                      (2.2)
```

and its divisor-energy estimate gives

```text
sum_C w_z(C)<<D q^o(1)||z||_2^4.                   (2.3)
```

The sum in (2.3) is over the all-distinct nondegenerate color sector.  The
already classified repeated-node and permutation sectors contribute only
`O(D q^o(1)||z||_2^4)` to the fourth trace.

For the remaining completed rectangles, take absolute values and group by
the oriented color matrix.  Equations (1.2) and (2.3) give

```text
|Q_nd(z)|
 <=sum_C m(C) w_z(C)+O(D q^o(1)||z||_2^4)
 <<D^(3/2) q^o(1)||z||_2^4.                        (2.4)
```

This is a genuine global estimate.  It does not use the false weighted
second-moment assertion `sum m(C)^2 w_z(C)<<D`; only the proved pointwise
classification and the proved first color moment enter.

---

## 3. Operator consequence

The exact fourth-trace expansion is

```text
||A_z||_op^4
 <=tr((A_z^* A_z)^2)
 <=2D ||z||_2^4+|Q_nd(z)|.                          (3.1)
```

Combining (2.4) and (3.1), then taking fourth roots, proves

### Theorem 3.1 (three-eighths carry operator)

For every complex color vector `z`,

```text
||A_z||_op
 <<D^(3/8) q^o(1)||z||_2.                          (3.2)
```

At `D=q^(16/33+o(1))`, the saving over Schur is

```text
D^(1/2)/D^(3/8)=D^(1/8)=q^(2/33+o(1)).             (3.3)
```

Thus this is not merely a logarithmic refinement.

---

## 4. Dyadic support profile

For one normalized dyadic coefficient block with support size `M`, (3.2)
can be combined with the earlier small-support Schur and diffuse fourth-
trace estimates.  Up to `q^o(1)`, one may use

```text
||A_z||_op
 <<min(M^(1/2), D^(3/8), D^(3/4) M^(-1/4)).        (4.1)
```

The middle term is strongest throughout the previously difficult
intermediate-support plateau

```text
D^(3/4) <= M <= D^(3/2).                            (4.2)
```

An `O(log q)` dyadic decomposition costs only `q^o(1)` by Cauchy--Schwarz
over the block `ell^2` masses, so (3.2) remains uniform for arbitrary
coefficient profiles.

The profile also shows exactly why this result stops at exponent `3/8`.
Neither the pointwise completion theorem nor the diffuse estimate lowers
the plateau in (4.2).  Reaching `D^(1/4)` still requires weighted secant
reuse or a direct tangent/generic trace decomposition.

---

## 5. Transverse exponent

The existing carry-to-transverse bookkeeping has the form

```text
transverse exponent =1/2+theta*(2-A),               (5.1)
```

when the carry operator is `D^(theta+o(1))` and
`D=Y^(2-A+o(1))`.  At the active aperture

```text
A=50/33,                  2-A=16/33.                (5.2)
```

Substitution of `theta=3/8` gives

```text
1/2+(3/8)*(16/33)=1/2+2/11=15/22=45/66.           (5.3)
```

Thus every downstream statement whose only arithmetic input was the
coefficient-uniform carry-operator norm may replace `49/66` by `45/66`,
with the same previously established logarithmic factors and truncation
bookkeeping.  This report does not independently restate those analytic
transfer hypotheses.

```text
uniform fixed-color completion m(C)<<sqrt(D)q^o:    PROVED;
absolute fourth trace <<D^(3/2)q^o:                 PROVED;
uniform carry operator <<D^(3/8)q^o:                PROVED;
transverse exponent 45/66 via existing transfer:    PROVED;
target operator exponent 1/4 / exponent 41/66:      OPEN;
full four-cycle bound:                              OPEN;
QP or uniform strip:                                NOT CLAIMED.
```
