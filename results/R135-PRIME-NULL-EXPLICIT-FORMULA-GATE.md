# Prime-null explicit-formula carriers and the arithmetic-alias gate

Status: R135 gives an exact scalar prime-null, pole-null, and
archimedean-tail-null construction; a stationary-phase theorem for its
unavoidable arithmetic aliases; a general prime-mesh uncertainty bound; and
exact matrix/Blaschke positivity reductions.  The construction really does
remove every prime-power term.  It does **not** prove a fixed zero-free strip,
because the operation that installs those zeros creates remote carrier bands
whose signed zero contribution is larger than the target under absolute
estimation and is of the target scale under square-root estimation.  A
target-conditioned signed estimate across those aliases remains open.

This is a successor to R90 and R99, not a repetition of them.  R90 treated
weights in differentiated logarithmic-derivative formulas and quantified the
condition number of hiding negative Laplace mass between prime logarithms.
R99 exhibited the infinite-order null alias

```text
cos(2 pi exp(x))-1.
```

Here that alias is put into an admissible compactly supported Guinand--Weil
test, with the pole and leading Gamma tail removed exactly.  This exposes the
full price on the zero side.

```text
pointwise cancellation at every prime power                 EXACT
both zeta-pole evaluations h(+-i/2)                         EXACTLY ZERO
leading archimedean exp(-|x|/2) tail                        EXACTLY ZERO
hypothetical beta+iT response                               exp((beta-1/2)L)
arithmetic-alias real bandwidth                             exp(L)
alias L1 ledger on Re(rho)=1/2+a                            exp((a+1/2)L)
alias L2 ledger on Re(rho)=1/2+a                            exp(aL)
absolute-value closure for the exact alias                  IMPOSSIBLE
PSD cancellation inside one high carrier band              TRIVIAL ONLY
finite Blaschke improvement of an autocorrelation           IDENTICALLY NONE
target-conditioned signed alias estimate                    OPEN
fixed zero-free strip                                       NOT PROVED
nonexistence of a fixed strip                               NOT PROVED.       (1.1)
```

## 2. Explicit-formula convention

Let `g` be a smooth compactly supported complex function and put

```text
h(z)=integral_R g(x) exp(i z x) dx.                           (2.1)
```

The usual Hermitian hypothesis can be imposed by splitting `g` into its two
Hermitian components; the explicit formula extends to arbitrary complex `g`
by linearity.  We deliberately use that complexified form below to avoid
artificial interference between mirrored stationary points.  In the standard
Guinand--Weil normalization, the finite-prime contribution is

```text
-sum_(n>=2) Lambda(n)/sqrt(n)
       [g(log n)+g(-log n)],                                  (2.2)
```

and the two pole evaluations are `h(i/2)` and `h(-i/2)`, up to the harmless
choice of which one is written first.  A nontrivial zero

```text
rho=beta+i gamma
```

is sampled at

```text
z_rho=(rho-1/2)/i=gamma-i(beta-1/2).                          (2.3)
```

Only three features of the archimedean term are needed below.  Away from
`x=0`, its time-side kernel is, up to the fixed normalization,

```text
K_infty(x)=exp(-|x|/2)/(1-exp(-2|x|))
            =sum_(m>=0) exp(-(2m+1/2)|x|).                   (2.4)
```

The `g(0)` distribution is kept separately.  Thus a test supported away
from zero has archimedean size controlled by pairing `g` with (2.4).  All
claims below are invariant under the usual harmless `2 pi` changes of
Fourier convention.

Write

```text
S={+-log(p^k): p prime, k>=1}.                                (2.5)
```

If `g` vanishes on `S`, (2.2) is exactly zero.  There is no truncation and no
prime-number-theorem error.

## 3. An exact prime-, pole-, and leading-Gamma-null carrier

The first important result is positive: the desired algebraic cancellation
can be done.

Choose once and for all

```text
0<d<log(2),
w in C_c^infinity((-d,0)),       w>=0, w not identically zero,
B(x)=[1-cos(2 pi exp(x))]^2.                                 (3.1)
```

