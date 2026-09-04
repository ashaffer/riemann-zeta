# Growing-degree trigonometric and Stechkin zero repulsion: a uniform scale gate

Date: 2026-08-12.

Status: **no fixed zero-free strip is proved here.**  This report audits the
strongest automatic version of the classical positive-logarithmic-derivative
argument when all of the following are allowed to depend on the putative zero
height `T`:

* the degree and coefficients of the trigonometric polynomial;
* the exterior line `sigma=1+r`;
* a single Stechkin comparison, or a positive measure of right-shifted
  Stechkin comparisons;
* exact cancellation, or asymptotic cancellation, of the leading Gamma term.

The outcome is a degree-uniform obstruction.

```text
nonnegative Fourier weights, arbitrary degree N(T)          moving 1/log(T) scale only
sharp optimistic necessary condition                        epsilon log(T)<=3-2sqrt(2)+o(1)
signed Fourier weights can cancel the Gamma logarithm        YES
termwise sign for collateral zeros after that cancellation  NO
wrong-sign collateral mass in the fixed-gap viable range   >=(a_1/2)log(T)-O_epsilon(a_1)
multiple positive Stechkin subtractions                      covered
exact Gamma cancellation + nonzero paired-zero positivity   IMPOSSIBLE
near Gamma cancellation with a fixed-gap target              target shrinks proportionally
unconditional fixed zeta zero-free strip                     NOT PROVED
```

The result does not assert that a uniform strip is false.  It proves that
degree growth, coefficient optimization, and sign-safe Stechkin shifts do
not turn this explicit-formula mechanism into such a proof.  The only
remaining version uses a new signed correlation of the actual zeta zeros
across `T,2T,...`, conditioned on a near-one zero at `T`.

Related earlier gates are

* [`R88-ARCHIMEDEAN-CANCELLED-POSITIVITY-GATE.md`](R88-ARCHIMEDEAN-CANCELLED-POSITIVITY-GATE.md),
* [`R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md`](R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md), and
* [`R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md`](R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md).

The new point here is to put the growing harmonic degree and an arbitrary
positive Stechkin shift measure into one uniform set of inequalities.

## 1. Exact prime and zero ledgers

Write

```text
D(s)=-zeta'(s)/zeta(s),                 Re(s)>1.                 (1.1)
```

For

```text
P(theta)=a_0+sum_(1<=k<=N) a_k cos(k theta),                    (1.2)
```

absolute convergence gives

```text
a_0 D(sigma)+sum_(1<=k<=N) a_k Re D(sigma+i kT)
 =sum_(n>=2) Lambda(n)n^(-sigma)P(T log n).                     (1.3)
```

Denote the left side of (1.3) by `F_P(sigma,T)`.  Thus `P>=0` gives the
exact sign

```text
F_P(sigma,T)>=0.                                               (1.3a)
```

It is important that
`P>=0` does **not** imply `a_k>=0`.  Sections 2 and 3 treat these two cases
separately.

For a zero `rho=beta+i gamma`, put

```text
p_x(y)=x/(x^2+y^2),
Z_sigma(t)=sum_rho p_(sigma-beta)(t-gamma).                     (1.4)
```

In a fixed Hadamard normalization there is a real constant `C_xi` such
that

```text
Re D(sigma+it)=B_sigma(t)-Z_sigma(t),                            (1.5)

B_sigma(t)
 =Re[1/(sigma+it)+1/(sigma-1+it)]
  -1/2 log(pi)+1/2 Re psi((sigma+it)/2)-C_xi.                   (1.6)
```

Uniformly for `0<r<=1`, `sigma=1+r`, `k>=1`, and `T>=2`, standard
right-half-plane digamma estimates give

```text
B_(1+r)(kT)>=1/2 log T-C_0,                                    (1.7)
D(1+r)=1/r+O(1)                         as r->0.                (1.8)
```

The constant in (1.7) is independent of `k` and of the polynomial degree.
The omitted term `+(1/2)log k` is nonnegative and can only make the
background larger.

Assume that

```text
rho_0=1-epsilon+iT,                 0<epsilon<1/2,              (1.9)
```

