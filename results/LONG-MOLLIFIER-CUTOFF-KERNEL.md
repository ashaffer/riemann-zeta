# Exact cutoff kernel for the long-mollifier strip route

Status: **exact kernel identity and deterministic bounds proved; no new
mollified-moment estimate or zero-free strip is claimed.**

Date: 2026-08-09.

This note resolves Gate B of
[`LONG-MOLLIFIER-ZERO-FREE-STRIP-SPRINT.md`](LONG-MOLLIFIER-ZERO-FREE-STRIP-SPRINT.md).
It shows exactly what averaging the terminal mollifier cutoff does and does
not provide.

## 1. Cutoff Gram kernel

For `y>1` and an integer `d>=1`, define

```text
g_d(y)=1_(d<=y) log(y/d)/log y.
```

For `Y>1`, define

```text
K_Y(d,e)=integral_1^Y g_d(y)g_e(y)dy.                    (1.1)
```

Expanding the cutoff average of the logarithmic mollifier produces precisely
this kernel.

### Proposition 1.1: positive Gram identity

For every finite complex sequence `(a_d)`,

```text
sum_(d,e<=Y) a_d conjugate(a_e) K_Y(d,e)
 =integral_1^Y
   |sum_(d<=y) a_d log(y/d)/log y|^2dy
 >=0.                                                     (1.2)
```

Thus `K_Y` is positive semidefinite.  This positivity is bookkeeping, not
arithmetic cancellation: the signs of the coefficients remain entirely
inside the square.

## 2. Exact Hardy representation

Put

```text
A(x)=sum_(d<=x)a_d.
```

Since

```text
log(y/d)=integral_d^y dx/x,
```

finite sum--integral interchange gives

```text
sum_(d<=y)a_d log(y/d)
 =integral_1^y A(x)dx/x.                                 (2.1)
```

Substitution into (1.2) yields the exact identity

```text
sum_(d,e<=Y) a_d conjugate(a_e) K_Y(d,e)
 =integral_1^Y 1/(log y)^2
   |integral_1^y A(x)dx/x|^2dy.                          (2.2)
```

This is the structural conclusion of the cutoff audit:

> terminal-cutoff averaging is a positive Hardy operator applied to the
> cumulative coefficient sums.

It does not manufacture a sign or a fixed power saving.  Any such saving has
to enter through cancellation in `A(x)` or through cancellation with the
other completed pieces of the approximate functional equation.

A direct Cauchy--Schwarz consequence is

```text
(2.2)
 <=integral_1^Y |A(x)|^2/x
    [integral_x^Y dy/log y] dx.                          (2.3)
```

Formula (2.3) is useful as a sufficient bound, but applying it before the
prime head, late-divisor correction, and dual approximate-functional-equation
piece have been combined may discard the cancellation needed for a strip.

## 3. Closed form

Let

```text
m=max(d,e),  a=log d,  b=log e.
```

If `m>=Y`, then `K_Y(d,e)=0`.  If `1<m<Y`, expansion of the integrand gives

```text
K_Y(d,e)
 =integral_m^Y [1-(a+b)/log y+ab/(log y)^2]dy.            (3.1)
```

Using

```text
integral_m^Y dy/(log y)^2
 =li(Y)-li(m)-Y/log Y+m/log m,                            (3.2)
```

one obtains

```text
K_Y(d,e)
 =(Y-m)
 +(ab-a-b)[li(Y)-li(m)]
 -ab[Y/log Y-m/log m].                                   (3.3)
```

The removable case `d=e=1` is simply

```text
K_Y(1,1)=Y-1.                                            (3.4)
```

No asymptotic input enters these formulas.

## 4. Log-coordinate mixed derivative

Write

```text
L=log Y,
calK_L(alpha,beta)=K_Y(exp alpha,exp beta).
```

Away from the diagonal `alpha=beta`, differentiation under the integral,
with vanishing lower-boundary terms, gives

```text
partial_alpha partial_beta calK_L(alpha,beta)
 =integral_max(alpha,beta)^L exp(u)/u^2 du >0.            (4.1)
```

The kernel is therefore a nested-tail covariance in log-cutoff coordinates,
not a sharply localized delta kernel.  Taking cutoff differences can reveal
cumulative sums, but does not supply independent oscillation.