For `L>d+1`, define on the positive half-line

```text
b_L(x)=w(x-L)B(x),                                           (3.2)
```

extend it by zero to the negative half-line, and put

```text
f_(T,L)(x)=exp(-i T x)b_L(x),
D=-partial_x^2+1/4,
g_(T,L)=T^(-2)D f_(T,L).                                     (3.3)
```

This is a one-sided complex carrier.  Its Hermitian real and imaginary parts
are ordinary admissible tests, and any contradiction from the complex
identity would give a contradiction from at least one of those parts.

### Theorem 3.1 (exact arithmetic and pole nulling)

For every integer `n>=1`,

```text
g_(T,L)(+-log n)=0.                                          (3.4)
```

If `h_(T,L)` is the Fourier transform of `g_(T,L)`, then

```text
h_(T,L)(z)=T^(-2)(z^2+1/4) F_(T,L)(z),                       (3.5)
h_(T,L)(i/2)=h_(T,L)(-i/2)=0,                                (3.6)
```

where `F_(T,L)` is the Fourier transform of `f_(T,L)`.

#### Proof

At `x=log n`, `exp(x)=n`, so `1-cos(2 pi exp(x))` has a double
zero.  Its square `B` has a zero of order four.  Both `f` and its second
derivative therefore vanish there.  Every negative logarithm lies outside
the support.  Formula (3.5) is
Fourier differentiation, and (3.6) follows from its displayed factor.

Prime powers are only a subset of the integers used in (3.4).  Thus this is
stronger than required for (2.2).

### Theorem 3.2 (leading archimedean mode also cancels)

The archimedean pairing of `g_(T,L)` satisfies

```text
|A_infty(g_(T,L))|
 <=C_w T^(-2) exp[-5(L-d)/2].                                (3.7)
```

#### Proof

There is no `g(0)` term because the support is separated from zero.  Move
`D` by integration by parts from `f` to (2.4).  On `x>0`,

```text
D exp[-(2m+1/2)x]
 =[1/4-(2m+1/2)^2]exp[-(2m+1/2)x].                           (3.8)
```

The `m=0` coefficient is exactly zero.  The first surviving exponent is
`2+1/2=5/2`.  The compact amplitude is bounded uniformly in `L`, which
gives (3.7).

This cancellation is stronger than merely subtracting a `log T` asymptotic:
the slowest time-side Gamma mode is annihilated at the operator level.

## 4. The hypothetical zero is strongly visible

Suppose

```text
rho_0=beta+iT,
a=beta-1/2>0.                                                 (4.1)
```

Then (2.3) samples the test at `T-ia`.  From (3.3),

```text
F_(T,L)(T-ia)=integral_(L-d)^L b_L(x)exp(a x)dx.              (4.2)
```

The elementary Fourier expansion

```text
B(x)=3/2-2cos(2 pi exp(x))
          +(1/2)cos(4 pi exp(x))                             (4.3)
```

separates a nonoscillatory target term from two arithmetic chirps.  Repeated
nonstationary integration by parts on the fixed interval `(L-d,L)` gives,
for every fixed `N`,

```text
F_(T,L)(T-ia)
 =(3/2)c_w(a)exp(aL)
   +O_(w,a,N)(exp[(a-N)L]),                                  (4.4)

c_w(a)=integral_(-d)^0 w(y)exp(ay)dy>0.                      (4.5)
```

Consequently, uniformly when `T` tends to infinity,

```text
h_(T,L)(z_(rho_0))
 =(3/2)c_w(a)exp(aL)(1+o(1)).                                (4.6)
```

The functional-equation partner at the same ordinate is attenuated by
`exp(-aL)` for this one-sided test.  Therefore the exact explicit formula
becomes

```text
sum_rho h_(T,L)(z_rho)
 =O_w(T^(-2)exp(-5L/2)),                                     (4.7)
```

while the selected quartet contains a term of size `exp(aL)`.

