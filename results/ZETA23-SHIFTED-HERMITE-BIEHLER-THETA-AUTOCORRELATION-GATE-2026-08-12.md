# Shifted Hermite--Biehler theta-autocorrelation gate

Status: no fixed zero-free strip is proved.  The exact Riemann theta problem
does, however, collapse to one coefficient-specific positive-definiteness
lemma.  Modular inversion makes the relevant autocorrelation pointwise
positive, but does not make it positive definite.  Hankel total positivity
fails for the actual theta kernel already at order two, reverse heat flow has
no degree-uniform strip bound, and the termwise theta expansion reaches its
abscissa-of-convergence wall exactly at the desired shift.

Date: 2026-08-12.

## 1. Exact normalization

Use the Rodgers--Tao theta kernel

```text
Phi(u)=sum_(n>=1)
  [2*pi^2*n^4*exp(9u)-3*pi*n^2*exp(5u)]
  *exp[-pi*n^2*exp(4u)].                              (1.1)
```

Poisson summation gives `Phi(-u)=Phi(u)`.  If

```text
Psi(v)=2*Phi(v/2),
X(s)=xi(1/2+s),                                      (1.2)
```

then the exact bilateral Laplace representation is

```text
X(s)=integral_R Psi(v)exp(sv)dv.                     (1.3)
```

Indeed, direct Mellin integration first gives

```text
integral_R Phi(u)exp(su)du=xi((1+s)/2)/4.            (1.4)
```

The kernel `Psi` is positive, even, real analytic, and
double-exponentially decreasing.  No qualitative substitute for `Psi` is
used below.

## 2. The exact autocorrelation equivalence

Fix `a,y>0` and define

```text
K_(a,y)(q)
 :=integral_R
    Psi((p+q)/2) Psi((p-q)/2)
    sinh(a*p)sinh(y*p) dp.                           (2.1)
```

This is a positive, even, rapidly decreasing function of `q`: the two sinh
factors have the same sign, while both theta factors are positive.  The
following identity is exact.

### Theorem 2.1 (theta autocorrelation identity)

For every real `t`,

```text
|X(a+y-i*t)|^2-|X(a-y-i*t)|^2
   =integral_R K_(a,y)(q)cos(t*q)dq.                 (2.2)
```

#### Proof

Writing `p=u+v` and `q=u-v`, expansion of the two modulus squares gives

```text
2*double_integral
 Psi(u)Psi(v)exp(a*p)sinh(y*p)cos(t*q) du dv.        (2.3)
```

Average (2.3) with its image under `(u,v)->(-u,-v)`.  Evenness of `Psi`
replaces `exp(a*p)sinh(y*p)` by
`sinh(a*p)sinh(y*p)`.  The Jacobian `du dv=(1/2)dp dq`
then gives (2.2).  QED.

Here and below the Fourier convention is
`Khat(t)=integral_R K(q)exp(i*t*q)dq`.  Since `K_(a,y)` is even, this is
the cosine transform in (2.2).  Thus the averaging factor `2` and the
Jacobian `1/2` cancel exactly; there is no hidden `2*pi` normalization in
(2.2).

Now put

```text
E_a(z)=X(a-i*z).
```

Reality and the functional equation give

```text
E_a#(z)=X(a+i*z)=X(-a-i*z).                          (2.4)
```

For `z=t+i*y`, the Hermite--Biehler inequality is therefore precisely the
strict positivity of the left side of (2.2).  Consequently:

### Corollary 2.2 (one exact live lemma)

For a fixed `0<a<1/2`, the following three statements are equivalent.

1. `E_a` satisfies the strict Hermite--Biehler inequality in the open upper
   half-plane.
2. For every `y>0`, the Fourier transform of `K_(a,y)` is strictly positive
   on the real line.
3. For every `y>0`, `K_(a,y)` is positive definite, with no real frequency
   at which its Fourier density vanishes.

Each of these statements implies

```text
every zero of xi(1/2+s) has abs(Re(s))<=a.            (2.5)
```

Conversely, if all zeros have `abs(Re(s))<=a_0`, then the three statements
hold for every `a` with `a_0<a<1/2` (and in fact for every `a>a_0`).  Hence
the following **existential** statements are equivalent:

```text
there is a uniform zero-free strip with half-width <1/2;
there is an a<1/2 for which E_a is Hermite--Biehler;
there is an a<1/2 for which every K_(a,y) has strictly
positive Fourier density.                            (2.6)
```

