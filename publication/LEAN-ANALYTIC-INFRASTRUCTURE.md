# Reusable analytic infrastructure in Lean

Status: declaration-level exposition of the 2026-08-05 repository snapshot.

This note describes the part of the repository that can be read as ordinary
formalized analysis rather than as an RH experiment.  Its unit of exposition is
a short theorem arc: definitions, normalization, mathematical statement, proof
idea, and exact Lean endpoint.  None of the arcs below uses a generated
positivity certificate, an RH hypothesis, or a project-specific literature
axiom.

The point is not that these classical theorems are mathematically new.  The
potential contribution is a checked and reusable Lean API.  Claims about
upstream novelty still require comparison with current mathlib immediately
before submission.

## 1. Normalization ledger

The following conventions are part of the statements, not cosmetic choices.

| Topic | Convention in the checked declarations |
|---|---|
| Digamma | `Complex.digamma z` is mathlib's logarithmic derivative of `Complex.Gamma`; all series and kernel theorems below assume `0 < z.re` (or `0 < a`). |
| Real-line Fourier transform | `FourierTransform.fourier` uses the unitary ordinary-frequency convention $\widehat f(\xi)=\int_{\mathbb R}e^{-2\pi i x\xi}f(x)\,dx$. |
| Translation | `RHP2Bridge.AutocorrelationPlancherel.translateFn u f x = f (x + u)`, hence $\widehat{T_u f}(\xi)=e^{2\pi i u\xi}\widehat f(\xi)$. |
| Complex inner product | Mathlib's complex inner product is conjugate-linear in the first argument and linear in the second.  Thus the time-domain integrand is $\overline{f(x)}g(x+u)$. |
| Compact Fourier--Laplace transform | `transform phi a z` uses $e^{-izx}$, with no $2\pi$.  It is therefore a different frequency normalization from `FourierTransform.fourier`. |
| Legendre pairing | Unweighted Lebesgue pairing $\int_a^b p(x)q(x)\,dx$; the Hilbert spaces are real `L2` spaces over interval subtypes with transported Lebesgue measure. |
| Rectangle contour | `rectBoundaryIntegral` is positive when the first corner has smaller real and imaginary coordinates than the second.  A Cauchy kernel contributes $2\pi i$. |
| Simple principal part | The local term is $r/(z-p)$.  `HasSimplePrincipalPartAt` permits $r=0$; `HasSimplePoleAt` additionally requires $r\ne0$. |

The two Fourier conventions should not be silently identified.  On the real
axis, `CompactSupportFourierLaplace.transform phi a (2 * pi * xi)` matches the
phase of the ordinary-frequency transform restricted to `[-a,a]`.

## 2. Dependency map

The reusable mathematical flow is:

```text
mathlib Gamma integral and GammaSeq formulas
  -> GammaSeq locally uniform on Re z > 0
  -> Gauss two-point digamma series and the trigamma derivative series
  -> positive-vertical-line Gauss kernel and logarithmic bounds

mathlib Lp Fourier transform + tempered distributions
  -> pointwise/L2 Fourier compatibility for L1 intersect L2
  -> L2 translation law
  -> cross-correlation Plancherel
  -> real autocorrelation / cosine-energy identity

mathlib shifted Legendre polynomials
  -> unshifted Rodrigues formula
  -> exact polynomial orthogonality and norm
  -> complete Hilbert basis on [-1,1]
  -> unitary dilation and translation to [b,c]
  -> Parseval and exact projection tails

mathlib Cauchy integral API
  -> simultaneous removal of finitely many simple principal parts
  -> circle formulas (including Banach-valued residues)
  -> rectangle subdivision and finite-simple-pole rectangle formula

compact interval L2-to-L1 + differentiation under the integral
  -> entire Fourier--Laplace transform
  -> exponential-type estimate and translated estimate
```

These are theorem dependencies.  The present source imports are sometimes
broader than this diagram, especially in the Legendre files; import reduction
is an extraction task, not a missing mathematical implication.

## 3. Gamma, digamma, and the Gauss vertical kernel

### 3.1 Source modules

