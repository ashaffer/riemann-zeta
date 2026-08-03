/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ZeroSideOvercompleteness

/-!
# Phase of an off-critical functional-equation quartet

For real test data, conjugate zeros contribute conjugate transform products.
The four members of an off-critical quartet therefore sum to four times the
real part of one product.  This is not a norm square; its sign requires phase
control relating the transform at the two reflected complex arguments.
-/

namespace RHP2Bridge.ZeroQuartetPhase

open scoped ComplexConjugate

/-- Algebraic form of the quartet sum. -/
theorem quartet_sum_eq_four_mul_re (a b : ℂ) :
    a * b + a * b + conj (a * b) + conj (a * b) =
      (4 * (a * b).re : ℝ) := by
  apply Complex.ext
  · simp [Complex.mul_re]
    ring
  · simp [Complex.mul_im]
    ring

/-- The quartet expression has no unconditional nonnegative sign. -/
theorem quartet_sum_can_be_negative :
    (((1 : ℂ) * (-1) + 1 * (-1) +
      conj ((1 : ℂ) * (-1)) + conj ((1 : ℂ) * (-1))).re) < 0 := by
  norm_num

/-- A purely imaginary nonzero transform value has strictly negative square
phase, the mechanism realized by symmetric positive masses at a quarter
oscillation. -/
theorem pureImaginary_square_re_neg {y : ℝ} (hy : y ≠ 0) :
    (((y : ℂ) * Complex.I) * ((y : ℂ) * Complex.I)).re < 0 := by
  simp
  exact hy

/-- A sufficient phase condition is exactly nonnegativity of the real part
of the reflected product; this condition is additional information, not a
consequence of quartet symmetry. -/
theorem quartet_sum_re_nonneg_of_product_re_nonneg
    {a b : ℂ} (hphase : 0 ≤ (a * b).re) :
    0 ≤ (a * b + a * b + conj (a * b) + conj (a * b)).re := by
  rw [quartet_sum_eq_four_mul_re]
  simpa using mul_nonneg (show 0 ≤ (4 : ℝ) by norm_num) hphase

end RHP2Bridge.ZeroQuartetPhase
