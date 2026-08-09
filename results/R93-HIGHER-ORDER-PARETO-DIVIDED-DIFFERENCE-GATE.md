# R93 higher-order Pareto divided-difference gate

Status: the higher-order construction is exact, positive, and genuinely
smoother, but it does not move the nonvanishing boundary.  With `k+1`
Pareto rates it applies a zero-free rational low-pass filter to the R92
carrier.  The resulting transform has exactly the same zeros as `zeta` in
`Re(s)>0`.  More sharply, after `k` smoothing steps the first unsmoothed
derivative still has a unit jump at every `log(n)`, so its exponentially
weighted total jump mass is

```text
sum_(n>=1) n^(-sigma).
```

It is finite exactly for `sigma>1`.  Thus ordinary Fourier decay,
bounded-variation, stationary-phase, total-positivity, and Rouché estimates
based only on the new smoothness all stop at the old absolute-convergence
line.  Letting the order grow suppresses the entire zeta signal by
`|t|^(-k-1)` and introduces exponential barycentric conditioning; it does
not preferentially suppress the cancelling part.  No fixed strip is proved
or disproved here.

Date: 2026-08-07.

## 1. Construction and verdict

Write

```text
a_j=r_j-1,                 0<a_j<=1,                  (1.1)
```

and initially suppose that the `a_j` are distinct.  The R92 Pareto carrier
at rate `a+1` will be denoted by `B_a(u)`.  Its Laplace transform is

```text
L B_a(s)
 = zeta(s)(s-1)/(s(s+a)),             Re(s)>0.        (1.2)
```

Let

```text
c_j = 1 / product_(ell!=j)(a_ell-a_j).                (1.3)
```

The partial-fraction identity

```text
sum_(j=0)^k c_j/(s+a_j)
 = 1/product_(j=0)^k(s+a_j)                            (1.4)
```

gives the divided-difference carrier

```text
H_a(u)=sum_(j=0)^k c_j B_(a_j)(u)                      (1.5)
```

and the exact transform

```text
F_a(s):=L H_a(s)
 = zeta(s)(s-1)
   /[s product_(j=0)^k(s+a_j)],       Re(s)>0.         (1.6)
```

The signed formula (1.5) hides positivity.  If

```text
K_a(u)=exp(-a u) 1_(u>=0),                             (1.7)
```

then the convolution theorem and (1.2) give the stronger identity

```text
H_a
 = B_(a_0) * K_(a_1) * ... * K_(a_k).                 (1.8)
```

The right side is nonnegative.  It also extends continuously to repeated
nodes; coalescing all nodes at `a` gives

```text
F_(a,k)(s)=zeta(s)(s-1)/[s(s+a)^(k+1)],                (1.9)
```

with a gamma-convolution kernel.

For every `s` with `Re(s)>0`, other than the removable point `s=1`, the
rational factor in (1.6) is finite and nonzero.  Consequently

```text
F_a(s)=0  iff  zeta(s)=0,              Re(s)>0.        (1.10)
```

including multiplicity.  This is a useful exact carrier, not a strip by
itself.  The rest of this report checks whether its additional regularity
creates an independent nonvanishing mechanism.  It does not under any of
the proposed general analytic principles.

## 2. The base Pareto density really is positive

For completeness, put `x=exp(u)`, `N=floor(x)`, and `0<a<=1`.  Directly
integrating the Pareto law `(a+1)q^(-a-2)dq` gives

```text
B_a(log x)
 = [(a+1)x^(-a) sum_(n<=N)n^a-N]/a.                   (2.1)
```

On each interval `N<=x<N+1`, the right side decreases with `x`.  The
concave-power Riemann-sum inequality

```text
(a+1)sum_(n=1)^N n^a >= N(N+1)^a,
                    0<a<=1,                           (2.2)
```

therefore proves `B_a>=0`.  One way to prove (2.2) is to scale by `N+1`
and use that the uniform measure on the interior grid
`{1/(N+1),...,N/(N+1)}` is smaller in convex order than uniform measure on
`[0,1]`; applying the concave function `x^a` gives

