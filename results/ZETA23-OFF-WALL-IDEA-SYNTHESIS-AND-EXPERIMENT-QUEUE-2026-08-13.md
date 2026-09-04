# Off-the-wall idea synthesis and experiment queue

**Date:** 2026-08-13

**Status:** research synthesis; **no zero-free strip and no improved zero bound**

This note records what survived an intentionally high-variance search across
optimal experimental design, control, quantum ancillas, coding, determinantal
processes, optimal transport, scattering, and nonlinear filtering.  The point
is not to rename the same obstruction.  Every promoted idea below either gives
an exact new reduction, a reproducible falsifier, or a sharply stated
experiment with a kill condition.

## 1. The consolidated lesson: change the normalization or gain nothing

Five conservation laws now explain most of the failed exotic imports.

1. **Linear-lift conservation.**  Matrix, quantum, character, and auxiliary
   channel lifts compress through the final scalar state to the same
   projective/Wiener norm.  Orthogonality before scalar readout is not a gain.
2. **Conductor conservation.**  Tensor, product-code, and ordinary higher
   moment amplification introduce products of length `Y^k`.  The first new
   layer needs aperture at least `Y^2`, while the available aperture is only
   `Y^(50/33+o(1))`.
3. **Principal-mode conservation.**  Centering, differentiating, squaring, or
   passing to a complementary lossless channel can remove the troublesome
   scalar mode only by removing the target carrier or recreating the same mode
   in another channel.
4. **Positive-smoothing conservation.**  Replacing a signed Wigner detector by
   a positive Husimi spectrogram necessarily smooths conjugate variables.  The
   uncertainty principle ties height localization to a positive unpolarized
   carrier, while exact recovery is signed backward heat.
5. **Finite-head nonidentifiability.**  Within a functional-equation-symmetric
   exponential-polynomial countermodel, a prescribed zero quartet can be
   inserted above any finite von Mangoldt head without changing that head.
   Thus the finite head plus a zero label alone is nonidentifying: any
   zeta-specific candidate-conditioned algebra must also carry a nonlocal
   completion or approximate-functional-equation remainder.

This is why QSP, paraunitary control, generic noncommutative probability,
ordinary sieve circuits, compact-core scattering observability, and the first
two theta-transport cones do not close the problem.  They improve a norm or a
channel which is not the one appearing in the final scalar explicit formula.

The most promising remaining ideas are therefore those which alter the proof
technology without pretending to alter the scalar objective:

```text
actual-node adversarial design / effective resistance       exact gate; asymptotic prior unfavorable
fermionic (exterior-power) volume representation            exact; collapses to directional leverage
continuous Remez tracking of the sparse arithmetic design   kill-or-promote conjecture engine
oscillatory noncompact packets                               admissible; translation/interpolation closed
third theta tail / Laguerre transition cone                  survives numerically; endpoint-obstructed
fractional theta tails below order two                       closed by the tail semigroup law
Wigner/Husimi phase-space lift                               exact smoothed theorem; reverse localization open
warped-lattice FFT/wavelet compilation                       separated square-root ledger closed
generic SUSY/topological factorization                       zero index/cross pairing; closed
machine-discovered finite-head SOS                           overfits unless completion remainder retained
```

## 2. The strongest exact survivor: adversarial optimal design

On a finite legal frequency set let `A` be the `M x D` prime-log evaluation
matrix and let `b` be the carrier row.  The scalar extremal is

```text
E(A,b)=sup{|<b,h>| : A h=0, ||h||_1<=1}
      =inf_lambda ||b-A^*lambda||_infinity.                 (2.1)
```

For a probability design `w`, with `W=diag(w)`, define

```text
G_w=A W A^*,        g_w=A W b,        c_w=b^*Wb,
Delta(w)=c_w-g_w^*G_w^dagger g_w.                           (2.2)
```

The exact minimax identity proved in the companion report is

