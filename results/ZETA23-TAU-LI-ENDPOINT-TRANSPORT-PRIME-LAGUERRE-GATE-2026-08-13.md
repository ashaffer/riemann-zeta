# The exact Freitas tau-Li target below 2

## Endpoint transport, zero-pair margins, and the prime-Laguerre gate

**Date:** 2026-08-13  
**Target:** prove

```text
alpha_m(1.999998)>=0 for every m>=1.                 (0.1)
```

**Binary verdict:** **not proved.**  The endpoint analysis does produce a
new exact consolidation.  All coefficients at `tau=2` are positive term by
term after conjugate-zero pairing, but transport to `tau<2` is an infinite
alternating binomial transform, not a positive perturbation.  A
functional-equation-symmetric quartet gives an exact countermodel to any
propagation theorem based only on endpoint positivity, reality, symmetry,
order, and the Freitas differential chain.  The only possible escape for
zeta is a new inequality using its exact prime/archimedean cancellation;
the Laguerre generating function shows that this cancellation recomposes
precisely into the original zero-free problem.

No zero-free region is improved in this report.

---

## 1. Definitions and the exact generating germ

Put

```text
L(s)=xi'(s)/xi(s)
```

and, for `tau>0`, define Freitas's coefficients by

```text
alpha_m(tau)
 =1/(m-1)! [d^m/ds^m {s^(m-1)log xi(s)}]_(s=tau).
                                                               (1.1)
```

Define their ordinary generating germ

```text
A_tau(t)=sum_(m>=1)alpha_m(tau)t^(m-1).             (1.2)
```

### Theorem 1.1 (exact generating function)

As an analytic germ at `t=0`,

```text
A_tau(t)=(1-t)^(-2)L(tau/(1-t)).                    (1.3)
```

#### Proof

Let `s=tau/(1-t)`.  Expanding the right side at zero and applying the
chain rule gives

```text
[t^(m-1)] (1-t)^(-2)L(tau/(1-t))
 =1/(m-1)! [d^m/ds^m {s^(m-1)log xi(s)}]_(s=tau).
```

Equivalently, this is Freitas's identification of `alpha_m` with the
Taylor coefficients of the logarithmic derivative of
`xi(1/(1-z))`.  QED.

The first two coefficients provide a direct check:

```text
alpha_1(tau)=L(tau),
alpha_2(tau)=2L(tau)+tau L'(tau).                   (1.4)
```

### Corollary 1.2 (transport between any two endpoints)

For positive `sigma,tau`, with the right side interpreted by analytic
continuation to a neighborhood of `1-sigma/tau`, wherever both sides are
regular,

```text
A_tau(t)=sigma^2/tau^2
 A_sigma(1-sigma/tau+(sigma/tau)t).                 (1.5)
```

Indeed, both sides evaluate `L` at `tau/(1-t)`.

For the only specialization used below, `sigma=2` and `1<tau<2`, the base
point `1-2/tau` lies in `(-1,0)`, inside the radius-one endpoint disk.  Thus
the endpoint transform (2.2)--(2.4) does not continue across a singularity.

This identity solves the entire Freitas differential hierarchy at once.
It is also the precise reason that continuity of each fixed coefficient at
`tau=2` does not provide a degree-uniform interval.

---

## 2. Exact endpoint-to-interior transform

Write

```text
tau=2/(1+h),       h=2/tau-1.                       (2.1)
```

Thus `tau<2` corresponds to `h>0`.  Equation (1.5) becomes

```text
A_tau(t)=(1+h)^2 A_2(-h+(1+h)t).                   (2.2)
```

Taking the coefficient of `t^(m-1)` gives two equivalent exact formulas.

### Theorem 2.1 (endpoint transport)

For every `m>=1`,

```text
alpha_m(2/(1+h))
 =(1+h)^(m+1) A_2^(m-1)(-h)/(m-1)!                 (2.3)

 =(1+h)^(m+1)
   sum_(j>=0)(-h)^j binom(m+j-1,j)alpha_(m+j)(2).  (2.4)
```

The series in (2.4) is absolutely convergent for `0<=h<1` before its
alternating signs are applied.  This follows from the radius-one endpoint
germ and the fact that `h<1`.

For the requested strip, put

```text
epsilon=10^(-6),
tau_*=2(1-epsilon)=1.999998,
h_*=epsilon/(1-epsilon)=0.000001000001000001....    (2.5)
```