```text
(1/N)sum_(n=1)^N (n/(N+1))^a
 >= integral_0^1 x^a dx=1/(a+1).                     (2.3)
```

For an elementary proof of the convex-order assertion, let `Q_N` be the
quantile function of the uniform interior grid.  If
`m/N<=t<=(m+1)/N`, direct summation gives

```text
integral_0^t [Q_N(v)-v]dv
 = sum_(j=1)^m j/[N(N+1)]
   +(t-m/N)(m+1)/(N+1)-t^2/2.                        (2.3a)
```

This is a concave quadratic in `t`.  At its two endpoints it equals

```text
m(N-m)/[2N^2(N+1)],
(m+1)(N-m-1)/[2N^2(N+1)],                           (2.3b)
```

so it is nonnegative.  The grid law and the continuous uniform law both
have mean `1/2`, which proves the claimed convex order.  The power
inequality is strict when `0<a<1` and is equality when `a=1`.

There is also a uniform bound.  The elementary estimate

```text
sum_(n<=N)n^a <= N^(a+1)/(a+1)+N^a                  (2.3c)
```

inserted in (2.1) gives

```text
0<B_a(u)<=(a+1)/a.                                  (2.3d)
```

The range `a<=1`, equivalently `r<=2`, is sharp for the carrier itself.
For fixed `a>1`, Euler summation at the left trace of `x=N+1` gives

```text
B_a(log(N+1)-)=(1-a)/(2a)+o(1)<0.                   (2.3e)
```

Thus an infinite-order construction cannot send its resolvent rates to
infinity while retaining the base positivity.

At every positive integer the floor term jumps by one while the continuous
Pareto average has no atom.  Hence

```text
B_a(log n+)-B_a(log n-)=1,             n>=2.          (2.4)
```

The jump size is independent of `a`.  This innocuous fact is the exact
reason moment cancellation smooths the carrier and the exact reason the
arithmetic jump comb eventually reappears.

Euler summation also gives, with `theta={x}`,

```text
B_a(log x)
 = (a+1)/(2a)-theta
   +[(a+1)/a] zeta(-a)x^(-a)+O_a(x^(-1)).             (2.5)
```

Thus the base carrier does not converge pointwise.  Its increasingly rapid
sawtooth has logarithmic local mean

```text
m_a=1/(2a).                                           (2.6)
```

The first convolution in (1.8) averages this sawtooth and produces a true
limit.

## 3. What the moment cancellation buys

Expansion of (1.4) at infinity gives the exact moment ledger

```text
sum_j c_j a_j^m = 0,                  0<=m<k,
sum_j c_j a_j^k = (-1)^k.                            (3.1)
```

Since the jump (2.4) and its first `k-1` response coefficients are
polynomials of the corresponding degrees in `a`, (3.1) cancels them.  The
equivalent convolution statement is simpler:

```text
H_a is C^(k-1),
H_a(u)=u^k/k!+O_a(u^(k+1)) as u->0+,                  (3.2)
```

where for `k=0` the function has the original jumps.  In particular,

```text
H_a^(m)(0+)=0,             0<=m<k,
H_a^(k)(0+)=1.                                        (3.3)
```

The regularity statement can be made completely local and exact.  On the
open cell `log N<u<log(N+1)`, differentiation of (2.1) gives, for `m>=1`,

```text
D^m B_a(u)
 =(-1)^m(a+1)a^(m-1)e^(-au)sum_(n<=N)n^a.            (3.3a)
```

Consequently its right-minus-left trace at `u=log N` is

```text
Delta D^m B_a(log N)=(-1)^m(a+1)a^(m-1).             (3.3b)
```

This is a monic degree-`m` polynomial in `a`, up to the displayed sign.
The barycentric moments (3.1) therefore imply

