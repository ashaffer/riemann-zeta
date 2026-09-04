# Global half-disk Pick transfer: an exact binomial screen and the remaining quantitative gap

Status: exact growing half-disk obstruction, exact depth-sensitive microscopic
zero count, exact all-jet continuum identity, and exact covariance descent,
2026-08-12.  These results substantially sharpen the global Pick gate, but
they neither prove nor disprove the budgeted actual-zeta transfer.  In
particular, no zero-free strip is proved.

## 1. Verdict

There are now two rigorous growing statements which were missing from the
fixed-cell audit.

1. A completely explicit list of `2(K+1)` half-disk rows forces every scalar
   Schur function to lose a fixed exponential amount when `K` is proportional
   to `L`.  The proof uses two interlaced binomial finite differences and has
   no growing-jet conditioning hypothesis.
2. A log-derivative argument improves the number of zeros in one microscopic
   ordinate cell at horizontal threshold `sigma_0` to

   ```text
   M(sigma_0;t,C/L)
       <=((1-sigma_0)/2+o(1))*L.                  (1.1)
   ```

The unconstrained optimizer of the explicit screen is compatible with the
coarse Riemann--von Mangoldt/Bellotti--Wong count and with the microscopic
count applied one cell at a time.  It is **not** compatible with the sharper
fixed-width integral of the same Poisson/log-derivative identity.  That
integrated count restricts its density parameter to

```text
c<=0.00465416454...                                 (1.2)
```

at the proposed strip edge.  The largest count-compatible forced
attenuation is consequently

```text
F(c)<=0.01118512309... .                            (1.3)
```

This is below the older residual reserve `0.0119000134...` by
`0.0007148903...`, and well below the improved `0.025391255...`
Green/Poisson margin in the companion audit.  Thus the first fully rigorous
growing obstruction is absorbed, narrowly, even by the old ledger once the
horizontal depth information is used correctly.  It remains a forced lower
loss for one adversarial list, not a universal construction proving that
every list is affordable.

It nevertheless proves that growing real half-disk constraints genuinely
can force exponential attenuation; a fixed-cluster theorem cannot simply be
iterated with an unspecified `X^o(1)` constant.

It does **not** yet falsify the desired budgeted theorem.  The displayed
configuration occupies about `K/2` phase cells, and the one-factor-per-cell
potential bill in the most dangerous central block can be larger than the
exponential loss certified below.  Conversely, it does not prove the global
lower bound.  A universal half-product (up to one subpower exceptional
factor) remains consistent with every exact test in this note.

The tempting one-cell `K -> infinity` obstruction also remains unproved.
There is an exact continuum measure annihilating every analytic jet and
fixed-order positive quadratures follow, but the measure has an unbounded
scaled-depth tail.  No quantitative quadrature theorem currently controls
both the largest depth and the conditioning when the order grows with `L`.

Finally, passing to a positive semidefinite covariance or a
Blaschke--Potapov matrix does not improve the final aggregate geometric
optimum.  Selected-positive trace zero holds channel by channel, and every
negative aggregate covariance certificate has a rank-one scalar component
with at least the same normalized aggregate negativity.

## 2. The exact interlaced-binomial screen

Fix

```text
0<alpha<1/2,       0<d<1,       D=d*L,             (2.1)
```

and an integer `K>=1`.  Put

```text
h_n =-1-i*n*pi/d,
h'_n=-1-i*(n+1/2)*pi/d,       0<=n<=K,             (2.2)

z_n =alpha+h_n/L,
z'_n=alpha+h'_n/L.                                  (2.3)
```

For `L>1/alpha` all these nodes lie in the right half-plane.  Their physical
phase angles are

```text
theta_n =n*pi,
theta'_n=(n+1/2)*pi.                                (2.4)
```

Thus the exact collateral conditions are

```text
Re[(-1)^n U(z_n)]>=0,
Re[-i*(-1)^n U(z'_n)]>=0.                           (2.5)
```