```text
E(A,b)^2=max_w Delta(w).                                    (2.3)
```

An optimizer uses at most `2M+1` frequencies in the complex problem and at
most `M+1` in the real-cosine problem.  Its residual equioscillates on that
support, and the optimal primal nuller is recovered directly from the design.

For the zeta strip program the missing theorem has become the concrete PSD
certificate

```text
there exists w_Y with
Delta(w_Y) >= Y^(-2*kappa+o(1)),    kappa<0.0180303234....  (2.4)
```

No zero occurs in (2.4).  This is a finite actual-prime-log harmonic-analysis
statement, not a reformulation which is already visibly equivalent to a
strip.  It is the best surviving place to seek genuinely new arithmetic
input.

### 2.1 Continuous full-aperture diagnostics

The semi-infinite real-cosine exchange problem was solved on the full legal
band `B=Y^(50/33)`, with width `.2` and `alpha=.49`:

| `Y` | prime-power nodes `M` | `E_Omega` | active atoms |
|---:|---:|---:|---:|
| 100 | 9 | .06842194 | 10 |
| 300 | 23 | .05541187 | 24 |
| 1000 | 61 | .04046958 | 62 |
| 3000 | 151 | .03157984 | 152 |

At `Y=3000`, the exchange discrepancy is `1.79e-6` relatively and the
prime-row residual is `2.30e-13`.
The median active frequency is `105746.8` in a band ending at `185509.2`.
Thus the design is saturated and macroscopically distributed; it is not a
small low-frequency cluster.

The local apparent power exponents are about `.23`--`.26`, but four floating
data points support no asymptotic inference.  Indeed, for
`Y=300,1000,3000`, the alternative diagnostic
`E_Omega*(log Y)^(5/3)` equals `1.009,1.014,1.011`, while
`E_Omega*sqrt(M)` rises `.266,.316,.388`.  The useful content is the stable
geometry: `M+1` active atoms, irregular signs, and full-band support.  The
right analytic object is the square
equioscillation/stationarity system, not a uniform-grid second moment.

### 2.2 What the optimizer is actually doing

The follow-up asymptotic audit identified the right scalar variable.  Split
the legal band into a low carrier region `L=[0,T]` and a high cancellation
region `H=[T,B]`, and let `C_(T,B)` be the least total variation of a low/high
signed measure which has low carrier one and whose prime-log evaluation
vector vanishes.  If

```text
epsilon_T=sup_(xi in H)|b(xi)|,
```

then the exact comparison is

```text
1/C_(T,B)-epsilon_T <= E_B <= 1/C_(T,B)+epsilon_T.          (2.5)
```

Thus, after taking `T` polynomial so that the target tail is negligible, a
subpower design is equivalent to the carrier-aware cancellation cost
`C_(T,B)=Y^(o(1))`.

The floating optimizers have a remarkably rigid architecture.  One low atom
at `xi` between about `6` and `8` supplies essentially 100 percent of the
carrier; the remaining `M` atoms cancel that atom's phase vector.  Their
cancellation costs `(1-w_0)/w_0` at `Y=100,300,1000,3000` are

```text
1.534, 1.917, 3.279, 4.280,
```

tracking `sqrt(M/log B)` within factors `1.18`--`1.36`.  The corresponding
random-polytope prior is

```text
E_B about sqrt(log(K/M)/M),                                (2.6)
```

not a subpower law.  This is a prior, not an actual-node upper theorem.
Conversely, normalized high-band Lebesgue measure gives an explicit legal
Gram design with directional leverage `L=q^*G_H^(-1)q` and carrier
`|b_0|/(1+sqrt(L))`; a frame estimate proves only the generic
`E_B >= c/sqrt(M)` scale.  The route remains live only for a targeted attempt
to find a carrier direction with subpower leverage.  Extending the present
floating fit without such a symbolic direction is not progress.  See
`ZETA23-ACTUAL-NODE-ADVERSARIAL-DESIGN-ASYMPTOTIC-AUDIT-2026-08-13.md`.