Equation (4.7) is the useful new identity.  It says that, if the hypothetical
zero exists, the rest of the zero set must cancel the target.  The remaining
question is whether that cancellation can be ruled out.

## 5. Exact arithmetic aliases spend the gain

They cannot be ruled out by taking absolute values.  The reason is visible
directly in (4.3).

For a horizontal zero line `Re(rho)=1/2+a`, isolate one chirp and set

```text
J_(L,a)(u)
 =integral_(L-d)^L w(x-L)exp(ax)
    exp{i[2 pi exp(x)-u x]}dx.                               (5.1)
```

Its stationary point is

```text
x_u=log(u/(2 pi)),                                           (5.2)
```

whenever `u` lies in the corresponding band

```text
2 pi exp(L-d)<u<2 pi exp(L).                                 (5.3)
```

Shrinking the fixed support of `w` if necessary makes the first and second
chirp bands in (4.3) disjoint.  Uniform stationary phase then gives the
following exact scale law.

### Theorem 5.1 (alias norm ledger)

For fixed `a>=0`, there are constants depending only on `w,a` such that

```text
||J_(L,a)||_infinity          asyp exp[(a-1/2)L],
||J_(L,a)||_1                 asyp exp[(a+1/2)L],
||J_(L,a)||_2                 asyp exp[aL].                   (5.4)
```

#### Proof

Write `x=L+y` and `u=exp(L)v`.  The large parameter in the phase is
`exp(L)`, its second derivative at the stationary point is comparable with
`exp(L)`, and the amplitude is comparable with `exp(aL)`.  This gives the
first line of scale in (5.4).  The `u`-band has length comparable with
`exp(L)`, giving the `L1` scale.  The `L2` identity also follows exactly from
Plancherel:

```text
(1/(2 pi))integral_R |J_(L,a)(u)|^2du
 =integral_(L-d)^L w(x-L)^2exp(2ax)dx
 asyp exp(2aL).                                               (5.5)
```

This is the central conservation law.  The target in (4.6) has size
`exp(aL)`, exactly the `L2` size of one alias band.  Its `L1` size is larger
by `exp(L/2)`.

Take, for example,

```text
L=c log T,             0<c<1.                                (5.6)
```

Then the aliases stay in ordinates `T+O(T^c)`, so the harmless multiplier
`(z^2+1/4)/T^2` in (3.5) is `1+o(1)`.  A critical-line zero in the alias band
has stationary envelope `T^(-c/2)`, while the band contains on the zero-count
scale `T^c log T` ordinates.  An absolute ledger is therefore of scale

```text
T^(c/2)log T,                                               (5.7)
```

whereas a target with `beta=1-eta` has size

```text
T^[c(1/2-eta)].                                              (5.8)
```

Thus even the critical-line bulk loses a factor `T^(c eta)` under absolute
estimation.  Zeros as far right as the target have the still larger `L1`
ledger from (5.4).

This absolute obstruction can be made rigorous at the actual zero ordinates,
not only for a continuum envelope.  Choose a closed subband strictly inside
(5.3), disjoint from the second chirp band.  The one-sided carrier has exactly
one stationary point there, and uniform stationary phase gives

```text
|h_(T,L)(z_rho)|
 >=c exp[(beta-1)L]                                          (5.9)
```

for every zero in that subband with `beta>=1/2`; here
`beta-1=(beta-1/2)-1/2`.  The functional equation pairs every zero with one
at the same ordinate and real part at least `1/2`.  Riemann--von Mangoldt,
applied to a band of length comparable with `exp(L)=T^c`, therefore gives

```text
sum_(rho in alias subband)|h_(T,L)(z_rho)|
 >=c exp(L/2)log T.                                         (5.10)
```

The selected quartet is outside this remote band.  Consequently every proof
which majorizes the collateral sum by the sum of absolute values has already
lost against `exp(aL)` for every `a<1/2`.  The actual *signed* samples may
still cancel.  Such cancellation is exactly the theorem one would need;
zero density, unit-interval zero counts, and termwise bounds cannot provide
it.  Even an `L2` or square-root treatment has no power reserve against
collateral zeros on the same rightmost line.