## 5. Two deterministic scale bounds

### 5.1 The early divisor block survives with order-`Y` mass

Fix `0<=kappa<1`.  Suppose

```text
d,e<=Y^kappa
```

and

```text
log Y >= 2 log 2/(1-kappa).                              (5.1)
```

For every `y in [Y/2,Y]`,

```text
log(y/d)/log y >= (1-kappa)/2,
log(y/e)/log y >= (1-kappa)/2.
```

Consequently

```text
K_Y(d,e) >= Y(1-kappa)^2/8.                              (5.2)
```

Thus the cutoff average does not damp the early divisor block by any power.

### 5.2 The terminal collar gains only logarithms

Fix `0<alpha<1` and assume `alpha Y>1`.  If

```text
alpha Y<=d,e<=Y,
```

then on the support of the integrand

```text
0<=log(y/d),log(y/e)<=log(1/alpha),
log y>=log(alpha Y).
```

Hence

```text
0<=K_Y(d,e)
 <=Y [log(1/alpha)]^2/[log(alpha Y)]^2.                  (5.3)
```

For the first terminal dyadic collar `Y/2<=d,e<=Y`, this is only a
`1/(log Y)^2` suppression.  It is not a fixed power of `Y` or `T`.

The bounds (5.2)--(5.3) make the scope precise: cutoff averaging can improve
weights and expose cumulative cancellation, but cannot by itself cross the
length barrier `theta=1`.

## 6. The first-band frequency barrier

The sharp reciprocal stress model has exact coefficients

```text
a_Y(n)=-mu(n),  Y<n<=2Y.
```

Let `W` be a fixed smooth time weight and use the Fourier convention

```text
hat W(xi)=integral_R W(u)exp(-iu xi)du.
```

For any finite coefficients `b_n`, direct expansion gives

```text
integral_R |sum_n b_n n^(-it)|^2 W(t/T)dt
 =T sum_(m,n) b_n conjugate(b_m)
      hat W(T log(n/m)).                                 (6.1)
```

If `hat W` is supported in a fixed bounded interval and `m,n` are of size
`Y`, only additive shifts

```text
|n-m| << H,   H=Y/T,                                    (6.2)
```

survive.  For `Y=T^theta`,

```text
H=T^(theta-1)=Y^(1-1/theta).                             (6.3)
```

A Gallagher/Fejer version of (6.1) measures the same obstruction through

```text
integral_Y^(2Y)
 |sum_(x<n<=x+H)mu(n)|^2dx.                              (6.4)
```

The natural square-root benchmark is

```text
(6.4) << Y H Y^o(1).                                    (6.5)
```

Indeed, after the standard `H^-2` normalization, (6.5) is exactly of size
`Y/H=T`, the natural critical-line second-moment scale.

The current Matomaki--Radziwill method, including Menon's 2026 refinement,
proves normalized decay for Liouville and analogously for Mobius of the form

```text
(1/Y) integral_Y^(2Y)
 |H^-1 sum_(x<n<=x+H)mu(n)|^2dx
 << (log log H/log H)^2 + logarithmic errors.             (6.6)
```

Clearing normalization makes the leading scale

```text
Y H^2 (log log H/log H)^2,                               (6.7)
```

which is larger than (6.5) by a full factor `H`, apart from logarithms.
This is why qualitative almost-all short-interval cancellation does not
produce a fixed strip.

## 7. Refined missing theorem

The cutoff audit reduces the active question to a completed, signed version
of square-root short-interval cancellation.

A valid proof must first combine:

1. the von Mangoldt head in the exact coefficient identity;
2. the late-divisor Mobius correction;
3. both halves of a smoothed approximate functional equation;
4. all boundary terms;
5. the positive cutoff kernel `K_Y`;
6. the time-frequency kernel in (6.1).

Only the resulting completed shifted form should be estimated.  Bounding the
Mobius collar by (6.6) before completion loses the factor `H` required for a
strip.

The next target is therefore an exact identity

```text
completed averaged mollified moment
 = diagonal + completed near-shift quadratic form + explicit remainder,
                                                               (7.1)
```

followed by a power-saving estimate for the **whole** near-shift form.  The
kernel calculations above are unconditional; the power saving remains open.