## 3. Fermionic/DPP proof language, not a determinant loophole

The Schur complement has an exact exterior-power representation which does
not require multiplying physical frequencies.  Let `mu` be a probability
design on the legal band, let

```text
a(xi)=(a_1(xi),...,a_M(xi)),
G=integral a(xi)a(xi)^* dmu(xi),
H=integral v(xi)v(xi)^* dmu(xi),
Delta_mu=det(H)/det(G),                                    (3.1)
```

In the convention (2.2), `g=integral a(xi)b(xi)dmu(xi)`, so take
`v(xi)=(a(xi),conj(b(xi)))`; then `H=[[G,g],[g^*,c]]`.  (With the conjugate
convention for `g`, conjugate this last coordinate instead.)

Here one restricts to the nonsingular span.  Andreief's identity
gives

```text
Delta_mu = 1/(M+1)
  * [integral_(Omega^(M+1)) |det[a_1;...;a_M;conj(b)](xi_0,...,xi_M)|^2 dmu^(M+1)]
  / [integral_(Omega^M) |det[a_1;...;a_M](xi_1,...,xi_M)|^2 dmu^M].          (3.2)
```

The numerator is the squared volume obtained by adding the carrier orbital
to `M` prime-log orbitals; the denominator is the prime-only fermionic
partition function.  Equivalently, (3.2) is the expected carrier innovation
under volume sampling by the prime determinantal point process.

This does **not** enlarge `Delta_mu`: it is exactly (2.2) for the same design.
Its possible value is methodological.  It introduces `M+1` independent
frequencies, each inside the legal band, and antisymmetrizes repeated prime
configurations.  Therefore an exterior-power estimate does not literally
need a one-variable aperture `Y^(M+1)`.  A successful proof would bound the
ratio (3.2) using actual prime-log separation or a Coulomb-gas/orthogonal-
ensemble argument.

The kill condition is equally clear.  A determinant lower bound which loses
an uncontrolled product of `M` singular values, or which first estimates the
numerator and denominator separately, merely recreates the square-root
barrier.  The estimate must be **relative** and carrier-sensitive.

The low-atom/high-band model can be evaluated completely.  If `nu_H` is a
high-band design, `q=a(xi_0)`, and `L=q^*G_H^(-1)q`, then for

```text
mu_epsilon=epsilon*delta_(xi_0)+(1-epsilon)*nu_H
```

with ideal zero high-band carrier,

```text
Delta(mu_epsilon)
 =|b_0|^2*epsilon*(1-epsilon)/(1-epsilon+epsilon*L),

max_epsilon sqrt(Delta)=|b_0|/(1+sqrt(L)).                 (3.3)
```

The common fermionic partition function cancels exactly; the remaining
bosonic quantity is the same directional Christoffel leverage.  Consequently
near-unique factorization of `det(G_H)`, Grassmann localization, or volume
repulsion cannot improve the carrier unless it proves a new bound for this
specific direction.  Keeping the DPP samples separate returns the Schur
complement; multiplying them into one physical test restores the `Y^2`
conductor bill.  There is no third option in this model.  See
`ZETA23-SUSY-DPP-PARTITION-FUNCTION-COLLAPSE-CARD-2026-08-13.md`.

## 4. Theta transport: two attractive cones were falsified

For the full theta kernel put

```text
h_T(p)=integral Phi((p+q)/2)Phi((p-q)/2)exp(-iTq)dq,
S_2(P,T)=integral_P^infinity (p-P)h_T(p)dp.                (4.1)
```

Pointwise slice positivity is false:

```text
h_30(0)=-5.2553375905398... * 10^(-7).                    (4.2)
```

The initially promising twice-integrated cone is rigorously false.
With `Z(t)=xi((1-it)/2)/4`, the exact identity is

