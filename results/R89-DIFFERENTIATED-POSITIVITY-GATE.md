# Differentiated positivity, power-sum localization, and the pole-resolution wall

Status: R89 exact differentiated explicit formula, exact prime-side
positivity, pole-versus-target theorem, trigonometric coefficient-budget
no-go, and a quantitative Turan/local-density tradeoff.  Differentiating
does remove the archimedean `log T` term.  It does **not** produce a fixed
zero-free strip.  The order needed to resolve the local zero cloud is
incompatible with retaining a zero a fixed distance from one against the
pole at one.

The proposed escape from R88 was to differentiate

```text
D(s)=-zeta'(s)/zeta(s)
```

before applying prime-side trigonometric positivity.  This is a real
improvement in one respect: the gamma/conductor term is differentiated from
size `log T` to a decaying power.  The resulting zero kernel, however, is a
high reciprocal power.  That same power distinguishes ordinates only after
an order of about `(sigma-1)log T`, while it attenuates a target at
`beta=1-e` relative to the pole by

```text
exp[-(m+1)e/(sigma-1)].
```

The two requirements are simultaneously possible only at the classical
moving scale `e=O(1/log T)`, not at any fixed `e`.

```text
archimedean log differentiation                 WORKS
positive von Mangoldt coefficients              EXACT
target reciprocal-power amplification           EXACT
target/pole ratio                                < 1
constant target reserve                          forces sigma-1 >> m(1-beta)
local-zero resolution                            forces m >> (sigma-1)log T
both conditions                                  force 1-beta << 1/log T
ordinary zero-density closure                    FAILS
fixed zero-free strip                            NOT PROVED.          (1.1)
```

## 2. Exact differentiated identities

For an integer `m>=0`, put

```text
Q_m(s)=(-1)^m D^(m)(s),
p=m+1.                                                        (2.1)
```

In `Re(s)>1`, absolute convergence gives

```text
Q_m(s)=sum_(n>=2) Lambda(n)(log n)^m n^(-s).                  (2.2)
```

Consequently

```text
|Q_m(sigma+it)|<=Q_m(sigma),             sigma>1.             (2.3)
```

This is the exact characteristic-function bound for the positive measure

```text
dmu_(m,sigma)(x)
 =sum_(n>=2)Lambda(n)(log n)^m n^(-sigma)delta_(log n).        (2.4)
```

Let

```text
P(theta)=a_0+sum_(1<=k<=d)a_k cos(k theta).                    (2.5)
```

Then the differentiated prime identity is

```text
F_(m,P)(sigma,T)
 :=a_0Q_m(sigma)+sum_(1<=k<=d)a_k Re Q_m(sigma+i kT)

 =sum_(n>=2)Lambda(n)(log n)^m n^(-sigma)P(T log n).           (2.6)
```

Thus

```text
P>=0  ==>  F_(m,P)(sigma,T)>=0.                                (2.7)
```

This includes every finite Fejer--Riesz or scalar Gram construction at one
derivative order.

For `m>=1`, differentiation also makes the completed explicit formula
particularly clean.  Hadamard factorization and the polygamma partial
fraction expansion give the absolutely convergent identity

```text
Q_m(s)/m!
 =1/(s-1)^p
  -sum_rho 1/(s-rho)^p
  -sum_(j>=1)1/(s+2j)^p.                                      (2.8)
```

The first term is the zeta pole, the second runs over nontrivial zeros with
multiplicity, and the third runs over the trivial zeros.  Formula (2.8) is
also a useful sign audit: a zeta zero always has coefficient `-1`, but the
real part of its reciprocal-power kernel changes sign as its vertical angle
is multiplied by `p`.

At `s=sigma+iT`, the pole term is `O(T^(-p))`, and the trivial-zero sum is
`O_(p,sigma)(T^(1-p))`.  The logarithmic conductor in R88 has genuinely
gone away.  The nontrivial-zero power sum is the remaining high-ordinate
object; it cannot be discarded, because zeros occur with local density
asymptotic to a constant times `log T`.

## 3. The pole is horizontally closer than the target

Write

```text
sigma=1+delta,             delta>0,
rho_0=1-e+iT,              e=1-beta>0.                          (3.1)
```

At zero ordinate, the pole principal part in (2.8) is

```text
m!/delta^p.                                                    (3.2)
```

At ordinate `T`, the target zero principal part is negative real and has
size

```text
m!/(delta+e)^p.                                                (3.3)
```

Their exact ratio is

```text
r_p(delta,e)
 :=[delta/(delta+e)]^p
  =exp[-p log(1+e/delta)]<1.                                  (3.4)
```

In particular, retaining a fixed fraction `r_0` of the pole scale requires