The two lists interlace at phase spacing `pi/2`; there are asymptotically
four rows per complete `2*pi` phase cell.

### Theorem 2.1 (quantitative growing Pick obstruction)

Let `U` be a right-half-plane Schur function satisfying (2.5).  Suppose

```text
K/L -> c,
0<c<alpha*d/(2*pi).                                 (2.6)
```

Then

```text
|U(alpha)|
 <=K^C * [2*pi*c/(alpha*d)+o(1)]^K,                (2.7)
```

where `C` depends only on `alpha,d,c` (and can be replaced by an explicit
fixed power).  Consequently

```text
limsup_(L->infinity) (1/L)*log|U(alpha)|
 <=-F_(alpha,d)(c),                                 (2.8)

F_(alpha,d)(c)
 =c*log[alpha*d/(2*pi*c)].                          (2.9)
```

The best exponent supplied by this family is

```text
max_c F_(alpha,d)(c)=alpha*d/(2*pi*e),
c_*=alpha*d/(2*pi*e).                              (2.10)
```

At the first-strip parameters

```text
alpha=.49,       d=.66,                             (2.11)
```

this is

```text
c_*=0.01893501551... .                              (2.12)
```

This number is an attenuation exponent for the artificial Pick list, not a
retained zeta carrier and not a zero-free bound.

#### Proof

Let `P` be any polynomial of degree below `K`.  Since both node lists are
arithmetic progressions with common step

```text
v=-i*pi/d,
h_n=-1+n*v,       h'_n=-1+(n+1/2)*v,               (2.13)
```

the `K`-th finite differences vanish:

```text
sum_(n=0)^K (-1)^n binom(K,n)P(h_n)=0,
sum_(n=0)^K (-1)^n binom(K,n)P(h'_n)=0.             (2.14)
```

Choose `r<alpha` with

```text
pi*c/d<r<alpha.                                     (2.15)
```

Taylor-expand `U(alpha+h/L)` at `h=0` through degree `K-1`.  Cauchy's
estimate in the disk `|s-alpha|<=r` gives, uniformly on both lists,

```text
U(alpha+h/L)=P_L(h)+E_L(h),
|E_L(h)|<=epsilon_L,

epsilon_L
 <=[q+o(1)]^K/[1-q+o(1)],
q=pi*c/(d*r)<1.                                    (2.16)
```

Put

```text
a_n=Re[(-1)^n P_L(h_n)],
b_n=Re[-i*(-1)^n P_L(h'_n)].                       (2.17)
```

The inequalities (2.5) give `a_n,b_n>=-epsilon_L`, while (2.14) gives

```text
sum_n binom(K,n)a_n=sum_n binom(K,n)b_n=0.          (2.18)
```

It follows termwise that

```text
|a_n|,|b_n|
 <=2^K*epsilon_L/binom(K,n).                        (2.19)
```

Write

```text
Q(t)=P_L(-1+v*t)=A(t)+i*B(t),                       (2.20)
```

where `A,B` have real coefficients.  Equation (2.19) bounds `A(n)` and
`B(n+1/2)`.  Interpolate a polynomial of degree at most `K` at
`0,1,...,K`.  Its Lagrange functions satisfy the exact cancellation

```text
|ell_n(t)|/binom(K,n)
 =|product_(m=0)^K(t-m)|/[K!*|t-n|].               (2.21)
```

For either fixed nonintegral `t`, the right side summed over `n` is
`K^O(1)`: this follows directly from the gamma quotient for the product and
the harmonic bound for the sum.  The target `h=0` corresponds to the fixed
point

```text
t_*=-(-1)/v=i*d/pi,                                 (2.22)
```

and `B(t_*)` is obtained by applying the same estimate to
`B(t+1/2)` at `t=t_*-1/2`.  Hence

```text
|P_L(0)|<=K^C*2^K*epsilon_L.                        (2.23)
```

But `P_L(0)=U(alpha)`.  Let `r` tend to `alpha` in (2.16) to obtain
(2.7)--(2.9).  Elementary differentiation gives (2.10).  QED

