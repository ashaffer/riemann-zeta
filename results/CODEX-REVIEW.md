# Codex review — current logical status and next moves

**Audit date:** 2026-07-28; canonical p=2 containment closure update: 2026-07-30

## Bottom line

This repository does **not** prove, disprove, or establish independence of RH,
and none of its current results implies one of those outcomes. It does contain
useful, reproducible work: exact finite-matrix certificates, a genuine abstract
Lean theorem, computer-assisted Galerkin enclosures, and analytic information
about the full truncated form. Positive finite Galerkin minima by themselves
remain only upper bounds on the full infimum. A new clipped-symbol transfer,
however, now composes a separately certified finite block with an analytic
orthogonal-complement estimate and proves the unrestricted local bounds

  inf Q_{7/4}/‖·‖² > 2.2699×10⁻⁵,
  inf Q_{497/200}/‖·‖² > 9.99×10⁻¹¹,
  inf Q_{749/250}/‖·‖² > 9.9×10⁻¹⁶.

Together with support monotonicity, this closes the finite-to-full gap for
every L≤749/250 under a documented FLINT-Arb plus analytic trust base. The
`L=7/4` proof skeleton is now kernel-checked through F7, the directed p=2
bounds, Fourier leakage, poles, operator algebra, parity, canonical matrix
containment, and the exact clipped-to-original integral comparison. The strict
clipped endpoint is now a Lean theorem. Weighted integrability and the
identification with the zeta form on its domain remain open. None of this
covers all support sizes or supplies a proved NT-4 converse,
so it is not RH or a claimed zero-exclusion result.

## Evidence tiers

| tier | what is genuinely established | what is not established |
|---|---|---|
| Lean kernel | Exact rational and arbitrary-real certificates for the two 24-dimensional parity blocks of the L=7/4 clipped V48 interval; scalar, Hilbert-space, bilinear, and canonical-projection F8 transfers; complete Legendre/Parseval/Fourier leakage through the actual band operator with `ρ≤81/10^23`; concrete pole norms and residuals; complement/cross operator algebra; unconditional locally uniform GammaSeq convergence and F7 monotonicity; the actual p=2 exterior comparison; directed bounds `109387/100000≤p2Alpha` and `abs (p2Omega-p2Alpha)≤7447/1000` on the band; canonical parity coordinates/matrices; exact parity decoupling; the clipped-versus-original symbol-integral comparison; canonical analytic matrix containment; and the strict clipped endpoint | The truncated zeta form, its precise domain, weighted integrability, and identification with the multiplier-plus-pole expression remain external; there is no all-L positivity theorem or Lean explicit-formula/RH equivalence; Hard Horizon's zeta anchor and the function-field geometric bridge are external |
| Analytic proof | The form has the correct logarithmic domain, is closed and semibounded, has compact resolvent, and attains its infimum; λ(L) is non-increasing and continuous; the entering-prime coupling has an explicit `O(1/log(1/h))` bound; F7–F8 give a sharp exterior symbol floor and a finite-to-full block theorem | The analytic theorem alone does not certify its finite clipped matrix hypothesis; no uniform all-L positivity transfer |
| Computer-assisted finite dimension | Several hat/Legendre matrices have positive eigenvalue enclosures under the stated `mpmath.iv` or Arb trust bases; the 12-dimensional window and the arbitrary-real-matrix L=7/4 clipped V48 interval statement have Lean-checked certificates; canonical p=2 containment is now independently checked with Lean analytic bounds | Ordinary Galerkin positivity alone remains an upper bound; m=80/m=132 containment and the zeta-form identification are not checked by Lean |
| Computer-assisted full space | FLINT-Arb plus F8 certify unrestricted bounds >2.2699×10⁻⁵ at L=7/4 (48 modes), >9.99×10⁻¹¹ at L=497/200 (80 modes), and >9.9×10⁻¹⁶ at L=749/250 (132 modes); monotonicity covers all smaller supports | Only L≤749/250; software/analytic trust base, not Lean; no named-zero or RH consequence |
| Computer-assisted restricted class | At L=7/4, F4 plus a committed closed-form interval tail calculation proves Q_L>1.1139×10⁻⁵ for every unit vector with normalized Fourier mass above 50 at most 10⁻¹⁵; an explicit normalized degree-28 polynomial has certified tail <3×10⁻¹⁷, placing a radius-2×10⁻⁸ unit-sphere cap inside the class | No certified NT-4 packet membership or zero-exclusion consequence |
| Numerical/empirical | Descending Galerkin ladders, a threshold glide, family comparisons, and an envelope compatible at depth with the known prolate `4π` coefficient | No proved envelope law, universality, density-only mechanism, or operator-level threshold positivity |
| Proposed | UPT beyond the certified range, NT-4, and a fully formal zeta bridge | These remain open targets, not lemmas available for composition |