is a zero.  Select one unit of its multiplicity; any further copies are
part of the collateral-zero sum below.  The selected functional-equation
quartet has real parts `1-epsilon`
and `epsilon` and ordinates `+T` and `-T`.  At the first harmonic its exact
aligned Poisson response is

```text
1/(r+epsilon)+1/(1+r-epsilon)+O(T^(-2)).                        (1.10)
```

If `0<r<=1`, the total response of this quartet at every other positive
integer harmonic is `O(T^(-2))`, uniformly after summing with nonnegative
weights:

```text
sum_(k>=1) a_k Q_k
 <=a_1[1/(r+epsilon)+1/(1+r-epsilon)]
   +C T^(-2)sum_(k>=1)a_k,             a_k>=0.                 (1.11)
```

Indeed, for `k!=1` every relevant ordinate separation is at least `T`,
and both horizontal widths are at most two.

## 2. Nonnegative harmonic coefficients: degree cannot improve the scale

Assume in this section that

```text
P>=0,             a_k>=0 (k>=1),             a_1>0,
A=sum_(k>=1)a_k.                                                  (2.1)
```

The Fourier coefficient bound and coefficient positivity give

```text
a_0>=a_1/2,                  A>=a_1.                            (2.2)
```

Write `Z_(1+r)(kT)=Q_k+R_k`, where `Q_k` is the selected quartet response
and `R_k>=0` is the response of every remaining zero, including any extra
multiplicity at the selected zero.  Keeping the zero-frequency Dirichlet
series exact, (1.5) gives

```text
F_P(1+r,T)
 =a_0D(1+r)+sum_(k>=1)a_k B_(1+r)(kT)
  -sum_(k>=1)a_k Q_k-sum_(k>=1)a_k R_k.
```

Because every `a_k` is nonnegative, deleting the last, nonpositive term is
a valid **upper** bound.  Define the resulting exact envelope by

```text
U_P(r,epsilon,T)
 =a_0D(1+r)+sum_(k>=1)a_k B_(1+r)(kT)
  -sum_(k>=1)a_k Q_k.
```

Combining (1.7)--(1.11) now gives

```text
F_P(1+r,T)<=U_P(r,epsilon,T),                                  (2.3)

U_P
 >=a_0[1/r-O(1)]+A[1/2 log T-O(1)]
   -a_1[1/(r+epsilon)+1/(1+r-epsilon)]-O(A/T^2).               (2.4)
```

All constants are independent of `N=N(T)`.  In particular, for every
fixed `epsilon>0`, the lower bound in (2.4), and hence the exact envelope
`U_P`, is positive for all sufficiently large `T`, after normalization by
`a_1`: the target is `O_epsilon(a_1)`, while
the high Gamma background is at least

```text
A[1/2 log T-O(1)]>=a_1[1/2 log T-O(1)].                         (2.5)
```

So a growing degree cannot produce a fixed-gap contradiction.  It cannot
even reduce the leading background-to-target ratio: every added
nonnegative harmonic adds a nonnegative `log k` correction.

The display was written for `0<r<=1`, the only range relevant to the sharp
moving optimization.  If `r>1`, both aligned target terms are bounded,
while the uniform lower bound `B_sigma(kT)>=1/2 log T-O(1)` still holds;
the fixed-gap conclusion is then even more immediate.

There is a sharper moving-scale consequence.

### Theorem 2.1 -- optimistic `1/log T` barrier

If the target-only deleted-zero envelope in (2.3) is negative along a
sequence `T->infinity`, then necessarily

```text
epsilon log T<=3-2sqrt(2)+o(1)=0.171572875...+o(1).              (2.6)
```

This is a necessary condition for this proof mechanism, not a claimed
zero-free-region constant.

#### Proof

First, (2.5) and (1.10) force

```text
r+epsilon=O(1/log T).                                          (2.7)
```

Consequently `r->0`, and (1.8) is uniform on the only potentially viable
scale.  Divide by `a_1`, use (2.2), and discard the bounded reflected
target term.  Negativity of `U_P`, together with its lower bound (2.4),
requires

```text
1/(r+epsilon)-1/(2r)
 >=(1/2-o(1))log T.                                             (2.8)
```