```text
p log(1+e/delta)<=log(1/r_0).                                  (3.5)
```

For `e/delta` small this is precisely

```text
delta >= (1+o(1)) p e/log(1/r_0).                              (3.6)
```

Even an ideal factor-two target coefficient only allows the target to beat
the pole principal part if

```text
r_p(delta,e)>1/2,
delta >(1+o(1))p e/log 2.                                     (3.7)
```

The factorial does not help: the same `m!` multiplies every pole and zero
at order `m`, so it cancels from all comparisons.

For fixed `delta`, the rest of `Q_m(1+delta)` is exponentially smaller than
the pole as `m` tends to infinity.  Indeed, on any fixed compact real
interval to the right of one, the pole at one is strictly closer than every
other pole in (2.8).  Hence, for some `R_delta>delta`,

```text
Q_m(1+delta)/m!
 =delta^(-p)+O_delta(R_delta^(-p)).                             (3.8)
```

Thus high differentiation makes the zero-frequency pole domination more,
not less, exact.  If `e` is fixed, (3.4) tends exponentially to zero.

## 4. A coefficient-budget no-go for every nonnegative trigonometric
polynomial

Suppose `P>=0` and `a_1>0`.  Evaluation at `theta=pi` gives the elementary
but decisive inequality

```text
0<=P(pi)=a_0-a_1+sum_(k>=2)(-1)^k a_k,

a_1<=a_0+sum_(k>=2)|a_k|.                                     (4.1)
```

Now make the most optimistic possible termwise argument:

* retain the target contribution `-m!/(delta+e)^p` at the first harmonic;
* suppose every collateral term at the first harmonic vanishes;
* use the exact prime bound (2.3) on all other harmonics.

Such an argument could contradict (2.7) only if

```text
a_1 m!/(delta+e)^p
 >(a_0+sum_(k>=2)|a_k|)Q_m(1+delta).                            (4.2)
```

In the high-order regime (3.8), (4.1) and (3.4) make (4.2) impossible.  At
the principal-part level it would require simultaneously

```text
a_1>a_0+sum_(k>=2)|a_k|     and     r_p<1.                       (4.3)
```

This explains exactly what happens to the apparent ratio `a_1/a_0 ->2`
available from shifted Fejer kernels.  The higher harmonics needed to create
that ratio consume all of the reserve.  Bounding them independently returns
the coefficient budget (4.1).

This is not a proof that a joint harmonic estimate is impossible.  It proves
that absolute values, individual zero-density bounds, and separate estimates
for `2T,3T,...` cannot close the argument.  A successful proof would have to
use a target-conditioned correlation between those ordinates.

## 5. Exact horizontal-localization tradeoff

There is a stronger obstruction than the inequality `r_p<1`.  Suppose a
collateral zero lies at horizontal gap `Ae` from one, where `A>=1`, and at
the same ordinate as the target.  Relative to the target, its reciprocal
power has size

```text
c_p(delta,e;A)
 =[(delta+e)/(delta+Ae)]^p.                                    (5.1)
```

### Theorem 5.1 (signal retention prevents fixed-factor localization)

If

```text
r_p(delta,e)>=r_0>0,                                          (5.2)
```

then for every real `A>=1`,

```text
c_p(delta,e;A)>=r_0^(A-1).                                    (5.3)
```

#### Proof

Put `x=e/delta`.  Convexity, or the binomial inequality, gives

```text
1+Ax<=(1+x)^A.                                                 (5.4)
```

Therefore

```text
[(1+x)/(1+Ax)]^p
 >=(1+x)^[-p(A-1)]
 =r_p(delta,e)^(A-1)
 >=r_0^(A-1).                                                  (5.5)
```

This is (5.3).

The theorem is independent of how large `m` is.  Once the target retains a
constant fraction of the pole, increasing `m` cannot distinguish it by more
than a constant factor from zeros whose gaps are any fixed multiple of `e`.
To gain even a factor `1/log T`, one must move the collateral boundary to

```text
A-1 >= log log T/log(1/r_0).                                   (5.6)
```

Thus the horizontally unresolved region grows from width `e` to width
`e log log T`; it does not remain a fixed multiple of the hypothesized gap.

The standard local zero count makes the same point quantitatively.  In the
relevant range `0<delta+eta<=1`, for `p>=2`, partitioning ordinates into
unit intervals and using
`N(t+1)-N(t)=O(log(t+2))` gives, schematically,

```text
sum_(rho: beta<=1-eta)|1+delta+iT-rho|^(-p)
 <<_p log(T+2)(delta+eta)^(-p) + O_p(1).                        (5.7)
```

For this absolute bound to be small compared with the target requires

```text
log T [(delta+e)/(delta+eta)]^p=o(1).                           (5.8)
```

