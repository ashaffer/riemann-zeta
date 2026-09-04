# QP reciprocal strip: fixed pair sums, tangent modes, and the nonzero-dual gate

**Date:** 2026-08-24  
**Verdict:** the pointwise bound

```text
R(S) << sqrt(D)*q^o(1)
```

for the full product strip is **not proved**.  Two sharp pieces are proved:

1. the zero Poisson mode in the exact two-inverse Selberg expansion has total
   size `O(sqrt(D))`; this includes its same-sign quadratic tangent saddles,
   but not the cubic caustics among nonzero dual modes;
2. the exact common-product slice `a*v=b*w` has
   `O(sqrt(D)*q^o(1))` solutions for fixed `S=a+b`.

The remaining term is now an explicit nonzero-dual three-index oscillatory
aggregate.  The nondegenerate termwise stationary-phase ledger is too large
by exactly `H=q/D=D^(17/16)`.  Opposite-sign frequencies also have cubic
caustics and require a separate uniform treatment.  No cancellation theorem
for the complete aggregate is supplied here, and no counterexample to the
pointwise bound was found.

## 1. Fixed-sum problem

Fix dyadic shell constants and assume

```text
a, b, v, w asymp q,       a+b=S asymp q,
|a*v-C|<=D,               |b*w-C|<=D,
q=D^(33/16).                                           (1.1)
```

Since `D=o(q)`, for each denominator there is at most one quotient.  On a
slightly enlarged fixed shell, (1.1) is majorized by

```text
||C/a|| <= delta,          ||C/(S-a)|| <= delta,
delta asymp D/q,           H=delta^(-1) asymp q/D.     (1.2)
```

Thus, with a smooth shell cutoff `W`, the pointwise count is bounded by

```text
R(S)=sum_a W(a)
       1_(||C/a||<=delta) 1_(||C/(S-a)||<=delta).      (1.3)
```

The replacement of the varying widths `D/a` and `D/(S-a)` by one larger
constant width changes only shell-dependent constants.

## 2. Exact Selberg expansion

Let `P_delta` be a nonnegative Selberg majorant for the interval
`[-delta,delta] mod 1`, of degree `H asymp delta^(-1)`.  It can be chosen with

```text
P_delta(theta)=sum_(|h|<=H) c_h e(h*theta),
c_0=2*delta+O(1/H),       |c_h|<<delta.               (2.1)
```

Consequently

```text
R(S) <= sum_(|h|,|k|<=H) c_h*c_k*T(h,k),              (2.2)

T(h,k)=sum_a W(a)
       e(C*(h/a+k/(S-a))).                             (2.3)
```

This is the scalar fixed-sum two-inverse formulation.  The zero-zero term is

```text
q*delta^2 = D^2/q = D^(-1/16).                        (2.4)
```

After Poisson summation in `a`, write

```text
T(h,k)=sum_(m in Z) I(h,k,m),                         (2.5)

I(h,k,m)=integral W(x)
 e(C*(h/x+k/(S-x))-m*x) dx.                           (2.6)
```

The saddle equation is

```text
C*(-h/x^2+k/(S-x)^2)=m.                               (2.7)
```

Equation (2.7), rather than two independent reciprocal sums, is the exact
frequency geometry.

## 3. The zero dual mode is exactly at square-root scale

For `m=0`, an interior saddle exists only when `h*k>0`.  For positive
frequencies it is

```text
x_0=S*sqrt(h)/(sqrt(h)+sqrt(k)),                      (3.1)
```

and

```text
Phi(x_0)=C*(sqrt(h)+sqrt(k))^2/S,

Phi''(x_0)
 =2*C*(sqrt(h)+sqrt(k))^4/(S^3*sqrt(h*k)).            (3.2)
```

Hence the stationary integral, with the harmless nonstationary remainder
included, satisfies

```text
|I(h,k,0)|
 <<1+sqrt(q)*(h*k)^(1/4)/(sqrt(h)+sqrt(k))^2.          (3.3)
```

Dyadic summation gives

```text
sum_(1<=h,k<=H)
 (h*k)^(1/4)/(sqrt(h)+sqrt(k))^2 << H^(3/2).          (3.4)
```

The negative-negative quadrant is its conjugate, and the opposite-sign
quadrants are nonstationary.  Therefore the entire `m=0` contribution to
(2.2) is