```text
S_2(P,T)=2/pi integral_0^infinity cos(P xi)
 [Z(T)^2-Z(T+xi)Z(T-xi)]/xi^2 dxi.                        (4.3)
```

High-precision calculation first gives

```text
S_2(0,97.2)=-4.25687874223465... * 10^(-30).              (4.4)
```

More strongly, `results/certify_theta_s2_negative.py` uses Arb quadrature,
a Cauchy estimate at the removable origin, and an elementary
gamma-recurrence/Euler--Maclaurin tail bound to certify

```text
-4.2626110089526610*10^(-30)
 < S_2(0,97.2)
 < -4.2511466914612062*10^(-30).                         (4.4a)
```

Higher integer tails are not a free renormalization hierarchy.  The target
weight `sinh(alpha p)sinh(eta p)` vanishes to exactly second order.  At the
third integration by parts the boundary term

```text
2 alpha eta S_3(0,T)                                      (4.5)
```

appears; exactly `S_3(0,T)=Z'(T)^2-Z(T)Z''(T)` in the normalization (4.3).
Thus the next
integer step imports rather than removes an RH-strength boundary sign.

Fractional orders do not rescue the cone.  For `1<nu<2`, the fractional
derivative of the target weight is positive, but the semigroup law gives

```text
S_2=I_-^(2-nu) S_nu.                                      (4.6)
```

Consequently `S_nu>=0` would imply the already-false `S_2>=0`; fractional
positivity is stronger, not weaker.  By (4.4a), this closes every
`1<nu<2` rigorously.  The failure is structural even in a
model class: the positive atomic inverse measure

```text
(delta_(-2)+delta_(-1)+delta_1+delta_2)/4
```

has the Laguerre--Polya transform `cos(3t/2)cos(t/2)`, yet its exact second
tail satisfies `S_(2,pi)(0)=-1/4`.  Positivity of the inverse measure,
positive definiteness, and real-rootedness together therefore do not imply
the needed divided-Turan sign.

## 5. What the control and scattering imports actually taught us

### 5.1 Linear quantum/noncommutative lifts are exactly scalar

For arbitrary left/right coefficients in a `C*`-algebra with state `phi`,
put `h_k=phi(L_k^*R_k)`.  GNS Cauchy--Schwarz gives

```text
sum_k |h_k| <= sqrt(E_L E_R).                              (5.1)
```

After normalization, every scalar carrier readout is bounded by `E(A,b)`;
the scalar construction attains equality.  Matrix dimension, entanglement,
free unitaries, and mixed states therefore give no gain under a linear final
readout.

QSP and lossless control exhibit the same phenomenon.  A notch in one
paraunitary channel moves the residue to its complementary channel, while
compact scalar descent pays the Wiener norm rather than the controlled
`H-infinity` norm.

### 5.2 Generic geometric scattering misses the principal cusp channel

A cutoff constant-horocycle Eisenstein wave can escape arbitrarily far into
the cusp with unit norm, `O(1/L)` residual, and vanishing compact observation.
At a zero of the incoming coefficient `Lambda(2s)`, the outgoing coefficient
`Lambda(2s-1)` remains.  Hence generic FUP, passivity, and compact-core
observability permit precisely the pure-outgoing resonance which must be
excluded.  Any inequality controlling that outgoing channel by the incoming
one is already a new arithmetic resonance-gap theorem.

### 5.3 Warped-lattice FFT compilation conserves the scoped ledger

On one multiplicative shell the phase
`exp(2*pi*i*r*(Y*exp(u)-N)/H)` agrees exactly with an additive character at
integer nodes.  For a fixed smooth window its ordinary Fourier Wiener cost is

```text
asymp max(1,sqrt(|r|*H/Y)).                              (5.2)
```

