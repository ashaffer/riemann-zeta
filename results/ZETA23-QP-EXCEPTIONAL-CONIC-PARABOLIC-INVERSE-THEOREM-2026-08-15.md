# QP four-cycle: exceptional-conic parabolic inverse theorem

**Date:** 2026-08-15  
**Verdict:** the polynomial-size part of the exceptional fixed-color branch
is necessarily a rational tangent family.  More precisely, when all product
matrices completing one color matrix lie in the exceptional rational
two-plane, its rank-one conic has the dichotomy

```text
nonparabolic conic:       m(C)<<q^o(1);
parabolic conic:          q^o(1) affine rational-tangent charts. (0.1)
```

Thus, for every fixed `epsilon>0`, `m(C)>=q^epsilon` forces the parabolic
alternative.  This is the inverse statement behind the translation grid: a
power-sized exceptional completion family cannot be a generic Pell conic.

This remains a fixed-color theorem.  It does not yet bound weighted reuse of
the tangent charts across different color matrices.

---

## 1. Plane section and its points at infinity

The exceptional successive-minima theorem puts all product matrices for a
fixed color matrix in

```text
M(x,y)=P0+xV+yW,               x,y in Z.            (1.1)
```

Completion matrices obey `F(x,y)=det M(x,y)=0`.  Its homogeneous quadratic
part is

```text
F_2(x,y)=det(V)x^2+B(V,W)xy+det(W)y^2,              (1.2)

B(V,W)=V11 W22+W11 V22-V12 W21-W12 V21.            (1.3)
```

The invariant discriminant is

```text
Delta_infinity=B(V,W)^2-4 det(V)det(W).             (1.4)
```

The conic is parabolic exactly when (1.4) vanishes, provided the full conic
is irreducible and genuinely quadratic.  This condition is independent of
the chosen plane basis up to a nonzero square factor.

For the translation grid

```text
a(t)=a0+t(1,1),       b(t)=b0-t(1,1),              (1.5)
```

the product matrix is `M(t)=M(0)+tV-t^2J`, with `J` the all-ones rank-one
matrix.  Direct calculation gives

```text
det(J)=0,       B(V,J)=0,                           (1.6)
```

so its plane section is parabolic.

---

## 2. Nonparabolic sections have only `q^o(1)` integral points

Assume the conic is absolutely irreducible and
`Delta_infinity!=0`.  Its full projective determinant is then nonzero;
otherwise the projective conic would be singular and reducible over the
algebraic closure.

An integral shear and completion of squares transform the equation,
injectively and with only congruence restrictions, into a binary norm
equation

```text
X^2-dY^2=N,             dN!=0,                     (2.1)
```

whose coefficients, right side, and coordinate box have size `q^O(1)`.  If
`d` is a square, (2.1) factors and the divisor bound applies.  If it is
nonsquare, ideal divisors of `(N)` in the quadratic order give `q^o(1)`
possibilities; generators differ by units, and only `O(log q)` unit powers
have polynomial height.  Therefore

```text
# {(x,y) in Z^2:F(x,y)=0, |x|+|y|<=q^O(1)}<<q^o(1). (2.2)
```

The product-matrix map is injective in the all-distinct actual sector, so
(2.2) proves the first line of (0.1).  Reducible plane sections contain at
most a constant number of actual completions: a line containing three would
force a rank-one difference, contrary to the proved nonzero-determinant
theorem.

---

## 3. A parabolic section factors into affine carrier directions

Now suppose the irreducible conic is parabolic.  Its repeated point at
infinity is rational because (1.2) has integral coefficients and
discriminant zero.  After an integral linear change, one primitive integral
coordinate `t` parametrizes its integral points and the other coordinate is
a quadratic polynomial in `t`, subject only to fixed congruence conditions.
Consequently

```text
M(t)=M0+tM1+t^2M2,        det M(t) identically 0.   (3.1)
```

Over `Q[t]`, a rank-one two-by-two polynomial matrix factors as

```text
M(t)=u(t)v(t)^T.                                    (3.2)
```

The total degree is two.  A degree split `(0,2)` or `(2,0)` would give all
matrices a common row or column projective direction, making every
difference `M(t)-M(t')` rank at most one.  That contradicts the nonzero
determinant theorem for distinct actual completions.  Hence

```text
deg u=deg v=1.                                     (3.3)
```

After clearing one fixed denominator,

```text
u(t)=u0+t u1,             v(t)=v0+t v1.            (3.4)
```

Returning to primitive actual carrier vectors costs only `q^o(1)` charts.
Indeed, `gcd(u_1(t),u_2(t))` divides the fixed resultant `det(u0,u1)`, and
similarly for `v`; each resultant has only `q^o(1)` divisors.  After fixing
these gcds and the denominator congruences, both carrier vectors are affine
rational functions of the same integral parameter `t`.  These are precisely
rational tangent/Hankel charts.  This proves the second line of (0.1).

---

## 4. Consequence and remaining global gate

Combining this theorem with the exceptional-plane theorem gives

```text
m(C)>=q^epsilon
  ==> one parabolic direction at infinity
  ==> q^o(1) rational tangent charts.               (4.1)
```

The window-thickened affine/Hankel theorem controls every fixed exact-
progression chart at `O(Dq^o(1))`.  What is not proved is that parabolic
charts arising from many color matrices group into only `q^o(1)` exact-
progression families per relevant color pair.  That cross-color reuse
statement, or a broad incidence substitute, is the remaining global narrow
gate.

```text
nonparabolic exceptional conic count q^o:           PROVED;
power multiplicity forces parabolic section:        PROVED;
parabolic carrier factorization into q^o charts:    PROVED;
weighted cross-color tangent-chart reuse:           OPEN;
global four-cycle bound:                            OPEN.
```

The invariant (1.4) and translation-grid replay are in
`src/qp_four_cycle_parabolic_inverse.py` and
`src/test_qp_four_cycle_parabolic_inverse.py`.