```text
<< delta^2*sqrt(q)*H^(3/2)+delta^2*H^2
 << sqrt(D)+1.                                        (3.5)
```

The exponent identity is exact:

```text
2*(-17/16)+(33/16)/2+(3/2)*(17/16)=1/2.              (3.6)
```

The one-zero-frequency terms have the same ceiling.  Standard
second-derivative/Poisson estimation gives

```text
|T(0,k)| << sqrt(q*k)+sqrt(q/k),                      (3.7)
```

so their sum with the Selberg coefficients is also `O(sqrt(D))`.

This proves that the `m=0` rational stationary phases do not themselves cause
a loss.  It does **not** estimate the nonzero Poisson modes, some of which can
be degenerate.

## 4. Exact surviving aggregate

For `h,k` of common size `K`, there are `O(K)` relevant nonzero dual
frequencies `m`, and a typical nondegenerate saddle has size
`O(sqrt(q/K))`.  The resulting nondegenerate absolute-summation ledger is

```text
delta^2*sqrt(q)*H^(5/2)=D^(25/16),                    (4.1)
```

whereas the target is `D^(1/2)`.  The gap is

```text
D^(25/16-1/2)=D^(17/16)=H.                            (4.2)
```

This is not yet a uniform proof for all nonzero saddles.  If `h` and `k` have
opposite signs, the equations

```text
C*(-h/x^2+k/(S-x)^2)=m,
2*C*(h/x^3+k/(S-x)^3)=0                              (4.3)
```

can hold simultaneously.  Such a saddle is cubic, with local size
`O((q^2/K)^(1/3))`, not `O(sqrt(q/K))`.  Allowing one cubic transition mode
for every opposite-sign pair gives the crude additional absolute ledger

```text
delta^2*q^(2/3)*H^(5/3)=D^(49/48).                    (4.4)
```

This is below `D^(25/16)`, but a uniform Airy decomposition has not been
written here, so the old phrase “the termwise ceiling is proved” would be too
strong.

There is a particularly transparent exact degeneracy.  If
`C=Q^2`, `S=2Q`, then

```text
(h,k,m,x)=(t,-t,-2t,Q)                                (4.5)
```

satisfies both equations in (4.3), and the phase is exactly

```text
2*t*Q-2*t*(x-Q)^3/(Q^2-(x-Q)^2).                      (4.6)
```

The actual even Selberg coefficients do **not** cancel this family:
`c_t*c_(-t)=|c_t|^2`.  Nevertheless it has only `H` members, and direct
Airy summation gives

```text
delta^2*q^(2/3)*sum_(t<=H)t^(-1/3)
 <<delta^2*q^(2/3)*H^(2/3)=D^(-1/24).                 (4.7)
```

Thus this coherent exact caustic is harmless by size, not by coefficient
symmetry.  The possible collective contribution of the full two-parameter
near-caustic set remains part of the open aggregate.

More generally, for `h>0`, `k=-l<0`, the cubic point and its caustic dual
frequency are

```text
x_c=S*h^(1/3)/(h^(1/3)+l^(1/3)),
m_c=-C*(h^(1/3)+l^(1/3))^3/S^2.                       (4.8)
```

Only an integer `m` within the narrow Airy transition width of `m_c`
contributes at cubic size.  Bounding how often that happens is an arithmetic
near-integer problem in `(h,l)`; treating every pair as caustic gives (4.4).

The precise sufficient input left by this reduction is

```text
| sum_(0<|h|,|k|<=H) c_h*c_k
    sum_(m!=0) I(h,k,m) |
       << sqrt(D)*q^o(1),                             (4.9)
```

uniformly in the physical `C,S` and shell cutoffs, for the actual Selberg
coefficients in (2.1).  A theorem uniform for arbitrary coefficients
`|beta_h|<<delta` would be stronger than needed.  Estimating the individual
`I(h,k,m)` and then summing cannot prove (4.9); in the nondegenerate bulk it
gives (4.1).

Equation (4.9) is a clean scalar version of the mask-sensitive
two-inverse large-sieve gate.  It is deliberately stated after removal of
the tangent mode, which has already been paid for in (3.5).

### 4.1 Summing the dual frequency first is an exact tautology

