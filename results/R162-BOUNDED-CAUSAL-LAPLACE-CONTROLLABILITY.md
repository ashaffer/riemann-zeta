# R162 bounded causal-Laplace controllability

## Status

The growing optional-prime route left open by R160 has a continuous model.
In the logarithmic prime coordinate `v=log(p/H)`, its leading cancellation
problem is to make

```text
1/lambda+integral_0^L a(v)exp(lambda v)dv                 (0.1)
```

small on a compact set of frequencies, using a real control with
`|a|<=1` and a horizon `L=O(log H)`.  At the high imaginary frequencies
arising from a nontrivial zeta zero, this problem is solvable with an
explicit **nonnegative** control.  No abstract density theorem or
ill-conditioned moment inversion is needed.

Let `K` be compact, put

```text
sigma=sup_(lambda in K) Re(lambda),
m_0=inf_(lambda in K)|lambda|,                             (0.2)
```

and suppose `m_0>0`.  If there is a real `alpha>0` such that

```text
alpha>sigma,
q=sup_(lambda in K)|alpha/(alpha-lambda)|<1,              (0.3)
```

then, for every `A>0` and all `H>=2`, there are a constant
`C=C(A,K,alpha)` and a real measurable `a_H:[0,C log H]->[0,1]` for which

```text
sup_(lambda in K)
 |1/lambda+integral_0^(C log H) a_H(v)exp(lambda v)dv|
 <=H^(-A).                                                 (0.4)
```

The construction is the truncated Poisson tail

```text
a_N(v)=exp(-alpha v)sum_(n=0)^N (alpha v)^n/n!.           (0.5)
```

Its infinite Laplace transform sums exactly to a geometric series.  Taking
`N asymp_A log H` gives the requested accuracy, and truncating (0.5) at
`L=cN` costs only another exponentially small error.

For `lambda=delta-i gamma` with `delta>0`, the contraction part of (0.3)
is equivalent to

```text
2 alpha delta<delta^2+gamma^2.                            (0.6)
```

Together with `alpha>delta`, it is therefore extremely nonrestrictive at
nontrivial-zero height.  The
same construction handles a small compact neighborhood and its conjugate
simultaneously.

```text
fractional causal-Laplace control                           EXPLICIT
real control                                               YES
nonnegative control                                        YES
uniform error exp(-cN)                                     THEOREM
horizon for error H^(-A)                                   O_A(log H)
outer optional-prime cutoff                                H^(1+O_A(1))
continuous dual/causality obstruction                      NONE HERE
rounding to one sign at each actual prime                  OPEN
exact prime-sum rather than continuum cancellation         OPEN
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md`](R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md)
and
[`R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md`](R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md).

## 1. The exact infinite-horizon identity

Fix `alpha>0` and an integer `N>=0`.  Define (0.5) for `v>=0`.
Since the partial exponential series is positive and bounded by the full
series,

```text
0<a_N(v)<=1.                                               (1.1)
```

If `Re(lambda)<alpha`, termwise integration is legitimate and gives

```text
integral_0^infinity a_N(v)exp(lambda v)dv
 =sum_(n=0)^N alpha^n/(alpha-lambda)^(n+1).               (1.2)
```

Put

```text
r(lambda)=alpha/(alpha-lambda).                            (1.3)
```

The finite geometric sum in (1.2) is

```text
sum_(n=0)^N alpha^n/(alpha-lambda)^(n+1)
 =-1/lambda [1-r(lambda)^(N+1)].                          (1.4)
```

Consequently

```text
1/lambda+integral_0^infinity a_N(v)exp(lambda v)dv
 =r(lambda)^(N+1)/lambda.                                 (1.5)
```

Under (0.3), (1.5) is bounded uniformly on `K` by

```text
m_0^(-1)q^(N+1).                                          (1.6)
```

This proves exponential controllability on the infinite half-line.  The
sign in (1.4) is important: although `a_N` is nonnegative, the high
imaginary oscillation of `exp(lambda v)` makes its transform converge to
`-1/lambda`.

## 2. Exponentially cheap truncation

Set

```text
beta=alpha-sigma>0.                                       (2.1)
```

Choose a constant `c>0` such that

```text
c>=max{1/alpha,2/beta},
tau=beta c-log(e alpha c)-1>0.                            (2.2)
```

Such a `c` exists because the linear term `beta c` eventually dominates
`log c`.  For `N>=1`, put `L=cN`.  If `v>=L`, then
`alpha v>=N`, so the terms in the partial exponential series increase up to
the last one.  The elementary Stirling bound `N!>=(N/e)^N` gives

```text
a_N(v)
 <=(N+1)(alpha v)^N exp(-alpha v)/N!
 <=(N+1)(e alpha v/N)^N exp(-alpha v).                    (2.3)
```

Uniformly for `lambda in K`, the transform of the deleted tail is therefore
at most

```text
(N+1)(e alpha/N)^N integral_L^infinity v^N exp(-beta v)dv.
                                                                    (2.4)
```

For `v=L+u`,