If `eta=Ae` with fixed `A` and (5.2) holds, Theorem 5.1 says the power ratio
in (5.8) is bounded below by a positive constant.  The `log T` local-density
loss therefore survives.  A marginal zero-density theorem cannot repair a
pointwise cluster at the ordinate of the exceptional zero.

Far critical-line zeros are not the essential obstruction.  If their
horizontal distance is about `delta+1/2`, their absolute bulk is of order

```text
log T (delta+1/2)^(1-p),                                       (5.9)
```

and `p` of order `log log T` can suppress it when `delta+e` is much smaller
than `delta+1/2`.  What remains is the near-one cluster, whose horizontal
scale is comparable with the target and is governed by (5.3).

## 6. The Turan order and the moving-strip scale

Power-sum localization does not evade the preceding tradeoff.  Near height
`T`, zeros have mean vertical spacing

```text
h asymp 1/log T.                                                (6.1)
```

For a zero with horizontal distance about `delta`, moving its ordinate by
`h` changes the argument of its reciprocal by

```text
theta asymp h/delta asymp 1/(delta log T).                      (6.2)
```

After raising to the `p`th power, the phase separation is `p theta`.
Resolving adjacent terms, or running a Turan lemma over the
`N asymp delta log T` zeros in a vertical window of radius `delta`, therefore
costs an order span at least

```text
p >> delta log T.                                               (6.3)
```

A standard Turan power-sum lemma selects an order in an interval whose
length is comparable with the number of competing powers.  Its additional
constant is at most one, so it cannot improve the target/pole ratio.

The incompatibility can be stated without asymptotic notation.  Suppose a
uniform power-sum step has to take

```text
p>=c delta log T                                                  (6.3a)
```

for some fixed `c>0`, and suppose it retains `r_p(delta,e)>=r_0`, with
`0<r_0<1`.  Since

```text
log(1+x)>=x/(1+x),
```

target retention implies

```text
p e/(delta+e)<=log(1/r_0).                                       (6.3b)
```

It also implies `delta/(delta+e)>=r_0`.  Combining these facts with (6.3a)
gives the exact bound

```text
e log T<=log(1/r_0)/(c r_0).                                    (6.3c)
```

Thus any Turan implementation with the local-count order budget proves at
most a moving `constant/log T` region, irrespective of how its remaining
constants are optimized.

On the other hand, keeping a constant target reserve in (3.4) requires

```text
delta >> p e.                                                   (6.4)
```

Combining (6.3) and (6.4) gives the self-consistency condition

```text
p >> delta log T >> p e log T,

e << 1/log T.                                                   (6.5)
```

Equivalently, if one takes `p asymp delta log T` to resolve the cloud, then

```text
r_p(delta,e)
 approx exp(-p e/delta)
 approx exp(-e log T)=T^(-e).                                  (6.6)
```

For fixed `e>0`, the target has lost a power of `T` before Turan
localization begins.  Conversely, taking `delta asymp p e` to preserve the
target makes the local cluster contain `asymp p e log T` zeros; asking an
order-`p` power sum to isolate it again forces `e log T=O(1)`.

This calculation accounts for all three apparent resources:

* the factorial `m!` cancels between all principal parts;
* growing `m` supplies angular resolution;
* the same growing `m` exponentially worsens the horizontally closer pole.

It recovers a moving zero-free scale of de la Vallee Poussin type.  It cannot
produce a fixed strip.

## 7. Mixing derivative orders inside the continuous positive cone

One might try to cancel the pole by combining several derivative orders.
Let

```text
W(x)=sum_(0<=m<=M)lambda_m x^m>=0,             x>=0,             (7.1)
```

and define

```text
Q_W(s)=sum_m lambda_m Q_m(s)
      =sum_(n>=2)Lambda(n)W(log n)n^(-s).                         (7.2)
```

The pole and target principal responses are the Laplace transforms

```text
H_W(delta)
 =sum_m lambda_m m! delta^(-m-1)
 =integral_0^infinity W(x)e^(-delta x)dx,

H_W(delta+e)
 =integral_0^infinity W(x)e^(-(delta+e)x)dx.                     (7.3)
```

Because `W>=0`,

```text
0<=H_W(delta+e)<=H_W(delta).                                    (7.4)
```

Thus no mixture which preserves positivity as a continuous Laplace weight
can make the farther target exceed the pole.  The coefficient budget from
Section 4 then applies unchanged.

There is a narrow coefficient-specific loophole: one could demand only
`W(log n)>=0` on the discrete prime-power support while allowing `W` to be
negative between support points.  Then (7.4) need not hold.  Exploiting that
loophole would require quantitative interpolation on the actual prime-power
set at the saddle `log n asymp m/delta`; it is no longer an automatic
differentiated-positivity argument.  It is a new prime-distribution estimate,
and no such estimate is proved here.

