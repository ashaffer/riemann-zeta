# Quantitative amplification of an off-line zero in localized Weil floors

## Status

This note proves a conditional theorem about what the localized zeta Weil
forms must do if an off-critical zero exists.  It does **not** prove or assume
that such a zero exists.

The main conclusion is that a zero at horizontal displacement `delta` forces
the negative localized floor to grow at least like

    exp((2 delta - epsilon) a)

for every sufficiently large support radius `a`.  This replaces the former
qualitative statement that the floors merely tend to minus infinity and
closes the proposed quantitative two-bump witness at the exponent level.

There are two proofs with different strengths.

1. A short Laplace-pole argument uses an arbitrary compact bump.  It gives
   the sharp exponent along arbitrarily large supports and already controls
   cancellation from the complete zero divisor.
2. The zeta-specific Fourier cardinal functions of Bondarenko--Radchenko--Seip
   isolate one quartet before a smooth truncation.  Their rapid decay in
   vertical strips upgrades the conclusion to every sufficiently large
   support.

The reverse exponent is also proved when the off-line divisor is finite, and
more generally when its local displacement-square measure is translation
bounded.  For the unrestricted zeta divisor it remains open.  Two fail-fast
audits show why: ordinary prime-counting error loses a half derivative, while
a synthetic divisor with essentially perfect counting and finite floor on
every fixed support can still have superexponentially negative selected
floors.  Thus the remaining input must be signed zeta arithmetic rather than
strip or density information alone.

The scalar passage from a large translated cross term to a negative spectral
floor is Lean-checked in
[`TwoBumpFloorAmplification.lean`](../lean/rhbridge/RHBridge/TwoBumpFloorAmplification.lean).
The divisor, Fourier-interpolation, and limiting arguments below remain
analytic mathematics.

## 1. Normalization

Use

    fhat(z) = integral_R f(x) exp(i z x) dx,
    f_tilde(x) = conjugate(f(-x)).

For a nontrivial zero `rho` of `xi`, put

    z_rho = (rho - 1/2) / i.

Thus, if `rho = beta + i tau` and `delta = beta - 1/2`, then

    z_rho = tau - i delta.

The Weil distribution and its polarized quadratic form are

    W(phi) = sum_rho m_rho phihat(z_rho),
    Q(f,g) = W(f * g_tilde)
           = sum_rho m_rho fhat(z_rho)
               conjugate(ghat(conjugate(z_rho))).                 (1.1)

Every series in this note is counted with multiplicity.  For compact smooth
tests it converges absolutely: the nodes lie in `|Im z| < 1/2`, the Fourier
transform decays faster than every power uniformly on compact horizontal
strips, and the Riemann--von Mangoldt formula gives

    N(T+1) - N(T) = O(log(T+2)).                                  (1.2)

Let

    lambda(a) = inf Q(f,f) / ||f||_2^2,

where the infimum is over nonzero smooth functions supported in `(-a,a)`, and
put

    c(a) = max(0, -lambda(a)),
    Delta = sup_rho |Re(rho) - 1/2|.                              (1.3)

The localized forms are lower semibounded, so `lambda(a)` is finite.  The
family `lambda` is antitone and `c` is nondecreasing.

## 2. The algebraic two-bump inequality

Fix `f` supported in `(-r,r)`, and write

    n = ||f||_2^2 > 0,
    q = Q(f,f),
    B_f(R) = Q(T_{-R/2} f, T_{R/2} f).

For `R > 2r` the two translates are disjoint and fit in the centered window

    a = R/2 + r.                                                   (2.1)

Translation invariance gives both diagonal entries equal to `q`.  Choosing
the phase of a scalar `alpha`, `|alpha|=1`, so that the two cross terms add to
`-2 |B_f(R)|` gives

    lambda(R/2+r) <= (q - |B_f(R)|) / n.                           (2.2)

Consequently,

    c(R/2+r) >= (|B_f(R)|-q)/n                                   (2.3)

whenever the right side is nonnegative.  No estimate is lost in this step.

## 3. Pole-to-floor amplification without interpolation