The actual Selberg coefficients permit one exact reassembly, but it does not
estimate the remainder.  Put

```text
F(x)=W(x)*P_delta(C/x)*P_delta(C/(S-x)).              (4.10)
```

Then, with the Fourier-transform convention in (2.6),

```text
sum_(h,k)c_h*c_k*I(h,k,m)=hat(F)(m),                  (4.11)
```

and Poisson summation gives

```text
sum_(m!=0) hat(F)(m)
 =sum_(a in Z)F(a)-integral F(x) dx.                  (4.12)
```

Thus “sum `m` first” returns the original lattice-versus-continuum
discrepancy.  It supplies no cancellation by itself.  Moreover `F` is
nonnegative for a genuine Selberg majorant, so a positivity argument cannot
discard its lattice spikes.  At `C=Q^2`, `S=2Q`, all integers
`a=Q+j`, `|j|<<sqrt(D)`, lie in the two reciprocal windows.  Any successful
bound for (4.12) must therefore recognize the same tangent packet already
visible in physical space.

A decoupled `TT*` or scalar large-sieve step has the analogous limitation.
Cauchy--Schwarz separates the two reciprocal windows and gives only the
one-strip count `O(D*q^o(1))`; it loses the required square root.  This is an
impossibility calculation for that decoupled implementation, not for a
genuinely coupled two-inverse large sieve.

## 5. A sharp theorem for the exact common-product slice

There is one useful arithmetic theorem beyond the spectral bookkeeping.

> **Lemma (fixed-sum common-product slice).**  Under the shell conditions
> in (1.1), the number of solutions with the additional constraint
> `a*v=b*w` is `O(sqrt(D)*q^o(1))`, uniformly in `C,S`.

### Proof

Put

```text
g=(a,b),       a=g*A,       b=g*B,       (A,B)=1,
A+B=T=S/g.                                                (5.1)
```

The equality `a*v=b*w` implies

```text
v=B*l,         w=A*l                                      (5.2)
```

for an integer `l`.  The shell conditions imply `l asymp g`, and the common
product is

```text
n=g*l*A*(T-A).                                            (5.3)
```

Fix `g|S`.  There are two complementary counts.

First fix `l`.  Completing the square in (5.3) shows that the preimage of an
interval of length `2D` contains

```text
O(1+sqrt(D/(g*l)))=O(1+sqrt(D)/g)                        (5.4)
```

integer values of `A`.  Since there are `O(g)` possible `l`, this gives

```text
N_g << g+sqrt(D).                                         (5.5)
```

For the second count, put `N=l*A*(T-A)`.  The condition
`|g*N-C|<=D` leaves only `O(1+D/g)` integer values of `N`.  For fixed `N`,
the factor `A*(T-A)` must divide `N`; divisor enumeration followed by the
quadratic equation for `A` gives only `q^o(1)` pairs `(l,A)`.  Hence

```text
N_g << (1+D/g)*q^o(1).                                   (5.6)
```

Use (5.5) when `g<=sqrt(D)` and (5.6) when `g>=sqrt(D)`.
This gives `N_g<<sqrt(D)*q^o(1)` for every `g`.  Finally, `g|S`, and the
number of divisors of `S` is `q^o(1)`.  The lemma follows.  `□`

This lemma controls a substantial resonant slice, but it is not an
identification of `a*v=b*w` with the Poisson mode `m=0`; the two statements
are separate sharp pieces.

## 6. Discriminant and factorization identities

Put

```text
n=a*v,       m=b*w,       x=a-b,
U=v+w,       y=w-v,       S=a+b.                         (6.1)
```

Then exactly

```text
S*U-x*y =2*(n+m),
x*U-S*y =2*(n-m),                                        (6.2)

(S^2-x^2)*(U^2-y^2)=16*n*m.                             (6.3)
```

Writing `sigma=2(n+m)`, `tau=2(n-m)`, and `M=S^2-x^2`, one obtains

```text
U=(S*sigma-x*tau)/M,
y=(x*sigma-S*tau)/M.                                    (6.4)
```

There is also the exact cross-factorization

```text
(S*v-n)*(S*w-m)=n*m,                                    (6.5)
```