## Changes made in this audit

1. Defined the full form on its logarithmically weighted domain and proved the
   standard closed-form/compact-resolvent proposition. This makes the ground
   state and monotone Galerkin convergence precise, while explicitly exposing
   the absent error bound.
2. Strengthened the Glide proof by using both support-edge slivers:
   `|ψ_φ(2a−ε)| = O(1/log(1/ε))`, improving the displayed continuity modulus
   from `O(log^{-1/2})` to `O(log^{-1})`. Several constants and endpoint
   conditions were repaired at the same time.
3. Added and kernel-checked
   `CertInstance.real_window_positive_via_framework`. Strict positivity for
   real vectors now follows directly from the exact congruence over `ℝ`, not
   from an invalid density argument.
4. Removed ordinary floating-point decisions from two interval-certificate
   paths: the kernel coefficient majorant is now an exact rational, and
   prime-power support membership is decided by interval separation or fails
   closed.
5. Repaired the missing high-frequency cross term in FULLINF F4, then committed
   a conservative m=48 driver that bounds `T₂` by closed-form interval
   antiderivatives. It certifies `Q_(7/4)>1.1139×10⁻⁵` on `𝒞(50,10⁻¹⁵)`; the old
   high-m ledger remains provisional. Exact polynomial moments and a uniform
   sinc remainder also certify an explicit degree-28 member with tail `<3×10⁻¹⁷`.
6. Added F7–F10 and three separate unrestricted drivers. Monotonicity of
   Re ψ(1/4+ir/2) gives an exterior symbol floor at |r|=50; the Legendre
   complement has certified band leakage `<8.1×10⁻²²`; Arb integration and
   Cholesky prove the clipped finite block `>2.27×10⁻⁵`; and a rational
   two-by-two determinant proves the unrestricted bound `>2.2699×10⁻⁵`.
   The same construction at L=497/200, S=70 and m=80 includes primes 2 and 3;
   1,640 independent Arb integrations prove the clipped block `>10⁻¹⁰`
   and the unrestricted bound `>9.99×10⁻¹¹`. Two complete runs and
   two independent mathematical audits passed. The scalar determinant
   implication is now kernel-checked as
   `CertFramework.two_by_two_strict_lower_bound`; the analytic block estimates
   and Arb bridge are not. At L=749/250, a 50,000-panel tail bridge sharpens
   the exterior floor to 0.29 at S=110. A resumable 4,422-entry Arb run proves
   the clipped 132-mode block `>10⁻¹⁵`; with band defect
   `<1.52×10⁻²⁰`, the transfer gives the third unrestricted bound
   `>9.9×10⁻¹⁶`. An independent checkpoint audit found all 4,422
   expected entries uniquely and six fresh integrations inside their cached
   balls. Lean also checks the three conservative rational
   scalar ledgers as `fullinf_p2_block_lower_bound`,
   `fullinf_p3_block_lower_bound`, and `fullinf_n4_block_lower_bound`.
7. Corrected the zero-side oracle's status: the sum-of-squares representation is
   RH-conditional and is a regression check, not a veto against a counterexample.
   The model-zero audit also found that nominal Gcut=420 runs silently stopped
   at 180 rather than roughly 215 points. With cutoff-safe generation, a
   phase-matched 13-seed ensemble spans both signs and 10–12 orders in the
   Poisson/smooth ratio. The density-only/maximal-rigidity verdict is withdrawn.