### Theorem 3.1

Suppose `rho_0` is an off-critical zero with

    delta = |Re(rho_0)-1/2| > 0.

For every `epsilon>0` there are a fixed compact smooth bump `f`, radii
`a_j -> infinity`, phases `alpha_j`, and two-bump tests

    F_j = T_{-R_j/2} f + alpha_j T_{R_j/2} f,
    supp(F_j) subset (-a_j,a_j),

such that

    Q(F_j,F_j) / ||F_j||_2^2
      <= -C_(rho_0,epsilon) exp((2 delta-epsilon) a_j).            (3.1)

In particular,

    limsup_(a->infinity) log(1+c(a))/(2a) >= delta.               (3.2)

### Proof

By the functional equation, choose the member of the zero quartet whose node
`z_0` has `Im z_0=delta`.  Choose a compact smooth `f` for which

    fhat(z_0) fhat(conjugate(z_0)) != 0.                           (3.3)

Such bumps exist: a sufficiently narrow rescaling of any bump with nonzero
integral has Fourier transform nonzero at both fixed points.

Put `psi=f*f_tilde`.  From (1.1) and the translation rule for the Fourier
transform,

    B_f(R)
      = sum_rho m_rho ahat_rho exp(-i z_rho R),
    ahat_rho
      = fhat(z_rho) conjugate(fhat(conjugate(z_rho))).             (3.4)

The coefficients are absolutely summable.  For `Im z>1/2`, termwise
integration is therefore justified and yields

    integral_0^infinity B_f(R) exp(i z R) dR
      = i sum_rho m_rho ahat_rho/(z-z_rho).                       (3.5)

The series on the right is normally convergent away from the nodes and is
meromorphic.  By (3.3), it has a genuine pole at `z_0`.

If

    limsup_(R->infinity) log(1+|B_f(R)|)/R < delta,               (3.6)

then `B_f(R)=O(exp(eta R))` for some `eta<delta`.  The left side of
(3.5) would be holomorphic on `Im z>eta`.  Meromorphic uniqueness, starting
from `Im z>1/2`, would then make the genuine pole at `z_0` removable, a
contradiction.  Hence the limsup in (3.6) is at least `delta`.

For every positive `epsilon`, there are therefore arbitrarily large `R_j`
with

    |B_f(R_j)| >= exp((delta-epsilon/3) R_j).                      (3.7)

Apply (2.2), absorb the fixed `q` and `n`, and use
`a_j=R_j/2+r`.  After a harmless adjustment of `epsilon`, this gives (3.1).
This proves the theorem.  Notice that no zero was declared rightmost and no
other zero contribution was estimated term by term: the pole of the transform
prevents the *complete* cross correlation from cancelling at every large
scale.

## 4. Cardinal interpolation and the all-support upgrade

The preceding proof does not bound the gaps between the large values of
`B_f`.  A zeta-specific interpolation theorem removes that defect.

Bondarenko--Radchenko--Seip prove that for every zero `rho` of positive
classical height and every jet index below its multiplicity there is an even
entire function `V_(rho,j)` with the cardinal Hermite property

    V_(rho,j)^(j')(z_sigma) = delta_((rho,j),(sigma,j')),          (4.1)

and which decays faster than every inverse power in every horizontal line.
Their proof gives rapid decay in vertical strips, uniformly when the other
kernel variable ranges over compact sets.  See their Theorem 1.1 and
Section 4.3.2.

Let `rho=beta+i tau`, with `tau>0` and `delta=beta-1/2>0`, and let

    rho_dagger = 1-conjugate(rho).

The corresponding nodes are `tau-i delta` and `tau+i delta`.  Set

    H = V_(rho,0) + V_(rho_dagger,0).                              (4.2)

Evenness and the functional-equation symmetries imply that `H` equals one at
the four nodes of this quartet and vanishes at every other zero node.

Define `v` by inverse Fourier transformation in the normalization of Section
1.  The rapid decay of `H` in every horizontal strip permits an arbitrary
contour shift.  For all `L>0` and all derivative orders `k`,

    |v^(k)(t)| <= C_(L,k) exp(-L |t|).                             (4.3)