For every `epsilon>0`, direct differentiation gives

```text
max_(r>0) [1/(r+epsilon)-1/(2r)]
 =(3-2sqrt(2))/(2 epsilon),                                    (2.9)
```

with the maximum at `r=(1+sqrt(2))epsilon`.  Equations (2.8)--(2.9)
prove (2.6).  QED.

The lower bounds `a_0/a_1>=1/2` and `A/a_1>=1` need not be simultaneously
sharp in the nonnegative-coefficient cone.  Using them simultaneously
makes (2.6) deliberately optimistic.  Any exact polynomial optimization
can only make the admissible constant smaller; it cannot change the
`1/log T` scale.

## 3. Signed Fourier coefficients: cancellation transfers to the zeros

One can cancel the leading high-ordinate Gamma term by allowing signed
Fourier coefficients while retaining `P>=0`.  The elementary example

```text
P(theta)=2+cos(theta)-cos(2theta)>=0                            (3.1)
```

has `a_1>0` and

```text
sum_(k>=1)a_k=0.                                                (3.2)
```

For a general conductor-cancelled polynomial, put

```text
B_+=sum_(a_k>0,k>=1)a_k,
B_-=sum_(a_k<0,k>=1)|a_k|.                                     (3.3)
```

Then (3.2) implies the exact coefficient debt

```text
B_+=B_->=a_1.                                                   (3.4)
```

The apparent cancellation is therefore not a sign-safe zero-repulsion
argument.  From (1.5), the zero aggregate at every negative harmonic
satisfies, for fixed `sigma>1`,

```text
Z_sigma(kT)>=1/2 log T-C_sigma,                 k>=1.           (3.5)
```

This follows directly from (1.5), the uniform digamma bound, and
`|D(sigma+it)|<=D(sigma)`.  Hence the wrong-sign zero contribution at the
negative harmonics obeys

```text
sum_(a_k<0)|a_k|Z_sigma(kT)
 >=B_-[1/2 log T-C_sigma]
 >=a_1[1/2 log T-C_sigma].                                     (3.6)
```

No upper bound on `N(T)` occurs in (3.6).  Removing the target quartet
changes the negative-harmonic ledger only by `O(B_-/T^2)`, because a
negative harmonic cannot be `k=1`.

The constant `C_sigma` in this standalone estimate is not uniform as
`sigma` approaches the pole at one.  Thus (3.6) by itself is a fixed-line
statement, not a uniform moving-`r` estimate.  This causes no gap in the
fixed-`epsilon` conclusion: Section 5, including the case `nu=0`, proves
that any ledger capable of beating the zero-frequency pole must satisfy
(5.3), which keeps `r` a positive distance from zero depending on
`epsilon`; (3.6) then has the asserted `O_epsilon(a_1)` error.  Without
that pole-viability step, the shorter `O(a_1)` claim would be unjustified.

Thus signed coefficients can cancel the explicit Gamma sum, but only by
creating harmonics at which the ordinary zeta-zero bulk has the opposite
sign and, in the fixed-gap viable range just specified, size at least
`(a_1/2)log T-O_epsilon(a_1)`.  A marginal zero-density
estimate cannot remove this term: it is supplied by the full critical-strip
zero density, even if every collateral zero is put on the critical line.

This is not an absolute impossibility theorem for every signed use of
(1.3).  It identifies the exact missing assertion.  One would need a
target-conditioned, signed estimate across all dilates, schematically

```text
sum_(rho outside target quartet) sum_(k>=1)
 a_k p_(sigma-beta)(kT-gamma)>=-O_epsilon(a_1),                 (3.7)
```

before separating positive and negative harmonics.  Neither positivity nor
ordinary zero density proves (3.7).

## 4. A positive measure of Stechkin shifts

The preceding conclusion survives optimization of the horizontal
comparison.  The natural multi-shift Stechkin class is the following.
Let `nu=nu_T` be any finite positive measure on `[0,infinity)` with

```text
kappa=nu([0,infinity))<=1,
C=1-kappa,                                                       (4.1)
```

and define

