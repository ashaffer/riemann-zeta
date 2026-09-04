# Off-the-wall sprint B: transport, scattering, control, SUSY, and RG

Status: **no fixed strip is proved**.  Two mechanisms were taken to exact
form and pressure-tested.  Conditional-slice positivity of the full theta
kernel is false numerically before modular-orbit integration, and an exact
divided-Turan representation plus Arb interval arithmetic rigorously
falsifies the stronger second-tail proposal as well.  Passive Maass--Selberg scattering
permits exactly the pure-outgoing zeta resonance that must be excluded.

Date: 2026-08-13.

## 1. Candidate census

```text
mechanism                         exact object                         outcome
conditional optimal transport    Fourier slices of the theta product false at first order
second-order convex order         twice-integrated slice tails        rigorously false at P=0,T=97.2
Maass--Selberg/passive scattering cusp flux of completed Eisenstein   pure-outgoing obstruction
cusp observability / FUP          cutoff Eisenstein cusp waves        compact observability fails
Toda/Hankel flow                  tilted theta moment determinants     positive only on real tilt
hyperbolic PDE                    subharmonic completed modulus        no directional sign
supersymmetric factorization      L_T=A_T^*A_T                         zero Witten index/cross term
topological spectral flow         Schur/de Branges negative index      crossing is the target zero
de Bruijn zero dynamics           heat-flow Calogero motion            generic rigidity false
modular renormalization           infinite odd-jet cancellation        possible, no invariant cone yet
```

The first two substantive candidates below were selected because they
produce identities for the **complete theta or Eisenstein object before any
zero-free assumption**.

## 2. Pressure test I: conditional theta transport

In the Rodgers--Tao normalization, put

```text
G_p(q)=Phi((p+q)/2)Phi((p-q)/2),
h_T(p)=integral_R G_p(q)exp(-i*T*q)dq.                    (2.1)
```

The exact full detector is

```text
Khat_(alpha,eta)(T)
 =integral_R sinh(alpha*p)sinh(eta*p) h_T(p)dp.           (2.2)
```

For fixed `p`, the normalized version of `G_p(q)dq` is the conditional law
of the difference of two independent theta variables given their sum `p`.
Thus the most direct optimal-transport proposal is:

```text
h_T(p)>=0 for every p,T.                                  (2.3)
```

Because the weight in (2.2) is nonnegative, (2.3) would immediately prove
the detector, without a zero formula or logarithmic derivative.

It is false.  At `p=0`, evenness gives the exact one-dimensional probe

```text
h_T(0)=4 integral_0^infinity Phi(v)^2 cos(2*T*v)dv.       (2.4)
```

Fifty-digit quadrature at `T=30` gives

```text
h_30(0)
 =-5.25533759053981345485990825256507663342... *10^(-7). (2.5)
```

The integrand scale at the cutoff `v=2` is about `3.4*10^(-8116)`.
The reproducible probe is
`results/probe_full_theta_slice_pd.py`.  This is a high-precision numerical
falsifier, not an interval certificate, but its scale is far from numerical
noise.  Pointwise conditional characteristic-function positivity is not the
missing theorem.

### 2.1 A second-order convex-order proposal

The failure of (2.3) suggests retaining modular compensation in `p`.  Define

```text
S_(1,T)(P)=integral_P^infinity h_T(p)dp,
S_(2,T)(P)=integral_P^infinity (p-P)h_T(p)dp.              (2.6)
```

The first tail is also signed: a double-precision scout gives
`S_(1,45)(0.175) about -1.72*10^(-12)`.  The second tail has a direct
two-variable form

```text
S_(2,T)(P)
 =2 double_integral_(u+v>=P)
      (u+v-P)Phi(u)Phi(v)cos(T(u-v))du dv.                 (2.7)
```

Here is an exact sufficient lemma which is not, on its face, a zero-free
statement:

> **Second-order modular convex-order lemma.**  For every real `T` and every
> `P>=0`, `S_(2,T)(P)>=0`.

Indeed, on `p>=0` let
`w(p)=sinh(alpha*p)sinh(eta*p)`.  Then

```text
w(0)=w'(0)=0,
w''(p)=(1/2)[(alpha+eta)^2 cosh((alpha+eta)p)
             -(alpha-eta)^2 cosh((alpha-eta)p)]>0.        (2.8)
```

Two integrations by parts give the exact identity

```text
integral_0^infinity w(p)h_T(p)dp
 =integral_0^infinity w''(P)S_(2,T)(P)dP.                 (2.9)
```

There are no suppressed endpoint terms in (2.9).  In detail,

