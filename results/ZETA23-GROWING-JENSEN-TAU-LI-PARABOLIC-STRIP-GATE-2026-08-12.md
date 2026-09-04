# Growing Jensen, Pólya-frequency, and tau-Li gates for a fixed strip

Status: no fixed zero-free strip is proved.  There are, however, two exact
coefficient formulations of the fixed-strip problem which are sharper than
asking for RH.  Squaring the centered xi variable turns a horizontal strip
into a parabola and shows that only the **base row** of the Jensen array can
locate the zeros of xi.  The best currently known simultaneous
degree--shift hyperbolicity wedge lies wholly in derivative rows and cannot be
integrated back without recovering one missing coefficient at every step.
Freitas's `tau`-Li coefficients give an exact criterion at the exterior point
`tau=1+2a`; for `a=0.499999` this point is `tau=1.999998`, where the Euler
series is absolutely convergent.  Its exact prime kernel is nevertheless an
oscillatory Laguerre polynomial, and the standard degree-uniform absolute
bound reaches its abscissa wall exactly at `tau=2`.

Date: 2026-08-12.

## 1. Square the centered variable: a strip is exactly a parabola

Write

```text
Y(w)=xi(1/2+w).
```

The functional equation makes `Y` even, so there is a unique entire function
`F` such that

```text
Y(w)=F(w^2),
F(z)=sum_(n>=0) gamma_n z^n/n!.                     (1.1)
```

In the Rodgers--Tao normalization from the theta reports,

```text
Y(w)=8 integral_0^infinity Phi(u)cosh(2wu)du,
gamma_n=8*4^n*n!/(2n)! * integral_0^infinity Phi(u)u^(2n)du.   (1.2)
```

In particular, every `gamma_n` is strictly positive.  If

```text
rho=1/2+w,       z=w^2,
```

then the elementary identity

```text
|z|+Re(z)=2(Re(w))^2                              (1.3)
```

gives the exact strip geometry.

### Theorem 1.1 (parabolic strip identity)

For `a>0`, all nontrivial zeta zeros obey

```text
|Re(rho)-1/2|<=a                                  (1.4)
```

if and only if every zero `z` of `F` belongs to

```text
P_a={z: |z|+Re(z)<=2a^2}
    ={X+iY: Y^2<=4a^2(a^2-X)}.                    (1.5)
```

At the degenerate endpoint `a=0`, the first description remains exact and is
`P_0=(-infinity,0]`; the quadratic inequality in the second description says
only `Y=0` and must additionally be supplemented by `X<=0`.

Thus a fixed horizontal strip is not a fixed angular sector for the squared
function.  At radius `R`, the allowed angular deviation from the negative
axis is only

```text
2 arcsin(a/sqrt(R)) = 2a/sqrt(R)+O_a(R^(-3/2)).   (1.6)
```

This shrinking angle is the key uniformity cost missed by fixed-degree
Jensen limits.

## 2. Which Jensen polynomials actually see the original zeros

Use the standard xi Jensen array

```text
J^(d,n)(X)=sum_(j=0)^d binom(d,j)gamma_(n+j)X^j.   (2.1)
```

For fixed `n`, put

```text
P_(d,n)(z)=J^(d,n)(z/d).
```

Since

```text
binom(d,j)(z/d)^j
 =[(d)_j/d^j] z^j/j!,
0<=(d)_j/d^j<=1,
```

the entire series in (1.1) gives, locally uniformly on the plane,

```text
P_(d,n)(z) -> F^(n)(z).                            (2.2)
```

### Theorem 2.1 (base-row parabolic Jensen criterion)

The set of bounded accumulation points of zeros of `P_(d,0)` as `d->infinity`
is exactly the zero set of `F`, with the usual local multiplicities.  Hence
(1.4) is equivalent to

```text
every bounded root accumulation z of J^(d,0)(z/d)
satisfies |z|+Re(z)<=2a^2.                         (2.3)
```

#### Proof

Local uniform convergence and Rouche show that every zero of `F` attracts the
correct number of roots of `P_(d,0)`.  Conversely, if roots `z_d` remain
bounded and converge to `z_*`, then uniform convergence near `z_*` gives
`F(z_*)=0`.  Equation (1.3) finishes the proof.  QED.

The shift index matters decisively: `P_(d,n)` for `n>0` converges to
`F^(n)`, not to `F`.  Eventual hyperbolicity deep in the derivative rows can
therefore coexist with nonreal zeros of the original function.

## 3. The unavoidable degree--height budget

There is a simple information-theoretic lower bound before any coefficient
estimate is attempted.  Suppose a degree-`d` polynomial `Q_d` approximates
`F` with Rouche accuracy on `|z|=R`, where the circle contains no zero of
`F`.  Then

```text
d >= N_F(R),                                       (3.1)
```