The legal aperture contains the central band, but exact finite-band node
correction remains the original condition-number problem.  More importantly,
the separated proof which gives each block of `M_j` nodes its Parseval/FFT
certificate and then uses the triangle inequality pays

```text
sum_j sqrt(M_j)>=sqrt(sum_j M_j).                         (5.3)
```

This is a conservation theorem for that **charged upper-bound method**, not a
lower bound for the true Wiener norm or for `E_Y`.  Coherent cancellation
within or between warped blocks remains possible, but proving it is exactly a
new global actual-node extremal estimate.  Local Taylor geometry alone does
not provide the saving.  See
`ZETA23-WARPED-LATTICE-MULTISCALE-FFT-WIENER-CONSERVATION-GATE-2026-08-13.md`.

### 5.4 Generic SUSY has zero index and the detector is not a norm

The completed theta operator has the exact constant-coefficient
factorization

```text
L_T=A_T^*A_T,       A_T=d_p^2-(1+i*T)^2.                 (5.4)
```

Since `A_T` and `A_T^*` commute, the elementary partner has zero Witten
index.  The desired detector is a cross pairing, not the positive norm
`||A_T f||^2`.  A Darboux factorization built from the Eisenstein state uses
`-(log E*)'` and becomes singular precisely at the zeros/resonances to be
excluded.  Likewise a de Branges/Schur index is constant only until such a
zero crosses the boundary.  Generic supersymmetry and topology therefore do
not forbid the crossing; a theta-specific complex minor inequality would be
new arithmetic input.

### 5.5 Machine-discovered SOS needs the missing nonlocal variable

Prime-power support does give an exact sparse split

```text
prime contribution = sum_p P_p(gamma*log p),               (5.5)
```

but the strongest lower bound in the explicitly prime-separable Fejer/SOS
class is `sum_p min P_p`.  In the floating centered finite stress test, the
sampled lower envelope is already negative at `X=256,512` while the completed
shifted squares are about `2.25,2.04`.  (The exact torus minima can only be
smaller than the sampled values; an interval coefficient replay was not
performed.)  The observed finite signs therefore use common-height
cross-prime coherence which independent prime-local squares discard.

There is also an exact signless compression,

```text
H_E=2*L_A-2*(log X)*diag(Re E_X),
rank([diag(tau),H_E])<=2,                                  (5.6)
```

but Loewner displacement rank is not Loewner positivity.  Most importantly,
for every head `X`, proposed candidate `rho`, and prime `q>X`,

```text
F_(rho,q)(s)=(1-q^(rho-s))(1-q^(conj(rho)-s))              (5.7)
```

has logarithmic-derivative support only at `q^k`.  The symmetric completion
`F(s)F(1-s)` inserts the candidate quartet (with the exponential model's
vertical aliases) while leaving every Dirichlet coefficient through `X`
unchanged; its additional constant logarithmic derivative is an explicit
completion term.  This is a structural model, not an Euler-product
counterexample to zeta.  It proves that the finite head and zero label alone
cannot identify a conditional identity; a valid zeta proof must expose an
exact nonlocal tail.  See
`ZETA23-CENTERED-ONE-SQUARE-MACHINE-SOS-OVERFIT-CARD-2026-08-13.md`.

## 6. Current experiment queue

### A. Atomic-cancellation coherence -- kill or promote

1. Search specifically for a carrier-rich low measure whose high-band atomic
   cancellation cost `C_(T,B)` is `Y^(o(1))`.
2. In the opposite direction, prove a carrier-aware correlation or
   large-sieve estimate forcing `C_(T,B)>=Y^delta` for some
   `delta>.0180303234`.
3. Fit only phase patterns which imply one of those symbolic alternatives;
   do not extend the four-point floating exponent fit for its own sake.
4. Interval-certify a proposed symbolic residual and Schur complement on the
   complete legal band before promoting it.

Success means an explicit family satisfying (2.4).  A power lower bound on
`C_(T,B)` instead closes this route.  Either outcome is progress; more
uncertified Remez points are not.