Thus `v` and all its derivatives decay faster than every exponential.  This
does not say that `v` has compact support: the BRS cardinal function has
infinite exponential type.

Choose an even cutoff `chi` supported in `(-1,1)` and equal to one on
`[-1/2,1/2]`, and put

    v_a(t)=chi(t/a)v(t),
    H_a=(v_a)hat.                                                  (4.4)

Repeated integration by parts, using (4.3), gives for every `L,N>0`

    sup_(|y|<=1/2,x in R)
      (1+|x|)^N |H_a(x+iy)-H(x+iy)|
        <= C_(L,N) exp(-La).                                      (4.5)

Combining (4.5) with (1.2) yields both `l1` and `l2` sampling estimates over
the complete zero multiset.  In particular,

    sum_rho m_rho |H_a(z_rho)-H(z_rho)|
      = O_L(exp(-La)).                                            (4.6)

For the translated cross term of `v_a`, (4.2) and (4.6) now give, uniformly
for `R>=0`,

    B_a(R)
      = 4m cos(tau R) cosh(delta R)
        + O_L(exp(R/2-La)),                                       (4.7)

where `m` is the common multiplicity of the quartet.  Also

    ||v_a||_2 -> ||v||_2 > 0,
    Q(v_a,v_a) = 4m + o(1).                                      (4.8)

### Theorem 4.1

For every off-critical zero of displacement `delta>0` and every
`epsilon>0`, there are constants `C>0` and `A_0` such that

    lambda(A) <= -C exp((2 delta-epsilon)A)                       (4.9)

for every `A>=A_0`.

### Proof

Fix `kappa>2`.  In (4.7), take `R` asymptotic to `kappa a` and choose `L`
so large that

    L > kappa(1/2-delta).                                         (4.10)

Then the error in (4.7) is `o(exp(delta R))`.  The set of `R` for which

    |cos(tau R)| >= 1/2                                          (4.11)

is relatively dense.  Hence, for every sufficiently large target radius
`A`, one may choose such an `R`, within a bounded distance of

    R_0 = 2 kappa A/(kappa+2),

and then set `a=A-R/2`.  We have `R/a -> kappa`, `a->infinity`, and the two
copies of `v_a` are disjoint.  Equations (4.7)--(4.8) and the phase choice in
Section 2 produce a test in `(-A,A)` with quotient at most

    -C_kappa exp(delta R).

Finally choose `kappa` so large that

    2 delta kappa/(kappa+2) > 2 delta-epsilon.                    (4.12)

This proves (4.9).

## 5. Growth consequences

Define the lower and upper floor exponents

    E_- = liminf_(a->infinity) log(1+c(a))/(2a),
    E_+ = limsup_(a->infinity) log(1+c(a))/(2a).                  (5.1)

Theorem 4.1, applied to every off-line zero and then to their supremal
displacement, gives

    Delta <= E_-.                                                 (5.2)

The elementary prime-side estimate already recorded in
`SEMIBOUNDED-WEIL-DICHOTOMY.md` gives

    lambda(a) >= -C_0 - 4sinh(a)
                 - sum_(log n<2a) 2 Lambda(n)/sqrt(n).

Using `Lambda(n)<=log n` shows that the last sum is `O((1+a)exp(a))`.
Therefore

    Delta <= E_- <= E_+ <= 1/2.                                  (5.3)

Two useful corollaries are immediate.

### Corollary 5.1: quantitative zero-free strip

If, for some `eta>=0`,

    c(a) = O(exp(2 eta a)),                                       (5.4)

then every nontrivial zero satisfies

    |Re(rho)-1/2| <= eta.                                         (5.5)

### Corollary 5.2: subexponential-floor criterion

The following are equivalent:

1. RH;
2. `c(a)` is subexponential in `a`;
3. for every `epsilon>0`, `c(a)=O_epsilon(exp(epsilon a))`;
4. `E_+=0`.