8. Added a Lean order-translation lemma and `hard_horizon_of_global_orders`, so
   the paper's global orders at `±t_k` feed the existing recentered abstract
   theorem without changing its hypotheses. The zeta/Riemann--von Mangoldt
   bridge remains external.
9. Re-audited T1PRIME line by line. The abstract Jensen theorem survives;
   distinct zeta ordinates now carry their total multiplicity, Trudgian's
   direct zero-count bound replaces an unsupported theta-tail shortcut, the
   zero-desert statement tracks the residual divisor, and action-height data
   are no longer presented as a hard-horizon test.
10. Moved the reusable FULLINF bridge toward the kernel. Lean now proves the
    abstract Hilbert and canonical orthogonal-projection F8 transfers plus
    three exact projection-level endpoint ledgers (`CertFramework` and
    `FullInfTransfer`), the complete factorial/geometric F2 tail plus an
    all-degree Rodrigues/plane-wave coefficient theorem (`LegendreTail`,
    `LegendrePlaneWave`, `LegendreRodrigues`), and convergence and positivity of F7's candidate
    trigamma slope (`Glide.DigammaMonotone`). The remaining hypotheses are
    stated explicitly rather than hidden behind numerical output.
11. Imported the smallest clipped finite block into the kernel.
    `FullInfClipped48.clipped48IntervalLowerBound` checks exact LDL congruences
    for the two parity-reordered 24-dimensional blocks and proves a strict
    `227/10^7` coordinate-norm lower bound for every rational matrix in the
    stored radius-`10^-12` intervals. `FullInfClipped48Real` casts the exact
    congruence data and proves the same strict result for arbitrary real
    matrices in those intervals. The generator checks Arb-ball containment
    externally; the analytic zeta identification remains open.
12. Composed that real finite certificate with F8 in
    `FullInfClipped48Transfer.p2_projection_lower_bound_of_clipped48_intervals`.
    The kernel now derives the full L=7/4 projection-ledger conclusion from
    explicit coordinate/form, interval-containment, complement, and cross
    premises; proving those premises for the zeta form remains the local gap.
13. Closed the algebraic Legendre normalization step.
    `LegendreOrthogonality` proves lower-degree and pairwise orthogonality,
    `integral P_n^2 = 2/(2n+1)`, and normalized Kronecker-delta
    orthonormality for every degree.
14. Closed the Legendre Hilbert-space and pointwise leakage bridge.
    `LegendreCoefficientTail` and `LegendreScaled` prove exact normalized and
    scaled coefficients and their complete geometric tails. `LegendreL2` and
    `LegendreScaledL2` use Weierstrass density to construct complete Hilbert
    bases, prove Parseval, identify canonical finite projections and their
    residual tails, and connect the real/imaginary plane waves to the complex
    coefficients. `LegendrePlaneWaveL2` composes these into the explicit
    pointwise F2 inequality for every `w ∈ V_mᗮ`. The later
    `IntervalZeroExtension` and `FullInfFourierBridge` modules close the band
    integration, Plancherel normalization, and endpoint `ρ` ledger.
15. Closed the F7 derivative gap.
    `Glide.DigammaSeries` proves the finite GammaSeq logarithmic-derivative
    formulas and shows that locally uniform Euler GammaSeq convergence on
    `Re z>0` implies the complex trigamma series, quarter-line derivative,
    strict monotonicity, and exterior comparison. `Glide.GammaUniform` proves
    the required locally uniform limit unconditionally.
16. Closed the directed p=2 scalar ledger. `Glide.EulerBounds` and
    `Glide.DigammaBounds` turn the quarter-line digamma difference into an
    exact positive rational series with explicit tails, proving
    `109387/100000≤p2Alpha` and the band bound `7447/1000` in the kernel.