```text
integral w*S_2''=[w*S_2']_0^infinity-[w'*S_2]_0^infinity
                  +integral w''*S_2.
```

The two terms at zero vanish because `w(0)=w'(0)=0`.  The theta kernel and
all its polynomial tails decrease faster than every fixed exponential,
whereas `w,w'` have only fixed exponential growth, so both terms at infinity
also vanish.

Both `h_T` and `w` are even, so the full detector (2.2) is twice either side
of (2.9).  Thus the lemma would prove the complete detector (in fact for
every positive `alpha,eta`, much more than the thin target).  The exact
representation below shows why this proposal is testable and supplies a
rigorous interval falsifier.  It is therefore a discarded
strong sufficient condition, not a surviving lemma.

### 2.2 Exact autocorrelation and Turan representations

The second tail does have an exact autocorrelation representation, but it
is **bilinear rather than Hermitian**, so it does not make the proposed sign
automatic.  Put

```text
f_T(u)=Phi(u)exp(-i*T*u),
Z(t)=integral_R Phi(u)exp(-i*t*u)du.
```

In this normalization `Z(t)=xi((1-i*t)/2)/4`, so the formula below is a
Turan identity for the actual completed zeta function, not for a model.

Evenness of `Phi` and the substitution `v=u-p` give

```text
h_T(p)=2 integral_R f_T(u)f_T(u-p)du.                    (2.10)
```

Consequently its `p`-Fourier transform is the exact Turan product

```text
Fourier_p[h_T](xi)=2*Z(T+xi)Z(T-xi).                    (2.10a)
```

More generally, for an integer `k>=1`, define

```text
S_(k,T)(P)=1/(k-1)! integral_P^infinity
              (p-P)^(k-1)h_T(p)dp.
```

Then, with `x_+=max(x,0)` (and the evident indicator convention when
`k=1`),

```text
S_(k,T)(P)=1/(k-1)! double_integral_R2
  (|u-v|-P)_+^(k-1) f_T(u)f_T(v)du dv.                  (2.11)
```

For `k=2` this becomes an exact divided-Turan formula:

```text
S_(2,T)(P)=2/pi integral_0^infinity cos(P*xi)/xi^2
 [Z(T)^2-Z(T+xi)Z(T-xi)]d xi.                           (2.12)
```

All constants in (2.12) use the Fourier convention in (2.1).  One quick
derivation is to write

```text
(|x|-P)_+=|x|-P+(P-|x|)_+,
Fourier[(P-|x|)_+](xi)=2(1-cos(P*xi))/xi^2,
```

and use the standard finite-part transform
`Fourier[|x|]=-2*Fp(1/xi^2)`.  The terms proportional to
`P*Z(T)^2` cancel exactly.  The integral in (2.12) is ordinary and absolutely
convergent: its bracket is `O(xi^2)` at zero and is
`Z(T)^2+o(1)` at infinity.

For the actual theta kernel, (2.12) gives the following reproducible
high-precision value:

```text
python3 results/probe_theta_tail_hierarchy.py \
  --verify-s2 97.2 0 --cutoff 115 --dps 60

S_(2,97.2)(0)
 =-4.2568787422346498289808946952651704240... *10^(-30). (2.12a)
```

A `cutoff=105,dps=50` run gives
`-4.2568785045283265...*10^(-30)`; changing both cutoff and precision moves
the answer by only `2.38*10^(-37)`.  A separate dense completed-xi cosine
transform gives `-4.25687874248...*10^(-30)`.  The removable value of the
integrand at `xi=0` is positive,
`Z'(T)^2-Z(T)Z''(T)=1.69196329284...*10^(-29)`, so the negative result is not
created by dividing an unresolved constant by `xi^2`.

The sign is in fact rigorous.  Running

```text
python3 results/certify_theta_s2_negative.py
```

uses Arb analytic quadrature on `10^(-8)<=xi<=200`, a Cauchy bound on the
removable origin segment, and a gamma-recurrence/Euler--Maclaurin bound on
the infinite product tail.  It returns

```text
-4.2626110089526610*10^(-30)
 < S_(2,97.2)(0)
 < -4.2511466914612062*10^(-30).                       (2.12b)
```

For the last estimate, recurrence gives
`|Gamma(1/4+iv)|<=Gamma(N+1/4)/|v|^N` with `N=40`, while the first
Euler--Maclaurin formula gives
`|zeta(1/2+it)|<=t+3`; the certified origin and tail errors are respectively
`4.408*10^(-33)` and `4.597*10^(-33)` before multiplication by `2/pi`.