Indeed, RH gives `c(a)=0` by Weil positivity.  Conversely, any off-line zero
would give a positive lower exponent by Theorem 3.1, and in fact the
all-support lower bound of Theorem 4.1.

This criterion is strictly more permissive at the estimate level than the
fixed semibound in `SEMIBOUNDED-WEIL-DICHOTOMY.md`: polynomial or arbitrary
subexponential deterioration would still suffice for RH.

## 6. Exact exponent when the off-line divisor is finite

The reverse estimate is immediate under the classical finite-exception
hypothesis used in Bombieri's inertia theorem.

### Theorem 6.1

Suppose that only finitely many nontrivial zeros are off the critical line.
Then, for a constant `C` depending only on those exceptional zeros,

    lambda(a) >= -C exp(2 Delta a)                                (6.1)

for every `a>0`.  Consequently

    E_- = E_+ = Delta.                                           (6.2)

### Proof

The critical-line terms in (1.1) are

    m_rho |fhat(z_rho)|^2

and are nonnegative.  Group the remaining zeros into off-line quartets.  A
quartet of common multiplicity `m`, height `tau`, and displacement
`delta>0` contributes

    2m Re[fhat(tau-i delta) conjugate(fhat(tau+i delta))]
      + 2m Re[fhat(-tau-i delta) conjugate(fhat(-tau+i delta))].   (6.3)

For a function supported in `(-a,a)`, Cauchy--Schwarz gives

    |fhat(tau plus_or_minus i delta)|^2
      <= [sinh(2 delta a)/delta] ||f||_2^2.                       (6.4)

Using `2 Re(u conjugate(v)) >= -|u|^2-|v|^2`, the quartet is therefore
bounded below by

    -4m [sinh(2 delta a)/delta] ||f||_2^2.                        (6.5)

There are only finitely many such quartets.  Summing (6.5) and using
`sinh(2 delta a) <= exp(2 Delta a)/2` proves (6.1).  Hence `E_+<=Delta`,
while (5.2) gives `Delta<=E_-`; this proves (6.2).

This result identifies the precise obstruction in the general reverse
problem.  No new estimate is needed for critical-line zeros, and no finite
collection of off-line zeros causes a loss.  The difficulty is entirely the
collective control of a potentially infinite off-line divisor, where taking
the negative part quartet by quartet destroys the high-frequency cancellation
that makes each localized form lower semibounded.

## 7. Exact boundary and next target

What is now proved:

* a conditional, explicit two-bump mechanism;
* the exponent `2 delta`, up to arbitrary epsilon;
* control of the complete infinite zero sum;
* an eventual bound at every support radius, not only a subsequence;
* the parametric implication from floor growth to a zero-free strip;
* the exact exponent for finite exceptions and for translation-bounded local
  displacement-square mass;
* the Selberg-density mean-square substitute and the two sharp generic
  no-go audits for prime error and unsigned zero sampling.

What is not proved:

* an off-critical zero;
* RH;
* the general reverse estimate

      lambda(a) >= -C_epsilon exp((2 Delta+epsilon)a);            (7.1)

* equality of `Delta`, `E_-`, and `E_+` without the finite-exception or
  translation-bounded second-moment hypothesis;
* optimized constants or effective numerical witnesses.

The next genuine target is (7.1).  It asks whether the maximal horizontal
width of the zero divisor also controls the negative floor from above.  It is
not another positivity reformulation: for a specified positive `Delta` it is
a conditional stability theorem.  A plausible proof must combine vertical
Paley--Wiener shifts with the logarithmic high-frequency energy; a bare
sampling estimate loses that energy and is insufficient.

### 7.1 Fail-fast audit: ordinary prime-counting error loses a half derivative

The most direct arithmetic attempt does not close.  This failure is exact,
not a loose exponential estimate.

Let `U=2a`, `X=exp(U)`,

    c_f(u)=integral_R f(x) conjugate(f(x+u)) dx,
    Psi(X)=sum_(n<=X) Lambda(n),
    R(X)=Psi(X)-X.