```text
mathcal D_nu(s)=D(s)-integral D(s+d)dnu(d),
H_nu(z)=1/z-integral 1/(z+d)dnu(d).                             (4.2)
```

Its prime multiplier is

```text
q_nu(u)=1-integral e^(-du)dnu(d)>=1-kappa=C>=0.                (4.3)
```

Therefore, for every `P>=0`, including polynomials with signed Fourier
coefficients,

```text
a_0 mathcal D_nu(sigma)
 +sum_(k>=1)a_k Re mathcal D_nu(sigma+i kT)
 =sum_(n>=2)Lambda(n)n^(-sigma)q_nu(log n)P(T log n)>=0.        (4.4)
```

This includes the affine comparison

```text
H(z)=1/z-kappa/(z+d)                                           (4.5)
```

as a point mass, and permits the number and locations of shifts to grow
arbitrarily with `T`.

For a functional zero pair with horizontal widths

```text
a=sigma-beta,             b=sigma-(1-beta),
a+b=2sigma-1=1+2r=:S,                                           (4.6)
```

the paired real kernel is

```text
G_beta(y)=Re H_nu(a+iy)+Re H_nu(b+iy).                         (4.7)
```

Assume that the proof wants to discard every collateral functional pair
termwise, so that

```text
G_beta(y)>=0 for every beta in [0,1] and every real y.          (4.8)
```

The following two constraints are exact.

### Lemma 4.1 -- vertical mass and tail moment

Let

```text
m_1=integral d dnu(d),                                         (4.9)
```

where finiteness will follow from (4.8).  Then

```text
integral_R G_beta(y)dy=2pi C,                                  (4.10)
m_1<=CS/2.                                                      (4.11)
```

Consequently, exact Gamma cancellation `C=0` is compatible with (4.8)
only for the zero operator: `nu` has mass one at `d=0` and `H_nu=0`.

#### Proof

Every resolvent Poisson kernel has integral `pi`; (4.10) follows by
linearity.  A nonzero nonnegative kernel has positive integral, so `C>0`.
If `C=0`, a nonnegative kernel of zero integral is identically zero; the
Fourier identity below then gives `q_nu=0`, hence `nu` is the unit mass at
zero and the operator is zero.  We may therefore suppose `C>0`.
Moreover, with `Fourier[p_x](u)=pi e^(-x|u|)`, one has

```text
Fourier[G_beta](u)
 =pi q_nu(|u|)[e^(-a|u|)+e^(-b|u|)].                           (4.12)
```

Because `G_beta>=0`, its Fourier transform has modulus at most its value
at zero, namely `2pi C`.  Since `q_nu>=0`, division in (4.12) gives, as
`u` decreases to zero,

```text
q_nu(u)
 <=2C/[e^(-au)+e^(-bu)]
 =C[1+(S/2)u+O(u^2)].
```

On the other hand, monotone convergence gives

```text
[q_nu(u)-C]/u
 =integral [(1-e^(-du))/u]dnu(d) -> integral d dnu(d).
```

This proves both finiteness of `m_1` and (4.11), without assuming any
higher shift moment.  QED.

The same mass identity holds for an arbitrary finite signed radial
combination

```text
H(z)=sum_j c_j/(z+d_j):
integral_R G_beta(y)dy=2pi sum_j c_j.                           (4.13)
```

Thus exact leading-Gamma cancellation is incompatible with a nonzero
globally one-sided pair kernel in the full finite-shift class, even when
the prime multiplier `sum_j c_j e^(-d_j u)` happens to be nonnegative.
The positive-measure class (4.2) additionally supplies the quantitative
moment bound below.

There is also a quantitative target bound which remains valid for the full
finite signed radial class.

### Lemma 4.1b -- universal endpoint-to-target convolution

Let `H(z)=sum_j c_j/(z+d_j)` with real coefficients and `d_j>=0`, put
`C=sum_j c_j`, and suppose the endpoint functional-pair kernel

```text
G_0(y)=Re H(r+iy)+Re H(r+1+iy)                                  (4.13a)
```

is nonnegative.  For `0<epsilon<=1/2`, define

```text
G_epsilon(y)
 =Re H(r+epsilon+iy)+Re H(r+1-epsilon+iy).                      (4.13b)
```

