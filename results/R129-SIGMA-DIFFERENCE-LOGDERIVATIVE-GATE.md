# Sigma-differenced logarithmic derivatives: the zero-mass sign gate

Status: exact prime-side positivity and divisor identities, a genuine
target-versus-pole parameter window, an exact Herglotz/sign obstruction, and
a fixed-power density ledger.  A forward difference in `sigma` really does
remove the leading archimedean `log T`.  It does **not** prove a fixed
zero-free strip.  In the parameter window where the target beats the pole,
the cancelled archimedean mass reappears as equal positive and negative mass
in the zero kernel.  Separating the unfavorable part costs order `log T`, and
known marginal zero-density estimates do not supply the required signed,
target-conditioned cancellation.

The main conclusions are

```text
positive prime coefficients after sigma differencing        EXACT
leading Gamma log T cancellation                             EXACT
target can beat the pole at principal-part level             YES
positive-real zero kernel after Gamma cancellation            IMPOSSIBLE
unfavorable bulk in the viable growing-step window            >> log T
fixed-gap target retention plus vertical resolution           INCOMPATIBLE
known marginal zero density                                   INSUFFICIENT
fixed zero-free strip                                         NOT PROVED.
```

This is a gate for this method, not a proof that a fixed strip does not
exist.

## 1. Exact finite-difference identities

Write

```text
D(s)=-zeta'(s)/zeta(s)
```

and, for an integer `m>=1` and `h>0`, define

```text
Delta_(m,h)D(s)
 =sum_(j=0)^m (-1)^j binom(m,j)D(s+jh).                         (1.1)
```

For `Re(s)>1`, absolute convergence gives

```text
Delta_(m,h)D(s)
 =sum_(n>=2) Lambda(n)n^(-s)(1-n^(-h))^m.                       (1.2)
```

Thus every coefficient in (1.2) is nonnegative.  If

```text
P(theta)=a_0+sum_(1<=k<=d)a_k cos(k theta)>=0,                  (1.3)
```

then

```text
S_(m,h,P)(sigma,T)
 :=a_0 Delta_(m,h)D(sigma)
   +sum_(1<=k<=d)a_k Re Delta_(m,h)D(sigma+i kT)

 =sum_(n>=2) Lambda(n)n^(-sigma)(1-n^(-h))^m P(T log n)>=0.     (1.4)
```

This includes every scalar Fejer--Riesz construction at a fixed difference
order.

The corresponding divisor kernel is

```text
K_(m,h)(z)
 :=sum_(j=0)^m (-1)^j binom(m,j)/(z+jh)
  =m! h^m/[z(z+h)...(z+mh)]
  =integral_0^infinity e^(-zu)(1-e^(-hu))^m du.                 (1.5)
```

The last identity holds for `Re(z)>0`.  Finite differencing kills the
normalization constant in the Mittag--Leffler expansion of `D`.  Since
`K_(m,h)(z)=O(|z|^(-m-1))`, the resulting divisor sums are absolutely
convergent and give the exact formula

```text
Delta_(m,h)D(s)
 =K_(m,h)(s-1)
  -sum_rho K_(m,h)(s-rho)
  -sum_(q>=1)K_(m,h)(s+2q).                                    (1.6)
```

The first term is the zeta pole, the second sum is over nontrivial zeros
with multiplicity, and the last sum is over the trivial zeros.

Formula (1.6) makes the archimedean cancellation exact.  For fixed `m` and
`|t|>=2`, adding a positive real number to a point in the right half-plane
can only increase its modulus, so comparison with an integral gives

```text
sum_(q>=1)|K_(m,h)(sigma+it+2q)|
 <=C_m m! h^m |t|^(-m).                                        (1.7)
```

There is no surviving `log |t|` term.  The qualification in (1.7) matters:
if `h` is comparable with or larger than `T`, its right side need not be
small.  For fixed `m` and `h=o(T)`, it is `o(1)` after the natural
normalization.

As `h->0`, one has