Then (0.1) is exactly

```text
A_2^(k)(-h_*)>=0 for every k>=0,                    (2.6)
```

or equivalently the positivity of every alternating sum in (2.4).  Thus
the desired theorem is **absolute monotonicity of the endpoint generating
function at one fixed point immediately to the left of zero**.  Ordinary
coefficient positivity says only that the derivatives at zero are positive.

### Conditioning of the endpoint transform

The bare binomial kernel in (2.4) satisfies

```text
sum_(j>=0) h^j binom(m+j-1,j)=(1-h)^(-m),
sum_(j>=0)(-h)^j binom(m+j-1,j)=(1+h)^(-m).         (2.7)
```

Consequently the unsigned-to-signed ratio for constant endpoint data is

```text
K_m(h)=((1+h)/(1-h))^m=exp(2hm+O(h^3 m)).           (2.8)
```

At the target, the transform is already nonperturbative when `m` is much
larger than `10^6`.  Formula (2.8) is not a lower bound on the difficulty of
every possible proof, but it proves that coefficientwise continuity or
coarse upper/lower estimates at `tau=2` cannot be propagated uniformly by
an absolute-value argument.

---

## 3. What is quantitatively true at the safe endpoint

Freitas's zero formula is

```text
alpha_m(tau)
 =1/tau sum_rho [1-(rho/(rho-tau))^m],              (3.1)
```

with a symmetric limiting convention.  At `tau=2`, set

```text
q_rho=rho/(rho-2)=r_rho exp(i theta_rho).           (3.2)
```

For a zero `rho=beta+i gamma`,

```text
r_rho^2
 =[beta^2+gamma^2]/[(2-beta)^2+gamma^2]
 =1-4(1-beta)/[(2-beta)^2+gamma^2] <1.              (3.3)
```

The strict inequality uses the classical fact that nontrivial zeta zeros
have `beta<1`.

Pairing `rho` with its conjugate makes (3.1) an absolutely convergent sum
of strictly positive terms:

```text
alpha_m(2)
 =sum_(Im rho>0)[1-Re(q_rho^m)]
 =sum_(Im rho>0)[1-r_rho^m cos(m theta_rho)] >0.    (3.4)
```

For fixed `m`, a paired summand is `O_m(gamma^(-2))`, so (3.4) converges.
It also yields, upon selecting any one nontrivial zero `rho_0`, the uniform
but small lower bound

```text
alpha_m(2)>=1-|q_(rho_0)|^m>=1-|q_(rho_0)|>0.       (3.5)
```

This is genuine endpoint positivity, not merely the abstract Freitas
criterion.

For example,

```text
alpha_1(2)
 =3/2-(EulerGamma+log pi)/2+zeta'(2)/zeta(2)
 =0.0690... .                                      (3.6)
```

### Endpoint average size

Stirling's formula gives, as real `s` tends to infinity,

```text
L(s)=1/2 log(s/(2pi))+3/(2s)+O(s^(-2)).             (3.7)
```

Hence, as `t` increases to one,

```text
A_2(t)
 =1/[2(1-t)^2] log(1/[pi(1-t)])
   +3/[4(1-t)]+O(1).                               (3.8)
```

Since all coefficients in (1.2) are nonnegative at `tau=2`, the power-series
Karamata theorem applies and gives

```text
sum_(m<=M)alpha_m(2) ~ (1/4)M^2 log M.              (3.9)
```

Thus `alpha_m(2)` has average scale `m log m`, and positivity also gives the
individual upper bound `alpha_m(2)=O(m^2 log m)`.  Equation (3.9) is
deliberately only an average statement; it gives no pointwise lower bound of
order `m log m`, and it does not control the alternating tail (2.4).

---

## 4. The differential chain has the wrong one-sided direction

Freitas's exact differential chain is

```text
(tau/m)alpha_m'(tau)+(m+1)/m alpha_m(tau)
 =alpha_(m+1)(tau),                                (4.1)
```

or

```text
[tau^(m+1)alpha_m(tau)]'
 =m tau^m alpha_(m+1)(tau).                         (4.2)
```

In particular,

```text
alpha_m'(2)
 =m/2 alpha_(m+1)(2)-(m+1)/2 alpha_m(2).            (4.3)
```