The exponent `1/2` is not an accident.  Exact arithmetic nulling uses a
phase with local frequency `exp(x)`; stationary phase returns its square
root.  Replacing `exp(x)` by an integer-valued polynomial in `exp(x)` only
increases the sideband growth.

## 6. A general prime-mesh uncertainty theorem

The preceding alias is explicit but not claimed optimal.  There is also a
construction-independent lower bound for every stable pointwise-null
interpolant.

R90 imported the Baker--Harman--Pintz prime-gap theorem in the form

```text
Delta(X)<=C exp(-kappa X),            kappa=19/40,             (6.1)
```

where `Delta(X)` is the largest gap between consecutive prime-power
logarithms above `X`.  Prime logarithms alone suffice.
The input is Baker, Harman, and Pintz, *The difference between consecutive
primes, II*, Proc. London Math. Soc. 83 (2001), 532--562.

### Theorem 6.1 (prime-null Poincare uncertainty)

Let `I_L=(L-d,L)`, and let `u` be a scalar or finite-dimensional vector in
`H_0^1(I_L)` which vanishes at every prime-power logarithm in `I_L`.  For
fixed `a>=0`, put

```text
q(x)=exp(ax)u(x),
Q(v)=integral_(I_L)q(x)exp(i v x)dx.                          (6.2)
```

Then, for all sufficiently large `L`,

```text
||q'||_2 >=c exp(kappa L)||q||_2,                             (6.3)

[integral v^2||Q(v)||^2dv]/[integral ||Q(v)||^2dv]
 >=c^2 exp(2kappa L).                                        (6.4)
```

#### Proof

Partition `I_L` at its prime-log nodes.  Every component has length at most
`C exp(-kappa L)`; the endpoint components obey the same bound after the
standard one-sided use of (6.1).  The Dirichlet Poincare inequality on every
component gives (6.3) after summing.  Plancherel applied to `q'` gives (6.4).
The vector statement is obtained componentwise and summed.

At `L=c log T`, the root-mean-square carrier bandwidth is therefore at least

```text
T^(19c/40).                                                   (6.5)
```

This theorem does not forbid superoscillation: a very small amount of mass at
an enormous frequency can make a second moment large.  It proves the precise
dichotomy needed here.  A pointwise prime-null family is either genuinely
broad on the zero side or has a correspondingly unbounded interpolation
condition number.  Treating that condition number as `O(1)` silently assumes
away the arithmetic cost.

### A positive-definite model of the bandwidth cost

There is an exact Gram construction which makes the dimension visible.  For
the finite active set `S_L^+=S intersect (0,L]`, put

```text
P_L(x)=product_(q in S_L^+) cos^8(pi x/(2q)).                 (6.6)
```

Every factor is positive definite (its Fourier expansion has nonnegative
binomial coefficients), hence so is the product.  It has a zero of order
eight at every active prime logarithm.  Multiplying by a compactly supported
positive-definite envelope preserves both properties.  Applying `D^2`
preserves positive definiteness on the spectral side and leaves at least a
fourth-order zero at every prime logarithm, while installing pole zeros.

The spectral measure underlying (6.6) is a Rademacher sum.  Its variance is

```text
2 pi^2 sum_(q in S_L^+) q^(-2)
 asyp exp(L)/L^3,                                             (6.7)
```

because ordinary primes dominate.  Its natural bandwidth is therefore

```text
exp(L/2)/L^(3/2).                                             (6.8)
```

This is not a lower bound for every positive-definite construction.  It is a
fully explicit witness that matrix/Gram positivity can achieve exact nulling
only by moving the complexity into a large spectral frame.  Near the origin,
the same product has correlation length of order the reciprocal of (6.8), so
the nominal long aperture has collapsed.

## 7. Why PSD matrices do not cancel the Gamma ledger

Matrix positivity does not supply a hidden sign.