```text
Delta D^m H_a(log N)=0,                 0<=m<k,
Delta D^k H_a(log N)=1,                 every N>=2.  (3.3c)
```

There are no hidden `N`-dependent lower terms.  In the original `x`
coordinate the corresponding first surviving jump is exactly `N^(-k)`.
Thus `H_a` is `C^(k-1)` but not `C^k` at any integer knot.

The final-value constant follows either from (2.5) and (1.8), or from the
residue of (1.6) at zero:

```text
lim_(u->infinity) H_a(u)
 = Res_(s=0) F_a(s)
 = 1/[2 product_j a_j]
 =: C_a,                              k>=1.           (3.4)
```

For fixed distinct nodes strictly below `1`, Euler summation gives the more
precise form

```text
H_a(u)
 = C_a + sum_j R_j exp(-a_j u)+O_a(exp(-k u)),        (3.5)

R_j = [(a_j+1)/a_j] zeta(-a_j)
      /product_(ell!=j)(a_ell-a_j).                   (3.6)
```

At repeated nodes the corresponding exponential is multiplied by a
polynomial in `u`; at the endpoint `a_j=1`, the arithmetic `exp(-u)`
remainder and the rational transient coalesce.  Neither qualification
affects the argument below.  Formula (3.5) explains the appeal of the
construction: each extra divided difference removes another visible order
of the floor ripple.

The first surviving floor ripple is also explicit.  Standard Euler
summation, with `theta={x}` and Bernoulli polynomial `B_ell(theta)`, gives

```text
B_a(log x)
 = (a+1)/(2a)-theta+[(a+1)/a]zeta(-a)x^(-a)
   +sum_(ell=2)^L (-1)^ell
      [(a+1) product_(h=1)^(ell-2)(a-h)/ell!]
      B_ell(theta)x^(1-ell)+O_(a,L)(x^(-L)).          (3.6a)
```

The product after `(a+1)` is empty for `ell=2`.  Its coefficient is a
degree-`ell-1` polynomial in `a`.  Hence all terms with `ell<=k` vanish in
the order-`k` divided difference, while the monic leading term at
`ell=k+1` survives.  For distinct nodes this yields

```text
H_a(log x)
 = C_a + sum_j [(a_j+1)zeta(-a_j)/a_j]
       x^(-a_j)/product_(ell!=j)(a_ell-a_j)
   -B_(k+1)(theta)/[(k+1)!x^k]+O_a(x^(-k-1)).        (3.6b)
```

If `a_0<...<a_k`, the first transient has coefficient

```text
[(a_0+1)/a_0]zeta(-a_0)
 /product_(j>0)(a_j-a_0)<0,                          (3.6c)
```

so the carrier approaches its limit from below.  At a repeated node the
same term is replaced by a negative leading multiple of
`u^k exp(-a u)`.  Formula (3.6b) makes the smoothing ledger precise: the
order-one sawtooth is pushed to amplitude `x^(-k)`, but the slower rational
transients and the complete zeta divisor remain.

But it removes it only from a lower derivative.  In the distributional
sense, `H_a^(k)` still has

```text
Delta H_a^(k)(log n)=1,                n>=2.           (3.7)
```

up to lower-order continuous terms.  Equivalently, applying all resolvents
in (1.8) backwards recovers the original forcing.  Extend all functions by
zero to `u<0` and interpret `D` distributionally, so the `n=1` atom records
the startup boundary.  Then

```text
product_(j=0)^k(D+a_j) H_a
 = sum_(n>=1) delta_(log n)-floor(exp(u)).             (3.8)
```

Taking Laplace transforms of (3.8) gives

```text
product_j(s+a_j)F_a(s)
 = (s-1)zeta(s)/s,                                    (3.9)
```

which is just (1.6).  Higher-order smoothing has moved the integer comb to
a higher derivative; it has not changed a single coefficient of that comb.

## 4. The sharp variation ledger: the wall remains `sigma=1`