Endpoint positivity alone gives no sign for (4.3).  If all
`alpha_(m+1)(u)` were already known positive on `[tau,2]`, integrating (4.2)
would give

```text
tau^(m+1)alpha_m(tau)
 =2^(m+1)alpha_m(2)
  -m integral_tau^2 u^m alpha_(m+1)(u)du.           (4.4)
```

The known-positive integral is subtracted, so (4.4) is an upper bound, not
a lower bound.  Descending induction would have to start at infinite degree.
Formula (2.4) is the closed-form expression of that infinite backward
hierarchy.

Any useful propagation theorem would therefore need a new adjacent-degree
inequality with the correct relative size, uniformly in `m`; for example, a
bound on the integral in (4.4) strictly below the endpoint term.  Such a
bound is not supplied by (3.5), (3.9), or the differential system itself.

---

## 5. The exact zero-pair margin and where it changes sign

For general real `tau>0`, define

```text
q_tau(rho)=rho/(rho-tau).
```

Then

```text
|q_tau(rho)|^2
 =1+2tau(beta-tau/2)/[(beta-tau)^2+gamma^2].        (5.1)
```

Consequently

```text
|q_tau(rho)| <=1    iff    beta<=tau/2.             (5.2)
```

At the endpoint, the positive modulus margin is exactly

```text
1-|q_2(rho)|^2
 =4(1-beta)/[(2-beta)^2+gamma^2].                   (5.3)
```

It has no zero-independent positive lower bound.  It tends to zero with
height even for critical-line zeros, and a hypothetical sequence with
`beta` tending to one makes its numerator tend to zero as well.  Lowering
`tau` crosses the unit circle precisely for the zeros that the desired strip
must exclude.

This proves the exact truth boundary of every pairwise-continuity argument:

> A uniform endpoint modulus margin is already a uniform zero-free strip.

Phase does not repair the loss.  If `|q_tau(rho)|>1`, then along infinitely
many integers `m` the phase `m arg q_tau(rho)` lies in a fixed neighborhood
of a multiple of `2pi`, and the conjugate-pair contribution becomes
exponentially negative.

---

## 6. Exact symmetric countermodel to soft endpoint propagation

The preceding obstruction can be realized by the smallest possible
functional-equation-symmetric divisor.

### Theorem 6.1 (endpoint positivity has no symmetry-forced window)

Fix any `1<tau_0<2`.  Choose

```text
0<eta<(2-tau_0)/2,       a=1/2-eta,       T>a,
```

and define

```text
P_(eta,T)(s)
 =[((s-1/2)-iT)^2-a^2]
  [((s-1/2)+iT)^2-a^2].                             (6.1)
```

Then:

1. `P_(eta,T)` is real on the real axis and satisfies
   `P_(eta,T)(1-s)=P_(eta,T)(s)`;
2. its zeros are `eta+-iT` and `1-eta+-iT`;
3. the Freitas coefficients defined from `log P_(eta,T)` satisfy
   `alpha_m^P(2)>0` for every `m>=1`;
4. `alpha_m^P(tau_0)<0` for infinitely many `m`.

#### Proof

The first two assertions follow directly from (6.1).  At `tau=2`, every
zero has real part below one, so its conjugate-pair contribution is positive
by (3.3)--(3.4).

At `tau=tau_0`, the pair with real part `1-eta` has

```text
r_R=|q_(tau_0)(1-eta+iT)|>1,                        (6.2)
```

while the reflected pair at real part `eta` has modulus `r_L<1`.  The four
zeros contribute

```text
alpha_m^P(tau_0)
 =2/tau_0 [2-r_R^m cos(m theta_R)
             -r_L^m cos(m theta_L)].                (6.3)
```

For every real `theta_R`, infinitely many positive integers `m` satisfy
`cos(m theta_R)>=1/2` (periodicity in the rational case and density modulo
`2pi` in the irrational case).  Along that subsequence,

```text
alpha_m^P(tau_0)
 <=2/tau_0 [3-r_R^m/2],                             (6.4)
```

which is negative for all sufficiently large selected `m`.  QED.

The countermodel obeys the same differential chain (4.1) and the same
transport identity (2.2), since those are algebraic consequences of the
definition (1.1).  If matching order one is desired, multiply (6.1) by

```text
cosh(c(s-1/2)),       c>0.                           (6.5)
```