- [`DigammaVertical.lean`](../lean/glide/Glide/DigammaVertical.lean)
- [`DigammaSeries.lean`](../lean/glide/Glide/DigammaSeries.lean)
- [`GammaUniform.lean`](../lean/glide/Glide/GammaUniform.lean)
- [`BasicCore.lean`](../lean/glide/Glide/BasicCore.lean)
- [`DigammaKernel.lean`](../lean/glide/Glide/DigammaKernel.lean)

The quarter-line and certificate-facing bridge modules are deliberately not
part of this arc.

### 3.2 The series arc

For `Re z, Re w > 0`, define

$$
 d_n(z,w)=\frac1{w+n}-\frac1{z+n}.
$$

`Complex.summable_digammaDifferenceTerm` proves absolute summability.  The
finite logarithmic derivative of Euler's Gamma approximant is computed first.
`GlideKernel.digamma_sub_eq_tsum_of_gammaSeq_locallyUniform` then isolates the
only analytic limit needed at this stage: locally uniform convergence of
`GammaSeq` on the positive half-plane.  It concludes

$$
 \psi(z)-\psi(w)=\sum_{n\ge0}d_n(z,w).
$$

The same locally uniform input, differentiated through mathlib's analytic
limit API, gives

$$
 \psi'(z)=\sum_{n\ge0}\frac1{(z+n)^2}.
$$

`Glide.GammaUniform` discharges that input.  Its central declaration is
`Complex.GammaSeq_tendstoLocallyUniformlyOn_re_pos`.  The proof rewrites the
Euler approximants as integrals and applies dominated convergence on the
product filter `atTop ×ˢ 𝓝 z`.  Near a fixed positive-real point it uses the
two-exponent majorant

$$
 e^{-x}x^{a-1}+e^{-x}x^{b-1},\qquad 0<a\le \Re z\le b,
$$

which is integrable both at zero and at infinity.  This is the limit-control
step that turns the conditional series module into an unconditional theorem.

The principal public endpoints are:

| Declaration | Checked mathematical content |
|---|---|
| `Complex.GammaSeq_tendstoLocallyUniformlyOn_re_pos` | Euler's `GammaSeq` converges locally uniformly to `Gamma` on `Re z > 0`. |
| `Complex.digamma_sub_eq_tsum` | Exact absolutely convergent two-point Gauss series. |
| `Complex.hasDerivAt_digamma` and `Complex.deriv_digamma` | The derivative of digamma is the trigamma series on `Re z > 0`. |
| `Complex.digamma_eq_neg_eulerMascheroniConstant_add_tsum` | The one-point series normalized by $\psi(1)=-\gamma$. |
| `Complex.digamma_conj` | Digamma commutes with conjugation. |
| `GlideKernel.verticalDigammaReal_neg` | `y -> Re psi(a + i y)` is even. |

### 3.3 The positive vertical-line kernel

For `a > 0`, the real summand is made explicit by
`GlideKernel.verticalDigammaDifferenceTerm_eq`:

$$
 \frac1{n+a}-\frac{n+a}{(n+a)^2+y^2}\ge0.
$$

Writing the reciprocal as a Laplace integral, using Tonelli/Fubini for the
nonnegative summands, and summing the geometric series gives the exact Gauss
kernel identity

$$
 \Re\psi(a+iy)-\Re\psi(a)
 =\int_0^\infty
   \frac{e^{-at}(1-\cos(yt))}{1-e^{-t}}\,dt.
$$

This is
`GlideKernel.verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral`,
with the namespace-neutral wrapper
`Complex.re_digamma_add_mul_I_sub_eq_integral`.

The elementary comparison

$$
 \frac1t\le\frac1{1-e^{-t}}\le\frac1t+1
 \quad(t>0)
$$

and the formally proved Frullani identity `GlideKernel.frullani_cos` yield

$$
 \frac12\log\!\left(1+\frac{y^2}{a^2}\right)
 \le \Re\psi(a+iy)-\Re\psi(a)
$$

and

$$
 \Re\psi(a+iy)-\Re\psi(a)
 \le \frac12\log\!\left(1+\frac{y^2}{a^2}\right)
      +\frac1a-\frac{a}{a^2+y^2}.
