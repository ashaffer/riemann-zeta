# QP reciprocal strip: nonzero Poisson cubic saddles and the dyadic gate

**Date:** 2026-08-24  
**Verdict:** nonzero dual cubic saddles really occur, but they do not account
for the missing power in the fixed-pair-sum estimate.  Every degeneracy is
exactly cubic, exact integer cubics form only `O(H)` frequency pairs, and their
total Selberg-weighted cost is at most

```text
delta^2 q^(2/3) H^(2/3) = D^(-1/24).
```

A uniform dyadic stratification, including one possibly near-cubic dual mode
for every opposite-sign pair, still gives the previously reported absolute
ceiling

```text
delta^2 sqrt(q) H^(5/2) = D^(25/16).
```

Thus the unresolved `H=D^(17/16)` cancellation is a problem among the regular
nonzero saddles, not an omitted cubic loss.  No such collective cancellation
theorem is proved here.

## 1. Complete classification of degenerate saddles

Write

```text
F(x)=C(h/x+k/(S-x))-m*x,       0<x<S.                 (1.1)
```

Its first three derivatives are

```text
F'(x) = C(-h/x^2+k/(S-x)^2)-m,
F''(x)=2C(h/x^3+k/(S-x)^3),
F'''(x)=6C(-h/x^4+k/(S-x)^4).                         (1.2)
```

If `h*k>=0`, then `F''` has no interior zero.  If `h*k<0`, put
`u=|h|`, `v=|k|`.  There is exactly one zero of `F''`, namely

```text
x_* = S*u^(1/3)/(u^(1/3)+v^(1/3)).                    (1.3)
```

At this point

```text
m_* = -sgn(h) C (u^(1/3)+v^(1/3))^3/S^2.             (1.4)
```

For example, when `h>0,k<0`, direct substitution gives

```text
F'''(x_*)
 =-6C*u*S/(x_*^4*(S-x_*)) != 0.                      (1.5)
```

Therefore a stationary point satisfying `F''=0` has order exactly three.
There are no quartic or higher saddles in the physical interval.

## 2. Integer cubic saddles and their sparsity

Here `S` is an integer and the physical product centre satisfies
`C/S^2=A/B in Q`, written in lowest terms.  No bounded-denominator hypothesis
is being made.  (The classification in this section is not asserted for an
arbitrary real centre.)  If the caustic value (1.4) is an integer,
multiplication by the rational number `S^2/C` shows that

```text
z=(u^(1/3)+v^(1/3))^3
```

must be rational.  This has a simple exact classification:

> **Lemma.** For positive integers `u,v`, the number `z` is rational if and
> only if
>
> ```text
> u=d*r^3,       v=d*s^3,       (r,s)=1               (2.1)
> ```
>
> for positive integers `d,r,s`.

Indeed, put `alpha=(u/v)^(1/3)`.  Rationality of `z/v=(alpha+1)^3`, together
with `alpha^3 in Q`, makes `3alpha^2+3alpha+1` rational.  Thus
`alpha^2+alpha=t in Q`, and

```text
alpha^3=alpha*(t+1)-t.
```

The exceptional possibility `t=-1` has no positive real solution, so
`alpha` is rational.  Clearing the coprime numerator and denominator gives
(2.1).  The converse is immediate.  In these parameters,

```text
x_* = S*r/(r+s),
m_* = -sgn(h) C*d*(r+s)^3/S^2.                       (2.2)
```

Integrality imposes the additional divisibility

```text
B | d*(r+s)^3.                                       (2.3)
```

The number of pairs with `u,v<=H` satisfying (2.1) is `O(H)`, uniformly in
`C,S`, since

```text
sum_(r,s coprime) H/max(r,s)^3
  << H sum_(n>=1) n/n^3
  << H.                                              (2.4)
```

The divisibility (2.3), whatever the denominator `B`, can only reduce this
count.  Requiring `x_*` to lie in the physical
cutoff can only reduce it again (and in fact forces `r/s` into a fixed compact
ratio range).

Exact cubic saddles are not merely formal.  Take

```text
C=Q^2,       S=2Q,       h=t,       k=-t,
m=-2t,       x_*=Q.                                  (2.5)
```

All variables are integral and `F'(Q)=F''(Q)=0`, while `F'''(Q)!=0`.

## 3. Exact centered cusp normal form

