# The actual prime--Laguerre sign below 2

## Exact pole cancellation, zero saddles, and the finite-degree frontier

**Date:** 2026-08-13  
**Target:** `alpha_m(1.999998)>=0` for every `m>=1`.

**Binary verdict:** **not proved; no uniform strip follows.**  The direct
prime calculation does, however, identify the obstruction exactly.  The
exponentially large alternating saddle in the uncentered prime sum is the
continuous prime-density term, and it cancels coefficient-for-coefficient
with the pole of `zeta` at 1.  After that cancellation, the remaining
exponential modes are precisely

```text
q_tau(rho)^m,             q_tau(rho)=rho/(rho-tau),
```

for nontrivial zeros `rho`.  Such a mode grows exactly when
`Re rho>tau/2`.  Thus sharper Plancherel--Rotach analysis cannot dispose of
the last saddle: its absence is the desired zero-free assertion itself.

The strongest clean consequence obtained here is finite in degree.  If zeros
through a sufficiently large height `H` lie in `Re rho<=tau/2`, then all
coefficients through

```text
m <= c_tau H/((1-tau/2) log(2H))
```

are positive.  The Vinogradov--Korobov zero-free region makes this range in
principle effective at `tau=1.999998` after explicit constants and a finite
low-height check are supplied, but never infinite.

---

## 1. The exact actual-prime ledger

Put `s=tau/(1-t)` and, with `n=m-1`, use

```text
sum_(n>=0) L_n^(1)(x)t^n=(1-t)^(-2)exp(-xt/(1-t)).       (1.1)
```

For `tau>1`, the prime coefficient is absolutely convergent at every fixed
degree:

```text
P_n(tau)=sum_(q>=2) Lambda(q)q^(-tau)L_n^(1)(tau log q),

sum_(n>=0)P_n(tau)t^n
 =(1-t)^(-2)(-zeta'/zeta)(tau/(1-t)).                    (1.2)
```

From

```text
xi'/xi(s)=1/s+1/(s-1)-(log pi)/2
           +(1/2)Gamma'/Gamma(s/2)+zeta'/zeta(s),        (1.3)
```

define `B_n(tau)` to be the coefficient contributed by all displayed
terms except `1/(s-1)` and `zeta'/zeta`.  Then

```text
alpha_(n+1)(tau)=B_n(tau)+I_n(tau)-P_n(tau),             (1.4)
```

where the pole coefficient equals the continuous prime-density integral:

```text
I_n(tau)
 =[t^n] 1/((1-t)(tau-1+t))
 =integral_1^infinity x^(-tau)L_n^(1)(tau log x) dx
 =1/tau {1+(-1)^n(tau-1)^(-n-1)}.                       (1.5)
```

Consequently, with `psi(x)=sum_(q<=x)Lambda(q)`, the exact centered form is

```text
R_n(tau)=P_n(tau)-I_n(tau)
 =integral_(1-)^infinity x^(-tau)L_n^(1)(tau log x)
                         d(psi(x)-x),

alpha_(n+1)(tau)=B_n(tau)-R_n(tau).                      (1.6)
```

For `tau<2`, the second term in (1.5) has size
`(tau-1)^(-n-1)` and alternating sign.  It is therefore invalid to bound
the prime sum and the pole term separately.  Their exact cancellation is
the first indispensable saddle cancellation.

---

## 2. The Mellin transform exposes every remaining saddle

For a complex parameter `rho`, direct Laplace transformation of (1.1)
gives

```text
J_n(rho;tau)
 =integral_1^infinity x^(rho-tau-1)L_n^(1)(tau log x) dx
 =1/tau {1-(rho/(rho-tau))^(n+1)}.                       (2.1)
```

Indeed,

```text
sum_(n>=0)J_n(rho;tau)t^n
 =1/((1-t)(tau-rho+rho t)).                              (2.2)
```

Insert the explicit formula for `d(psi-x)`, first truncated symmetrically
in zero height and then pass to the limit.  The trivial-zero and boundary
terms recombine with `B_n`; the nontrivial-zero terms in (2.1) give exactly
Freitas's formula

```text
alpha_m(tau)=1/tau sum_rho {1-q_tau(rho)^m},
q_tau(rho)=rho/(rho-tau).                                (2.3)
```

Conjugate zeros are paired throughout.  This derivation does not use a
termwise absolutely convergent untruncated explicit formula.

For `rho=beta+i gamma`,

```text
|q_tau(rho)|^2
 =1+2tau(beta-tau/2)/((beta-tau)^2+gamma^2).              (2.4)
```

Equivalently, the zero pole occurs in the `t`-plane at

```text
t_rho=1-tau/rho=q_tau(rho)^(-1),

|t_rho|<1  <=>  beta>tau/2.                              (2.5)
```

Equations (2.1)--(2.5) answer the saddle-cancellation question sharply.
After the pole-at-1 mode (1.5) is removed, an interior zero pole cannot be
canceled analytically by the archimedean factor or by a distinct zero:
its location and residue are unique (multiplicity only enlarges the
residue).  Excluding all such interior poles is exactly excluding zeros in
`Re rho>tau/2`.  Oscillation can hide a mode at selected degrees, but it
does not turn this all-degree problem into an error-estimate problem.

---

## 3. A rigorous finite-degree theorem

Write

```text
epsilon=1-tau/2>0.
```