The simplest version of this loophole can already be bounded exactly.  Take

```text
W_M(x)=x^M(x-a)(x-b),             M>=1,                          (7.5)
```

where `(a,b)` contains no point `log n` with `Lambda(n)>0`.  The support
contains every `log(2^j)=j log 2`, so necessarily

```text
b-a<=log 2.                                                       (7.6)
```

Put `c=(a+b)/2`, `h=(b-a)/2`, and let `X` have the gamma distribution with
shape `M+1` and rate `delta`.  The pole response is exactly

```text
integral_0^infinity W_M(x)e^(-delta x)dx

=M! delta^(-M-1)
  [(M+1)/delta^2+((M+1)/delta-c)^2-h^2].                         (7.7)
```

For fixed `delta`, (7.6)--(7.7) rule out exponential pole cancellation as
`M` grows.  Replacing `delta` by `delta+e` changes the square bracket by at
most a polynomial-order factor, whereas the prefactor loses
`[delta/(delta+e)]^(M+1)`.  Thus one empty prime-power gap cannot compensate
the fixed-`e` target loss at high order.  A surviving discrete construction
would need many gaps and growing oscillation degree, with its full size and
Turan costs retained.

## 8. A countermodel for differentiated positivity plus upper zero density

The failure is structural, not merely a weak choice of polynomial.  Fix
arbitrary `e>0`, `gamma!=0`, and choose

```text
A>=log 2/e.                                                     (8.1)
```

For `x>=A`, set

```text
w(x)=e^x-2e^((1-e)x)cos(gamma x)>=0.                            (8.2)
```

Its Laplace transform is

```text
F_*(s)
 =e^(-(s-1)A)/(s-1)
  -e^(-(s-rho)A)/(s-rho)
  -e^(-(s-conjugate(rho))A)/(s-conjugate(rho)),

rho=1-e+i gamma.                                                (8.3)
```

It has logarithmic-derivative residues `+1` at one and `-1` at `rho` and
its conjugate.  For every `m>=0`,

```text
Q_m^*(s)=integral_A^infinity x^m e^(-sx)w(x)dx                  (8.4)
```

has positive coefficients in the Laplace sense.  Hence for every
nonnegative trigonometric polynomial `P`, every derivative order, and every
`sigma>1`,

```text
a_0Q_m^*(sigma)+sum_(k>=1)a_k Re Q_m^*(sigma+i kT)
 =integral_A^infinity x^m e^(-sigma x)w(x)P(Tx)dx>=0.           (8.5)
```

The model has only one nonreal zero pair, so it also satisfies every usual
upper zero-density assertion after an inessential adjustment of constants.
Since `e` is arbitrary, differentiated positivity plus marginal upper zero
density cannot logically imply a uniform gap.  Extra symmetric zero pairs
can be added while preserving positivity by increasing `A`.

This is a structural countermodel, not a counterexample to a statement
about zeta: it does not have the exact coefficients `Lambda(p^k)=log p` over
all primes.  It proves that any successful continuation must use that exact
cross-prime coefficient structure, rather than only positivity of all its
derivatives and a census of zeros.

## 9. Decision and the surviving estimate

Differentiation solves the superficial R88 problem and exposes the deeper
one:

1. `Q_m` has nonnegative prime coefficients and no high-ordinate
   archimedean `log T` term.
2. Its zero kernel is the exact reciprocal power `(s-rho)^(-m-1)`.
3. The target is horizontally farther from `1+delta` than the pole is from
   the zero-frequency point, giving the ratio (3.4).
4. Nonnegative trigonometric polynomials cannot supply a coefficient reserve
   after their other harmonics are bounded separately, by (4.1).
5. Turan localization needs `m+1` of order `delta log T`; target retention
   needs `delta` of order at least `(m+1)(1-beta)`.  Together they force
   `1-beta=O(1/log T)`.
6. Ordinary upper zero density cannot control the signed, target-conditioned
   near-one cluster, and the countermodel (8.3) shows why.

The only live escape inside this branch is therefore one of the following:

```text
(i)  a signed target-conditioned power-sum estimate for the zeros near T
     whose cost is o(delta log T), or

(ii) a coefficient-specific derivative weight W which is nonnegative on
     every actual prime power, violates the continuous Laplace domination
     (7.4), and has quantitatively controlled degree and size.              (9.1)
```

Neither input follows from known Turan lemmas or zero-density bounds, and
neither is established in this repository.  The differentiated route thus
does not prove a fixed zero-free strip and does not prove that no such strip
exists.