This adds only critical-line zeros and preserves reality and the functional
equation.  Their coefficients at `tau_0>1` are nonnegative and have
subexponential growth, so the `r_R^m` term still dominates along the selected
subsequence.  Concretely, the symmetric canonical product

```text
cosh(cw)=product_(k>=0)
 [1+4c^2 w^2/((2k+1)^2 pi^2)]
```

has no hidden exponential Hadamard factor.  Its zeros have real part `1/2`,
and its transported generating germ is analytic in `|t|<1` for `tau_0>1`.
Cauchy's estimate therefore gives `O_epsilon((1+epsilon)^m)` for every
`epsilon>0`, which is enough for the comparison with `r_R^m`.

Theorem 6.1 is not a counterexample with zeta's Euler product.  Its exact
scope is that **endpoint positivity, functional-equation symmetry, reality,
entire-function order, and the Freitas differential chain do not propagate
positivity below 2**.  Any successful proof must use arithmetic information
that excludes the exterior pair.

### Corollary 6.2 (finite endpoint data are blind to a remote offender)

Fix `1<tau_0<2`, a degree cutoff `M`, and an error tolerance `epsilon>0`.
The height `T` in Theorem 6.1 can be chosen so large that

```text
0<alpha_m^P(2)<epsilon,          1<=m<=M,           (6.6)
```

while `alpha_m^P(tau_0)<0` still holds for infinitely many larger `m`.

Indeed, for fixed `m`,

```text
q_2(rho)=1+2/(rho-2)=1+O(1/T),
1-Re(q_2(rho)^m)=O_m(T^(-2))                       (6.7)
```

after conjugate pairing.  There are only four zeros, so all of the first
`M` endpoint coefficients tend to zero.  At `tau_0`, however, (6.2) remains
strict for every finite `T`, and its exponential power eventually wins.

Thus no finite verification at `tau=2`, even with arbitrarily accurate
values and all the soft symmetries imposed, supplies a fixed interval below
two.  The failure can be postponed to arbitrarily high coefficient degree.
If order one is included among the imposed data, first choose `T` as above
and then multiply by the factor (6.5) with `c>0` sufficiently small.  For
each fixed `m` its contribution to `alpha_m(2)` tends to zero with `c`, so
the first `M` inequalities in (6.6) persist after splitting the tolerance,
whereas its subexponential coefficients still cannot cancel the quartet's
`r_R^m` subsequence.

---

## 7. The actual-prime Laguerre ledger

For `tau>1`, the Euler series is absolutely convergent and gives

```text
alpha_(n+1)(tau)
 =G_(n+1)(tau)
  -sum_(q>=2)Lambda(q)q^(-tau)L_n^(1)(tau log q),   (7.1)
```

where `q` ranges over the positive integers (the nonzero atoms are prime
powers), `G_(n+1)` is the explicit contribution of

```text
(1/2)s(s-1)pi^(-s/2)Gamma(s/2),
```

and

```text
1/n! d^(n+1)/ds^(n+1)[s^n exp(-Ls)]
 =-L exp(-Ls)L_n^(1)(Ls).                           (7.2)
```

The Laguerre generating identity is

```text
sum_(n>=0)L_n^(1)(x)t^n
 =(1-t)^(-2)exp(-xt/(1-t)).                         (7.3)
```

Summing the prime part of (7.1) over degree therefore gives exactly

```text
-sum_q Lambda(q)q^(-tau)
 sum_(n>=0)L_n^(1)(tau log q)t^n

 =(1-t)^(-2) zeta'/zeta(tau/(1-t)).                 (7.4)
```

Thus the signed Laguerre blocks do not create a second independent object;
they reassemble into the prime part of (1.3).

### 7.1 Why the standard degree-uniform absolute envelope stops at the endpoint

The standard uniform bound, valid for `x>=0`,

```text
exp(-x/2)|L_n^(1)(x)|<=n+1                         (7.5)
```

would majorize the prime sum by

```text
(n+1)sum_q Lambda(q)q^(-tau/2),                    (7.6)
```