### Compact PW/Gabor scope

Theorem 2.1 is an upper bound over the entire Schur class.  Every normalized
causal endpoint transfer, and hence every compact PW/Gabor endpoint transfer
admitted by the current two-leg reduction, is a member of this class.
Therefore compact support cannot evade (2.7).  No compact approximation or
finite-section limiting argument is used in the proof.

The converse is not asserted: the theorem supplies no compact function
attaining the upper bound.

## 3. Count audit of the binomial screen

The screen has

```text
M=2(K+1)=(2*c+o(1))*L                              (3.1)
```

rows in the one-sided ordinate interval

```text
0<=delta<=(c*pi/d+o(1)).                            (3.2)
```

The symmetric Riemann--von Mangoldt/Bellotti--Wong pair-center envelope at
`h=c*pi/d` is

```text
M(h)/L<=h/(2*pi)+0.10076+o(1)
       =c/(2*d)+0.10076+o(1).                       (3.3)
```

At (2.12), the right side is `0.1151...`, while the screen uses only
`0.03788...`.  It is therefore admissible under this **coarse window count**
with a wide margin.  All nodes have selected-relative depth `alpha-1/L`, so
they also lie above the carrier-relevant threshold `alpha*d`.

The actual horizontal coordinate of every row is

```text
sigma_0=1/2+alpha-1/L=.99-1/L.                     (3.4)
```

Theorem 4.1 consequently permits as many as

```text
(.005+o(1))*L                                       (3.5)
```

rows in **each one microscopic ordinate window**.  The screen does not put
`2cL` rows in one such window.  Its ordinate span is

```text
c*pi/d+o(1),                                        (3.6)
```

which contains `(c/2+o(1))*L` complete phase cells, and its two interlaced
chains put asymptotically four rows in each cell.  Hence (3.5) is satisfied
with a wide margin for every fixed `c`; the cellwise theorem alone imposes
no extra restriction on the optimizer (2.12).

One must, however, integrate the Poisson identity over the **whole** fixed
ordinate interval.  The reflected-pair version of that argument is Theorem
4.2 below.  It gives

```text
c<=0.00465416454...,
F_(.49,.66)(c)<=0.01118512309... .                  (3.7)
```

Thus neither the coarse count nor a mistaken one-cell application is sharp;
the fixed-width depth-sensitive integral is the correct admissibility test.

Count compatibility does not assert that zeta realizes the screen.  It says
only that the present local and fixed-window counts do not exclude it.

## 4. A depth-sensitive microscopic zero count

The large endpoint constant in (3.3) is not sharp when both the ordinate
window and a fixed horizontal threshold are retained.

### Theorem 4.1 (microscopic Poisson cap)

Fix `C>0` and `sigma_0<1`.  Uniformly for large `t`, let

```text
M(sigma_0;t,C/L)
 =#{rho=beta+i*gamma:
       beta>=sigma_0,
       |gamma-t|<=C/L},
L=log t,                                            (4.1)
```

with multiplicity.  Then

```text
M(sigma_0;t,C/L)
 <=[(1-sigma_0)/2+o(1)]*L.                         (4.2)
```

#### Proof

Take

```text
sigma=1+u,       u=L^(-1/2).                       (4.3)
```

The completed logarithmic derivative gives, uniformly in this range,

```text
sum_rho (sigma-beta)/[(sigma-beta)^2+(t-gamma)^2]
 =L/2+Re[zeta'/zeta(sigma+i*t)]+O(1)
 <=L/2+O(1/u).                                     (4.4)
```

The last inequality follows from the absolutely convergent Dirichlet series

```text
|zeta'/zeta(sigma+i*t)|
 <=-zeta'/zeta(sigma)=O(1/u).                      (4.5)
```

For every zero counted by (4.1), put `x=sigma-beta`.  The classical
zero-free half-plane `beta<1` and the threshold give