Tilt by `exp(-sigma u)`.  The total mass of the jumps in (3.7), through
`log X`, is exactly

```text
V_sigma(X)=sum_(n<=X)n^(-sigma).                       (4.1)
```

For fixed `0<sigma<1`, Euler summation gives

```text
V_sigma(X)
 = X^(1-sigma)/(1-sigma)+zeta(sigma)+O_sigma(X^(-sigma)),
                                                               (4.2)
```

while

```text
V_1(X)=log X+gamma+O(1/X).                             (4.3)
```

Therefore

```text
V_sigma(infinity)<infinity  iff  sigma>1.             (4.4)
```

After `k+1` integrations by parts, every absolute Fourier or
bounded-variation estimate encounters (4.1).  The formal factor
`|t|^(-k-1)` is real, but the remaining variation is infinite throughout
the desired strip.  On a cutoff `X` the best absolute jump estimate has
the scale

```text
|t|^(-k-1) X^(1-sigma)/(1-sigma),     sigma<1.        (4.5)
```

The exponent `1-sigma` is completely independent of `k`.

This is not merely a limitation of integration by parts.  From (1.6), for
`|t|>=2` and `0<sigma<=1`,

```text
|F_a(s)|
 = |zeta(s)| |t|^(-k-1)
   exp(O((k+1)/t^2)),                  s=sigma+it,     (4.6)
```

uniformly for `0<a_j<=1` when `k=o(t^2)`.  Without that restriction one has
the elementary two-sided ledger

```text
(2/sqrt(5)) |zeta(s)|/(t^2+4)^((k+1)/2)
 <= |F_a(s)|
 <= (sqrt(5)/2) |zeta(s)|/|t|^(k+1).                 (4.7)
```

Thus the gain in Fourier decay is exactly a common nonzero multiplier.  It
reduces the wanted signal and the unwanted cancellation by the same power.
There is no relative gain to spend on nonvanishing.

## 5. Constant-tail Rouché fails at the startup boundary

The limit (3.4) suggests writing

```text
F_a(s)=C_a/s+R_a_hat(s),
R_a(u)=H_a(u)-C_a.                                    (5.1)
```

For `k>=1`, however, `R_a(0+)=-C_a`.  Integration by parts makes the exact
leading cancellation visible:

```text
R_a_hat(s)=-C_a/s+terms of order s^(-k-1).            (5.2)
```

Along the positive real axis this can be read without any oscillatory
estimate.  Since `zeta(s)=1+O(2^(-s))`, (1.6) and (3.3) give

```text
F_a(s)=s^(-k-1)(1+O_a(1/s)+O(2^(-s))),
                                             s->+infinity.   (5.3)
```

Consequently

```text
R_a_hat(s)/(C_a/s) -> -1.                             (5.4)
```

No inequality of the form

```text
|R_a_hat(s)| <= q |C_a/s|,             q<1,           (5.5)
```

can hold on the whole right half-plane.  The attractive constant tail and
the equally necessary zero startup cancel to `k` orders before the
arithmetic signal appears.

Subtracting the transients in (3.5) does not alter the basic ledger.  More
generally, let

```text
T_a(s)=(s-1)/[s product_j(s+a_j)].                    (5.6)
```

For any comparison function `Z_0`, a model produced through the same
resolvent is `M=T_a Z_0`, and

```text
|F_a-M|<|M|
 iff
|zeta-Z_0|<|Z_0|.                                    (5.7)
```

The divided-difference carrier cancels exactly out of the Rouché
inequality.  Taking `Z_0=1`, a truncated Euler--Maclaurin main term, or a
pole model therefore gives precisely the corresponding classical zeta
problem.  A successful different model is logically possible, but its
relative estimate is the new number-theoretic theorem; positivity and
smoothing have supplied none of it.

## 6. Positive-real and monotonicity routes

The decreasing-density theorem from R91 cannot apply:

* for `k=0`, `B_a` has an upward jump at every `log n`;
* for `k>=1`, `H_a(0)=0` and `H_a(u)>0` immediately afterward, so it cannot
  be nonnegative and nonincreasing;