Then

```text
G_epsilon=G_0*mu_epsilon,
0<=G_epsilon(y)<=2pi C*csc(pi*epsilon),                         (4.13c)
```

where `mu_epsilon` is a probability density with Fourier transform

```text
mu_epsilon_hat(u)
 =[e^(-epsilon*abs(u))+e^(-(1-epsilon)*abs(u))]
   /[1+e^(-abs(u))]
 =cosh((1/2-epsilon)u)/cosh(u/2).                               (4.13d)
```

#### Proof

Writing `q(u)=sum_j c_j e^(-d_j*u)`, the Poisson-kernel Fourier formula
gives

```text
Fourier[G_epsilon](u)
 =pi*q(abs(u))*e^(-r*abs(u))
   [e^(-epsilon*abs(u))+e^(-(1-epsilon)*abs(u))],
Fourier[G_0](u)
 =pi*q(abs(u))*e^(-r*abs(u))[1+e^(-abs(u))].                    (4.13e)
```

The ratio in (4.13d) is positive definite.  More explicitly, its inverse
Fourier transform is

```text
mu_epsilon(y)
 =2*sin(pi*epsilon)*cosh(pi*y)
   /[cosh(2pi*y)-cos(2pi*epsilon)]>=0.                          (4.13f)
```

It has integral one and maximum
`mu_epsilon(0)=csc(pi*epsilon)`.  Equations (4.13d)--(4.13e) prove the
convolution identity.  Finally, (4.13) gives
`integral G_0=2pi C`; convolving the nonnegative `G_0` with
`mu_epsilon` proves (4.13c).  QED.

Thus in **every** finite radial class with a sign-safe endpoint pair, a
fixed-gap target is `O_epsilon(C)`.  A target cannot stay nonzero while
the vertical/Gamma mass `C` tends to zero.  What needs the positive
Stechkin-measure hypothesis below is the stronger control of remote shifts
in the actual high-ordinate Gamma factor.

### Lemma 4.2 -- target and Gamma residual have the same factor

The identity

```text
H_nu(z)=C/z+integral d/[z(z+d)]dnu(d)                           (4.14)
```

and (4.11) imply, for `Re(z)=x>0`,

```text
|H_nu(z)|
 <=C[1/x+S/(2x^2)].                                            (4.15)
```

On the other hand, uniformly for every `sigma>1`, every `k>=1`, every
`T>=2`, and every `nu` satisfying (4.11), the nonzero-divisor background
obeys

```text
B_sigma(kT)-integral B_(sigma+d)(kT)dnu(d)
 >=C[1/2 log T-C_1].                                           (4.16)
```

The absolute constant `C_1` does not depend on the number, sizes, or
locations of the shifts.

#### Proof

Since `|z+d|>=|z|`, (4.14) and `m_1<=CS/2` give (4.15).  For (4.16), put
`R=|sigma+i kT|`.  For every `d>=0`, including `d` much larger than `T`,

```text
0<=log(|sigma+d+ikT|/R)<=log(1+d/R)<=d/R.
```

Thus the logarithmic part satisfies

```text
log R-integral log|sigma+d+i kT|dnu(d)
 =C log R-integral log(|sigma+d+i kT|/R)dnu(d)
 >=C log T-m_1/R
 >=C(log T-1),                                                  (4.17)
```

because `S<2sigma<=2R`.  The standard digamma remainder and the two
rational terms in (1.6) are Lipschitz in `sigma`, with size `O(1/R)` and
derivative `O(1/R^2)`.  Splitting each remainder as `C` times its value at
`sigma` plus its shift difference and using `m_1<=CS/2` bounds their total
by `O(C)`.  Constants in the Hadamard normalization are multiplied exactly
by `C`.  This proves (4.16).  QED.

For the target quartet, take

```text
x_1=r+epsilon,             x_2=1+r-epsilon.                    (4.18)
```

When `0<epsilon<=1/2`, (4.15) gives, uniformly in `r>=0`,

```text
sum_(j=1)^2 [1/x_j+S/(2x_j^2)]
 <=1/(2epsilon^2)+2/epsilon+4.                                 (4.19)
```