because the two factors are `b*v` and `a*w`.  For fixed `(n,m)`, (6.5) gives
only `q^o(1)` possibilities, but summing it over the `O(D^2)` possible label
pairs loses far more than the target.  Equations (6.2)--(6.5) are therefore
exact parameterizations, not by themselves a proof of the full bound.

For a fixed quotient sum `U`, centered variables

```text
a=S/2+h,       b=S/2-h,
v=U/2+k,       w=U/2-k                                  (6.6)
```

give

```text
n-m=U*h+S*k,
(n+m)/2=S*U/4+h*k.                                      (6.7)
```

The first relation makes `k=-U*h/S+O(D/q)`.  More exactly, if
`n=C+e`, `m=C+f`, then

```text
| S*U/4-C-(U/S)*h^2 | <<D.                            (6.8)
```

Indeed the discarded term is `(e-f)*h/S=O(D)`.  Incrementing `U` by one
changes `S*U/4-C` by `S/4 asymp q`.  Designate the first integer `U` for
which the left centre can be nonnegative up to `O(D)` as the one
**exceptional** level.  Wherever its centre lies in the first interval of
length `asymp q`, it contributes at most `O(sqrt(D))` values of `h`.

Every earlier `U` is inadmissibly negative, and for every later `U` the
interval for `h^2` is centred at least `c*q` away from zero.  Consecutive
squares there are separated by
`>>sqrt(q)>D`, because `q=D^(33/16)>D^2`.  Hence every noncentral `U`
supports only `O(1)` solutions.

This sharpens the direct reduction:

```text
R(S) <<sqrt(D)+#{occupied noncentral quotient sums U}. (6.9)
```

The remaining pointwise theorem is therefore equivalent, up to `q^o(1)`,
to proving that only `O(sqrt(D)*q^o(1))` scattered `U`-levels are occupied.
Counting those levels independently restores the one-strip `D` ceiling.
This is the physical counterpart of the nonzero-dual aggregation in (4.9).

## 7. Tangent sharpness and finite audit

For fixed coprime positive `r,s`, take

```text
a_h=s*(Q+h),       b_h=s*(Q-h),
v_h=r*(Q-h),       w_h=r*(Q+h),
C=r*s*Q^2-D.                                             (7.1)
```

Then `a_h+b_h=2sQ` and

```text
a_h*v_h=b_h*w_h=r*s*(Q^2-h^2).                          (7.2)
```

All `|h|<=sqrt(2D/(r*s))` satisfy both product windows.  For `r=s=1`
this gives `asymp sqrt(D)` solutions, proving that the target scale is sharp.

An exact interval-sweep probe was also run on sampled fixed sums.  It
enumerated all shell variables for each sampled `S` and maximized over the
common window centre.  Representative `(q,D)` values

```text
(100,9), (200,13), (400,18), (800,26), (1200,31)
```

gave largest sampled total counts

```text
15, 15, 19, 23, 25,
```

and, after deleting `a*v=b*w`, largest sampled counts

```text
12, 14, 16, 18, 20.
```

These are constant multiples of `sqrt(D)`, not evidence for a proof.  The
maximizers visibly contain the quadratic packets (7.1), plus a few isolated
factorization points.  No power-sized counterexample was found.

## 8. Reproducibility and status

Exact identities and exponent arithmetic are recorded in
`src/qp_pair_sum_selberg_ledger.py`; tests are in
`src/test_qp_pair_sum_selberg_ledger.py`.

```text
fixed-sum Selberg/two-inverse expansion:              PROVED;
zero-zero and one-frequency terms <=sqrt(D):         PROVED;
zero-dual same-sign stationary aggregate <=sqrt(D):  PROVED;
common-product slice <=sqrt(D)*q^o(1):               PROVED;
nondegenerate termwise ledger D^(25/16):            EXACT CALCULATION;
pairwise Airy ledger D^(49/48):                     EXACT CALCULATION;
uniform decomposition of all nonzero saddles:       NOT WRITTEN;
required gain over nondegenerate ledger H=D^(17/16): EXACT;
sum-m-first identity (4.12):                       EXACT / TAUTOLOGICAL;
exceptional U level <=sqrt(D), later U levels O(1): PROVED;
occupied scattered U-level bound:                 OPEN;
nonzero-dual aggregate (4.9):                      OPEN;
full pointwise pair-sum bound:                       NOT PROVED;
power counterexample:                               NOT FOUND.
```