Splitting `dPsi=dX+dR`, the pole term cancels the exponentially large main
part of the prime term.  In the present normalization the remainder is

    Q(f)=A(f)+B(f)-E_U(f),
    B(f)=2 integral_0^U Re(c_f(u)) exp(-u/2) du,
    B(f) >= -4 ||f||_2^2,                                       (7.2)

where `A` is the archimedean term and

    E_U(f)=2 Re integral_0^U c_f(u) exp(-u/2) dR(exp u).          (7.3)

A zero strip of width `Delta` gives, for every `eta>0`,

    R(X)=O_eta(X^(1/2+Delta+eta)).                               (7.4)

Writing (7.3) by Plancherel gives

    E_U(f)=(1/(2 pi)) integral_R |fhat(t)|^2 r_U(t) dt,
    r_U(t)=2 Re integral_(1-)^X x^(-1/2-it) dR(x).               (7.5)

Stieltjes partial summation yields only

    |r_U(t)| <= C_(Delta,eta) (1+|t|) X^(Delta+eta).             (7.6)

Taking `eta=epsilon/2` produces the desired exponential factor
`exp((2 Delta+epsilon)a)`, but (7.6) controls (7.3) by

    C exp((2 Delta+epsilon)a)
      [||f||_2^2 + (1/(2 pi)) integral |t| |fhat(t)|^2 dt].      (7.7)

The extra term is the squared homogeneous `H^(1/2)` norm.  The archimedean
part controls only a logarithmic Fourier weight.  This mismatch cannot be
removed using compact support: for a fixed compact bump `g`, the modulations
`f_N(x)=exp(iNx)g(x)` have the same support and `L2` norm, while the two
weights in question grow like `N` and `log N`.  Reverting to total variation
of the prime measure gives only the old `O(exp(a))` bound.

Thus (7.4), Abel summation, and the available archimedean coercivity cannot
prove (7.1).  A surviving prime-side proof needs a uniform oscillatory
Mellin/exponential-sum estimate that saves this derivative, or an equivalent
joint prime--archimedean argument.  The calculation does not disprove (7.1).

### 7.2 A sufficient local second-moment condition

There is a clean condition under which the general reverse estimate does
hold, even for infinitely many off-line zeros.  Index all vertical conjugate
off-line node pairs by `j` (so both signs of the classical height occur),
writing their nodes as

    gamma_j plus_or_minus i delta_j,
    0 < delta_j <= Delta,

with common multiplicity `m_j`, and define the horizontal second-moment
measure

    nu_2 = sum_j m_j delta_j^2 delta_(gamma_j),
    M_2 = sup_(x in R) nu_2([x,x+1]).                             (7.8)

#### Theorem 7.1

If `M_2<infinity`, then, for an absolute sampling constant `C_0`,

    Q(f,f) >= -2 C_0 M_2 (1+a^2)
      [sinh(Delta a)/Delta]^2 ||f||_2^2                          (7.9)

for every `f` supported in `(-a,a)`.  At `Delta=0`, interpret the ratio as
`a`.  Consequently (7.1) holds and

    E_- = E_+ = Delta.                                          (7.10)

#### Proof

For one conjugate node pair put

    u=fhat(gamma+i delta),  v=fhat(gamma-i delta).

The elementary identity behind the estimate is

    2 Re(u conjugate(v))
      >= -(1/2)|u-v|^2
      = -2 |Fourier[sinh(delta .)f](gamma)|^2.                  (7.11)

A translation-bounded positive measure `nu` obeys the
Plancherel--Polya/Sobolev sampling bound

    integral |ghat(x)|^2 dnu(x)
      <= C_0 sup_y nu([y,y+1])
        [||g||_2^2+||t g||_2^2].                                (7.12)

Apply (7.12) termwise to the power series

    sinh(delta t)/delta
      = sum_(n>=0) delta^(2n) t^(2n+1)/(2n+1)!,                 (7.13)

using Minkowski in `L2(nu_2)` and `|t|<=a`.  The resulting series sums to
`sinh(Delta a)/Delta`, and (7.11) gives (7.9).  Polynomial factors in `a`
are absorbed by `exp(epsilon a)`, proving the reverse exponential estimate.
Combine it with (5.2) to obtain (7.10).