There are two ordinates in the quartet, so at **every** harmonic its total
absolute response is at most

```text
C K_epsilon,
K_epsilon=1/epsilon^2+4/epsilon+8.                             (4.20)
```

Combining (4.16) and (4.20), for nonnegative harmonic coefficients,

```text
sum_(k>=1)a_k[background_k-target_quartet_k]
 >=CA[1/2 log T-C_1-K_epsilon].                                (4.21)
```

The zero-frequency prime series `mathcal D_nu(sigma)` is nonnegative by
(4.3).  Therefore (4.21) is positive for all sufficiently large `T` when
`C>0`, for every fixed `epsilon`, uniformly in

```text
N(T), P_T, r(T), nu_T, kappa(T), and all shift locations.       (4.22)
```

When `C=0`, Lemma 4.1 has already shown that the operator is identically
zero, so it supplies no strict contradiction.  This is the promised
optimized-shift no-go.  Taking `kappa->1` makes `C->0`, but (4.11), (4.15),
and (4.16) show that the allowed shift moment, the retained target, and the
Gamma background all shrink by the same factor.  Sending comparison
shifts to infinity does not help: their logarithmic leverage is bounded by
their first moment in (4.17).

## 5. Signed harmonics on top of Stechkin pairing

Could one combine Section 3 with Section 4, cancelling the residual
`C log T` by choosing `sum a_k=0`?  Algebraically, yes.  Termwise zero
repulsion again fails.

The Laplace weight in (4.14) is

```text
q_nu(u)=C+integral (1-e^(-du))dnu(d),                           (5.1)
```

which is increasing.  By Lemma 4.1, `C=0` under pair positivity is the zero
operator; exclude that vacuous case below.  For real `x>0` (and hence for
the ratios below, `r>0`),

```text
H_nu(x)=integral_0^infinity e^(-xu)q_nu(u)du.                  (5.1a)
```

Negative covariance with the decreasing target ratios gives both the
one-pole and completed-pole bounds

```text
[H_nu(r+epsilon)+H_nu(r+1-epsilon)]/H_nu(r)
 <=r/(r+epsilon)+r/(r+1-epsilon),                              (5.2a)

[H_nu(r+epsilon)+H_nu(r+1-epsilon)]
 /[H_nu(r)+H_nu(r+1)]
 <=r(r+1)/[r(r+1)+epsilon(1-epsilon)].                         (5.2b)
```

For (5.2a), apply the reverse Chebyshev integral inequality to the
increasing function `q_nu(u)` and the decreasing function

```text
e^(-epsilon u)+e^(-(1-epsilon)u)
```

under the base weight `e^(-ru)du`.  For (5.2b), use the base weight
`e^(-ru)(1+e^(-u))du`; the relevant ratio is

```text
[e^(-epsilon u)+e^(-(1-epsilon)u)]/[1+e^(-u)]
 =cosh((1/2-epsilon)u)/cosh(u/2).                              (5.2c)
```

It is decreasing for `0<epsilon<=1/2`, since `x tanh(xu)` is increasing
in `x>=0`.  Evaluating the corresponding ratios with `q_nu` omitted gives
exactly the right sides of (5.2a)--(5.2b).  This verifies both inequality
directions.

Since every nonnegative trigonometric polynomial satisfies `a_1<=2a_0`,
even the weaker, optimistic one-pole ledger can beat the pole only if

```text
3r^2+r>epsilon(1-epsilon).                                     (5.3a)
```

The completed ledger imposes the stronger condition

```text
r(r+1)>epsilon(1-epsilon).                                     (5.3b)
```

Either condition keeps `r` a fixed positive distance from zero when
`epsilon` is fixed.
In that viable range, (4.3), (4.11), and `1-e^(-du)<=du` give

```text
0<=mathcal D_nu(1+r)
 <=C{D(1+r)+(S/2)[-D'(1+r)]}=O_epsilon(C).                     (5.4)
```

Indeed, this follows termwise from

```text
q_nu(u)<=C+m_1u<=C(1+Su/2).
```

At high harmonics, absolute convergence gives in addition

```text
|mathcal D_nu(1+r+ikT)|<=mathcal D_nu(1+r)=O_epsilon(C).
```