The contribution of the conjugate pair `rho,rho-bar` is

```text
C_m(rho)=2/tau {1-r_rho^m cos(m theta_rho)},
q_tau(rho)=r_rho exp(i theta_rho).                        (3.1)
```

It is nonnegative if `beta<=tau/2`.  If `beta>tau/2`, then `beta<=1`
and (2.4) gives

```text
log r_rho <= tau epsilon/gamma^2.                         (3.2)
```

Hence, when `gamma>=H` and `m tau epsilon/H^2<=1`,

```text
[C_m(rho)]_- <= 2/tau (exp(m tau epsilon/gamma^2)-1)
                <= 4m epsilon/gamma^2.                   (3.3)
```

The Riemann--von Mangoldt estimate implies

```text
sum_(gamma>=H) gamma^(-2) <= C log(2H)/H.                 (3.4)
```

Choose one known critical-line zero `rho_0` below `H` (so `H` is assumed
larger than the ordinate of this fixed zero).  It supplies the
degree-uniform positive margin

```text
c_(tau,0)=2/tau (1-|q_tau(rho_0)|)>0.                     (3.5)
```

All other safe pairs may be discarded from a lower bound.  Therefore:

### Proposition 3.1

Fix a known critical-line zero `rho_0`, and take `H>Im(rho_0)` sufficiently
large.  If every nontrivial zero with `0<Im rho<H` satisfies
`Re rho<=tau/2`, then

```text
alpha_m(tau)
 >=c_(tau,0)-C m epsilon log(2H)/H                        (3.6)
```

whenever `m tau epsilon/H^2<=1`.  In particular, after decreasing the
effective constant so that this auxiliary condition is also satisfied,

```text
alpha_m(tau)>0 for
m <= c'_(tau,0) H/(epsilon log(2H)).                      (3.7)
```

All constants can be made effective.  This is a genuine consequence for
the actual coefficients, not a finite-prime truncation.

---

## 4. Best unconditional range obtained by this contour

An effective Vinogradov--Korobov region has the form

```text
beta <= 1-c_0/
 [(log(|gamma|+3))^(2/3)(log log(|gamma|+3))^(1/3)].       (4.1)
```

Choose `H=H_epsilon` so that the width on the right of (4.1) is at least
`epsilon` through height `H`.  Up to effective constants,

```text
log H_epsilon
  asymp epsilon^(-3/2)/sqrt(log(1/epsilon)).               (4.2)
```

Combining (3.7) and (4.2), together with explicit zero-free-region constants
and a rigorous check of the remaining compact low-height range, would give
positivity through

```text
M_epsilon
 >= c H_epsilon/(epsilon log H_epsilon),                  (4.3)
```

At the target, `epsilon=10^(-6)`, the logarithmic height scale
is of order `10^9/sqrt(log 10^6)` before the constants in (4.1) are
inserted.  No numerical height, and hence no instantiated numerical degree
range, is claimed here without those constants and the stated finite check.

For **all degrees**, the direct pair geometry proves unconditionally only

```text
tau>=2.                                                   (4.4)
```

For every fixed `tau<2`, (4.1) eventually becomes narrower than
`1-tau/2`; it supplies no all-height exclusion and hence no all-degree
sign theorem.  Formula (4.3), not an infinite range, is the best clean
unconditional output of this contour/absolute-tail attack.

---

## 5. Why Plancherel--Rotach does not extend (4.3) to infinity

Under `y=tau log x`, the continuous-density integral has exponential
weight

```text
exp(-y+y/tau)L_n^(1)(y).
```

In the oscillatory Laguerre region, Plancherel--Rotach contributes the
envelope `exp(y/2)`; near the turning scale `y about 4n`, the remaining
absolute envelope is therefore

```text
exp((1/tau-1/2)y) about exp(4 epsilon n/tau).              (5.1)
```

The Vinogradov--Korobov PNT remainder contributes only a subexponential
gain on this scale,

```text
exp(-c n^(3/5)(log n)^(-1/5)).                            (5.2)
```

Thus any argument taking absolute values eventually loses to the linear
`epsilon n` exponent.  Equations (5.1)--(5.2) are an envelope diagnosis,
not a replacement proof of Proposition 3.1.  The exact residue calculation
(2.1)--(2.5) explains the phenomenon: beyond the finite VK range the
uncontrolled object is a possible genuine zero pole, not slack in the
Laguerre asymptotic.

---

## 6. Reproducible algebra check

For `n=0,...,8`, expand

```text
L_n^(1)(y)=sum_k a_k y^k
```

and use `integral_0^infinity exp(-a y)y^k dy=k!/a^(k+1)`.
The following two identities simplify symbolically to zero:

```text
(1/tau) sum_k a_k k!/((tau-1)/tau)^(k+1)
 -1/tau*(1+(-1)^n/(tau-1)^(n+1));

(1/tau) sum_k a_k k!/(1-rho/tau)^(k+1)
 -1/tau*(1-(rho/(rho-tau))^(n+1)).                        (6.1)
```

They verify independently the principal pole mode (1.5) and every zero
mode (2.1).

---

## Truth boundary

This report proves exact cancellation of the prime-density saddle, the
exact zero-pole conformal geometry, and a VK-powered finite-degree
positivity range.  It does **not** prove `alpha_m(1.999998)>=0` for every
`m`, does **not** improve a zero-free region, and does **not** prove a
uniform zero-free strip.
