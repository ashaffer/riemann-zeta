/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

/-!
# Exact two-moment correction for the regularized CCM source

After applying a flat endpoint cutoff, subtracting one scalar multiple of a
fixed interior bump restores zero integral without changing the value at the
origin.  This elementary step is proved here rather than included in the
prolate literature boundary.
-/

namespace RHP2Bridge.Stage4MomentCorrection

open MeasureTheory

noncomputable section

/-- Flat-cutoff source corrected by a bump of integral one. -/
def momentCorrected (q φ b : ℝ → ℝ) : ℝ → ℝ :=
  fun x ↦ q x * φ x - (∫ y, q y * φ y) * b x

/-- A bump vanishing at zero preserves the zero-at-origin condition. -/
theorem momentCorrected_zero (q φ b : ℝ → ℝ)
    (hφ : φ 0 = 0) (hb : b 0 = 0) :
    momentCorrected q φ b 0 = 0 := by
  simp [momentCorrected, hφ, hb]

/-- If the bump has integral one, the corrected source has exactly zero
integral. -/
theorem integral_momentCorrected_eq_zero (q φ b : ℝ → ℝ)
    (hqφ : Integrable (fun x ↦ q x * φ x))
    (hb : Integrable b) (hbint : ∫ x, b x = 1) :
    ∫ x, momentCorrected q φ b x = 0 := by
  change ∫ x, (q x * φ x - (∫ y, q y * φ y) * b x) = 0
  rw [integral_sub hqφ (hb.const_mul _), integral_const_mul, hbint]
  ring

end

end RHP2Bridge.Stage4MomentCorrection