Combining this with (4.16), the paired zeta-zero aggregate at every high
harmonic consequently obeys

```text
Z_nu(kT)>=C[1/2 log T-O_epsilon(1)].                            (5.5)
```

If `sum a_k=0`, (3.4) still says `B_->=a_1`.  Hence the negative
harmonics carry the unavoidable wrong-sign term

```text
sum_(a_k<0)|a_k|Z_nu(kT)
 >=C a_1[1/2 log T-O_epsilon(1)].                              (5.6)
```

Meanwhile (4.15) bounds the fixed-gap target by `O_epsilon(Ca_1)`.
Thus neither `C->0`, growing harmonic degree, nor a growing number of
Stechkin shifts changes the logarithmic ratio.  A proof using signed
harmonics would still require the new conditional cross-dilate
cancellation (3.7), now for the paired kernel `H_nu`.

## 6. Uniformity and scope audit

The quantifiers used above are worth making explicit.

1. **Growing harmonic degree.**  All estimates are per unit of
   `A=sum |a_k|` or `sum a_k`; `kT>=T` and `log k>=0`.  There is no hidden
   `N/T` error, so `N(T)` may grow arbitrarily fast while remaining finite
   for each `T`.

2. **Coefficient size.**  No normalization besides `a_1>0` is assumed.
   Every error scales with the same coefficient mass as its main term.

3. **Pole terms.**  In Section 2 the pole is the positive
   `a_0D(1+r)` term and yields the sharp optimistic barrier (2.6).  In
   Section 4 the entire zero-frequency Stechkin prime series is kept exact
   and nonnegative.  Expanding it and discarding more zeros only makes the
   target-only upper envelope larger.

4. **Gamma factors.**  Equations (1.7) and (4.16) are lower bounds on the
   background that a target-only contradiction must beat.  Remote shifts
   are covered by `log(1+d/R)<=d/R` and the tail moment (4.11); no
   `d=o(T)` assumption is used in the multi-shift theorem.

5. **Other-zero signs.**  They may be discarded only when both the
   harmonic coefficient and the paired kernel have the correct sign.
   Signed harmonic cancellation violates the first condition; exact radial
   cancellation violates the second by (4.10).  Treating either failure by
   absolute values restores a term of order `log T`.

6. **Broader signed radial combinations.**  For an arbitrary finite signed
   shift combination `sum c_jD(s+d_j)`, (4.13) proves the exact
   mass/cancellation obstruction.  The quantitative moment and target
   bounds (4.11)--(4.21) use the natural Stechkin cone consisting of one
   base logarithmic derivative minus a positive measure of right shifts.
   Outside that cone, prime-node positivity alone does not impose a
   quantitative bound on the signed shift moments.  Such a proposal has not
   produced a sign-safe zero kernel; if it gives up sign safety, it lands in
   the same uncontrolled signed zero ledger rather than in a proof.

## 7. Verdict and search-space pruning

There is no uniform zero-free strip in this report.  What is proved is a
fairly broad fail-fast theorem for the classical route:

* with nonnegative harmonic coefficients, arbitrary degree growth remains
  on the `1/log T` scale, with the optimistic necessary constant
  `3-2sqrt(2)` in (2.6);
* cancelling the harmonic Gamma coefficient requires negative harmonics,
  and in the fixed-gap pole-viable range their collateral-zero mass is
  uniformly `>= (a_1/2)log T-O_epsilon(a_1)`;
* cancelling the Gamma coefficient radially gives a zero-mass kernel, which
  cannot be globally one-sided;
* every sign-safe positive Stechkin shift measure has a positive residual
  mass `C`, and both its fixed-gap target and its Gamma background carry the
  same factor `C`; degree and shift growth cannot change their ratio.

Accordingly, further searches over higher-degree positive polynomials,
larger Stechkin shift grids, or parameters with `kappa` closer to one are
not promising.  The only mathematically distinct continuation is a
coefficient-specific theorem about the **signed joint zeta-zero process**
at the dilated ordinates, conditional on the target zero.  That is new
arithmetic information, not another optimization of the classical
positivity argument.