```text
u<=x<=1+u-sigma_0,
|t-gamma|<=C/L=o(u).                               (4.6)
```

Since `x/(x^2+y^2)` is decreasing for `x>|y|`, each such zero contributes at
least

```text
(1+u-sigma_0)/[(1+u-sigma_0)^2+C^2/L^2]
 =(1+o(1))/(1-sigma_0).                            (4.7)
```

Combining (4.4) and (4.7) proves (4.2).  QED

For the proposed strip edge `sigma_0=.99`, this permits

```text
(0.005+o(1))*L                                     (4.8)
```

zeros in one microscopic cell.  The optimized screen has only four rows in
each such cell, so it does not approach this ceiling.  At the carrier
threshold

```text
sigma_0=1/2+alpha*d=.8234                           (4.9)
```

it permits `(0.0883+o(1))*L`.  Thus (4.2) improves the `0.10076 L`
endpoint allowance for a single cell, but still permits any
`O(L/log L)` growing-jet fixture near `sigma=.99`.

The cellwise statement is not the strongest consequence for a list spanning
a fixed ordinate interval.

### Theorem 4.2 (fixed-width reflected-pair Poisson cap)

Let `I` be an ordinate interval of fixed length `H`, and suppose `N_pair`
horizontal reflected pairs have ordinates in `I` and right-hand coordinates

```text
1/2+b_j,       0<b_0<=b_j<=b_1<1/2.               (4.10)
```

Put

```text
a_R=1/2-b_0,       a_L=1/2+b_1.                   (4.11)
```

Then for every fixed padding `s>0`,

```text
N_pair/L
 <=(H+2*s)
   /{2*sum_(a in {a_R,a_L})
       [atan((H+s)/a)+atan(s/a)]}
   +o(1).                                          (4.12)
```

#### Proof

Evaluate the completed logarithmic derivative on `Re z=1+L^(-1/2)`
and integrate its nonnegative zero Poisson sum over the interval obtained by
padding `I` by `s` at both ends.  The integrated right side is

```text
(H+2*s)*L/2+o(L).                                  (4.13)
```

For a pair at ordinate `gamma in I`, the right-member horizontal distance is
at most `a_R`, while the left-member distance is at most `a_L`.  The
integrated Poisson kernel decreases with the horizontal distance.  For
either upper distance `a`, its integral over the padded interval is
minimized when `gamma` is at an endpoint of `I`, and is at least

```text
atan((H+s)/a)+atan(s/a)+o(1).                      (4.14)
```

Both reflected zeros occur in the completed Poisson sum.  Summing (4.14)
over the two horizontal members and comparing with (4.13) proves (4.12).
QED

For the binomial screen,

```text
H=c*pi/d,       N_pair/L=2*c+o(1),
b_0=b_1=.49-o(1),       d=.66.                     (4.15)
```

Using `s=.003` in (4.12), or optimizing over `s`, gives the unique numerical
crossing

```text
c_pair=0.00465416454... .                           (4.16)
```

Hence an actual count-compatible member of the family satisfies

```text
c<=c_pair+o(1),
F_(.49,.66)(c)
 <=F_(.49,.66)(c_pair)
 =0.01118512309... .                                (4.17)
```

This is `0.0007148903...` below the original reserve
`E_0=0.0119000134...`.  The comparison uses both horizontal members of each
pair; omitting the far reflected member gives the slightly weaker crossing
`0.0048725925...`.

## 5. Distinct-cell repetitions cannot create a hidden fixed exponent

The fixed five-row fixture costs one extra local Schur factor beyond a
single representative.  Repeating it in `M=o(L)` **distinct** cells near the
target does not turn that local cost into a fixed power.

### Lemma 5.1 (distinct-cell entropy bound)

Let at most one extra factor be charged in each of `M` distinct phase cells
of width `2*pi/(dL)`, and let its real depth be at most `alpha`.  Then the
largest possible additional target potential satisfies

```text
S_extra
 <=M*log(L/M)+O_(alpha,d)(M+log L).                 (5.1)
```