```text
h^(-m) Delta_(m,h)D(s) -> (-1)^m D^(m)(s),                      (1.8)
```

so this family contains the differentiated-positivity route of R89.  As
`h->infinity` at a fixed point, it tends locally to `D(s)`; the compensating
negative kernel mass then moves out to vertical scale comparable with `h`.

## 2. The target can genuinely beat the pole

Suppose a hypothetical zero is

```text
rho_0=1-epsilon+iT,       epsilon>0,
sigma=1+r,                r>0.                                  (2.1)
```

At the zero-frequency point the pole response in (1.6) is `K_(m,h)(r)`.
At the first harmonic the target response is `K_(m,h)(r+epsilon)`.  Their
exact ratio is

```text
R_(m,h)(r,epsilon)
 :=K_(m,h)(r+epsilon)/K_(m,h)(r)
  =product_(j=0)^m (r+jh)/(r+epsilon+jh).                       (2.2)
```

Nonnegativity of `P` implies the sharp Fourier bound

```text
a_1<=2a_0.                                                       (2.3)
```

Fejer kernels with `a_0=1` have `a_1->2`.  Consequently the optimistic
principal-part comparison has reserve precisely when

```text
R_(m,h)(r,epsilon)>1/2.                                         (2.4)
```

Unlike high differentiation, finite differences do have a nonempty
fixed-gap window satisfying (2.4).  The cleanest example is

```text
m=1,       h=T^alpha with 0<alpha<1,
r=c epsilon with fixed c>1.                                    (2.5)
```

Here

```text
K_(1,h)(x)=h/[x(x+h)],
R_(1,h)(r,epsilon)
 =r(r+h)/[(r+epsilon)(r+epsilon+h)] -> c/(c+1)>1/2,             (2.6)
```

while the high-ordinate trivial-zero term in (1.7) is
`O(h/T)=o(1)`.  The high-harmonic zeta-pole terms are smaller still.  Thus
the proposal does not fail because the target is automatically weaker than
the pole.  There is a real principal-part opening.

The reflected zero `epsilon+iT` supplies another same-sign target term and
only improves this optimistic comparison.  It does not repair the
collateral-zero sign problem below.

## 3. Exact positive-real obstruction

The price of (1.7) is an unavoidable loss of sign.

### Theorem 3.1 (zero vertical mass)

For every `m>=1`, `h>0`, and `x>0`,

```text
integral_(-infinity)^infinity K_(m,h)(x+iy)dy=0.                (3.1)
```

In particular,

```text
integral Re K_(m,h)(x+iy)dy=0.                                 (3.2)
```

Since `K_(m,h)(x)>0`, its real part takes both signs, and

```text
integral [Re K]_+ dy=integral [-Re K]_+ dy>0.                   (3.3)
```

#### Proof

The rational function in (1.5) has no pole in `Re(z)>0` and is
`O(|z|^(-m-1))`.  Close the vertical line `Re(z)=x` by a right semicircle.
The arc integral tends to zero for `m>=1`, proving (3.1).  Positivity at
`y=0`, continuity, and (3.2) prove (3.3).

There is also a direct Herglotz interpretation.  Each resolvent
`1/(x+jh+iy)` has real-part integral `pi`.  The coefficient of the
archimedean `log T` is the total resolvent coefficient, while

```text
sum_(j=0)^m(-1)^j binom(m,j)=0.                                 (3.4)
```

Cancelling that coefficient therefore cancels the vertical mass.  A
nonzero positive-real function cannot have zero nonnegative mass.  Hence
Gamma cancellation and a termwise nonnegative zero kernel are incompatible,
not merely difficult to arrange.

The same obstruction survives a trigonometric polynomial.  For a zero of
fixed real part, its effective kernel is a finite linear combination of
vertical translates of `Re K`; its integral is again zero.  Distinct
translates are linearly independent as rational functions, so a nontrivial
combination cannot be nonnegative everywhere.  No Fejer--Riesz or finite
Gram reparameterization restores a pointwise sign.