Thus the proposed lemma is precisely the assertion that, for every `T`,
the cosine transform of

```text
[Z(T)^2-Z(T+xi)Z(T-xi)]/xi^2                            (2.13)
```

is nonnegative on the half-line.  Equivalently, the even function (2.13)
must be positive definite.  This is a useful exact reformulation, not a
positivity proof: the autocorrelation in (2.11) has no complex conjugate,
the cosine in (2.12) changes sign, and the interval certificate (2.12b)
falsifies the proposed sign rigorously.

Finally, the higher tails satisfy

```text
d/dP S_(k,T)=-S_(k-1,T)  (with S_(0,T)=h_T),
d^k/dP^k S_(k,T)=(-1)^k h_T.                            (2.14)
```

Repeated integration by parts is boundary-free only when
`w^(j)(0)=0` for `0<=j<k`.  The present weight has a zero of exactly order
two: `w''(0)=2*alpha*eta`.  Hence `k=2` is the last free step.  For example,
the `k=3` formula contains the additional endpoint
`2*alpha*eta*S_(3,T)(0)`; a higher-tail hierarchy cannot silently discard
it.

### 2.3 Exact boundary ledger and the next integer tail

The endpoint statement can be made completely explicit.  For every integer
`k>=1`, decay at infinity and repeated integration by parts give

```text
integral_0^infinity w(p)h_T(p)dp
 =sum_(j=0)^(k-1) w^(j)(0)S_(j+1,T)(0)
   +integral_0^infinity w^(k)(P)S_(k,T)(P)dP.             (2.15)
```

There are no alternating signs in the endpoint sum.  If
`c=alpha+eta` and `d=|alpha-eta|`, then the even derivatives of `w` are
one half of `c^j cosh(cP)-d^j cosh(dP)`, and the odd derivatives are one
half of `c^j sinh(cP)-d^j sinh(dP)`.  They are positive for `P>0`; at zero
the odd derivatives vanish and the even derivatives of order at least two
are positive.  Therefore

```text
S_(3,T)(P)>=0 for every P,T                              (2.16)
```

would still suffice, since its only endpoint is
`w''(0)S_(3,T)(0)>=0`.  For `k>=4`, however, one must additionally prove
all the odd boundary tails `S_(2m+1,T)(0)` that occur in (2.15).

Those boundary gates are classical Laguerre quantities.  If
`g_T(xi)=Z(T+xi)Z(T-xi)`, then

```text
S_(2m+1,T)(0)=(-1)^m g_T^(2m)(0)/(2m)!,
S_(3,T)(0)=Z'(T)^2-Z(T)Z''(T).                           (2.17)
```

(A convention in which `Z` is twice the transform multiplies the latter by
two.)  Also `S_3(P)=integral_P^infinity S_2(Q)dQ`.  Hence global positivity
of `S_2` would force the global first Laguerre inequality (2.17); it was an
RH-strength condition, not an easy strip lemma.  At the negative candidate
`T=97.2`, the endpoint itself remains positive:

```text
S_(3,97.2)(0)=1.69196329284415989...*10^(-29).           (2.18)
```

The exact integrated-Turan formula used to test the promoted tail is

```text
S_(3,T)(P)=S_(3,T)(0)
 -(2/pi)integral_0^infinity
   [Z(T)^2-Z(T+xi)Z(T-xi)]sin(P*xi)/xi^3 dxi.             (2.19)
```

High-precision scouts at `T=97.2` give positive values
`S_3(0.2)=1.7071660672...*10^(-29)`,
`S_3(0.8)=2.1993566418...*10^(-30)`, and
`S_3(1.0)=5.0807658647...*10^(-32)`.  These are not a global sign
certificate.  Thus `k=3` is the first integer tail not currently
falsified, but it imports the first Laguerre gate explicitly.

### 2.4 Fractional tails below two are stronger, not weaker

For `1<nu<2`, set

```text
S_(nu,T)(P)=1/Gamma(nu) integral_P^infinity
               (p-P)^(nu-1)h_T(p)dp.                    (2.20)
```

Let `D_(0+)^nu` denote the left Riemann--Liouville derivative.  Since
`w(0)=w'(0)=0`, fractional integration by parts has no endpoint term and
is exact:

```text
integral_0^infinity w*h_T
 =integral_0^infinity (D_(0+)^nu w)(P)S_(nu,T)(P)dP,
D_(0+)^nu w(P)
 =1/Gamma(2-nu) integral_0^P(P-x)^(1-nu)w''(x)dx >0.     (2.21)
```