In particular,

```text
M=o(L)       implies       S_extra=o(L).            (5.2)
```

#### Proof

The potential is maximized by taking the `M` cells nearest the target and
maximal real depth.  In the `k`-th nearest distinct cell,

```text
|delta_k|>=(c_d*k+O(1))/L                          (5.3)
```

after treating the finitely many cells meeting the target separately.  The
one-factor potential obeys

```text
V_alpha(delta_k)
 <=log(C_(alpha,d)*L/(k+1))+O(1).                  (5.4)
```

Summing and using `log(M!)=M log M-M+O(log M)` proves (5.1).  QED

For the often-proposed repetition count

```text
M=eta*L/log L,                                     (5.5)
```

the correct cost is

```text
S_extra
 =O[eta*L*log log L/log L]=o(L),                  (5.6)
```

not `eta*L`.  The mistake in the latter charge is to assign `log L` to every
cell; the `k`-th cell costs only `log(L/k)+O(1)`.

This closes one possible growing obstruction.  A fixed exponent can still
come from `Theta(L)` distinct cells, which is the global density problem, or
from growing multiplicity concentrated in one or a few cells.  The latter
requires the quantitative growing-jet theorem which remains open below.

## 6. An exact continuum annihilating every analytic jet

The fixed-order high-jet existence lemma has a useful exact source.

Fix `lambda_0>0`.  For `-pi<x<pi`, put

```text
h(x)=-lambda_0+(2/d)*log cos(x/2)-i*x/d.            (6.1)
```

### Theorem 6.1 (all-jet contour identity)

For every integer `k>=0`,

```text
integral_(-pi)^pi exp(-i*x)*h(x)^k dx=0.            (6.2)
```

#### Proof

Direct differentiation gives

```text
exp(-i*x)dx
 =i*d*exp[(d/2)*(h+lambda_0)]dh.                   (6.3)
```

The curve (6.1) runs from real part `-infinity` below the real axis to
`-lambda_0`, then back to real part `-infinity` above it.  Close it by the
vertical segment at `Re h=-R`.  The integrand

```text
exp(d*h/2)*h^k dh                                  (6.4)
```

is entire, and the closing segment is
`O(exp(-d*R/2)R^k)`.  Letting `R` tend to infinity proves (6.2).  QED

Equivalently, with `t=tan(x/2)`,

```text
h=-(2/d)*Log(1+i*t)-lambda_0,
exp(-i*x)dx=2*dt/(1+i*t)^2.                        (6.5)
```

The real and imaginary parts of (6.2) give a positive continuous dependence
among the real jet normals.  The Richter--Tchakaloff/Caratheodory theorem
therefore gives, for every **fixed** `r`, a positive atomic fixture with at
most `2r+3` points annihilating the complex moments through order `r`.

The qualification “fixed” is essential.  Its scaled depth is

```text
lambda(x)=lambda_0-(2/d)*log cos(x/2),              (6.6)
```

which tends to infinity at the endpoints.  The induced tail is of size
`exp(-d*lambda/2)`.  Neither abstract Tchakaloff nor (6.2) bounds the largest
quadrature node or the positive-spanning condition number as `r` grows.
Consequently the often-suggested choice `r asymp L/log L` has **not** been
promoted to a theorem.  Doing so requires a quantitative positive
quadrature for (6.2), with a depth profile compatible with Theorem 4.1 and
errors smaller than the claimed carrier.

## 7. Why covariance and Potapov rank do not lower the aggregate gate

Let a positive covariance on scalar packet states be

```text
Gamma=sum_k lambda_k*q_k*q_k^*,
lambda_k>=0,       sum_k lambda_k=1.                (7.1)
```

The selected positive row is a rank-one square.  In endpoint notation,

```text
Tr(K_+*Gamma)=sum_k lambda_k*|A_k+B_k|^2.           (7.2)
```

Therefore

```text
Tr(K_+*Gamma)=0
 implies A_k+B_k=0
 for every k with lambda_k>0.                       (7.3)
```