where `N_F(R)` counts the zeros of `F` in the disk.  The square map and the
Riemann--von Mangoldt formula give

```text
N_F(T^2)
 =T/(2*pi) log(T/(2*pi))-T/(2*pi)+O(log T).         (3.2)
```

Consequently any disk-wide polynomial certificate reaching zeta height `T`
needs at least

```text
d >=T/(2*pi) log(T/(2*pi))-T/(2*pi)+O(log T)
  =(1/(2*pi)+o(1))*T log T.                        (3.3)
```

This lower bound applies to a growing-domain use of the base Jensen
polynomials as well as to Taylor polynomials.  It is not a lower bound for a
purely local approximation around one preselected zero.

Jenkins--McLaughlin's growing Taylor-polynomial analysis reaches the same
information scale: for Taylor degree `2m` (up to their harmless index shift),
their saddle scale is

```text
lambda_m=4m/W(2m/pi)*(1+O(1/m)),                   (3.4)
```

and their error majorant is uniformly small on `|w|<lambda_m/e`.  Their
proved Hurwitz-zero theorem is stated for each fixed zero; uniform capture of
zeros growing with `lambda_m` requires the additional multiplicity and
derivative control listed in their Remark 5.2.  Thus `m/log m` is the natural
growing scale of the analysis, not an unconditional disk-wide zero-capture
theorem.  Fixed off-line zeros would be copied just as faithfully as fixed
critical-line zeros.

## 4. Finite Pólya-frequency order becomes quadratic in height

Let

```text
Q_d(X)=J^(d,0)(X)=sum_(j=0)^d b_j X^j,
b_j=binom(d,j)gamma_j.                              (4.1)
```

Say that `(b_j)` is `PF_k` when all minors of order at most `k` of its
Toeplitz matrix are nonnegative.  Schoenberg's sharp sector theorem says
that a degree-`d` `PF_k` polynomial has no zero in

```text
|arg X| < alpha_(d,k),
alpha_(d,k)=pi*k/(d+k-1).                           (4.2)
```

Thus every root lies in a cone about the negative axis with half-angle

```text
theta_(d,k)=pi*(d-1)/(d+k-1).                       (4.3)
```

For a rescaled root `z=dX` of modulus at most `R`, (4.3) gives only

```text
|z|+Re(z)
 <=2R sin^2(theta_(d,k)/2).                         (4.4)
```

For `d>=2` and `R>a^2`, to force the parabolic bound (1.5) through radius
`R` using only Schoenberg's sector theorem, the exact integer sufficient
order is therefore

```text
k >=max(1,ceil((d-1){pi/[2 arcsin(a/sqrt(R))]-1})). (4.5)
```

At zeta height `T`, where `R=T^2+O(1)`, this is

```text
k >=(pi/(2a)+o(1))*d*T.                             (4.6)
```

Combining this with the disk-counting floor (3.3) gives the optimistic minor
budget

```text
k >=(1/(4a)+o(1))*T^2 log T.                        (4.7)
```

For `a=0.499999`, the leading constant in (4.7) is essentially `1/2`.
Finite-order total positivity is therefore a legitimate weakening of full
hyperbolicity, but the order required by this sharp Schoenberg-sector
certificate still grows quadratically with height.  In particular, keeping
`k` fixed in this certificate cannot yield a fixed horizontal strip.

The positive theta moment formula (1.2) does not supply these minors for
free.  It makes Hankel moment matrices positive.  The needed `PF_k`
conditions are Toeplitz minors of binomially weighted coefficients.  Already
the adjacent inequalities require an *upper* bound on the log-convexity ratio
of consecutive even theta moments (a quantitative concentration estimate),
whereas Cauchy--Schwarz gives only the opposite lower bound.  This is an exact
Hankel-versus-Toeplitz mismatch, not a lack of coefficient positivity.

## 5. Why the known simultaneous Jensen wedge does not descend

The fixed-degree Hermite limit proves hyperbolicity of `J^(d,n)` for every
fixed `d` and all sufficiently large `n`.  The 2022 effective xi result gave,
among other estimates, a sufficient range of the form `n>=c exp(d/2)`.
A very recent preprint states the simultaneous wedge (for integers `d>=1`,
`n>=0`)

```text
n^3 log^2(n+2) >= K d^5
       => J^(d,n) is hyperbolic,                    (5.1)
```

for an absolute `K`, and in fact concludes that the `d` roots are distinct
and negative.  This is substantial progress on the two-parameter array, but
(5.1) has empty intersection with the base edge `n=0` for every positive
degree.  It therefore does not enter the criterion (2.3).  The source is an
August 2026 arXiv preprint, so this paragraph records its stated theorem
rather than a peer-reviewed result.

There is also an exact obstruction to integrating the wedge backwards.  The
Jensen array satisfies