```text
(v/L)^N<=(exp(u/L))^N=exp(u/c)<=exp(beta u/2),             (2.5)
```

where (2.2) was used in the last inequality.  It follows that

```text
integral_L^infinity v^N exp(-beta v)dv
 <=2 beta^(-1)L^N exp(-beta L).                           (2.6)
```

Combining (2.4)--(2.6), and using `N+1<=exp(N)`, yields

```text
sup_(lambda in K)
 |integral_L^infinity a_N(v)exp(lambda v)dv|
 <=2 beta^(-1)exp(-tau N).                                (2.7)
```

Thus finite horizon changes the exact identity by only `O(exp(-tau N))`.

## 3. Power accuracy in logarithmic horizon

Let

```text
eta=min{-log q,tau}>0,
C_0=m_0^(-1)+2 beta^(-1).                                 (3.1)
```

Equations (1.6) and (2.7) imply

```text
sup_(lambda in K)
 |1/lambda+integral_0^(cN) a_N(v)exp(lambda v)dv|
 <=C_0 exp(-eta N).                                       (3.2)
```

For a prescribed `A>0`, take

```text
N_H=ceil([A log H+log^+ C_0]/eta).                        (3.3)
```

Then (3.2) is at most `H^(-A)`.  Moreover,

```text
cN_H<=C(A,K,alpha)log H,                 H>=2,            (3.4)
```

after increasing the constant to absorb the ceiling.  Extend `a_(N_H)` by
zero from `cN_H` to the right side of (3.4).  This proves (0.4).

The dependence is explicit.  Up to the harmless ceiling term, one may take

```text
C(A,K,alpha)=c A/eta+O_(K,alpha)(1).                      (3.5)
```

Thus every additional requested power of `H` costs only a fixed additional
multiple of `log H` in control horizon.

## 4. Geometry of the admissible frequency set

For `alpha>0`,

```text
|alpha/(alpha-lambda)|<1

iff

2 alpha Re(lambda)<|lambda|^2.                            (4.1)
```

If `Re(lambda)>0` throughout `K`, an admissible `alpha` exists whenever

```text
sup_K Re(lambda)
 <inf_(lambda in K) |lambda|^2/[2 Re(lambda)].            (4.2)
```

Any `alpha` strictly between the two sides satisfies (0.3).  Frequencies
with nonpositive real part impose no upper restriction in (4.1), although
`alpha>sigma` is still needed for the uniform tail integral.

For a concrete high-frequency disc, suppose

```text
K subset {lambda:|lambda-(delta-i gamma)|<=rho}
          union
          {lambda:|lambda-(delta+i gamma)|<=rho},         (4.3)
```

where `delta>rho>0` and `|gamma|>rho`.  It is enough to choose

```text
delta+rho<alpha
 <(|gamma|-rho)^2/[2(delta+rho)].                         (4.4)
```

In particular such an interval exists if

```text
(|gamma|-rho)^2>2(delta+rho)^2.                           (4.5)
```

The first nontrivial zeta-zero height is already much larger than every
possible `delta=1-Re(rho_zeta)` in the critical strip.  Hence (4.5) has an
enormous margin on the target microdiscs used in R153--R161.  Because the
control is real, conjugation in (4.3) is automatic.

## 5. Meaning for the optional-prime route

The prime number theorem suggests, at leading order and with
`lambda=1-s`,

```text
sum_(p<=H) p^(-s)
       ~H^lambda/[lambda log H],

sum_(H<p<=H exp L) a(log(p/H))p^(-s)
       ~H^lambda/log H integral_0^L a(v)exp(lambda v)dv.  (5.1)
```

Theorem (0.4) therefore gives an explicit continuum profile which cancels
the mandatory head to arbitrary fixed power.  Since `L=O_A(log H)`, its
outer endpoint is only

```text
Y=H exp L=H^(1+O_A(1)).                                   (5.2)
```

This is the favorable polynomial-cutoff regime anticipated after R160.  It
also shows that no separation functional, causality principle, or bounded-
amplitude obstruction can close the optional-prime route at the continuum
level.  The control need not exploit negative fractional amplitudes.

Equation (5.1) is not an arithmetic theorem at the accuracy required by the
strip program.  Replacing the exact prime sum by its PNT density leaves a
relative error far larger than `H^(-A)`.  In addition, (0.5) assigns a
fractional amplitude to every logarithmic location, whereas (8.1) of R160
allows one discrete sign at each actual prime.  A valid continuation must
prove a quantitative rounding theorem of the following kind:

```text
fractional Poisson profile
       -> one allowed local exponent at each H<p<=H^(1+C)
       -> uniform analytic error H^(-A) on K,             (5.3)
```

while retaining the exact Euler factors and controlling the higher prime-
power terms.  Ordinary PNT substitution does not prove (5.3).

The continuous problem is therefore decided affirmatively, but the exact
prime-discrepancy problem is now the sharp arithmetic gate.  R162 by itself
proves neither a fixed zero-free strip nor zeros approaching `Re(s)=1`.