* a completely monotone function is nonincreasing, so that class is also
  excluded at the endpoint.

It is conceivable for a heavily smoothed `H_a` to be eventually increasing
toward `C_a`.  That property is not enough.  Even if `dH_a` were a positive
measure, one would only obtain

```text
sF_a(s)=integral exp(-su)dH_a(u).                     (6.1)
```

Laplace transforms of positive measures can vanish in `Re(s)>0`; the
two-atom example

```text
1+2exp(-s)                                            (6.2)
```

has zeros at `s=log(2)+(2m+1)pi i`.

Nor can `F_a` have positive real part, or remain in any fixed open
half-plane, throughout a vertical strip inside `1/2<sigma<1`.  For a fixed
such `sigma`, zeta universality gives values of `zeta(sigma+it)` in every
open angular sector.  Meanwhile

```text
arg T_a(sigma+it)=-(k+1)pi/2+o(1),       t->+infinity. (6.3)
```

Hence `F_a(sigma+it)` also enters every angular sector.  This
unconditionally rules out a fixed-sector or fixed-rotation positive-real
proof.  A rotation chosen from the phase of zeta would of course assume the
quantity whose nonvanishing is at issue.

There is also a generic reality check.  Given any `s_0` with
`Re(s_0)>0`, `Im(s_0)!=0`, and any finite smoothness order, one can choose
three nonnegative compactly supported smooth bumps at delays whose phases
`exp(-i Im(s_0)u_j)` surround the origin.  Positive amplitudes can then be
chosen so that their Laplace vectors sum to `-C/s_0`.  Adding them to the
constant density `C` produces a nonnegative smooth function, equal to `C`
outside a compact set, whose Laplace transform vanishes at `s_0`.
Positivity, arbitrary finite smoothness, and asymptotic constancy are
therefore not a generic zero-free package.

The shift relevant to a fixed strip makes the endpoint obstruction exact.
For `0<sigma_0<1`, put

```text
G_(a,sigma_0)(u)=exp(-sigma_0 u)H_a(u).              (6.4)
```

Then

```text
L G_(a,sigma_0)(z)
 =[(z+sigma_0-1)zeta(z+sigma_0)]
  /[(z+sigma_0)product_j(z+sigma_0+a_j)].            (6.5)
```

Nonvanishing of (6.5) in `Re(z)>0` is exactly zeta nonvanishing in
`Re(s)>sigma_0`.  For `k=0`, (6.4) retains upward jumps of size
`n^(-sigma_0)`.  For `k>=1`, it starts at zero and is strictly positive
immediately afterward, so it cannot be nonincreasing.  Product
differentiation and (3.3c) give the sharper invariant

```text
Delta D^k G_(a,sigma_0)(log n)=n^(-sigma_0).         (6.6)
```

Thus even a proposed `k`-monotone extension of the decreasing-density
theorem encounters an upward jump at its first unsmoothed derivative.
Its variation is precisely the divergent ledger in Section 4.

Log-concavity, unimodality, and arbitrary finite smoothness would not be
enough even if they happened to hold.  For an exact counterexample, take

```text
w(u)=exp(bu)1_[0,L](u),                 b>0,          (6.7)
q_m(u)=u^(m-1)exp(-cu)/(m-1)!,          c>0.          (6.8)
```

Both are log-concave on their supports, and so is `w*q_m`.  The latter is
strictly positive for `u>0`, can have any prescribed finite boundary order
and smoothness by increasing `m`, and has Laplace transform

```text
[1-exp(-(z-b)L)]/[(z-b)(z+c)^m].                     (6.9)
```

It vanishes at

```text
z=b-2 pi i ell/L,                       ell!=0,       (6.10)
```

inside the right half-plane.  Hence none of these softer shape properties
is a zero-free Laplace class.  The decreasing/completely-monotone and
`PF_infinity` classes are special precisely because they impose much more
than a smooth single hump.