## 4. Quantitative cancellation debt

The sign loss has a scale fixed by the same logarithmic derivative that
controls target retention.  Put

```text
A_(m,h)(x)=sum_(j=0)^m 1/(x+jh).                                (4.1)
```

For `y>=0`, (1.5) gives

```text
arg K_(m,h)(x+iy)
 =-sum_(j=0)^m arctan(y/(x+jh)),                                (4.2)

|K_(m,h)(x+iy)|/K_(m,h)(x)
 =product_(j=0)^m [1+(y/(x+jh))^2]^(-1/2).                     (4.3)
```

For `|y|<=1/[2A_(m,h)(x)]`, the argument has modulus at most `1/2`, and
`sqrt(1+u^2)<=exp(|u|)` shows

```text
Re K_(m,h)(x+iy)
 >=c_0 K_(m,h)(x),
c_0=e^(-1/2)cos(1/2).                                          (4.4)
```

Combining (4.4) with Theorem 3.1 gives the exact lower bound

```text
integral [-Re K_(m,h)(x+iy)]_+ dy
 >=c_0 K_(m,h)(x)/A_(m,h)(x).                                  (4.5)
```

On the other hand,

```text
-log R_(m,h)(r,epsilon)
 =integral_r^(r+epsilon) A_(m,h)(u)du
 >=epsilon A_(m,h)(r+epsilon).                                 (4.6)
```

Therefore, if the target retains a fraction `R>=r_0` of the pole, then

```text
A_(m,h)(r+epsilon)<=log(1/r_0)/epsilon                          (4.7)
```

and its unavoidable unfavorable vertical mass satisfies

```text
integral [-Re K_(m,h)(r+epsilon+iy)]_+ dy
 >=[c_0 epsilon/log(1/r_0)]K_(m,h)(r+epsilon).                  (4.8)
```

At the pole-beating threshold `r_0=1/2`, the constant in brackets is about
`0.768 epsilon`.  Thus no choice of `m` and `h` can both retain a fixed-gap
target and make the sign-indefinite part have vanishing normalized `L^1`
mass.

This is the precise cancellation debt hidden by the disappearance of the
Gamma term.  Against a vertical zero density of order `log T`, an
absolute-value treatment naturally costs

```text
epsilon log T times the target scale.                            (4.9)
```

For a fixed `epsilon`, that cost grows rather than vanishes.

## 5. The apparent window (2.5) contains an actual bad bulk

For `m=1`, the sign can be seen without an abstract theorem:

```text
Re K_(1,h)(x+iy)
 =x/(x^2+y^2)-(x+h)/[(x+h)^2+y^2].                              (5.1)
```

It is negative exactly when

```text
|y|>sqrt[x(x+h)].                                               (5.2)
```

The positive and negative areas are equal.  If
`y_0=sqrt[x(x+h)]`, their common value is

```text
2[arctan(y_0/x)-arctan(y_0/(x+h))] -> pi                       (5.3)
```

as `h/x->infinity`.

More importantly, the unfavorable mass is not only a continuum norm in the
growing-step window.  Fix a bounded range `0<x<=B`.  Once `h>=40B`, (5.1)
gives uniformly for

```text
h/2<=|y|<=h
```

the bound

```text
Re K_(1,h)(x+iy)<=-1/(10h).                                    (5.4)
```

Take `h=T^alpha`, `0<alpha<1`.  Riemann--von Mangoldt on the interval
`[T-h,T-h/2]` gives

```text
N(T-h/2)-N(T-h)
 =(h/(4pi))log T+O(h^2/T+log T)
 >>h log T.                                                     (5.5)
```

For every zero in that interval, `x=sigma-beta` stays in the bounded range
`r<x<r+1`.  Equations (5.4)--(5.5) therefore imply

```text
sum_(T-h<=gamma<=T-h/2) Re K_(1,h)(sigma-beta+i(T-gamma))
 <=-c log T.                                                    (5.6)
```