17. Closed the remaining reusable Fourier, pole, and operator premises.
    `IntervalZeroExtension`, `FullInfFourierBridge`, `PoleProjectionL2`,
    `BoundedSymbolMultiplier`, and `FullInfOperatorLedger` construct the actual
    band operator and poles and derive the complement/cross estimates.
18. Added canonical parity coordinates and the original-symbol comparison.
    `LegendreParityCoordinates` identifies the true even/odd coefficients and
    basis-entry matrices. `SymbolQuadraticComparison` proves the exact clipped
    identity and its inequality against the original, potentially unbounded,
    multiplier integral, with the correct `2π` scaling.
19. Composed the two Lake developments in `lean/rhbridge`.
    `RHP2Bridge.p2_clipped_endpoint_of_matrix_containment_no_parity` discharges every
    scalar, symbol, Fourier, pole, operator, coordinate, and parity premise,
    leaving only even/odd interval containment. Its original-integral
    corollary transfers the strict `22699/10^9` bound to the unbounded p=2
    weighted Fourier integral plus exact pole term under weighted integrability.
    This is deliberately not identified with the zeta Weil form.
20. Closed canonical p=2 matrix containment in Lean.
    `RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment`
    verifies the analytic approximation/rounding ledger, exact moment and
    matvec identities, bounded product-error propagation, and all 19,200 entry
    refinements. Its corollary `p2_canonical_clipped_endpoint` closes the fixed
    clipped endpoint. The axiom audit reports only
    `[propext, Classical.choice, Quot.sound]`.

## The shortest honest route forward

1. **Finish the zeta-form/domain bridge.** Define the truncated zeta Weil form
   and its domain, prove the required weighted Fourier integrability, and
   identify it with the multiplier-plus-pole expression. The exact
   original-versus-clipped integral inequality is already formal.
2. **Treat NT-4 as a theorem-proving project.** State the admissible test class,
   off-line-zero quartet contribution, all remaining zero/prime tails, and
   explicit constants. Do not compose it with certificates until those pieces
   are proved.

Even after those local steps, positivity for arbitrary support and the formal
explicit-formula/RH equivalence remain. Further n=5 scouting and model-zero
experiments are lower priority than these kernel-facing steps.

## Note for future Claude/Codex sessions

- Write `λ_m` for every finite matrix minimum and reserve `λ` for the full form.
- A positive `λ_m` never proves positive `λ` by itself; F8 works only because it
  adds an independently proved orthogonal-complement and cross-block bound.
- Label every zero-side square identity “under RH.”
- Keep kernel algebra, analytic bridges, interval-software results, and empirical
  fits in separate claim tiers.
- Do not call `CurveCertE5` end-to-end until Parseval–Zak/Riemann–Roch are in the
  formal chain. Distinguish the F4 class certificate from the separate F8
  unrestricted certificates, and label F8–F10's Arb/analytic trust base.

## Prior-art positioning

The deep `4π` behavior is consistent with the classical prolate/Fuchs comparison
already central in [Connes's 2026 analysis](https://arxiv.org/html/2602.04022v1),
not a new asymptotic theorem here. Qualitative continuity is also prior art; see
[Suzuki's 2026 theorem](https://arxiv.org/html/2606.09096v1). Recent finite-cutoff
limitations and computations should be compared with
[Groskin 2026](https://arxiv.org/html/2607.02828v1). Finally, the Python interval
claims should continue to name their software trust base; `mpmath.iv` is documented
as experimental in the [mpmath interval arithmetic documentation](https://mpmath.org/doc/current/contexts.html).

A focused keyword search did not locate the exact F8–F10 clipped-symbol/Legendre-
defect transfer, but that is not a novelty proof. The closest established lines
include Connes–Consani's prolate/Toeplitz treatment of the archimedean local
factor ([arXiv:2006.13771](https://arxiv.org/abs/2006.13771)) and Groskin's
different finite-cutoff-to-cutoff-free certification rule
([arXiv:2607.02828](https://arxiv.org/abs/2607.02828)). Treat F8 as a correct
repository theorem whose literature novelty remains unresolved pending expert
review.
