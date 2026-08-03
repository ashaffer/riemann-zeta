# Stage 4 prolate regularization and Mellin-tail proof

## Endpoint correction

Let `psi_0, psi_4` be two fixed even prolate modes with the same Fourier
sign.  Their sharp zero extensions cannot be used directly: even an
exponentially small endpoint jump produces a nonzero `1/xi` Fourier tail.
Thus the weighted `L1` estimate for `Fourier(h)-h` claimed in an earlier
draft was false for the sharp vectors.

Choose an even flat cutoff `q_lambda`, equal to one on
`[-lambda+1,lambda-1]` and flat at `+-lambda`.  Start with the normalized CCM
combination

`phi_lambda = c_lambda
  (psi_4 psi_0(0) - psi_0 psi_4(0))`,

so `phi_lambda(0)=0`.  Fixed-mode prolate/Hermite asymptotics show that every
fixed Sobolev norm of `(1-q_lambda) phi_lambda` is exponentially small.  The
integral of `q_lambda phi_lambda` is exponentially small as well: before the
cutoff it is the difference of two same-sign truncated-Fourier eigenvalues,
times polynomially bounded normalization factors.

Fix an even smooth bump `b`, supported in `[-1,1]`, with `b(0)=0` and
`integral b=1`, and set

`h_lambda = q_lambda phi_lambda
  - (integral q_lambda phi_lambda) b`.

Then `h_lambda` is smooth and compactly supported and satisfies exactly

`h_lambda(0)=0`,  `Fourier(h_lambda)(0)=integral h_lambda=0`.

It is exponentially close to the sharp CCM vector in every fixed Sobolev
norm, hence in the logarithmic graph norm.

## Weighted Fourier leakage

Put `r_lambda = Fourier(h_lambda)-h_lambda`.  Prolate concentration gives

`||r_lambda||_2 <= P(lambda) exp(-2*pi*lambda^2)`.

The prolate differential equation, the flat cutoff, and the moment bump give
polynomial high-norm bounds.  Interpolation therefore yields, for every fixed
low pair `(p,q)`,

`||x^p derivative^q(r_lambda)||_2 <= eta_lambda`,

where `eta_lambda -> 0` exponentially.  The regularized defect is Schwartz,
so weighted Cauchy--Schwarz gives the required `L1` bounds for `r_lambda`,
`r_lambda'`, and their first weighted versions.

## Poisson reduction

For `0<u<lambda^-1`, Poisson summation and the two exact moment conditions
give

`E(h_lambda)(u)
 = E(Fourier(h_lambda))(u^-1)
 = E(r_lambda)(u^-1)`,

because `E(h_lambda)(u^-1)=0` when `u^-1>lambda`.

Let `x=log u`, `L=log lambda`, and let `alpha` be in the open centered
critical strip.  Expanding `E(r)` and changing variables `y=n exp(-x)` gives

`integral_(x<-L) exp(alpha*x) |E(r)(exp(-x))| dx
 <= lambda^(-delta)/delta * integral_lambda^infinity |r(y)| dy`,

where `delta=1/2-|alpha|`.  Applying the same calculation after `d/dx` and
using the weighted `L1` estimates gives

`||exp(alpha*x) E(h_lambda)(exp x)||_W11(x<-L)
 <= eta_lambda/delta`.

## Mellin estimate at zeta zeros

The untruncated Mellin transform of `E(h_lambda)` contains
`zeta(1/2+z)`, hence vanishes at every corresponding nontrivial zero.  The
transform `K_lambda` of the windowed regularized comparator is the negative
omitted lower tail.  The preceding estimate and one integration by parts
give

`|K_lambda(alpha+i*t)|
 <= C eta_lambda/(delta*(1+|t|))`.

For a zeta zero, the symmetric de la Vallee Poussin zero-free region gives

`delta^-1 <= C log(2+|t|)`.

Consequently, for both complementary centered arguments,

`|K_lambda| <= A_lambda log(2+|t|)/(1+|t|)`,

with `A_lambda -> 0` exponentially.

## Global zero samples and transfer to the sharp family

Riemann--von Mangoldt implies

`sum_rho multiplicity(rho)
  log(2+|Im rho|)^2/(1+|Im rho|)^2 < infinity`.

Dominated summation yields vanishing global zero-sample energy for the
regularized comparators.  The fixed-support logarithmic Paley--Wiener
sampling inequality then converts the vanishing logarithmic graph distance
between regularized and sharp vectors into vanishing zero-sample distance.
Infinite-series Cauchy--Schwarz transfers the residual limit to the original
sharp CCM family.

The dependence of the upper-sampling constant on the support is harmless but
must not be suppressed.  The usual local Plancherel--Polya proof gives at
most `exp(C lambda)` growth after allowing real parts throughout the centered
critical strip (and only polynomial growth on the critical line).  The
regularization error is `P(lambda) exp(-c lambda^2)` in a fixed positive
Sobolev norm.  Hence the sampling error still tends to zero.  This is the
quantitative content of `regularizationError_tendsto_zero` in the Lean
interface.

This transfer is essential: the sharp Fourier defect is not weighted
integrable merely because its endpoint jump is small.

## Lean composition and trust boundary

Lean packages the summable square height weight, fixed-support logarithmic
sampling, infinite-series Cauchy--Schwarz, the full form-domain extension,
the zero-free-region conversion, and the cofinal moving-support conclusion.
The remaining construction interface must distinguish the regularized
Mellin certificate from logarithmic-graph convergence back to the sharp CCM
family.  Its literature inputs are fixed-mode prolate asymptotics, Poisson
summation, the symmetric zero-free region, Riemann--von Mangoldt counting,
and Paley--Wiener sampling; neither RH nor Weil positivity is used.
