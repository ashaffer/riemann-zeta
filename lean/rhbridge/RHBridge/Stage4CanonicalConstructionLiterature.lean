/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4CCMComparatorFamily
import RHBridge.Stage4MomentCorrection
import RHBridge.Stage4PoissonReduction

/-!
# Canonical CCM prolate construction

This file is the formal boundary for the classical fixed-mode prolate
asymptotics and their smooth endpoint regularization.  Concretely, the family
is obtained from the same-sign modes `psi_0, psi_4`, their normalized
zero-at-origin combination, a flat endpoint cutoff, and an exponentially
small interior moment correction.

The supplied estimates are exactly those proved analytically in
`results/STAGE4-PROLATE-MOMENT-PROOF.md`: the Poisson--Mellin certificate for
the regularized family and logarithmic-sampling convergence back to the
original sharp family.  No location assertion about zeta zeros, Weil
positivity, or RH is part of this construction interface.
-/

namespace RHP2Bridge.Stage4CanonicalConstructionLiterature

open Filter Topology GeneralZetaWeilForm
open Stage4CanonicalResidual Stage4CCMComparatorFamily
open Stage4ProlateMellinCertificate Stage4SamplingLiterature

/-- Logarithmic support radii of the canonical sequence, with source prolate
scale `lambda = n + 2`. -/
noncomputable def canonicalSupportRadius (n : ℕ) : ℝ :=
  Real.log ((n : ℝ) + 2)

/-- Original sharply truncated CCM prolate vectors. -/
axiom canonicalSharpComparator :
  (n : ℕ) → LogarithmicFormDomain (canonicalSupportRadius n)

/-- Flat-cutoff, exactly moment-corrected regularizations. -/
axiom canonicalRegularizedComparator :
  (n : ℕ) → LogarithmicFormDomain (canonicalSupportRadius n)

/-- The canonical windows exhaust every fixed compact support. -/
theorem canonicalSupportRadius_cofinal :
    Tendsto canonicalSupportRadius atTop atTop := by
  apply Real.tendsto_log_atTop.comp
  simpa using
    (tendsto_natCast_atTop_atTop.atTop_add
      (tendsto_const_nhds : Tendsto (fun _ : ℕ ↦ (2 : ℝ)) atTop (𝓝 2)))

/-- Weighted prolate leakage plus the normalized Poisson--Mellin argument for
the regularized vectors. -/
axiom canonicalRegularized_prolateMellin :
  ProlateMellinTailCertificate canonicalRegularizedComparator

/-- Zero-sampling error made by replacing the sharp vector by its smooth
moment-corrected regularization. -/
axiom canonicalRegularizationError : ℕ → ℝ

axiom canonicalRegularizationError_nonneg :
  ∀ n, 0 ≤ canonicalRegularizationError n

axiom canonicalRegularizationError_tendsto_zero :
  Tendsto canonicalRegularizationError atTop (𝓝 0)

axiom canonicalSharp_zeroSampleEnergy_le : ∀ n,
  zeroSampleEnergy (canonicalSupportRadius n)
      (canonicalSharpComparator n).val ≤
    2 * zeroSampleEnergy (canonicalSupportRadius n)
      (canonicalRegularizedComparator n).val +
      canonicalRegularizationError n

/-- The canonical family assembled from the individually audited analytic
inputs.  Unlike the former opaque structure-valued axiom, this definition
does not conceal which estimates remain at the literature boundary. -/
noncomputable def canonicalCCMComparatorFamily :
    CertifiedCCMComparatorFamily where
  supportRadius := canonicalSupportRadius
  comparator := canonicalSharpComparator
  regularized := canonicalRegularizedComparator
  support_cofinal := canonicalSupportRadius_cofinal
  prolate_mellin := canonicalRegularized_prolateMellin
  regularizationError := canonicalRegularizationError
  regularizationError_nonneg := canonicalRegularizationError_nonneg
  regularizationError_tendsto_zero :=
    canonicalRegularizationError_tendsto_zero
  sharp_zeroSampleEnergy_le := canonicalSharp_zeroSampleEnergy_le

/-- Stage 4 for the actual canonical CCM family: every fixed compactly
supported logarithmic-form vector has vanishing polarized Weil residual
against the cofinal sharp comparator sequence. -/
theorem canonical_full_logarithmic_residual
    (b : ℝ) (g : LogarithmicFormDomain b) :
    ∃ N : ℕ,
      ∃ hba : ∀ n,
        b ≤ canonicalCCMComparatorFamily.supportRadius (N + n),
      Tendsto
        (movingWeilCross
          (fun n ↦ canonicalCCMComparatorFamily.comparator (N + n))
          hba g)
        atTop (𝓝 0) :=
  full_logarithmic_residual canonicalCCMComparatorFamily b g

end RHP2Bridge.Stage4CanonicalConstructionLiterature