The epsilon in the converse is intentional.  Suzuki's shifted-xi theorem
states the zero-free/inner equivalence with `Theta_a` inner for every shift
strictly larger than the asserted zero bound.  At the exact extremal shift,
real boundary zeros or zeros approaching the boundary require a separate
limiting convention.  No equality-at-the-supremum assertion is used here.

Thus the target `Re(rho)<=0.99` follows from the explicit sufficient
statement

```text
K_(49/100,y) is strictly positive definite for every y>0,  (2.7)
with strictly positive Fourier density.
```

There is a useful compact reduction in the displacement parameter.  Formula
(2.1) is symmetric in `a,y`.  If `y>1/2`, the classical critical strip,
together with Suzuki's Proposition 1.2 at `omega_0=1/2`, says that
`Theta_y=E_y#/E_y` is meromorphic inner.  It is nonconstant, so `E_y`
satisfies the strict Hermite--Biehler inequality.  Hence (2.2), with `a,y`
interchanged, is strictly positive.  It is therefore enough in (2.7), and
for every other `a<1/2`, to prove

```text
0<y<=1/2.                                             (2.8)
```

This is a genuine narrowing: the whole surviving Fourier route is one
two-parameter family of positive-definiteness statements on a compact
`y`-interval.  Pointwise positivity of `K_(a,y)` is not enough.  A positive
function can have a Fourier transform of either sign.

The diagonal of the de Branges kernel is exactly

```text
K_Ea(z,z)
 =[|X(a+y-i*t)|^2-|X(a-y-i*t)|^2]/(4*pi*y),          (2.9)
```

so (2.1) is also an explicit theta formula for the diagonal Pick defect.
Once the scalar Hermite--Biehler inequality holds throughout the upper half
plane, the full Pick-kernel positivity follows from the Schur theorem.

No finite-exponential-type hypothesis is being smuggled into this step.
The forward implication used for the strip is elementary: if `E_a` vanished
at an upper-half-plane point, the strict modulus inequality would be
impossible there.  Reflection then gives both sides of (2.5).  For the
converse with `a>a_0`, the needed bounded-type/inner conclusion is precisely
Suzuki's Proposition 1.2 for the shifted-xi quotient, not a generic claim
about order-one entire functions.  Real zeros of `E_a` cause no defect in the
open-half-plane inequality; when forming a de Branges space they may
equivalently be removed as common real factors of `E_a` and `E_a#`.

## 3. A Wronskian is only the infinitesimal shadow

Let

```text
K_a^(1)(q)
 :=integral_R p*sinh(a*p)
    Psi((p+q)/2)Psi((p-q)/2) dp.                    (3.1)
```

Dividing (2.2) by `y` and taking `y->0+` gives

```text
integral_R K_a^(1)(q)cos(t*q)dq
 =4*Re[X'(a-i*t)conj(X(a-i*t))].                    (3.2)
```

Away from a zero, division by `4|X|^2` gives the familiar boundary phase
density `Re X'/X`.  This is a necessary consequence of (2.2), but a scalar
Wronskian sign on the boundary is not by itself equivalent to the full
Hermite--Biehler inequality.  For example,

```text
E(z)=(z-i)(z+2i)^3
```

has an upper-half-plane zero, while on the real line

```text
-Im E'(x)/E(x)
 =-1/(x^2+1)+6/(x^2+4)>0.                           (3.3)
```

Thus any proposed “equivalent Wronskian proof” must supply the missing
zero-free/Schur input or prove the full interior modulus gap (2.2).  Checking
only (3.2) can miss upper-half-plane zeros masked by lower-half-plane zeros.

## 4. Hankel total positivity fails for the actual theta coefficients

Tilting does not repair the most natural Hankel-total-positivity proposal.
Put

```text
f_a(v)=exp(a*v)Psi(v).
```

For the Hankel kernel `f_a(x+y)`, order-two total nonnegativity near the
origin would require

```text
f_a(0)f_a''(0)-f_a'(0)^2>=0.                        (4.1)
```

The exponential tilt cancels from this logarithmic-curvature determinant.
Since `Psi` is even,

```text
f_a(0)f_a''(0)-f_a'(0)^2=Psi(0)Psi''(0).            (4.2)
```

For the exact series (1.1), write `A_n=pi*n^2`.  Twice differentiating at
zero gives

```text
Phi''(0)=sum_(n>=1)
 A_n*(32*A_n^3-224*A_n^2+330*A_n-75)*exp(-A_n).     (4.3)
```