The condition is not known for zeta and is not equivalent to RH.  Riemann--
von Mangoldt counting and the strip bound alone give only

    nu_2([T,T+1]) = O(Delta^2 log(T+2)),                         (7.14)

not the uniform estimate (7.8).  Thus (7.8) is a genuine intermediate
arithmetic checkpoint: it asks for square-average horizontal concentration,
not the vanishing of every displacement.

There is, however, a useful unconditional mean substitute.  With the
pair-counting convention of (7.8), put

    N_u(I)=sum_(gamma in I, beta>1/2+u) m_rho.

Layer cake and functional-equation symmetry give the exact identity

    nu_2(I)=2 integral_0^(1/2) u N_u(I) du.                       (7.15)

(If `nu_2` is instead defined by counting both zeros of each pair, the factor
is `4`.)  Selberg's near-critical-line density estimate

    N(1/2+u,X) << X^(1-u/4) log X                                (7.16)

therefore implies

    nu_2((0,X]) << X/log X.                                      (7.17)

If `m(t)=nu_2([t,t+1])`, (7.14), (7.17), and Fubini yield

    (1/X) integral_X^(2X) m(t) dt << 1/log X,
    (1/X) integral_X^(2X) m(t)^2 dt << 1.                        (7.18)

More generally the `p`-th mean is `O((log X)^(p-2))` for `1<=p<=2`.
Karatsuba--Korolev short-interval density estimates similarly give, for
`H=T^(27/82+epsilon)`,

    nu_2([T-H,T+H]) <<_epsilon H/log T.                          (7.19)

The newer Guth--Maynard density exponent improves the far-right regime but
does not improve this moment: the layer-cake integral is concentrated at
`u` near zero, where their exponent is larger than one.

These are genuine concentration restrictions, but they do not imply the
supremum in (7.8): a compactly supported test may be modulated to target one
exceptional height window.  Positive Poisson smoothing does not weaken the
uniform checkpoint either,

    sup_T integral dnu_2(y)/(1+(T-y)^2) < infinity
      iff M_2 < infinity.                                       (7.20)

A concrete unit-window density hypothesis that would close (7.8) is

    N_u([T,T+1]) <<_eta u^(-2+eta),
    1/log T <= u <= 1/2.                                        (7.21)

Together with the trivial count below `1/log T`, (7.15) makes the right side
uniformly integrable.  No current unit-interval density theorem located in
the audit reaches (7.21).  Thus the mean-square statement in (7.18) is a
reasonable weaker analytic checkpoint, but it cannot by itself control the
worst localized floor.

### 7.3 The continuous logarithmic energy is not the obstruction

Put

    E(f)=(1/(2 pi)) integral log(1+xi^2)|fhat(xi)|^2 dxi.

For `0<=delta<1`, contour shifting (equivalently, the Levy representation of
the logarithm) gives

    E(cosh(delta .)f)-E(sinh(delta .)f)
      >= E(f)+log(1-delta^2)||f||_2^2.                           (7.22)

Indeed, the polarized difference has multiplier
`Re log(1+(xi+i delta)^2)`, and

    |1+(xi+i delta)^2|
      >= (1-delta^2)(1+xi^2).                                   (7.23)

So a constant vertical displacement preserves the positive logarithmic
principal energy up to a bounded `L2` error.  The difficulty is the discrete,
height-dependent sampling of the even `cosh(delta t)` and odd
`sinh(delta t)` traces.

Standard strip sampling makes this distinction precise.  Using only
`delta_j<=Delta` and the local `O(log T)` zero count gives

    Q(f,f) >= -C_epsilon exp((2 Delta+epsilon)a)
      [||f||_2^2+E(f)].                                         (7.24)

This is the endpoint of an unsigned Plancherel--Polya argument: it controls
the sum of the even and odd trace energies, whereas the Weil form is their
difference.  The coefficient of `E(f)` in (7.24) cannot be absorbed into the
left side uniformly.  A useful proof of (7.1) must retain the signed
cancellation visible in (7.22).