which diverges for every `tau<=2`.  Fixed-degree polynomial bounds converge
for every `tau>1`; in particular, the actual absolute prime sum in (7.1) is
finite for each fixed `n` even when `tau<=2`.  Thus (7.6) does **not** prove
divergence of that fixed-degree sum.  It proves only that the standard
uniform envelope (7.5) is unusable at and below two.  Naively expanding the
fixed-degree Laguerre polynomial also gives bounds whose `n`-dependence does
not establish (0.1).  A more coefficient-specific signed or absolute
estimate is not ruled out by this calculation; it would have to improve
substantially on (7.5).

### 7.2 The pole cancellation is itself nonuniform

The logarithmic derivative is

```text
L(s)=1/s+1/(s-1)-1/2 log pi
     +1/2 psi(s/2)+zeta'/zeta(s).                   (7.7)
```

The separate transformed term `1/(s-1)` has a singularity at

```text
t=1-tau.                                            (7.8)
```

For `tau<2`, this lies strictly inside the unit disk.  It is canceled
exactly by the pole `-1/(s-1)` of `zeta'/zeta(s)`.  Separating the
analytically continued prime and pole ledgers therefore creates
exponentially large alternating coefficient pieces of scale
`(tau-1)^(-n+O(1))` which must cancel before positivity can even be asked.
This statement concerns their degree-generating germs and is compatible
with the fixed-degree absolute convergence noted in Section 7.1.

After combining them as

```text
1/(s-1)+zeta'/zeta(s)
 =d/ds log[(s-1)zeta(s)],                           (7.9)
```

the artificial pole disappears.  The remaining singularities are precisely
the nontrivial and trivial zeros.  In the completed combination (7.7), the
trivial-zero/gamma singularities cancel as well, leaving exactly the
nontrivial-zero geometry encoded by (5.1).

This is the sharp arithmetic obstruction: the cancellation needed to turn
(7.1) into a positive coefficient is not controlled by positivity of the
Mangoldt atoms.  Once all forced pole/gamma cancellations are performed, a
degree-uniform interval below two is equivalent to excluding the offending
nontrivial singularities.

---

## 8. What would close the target

The endpoint formulation isolates three equivalent new inputs.  Any one of
the following would prove the requested strip:

1. **Endpoint absolute monotonicity**

   ```text
   A_2^(k)(-h_*)>=0 for every k>=0.                 (8.1)
   ```

2. **Alternating endpoint inequalities**

   ```text
   sum_(j>=0)(-h_*)^j binom(m+j-1,j)alpha_(m+j)(2)
   >=0 for every m>=1.                              (8.2)
   ```

3. **Actual-prime Laguerre domination**

   ```text
   sum_q Lambda(q)q^(-tau_*)
          L_(m-1)^(1)(tau_* log q)
   <=G_m(tau_*) for every m>=1.                     (8.3)
   ```

They are exact rewritings of the same statement, not three independent
sources of slack.  The pair margin (5.3), the transport condition number
(2.8), and the countermodel in Theorem 6.1 show what any proof of one of them
must overcome.

The highest-value surviving subproblem is a coefficient-specific estimate
for the combined analytic function

```text
d/ds log[(s-1)zeta(s)]                              (8.4)
```

after the exact pole cancellation, strong enough to retain the signs of all
translated derivatives in (2.6).  Bounding the prime series absolutely,
using endpoint continuity coefficient by coefficient, or using the
differential chain without a new adjacent-degree inequality cannot close the
uniform quantifier.

---

## 9. Final truth table

```text
alpha_m(2)>0 termwise after conjugate pairing       PROVED
endpoint partial-sum asymptotic (1/4)M^2 log M      PROVED
exact endpoint-to-interior binomial transport       PROVED
target equals A_2 absolute monotonicity at -h_*     PROVED
endpoint positivity alone propagates below 2       FALSE (Theorem 6.1)
differential chain gives a one-sided lower bound    FALSE
standard envelope (7.5) closes at tau_*             FALSE (majorant diverges)
actual-prime signed cancellation (8.3)              NOT PROVED
alpha_m(1.999998)>=0 for every m                    NOT PROVED
fixed zero-free strip                               NOT PROVED
```

## References

1. P. Freitas, *A Li-type criterion for zero-free half-planes of Riemann's
   zeta function*, J. London Math. Soc. 73 (2006), 399--414,
   https://arxiv.org/abs/math/0507368.
2. The endpoint and prime-Laguerre formulas are derived directly above from
   Freitas's definition, the completed zeta factorization, and the classical
   Laguerre generating function.
