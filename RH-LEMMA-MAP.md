# RH-LEMMA-MAP: from this repository's formal artifacts to `RiemannHypothesis`

Mathlib states RH (`Mathlib/NumberTheory/LSeries/RiemannZeta.lean`:
`def RiemannHypothesis : Prop`). This document is the honest dependency map
from what is FORMALIZED HERE to that statement, level by level, with each gap
named and sized. It is the program's Track-A/F ledger (PROGRAM.md §4) in
actionable form, and the index of "lemmas that help pursue the final goal."

## The standing objective and its three-outcome structure

The program's ultimate goal (standing directive, 2026-07-26): proof, disproof,
or proven ZFC-independence of RH, pursued by incremental lemma accumulation.
The outcomes are NOT symmetric, and the lemma streams serve them differently:

- **DISPROOF** — the finitely-certifiable branch (RH is Π₁). Our machinery is
  sign-symmetric: a rigorously bridged negative Rayleigh quotient for an
  actual admissible test function, with every prime power allowed by its
  support included, is a finite disproof. A negative eigenvalue of a rounded
  or proxy matrix is not such a disproof until its analytic bridge is proved.
  Proposed disproof-side lemmas include NT-4 (quantitative converse Weil: an
  off-line zero at (½+δ₀, γ₀) should force λ(L₀) < 0 at explicit L₀; NT-4 is
  not proved in this repository), CO-4
  (the odd-sector one-scalar channel θ(L) ≤ 1), Track D's four hunters, and
  the certificate depth law (which prices how deep a disproof certificate
  must go). Every certified-positivity tool doubles as a disproof tool.
- **PROOF** — requires a full-domain uniform statement (UPT, §3 of
  PROGRAM.md), together with the analytic identification and exhaustion steps
  below. Positive certificates for finite Galerkin sections, even at every
  sampled L, do not imply positivity of the full form. The empirical envelope
  suggests normalizations to test; it does not pin a proved UPT normalization.
- **PROVEN INDEPENDENCE** — RH has Π₁ formulations, so a false instance has a
  finite arithmetical witness. After formalizing one such equivalence and the
  proof predicate, Σ₁ completeness gives the metamathematical implication
  `¬Prov_ZFC(¬RH) → RH` (semantic truth, not a ZFC proof of RH). Thus any genuine
  independence proof would in particular establish that RH is true but
  unprovable in ZFC. This repository has not encoded the requisite Π₁
  equivalence, ZFC proof predicate, soundness/consistency assumptions, or
  nonprovability argument; the finite matrix stack does not materially advance
  those tasks.

## Level 0 — kernel-checked today (axioms: propext, Classical.choice, Quot.sound)

The matrix rows below are exact algebraic theorems about the displayed rational
data. Calling a row a ζ, GRH, or function-field window records its intended
provenance; it does not by itself formalize the analytic identification with a
Weil form. Those bridges are listed explicitly below.