Let `H_T(t)` be an integrable Hermitian matrix-valued test with

```text
H_T(t)>=0                 for real t.                         (7.1)
```

The Guinand--Weil formula applies entrywise.  Pairing it with any constant
positive matrix `C` gives exactly the scalar nonnegative test

```text
h_C(t)=Tr[C H_T(t)].                                         (7.2)
```

Thus every linear PSD matrix argument scalarizes.  A determinant or log
determinant is nonlinear and is not the same explicit formula; its Fourier
coefficients introduce convolutions and mixed composites.

There is also a faithful-trace obstruction to Gamma cancellation.  If
`H_T` is concentrated in a band `|t-T|=o(T)`, Stirling's formula gives

```text
A_infty(H_T)
 =c_Gamma log T integral_R Tr H_T(t)dt
    +o(log T)integral_R Tr H_T(t)dt,                          (7.3)
```

with the positive convention constant `c_Gamma`.  But

```text
integral_R Tr H_T(t)dt=0
```

and (7.1) imply `H_T=0` almost everywhere.  Equivalently, the time-side
matrix at zero is

```text
G_T(0)=(1/(2 pi))integral H_T(t)dt>=0,                        (7.4)
```

and faithful trace zero forces it to vanish.

Therefore a nontrivial PSD scalar or matrix carrier cannot cancel its leading
Gamma mass *within the same translated high band*.  A separate PSD band in a
fixed low-frequency region, where the Gamma symbol is negative, can cancel
the numerical value.  Since that symbol is bounded on a compact region, its
required trace mass is

```text
M_low >=c M_high log T.                                      (7.5)
```

It therefore imports a `log T`-larger low-band zero, pole, and prime ledger;
this is a scalar compensation, not a matrix gain.  Signed combinations can
cancel the high-band moment directly, as Section 3 does, but then the
zero-side kernel is signed and Section 5's collateral ledger cannot be
discarded.  If pointwise PSD time data are proposed instead, the even simpler
fact applies:

```text
G(q)>=0 and Tr G(q)=0  ==>  G(q)=0.                           (7.6)
```

So trace cancellation at a prime does not preserve hidden matrix energy.

## 8. Finite Blaschke and de Branges lifts

Finite inner factors do not alter an autocorrelation test.  If

```text
F^*(z)=conjugate(F(conjugate(z))),
h(z)=F(z)F^*(z),                                              (8.1)
```

and `B` is a finite half-plane Blaschke product, then

```text
B^*(z)=1/B(z),
(BF)(BF)^*=FF^*.                                              (8.2)
```

The apparent poles are removable.  Thus a Blaschke phase changes the factor
but not the entire Weil test, on or off the real axis.  Multiplying `h`
itself by `B` instead produces a meromorphic or signed object unless separate
zeros cancel every pole; positivity has then been abandoned.

A finite de Branges Gram matrix has the same issue.  Every positive
scalarization is a sum of terms `F_jF_j^*`, so the entrywise explicit formula
reduces it to the scalar cone of Section 7.  A generalized de Branges kernel
with negative squares can certainly detect an off-line zero, but the negative
index is then the detector; it supplies no arithmetic theorem forcing that
index to vanish.

The universal Paley--Wiener evaluation bound makes the available amplification
explicit.  If `F` has time support in `[-L,L]`, then

```text
|F(T-ia)|^2
 <=[sinh(2aL)/(2 pi a)] ||F||_(L2(R))^2.                     (8.3)
```

This is just Cauchy--Schwarz in the time variable and is sharp.  Finite
Blaschke factors preserve the norm and, by (8.2), do not improve the paired
autocorrelation response.  Prime-null interpolation must therefore pay its
bandwidth or condition number in addition to, not instead of, the ordinary
`exp(aL)` Paley--Wiener gain.

Finally, a finite-type canonical product cannot install zeros at every prime
logarithm.  There are `asymp exp(L)/L` such points below `L`, while a
Cartwright function of fixed exponential type has only linearly many real
zeros.  A height-dependent finite product needs degree at least the number of
active conditions, or else a superoscillatory norm.  This is the same
interpolation cost as R90, now seen on the Weil-test side.