## 7. Total positivity and variation diminution

Each exponential kernel `K_a` in (1.7) is a Pólya-frequency kernel, and
their convolution is again totally positive.  What follows from this is
that convolution does not increase the number of real sign changes of an
input.  The input `B_a` is already nonnegative, so the conclusion here is
only the positivity already recorded in (1.8).

It does **not** follow that the output, viewed as a translation kernel, is a
Pólya-frequency function.  Such an inference would require the input to
belong to that class.  In fact it cannot: Hardy's theorem supplies
infinitely many zeros `1/2+i gamma` of zeta, and (1.10) gives

```text
F_a(1/2+i gamma)=0.                                   (7.1)
```

After exponential tilting, a genuine `PF_infinity` density has the standard
zero-free bilateral Laplace representation in its convergence strip.
Equation (7.1) therefore rules out `PF_infinity` for every order and every
choice of nodes.  This uses known critical-line zeros, not RH.

Finite-order variation diminution is also inert.  Applied separately to
the real and imaginary parts of `exp(-itu)`, the input has infinitely many
sign changes on `[0,infinity)`.  The resulting `infinity<=infinity` bound
cannot prevent the two Fourier components from vanishing simultaneously.
The exact jump ledger (4.1) is the quantitative form of this failure.

## 8. Stationary phase just reconstructs zeta

Between consecutive `log n`, repeated integration by parts is legitimate.
Summing the boundary terms at all cells yields

```text
sum_(n>=1) exp(-s log n)=sum_(n>=1)n^(-s)=zeta(s)     (8.1)
```

in the absolute half-plane, and its analytically continued counterpart
elsewhere.  Thus there is no hidden stationary point created by the
Pareto parameters.  They appear only in the common transfer function
`T_a(s)`.

With a cutoff at `X`, absolute summation gives (4.5).  Any improvement must
use cancellation in

```text
sum_(n<=X)n^(-sigma-it),                              (8.2)
```

or, after arithmetic decompositions, in the corresponding prime/divisor
sums.  Those are standard zeta exponential sums.  Upper bounds for (8.2)
control growth but do not by themselves give a lower bound excluding a
zero.  A uniform Rouché lower bound strong enough in a fixed strip is the
desired new zeta theorem, not an output of the extra differentiability.

The sharp fail-fast statement is therefore:

```text
number of added smoothings                 k
Fourier power gained                       |t|^(-k)
weighted jump abscissa                     1
arithmetic exponent below that abscissa    X^(1-sigma)
change in the zero set                     none.       (8.3)
```

## 9. Barycentric conditioning

The convolution representation is stable and positive, but the signed
divided-difference representation becomes badly conditioned when the
nodes are close.  If the nodes are equally spaced across an interval of
length `L`, so `a_j=a_0+jL/k`, then

```text
sum_j |c_j|
 = (2k/L)^k/k!
 ~ (2e/L)^k/sqrt(2 pi k).                              (9.1)
```

Thus any argument which estimates the terms in (1.5) separately pays an
exponential factor.  Coalescing the nodes avoids numerical cancellation by
using the gamma convolution (1.9), but does not change (1.10) or (4.4).

There are two further parameter costs:

```text
C_a=1/(2 product_j a_j),                              (9.2)

slowest transient scale = 1/min_j a_j.               (9.3)
```

Taking a node toward zero makes the apparent constant tail large while
making the approach to that tail proportionally slower.  Normalizing the
tail cancels the large factor and leaves no improved relative estimate.

## 10. Logarithmic complete-monotonicity also fails

There is one plausible refinement worth killing separately.  Numerical
experiments suggest that for some node sets, especially at order at least
two, `H_a` itself may be increasing.  Suppose, conditionally, that
`H_a'(u)>=0` for a chosen family.  Since `H_a(0)=0`, its derivative has
Laplace transform

