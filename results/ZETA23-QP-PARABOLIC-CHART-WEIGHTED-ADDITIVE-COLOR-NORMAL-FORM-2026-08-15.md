# QP four-cycle: parabolic-chart weighted-additive color normal form

**Date:** 2026-08-15  
**Verdict:** a power-sized parabolic completion chart does force an exact
additive rectangle, but generally only after rational row/column scaling.
If its affine carrier directions are

```text
r=(r1,r2),             s=(s1,s2),                  (0.1)
```

then the scaled colors `x_ij=r_i s_j c_ij` obey

```text
x11+x22=x12+x21.                                  (0.2)
```

After removing the row/column direction gcds, the two additive gaps `h,l`
satisfy the exact determinant identity

```text
h l=-det(C) gcd(r1,r2) gcd(s1,s2).                 (0.3)
```

Thus the equal-direction translation grid is the special case with ordinary
unscaled colors.  The rational-coefficient variant still has only divisor
multiplicity per determinant layer.  What remains is to absorb the number
of carrier parameters in the direct Hankel operator, rather than multiplying
the color correlation by the fixed-color completion count.

---

## 1. Common-level pinning gives the weighted additive relation

On a parabolic chart, after clearing a fixed denominator,

```text
a(t)=a0+t r,             b(t)=b0+t s,              (1.1)
```

and `M(t)=a(t)b(t)^T`.  The pinned color level is

```text
<K,M(t)>=L,
K=(c11,-c12;-c21,c22).                              (1.2)
```

For three or more distinct chart parameters, the quadratic polynomial in
(1.2) is constant identically.  Its quadratic coefficient is

```text
r^T K s
 =r1s1c11-r1s2c12-r2s1c21+r2s2c22=0.              (1.3)
```

This is exactly (0.2).

No direction coordinate can vanish in a nonconstant actual chart.  For
example, if `r1=0`, then `a1` is fixed.  Two different values of `b_j` with
the same fixed `(a1,c_1j)` change `8a1b_jc_1j` by at least a fixed multiple
of `q^2`, larger than the width `2H=O(qD)=o(q^2)`.  Thus both column
coordinates are fixed; the bottom edges then fix the second row as well.
The other cases are symmetric.

---

## 2. Primitive gaps and determinant

Write

```text
r=g_r (rho1,rho2),       gcd(rho1,rho2)=1,
s=g_s (sigma1,sigma2),   gcd(sigma1,sigma2)=1.      (2.1)
```

Equation (1.3) says

```text
rho1(s1c11-s2c12)=rho2(s1c21-s2c22).               (2.2)
```

Coprimality gives one integer `h` with

```text
s1c11-s2c12=rho2 h,
s1c21-s2c22=rho1 h.                                (2.3)
```

The column version gives one integer `l` with

```text
r1c11-r2c21=sigma2 l,
r1c12-r2c22=sigma1 l.                              (2.4)
```

Now put `x_ij=r_i s_j c_ij`.  Its two additive gaps are

```text
x11-x12=g_r rho1 rho2 h,
x11-x21=g_s sigma1 sigma2 l.                       (2.5)
```

For any additive rectangle,

```text
x11x22-x12x21
 =-(x11-x12)(x11-x21).                             (2.6)
```

The left side is

```text
r1r2s1s2 det(C).                                   (2.7)
```

Canceling the nonzero primitive direction factors in (2.5)--(2.7) proves
(0.3).

Consequently, for fixed direction gcds and fixed nonzero determinant `k`,
the normalized gaps have only

```text
tau(|k| g_r g_s)=q^o(1)                            (2.8)
```

possibilities.  Summing over `1<=|k|<<D` costs only `Dq^o(1)`, independent
of the sizes of the primitive slope numerators.

For fixed directions and gaps, all four colors are affine rational
functions of one base color.  The corresponding four-correlation is at most
`||z||_2^4` by two applications of Cauchy--Schwarz, because each relevant
pair map is injective.  This rigorously proves the color-side divisor budget
suggested by the ordinary additive model.

---

## 3. Exact remaining narrow step

The color normal form alone does not remove fixed-color completion
multiplicity.  A chart with `T` carrier parameters repeats the same color
monomial `T` times.  Multiplying the `Dq^o(1)` color budget by the pointwise
bound `T<=sqrt(D)q^o(1)` would lose `sqrt(D)`.

The affine/Hankel patch theorem shows how this loss disappears in the equal-
direction translation grids: charts with overlapping colors merge before
the fourth trace is taken.  The remaining narrow theorem must extend that
operator merger to the rationally scaled normal form (2.3)--(2.4).  In
particular, it must use the shared carrier parameter and cannot be replaced
by a scalar sum of `m(C)w(C)` estimates.

```text
weighted additive relation (0.2):                  PROVED;
zero direction coordinates excluded:               PROVED;
primitive determinant-gap identity (0.3):          PROVED;
color-side divisor budget D q^o:                    PROVED;
rational-chart operator merger across colors:      OPEN;
global narrow four-cycle bound:                     OPEN.
```

The exact identities are replayed in
`src/qp_four_cycle_parabolic_color_normal_form.py` and its test module.