Thus positivity of one fractional tail would suffice.  It cannot weaken
the failed `S_2` condition, because the right-sided fractional integrals
form a semigroup:

```text
S_(2,T)(P)=1/Gamma(2-nu) integral_P^infinity
              (Q-P)^(1-nu)S_(nu,T)(Q)dQ.                (2.22)
```

Therefore `S_nu>=0` would imply `S_2>=0`.  In particular, by the certified
negative value (2.12b), every `1<nu<2` must fail somewhere; taking a
critical fractional exponent cannot rescue the cone.  At the origin its
exact divided-Turan representation is

```text
S_(nu,T)(0)=2*sin(pi*(nu-1)/2)/pi integral_0^infinity
 [Z(T)^2-Z(T+xi)Z(T-xi)]/xi^nu dxi.                     (2.23)
```

### 2.5 Generic real-rootedness does not control the divided Turan sign

Laguerre--Polya theory gives the local signs in (2.17), but it does not give
(2.12), even if the inverse Fourier object is positive.  Take

```text
mu=(delta_(-2)+delta_(-1)+delta_1+delta_2)/4.
```

Its transform

```text
Z_mu(t)=(cos(t)+cos(2t))/2=cos(3t/2)cos(t/2)             (2.24)
```

has only real zeros and is positive definite.  Direct summation of its
sixteen atom pairs gives the rigorous counterexample

```text
S_(2,pi)(0)=-1/4.                                      (2.25)
```

Convolving `mu` with a sufficiently narrow Gaussian keeps the inverse
positive and smooth, multiplies (2.24) by an allowed Laguerre--Polya
Gaussian factor, and preserves the strict negative sign by continuity.
Thus positivity, positive definiteness, real-rootedness, and their
conjunction are all insufficient; a surviving `S_3` proof must use finer
theta/modular information.

Finally, the large-`p` theta saddle does localize the remaining search.
Uniformly for `tau=T*exp(-p)` in a fixed compact set,

```text
h_T(p)=2*pi^4 exp(8p-2*pi*exp(2p)-tau^2/(16*pi))
       [1+O_tau(exp(-2p))].                              (2.26)
```

Hence every tail is positive once
`P>=log(1+|T|)+O(1)`.  What remains for `S_3` is the expanding transition
region below that wedge, together with the Laguerre endpoint (2.17).

## 3. Pressure test II: inverse scattering and Maass--Selberg energy

For the modular surface, the completed Eisenstein constant term is

```text
u(y)=A(s)y^s+B(s)y^(1-s),
A(s)=Lambda(2s),       B(s)=Lambda(2s-1).                 (3.1)
```

Write `s=sigma+i*kappa`.  The exact cusp boundary flux at height `Y`, in
the standard constant-channel normalization, is

```text
F_Y=kappa[|A|^2 Y^(2sigma-1)-|B|^2 Y^(1-2sigma)]
    +(2sigma-1)Im[A conjugate(B)Y^(2i*kappa)].             (3.2)
```

On `sigma=1/2`, (3.2) is the familiar unitary scattering conservation law.
Off that line it is not positive.  If `zeta(2s)=0`, then `A(s)=0`, while
generically `B(s)!=0`, and

```text
F_Y=-kappa |B(s)|^2 Y^(1-2sigma).                         (3.3)
```

This is a legal pure-outgoing resonance with the adverse sign.  The positive
truncated Eisenstein norm in the Maass--Selberg relation contains (3.2) as a
boundary counterterm; after renormalization its finite part is not a positive
norm.  Consequently passivity, self-adjointness of the modular Laplacian,
and unitary-axis scattering do not exclude the desired denominator zero.
A bound of the form `|B|<=C|A|` in the target region would exclude it, but is
already a resonance-free-strip theorem for the global scattering scalar.

## 4. Arithmetic FUP and control encounter the same cusp channel

A compact-core observability inequality fails before arithmetic enters.
In logarithmic cusp coordinate `r=log y`, the constant horocycle mode is
`exp(i*kappa*r)` after the standard `y^(1/2)` conjugation.  For a smooth
cutoff `chi`, set

```text
v_(R,L)(r)=L^(-1/2) chi((r-R)/L)exp(i*kappa*r).            (4.1)
```

Its norm is bounded above and below independently of `R,L`, its compact-core
mass tends to zero as `R->infinity`, and

```text
||(Delta-(1/4+kappa^2))v_(R,L)||=O_kappa(1/L).            (4.2)
```