### 7.4 Strip width and Riemann--von Mangoldt counting are insufficient

There is an explicit synthetic divisor showing that the missing signed
estimate cannot follow from strip and counting data alone.  Fix `Delta>0`
and take

    Z = {plus_or_minus exp(k) plus_or_minus i Delta : k>=1},

with multiplicity `k`.  It has width `Delta` and unit-interval count
`O(log T)`.  Choose a real, even, nonnegative compact bump `phi` and put

    f_0(t)=phi(t-b)-phi(t+b),
    F_0(z)=2i phihat(z) sin(bz).

Then

    2 Re[F_0(i Delta) conjugate(F_0(-i Delta))]
      = -8 phihat(i Delta)^2 sinh(b Delta)^2 < 0.                (7.25)

The modulations `f_k(t)=exp(-i exp(k)t)f_0(t)` have fixed support and norm.
Their `k`-th block contributes `k` times the negative constant in (7.25),
while every other block is `o(1)` by uniform strip-Schwartz decay.  Hence the
fixed-window floor of this synthetic zero form is `-infinity`.

A stronger construction retains both essentially perfect counting and a
finite floor on every fixed support.

#### Theorem 7.2: semibounded synthetic countermodel

For every `0<Delta<1/2`, there is a simple symmetric divisor of order one
such that:

1. every node lies in `|Im z|<=Delta` and all functional-equation and
   conjugation symmetries hold;
2. its height count is the Riemann--von Mangoldt main term plus `O(1)`;
3. its quadratic form is lower semibounded on every fixed Paley--Wiener
   support;
4. along radii `A_k->infinity`,

       lambda_Z(A_k) <= -c exp(A_k^2+Delta A_k).                 (7.26)

In particular, even the conjunction of strip width, full counting, symmetry,
and qualitative local semiboundedness does not imply (7.1).

#### Construction and proof

Begin with a critical-line quantile divisor `Gamma` for the Riemann--von
Mangoldt density `w(T) asymp log(T+2)`.  Cellwise Sobolev estimates on its
quantile cells, followed by Bernstein's inequality, give for every fixed
Paley--Wiener type `a`

    c_a integral w(x)|F(x)|^2 dx-C_a||F||_2^2
      <= sum_(gamma in Gamma)|F(gamma)|^2
      <= C_a integral w(x)|F(x)|^2 dx+C_a||F||_2^2.              (7.27)

Choose

    A_k -> infinity,
    d_k=exp(A_k^2),
    log T_k asymp d_k,
    p_k=exp(-Delta A_k),                                        (7.28)

with the heights rapidly separated.  An interval of length comparable to
`p_k` near `T_k` contains

    m_k asymp p_k d_k                                           (7.29)

base nodes.  Pair consecutive nodes and replace each pair by the two simple
off-line zeros of displacement `Delta` at their midpoint, adding the required
reflections.  Moving two real counting jumps to a double midpoint jump changes
the counting function by at most one, which proves item 2.

Fix a support `a`.  The tail clusters have local relative density at most
`sup_(k>K)p_k`.  The vertical Plancherel--Polya bound and (7.27) bound their
total form perturbation by

    C_(a,Delta) sup_(k>K)p_k
      [integral w(x)|F(x)|^2 dx+||F||_2^2].                     (7.30)

Since `p_k->0`, choose `K` so that (7.30) is absorbed by the positive lower
bound in (7.27).  The first `K` clusters are a finite-rank bounded
perturbation.  This proves item 3.  This weighted sampling lemma is standard
but is not formalized in the repository.

For item 4, take a fixed even nonnegative bump `phi` and put two copies near
the endpoints of `(-A,A)` with opposite sign:

    g_A(t)=phi(t-c)-phi(t+c),  c=A-O(1).

As in (7.25), its paired values at `plus_or_minus i Delta` contribute at most
`-c_0 exp(2 Delta A)`.  Modulate `g_(A_k)` to height `T_k`.  Because
`A_k p_k->0`, the sign and size persist across the microscopic cluster.  The
positive quantile background is `O(d_k)`, while the selected cluster is

    -c m_k exp(2 Delta A_k)
      asymp -c d_k exp(Delta A_k).                               (7.31)