Every spectral component lies in the same scalar selected-positive kernel.
Let `H_zero` denote the **aggregate** selected-negative plus collateral
zero-side form.  If

```text
Tr(H_zero*Gamma)<=-K_0,                             (7.4)
```

then

```text
sum_k lambda_k*(q_k^*H_zero*q_k)<=-K_0,             (7.5)
```

so at least one scalar component satisfies

```text
q_k^*H_zero*q_k<=-K_0.                              (7.6)
```

Thus PSD rank cannot improve the optimum of the final linear aggregate
certificate.  It may make a system of row-by-row trace inequalities
feasible even though no one component satisfies every row separately, but
those rowwise inequalities are only a sufficient construction device.  The
rank-one component (7.6) already supplies the aggregate zero-side conclusion
needed by the explicit formula.

A scalar coefficient of a `2 x 2` Blaschke--Potapov product is itself a
scalar Schur function, so Theorems 2.1 and 6.1 apply to it unchanged.  Using
the full matrix as a physical direct-sum channel returns to (7.1)--(7.6).
There is therefore no operator-rank escape from the scalar aggregate gate.

## 8. Exact remaining theorem

The present evidence supports, but does not prove, the following budgeted
version rather than an exact one-row-per-cell rule:

> For every actual target-local list in the fixed band `alpha>=.49`, start
> from the centered Green/Poisson one-representative bill
> `0.298008745 L+o(L)` and construct a scalar Schur function satisfying all
> residual half-disk signs with total Pick/compact surcharge
> `kappa L+o(L)`, for some `kappa<0.025391255`; then transfer it to the two
> compact endpoint legs with no larger loss.

The conditional base bill and margin are proved in
[`ZETA23-GREEN-POISSON-DUAL-PICK-LEDGER-2026-08-12.md`](ZETA23-GREEN-POISSON-DUAL-PICK-LEDGER-2026-08-12.md).

The binomial screen shows that `kappa=0` cannot be inferred by simply
iterating fixed-cell estimates without a global theorem.  Its unrestricted
artificial maximum is `0.01893502...`, but the fixed-width reflected-pair
count reduces the actual-count-compatible maximum to `0.01118513...`.
This lies below even the old `0.01190001...` reserve and gives appreciable
room inside the improved companion margin.  It is not a universal upper
bound for arbitrary multirow lists.  The continuum identity identifies the
remaining potentially sharper obstruction, but its growing quantitative
realization is open.

## 9. Truth table

| assertion | verdict |
|---|---|
| a growing coarse-count-admissible half-disk list can force exponential Schur attenuation | **proved**, Theorem 2.1 |
| its exponent can be computed without a numerical SDP | **proved**, (2.9)--(2.12) |
| compact PW/Gabor states evade that upper bound | **no**, they form a subclass |
| the artificial optimizer (2.12) obeys the microscopic per-cell cap | **yes**; it has only four rows per cell |
| the artificial optimizer obeys the fixed-width reflected-pair cap | **no**, Theorem 4.2 |
| the actual-count-compatible binomial exponent exceeds the old `E_0` reserve | **no**; it is `0.01118513...` |
| it exceeds the improved `0.02539125...` conditional Green margin | **no** |
| the binomial list defeats the current `E_0` budget after its cell bill is charged | **not proved** |
| one microscopic deep cell contains at most `((1-sigma_0)/2+o(1))L` zeros | **proved**, Theorem 4.1 |
| `o(L)` fixed-order repetitions in distinct cells create a fixed loss | **no**, by Lemma 5.1 |
| there is a positive continuum dependence annihilating every fixed analytic jet | **proved**, Theorem 6.1 |
| it has a uniformly controlled `r asymp L/log L` finite quadrature | open |
| PSD covariance or Potapov rank beats the scalar aggregate optimum | **no**, by (7.2)--(7.6) |
| budgeted global compact half-disk transfer for actual zeta lists | open |
| uniform zero-free strip | not proved |
