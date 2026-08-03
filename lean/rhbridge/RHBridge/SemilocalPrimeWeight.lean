/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# The one-prime semilocal spectral weight is not ordered

Writing `q=p^(-1/2)`, adjoining `p` multiplies the semilocal spectral measure
by `|L_p(1/2+it)|^2 = (1+q^2-2q cos(theta))^{-1}`.  The lemmas below show that
this multiplier lies on both sides of one during a period.  Consequently the
old and new multiplication metrics admit no Loewner ordering.
-/

namespace RHBridge.SemilocalPrimeWeight

noncomputable def localWeight (q theta : ℝ) : ℝ :=
  (1 + q ^ 2 - 2 * q * Real.cos theta)⁻¹

theorem denominator_zero_lt_one {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    1 + q ^ 2 - 2 * q * Real.cos 0 < 1 := by
  simp only [Real.cos_zero, mul_one]
  nlinarith

theorem denominator_zero_pos {q : ℝ} (_hq0 : 0 < q) (hq1 : q < 1) :
    0 < 1 + q ^ 2 - 2 * q * Real.cos 0 := by
  simp only [Real.cos_zero, mul_one]
  nlinarith [sq_pos_of_pos (sub_pos.mpr hq1)]

theorem one_lt_localWeight_zero {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    1 < localWeight q 0 := by
  unfold localWeight
  exact (one_lt_inv₀ (denominator_zero_pos hq0 hq1)).2
    (denominator_zero_lt_one hq0 hq1)

theorem one_lt_denominator_pi {q : ℝ} (hq0 : 0 < q) :
    1 < 1 + q ^ 2 - 2 * q * Real.cos Real.pi := by
  rw [Real.cos_pi]
  nlinarith [sq_pos_of_pos hq0]

theorem localWeight_pi_lt_one {q : ℝ} (hq0 : 0 < q) :
    localWeight q Real.pi < 1 := by
  unfold localWeight
  exact inv_lt_one_of_one_lt₀ (one_lt_denominator_pi hq0)

/-- The local-factor multiplier cannot be uniformly above or uniformly below
the old metric. -/
theorem localWeight_crosses_one {q : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    localWeight q Real.pi < 1 ∧ 1 < localWeight q 0 :=
  ⟨localWeight_pi_lt_one hq0, one_lt_localWeight_zero hq0 hq1⟩

end RHBridge.SemilocalPrimeWeight