```text
J_a(s)=sF_a(s)
      =(s-1)zeta(s)/product_(j=0)^k(s+a_j).           (10.1)
```

Positivity would make `J_a` completely monotone on the positive real
axis.  A tempting next step is to seek infinite divisibility or logarithmic
complete monotonicity, because a normalized infinitely divisible Laplace
transform is zero-free.  That stronger step has an exact signed-measure
obstruction.

For real `s>1`, logarithmic differentiation of (10.1) and the Euler product
give

```text
-J_a'(s)/J_a(s)
 = sum_j 1/(s+a_j)
   +sum_(n>=2) Lambda(n)n^(-s)-1/(s-1).              (10.2)
```

Its unique inverse Laplace distribution is

```text
dnu_a(u)
 =sum_(n>=2)Lambda(n)delta_(log n)
  +[sum_j exp(-a_j u)-exp(u)]du.                     (10.3)
```

The absolutely continuous density in (10.3) is strictly negative for all
sufficiently large `u`.  The positive prime-power atoms cannot cancel a
negative absolutely continuous component.  By uniqueness in Bernstein's
theorem, `-J_a'/J_a` is not completely monotone on any real half-line on
which (10.2) is represented.  Replacing `J_a(s)` by `J_a(s+sigma_0)` merely
multiplies (10.3) by `exp(-sigma_0 u)` and preserves the negative sign.

Therefore, even if monotonicity of a particular second- or higher-order
carrier derivative were proved, its law would not be infinitely divisible
and the logarithmically-completely-monotone zero-free route would still
fail.  This conclusion is exact and does not depend on the numerical
monotonicity observation.

## 11. Growing order and continuum limits

Normalize the carrier to have limiting value one.  Its transform is

```text
Fbar_a(s)
 = 2 product_j a_j
   zeta(s)(s-1)/[s product_j(s+a_j)].                 (11.1)
```

The product

```text
product_j a_j/(s+a_j)                                (11.2)
```

is the Laplace transform of a sum of independent exponential delays.  Its
mean and variance satisfy

```text
mean = sum_j 1/a_j >= k+1,
variance = sum_j 1/a_j^2 >= k+1.                     (11.3)
```

For every fixed `sigma>0`,

```text
|product_j a_j/(s+a_j)|
 <= (1/(1+sigma))^(k+1).                              (11.4)
```

So the normalized carriers drift to the right and their transforms tend
to zero locally in `Re(s)>0`.  The limit has lost the signal; it has not
become a nonvanishing comparison function.

For coalesced nodes the factor is simply

```text
[a/(s+a)]^(k+1),                                     (11.5)
```

the gamma-delay transform.  For an empirical continuum of rates, its
logarithm converges after division by `k+1` to

```text
integral log(a/(s+a)) dnu(a).                         (11.6)
```

Exponentiating (11.6) produces a zero-free infinitely divisible transfer
factor.  Multiplying zeta by a zero-free factor preserves all zeta zeros.
Centering the delay multiplies by `exp(ms)`, also zero-free, and sacrifices
causal positivity without changing that conclusion.

There is no nontrivial finite-variation superposition which cancels the
knots to every order.  Indeed, for a finite signed measure `omega` on
`0<a<=1`, the jump formulas are

```text
integral domega(a),
(-1)^m integral (a+1)a^(m-1)domega(a),   m>=1.       (11.6a)
```

If all of these vanish, `omega` annihilates every polynomial: the displayed
polynomials are a triangular basis by degree.  Density of polynomials in
continuous functions then forces `omega=0`.  A nonzero bounded
superposition must leave a first uncancelled derivative.

The positive infinite-convolution version degenerates for a different but
equally exact reason.  After tail normalization, each new factor is the
probability density `a_j exp(-a_j u)`.  The accumulated delay has mean
`sum 1/a_j`, which tends to infinity because `a_j<=1`.  For each fixed
`U`, its probability of lying in `[0,U]` tends to zero (it is
stochastically larger than a gamma sum of unit-rate exponentials).  Hence
the normalized carrier tends locally to zero while its plateau escapes to
infinity.  Infinite smoothing does not leave a nontrivial fixed-scale
carrier on which to apply a zero-free theorem.