$$

The Lean endpoints are `GlideKernel.verticalDigammaReal_log_lower` and
`GlideKernel.verticalDigammaReal_log_upper`, with corresponding declarations
in namespace `Complex`.

### 3.4 Trust, extraction, and nonclaims

The selected endpoints are audited in
[`Glide/UpstreamAudit.lean`](../lean/glide/Glide/UpstreamAudit.lean).  Their
printed dependencies are only `propext`, `Classical.choice`, and `Quot.sound`.
There is no assumed asymptotic expansion and no literature axiom.

A review-sized upstream split is:

1. conjugation and vertical-line continuity;
2. local uniform convergence of `GammaSeq`;
3. the two-point and derivative series;
4. the elementary Laplace/Frullani lemmas;
5. the Gauss kernel and its two-sided bound.

The first three belong naturally near mathlib's Gamma/digamma API; the last
two may be more reviewable as separate integral and special-function files.
Fixed values such as `a = 1/4`, prime weights, and RH terminology should remain
outside the extraction.

This arc does **not** prove a global meromorphic trigamma expansion across the
Gamma poles, an optimal asymptotic remainder, or any statement about zeta
zeros.  Its domain is explicitly the positive-real half-plane.

## 4. Real-line Plancherel and autocorrelation

### 4.1 Source and hypotheses

The complete standalone arc is
[`AutocorrelationPlancherelCore.lean`](../lean/rhbridge/RHBridge/AutocorrelationPlancherelCore.lean).
It has no zeta or certificate import.

`RHP2Bridge.AutocorrelationPlancherel.FullLineL2` abbreviates
`Lp Complex 2 volume` on the real line.
`RHP2Bridge.AutocorrelationPlancherel.toFullLineL2` turns a function with a
`MemLp 2` proof into that space, and
`RHP2Bridge.AutocorrelationPlancherel.translateFn u f` is the right translate
`x -> f (x + u)`.

The main compatibility lemma,
`RHP2Bridge.AutocorrelationPlancherel.coe_fourier_toFullLineL2_ae_eq_fourierFn`,
assumes `f` is in both `L1` and `L2`.  It identifies almost everywhere:

- the function underlying mathlib's unitary `L2` Fourier operator, and
- mathlib's pointwise Fourier integral.

The proof tests the two locally integrable representatives against compactly
supported smooth functions, uses the tempered-distribution Fourier identity
and Fubini, and invokes uniqueness of distributions represented by locally
integrable functions.  This is the substantive bridge; it is not a change of
notation.

### 4.2 Translation and correlation

`RHP2Bridge.AutocorrelationPlancherel.coe_fourier_translateL2` proves, almost
everywhere,

$$
 \widehat{g(\mathord\cdot+u)}(\xi)
   =e^{2\pi i u\xi}\widehat g(\xi).
$$

For `f in L2` and `g in L1 intersect L2`, the human-facing
`RHP2Bridge.AutocorrelationPlancherel.integral_inner_translate_eq_integral_fourier`
states

$$
 \int_{\mathbb R}\langle f(x),g(x+u)\rangle_{\mathbb C}\,dx
 =\int_{\mathbb R}
   \left\langle\widehat f(\xi),
     e^{2\pi i u\xi}\widehat g(\xi)\right\rangle_{\mathbb C}\,d\xi.
$$

The asymmetric hypotheses are intentional: `f` only needs an `L2` Fourier
representative, while the current translation bridge for `g` passes through
its pointwise `L1` transform.

Taking `g=f` and real parts gives the Wiener--Khinchin endpoint
`RHP2Bridge.AutocorrelationPlancherel.integral_re_inner_translate_eq_cos_fourier_energy`:

$$
 \int_{\mathbb R}\Re\langle f(x),f(x+u)\rangle\,dx
 =\int_{\mathbb R}\cos(2\pi u\xi)|\widehat f(\xi)|^2\,d\xi,
$$

for `f in L1 intersect L2`.  Plancherel contributes no extra scalar because
the Fourier operator is unitary in this normalization.

### 4.3 Trust, extraction, and nonclaims