### B. Fermionic relative determinant -- same gate, not a second route

The exact calculation (3.3) shows that a DPP proof is useful only if it bounds
the carrier-specific leverage `L` subpolynomially.  Estimates for the common
fermionic partition function or for `det(G_H)` alone cancel from the ratio.
This language may suggest a relative Christoffel estimate, but it is not an
independent item in the portfolio.

### C. Oscillatory noncompact packets -- admissible, scoped closure negative

A nonlinear-phase causal packet really can have a slowly decaying envelope
and a superexponentially decreasing autocorrelation.  The exact packet
`chi(t)exp(-a*t+i*exp(theta*t))` passes prime-side Weil admissibility and can
retain a nonzero boundary Laplace carrier.  Stationary phase nevertheless
gives the exact remote alias

```text
K(s-i*T)~2*pi/(theta*T)*(T/theta)^(-2a/theta),              (6.1)
```

independent of the depth `s`.  Translating two copies to obtain a signed
depth-`alpha` carrier gives target scale `|d|exp(alpha*L)` but absolute prime
scale `|d|exp(L/2)`.  Exact prime interpolation forces `d` to decay faster
than every prescribed exponential in the flat-onset model; exact pole
interpolation gives `|d|=1/(2cosh(L/2))`.  Thus chirping removes literal tail
divergence but does not compact-realize the causal Pick filter.  Only a new
target-conditioned signed von Mangoldt estimate remains.  See
`ZETA23-OSCILLATORY-NONCOMPACT-CHIRP-WEIL-KERNEL-GATE-2026-08-13.md`.

### D. Third theta tail -- endpoint-obstructed diagnostic

The first unfalsified integer cone is `S_3(P,T)>=0`, but it is not a free
promotion of the detector argument.  The theta weight has a zero of exactly
order two, so the third integration by parts includes the endpoint
`2*alpha*eta*S_3(0,T)`, with
`S_3(0,T)=Z'(T)^2-Z(T)Z''(T)`.

There is now an exact positive-density formulation.  Define

```text
B_P(w)=1/4 integral_R (|d|-P)_+^2
       Phi((w+d)/2)Phi((w-d)/2)dd.                       (6.2a)
```

Then `S_3(P,T)` is the Fourier transform of `B_P` in `w`.  Thus the proposal
is precisely positive definiteness of every member of a diagonal-excised
Laguerre family.  At `P=0` this is the RH-strength first Laguerre gate; the
positive-`P` conditions are genuinely additional.  They do not follow from
ordinary Laguerre--Polya/Hermite--Biehler structure: the positive atomic
inverse with transform

```text
cos(T)cos(3T)cos(4T)
```

has the exact value `S_3(7,pi/2)=-1/16`.  An irrational perturbation makes
all its zeros simple, and narrow Gaussian smoothing makes the inverse density
positive and smooth while preserving the negative sign.

For the actual theta kernel, a gamma-rescaled completed-xi/DST scan over two
offset height lattices tested `T<=1000` and
`0<=P<=log(1+T)+3`.  It found no scale-separated negative.  Every apparent
negative lay at the subtractive quadrature floor, and representative
arbitrary-precision reruns returned positive values.  This is **numerical
survival only**, not a theorem or an interval certificate.  The next valid
move is a full-Poisson positive-definite factorization of `B_P`, or an Arb
certificate for a targeted negative generated above the current numerical
floor.  See
`ZETA23-THIRD-THETA-TAIL-S3-ATTACK-2026-08-13.md`.

### E. Wigner--Husimi reverse localization -- exact smoothed survivor

The theta slice is exactly a Wigner distribution,
`h_T(p)=W_Phi(p/2,T)`.  Hudson's theorem makes its pointwise negativity
structural because `Phi` is not Gaussian.  A squeezed Gaussian Husimi lift is
nevertheless positive and proves, with