## 9. Aggregate signed cancellation is a different, still-open gate

One can ask only for the weighted sum (2.2) to vanish, rather than every
sample.  Algebraically this is easy: it is one linear condition.  It does not
retain positivity.

Define the prime functional

```text
P(g)=sum_(n>=2) Lambda(n)/sqrt(n)
       [g(log n)+g(-log n)].                                  (9.1)
```

Given two tests `u,v` with `P(v)!=0`, the combination

```text
g=u-[P(u)/P(v)]v                                             (9.2)
```

has zero aggregate prime term.  The explicit formula is linear, so the target,
all collateral zeros, the poles, and the Gamma term acquire the identical
coefficient in (9.2).  A matrix presentation of (9.2) changes nothing after
scalarization.  Unless one has an independent sign or a bound for the
collateral combination, (9.2) is a projection of the identity, not an
exclusion theorem.

This observation separates two claims which should not be conflated:

```text
pointwise prime nulling       pays the uncertainty ledger in Sections 5--6;
aggregate signed nulling      is cheap but forfeits zero-side positivity. (9.3)
```

The second route is live only as a target-conditioned signed prime/zero
correlation theorem.

## 10. The exact remaining theorem

For the explicit carrier of Section 3, remove the selected functional-equation
quartet from (4.7) and write

```text
R_(T,L,rho_0)
 =sum_(rho not in quartet(rho_0)) h_(T,L)(z_rho).             (10.1)
```

The target quartet has a computable leading term

```text
M_(T,L,rho_0)=(3/2)c_w(beta-1/2)
               exp[(beta-1/2)L](1+o(1)),                    (10.2)
```

with the harmless convention-dependent multiplicity factor included in the
constant.  A contradiction would follow from any uniform estimate of the
correct sign such as

```text
Re R_(T,L,rho_0)>=-(1-epsilon_0)M_(T,L,rho_0)                (10.3)
```

for one fixed `epsilon_0>0`, with `L=c log T` and every putative
`beta>1-eta` in the claimed strip.

Theorem 5.1 proves exactly what (10.3) cannot be derived from:

* absolute values or marginal zero density;
* independent estimates for the central and chirped carrier bands;
* an unconditioned `L2` estimate when collateral zeros can lie on the same
  rightmost line;
* finite PSD matrix or inner-factor repackaging.

What could still prove (10.3) is a signed relation between the actual zeta
zeros in the chirp bands, conditional on the central ordinate being a
near-one zero.  On the prime side this is the same kind of coefficient-specific,
target-conditioned correlation left open in R88--R90.  The present report has
made its carrier and norm ledger explicit; it has not supplied that theorem.

## 11. Decision

This branch produced a genuine new cancellation mechanism, but not a strip.

1. Compact support, exact zeros at every prime-power logarithm, both pole
   moments, and the leading Gamma tail are simultaneously compatible.
2. The arithmetic null alias necessarily creates high-frequency spectral
   bands.  For the exact integer alias their `L1` cost is an extra
   `exp(L/2)`, while their `L2` cost is exactly the target scale.
3. Every stable pointwise-null interpolant has at least the
   Baker--Harman--Pintz bandwidth `exp(19L/40)`; escaping it means an
   explicitly unbounded superoscillation condition number.
4. PSD matrices cannot cancel the leading Gamma mass inside one high carrier
   band except trivially; a low-band compensation costs `Omega(log T)` extra
   mass.  Every linear matrix explicit formula scalarizes, and finite
   Blaschke phases leave an autocorrelation test identically unchanged.
5. Aggregate signed prime cancellation is cheap, but it simply transfers the
   unresolved sign to the collateral zero sum.

Accordingly the construction is worth retaining as an exact laboratory for
a future signed estimate.  It does not prove a fixed zero-free strip, and its
failure does not prove that no fixed zero-free strip exists.