The symmetric example admits an exact, not asymptotic, reparametrization.
Set

```text
x=Q+y,       p=h+k,       d=k-h,       ell=d-m.       (3.1)
```

For `C=Q^2,S=2Q`, elementary division gives

```text
F(Q+y)
 =Q*(p-m)+ell*y+(Q*p*y^2+d*y^3)/(Q^2-y^2).           (3.2)
```

Thus `p` is the curvature variable, `ell` is the transverse distance to the
centered stationary point, and `p=ell=0` is the cubic cusp.  The inverse
frequency map is

```text
h=(p-d)/2,       k=(p+d)/2.                           (3.3)
```

This is a plausible coordinate system for a collective Airy/large-sieve
estimate.  It does not itself provide cancellation: on the cusp `p=0`, the
Selberg coefficient is

```text
c_h*c_k=c_(-d/2)*c_(d/2)=|c_(d/2)|^2                 (3.4)
```

for a real symmetric majorant.

For the family (2.5), (3.2) reduces modulo its integral constant to

```text
F(Q+y)=(-2t)*y^3/(Q^2-y^2).                           (3.5)
```

With a symmetric cutoff, the conjugate pair removes the odd imaginary part
but leaves the nonzero real Airy main term.  Consequently there is no
coefficient or conjugation cancellation forced on this family.

## 4. Uniform termwise and dyadic bounds

Assume the cutoff lies where

```text
x asymp S-x asymp q,       C asymp q^2,
|h|,|k| asymp K.                                      (4.1)
```

For same-sign `h,k`, one has `|F''| asymp K/q`.  The second-derivative
estimate therefore gives

```text
|I(h,k,m)| << sqrt(q/K).                              (4.2)
```

For opposite signs, `F'''` has constant sign and
`|F'''| asymp K/q^2`; the uniform cubic estimate gives

```text
|I(h,k,m)| << q^(2/3) K^(-1/3).                      (4.3)
```

Using (4.3) for every one of the `O(K)` relevant values of `m` would produce
the unnecessarily large `D^(25/12)`.  There is only one caustic per pair.
Let `m_*` be (1.4).  Away from the integer nearest to `m_*`, Taylor's theorem
at `x_*` gives, at a stationary point,

```text
|F''| asymp sqrt(K*|m-m_*|)/q.
```

Splitting the two sides of `x_*` and applying the second-derivative estimate
therefore yields

```text
|I(h,k,m)|
 << sqrt(q) K^(-1/4) |m-m_*|^(-1/4)                 (4.4)
```

for the nonexceptional integer modes.  Frequencies outside `|m|<<K` are
removed by integration by parts.  Since only one integer can be nearest to
`m_*`, (4.3)--(4.4) imply the uniform fixed-pair sum

```text
sum_m |I(h,k,m)|
 << q^(2/3)K^(-1/3)+sqrt(q)K^(1/2).                  (4.5)
```

There are `O(K^2)` pairs in a dyadic block.  After the two Selberg
coefficients, the two terms in (4.5) contribute at `K=H`

```text
delta^2 q^(2/3) H^(5/3) = D^(49/48),
delta^2 sqrt(q) H^(5/2) = D^(25/16).                 (4.6)
```

The regular term dominates.  Restricting the first term to *exact* cubic
pairs and using (2.4) improves it to

```text
delta^2 q^(2/3) H^(2/3)=D^(-1/24).                  (4.7)
```

For reference, the exponent arithmetic uses

```text
q=D^(33/16),       delta=D^(-17/16),       H=D^(17/16).
```

## 5. Decisive conclusion

The fixed-pair-sum report's `D^(25/16)` absolute nonzero-dual bound remains
valid after the omitted saddle coalescence is treated correctly.  Cubic
saddles neither disprove the desired `sqrt(D)` estimate nor supply its proof.
The exact remaining theorem must save

```text
D^(25/16-1/2)=D^(17/16)=H                            (5.1)
```

collectively across the regular three-index `(h,k,m)` aggregate.  Formula
(3.2) exposes the cusp geometry a successful theorem must tolerate, while
(3.4) shows that arbitrary optimism about sign cancellation at the cusp is
unjustified.

## Reproducibility

Exact algebra and exponent ledgers are in:

```text
src/qp_nonzero_poisson_cubic_saddle.py
src/test_qp_nonzero_poisson_cubic_saddle.py
```