```text
U_x(T)=|F(x-i*T)|^2,
G_s(Omega)=s/sqrt(pi)*exp(-s^2*Omega^2),
M_s(x,T)=G_s*U_x(T),
```

the unconditional inequality

```text
e^(s^2*A^2)M_s(A,T)>=e^(s^2*B^2)M_s(B,T),    A>=B>=0.      (6.2)
```

For `A=alpha+eta`, `B=alpha-eta`, this is

```text
M_s(A,T)>=e^(-4*s^2*alpha*eta)M_s(B,T).                    (6.3)
```

It is not the pointwise detector: smoothing adds the exact positive common
mode `tanh(2*s^2*alpha*eta)*(G_s*(U_A+U_B))`.  In `(p,T)` coordinates the
kernel has `sigma_p*sigma_T=1`, so height localization forces this
contamination.  Anti-Wick recovery and signed differences of spectrograms
both reduce to ill-conditioned backward heat.

The remaining coefficient-specific test is sharp.  Could a hypothetical
outer-line zero force, at its height `T_0`,

```text
M_s(A,T_0)<e^(-4*s^2*alpha*eta)M_s(B,T_0)?                 (6.4)
```

That would contradict (6.3) and prove exclusion.  Generic phase-space
positivity cannot supply (6.4); any attempt should be fail-fast tested on the
actual theta coefficients.  See
`ZETA23-WIGNER-HUSIMI-ANTI-WICK-THIN-DISPLACEMENT-GATE-2026-08-13.md`.

## 7. Portfolio decision

```text
adversarial Schur identity                 PROVED and promoted
real-cosine support bound <=M+1            PROVED; observed saturation numerical
uniform arithmetic Schur lower bound       OPEN
atomic cancellation cost C_(T,B)           EXACT gate; random-polytope prior unfavorable
fermionic/DPP ratio                        PROVED; generic calculation collapses to leverage
linear quantum/QSP advantage               CLOSED
generic cusp/FUP advantage                 CLOSED
warped-lattice local phase/curvature       PROVED for fixed uniform windows
separated FFT/wavelet compilation          NO IMPROVEMENT in its charged ledger
coherent warped-block cancellation         OPEN; returns to global E_Y
generic SUSY/topological protection        CLOSED (zero index/cross pairing)
first theta slice cone                     NUMERICALLY FALSE
second theta tail cone                     RIGOROUSLY FALSE (Arb certificate)
fractional theta cone                      CLOSED (stronger than false S2)
third theta tail / Laguerre cone            NUMERICALLY SURVIVES to T=1000; endpoint-obstructed
oscillatory noncompact packet              ADMISSIBLE; translation/interpolation CLOSED
Wigner pointwise positivity                STRUCTURALLY FALSE (Hudson)
Husimi radial monotonicity                  PROVED after Gaussian smoothing
generic anti-Wick/positive-bank recovery   CLOSED by uncertainty/backward heat
coefficient-specific Husimi localization   OPEN, exact target (6.4)
prime-separable machine SOS                 CLOSED in the stated separable class
finite-head plus candidate-zero label       NONIDENTIFYING without a nonlocal remainder
uniform zeta zero-free strip               NOT PROVED
```

The strategic conclusion is deliberately narrow.  The actual-node Schur
problem is now a **kill-or-promote** experiment, not the default favorite:
its exact formulation is attractive, but its observed one-atom cancellation
geometry has a square-root random-polytope prior.  The only analytic cone to
survive direct falsification is the theta-specific positive-definiteness of
the complete `B_P` family, and even that contains the RH-strength Laguerre
endpoint.  Husimi smoothing supplies a second exact theorem but leaves the
coefficient-specific reverse-localization estimate (6.4).  Future work should
attack one of these named arithmetic statements directly; another change of
norm, lift, or basis is overwhelmingly likely to hide one of the conservation
laws rather than evade it.