The minus sign in the explicit formula turns (5.6) into a positive
`c log T` obstruction to the desired contradiction.  Other vertical zones
carry an opposite mass of the same order; their cancellation is what
replaces the deleted Gamma term.  Bounding the unfavorable zone separately
therefore loses `log T` even though the target and pole in (2.6) are only of
fixed size.

For any fixed `m`, the same phenomenon occurs when `h->infinity` and
`h=o(T)`.  On the scale `y=theta h`,

```text
h K_(m,h)(x+i theta h)
 ->m!/[i theta product_(j=1)^m(j+i theta)].                     (5.7)
```

The limiting real part is negative on a nonempty compact theta interval
(near zero its finite real part begins with `-H_m`).  Such an interval has
length comparable with `h`, contains `>>h log T` zeta zeros, and each kernel
value is `<=-c_m/h`.  Hence every fixed-order, growing-step version of the
principal-part window carries an actual unfavorable bulk `>>_m log T`.

This does not say that the *signed total* zero sum is `log T`; it is not.
It says exactly why zero density plus separation into favorable and
unfavorable terms cannot close the proof.  One needs cancellation between
those terms before taking absolute values.

## 6. Exact signal/localization tradeoffs

Two inequalities show that growing order does not evade the debt.

### 6.1 Horizontal localization

For every real `C>=1`, termwise use of
`1+Cu<=(1+u)^C` gives

```text
K_(m,h)(r+C epsilon)/K_(m,h)(r+epsilon)
 >=R_(m,h)(r,epsilon)^(C-1).                                   (6.1)
```

Thus, if `R>=r_0`, a zero whose distance from one is any fixed multiple
`C epsilon` is attenuated relative to the target by no more than the fixed
factor `r_0^(C-1)`.  To gain even `1/log T` requires

```text
C-1>=log log T/log(1/r_0).                                     (6.2)
```

The horizontally unresolved band therefore grows to width
`epsilon log log T`; it does not remain a fixed multiple of the target gap.

### 6.2 Vertical resolution

By (4.2) and (4.7), the phase change at vertical separation `d` is at most

```text
|arg K_(m,h)(r+epsilon+id)|
 <=d A_(m,h)(r+epsilon)
 <=d log(1/r_0)/epsilon.                                       (6.3)
```

Zeros near height `T` have mean spacing of order `1/log T`.  Any Turan or
angular-isolation step which needs an order-one phase change across that
scale must have

```text
A_(m,h)(r+epsilon)>=c log T.                                   (6.4)
```

Together, (4.7) and (6.4) force

```text
epsilon log T<=log(1/r_0)/c.                                   (6.5)
```

This is the de la Vallee Poussin moving scale, not a fixed strip.  In the
small-step limit, `A=(m+1)/(r+epsilon)+o(1)`, and (6.5) becomes exactly the
derivative-order/Turan tradeoff in R89.  Large steps merely move the
negative mass to a wider vertical band, as Section 5 shows.

## 7. What known zero density does and does not buy

The relevant imported bounds have the following shapes:

```text
N(U+1)-N(U)=O(log(U+2)),                                        (7.1)

N(sigma,T)<=T^[(30/13)(1-sigma)+o(1)]                           (7.2)
```

in the near-one range of the Guth--Maynard consequence audited in R98.
The first estimate permits `O(log T)` zeros in a unit interval.  The second
permits

```text
T^[(30/13)C epsilon+o(1)]                                      (7.3)
```

zeros with `beta>=1-C epsilon` up to height `T`, for every fixed positive
`C epsilon`.  Neither is a signed estimate conditioned on one of those
zeros being the target at ordinate `T`.

Combining (7.1) with absolute values incurs the cancellation debt (4.9).
Combining (7.2) with (6.1) does not help: a fixed horizontal multiple gives
only a fixed attenuation, while the density bound still has a positive
power of `T`.  Choosing `C` as in (6.2) enlarges the unresolved near-one
band and makes the density exponent worse.  Most fundamentally, an upper
density theorem can declare exceptional ordinates sparse but cannot exclude
the one exceptional ordinate at which the hypothetical zero is assumed.