Uniform strip-Schwartz decay and rapid separation make all other clusters
negligible.  Equations (7.28) and (7.31) prove (7.26).

This is still not a model of zeta: it deliberately omits Euler-product
arithmetic.  It is sparse enough to satisfy ordinary global zero-density
bounds, including the mean conclusions in (7.18).  The construction proves
that the missing ingredient is specifically signed arithmetic control of
where horizontal splitting occurs, not strip geometry, zero count, average
density, or mere fixed-window semiboundedness.

The subsequent arithmetic audit sharpens this target.  The **minimal**
signed sampling-discrepancy estimate needed for the reverse exponent is

    Q(f,f)
      >= -C_epsilon exp((2 Delta+epsilon)a)||f||_2^2.            (7.32)

After exact prime--pole cancellation, this is a one-sided logarithmic
relative bound for the oscillatory von Mangoldt discrepancy on the compressed
Paley--Wiener space.  At `Delta=0` its endpoint is RH-equivalent.  Requiring
the former strict reserve `Q>=cE-error`, `c>0`, is genuinely stronger: it also
forces `(gamma_(n+1)-gamma_n)log log gamma_n->0`.  Pointwise endpoint control
is too strong in a different direction, since Kronecker recurrence requires
an `exp(a)` remainder even when the compression is positive.  See
[`SIGNED-PRIME-GARDING-CHECKPOINT.md`](SIGNED-PRIME-GARDING-CHECKPOINT.md).

The second-moment condition (7.8) is one sufficient checkpoint for (7.32);
without it, one must compare the even and odd vertical traces jointly rather
than bound them separately.

## 8. Literature inputs and novelty boundary

Primary inputs:

* Bondarenko, Radchenko, and Seip,
  [*Fourier interpolation with zeros of zeta and L-functions*](https://arxiv.org/abs/2005.02996),
  Theorem 1.1 and Section 4.3.2, for the cardinal functions and their
  vertical-strip decay.
* Suzuki,
  [*Aspects of the screw function corresponding to the Riemann zeta-function*](https://arxiv.org/abs/2206.03682),
  for the Weil-distribution normalization and the unconditional screw
  transform used by the surrounding project.
* Bombieri,
  [*Remarks on Weil's quadratic functional in the theory of prime numbers, I*](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0),
  for the earlier finite-off-line-zero inertia theorem and localized
  variational setting.  That result is qualitative in the support-depth
  variable and does not state the exponential rate proved here.
* Selberg's near-critical-line density theorem, in the modern explicit
  treatment of Simonič,
  [*Explicit zero density estimate for the Riemann zeta-function near the critical line*](https://doi.org/10.1016/j.jmaa.2020.124303),
  for (7.16)--(7.18).
* Karatsuba and Korolev,
  [*The argument of the Riemann zeta function*](https://www.mathnet.ru/eng/rm1741),
  for the short-interval estimate used in (7.19).
* Bellotti and Wong,
  [*Improved estimates for the argument and zero-counting of Riemann zeta-function*](https://arxiv.org/abs/2412.15470),
  for the current explicit `O(log T)` unit-window counting scale.
* Guth and Maynard,
  [*New large value estimates for Dirichlet polynomials*](https://annals.math.princeton.edu/2026/203-2/p06),
  for the current global zero-density comparison; its strongest regime does
  not improve the near-line second moment used here.
* The classical Riemann--von Mangoldt zero count.

The pole-to-floor lemma, the BRS truncation-to-localized-floor consequence,
and the exact finite-exception exponent appear to be a new synthesis, but the
prior-art search is not exhaustive and no novelty claim should be made before
expert review.  Fixed-exponential-type
exact isolation is still impossible on density grounds: a Paley--Wiener zero
set has linear counting density, whereas the zeta nodes have order
`T log T`.  The BRS construction evades this by using an infinite-type entire
cardinal function and only then truncating its inverse transform.