Thus waves can spend arbitrarily long time entirely in the parabolic cusp.
The constant cusp channel is not a porous fractal trapped set, so a standard
fractal-uncertainty or geometric-control gap cannot see it.  If the
observation is enlarged to the incoming cusp trace, a zeta resonance has
exactly zero incoming datum `A` and nonzero outgoing datum `B`; an
observability inequality controlling `B` by `A` is again the desired
arithmetic resonance gap.

An arithmetic transfer-operator/FUP theorem could still be new, but it must
prove a quantitative gap for this principal parabolic channel.  Ordinary
porosity, compact control, or continuous-spectrum estimates leave it intact.

## 5. Short pressure tests of the other imports

### 5.1 Toda and tilted moments

Up to a harmless normalization, write

```text
X(z)=integral_R Phi(u)exp(z*u)du.
```

For real `x`, exponential tilting gives the exact first Toda minor

```text
X(x)X''(x)-X'(x)^2=X(x)^2 Var_(mu_x)(u)>0.                (5.1)
```

At `x+iT`, the measure is complex and (5.1) loses its sign.  Near a zero
`rho`, `(log X)''(z)=-1/(z-rho)^2+O(1)`, whose real part has both signs.
The Toda hierarchy therefore supplies real-axis convexity, not the required
horizontal complex monotonicity.

### 5.2 Hyperbolic PDE and stress energy

For

```text
P(r,T)=|xi((1+r+iT)/2)|^2,
```

holomorphy gives the exact subharmonic identity

```text
(partial_r^2+partial_T^2)P
 =|xi'((1+r+iT)/2)|^2>=0.                                (5.2)
```

Away from zeros, `log P` is harmonic; distributionally its Laplacian places
positive point masses at zeros.  Neither fact determines the sign of
`partial_r P`.  Applying a source-free maximum principle in the desired
collar assumes that the offending point masses are absent.

### 5.3 Supersymmetry and index theory

The exact completion already factors as

```text
L_T=A_T^*A_T,
A_T=D_p^2-(1+iT)^2.                                      (5.3)
```

Because the coefficients are constant, `A_T A_T^*=A_T^*A_T`; the elementary
SUSY partner has zero Witten index.  The detector is the cross pairing
`<A_T w,A_T E*>`, not a norm.  A Darboux factorization using the Eisenstein
state itself has superpotential `-(log E*)'`, which is singular precisely at
the zeros/resonances to be excluded.

Likewise, the de Branges/Schur negative index is stable as the shift moves
only until a zero crosses the boundary.  Computing that no crossing occurs
is the strip statement, not a topologically protected consequence.

### 5.4 Heat-flow zero dynamics

The de Bruijn family satisfies `partial_lambda H=-partial_z^2 H`; simple
zeros obey the associated Calogero repulsion law.  Heat flow and even/real
symmetry alone impose no quantitative gap.  The exact polynomial solution

```text
H_lambda(z)=z^2+c-2lambda                              (5.4)
```

has an arbitrarily close conjugate imaginary pair before its collision and
two real zeros afterward.  Any useful rigidity must use the coefficient-
specific theta initial state, not merely integrability of the zero flow.

## 6. Ranking after pressure tests

1. **Arithmetic cusp observability.**  A relative incoming/outgoing estimate
   for the principal Eisenstein channel would prove a strip.  Generic FUP and
   control fail; only a new arithmetic version remains live.
2. **Third-tail/Laguerre modular cone.**  The second tail and every
   fractional tail below order two are rigorously ruled out.  The first
   promoted candidate is `S_3>=0`, with the unavoidable endpoint
   `Z'^2-ZZ''>=0`; use (2.19) and the wedge (2.26) to target only the
   transition region.
3. **Divided-Turan diagnostics.**  Use (2.12) to search for a weaker weighted
   transform matched directly to `w''`; do not require pointwise positivity
   of every second tail.
4. **Toda/canonical-system hierarchy.**  Continue only if a theta-specific
   complex minor inequality is found; real tilt convexity is insufficient.
5. **Generic SUSY, topology, or heat rigidity.**  Deprioritize: their exact
   invariants either vanish or count the offending zeros after the fact.

## 7. Truth boundary

The sprint produced the exact slice decomposition (2.1)--(2.2), a robust
numerical falsifier of first-order slice positivity and a rigorous interval
falsifier of the stronger
second-tail proposal, the exact bilinear-autocorrelation/divided-Turan form
(2.10)--(2.13), the exact integer/fractional endpoint audit (2.14)--(2.23),
the generic Laguerre--Polya counterexample (2.24)--(2.25), and the cusp
quasimode/control obstruction (4.1)--(4.2).  The sprint did not establish an arithmetic
observability estimate and did not prove a zero-free strip.