The two human-facing endpoints are printed by
[`RHBridge/ReusableAudit.lean`](../lean/rhbridge/RHBridge/ReusableAudit.lean)
and depend only on the three standard Lean axioms listed above.

The strongest upstream seam is the `L1 intersect L2` compatibility declaration
itself.  Once that is available, translation and correlation are short and
can be proposed separately.  A polished extraction should move the namespace
out of `RHP2Bridge`, add a simple non-number-theoretic example, and consider
generalizing the scalar codomain where mathlib's Fourier API permits it.

This file does **not** provide a pointwise theorem for arbitrary `L2`
representatives, a pure-`L2` formulation of every displayed integral, a
locally compact abelian group version, or a spectral-density theorem for
stochastic processes.  Equality of `L2` representatives remains almost
everywhere equality.

## 5. Compact-support Fourier--Laplace transforms

### 5.1 Source, statement, and proof

The source is
[`CompactSupportFourierLaplace.lean`](../lean/glide/Glide/CompactSupportFourierLaplace.lean).
For `a > 0`, it defines

$$
 F_\varphi(z)=\int_{[-a,a]}\varphi(x)e^{-izx}\,dx.
$$

The identity `exponent_re` records the sign check

$$
 \Re(-izx)=x\,\Im z,
$$

so the norm of the integrand is
`norm(phi x) * exp (x * z.im)`.

`CompactSupportFourierLaplace.differentiable_transform` assumes only that
`phi` is integrable on the interval and proves
`Differentiable Complex (transform phi a)`, i.e. that the transform is entire.
Around each `z0`, differentiation under the integral is justified by the
integrable local majorant

$$
 |\varphi(x)|\,e^{a(|\Im z_0|+1)}a.
$$

For the intrinsic `L2` interface,
`CompactSupportFourierLaplace.integrableOn_of_integrableOn_norm_sq` proves
`L2 subset L1` on this finite interval from strong measurability and
integrability of `norm(phi x)^2`.  Consequently
`CompactSupportFourierLaplace.differentiable_transform_of_integrableOn_norm_sq`
proves entirety from those two hypotheses.

Cauchy--Schwarz and `|x| <= a` give
`CompactSupportFourierLaplace.norm_transform_le_sqrt_integral_sq_mul_exp`:

$$
 |F_\varphi(z)|
 \le
 \left(\int_{-a}^a|\varphi(x)|^2dx\right)^{1/2}
 \sqrt{2a}\,e^{a|\Im z|}.
$$

If the squared `L2` norm is at most one,
`CompactSupportFourierLaplace.norm_transform_le_exp_of_integral_sq_le_one`
removes the first factor.
`CompactSupportFourierLaplace.norm_transform_translate_le_exp_of_integral_sq_le_one`
observes that a real translation of `z` does not alter the bound.  Finally,
`CompactSupportFourierLaplace.analyticOrderAt_translate` proves that
translation preserves local analytic order for an entire function.

### 5.2 Trust, extraction, and nonclaims

The main entirety, `L2-to-L1`, growth, and analytic-order endpoints are in
`Glide/UpstreamAudit.lean`; the audit reports only the standard Lean axioms.

The module is already independent of the RH development.  The likely
extraction seam is to upstream the `L2-to-L1` bridge and entirety theorem
first, followed by the quantitative growth corollaries.  A more ambitious
mathlib design may parameterize a compact measurable set or start from a
globally defined function with `HasCompactSupport`; that generalization is not
needed to understand the current theorem.

This is the forward elementary half of Paley--Wiener theory.  It does **not**
prove a converse support theorem, characterize an image space, determine the
exact exponential type, or use the ordinary-frequency `2*pi` convention.
The factor `sqrt (2*a) * exp (a*abs (Im z))` is a convenient uniform bound,
not a claim of pointwise sharpness.

## 6. Legendre orthogonality, Hilbert bases, and projection tails

### 6.1 Source modules

