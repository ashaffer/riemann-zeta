import Mathlib

/-!
# Pre-factorial affine-compression algebra

These lemmas certify the elementary algebra in the hybrid affine-compression
transfer.  They do not construct affine packets or prove their global
Carleson packing estimate.
-/

namespace QPHybridAffineCompression

/-- A completion partition is linear at the level of the direct count. -/
theorem direct_split (a r : ℤ) : a + r = a + r := by
  rfl

/-- Factorialization creates an affine term and a mixed term which direct
affine trace control does not estimate. -/
theorem factorial_split (a r : ℤ) :
    (a + r) * (a + r - 1) =
      a * (a - 1) + r * (r - 1) + 2 * a * r := by
  ring

/-- For a nonempty residual fibre, its first moment is controlled by its
presence plus half of its ordered factorial moment. -/
theorem twice_residual_le_presence_plus_factorial
    (r : ℤ) (hr : 0 < r) :
    2 * r ≤ 2 + r * (r - 1) := by
  by_cases hone : r = 1
  · subst r
    norm_num
  · have htwo : 2 ≤ r := by omega
    nlinarith [mul_nonneg (sub_nonneg.mpr (by linarith : 0 ≤ r - 1))
      (sub_nonneg.mpr (by linarith : 0 ≤ r - 2))]

/-- Weighted real form of the preceding integer inequality. -/
theorem weighted_residual_le_presence_plus_factorial
    (r : ℤ) (w : ℝ) (hr : 0 < r) (hw : 0 ≤ w) :
    (r : ℝ) * w ≤ w + (r : ℝ) * ((r : ℝ) - 1) * w / 2 := by
  have h := twice_residual_le_presence_plus_factorial r hr
  have hreal : (2 : ℝ) * r ≤ 2 + r * (r - 1) := by exact_mod_cast h
  have hmul := mul_le_mul_of_nonneg_right hreal hw
  nlinarith

/-- The quadratic inequality used by the alternative Cauchy bootstrap. -/
theorem cauchy_residual_quadratic
    (S W P : ℝ) (_hS : 0 ≤ S) (hW : 0 ≤ W) (hP : 0 ≤ P)
    (h : S ^ 2 ≤ W * (S + P)) :
    S ≤ (W + Real.sqrt (W ^ 2 + 4 * W * P)) / 2 := by
  have hrad : 0 ≤ W ^ 2 + 4 * W * P := by positivity
  have hsqrt : 0 ≤ Real.sqrt (W ^ 2 + 4 * W * P) := Real.sqrt_nonneg _
  have hsqrt_sq : (Real.sqrt (W ^ 2 + 4 * W * P)) ^ 2 =
      W ^ 2 + 4 * W * P := by
    exact Real.sq_sqrt hrad
  nlinarith

end QPHybridAffineCompression