| artifact | statement | file |
|---|---|---|
| `WeilCert.weil_window_positive` | every rational 12×12 matrix within 1e−20 of `mRat` (ζ, L=497/200) has positive quadratic form — data regenerated 2026-07-26 after pathology #5 | `lean/weilcert/Weilcert.lean` |
| `WeilCertDeep.weil_window_positive` | same at m=24, δ=1e−14 (1e−10-scale window) | `WeilcertDeep.lean` |
| `WeilCertDeeper.weil_window_positive` | same at m=48, δ=1e−19 (1e−15-scale window); 10-min kernel check | `WeilcertDeeper.lean` |
| `WeilCertFamily.weil_window_positive` | positive rational matrix intended to model the χ₋₇, L=5, m=16 Galerkin section; the numerical/analytic bridge is outside Lean | `WeilcertFamily.lean` |
| `Bridge.legendre` + `Bridge.overlap_k_j` (49 pairs) | Legendre polynomials + ALL shifted-overlap integral identities for k+j ≤ 12, pure FTC | `BridgeLegendre.lean`, `BridgeOverlap.lean` |
| `CertFramework` / `CertInstance` | n-generic certificate framework; `WeilCert` re-derived through it; scalar and real-inner-product-space F8 determinant transfer | `CertFramework.lean`, `CertInstance.lean` |
| `FullInfTransfer.*` | symmetric-bilinear and canonical orthogonal-projection forms of F8: exact finite, complement, and cross-block estimates imply a global strict lower bound; named p2, p3, and n4 theorems instantiate every rational endpoint ledger | `FullInfTransfer.lean` |
| `LegendreTail.weightIntegral_eq`, `norm_sphericalJIntegralModel_le`, `sphericalJIntegralModel_tsum_tail_le` | the exact weight integral, an oscillatory spherical-integral model with its sharp double-factorial bound, and the resulting infinite F2 geometric tail | `LegendreTail.lean` |
| `LegendrePlaneWave.rodriguesWeight_iterate_derivative_fourier` + phase/model bridge | generic repeated complex integration by parts, all lower endpoint derivatives of `(1-X²)^n` vanish, and the positive/negative Fourier phases agree for the even weight | `LegendrePlaneWave.lean` |
| `LegendreRodrigues.rodrigues_plainLegendre` + `polyFourierIntegral_plainLegendre_eq_sphericalJIntegralModel` | all-degree Rodrigues and exact plane-wave coefficient `FI(P_n)=2(-i)^n j_n` for an analysis-facing family transported from mathlib's shifted Legendre polynomials, valid also at z=0 | `LegendreRodrigues.lean` |
| `LegendreOrthogonality.plainLegendre_norm_sq` + `normalizedPlainLegendre_orthonormal` | lower-degree and pairwise orthogonality, exact norm `integral P_n^2=2/(2n+1)`, and normalized Kronecker-delta orthonormality for every degree | `LegendreOrthogonality.lean` |
| `LegendreCoefficientTail.*` + `LegendreScaled.*` | exact normalized plane-wave coefficients, squared moduli, arbitrary symmetric-interval scaling, and complete explicit coefficient-tail bounds | `LegendreCoefficientTail.lean`, `LegendreScaled.lean` |
| `LegendreL2.*` + `LegendreScaledL2.*` | normalized Legendre polynomials form complete Hilbert bases of real L² on the unit and arbitrary symmetric intervals; Weierstrass density, Parseval, canonical finite projections, exact residual-tail identities, and real/imaginary plane-wave coefficient bridges | `HilbertBasisTail.lean`, `LegendreL2.lean`, `LegendreScaledL2.lean` |
| `LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal` | explicit pointwise F2 leakage bound for every `w` orthogonal to the first `m` scaled modes, obtained from the complete complex coefficient tail | `LegendrePlaneWaveL2.lean` |
| `IntervalZeroExtension.norm_angularFourierBandCLM_apply_sq_eq_normalizedIntervalFourierBandEnergy` + `FullInfFourierBridge.p2_angularFourierBandCLM_norm_sq_le` | canonical zero extension, `L¹∩L²` compatibility with Mathlib's Fourier transform, exact `z/(2π)` band-norm identity, and the p=2 bound `ρ≤81/10^23` for the actual Plancherel band operator | `IntervalZeroExtension.lean`, `FullInfFourierBridge.lean` |
| `PoleProjection.p2_polePlus_projection_residual_lt` + `p2_poleMinus_projection_residual_lt` | the concrete `exp(±x/2)` vectors have norm at most one and canonical 48-mode projection residual below `195/10^95` | `PoleProjectionL2.lean` |
| `GlideKernel.gammaSeq_tendstoLocallyUniformlyOn` + `hasDerivAt_digamma_trigammaSeries` | unconditional locally uniform Euler GammaSeq convergence on `Re z>0`, the complex trigamma derivative, quarter-line strict monotonicity, and F7 exterior comparison | `lean/glide/Glide/GammaUniform.lean` |
| `GlideKernel.p2Omega_exterior_lower_bound` | for the actual p=2 symbol, `p2Alpha ≤ p2Omega r` whenever `50≤|r|`; this combines unconditional digamma monotonicity with the prime oscillation bound `cos≤1` | `lean/glide/Glide/P2Symbol.lean` |
| `GlideKernel.p2Alpha_lower_bound` + `p2Omega_sub_alpha_abs_le` | exact-series directed bounds `109387/100000 ≤ p2Alpha` and `abs (p2Omega r-p2Alpha)≤7447/1000` on `abs r≤50`; the former scalar endpoint gap is closed in the kernel | `lean/glide/Glide/EulerBounds.lean`, `lean/glide/Glide/DigammaBounds.lean` |
| `FullInfClipped48.clipped48IntervalLowerBound` + `FullInfClipped48Real.clipped48IntervalLowerBoundReal` + `FullInfClipped48Transfer.p2_projection_lower_bound_of_clipped48_intervals` | exact L=7/4 clipped V48 certificate, parity-reordered as two Fin 24 blocks: every rational and every real matrix in the stored radius-10^-12 intervals has strict lower bound 227/10^7; the real theorem is composed with the abstract F8 ledger under explicit analytic premises; analytic/Arb containment and those zeta-specific premises remain external | `FullInfClipped48.lean`, `FullInfClipped48Real.lean`, `FullInfClipped48Transfer.lean` |
| `FullInfP2Endpoint.projection_lower_bound_of_fourier_clipped48_p2_symbol` | strongest p=2 composition: an a.e.-real bounded multiplier symbol, the actual Fourier band map, exact leakage and poles, stored real interval certificate, complement/cross algebra, and determinant imply the `22699/10^9` clipped-form lower bound; no Fourier, pole, or F8 premise remains | `BoundedSymbolMultiplier.lean`, `BandOperatorBilinear.lean`, `FullInfOperatorLedger.lean`, `FullInfP2Endpoint.lean` |
| `LegendreParityCoordinates.norm_sq_eq_evenCoord_dot_add_oddCoord_dot` + `bilinear_eq_parity_matrices` | canonical even/odd coordinates on the 48-mode Legendre section, exact finite-span Parseval, and representation by the actual parity basis-entry matrices | `LegendreParityCoordinates.lean` |
| `SymbolQuadraticComparison.interval_clipped_bandForm_le_original_integral` | exact clipped-band identity and inequality against the original, possibly unbounded, symbol integral, including zero extension, Plancherel, band restriction, and `2π` scaling; assumes integrability of the original weighted energy | `SymbolQuadraticComparison.lean` |
| `RHP2Bridge.p2ClippedForm_even_odd` + `p2_clipped_endpoint_of_matrix_containment_no_parity` + `p2_original_integral_lower_bound_of_matrix_containment_no_parity` | exact Legendre/Fourier/pole parity eliminates the mixed block; even/odd interval containment alone then implies the `22699/10^9` clipped lower bound, and weighted integrability transfers it to the original unbounded p=2 Fourier integral plus exact pole term. All scalar, symbol, Fourier, pole, coordinate, and parity premises are discharged; no identification with the zeta Weil form is claimed | `lean/rhbridge/RHBridge/P2Parity.lean` |
| `FloorWitness.*` (4 thms) | kernel-checked impossibility result for the repository's entrywise-ball certificate format: at (L, m) = (711/200, 40), no radius-1e−20 certificate of that format exists around the displayed rational matrix; this is not an impossibility theorem for other certificate formats or for the full Weil form | `FloorWitness.lean` |
| `CurveCertE5.*` (36 thms) | end-to-end for a finite combinatorial model built from kernel-checked point counts: E: y²=x³+x+1/F₅, positivity and Cayley–Hamilton identities, plus a genus-2/F₇ block. No interval arithmetic is used. Identification of these matrices with the function-field Weil form still uses unformalized Parseval–Zak/Riemann–Roch mathematics, so this is not yet an end-to-end formal function-field RH window and gives no bridge to ζ | `CurveCertE5.lean` |
| `HardHorizon.hard_horizon` + `hard_horizon_of_global_orders` + `zero_desert` + `anchor_collapse`(`_of_deep`) | analytic kernel-checked theorems for the abstract rigid-staircase hypotheses: an explicit hard horizon, its global-order wrapper, a selected-radius/raw-remainder core of the paper's desert corollary, and annihilating-pair bounds. The ζ specialization is not formalized; it still requires the Riemann–von Mangoldt/S(T) bridge | `lean/glide/Glide/HardHorizon.lean` |
| `GlideKernel.laplace_sin` | ∫₀^∞ e^{−at} sin(st) dt = s/(a²+s²) (a>0) | `lean/glide/Glide/Basic.lean` |
| `GlideKernel.frullani_cos` | ∫₀^∞ e^{−at}(1−cos bt)/t dt = ½log(1+b²/a²) | same |
| `GlideKernel.kernel_lower/upper` | ½log(1+4r²) ≤ ∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t})dt ≤ ½log(1+4r²)+8 | same |
| `GlideKernel.quarterDigammaReal_neg` + `quarterTrigammaSlope_pos` + `quarterDigammaReal_strictMonoOn_of_hasDerivAt` | continuity/evenness of the quarter-line digamma real part, convergence and positivity of F7's candidate derivative series, and strict monotonicity from the exact derivative identity | `lean/glide/Glide/DigammaMonotone.lean` |