Outward-rounded Arb evaluation of `n<=11`, followed by an elementary
positive tail bound, gives

```text
-33.461001549407 < Phi''(0) < -33.461001549406,      (4.4)
  0.446696900467 < Phi(0)   <  0.446696900468.
```

For completeness, for `n>=12` the summand in (4.3) is positive and is at
most

```text
35*(pi*n^2)^4*exp(-pi*n^2).
```

Successive majorants have ratio less than
`(13/12)^8 exp(-25*pi)`, and the whole omitted tail is less than
`10^(-184)`.  Hence (4.4) is a rigorous sign certificate, not a floating
point scout.  Scaling from `Phi` to `Psi` preserves the sign, and (4.2) is
strictly negative.

Equivalently, for small `h>0`,

```text
det [[f_a(0),f_a(h)],
     [f_a(h),f_a(2h)]]
 =h^2[Psi(0)Psi''(0)]+O(h^3)<0.                    (4.5)
```

Therefore the exact shifted Riemann theta kernel is not Hankel `TP_2`, for
any shift `a`.  Translation `PF_infinity` was already impossible because
its Fourier transform has known zeros; (4.5) closes the distinct Hankel
escape at its first nontrivial determinant.

This does not refute positive definiteness of the autocorrelations (2.1).
It proves that such positive definiteness cannot be imported from Hankel
total positivity of the one-variable shifted theta density.

## 5. What modular inversion does, and where it stops

The exact coefficient wall can be seen before taking any estimates.  Let
`Phi_n` denote the `n`th summand of (1.1).  For `Re(s)>-5`, direct Mellin
integration gives

```text
integral_R Phi_n(u)exp(su)du
 =(s-1)/8 * (pi*n^2)^(-(1+s)/4)
   *Gamma((5+s)/4).                                  (5.1)
```

Only for `Re(s)>1` can (5.1) be summed ordinarily over `n`; there it yields

```text
sum_n integral_R Phi_n(u)exp(su)du
 =xi((1+s)/2)/4.                                    (5.2)
```

For the centered shift `a`, the boundary value in (3.2) uses `Re(s)=2a`.
Every desired `a<1/2` therefore lies strictly beyond the termwise
theta-series convergence line.  Modular inversion is exactly what recombines
the divergent negative-`u` tails and analytically continues (5.2).

The same obstruction appears in the two-dimensional product entering
(2.1).  Before modular recompletion, the `(n,m)` block has the exact four
term pattern

```text
exp[-B_(n,m)(q) exp(2p)] *
 {+4*A_n^2*A_m^2 exp(9p)
  -6*A_n^2*A_m   exp(7p+2q)
  -6*A_n*A_m^2   exp(7p-2q)
  +9*A_n*A_m     exp(5p)},                          (5.3)

B_(n,m)(q)=A_n exp(2q)+A_m exp(-2q).
```

The signs are `+,-,-,+`; diagonal and swap-completed blocks do not provide
a positive Gram decomposition.  Integrating in `p` produces gamma factors
and a rectangular Epstein-lattice kernel, but its four separate lattice
sums are not the convergent modular object.  Two-dimensional Poisson
summation must mix all four derivative pieces and infinitely many lattice
pairs before the even, positive function (2.1) is recovered.

Thus modular inversion achieves two exact things:

1. it makes the full one-variable kernel even and cancels every odd boundary
   jet;
2. it makes the recompleted autocorrelation (2.1) pointwise positive.

It does **not** establish that (2.1) is positive definite.  A valid modular
breakthrough would have to turn the fully recompleted rectangular Epstein
kernel into a spectral sum of squares whose Fourier density is positive.
Calling the unreduced full lattice sum a “positive orbit” simply restates
(2.2).

## 6. Heat flow cannot be reversed with a uniform strip bound

Let

```text
H_tau(z)=integral_R exp(tau*u^2)Psi(u)exp(i*z*u)du,
X_tau(s)=integral_R exp(tau*u^2)Psi(u)exp(s*u)du,
```

so `H_tau(z)=X_tau(i*z)` and
`partial_tau H_tau=-partial_z^2 H_tau`.  Real-rootedness is known for
sufficiently large positive `tau`.  It is tempting to evolve back to zero
and hope for a strip depending only on `tau`.  No such degree-uniform theorem
is possible.

Take the real-rooted polynomial `P_N(z)=z^(2N)`.  Reversing heat by time
`tau>0` gives exactly

