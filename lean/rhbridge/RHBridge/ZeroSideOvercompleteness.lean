/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LogEllipticReduction

/-!
# Overcomplete zero-side cancellation obstruction

Completeness of an exponential family does not permit isolation of its
individual coefficients.  This elementary two-dimensional model has three
sampling directions.  One contribution has negative weight, while their sum
is nonnegative and has a nonzero radical vector.
-/

namespace RHP2Bridge.ZeroSideOvercompleteness

def sampleForm (x y : ℝ) : ℝ :=
  2 * x ^ 2 + 2 * y ^ 2 - (x + y) ^ 2

theorem sampleForm_eq_difference_sq (x y : ℝ) :
    sampleForm x y = (x - y) ^ 2 := by
  unfold sampleForm
  ring

theorem sampleForm_nonneg (x y : ℝ) :
    0 ≤ sampleForm x y := by
  rw [sampleForm_eq_difference_sq]
  positivity

theorem sampleForm_radical_example : sampleForm 1 1 = 0 := by
  norm_num [sampleForm]

theorem negative_sample_nonzero_on_radical :
    -((1 : ℝ) + 1) ^ 2 ≠ 0 := by
  norm_num

theorem positive_samples_nonzero_on_radical :
    2 * (1 : ℝ) ^ 2 ≠ 0 ∧ 2 * (1 : ℝ) ^ 2 ≠ 0 := by
  norm_num

end RHP2Bridge.ZeroSideOvercompleteness