Allowing `k=k(t)` does not help pointwise.  At every proposed zero `rho`,

```text
F_(a,k(rho))(rho)=T_(a,k(rho))(rho)zeta(rho)=0        (11.7)
```

because the selected transfer factor is nonzero.  All orders and all node
choices form a rank-one family over zeta:

```text
F_a/F_b = T_a/T_b                                    (11.8)
```

where defined, and the right side is explicit and contains no arithmetic.
Parameter derivatives, Wronskians, and finite determinants either retain a
power of zeta or cancel zeta completely and become rational identities.
They do not create an independent common-zero channel.

## 12. Reproducible probe and method ledger

The companion files

```text
src/pareto_divdiff_probe.py
src/test_pareto_divdiff_probe.py
```

evaluate (2.1), Newton divided differences, one-sided knot derivatives,
the truncated piecewise Mellin integral, and the jump-variation ledger.
For the nodes `(1.2,1.5,2.0)`, direct sampling gives

```text
sampled order-two carrier range on 1<=x<=50:
    [0.00113886010566, 1.59172308570]

jumps at u=log(17):
    Delta H                 -1.82e-14
    Delta H'                 7.22e-15
    Delta H''                1.00000000000

sum_(n<=X)n^(-0.9):
    X=100        5.42673048458
    X=1000       9.52350661180
    X=10000     14.68887588810.                       (12.1)
```

At `s=2.7+0.4i`, summing the exact integrals on the first 3000 integer
cells differs from (1.6) by `5.13e-10`.  The five automated tests check
sampled positivity through order three, the zero/unit knot-jump pattern,
the order-`k` startup, the transform identity, and divergence of the
weighted jump mass.  These computations verify formulas; they are not
used as evidence for nonvanishing.

The analytic ledger is:

```text
method                         genuine gain              fatal remainder
positive convolution           H_a>=0                    positive Laplace transforms can vanish
decreasing-density theorem     none                       H_a starts upward / keeps jump ancestry
positive-real rotation         none                       universality fills every angular sector
constant-tail Rouche           explicit C_a              startup cancels C_a/s to k orders
transient subtraction          explicit residues R_j     relative inequality reduces to zeta
PF-infinity                    smooth PF kernels          known critical-line zeros exclude output PF
finite variation diminution    k-1 continuous derivatives infinite oscillatory sign changes
Fourier integration by parts   |t|^(-k-1)                sum n^(-sigma), abscissa 1
stationary phase               standard log-n phases     reconstructs zeta exponential sums
large k / repeated nodes       gamma smoothing            whole signal shrinks, zeros unchanged
continuum of rates             zero-free Levy factor      still a scalar multiple of zeta
separate barycentric estimates none                       conditioning about (2e/L)^k.
```

## 13. Exact disposition

The higher-order Pareto construction should be retained as an exact smooth
positive reformulation:

```text
zeta has a fixed zero-free strip
iff
some/every H_a has a zero-free Laplace transform in that strip.          (12.1)
```

Its useful contribution is diagnostic.  It proves that arbitrarily high
finite smoothness, nonnegativity, asymptotic constancy, and a nonlattice
delay spectrum can coexist with the full zeta zero set.  It also identifies
the invariant obstruction more sharply than a generic equivalence: the
unit logarithmic integer comb survives in derivative order `k`, and its
absolute mass has abscissa exactly one.

Accordingly, another scalar Pareto smoothing is not the next target.  A
viable continuation must introduce information that is not a zero-free
scalar transfer of the same comb -- for example, a genuinely joint
arithmetic channel whose determinant is not identically rank one, or a new
signed estimate for the complete comb below its absolute-convergence line.
Proving such an estimate may prove a fixed strip; none of the general
analytic properties audited here does so.
