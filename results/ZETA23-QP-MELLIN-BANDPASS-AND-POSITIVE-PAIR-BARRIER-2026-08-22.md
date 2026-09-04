# QP dyadic reciprocal moment: Mellin and positive-pair barrier

**Date:** 2026-08-22  
**Verdict:** Mellin separation is exact, but an ordinary positive
Dirichlet-polynomial mean value cannot prove the scale-correct dyadic
reciprocal moment.  The Mellin bandwidth is `T=K*q`, whereas there are only
`K` reciprocal-frequency outputs.  Even granting an ideal Bessel step, the
diagonal of the positive Mellin mean is too large by a power of `q` on the
entire active range.  Replacing it by a positive near-pair count also fails:
the generic close-pair volume is polynomially larger than the target at the
upper frequencies.  The dyadic kernel cancels that volume because its
Fourier transform has integral zero.  Thus the missing statement is a
**centered band-pass pair-correlation theorem**, equivalently the signed
shifted-multiplication-table HSM already isolated in stationary
coordinates.

This is a method obstruction, not a counterexample to

```text
sum_(ell~K)|S_ell(A,C)|^2 << (q^2/K) q^o(1).       (0.1)
```

No new four-cycle exponent is proved here.

---

## 1. Exact Mellin separation and its bandwidth

Let `A,C` lie in fixed compact subintervals of the `q`-shell and insert
fixed smooth shell majorants.  Put

```text
x=a/q,  y=c/q,  lambda_ell=ell*q/8,
S_ell=sum_(a,c) w_1(x)w_2(y)e(lambda_ell/(x*y)).   (1.1)
```

Choose `w_0` equal to one on all products `x*y` occurring in (1.1), and
let

```text
g_lambda(z)=w_0(z)e(lambda/z),
g_hat_lambda(t)=integral_0^infinity
  g_lambda(z) z^(-it) dz/z.                        (1.2)
```

Mellin inversion gives exactly

```text
S_ell=(2*pi)^(-1) integral_R g_hat_(lambda_ell)(t)
  A(t)C(t) dt,                                    (1.3)

A(t)=sum_a w_1(a/q)(a/q)^(it),
C(t)=sum_c w_2(c/q)(c/q)^(it).                    (1.4)
```

In the logarithmic coordinate `z=exp(u)`, the phase in
`g_hat_lambda(-tau)` is

```text
2*pi*lambda*exp(-u)+tau*u.                         (1.5)
```

Its stationary point satisfies

```text
tau=2*pi*lambda*exp(-u).                           (1.6)
```

Since `u` stays in a fixed compact interval, stationary phase yields

```text
tau asymp lambda,
|g_hat_lambda(-tau)|<<lambda^(-1/2),               (1.7)
```

with rapid decay off a fixed enlargement of that interval.  Parseval gives
`integral |g_hat_lambda(t)|^2 dt=O(1)`.  Consequently, on a dyadic block
`ell~K`, the Mellin bandwidth is

```text
T=K*q.                                             (1.8)
```

This is much longer than the output list: `T/K=q`.

## 2. Why a positive Mellin mean necessarily loses

Suppose one grants the strongest outcome that ordinary Mellin Bessel and
positive mean-value arguments could reasonably give, namely

```text
sum_(ell~K)|S_ell|^2
  << integral_(t~T)|A(t)C(t)|^2 dt.                (2.1)
```

The diagonal in the integral on the right is already

```text
T*|A|*|C| asymp K*q*D^2                           (2.2)
```

for maximal completed strips.  The desired right side in (0.1) is
`q^2/K`.  Writing `D=q^(16/33)` and `K=q^kappa`, with

```text
1/33<=kappa<=17/33,                                (2.3)
```

the ratio of (2.2) to the target is

```text
K^2*D^2/q=q^(2*kappa+32/33-1).                    (2.4)
```

It ranges from `q^(1/33)` at the lower endpoint to `q` at the upper
endpoint.  Thus even the diagonal of the positive mean is polynomially too
large throughout the active range.  This is not a weak fourth-moment
estimate: a single exponential `(a*c)^(it)` has `L^2` mass `T`, while its
projection onto the `K` reciprocal-frequency kernels has mass only `K`.
The missing factor `K/T=1/q` is a projection phenomenon, not something a
positive full-band mean value can recover.

Equivalently,

```text
integral_(t~T)|A(t)C(t)|^2 dt
 <<sum_(a,c,a',c') min(T,q^2/|a*c-a'*c'|)          (2.5)
```