Certificate scaling (measured, `results/agent-lean-depth.md`): digits(c) ≈
0.21·m²·(digits per entry); kernel decide time ≈ m³·√digits — the formal
ladder's reach is priced (see also PLAN-computer-science.md walls). Standing
oracle since pathology #5: nested certificates at the same L must agree on
overlapping blocks within their combined rounding budgets.

## Level 1 — the Bridge (computer-assisted → formal)

Gap: prove IN LEAN that the truncated Weil matrix at (L = 497/200, Legendre
m = 12) lies in the 1e−20 ball around `mRat` (today: interval arithmetic with
stated trust base; THEOREMS.md Bridge Proposition — corrected 2026-07-26, see
pathology log #5). Sub-lemmas, status as of 2026-07-26:
1. **Overlap polynomials** — ✅ DONE (bridge-formal agent): `Bridge.overlap_k_j`
   for ALL 49 pairs k+j ≤ 12, pure FTC proofs, plus `Bridge.legendre` with
   degree/leading-coefficient lemmas (mathlib had only shiftedLegendre) and
   the scaled ledger identity T_kj(u) = a·F_kj(u/a). 84/84 theorems on the
   three standard axioms. Files: lean/weilcert/Bridge{Legendre,Overlap}.lean;
   generic framework: CertFramework.lean (arbitrary n; WeilCert re-derived).
2. **Kernel-moment identities**: Bernoulli generating identity EXISTS formally
   (`bernoulli'PowerSeries_mul_exp_sub_one`); the ANALYTIC z/(e^z−1) with
   radius-2π coefficient bounds is absent. Effort: 8–15 person-days.
3. **Pole vectors**: elementary positive-series bounds. Effort: days.
4. **Numeric enclosures**: π to 20 digits exists (`Real.pi_gt_d20`), e to
   1e−20 (`exp_one_near_20`), log 2 to 1e−10 (extensible); γ is the bottleneck
   (mathlib: only 1/2 < γ < 2/3; no Euler–Maclaurin). Effort: 10–20 pd. NOTE:
   the integer-congruence design needs NO γ at Level 1; γ enters at Level 2.
Total bridge estimate (bridge-formal agent's audit): ≈ 60–115 person-days,
three parallelizable long poles (Gauss integral, analytic Bernoulli, γ).

## Level 2 — Gauss's digamma formula (the identification lemma)

Gap: `Re (Complex.digamma (1/4 + I*r/2)) − Complex.digamma (1/4) =
∫₀^∞ e^{−t/4}(1−cos(rt/2))/(1−e^{−t}) dt`. Mathlib has `Complex.digamma`
(logDeriv Gamma, recurrence, special values incl. γ) but NOT Gauss's integral.
Route: Binet/Gauss via the Gamma integral representation + differentiation
under the integral (mathlib has the dominated-convergence machinery). This
lemma converts `kernel_lower/upper` into the digamma sandwich of THEOREMS.md
Lemma A — the exact form used by the Glide Theorem. Effort: weeks; a clean,
publishable mathlib contribution on its own.

For the narrower F7 monotonicity route, the former local-uniformity gap is
closed. `Glide.GammaUniform` proves locally uniform convergence of
`Complex.GammaSeq` to `Complex.Gamma` on `Re z>0` using Euler's integral and a
two-exponent dominated-convergence majorant. Together with
`Glide.DigammaSeries` and `Glide.DigammaMonotone`, this gives the derivative,
strict monotonicity, and exterior comparison without a premise.
`Glide.DigammaBounds` also closes the former p=2 scalar task with the exact
rational floor and band-multiplier bounds used by the certificate.

## Level 3 — the Glide Theorem, formal

Gap: formalize THEOREMS.md Theorem 1 (monotonicity + explicit-modulus
continuity of λ(L)). Needs: L² on an interval (mathlib ✓), Fourier–Plancherel
(mathlib ✓), the kernel sandwich (✓ Level 0 + Level 2), the elementary
a-priori lemmas B–E (routine given the above), and the dilation bookkeeping.
Effort: months. Prior art note: qualitative continuity is Suzuki
(arXiv:2606.09096, Thm 1.3), asserted earlier by Bombieri. The truncated Weil
form and this framework are not yet formalized in this repository; any broader
priority claim needs a separate literature audit.

## Status of the proposed full-space and zero-side bridges

- The square-frame identity
  `Q_L(φ) = 2 Σ_{γ>0}|φ̂(γ)|²` is conditional on RH (and on the
  usual symmetry/normalization). It is a valuable regression check, but it
  cannot be used as an unconditional lower bound or to reject a counterexample.
- NT-4 is a proposed quantitative converse-Weil lemma, not a theorem. No
  zero-exclusion conclusion in the panel reports should be treated as proved
  until NT-4 is supplied with a rigorous proof and explicit constants.
- `results/experts/FULLINF.md` now bounds three unrestricted endpoint infima.
  F7 gives a sharp exterior symbol floor and F8 transfers FLINT-Arb-certified
  clipped V₄₈, V₈₀ and V₁₃₂ blocks to the entire form domain, proving
  λ(7/4)>2.2699×10⁻⁵, λ(497/200)>9.99×10⁻¹¹, and
  λ(749/250)>9.9×10⁻¹⁶. Monotonicity gives positivity for every
  L≤749/250. The Hilbert/projection transfer and exact F2 geometric tail are
  now Lean-formalized through arbitrary-interval L² completeness, Parseval,
  canonical projections, zero extension, Plancherel compatibility, and the
  exact integrated p=2 leakage ledger. F7 monotonicity, the actual p=2
  exterior-symbol comparison, and the tight p=2 scalar enclosures are
  unconditional Lean theorems. Pole estimates, bounded-symbol operator
  algebra, canonical parity coordinates, and the p=2 two-block composition are
  also formal. The exact clipped-versus-original multiplier-integral
  comparison is formal under a weighted-integrability hypothesis. The
  zeta-form/domain identification is not formal. The analytic matrix interval
  containment is now closed by
  `RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`, and
  `p2_canonical_clipped_endpoint` composes it with every reusable p=2 result.
  The original-integral theorem additionally assumes weighted integrability.
  The exact
  L=7/4 clipped block, including its strict extension to arbitrary real
  interval matrices, is kernel-checked, and Lean composes that real
  certificate with the abstract L=7/4 projection ledger under explicit
  analytic premises.
  Hence the fixed clipped multiplier-plus-pole endpoint is a Lean theorem, but
  its identification with the zeta form remains software-certified and it does
  not cover all L or imply a zero-exclusion statement. Separately, F4 is
  an analytic bound on an explicit frequency-tail class;
  `src/fullinf_class_certificate.py` gives one conservative instantiation and
  an explicit member. NT-4 remains unproved, and the older high-m F4 table
  remains provisional.

## Level 4 — the finite criterion, formal

Gap: state IN LEAN the windowed Weil criterion: "for every L, the truncated
form Q_L is positive semidefinite on C_c^∞(−L/4, L/4)" and prove its
equivalence with `RiemannHypothesis`. Ingredients: the explicit formula
(Guinand–Weil) in Lean — the serious item; mathlib has `riemannZeta`, the
functional equation, `ArithmeticFunction.vonMangoldt`, Hadamard factorization
pieces; the explicit formula itself is a known missing keystone (also needed
by PrimeNumberTheoremAnd-style projects). Effort: a research-grade
formalization project (many months), but with independent value far beyond
this program.

## Level 5 — RH

By Level 4's equivalence, RH follows from positivity of the **full** form for
every L. A bare λ_m(L) remains only a Rayleigh–Ritz upper bound. FULLINF F8–F10
shows how one finite block can contribute when accompanied by an exterior
symbol floor, an orthogonal-complement defect bound, and a cross-block
determinant; this has been certified through L=749/250. No finite collection of
such local windows closes Level 5.

The envelope and its deep-window bend are finite-Galerkin numerical models,
not inputs to this implication. In particular, the coefficient 4π is already
the classical Fuchs/prolate coefficient used explicitly by Connes
(arXiv:2602.04022, §6.4); the repository's one-sided finite-basis data are
consistent with that asymptotic but do not prove an operator-level 4π cap or a
new 4π law. No finite process closes Level 5; the map exists so that every
finite step lands in the right place.

## The Lean steps most worth proving next

1. **The zeta-form/domain bridge.** Define the relevant truncated zeta Weil
   form and its domain in Lean, prove the weighted Fourier integral is
   integrable there, and identify it with the original p=2 multiplier plus the
   pole term. `SymbolQuadraticComparison` already supplies the exact
   original-versus-clipped integral inequality.
2. **Uniform support and the explicit formula.** The completed containment is
   only the fixed `p=2`, `L=7/4`, 48-mode window. An all-support transfer and
   the explicit-formula/RH equivalence remain separate research-scale goals.

*Prior-art annotations per results/agent-prior-art.md: margin decay of
"exponential-of-exponential" type and the 4π Fuchs/prolate coefficient appear
in Connes arXiv:2602.04022 §6.4; qualitative continuity is Bombieri/Suzuki.
The three-constant fit, family collapse, and mechanism experiment are numerical
observations whose novelty and robustness remain unestablished. The exact
Level-0 algebraic statements are proved as stated, but priority claims such as
"first" require an external literature audit.*