```text
d/dX J^(d,n)(X)=d J^(d-1,n+1)(X).                  (5.2)
```

Suppose the polynomial on the right has simple real roots
`r_1<...<r_(d-1)`, and put

```text
A(X)=d integral_0^X J^(d-1,n+1)(u)du.
```

Then

```text
J^(d,n)(X)=gamma_n+A(X).                            (5.3)
```

The antiderivative is hyperbolic if and only if its actual missing constant
obeys all of the critical-value inequalities

```text
(-1)^(d-i)[gamma_n+A(r_i)]>=0,
i=1,...,d-1.                                        (5.4)
```

Equation (5.4) follows by interlacing and the signs at the two infinities,
and is also sufficient by the intermediate value theorem.  Hyperbolicity of
the derivative controls the critical points but says nothing about whether
the coefficient-specific constant `gamma_n` lies in the required interval.
Thus descending one derivative row restores exactly the constant
coefficient that differentiation forgot.  Repeating (5.4) down to `n=0`
is not a formal consequence of the known wedge; it is the missing xi
inequality.

## 6. The exact tau-Li formulation of the desired strip

For `tau>0`, define Freitas's coefficients

```text
alpha_m(tau)
 =1/(m-1)! [d^m/ds^m {s^(m-1)log xi(s)}]_(s=tau).   (6.1)
```

With functional-equation pairing of the zeros,

```text
alpha_m(tau)
 =1/tau sum_rho [1-(rho/(rho-tau))^m].              (6.2)
```

For `tau>=1/2`, Freitas's half-plane criterion gives the exact equivalence

```text
alpha_m(tau)>=0 for every m>=1
 iff zeta has no zero with Re(rho)>tau/2.            (6.3)
```

The functional equation supplies the reflected half-plane.  Hence, for
`0<=a<=1/2`, a strip of half-width `a` is proved by

```text
tau=1+2a,
alpha_m(1+2a)>=0 for every m.                       (6.4)
```

For the explicit target in the theta report,

```text
a=0.499999,       tau=1.999998.                     (6.5)
```

This is genuinely weaker than ordinary Li positivity at `tau=1`, and it has
the advantage that all Euler series below converge absolutely.

## 7. Exact e-folding scale for one offending zero

Let an offending zero be

```text
rho=beta+iT,
beta=tau/2+delta,       delta>0.
```

Its conformal amplification factor in (6.2) is

```text
R_tau(rho)=|rho/(rho-tau)|,

R_tau(rho)^2
 =1+2*tau*delta/[T^2+(beta-tau)^2].                 (7.1)
```

Therefore

```text
log R_tau(rho)
 =1/2 log(1+2*tau*delta/[T^2+(beta-tau)^2])
 =tau*delta/T^2+O_tau,delta(T^(-4)).                (7.2)
```

Even one e-fold of exceptional-zero amplification requires

```text
m_amp=1/log R_tau(rho)
      =(1+o(1))*T^2/(tau*delta).                    (7.3)
```

A dominant-zero proof which requires one e-fold cannot operate below this
degree; phase alignment and domination of the remaining zero terms impose
additional conditions.  Thus a finite verification interpreted through that
specific amplification mechanism has the optimistic resolution
`delta asymp T^2/M`.  This does not exclude a more delicate finite,
cancellation-sensitive inference before one e-fold.  An all-height use of the
exact criterion still requires control of unbounded coefficient degree.

## 8. Exact prime and theta ledgers: both lose termwise sign

For `tau>1`, use the absolutely convergent identity

```text
log zeta(s)=sum_(q>=2) Lambda(q)/log(q) *q^(-s).     (8.1)
```

Here `q` ranges over the positive integers; the von Mangoldt weight restricts
the nonzero atoms to prime powers.

Applying the differential operator in (6.1) term by term gives

```text
alpha_(n+1)(tau)
 =A_(n+1)(tau)
  -sum_(q>=2) Lambda(q)q^(-tau)
       L_n^(1)(tau log q),                          (8.2)
```

where `A_(n+1)` is the explicit contribution of

```text
(1/2)s(s-1)pi^(-s/2)Gamma(s/2),
```

and `L_n^(1)` is the generalized Laguerre polynomial.  Formula (8.2) follows
from the exact identity

```text
1/n! d^(n+1)/ds^(n+1)[s^n exp(-Ls)]
 =-L exp(-Ls)L_n^(1)(Ls).                           (8.3)
```

For every `n>=1`, `L_n^(1)` has `n` positive simple zeros and alternates
sign.  Thus positive Mangoldt atoms do not give primewise positivity.

There is a sharp uniformity warning.  The standard global Laguerre bound

```text
exp(-x/2)|L_n^(1)(x)|<=n+1,       x>=0,             (8.4)
```

turns the absolute majorant in (8.2) into