- [`LegendreRodrigues.lean`](../lean/weilcert/LegendreRodrigues.lean)
- [`LegendreOrthogonality.lean`](../lean/weilcert/LegendreOrthogonality.lean)
- [`LegendreL2.lean`](../lean/weilcert/LegendreL2.lean)
- [`LegendreScaled.lean`](../lean/weilcert/LegendreScaled.lean)
- [`LegendreIntervalL2.lean`](../lean/weilcert/LegendreIntervalL2.lean)
- optional plane-wave layer:
  [`LegendrePlaneWaveL2.lean`](../lean/weilcert/LegendrePlaneWaveL2.lean)

The base arc contains no matrices or generated certificates.

### 6.2 From mathlib's polynomial to Rodrigues and orthogonality

`LegendreRodrigues.shiftedLegendreReal` maps mathlib's integer shifted
Legendre polynomial to real coefficients.  The analysis-facing convention is

$$
 P_n(X)=\operatorname{shiftedLegendre}_n((1-X)/2),
$$

implemented by `LegendreRodrigues.plainLegendre`.  With
`rodriguesWeight n = (1-X^2)^n`, `rodrigues_plainLegendre` proves the
division-free polynomial identity

$$
 2^n n! P_n(X)=(-1)^n\frac{d^n}{dX^n}(1-X^2)^n.
$$

The proof is anchored to mathlib's independently defined shifted family: an
iterated affine chain rule transfers its Rodrigues formula and then clears the
powers of two.

`LegendreOrthogonality.polynomialPairIntegral p q a b` is the signed interval
integral of `p.eval x * q.eval x`.  Repeated integration by parts, with the
first `n` endpoint jets of `(1-X^2)^n` vanishing, shows that `P_n` is
orthogonal to every polynomial of degree below `n`.  Degree comparison gives
pairwise orthogonality.  A separate top-coefficient and weight-integral
calculation gives

$$
 \int_{-1}^{1}P_n(x)^2\,dx=\frac{2}{2n+1}.
$$

The normalized polynomial

$$
 \widetilde P_n=\sqrt{\frac{2n+1}{2}}P_n
$$

is `LegendreOrthogonality.normalizedPlainLegendre`, and
`normalizedPlainLegendre_orthonormal` states its exact Kronecker-delta
pairing.

Useful declaration landmarks are:

| Declaration | Role |
|---|---|
| `LegendreRodrigues.iterate_derivative_comp_affine` | Reusable iterated affine chain rule for polynomials. |
| `LegendreRodrigues.rodrigues_plainLegendre` | All-degree Rodrigues identity. |
| `LegendreOrthogonality.polynomialPairIntegral_iterate_derivative_of_boundary_zero` | General repeated integration-by-parts lemma. |
| `LegendreOrthogonality.plainLegendre_orthogonal_of_natDegree_lt` | Triangular orthogonality statement. |
| `LegendreOrthogonality.plainLegendre_pair_self` | Exact norm `2/(2*n+1)`. |
| `LegendreOrthogonality.normalizedPlainLegendre_orthonormal` | Polynomial-level orthonormality. |

### 6.3 Completeness on `[-1,1]`

`LegendreL2.intervalMeasure` is Lebesgue measure transported to the subtype
`Set.Icc (-1) 1`, and `LegendreL2.IntervalL2` is the corresponding real `L2`
space.  `inner_polynomialToL2` identifies the Hilbert inner product of
polynomial classes with the ordinary interval integral.

Completeness is proved in three human-readable steps:

1. exact degree `n` makes the normalized family a `Polynomial.Sequence`, so
   its algebraic span is every real polynomial
   (`LegendreL2.normalizedPlainLegendre_span`);
2. Weierstrass approximation makes polynomial evaluations dense in the
   continuous functions on the compact interval
   (`LegendreL2.polynomialToContinuousMap_denseRange`);
3. continuous functions are dense in finite-measure `L2`, giving
   `LegendreL2.polynomialToL2_denseRange` and then
   `LegendreL2.normalizedLegendreL2_dense_span`.

`LegendreL2.normalizedLegendreHilbertBasis` packages the result as a genuine
`HilbertBasis Nat Real IntervalL2`.  The main consequences are:

$$
 \sum_{n\ge0}|\langle\widetilde P_n,f\rangle|^2=\|f\|_2^2
$$

from `LegendreL2.tsum_sq_norm_inner_normalizedLegendreL2`, and the exact
finite-section
identity