Thus there is no `m,h,r` window in which the known marginal density inputs
make the collateral term `o(K_(m,h)(r+epsilon))` for fixed `epsilon`.  The
growing-step window fails by the actual bulk theorem (5.6); bounded or
growing-order windows stop at the signed, target-conditioned estimate
identified by (4.8), (6.1), and (6.3).

## 8. Trigonometric freedom does not supply the missing correlation

The exact characteristic-function bound from (1.2) is

```text
|Delta_(m,h)D(sigma+it)|<=Delta_(m,h)D(sigma).                  (8.1)
```

For every nonnegative trigonometric polynomial with `a_1>0`, evaluation at
`theta=pi` gives

```text
a_1<=a_0+sum_(k>=2)|a_k|.                                      (8.2)
```

Consequently, estimating the harmonics `2T,3T,...` separately by (8.1)
uses all of the apparent Fejer reserve.  A successful use of (1.4) must
keep a signed joint zero sum across the dilates rather than apply marginal
density or absolute values at each one.

There is also a structural countermodel showing exactly what extra input is
missing.  Fix arbitrary `epsilon>0`, `gamma!=0`, and
`A>=log(2)/epsilon`, and put

```text
w(x)=e^x-2e^((1-epsilon)x)cos(gamma x)>=0,       x>=A,

D_*(s)=integral_A^infinity w(x)e^(-sx)dx
 =e^(-(s-1)A)/(s-1)
  -e^(-(s-rho)A)/(s-rho)
  -e^(-(s-conjugate(rho))A)/(s-conjugate(rho)),

rho=1-epsilon+i gamma.                                         (8.3)
```

This model has residue `+1` at the pole `1` and residue `-1` at an
arbitrarily near-one nonreal pair.  Yet for every `m,h`, every `sigma>1`,
and every `P>=0`,

```text
a_0 Delta_(m,h)D_*(sigma)
 +sum_(k>=1)a_k Re Delta_(m,h)D_*(sigma+i kT)

 =integral_A^infinity w(x)e^(-sigma x)(1-e^(-hx))^m P(Tx)dx
 >=0.                                                          (8.4)
```

The model has only finitely many zero-like poles, so it satisfies every
marginal upper zero-density inequality.  It is not a model of zeta's exact
prime coefficients or functional equation.  It proves that positivity of
all sigma differences, nonnegative trigonometric tests, and marginal upper
zero density cannot logically imply a fixed strip.  Any continuation must
use coefficient-specific zeta information or a genuinely joint signed
correlation.

## 9. Verdict and surviving theorem

Sigma differencing improves the superficial ledger and even opens a real
target-versus-pole window.  The exact obstruction is deeper:

1. cancelling the leading Gamma term forces the zero kernel to have zero
   vertical mass;
2. a nonzero kernel of zero mass cannot be positive real;
3. retaining enough target signal to beat the pole forces a fixed amount of
   negative `L^1` mass and prevents both horizontal and vertical
   localization at fixed gap;
4. in the clean growing-step window, actual zeta zeros supply an unfavorable
   contribution `>>log T` before signed cancellation;
5. known zero density controls counts, not that signed cancellation at an
   ordinate already conditioned to contain a near-one zero.

The precise new input that would revive the route is a bound of the form

```text
sum_(rho not in target quartet) sum_(k=0)^d
 a_k Re K_(m,h)(1+r+i kT-rho)
 >=-o(K_(m,h)(r+epsilon)),                                     (9.1)
```

uniformly under the condition that `1-epsilon+iT` is a zeta zero, in a
parameter regime satisfying (2.4).  It must be signed before absolute
values and joint across all harmonic centers.  No theorem in the audited
literature or this repository supplies (9.1).

Accordingly, this method proves neither a fixed zero-free strip nor the
nonexistence of one.  It rigorously closes the proposed automatic route
through high-order sigma differences plus ordinary zero density.