```text
(n+1)sum_q Lambda(q)q^(-tau/2),                    (8.5)
```

which diverges for every `tau<=2`.  Hence the most natural
degree-uniform absolute estimate reaches its abscissa-of-convergence wall
exactly at the safe endpoint `tau=2`; it cannot move even infinitesimally to
`tau=1.999998`.  Fixed-`n` convergence of (8.2) uses the polynomial growth
in `log q`, but that bound deteriorates exponentially/factorially with `n`
and does not supply the uniform sign.

The exact theta representation has the same gate in nonlinear form.  Let
`Phi_ev(u)=Phi(|u|)` be the even extension of the kernel in (1.2).  At a real
`tau`, normalize

```text
dP_tau(u)
 =Phi_ev(u)exp((2tau-1)u)du
   /integral_R Phi_ev(v)exp((2tau-1)v)dv.           (8.6)
```

Then derivatives of `log xi` are cumulants of the random variable `2u`:

```text
(log xi)^(j)(tau)=kappa_j,tau(2u),                  (8.7)
```

and Leibniz gives

```text
alpha_(n+1)(tau)
 =sum_(j=1)^(n+1) binom(n+1,j)
    tau^(j-1)/(j-1)! *kappa_j,tau(2u).              (8.8)
```

The density in (8.6) is positive, so its variance is positive, but higher
cumulants have no general sign.  Replacing the actual theta density by a
generic positive or log-concave density therefore cannot prove (8.8).  The
missing statement is coefficient-specific cancellation among all cumulant
orders, equivalently among all signed Laguerre blocks in (8.2).

Finally, the Freitas coefficients satisfy the exact differential chain

```text
(tau/n)alpha_n'(tau)+(n+1)/n alpha_n(tau)
 =alpha_(n+1)(tau).                                 (8.9)
```

Although every `alpha_n(2)` is nonnegative by (6.3), the elementary
absolute/Gronwall continuation of (8.9) carries a factor `n/tau` and has
natural scale `1/n` unless one proves a new relative relation between adjacent
coefficients (and mere nonnegativity gives no positive margin at all).  In
particular, continuity at the safe endpoint by itself supplies no window
uniform in degree.

## 9. Search-space verdict

No explicit `a<1/2` is obtained.  The audit does materially narrow the two
coefficient routes.

1. The relevant Jensen object is not the eventually hyperbolic derivative
   wedge.  It is the base row `J^(d,0)` with the parabolic bounded-root
   condition (2.3).
2. A proof relying only on Schoenberg's generic finite-PF sector guarantee
   needs order growing at least like `T^2 log T/a` when coupled to a
   disk-wide height-`T` certificate.
3. The current simultaneous hyperbolicity wedge cannot be descended by
   Rolle/interlacing: each descent requires the exact critical-value test
   (5.4) for the missing theta coefficient.
4. The direct fixed-strip Li criterion is `alpha_m(1.999998)>=0` for all
   `m`.  Its standard exceptional-zero dominance mechanism has optimistic
   e-folding degree `T^2/delta`.
5. At this exterior evaluation point the prime formula is fully convergent,
   but its Laguerre weights are signed; the standard uniform absolute bound
   fails precisely at `tau=2`.

The most focused surviving coefficient problem is therefore either

> prove all signed Laguerre sums (8.2) are positive at
> `tau=1.999998`, using cancellation tied to the actual primes,

or, equivalently on the theta/Jensen side,

> prove the coefficient-specific critical-value inequalities (5.4) down to
> the base row with enough quantitative strength to force the parabola
> `P_(0.499999)`.

Fixed-degree Hermite limits, fixed-order Schoenberg/PF certificates, finite
Li verification, generic moment positivity, and endpoint continuity do not
reach this diagonal.

## Literature anchors

- M. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp, and I. Wagner,
  *Jensen Polynomials for the Riemann Xi Function*, Adv. Math. 397 (2022):
  https://arxiv.org/abs/1910.01227
- J. Holland, *A new hyperbolicity wedge and a joint semicircle limit for
  Jensen polynomials of Riemann's xi-function* (2026 preprint):
  https://arxiv.org/abs/2608.08682
- R. Jenkins and K. D. T.-R. McLaughlin, *Dynamic behavior of the roots of
  the Taylor polynomials of the Riemann xi function with growing degree*:
  https://arxiv.org/abs/1609.05965
- P. Freitas, *A Li-type criterion for zero-free half-planes of Riemann's
  zeta function*, J. London Math. Soc. 73 (2006):
  https://arxiv.org/abs/math/0507368
- I. J. Schoenberg's sharp finite-PF sector theorem is quoted, with the
  precise angle used in (4.2), in:
  https://d-nb.info/1147681783/34
- N. Palojarvi, *Explicit zero-free regions and a tau-Li-type criterion*:
  https://arxiv.org/abs/1807.01506