$$
 \left\|f-\operatorname{proj}_{<m}f\right\|_2^2
 =\sum_{n\ge0}|\langle\widetilde P_{m+n},f\rangle|^2
$$

from `LegendreL2.tsum_tail_eq_norm_starProjection_residual_sq`.  The explicit
finite sum is identified with mathlib's canonical orthogonal projection by
`LegendreL2.finiteLegendreSubspace_starProjection`.

### 6.4 Unitary scaling and arbitrary intervals

For `a > 0`, `LegendreScaled.scaledNormalizedPlainLegendre a n` is

$$
 a^{-1/2}\widetilde P_n(x/a).
$$

`LegendreScaled.scaledNormalizedPlainLegendre_pair` proves directly by change
of variables that this dilation preserves the pairing on `[-a,a]`, and
`LegendreScaled.scaledNormalizedPlainLegendre_orthonormal` gives the delta
formula.

For `b < c`, set

$$
 d=(b+c)/2,\qquad r=(c-b)/2.
$$

`LegendreIntervalL2.normalizedLegendrePolynomial b c n` translates the
symmetric mode by `d`.  In ordinary notation its evaluation is

$$
 \sqrt{\frac{2n+1}{c-b}}
 P_n\!\left(\frac{2x-b-c}{c-b}\right).
$$

`LegendreIntervalL2.normalizedLegendrePolynomial_pair` proves exact
orthonormality on `[b,c]`.
The file then repeats the transparent polynomial-density argument on the
actual interval subtype, rather than hiding it behind an unformalized affine
identification.  It exports:

- `LegendreIntervalL2.normalizedLegendreHilbertBasis b c hbc`;
- the coefficient isometry `LegendreIntervalL2.FourierLegendre.transform`;
- arbitrary-interval Parseval,
  `LegendreIntervalL2.FourierLegendre.parseval`;
- the canonical finite projection,
  `LegendreIntervalL2.FourierLegendre.finiteSubspace_starProjection`;
- the exact tail/error identity,
  `LegendreIntervalL2.FourierLegendre.projection_error`.

The optional plane-wave layer uses the phase `exp (-i*z*x)`.  It derives exact
Legendre coefficients from Rodrigues and integration by parts and packages
the omitted coefficient energy as a projection residual.  The endpoint
`LegendrePlaneWaveL2.complexPlaneWave_projection_tail` includes both the exact
tail identity and an explicit geometric/double-factorial upper bound.  This
layer is useful, but it should be reviewed separately from the basic Hilbert
basis.

### 6.5 Trust, extraction, and nonclaims

[`Weilcert/UpstreamAudit.lean`](../lean/weilcert/Weilcert/UpstreamAudit.lean)
prints the axioms of the arbitrary-interval pairing, Hilbert basis, Parseval,
projection error, and plane-wave tail.  Each uses only `propext`,
`Classical.choice`, and `Quot.sound`.

The clean upstream decomposition is:

1. the real Legendre polynomial convention and Rodrigues bridge;
2. polynomial integration by parts, orthogonality, and exact norm;
3. the `[-1,1]` Hilbert basis and Parseval;
4. a reusable affine `L2` transport, or the present direct `[b,c]` basis;
5. plane-wave coefficients and quantitative tails as a separate extension.

The current imports are not yet minimal: `LegendreRodrigues` reaches the
Rodrigues weight through the plane-wave layer.  Extraction should move the
weight and polynomial-only integration-by-parts facts into the base files,
leaving spherical-function models and quantitative tails downstream.

This arc does **not** formalize weighted Jacobi spaces, numerical stability of
coefficient evaluation, or a complex Legendre Hilbert basis.  The complex
plane-wave residual is presently represented by the sum of real and imaginary
real-`L2` residual energies.  The name `sphericalJIntegralModel` is an integral
model; the source explicitly does not identify it with a library Bessel
function.

## 7. Finite simple poles and rectangle residues

### 7.1 Source modules and local predicate

- [`SimplePole.lean`](../lean/rhbridge/RHBridge/SimplePole.lean)
- [`ComplexResidue.lean`](../lean/rhbridge/RHBridge/ComplexResidue.lean)

