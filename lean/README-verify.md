# Verifying the Lean developments

Two main Lake projects (`glide` and `weilcert`), plus the small `rhbridge`
project that imports both for cross-project composition:

## 2. GlideKernel (lean/glide) — the archimedean kernel sandwich

```
cd lean/glide && lake exe cache get && lake build     # ~20 s after cache
lake env lean <file with: import Glide.Basic, #print axioms GlideKernel.kernel_lower, ...>
```
Verified output (2026-07-26):
```
'GlideKernel.kernel_lower'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.kernel_upper'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.frullani_cos'  depends on axioms: [propext, Classical.choice, Quot.sound]
'GlideKernel.laplace_sin'   depends on axioms: [propext, Classical.choice, Quot.sound]
```
Content: ½log(1+4r²) ≤ ∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t}) dt ≤ ½log(1+4r²)+8
for all real r — Lemma A of THEOREMS.md in integral form (the digamma
identification awaits Gauss's formula in mathlib; RH-LEMMA-MAP.md Level 2) —
plus the Laplace transform of sine and the Frullani-type integral as
standalone formalized lemmas.

`Glide.DigammaMonotone` now formalizes the positive-series core of F7. It
proves convergence and strict positivity of the candidate trigamma slope and
deduces strict monotonicity of `quarterDigammaReal` from the exact derivative
identity:

```
import Glide.DigammaMonotone
#print axioms GlideKernel.hasDerivAt_quarterDigammaReal_of_complex
#print axioms GlideKernel.quarterDigammaReal_neg
#print axioms GlideKernel.summable_quarterTrigammaTerm
#print axioms GlideKernel.summable_quarterTrigammaComplexTerm
#print axioms GlideKernel.quarterTrigammaSlope_eq_re_tsum
#print axioms GlideKernel.hasDerivAt_quarterDigammaReal_of_trigammaSeries
#print axioms GlideKernel.quarterTrigammaSlope_pos
#print axioms GlideKernel.quarterDigammaReal_strictMonoOn_of_hasDerivAt
#print axioms GlideKernel.quarterDigammaReal_exterior_lower_bound_of_hasDerivAt
```

All nine use only `[propext, Classical.choice, Quot.sound]`. Conjugation of
Gamma and its derivative also proves that `quarterDigammaReal` is even, so the
negative exterior half-line is no longer an analytic gap. The chain-rule
theorem converts a complex derivative of `Complex.digamma` into the required
real derivative, and `quarterTrigammaTerm_eq_re` checks every summand including
its factor and sign. `summable_quarterTrigammaComplexTerm` and
`quarterTrigammaSlope_eq_re_tsum` close the complex-`tsum`/real-part step, and
`hasDerivAt_quarterDigammaReal_of_trigammaSeries` converts the standard
complex trigamma derivative series directly to the exact real derivative.
`Glide.DigammaSeries` goes further by differentiating the finite Euler
`GammaSeq` logarithmic derivatives and passing through two locally uniform
limits:

```
import Glide.DigammaSeries
#print axioms GlideKernel.summable_trigammaSeries_term
#print axioms GlideKernel.hasDerivAt_digamma_of_gammaSeq_locallyUniform
#print axioms GlideKernel.hasDerivAt_quarterDigammaReal_of_gammaSeq_locallyUniform
#print axioms GlideKernel.quarterDigammaReal_exterior_lower_bound_of_gammaSeq_locallyUniform
```

These also use only `[propext, Classical.choice, Quot.sound]`. They derive the
standard trigamma derivative, strict monotonicity, and F7 exterior comparison
from locally uniform convergence of `Complex.GammaSeq`. `Glide.GammaUniform`
now proves that convergence unconditionally on `Re z>0`, so F7 has no remaining
premise:

```
import Glide.GammaUniform
#print axioms GlideKernel.gammaSeq_tendstoLocallyUniformlyOn
#print axioms GlideKernel.hasDerivAt_digamma_trigammaSeries
#print axioms GlideKernel.quarterDigammaReal_strictMonoOn
```

`Glide.DigammaBounds` closes the directed p=2 scalar ledger as well:

```
import Glide.DigammaBounds
#print axioms GlideKernel.p2Alpha_lower_bound
#print axioms GlideKernel.p2Omega_sub_alpha_abs_le
```

The first theorem proves `109387/100000 ≤ p2Alpha`; the second proves
`|p2Omega r-p2Alpha|≤7447/1000` on `|r|≤50`. Their proofs use an exact positive
rational series and explicit integral tails. All five declarations above have
axiom set `[propext, Classical.choice, Quot.sound]`. Gauss's digamma integral
remains a separate route needed for the broader kernel sandwich.

The same project also contains the abstract Hard Horizon development.  Its
paper-facing wrapper states the vanishing orders directly at `±tₖ`, rather
than at points of a recentered transform:

```
cd lean/glide
lake build Glide
cat >/tmp/check-hard-horizon.lean <<'EOF'
import Glide.HardHorizon
#print axioms HardHorizon.analyticOrderAt_translate
#print axioms HardHorizon.hard_horizon_of_global_orders
#print axioms HardHorizon.zero_desert
EOF
lake env lean /tmp/check-hard-horizon.lean
```

All three declarations depend only on `[propext, Classical.choice,
Quot.sound]`.  `analyticOrderAt_translate` proves that translation preserves
analytic order for an entire function, and
`hard_horizon_of_global_orders` uses it to match T1PRIME's global (S3)
hypothesis.  These remain abstract finite-head/staircase theorems: no zeta
zero-counting theorem is imported.  Also, `zero_desert` exports existence of
one zero-free Jensen radius and the corresponding divisor-remainder bound;
the paper's “any such radius” and subsequent zero-count corollary are not yet
separate Lean declarations.

# 1. Verifying the WeilCert development

Toolchain: Lean 4.32.1 (via elan), mathlib pinned by `weilcert/lake-manifest.json`.

```
cd lean/weilcert
lake exe cache get     # fetch mathlib oleans (~8.6k files)
lake build             # compiles Weilcert.lean; ~10 s after cache
lake build CertInstance # also compiles the generic-framework and real-matrix corollaries
lake build LegendreRodrigues # exact all-degree Rodrigues/plane-wave bridge
lake build LegendreOrthogonality # exact norm and orthonormality
lake build LegendreCoefficientTail # normalized coefficient tail
lake build LegendreScaled # arbitrary-interval scaling and tail
lake build LegendreL2 LegendreScaledL2 # complete L² bases and Parseval
lake build LegendrePlaneWaveL2 # pointwise F2 projection leakage
lake build IntervalZeroExtension FullInfFourierBridge # exact band operator and rho ledger
lake build PoleProjectionL2 FullInfOperatorLedger # concrete poles and block estimates
lake build FullInfClipped48 # exact L=7/4 clipped-block intervals; ~50 s after cache
lake build FullInfClipped48Real # direct strict scalar extension to real matrices
lake build FullInfClipped48Transfer # real certificate + L=7/4 projection ledger
lake build LegendreParityCoordinates # canonical even/odd coordinates and matrices
lake build SymbolQuadraticComparison # exact original-versus-clipped integral comparison
lake build FullInfP2Endpoint # specialized p=2 operator composition
```

Axiom audit (the entire point — run it yourself):

```
$ cat > /tmp/check.lean <<'EOF'
import Weilcert
import CertInstance
import CertFramework
import FullInfTransfer
import LegendreTail
import LegendrePlaneWave
import LegendreRodrigues
import LegendreOrthogonality
import LegendreCoefficientTail
import LegendreScaled
import HilbertBasisTail
import LegendreL2
import LegendreScaledL2
import LegendrePlaneWaveL2
import FullInfClipped48
import FullInfClipped48Real
import FullInfClipped48Transfer
#print axioms WeilCert.weil_window_positive
#print axioms WeilCert.mRat_positive
#print axioms WeilCert.key_int
#print axioms CertInstance.real_window_positive_via_framework
#print axioms CertFramework.two_by_two_strict_lower_bound
#print axioms CertFramework.hilbert_two_block_strict_lower_bound
#print axioms CertFramework.fullinf_p2_block_lower_bound
#print axioms CertFramework.fullinf_p3_block_lower_bound
#print axioms CertFramework.fullinf_n4_block_lower_bound
#print axioms FullInfTransfer.bilinear_two_block_strict_lower_bound
#print axioms FullInfTransfer.bilinear_decomposition_strict_lower_bound
#print axioms FullInfTransfer.starProjection_strict_lower_bound
#print axioms FullInfTransfer.fullinf_p2_projection_lower_bound
#print axioms FullInfTransfer.fullinf_p3_projection_lower_bound
#print axioms FullInfTransfer.fullinf_n4_projection_lower_bound
#print axioms LegendreTail.doubleFactorialMajorant_tsum_tail_le
#print axioms LegendreTail.weighted_sq_tsum_tail_le
#print axioms LegendreTail.weightIntegral_eq
#print axioms LegendreTail.norm_sphericalJIntegralModel_le
#print axioms LegendreTail.sphericalJIntegralModel_tsum_tail_le
#print axioms LegendrePlaneWave.rodriguesWeight_iterate_derivative_fourier
#print axioms LegendrePlaneWave.polyFourierIntegral_rodriguesWeight_eq_positive_phase
#print axioms LegendreRodrigues.rodrigues_plainLegendre
#print axioms LegendreRodrigues.polyFourierIntegral_plainLegendre_eq_sphericalJIntegralModel
#print axioms LegendreOrthogonality.plainLegendre_norm_sq
#print axioms LegendreOrthogonality.plainLegendre_pairwise_orthogonal
#print axioms LegendreOrthogonality.normalizedPlainLegendre_orthonormal
#print axioms LegendreCoefficientTail.normalizedPlainLegendre_coefficient_tsum_tail_le
#print axioms LegendreScaled.scaledNormalizedPlainLegendre_coefficient_tsum_tail_le
#print axioms HilbertBasisTail.tsum_nat_add_sq_norm_inner_eq_sub_sum
#print axioms LegendreL2.normalizedLegendreL2_dense_span
#print axioms LegendreL2.tsum_tail_eq_norm_starProjection_residual_sq
#print axioms LegendreScaledL2.scaledNormalizedLegendreL2_dense_span
#print axioms LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveReal
#print axioms LegendrePlaneWaveL2.planeWave_projection_residual_energy_le
#print axioms LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal
#print axioms FullInfClipped48.evenIntervalLowerBound
#print axioms FullInfClipped48.oddIntervalLowerBound
#print axioms FullInfClipped48.clipped48IntervalLowerBound
#print axioms FullInfClipped48Real.evenIntervalLowerBoundReal
#print axioms FullInfClipped48Real.oddIntervalLowerBoundReal
#print axioms FullInfClipped48Real.clipped48IntervalLowerBoundReal
#print axioms FullInfClipped48Transfer.p2_projection_lower_bound_of_clipped48_intervals
EOF
$ lake env lean /tmp/check.lean
'WeilCert.weil_window_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCert.mRat_positive' depends on axioms: [propext, Classical.choice, Quot.sound]
'WeilCert.key_int' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertInstance.real_window_positive_via_framework' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.two_by_two_strict_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.hilbert_two_block_strict_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.fullinf_p2_block_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.fullinf_p3_block_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'CertFramework.fullinf_n4_block_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.bilinear_two_block_strict_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.bilinear_decomposition_strict_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.starProjection_strict_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.fullinf_p2_projection_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.fullinf_p3_projection_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfTransfer.fullinf_n4_projection_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreTail.doubleFactorialMajorant_tsum_tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreTail.weighted_sq_tsum_tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreTail.weightIntegral_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreTail.norm_sphericalJIntegralModel_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreTail.sphericalJIntegralModel_tsum_tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendrePlaneWave.rodriguesWeight_iterate_derivative_fourier' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendrePlaneWave.polyFourierIntegral_rodriguesWeight_eq_positive_phase' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreRodrigues.rodrigues_plainLegendre' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreRodrigues.polyFourierIntegral_plainLegendre_eq_sphericalJIntegralModel' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreOrthogonality.plainLegendre_norm_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreOrthogonality.plainLegendre_pairwise_orthogonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreOrthogonality.normalizedPlainLegendre_orthonormal' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreCoefficientTail.normalizedPlainLegendre_coefficient_tsum_tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreScaled.scaledNormalizedPlainLegendre_coefficient_tsum_tail_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'HilbertBasisTail.tsum_nat_add_sq_norm_inner_eq_sub_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreL2.normalizedLegendreL2_dense_span' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreL2.tsum_tail_eq_norm_starProjection_residual_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreScaledL2.scaledNormalizedLegendreL2_dense_span' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveReal' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendrePlaneWaveL2.planeWave_projection_residual_energy_le' depends on axioms: [propext, Classical.choice, Quot.sound]
'LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48.evenIntervalLowerBound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48.oddIntervalLowerBound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48.clipped48IntervalLowerBound' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48Real.evenIntervalLowerBoundReal' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48Real.oddIntervalLowerBoundReal' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48Real.clipped48IntervalLowerBoundReal' depends on axioms: [propext, Classical.choice, Quot.sound]
'FullInfClipped48Transfer.p2_projection_lower_bound_of_clipped48_intervals' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`propext, Classical.choice, Quot.sound` are the three standard axioms of
mathlib; the absence of `Lean.ofReduceBool`/`Lean.trustCompiler` certifies that
no `native_decide` was used (all integer computations were reduced by the
kernel), and the absence of `sorryAx` certifies completeness.

What is proved: `WeilCert.weil_window_positive` gives the rational 12x12
matrix theorem, while `CertInstance.real_window_positive_via_framework`
casts the exact congruence certificate and applies the field-generic framework
directly over the reals.  Thus every real (not necessarily symmetric) 12x12
matrix within 1e-20 entrywise of the real scalar extension of `mRat` has a
strictly positive quadratic form on every nonzero real vector.  Strictness is
not inferred merely by density (which by itself would only give
nonnegativity).  By the Bridge Proposition of `../THEOREMS.md`
(computer-assisted, interval arithmetic, trust base stated there), the
truncated Weil form of zeta at support L = 497/200 in the 12-dimensional
Legendre test space is such a real matrix.

`CertFramework.two_by_two_strict_lower_bound` and
`hilbert_two_block_strict_lower_bound` kernel-check the scalar and abstract
inner-product-space versions of FULLINF F8. `FullInfTransfer` goes one step
further: for a symmetric bilinear form it expands the two blocks and applies
the theorem to the canonical orthogonal projection onto any subspace that
admits one. Its three named `fullinf_*_projection_lower_bound` theorems insert
the exact rational constants for all certified endpoints, leaving only the
finite, complement, and cross-block estimates as hypotheses.
`LegendreTail` now goes further than an abstract pointwise hypothesis. It
evaluates `∫_{-1}^1(1-t²)^k dt` exactly, defines a local oscillatory
`sphericalJIntegralModel`, proves its sharp double-factorial bound, and sums
its complete model coefficient tail. No identification with a library Bessel
function is asserted. `LegendrePlaneWave` proves the generic repeated
integration-by-parts and phase steps, while `LegendreRodrigues` transports
mathlib's shifted Legendre family to `[-1,1]`, proves its all-degree Rodrigues
formula, and proves exactly
`FI(P_n)=2*(-I)^n*sphericalJIntegralModel n z`, including `z=0`.
`LegendreOrthogonality` proves lower-degree and pairwise orthogonality, the
exact norm `2/(2n+1)`, and normalized Kronecker-delta orthonormality.
`LegendreCoefficientTail` and `LegendreScaled` give the exact normalized and
arbitrary-interval coefficient tails. `LegendreL2` and `LegendreScaledL2`
use Weierstrass density to construct complete real L² Hilbert bases, prove
Parseval and canonical finite-projection tail identities, and identify the
real and imaginary plane-wave coefficients. `LegendrePlaneWaveL2` proves the
complete pointwise real-form F2 leakage bound for `w` orthogonal to the first
`m` modes. `IntervalZeroExtension` then constructs canonical zero extension,
proves `L¹∩L²` compatibility with Mathlib's Plancherel transform, and gives the
exact band norm with its `z/(2π)` scaling. `FullInfFourierBridge` proves the
p=2 operator bound `ρ≤81/10^23`. `PoleProjectionL2` proves the concrete pole
norms and residuals, while `FullInfOperatorLedger` derives complement and cross
estimates from these facts. `FullInfClipped48` separately kernel-checks the
exact finite `L=7/4`, `m=48` rational certificate for two explicit
24-dimensional parity intervals, and `FullInfClipped48Real` casts the
congruence data to prove that every arbitrary real matrix in those intervals
has direct-sum quadratic form strictly above `(227/10^7)` times the squared
coordinate norm. This direct scalar extension preserves strictness without a
density argument. The generator checked that the Arb outward balls lie inside
radius `10^-12` rational intervals, but the analytic identification is
deliberately not a Lean premise. `FullInfClipped48Transfer` composes this real
finite certificate with the exact L=7/4 projection ledger, leaving the
analytic coordinate/form, interval, complement, and cross estimates as
premises. `LegendreParityCoordinates` now supplies canonical even/odd
coordinates, their exact norm identity, and the actual basis-entry matrices.
`SymbolQuadraticComparison` proves the exact clipped-band identity and the
inequality against the original, possibly unbounded, multiplier integral under
weighted integrability. `RHBridge.P2Parity` additionally proves exact even/odd
decoupling, and `RHBridge.P2RoundedBoundedCertificateCheck` proves containment
for the two canonical matrices with Lean-checked analytic errors. Thus the
remaining local p=2 gap is the zeta-form/domain/integrability
identification—not F7, Fourier normalization,
poles, operator algebra, scalar bounds, or coordinate representation.
The three named
`fullinf_*_block_lower_bound` corollaries
kernel-check the exact rational scalar arithmetic used at L=7/4, 497/200, and
749/250.

Further weilcert targets (same project, same audit procedure — full audits in
`../../results/`): `WeilcertDeep` (m=24, δ=1e−14), `WeilcertDeeper` (m=48,
δ=1e−19; ~10-min kernel check), `WeilcertFamily` (χ₋₇, L=5, m=16 — first
GRH-side window), `BridgeLegendre`/`BridgeOverlap` (49 overlap identities),
`CertFramework`/`CertInstance` (n-generic framework), `FullInfTransfer`
(orthogonal-projection F8), `LegendreTail`/`LegendrePlaneWave`/
`LegendreRodrigues`/`LegendreOrthogonality`/`LegendreCoefficientTail`/
`LegendreScaled`/`LegendreL2`/`LegendreScaledL2`/
`LegendrePlaneWaveL2`/`IntervalZeroExtension`/`FullInfFourierBridge` (the
complete p=2 F2/Fourier bridge), `PoleProjectionL2`/`FullInfOperatorLedger`,
`LegendreParityCoordinates`, `SymbolQuadraticComparison`, `FullInfP2Endpoint`,
`FullInfClipped48`/`FullInfClipped48Real`/
`FullInfClipped48Transfer` (the L=7/4 finite certificate and abstract
composition), and `CurveCertE5` —
the **first end-to-end kernel-checked window** (curve E: y²=x³+x+1 over F₅):
the point count #E(F₅)=9 is itself computed by `decide` over `ZMod 5` and the
Gram matrices are *defined* from it, so positivity (rung 2), the
Cayley–Hamilton kernel vector (rung 3), the sign-flip witness, and the
genus-2/F₇ block carry NO interval-arithmetic trust base at all (36 theorems,
audit in `../../results/agent-curve-lean.md`; build `lake build CurveCertE5`).

## 3. RHBridge (lean/rhbridge) — cross-project p=2 composition

```
cd lean/rhbridge
export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu # if cache compilation needs it
lake exe cache get
lake build RHBridge.P2RoundedBoundedCertificateCheck
lake env lean RHBridge/P2RoundedBoundedCertificateAudit.lean
```

`RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`
proves entrywise containment of the canonical even and odd matrices in the
stored intervals. Python/FLINT generates exact-rational candidates, but Lean
verifies the analytic truncation and rounding bounds, moment/matvec identities,
bounded product-error propagation, 608 range leaves covering all 19,200 entry
refinements, and final aggregation. Its corollary
`p2_canonical_clipped_endpoint` proves
`(22699/10^9) * ‖f‖² < p2ClippedForm f f` from only `f≠0`.

`RHP2Bridge.p2_original_integral_lower_bound_of_matrix_containment_no_parity` transfers
the same strict bound to the original unbounded p=2 weighted Fourier integral
plus the exact pole term. Canonical containment now discharges its finite
matrix hypotheses; weighted integrability is still explicit. This is not yet a
theorem about the zeta Weil form because the integral-plus-pole expression has
not been identified with that form on its precise domain.

For the focused axiom audit, run
`RHBridge/P2RoundedBoundedCertificateAudit.lean`, which includes:

```
#print axioms RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment
#print axioms RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_clipped_endpoint
```

All report only `[propext, Classical.choice, Quot.sound]`.

Note on the multiarch clang issue: if `lake exe cache get` fails building the
cache tool with `bits/libc-header-start.h not found`, set
`export C_INCLUDE_PATH=/usr/include/x86_64-linux-gnu` first (Ubuntu multiarch).

Regenerating the certificate data from the analytic side:
`python3` + the repository's `src/certified_spectral.py` produce the integer
data (see the generator embedded in the session record / scratch scripts);
the LDL^T pivots, the integer congruence c^2 B = W^T diag(g) W, and the
inverse identity Winv W = f I are all re-verified exactly in Fractions before
emission.