```text
exp(tau*partial_z^2)P_N(z)
 =(i*sqrt(tau))^(2N)
   H_(2N)(z/(2*i*sqrt(tau))),                       (6.1)
```

where `H_(2N)` is the physicists' Hermite polynomial.  Its roots are real,
and the sum of their squares is

```text
sum_j r_j^2=(2N)(2N-1)/2.                           (6.2)
```

Consequently (6.1) has a zero with imaginary part at least

```text
sqrt[2*tau*(2N-1)],                                 (6.3)
```

which tends to infinity with the degree.  Multiple roots in the starting
polynomial are inessential: a sufficiently small real-rooted perturbation
and continuity of polynomial zeros retain an arbitrarily large imaginary
root after reverse heat.

This explains why an unconditional upper bound for the de
Bruijn--Newman constant does not imply a fixed strip for `H_0`.  Any reverse
estimate must pay for the number or crowding of zeros.  A growing-degree
Jensen approximation has exactly the same problem: its necessary degree
grows with the height being resolved, and the worst reverse-heat width grows
like `sqrt(N*tau)` rather than staying fixed.

There is also no scalar maximum principle hiding here.  If

```text
F_tau(x,t)=|X_tau(x-i*t)|^2,
```

then direct differentiation gives the ultrahyperbolic equation

```text
partial_tau F_tau=(1/2)(partial_x^2-partial_t^2)F_tau. (6.4)
```

The Hermite--Biehler modulus gap obeys the same sign-indefinite evolution.
The theta heat equation alone therefore cannot propagate (2.2) backwards;
one again needs a nonlocal, coefficient-specific modular inequality.

## 7. Laguerre and growing-Jensen verdict

The standard first Laguerre inequality for the de Bruijn--Newman flow is the
Fourier positivity of another explicit positive convolution density.  The
shifted-strip version is (3.2).  Both are necessary shadows of a full
Hermite--Biehler theorem, but neither boundary scalar sign supplies the
interior Schur condition by itself.

Fixed-order Laguerre or Jensen inequalities cannot resolve a horizontal
displacement `a` at height `T`: in a centered Hadamard moment the angular
change is `a/T`, so the required order is at least proportional to `T/a`.
Allowing the order to grow removes that angular blindness but encounters the
degree loss (6.3), while origin-centered moments suppress the remote quartet
behind the lower zeros.  A useful growing-order theorem would therefore need
uniform, height-localized theta arithmetic; ordinary Jensen asymptotics do
not provide it.

## 8. Final verdict and the one live target

No explicit `a<1/2` has been certified.  The attempted routes have the
following exact outcomes.

- **Modular inversion:** indispensable, but it proves evenness and
  pointwise autocorrelation positivity, not positive definiteness.
- **Theta heat flow:** reverse strip control is false without a degree or
  zero-spacing cost, and its scalar PDE has no maximum principle.
- **Translation total positivity:** infinite order is impossible for the
  actual kernel; finite order controls the wrong coordinate.
- **Hankel total positivity:** actual-coefficient failure already at `TP_2`,
  by (4.2)--(4.5).
- **Laguerre/Wronskian tests:** necessary diagonals, not the full
  Hermite--Biehler condition.
- **Growing Jensen order:** it reaches the required angular resolution only
  after acquiring the nonuniform degree loss in (6.3).
- **Prime/theta arithmetic:** termwise positivity hits the exact Mellin wall
  `Re(s)=1`; below it, all four two-dimensional lattice pieces must be
  modularly recompleted together.

The surviving theorem is now sharply isolated:

> Prove, for one explicit `a<1/2` (in particular `a=49/100`), that the exact
> full-theta autocorrelation `K_(a,y)` in (2.1) is positive definite and has
> strictly positive Fourier density for every `0<y<=1/2`.

By Theorem 2.1 and Corollary 2.2, that statement immediately gives the fixed
zero-free strip.  A credible next attempt must produce a genuinely positive
spectral factorization of the **fully recompleted** two-dimensional theta
kernel; no one-variable shape property, finite theta truncation, reverse-heat
estimate, or scalar boundary Wronskian can substitute for it.

## References

- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17
  (1950), 197--226.
- B. Rodgers and T. Tao, *The de Bruijn--Newman constant is non-negative*,
  Forum Math. Pi 8 (2020), e6.
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the
  Riemann xi function, and a new upper bound for the de Bruijn--Newman
  constant*, Res. Math. Sci. 6 (2019), 31.
- M. Suzuki, *A canonical system of differential equations arising from the
  Riemann zeta-function*, arXiv:1204.1827.