`RHBridge.ComplexResidue.HasSimplePrincipalPartAt h p r` means that some
function differentiable at `p` agrees with

$$
 h(z)-\frac r{z-p}
$$

on a punctured neighborhood of `p`.  Allowing `r=0` makes the same predicate
cover removable singularities.  `RHBridge.ComplexResidue.HasSimplePoleAt`
adds `r ≠ 0`.

For a finite set of poles,
`RHBridge.ComplexResidue.finitePoleRegularization` subtracts every
principal part away from the poles and fills each missing value with its local
remainder after subtracting the other, nonsingular principal parts.
`RHBridge.ComplexResidue.differentiableOn_finitePoleRegularization` proves
this piecewise definition is differentiable on a supplied set.  Its global
specialization and exact reconstruction yield
`RHBridge.ComplexResidue.exists_entire_add_finite_simplePrincipalParts`:

$$
 h(z)=g(z)+\sum_{p\in P}\frac{r_p}{z-p}\qquad(z\notin P),
$$

where `g` is entire, provided `h` is differentiable off `P` and has each
specified local principal part.

This is simultaneous singularity removal.  No separation condition on the
finite poles is built into the statement; a `Finset Complex` has distinct
members by construction.

### 7.2 Circle formulas

`RHBridge.ComplexResidue.simplePrincipalPart p r z = (z-p)^(-1) * r`.  If
`p` lies in the open ball bounded by the circle,
`RHBridge.ComplexResidue.circleIntegral_simplePrincipalPart` proves

$$
 \oint\frac r{z-p}\,dz=2\pi i r.
$$

`RHBridge.ComplexResidue.circleIntegral_sub_inv_smul` is the same result for a
residue vector in any complete complex normed space.  Linearity and the zero
integral of a holomorphic remainder give
`RHBridge.ComplexResidue.circleIntegral_add_finite_sub_inv_smul`, the
Banach-valued finite-sum
formula.  Scalar wrappers include the empty pole set and extensional variants
whose decomposition only has to agree with the target function on the
contour.

The holomorphic remainder hypothesis in the finite circle formula is
mathlib's `DiffContOnCl Complex g (ball c R)`; the empty-set version also
requires `0 <= R`.  Every listed pole must lie in `ball c R`, so no pole is on
the contour.

### 7.3 Rectangle formulas

`RHBridge.ComplexResidue.rectBoundaryIntegral f z w` is the signed sum of the
four real interval integrals around the axis-aligned rectangle.  The bridge
`RHBridge.ComplexResidue.rectBoundaryIntegral_eq_wedgeIntegral_add` identifies
it with mathlib's two opposite `wedgeIntegral`s, and
`RHBridge.ComplexResidue.rectBoundaryIntegral_eq_zero_of_differentiableOn` is
Cauchy--Goursat on the closed unordered rectangle.

`RHBridge.ComplexResidue.RectIntegrable` records integrability on the four
parametrized edges.  The module proves linearity, finite-sum rules, vertical
and horizontal splitting, and gluing.  The key geometric lemma
`RHBridge.ComplexResidue.rectBoundaryIntegral_eq_center_of_three_by_three_frame`
says that if the eight cells of a `3 × 3` frame have zero boundary integral,
the outer boundary equals the central boundary.

For one Cauchy kernel the proof proceeds as follows:

1. compute the integral of `z^(-1)` on a centered square explicitly, reducing
   the four sides to the elementary integral of `(r^2+x^2)^(-1)`;
2. translate the square to an arbitrary pole;
3. surround the pole by a square strictly inside the outer rectangle;
4. apply the `3 × 3` frame lemma, with Cauchy--Goursat on the eight pole-free
   cells.

This yields `RHBridge.ComplexResidue.rectBoundaryIntegral_sub_inv`.  Linearity
then gives the public finite formula.  The most human-facing version is
`RHBridge.ComplexResidue.rectBoundaryIntegral_finite_simplePoles_of_mem_openRectangle`:
if `g` is differentiable on the closed rectangle and every listed pole is
strictly inside it, then