up to smooth harmless variants.  The diagonal in this standard
near-product energy is exactly (2.2).  Subtracting it still does not create
the reciprocal modulo-one aliases or the sign of the dyadic band-pass
kernel.

## 3. The exact band-pass identity

Let `W` be an even smooth nonnegative function supported in
`1<=|u|<=2`.  Put

```text
alpha_(n,n')=q^3/8*(1/n-1/n'),  n=a*c, n'=a'*c'.  (3.1)
```

Poisson summation in `ell` gives the exact identity

```text
sum_ell W(ell/K)|S_ell|^2
 =K*sum_(a,c,a',c') sum_(r in Z)
   W_hat(K*(r-alpha_(a*c,a'*c'))).                 (3.2)
```

The decisive feature is

```text
integral_R W_hat(v)dv=W(0)=0,                     (3.3)
```

because `W` is separated from zero frequency.  Thus the generic local
pair-density main term in (3.2) cancels.  Any replacement of `W_hat` by
`|W_hat|`, a Fejer kernel, or a positive close-pair majorant destroys (3.3).

## 4. A universal positive-pair lower barrier

The loss from destroying (3.3) is polynomial even before using any special
strip geometry.  Let

```text
N=|A|*|C| asymp D^2                              (4.1)
```

and place the `N` phases `q^3/(8*a*c) mod 1` into `K` equal arcs.  If the
arc occupancies are `n_1,...,n_K`, Cauchy gives

```text
sum_j n_j^2 >=N^2/K=D^4/K.                        (4.2)
```

Hence there are at least `D^4/K` ordered phase pairs at circular distance
`O(1/K)`.  A positive kernel of height `K` charges at least

```text
D^4.                                               (4.3)
```

The target is `q^2/K`.  Their ratio is

```text
K*D^4/q^2=q^(kappa-2/33).                         (4.4)
```

Therefore a positive close-pair proof is already power-too-large for every
`K>=q^(2/33+epsilon)`.  At the upper endpoint `K=q/D`, its loss is

```text
D^3/q=q^(5/11)=D^(15/16).                         (4.5)
```

This generic volume is not evidence against (0.1).  For randomly spread
phases the signed kernel in (3.2) cancels it, leaving the product diagonal
`K*D^2`, which is exactly admissible when `K<=q/D`.  Formula (4.2) shows
only that a positive spacing theorem cannot see this cancellation.

## 5. What a successful Mellin theorem would have to say

The required input is a centered estimate for (3.2), after its uniform
pair-density term has been removed, or an equivalent restriction theorem
for the `K`-dimensional reciprocal-kernel subspace inside Mellin bandwidth
`K*q`.  In the completed balanced fan coordinates, stationary phase turns
that centered form into

```text
sum_(ell~K)|sum_(j,k)u(j)v(k)
 e(3*(q^3*ell*j*k/(8*R*S))^(1/3))|^2,             (5.1)
```

with the interval-transform weights `u,v`.  Grouping `x=j*k` makes (5.1)
the signed shifted-multiplication-table HSM.  Ordinary Dirichlet-polynomial
mean values and positive near-product energies do not bound this centered
projection.

If a genuine **primal** dyadic theorem were proved with loss `D^beta`,

```text
sum_(ell~K)|S_ell|^2
 <<(q^2/K)*D^beta*q^o(1),                          (5.2)
```

then dyadic Cauchy and the Selberg coefficient would give the uniform trace
bound

```text
Q_nd(z)<<D^(1+beta/2+o(1))*||z||_2^4.             (5.3)
```

Thus `beta<5/8` would improve the current `D^(21/16)` theorem, and an actual
primal `beta=1/2` estimate would give `D^(5/4)`.  The proved local spacing
fallback `N(delta)<<delta*P^4+P^3` is not (5.2): it controls a positive
single-center/Schur subkernel before the missing cross-center aggregation.
Its factor `P=sqrt(D)` therefore cannot presently be square-rooted into a
new trace exponent.

## 6. Status

```text
exact compact-shell Mellin separation:             PROVED;
Mellin bandwidth T=K*q:                            PROVED;
positive Mellin mean closes dyadic target:          FALSE (DIAGONAL LOSS);
positive reciprocal close-pair majorant closes:     FALSE (VOLUME LOSS);
band-pass kernel has zero integral:                 PROVED;
centered pair-correlation / signed HSM estimate:     OPEN;
scale-correct dyadic moment (0.1):                  OPEN;
new slope-block or four-cycle exponent:             NONE.
```