$$
 \int_{\partial R}\left(g(z)+
   \sum_i\frac{r_i}{z-p_i}\right)dz
 =2\pi i\sum_i r_i.
$$

The local radii are selected internally.  They need not be pairwise disjoint,
because the proof evaluates and sums each Cauchy kernel separately.  The
declaration
`RHBridge.ComplexResidue.wedgeIntegral_add_wedgeIntegral_finite_simplePoles_of_mem_openRectangle`
exports the same result in mathlib's native wedge language.

### 7.4 Trust, extraction, and nonclaims

[`SimplePoleAudit.lean`](../lean/rhbridge/RHBridge/SimplePoleAudit.lean) and
[`ComplexResidueAudit.lean`](../lean/rhbridge/RHBridge/ComplexResidueAudit.lean)
print the axioms for the regularization, circle, subdivision, one-pole, and
finite-pole endpoints.  All reported dependencies are the three standard Lean
axioms.

The most independent upstream unit is `SimplePole.lean`: the local predicate,
simultaneous regularization, and Banach-valued circle formula.  The rectangle
layer should be coordinated with current work on mathlib's residue API and
rectangle theorem rather than advertised as an unrelated new development.
Within that layer, `RHBridge.ComplexResidue.RectIntegrable` and the
subdivision/gluing lemmas may be
useful even if upstream ultimately proves the final residue theorem by a
different route.

This package does **not** define arbitrary Laurent coefficients, higher-order
poles, winding-number contour integrals, or a general residue theorem for all
meromorphic functions and all cycles.  The public rectangle theorem applies
to an explicit finite sum of simple principal parts plus a holomorphic
remainder.
`RHBridge.ComplexResidue.exists_entire_add_finite_simplePrincipalParts`
supplies such a decomposition under its stronger global off-pole
differentiability hypothesis; the module does not pretend that every local
meromorphic problem has already been packaged into that interface.

## 8. Axiom and reproduction record

The audits used for this map can be replayed independently:

```bash
cd lean/glide
lake env lean Glide/UpstreamAudit.lean

cd ../rhbridge
lake env lean RHBridge/ReusableAudit.lean
lake env lean RHBridge/SimplePoleAudit.lean
lake env lean RHBridge/ComplexResidueAudit.lean

cd ../weilcert
lake env lean Weilcert/UpstreamAudit.lean
```

For every endpoint named by those audit files, the current output is a subset
of:

```text
[propext, Classical.choice, Quot.sound]
```

These are ordinary foundational dependencies of the Lean/mathlib
development.  In particular, the audits print no `GuinandWeilLiterature`, no
project oracle, and no certificate assumption.  `noncomputable` definitions
such as a Hilbert basis or an `Lp` representative use classical choice; that
is not numerical computation and is not a hidden analytic hypothesis.

An upstream submission should still add a minimal audit or example in the
extracted namespace, because a source-level import can contain declarations
that the advertised endpoint does not actually depend on.  The declaration
audit establishes logical dependency; import minimization establishes that
the contribution is reviewable.

## 9. Recommended exposition and extraction order

For human review, the material should not be submitted as one large
number-theory package.  A sensible order is:

1. **Fourier representative compatibility.**  It is a sharply isolated
   bridge between existing `L1` and `L2` APIs, and the correlation formulas
   become short applications.
2. **Gamma/digamma series.**  Present the locally uniform Gamma limit before
   differentiating it; then make the Gauss kernel a separate integral
   application.
3. **Finite principal-part removal.**  Upstream the local predicate and circle
   formulas before deciding how they should meet the evolving general residue
   API.
4. **Legendre basis.**  Separate polynomial orthogonality from Hilbert-space
   completeness and keep quantitative plane-wave tails downstream.
5. **Compact Fourier--Laplace entirety.**  Submit the compact-interval theorem
   with its exact phase and growth normalization; discuss broader
   Paley--Wiener abstractions only as future API design.

Each unit should include one conventional mathematical example, a short proof
outline matching the Lean decomposition, an exact normalization note, and the
smallest `#print axioms` audit for its public endpoint.  Generated
certificates, zeta-specific constants, and research-program terminology are
not needed to explain or justify any theorem in this document.
