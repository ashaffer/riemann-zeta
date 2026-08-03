/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Zero-phase-normalized local Euler contractions

For `q=p^(-sigma)`, normalize the reflected local Euler weight by its value at
zero phase.  The resulting multiplier is at most one, and its defect from one
is exactly controlled by `1-cos(theta)`.  This is the finite-place contraction
whose logarithmic scale derivative produces the prime translation-defect
symbol.
-/

namespace RHBridge.NormalizedLocalContraction

noncomputable def contraction (q theta : ℝ) : ℝ :=
  (1 - q) ^ 2 / (1 + q ^ 2 - 2 * q * Real.cos theta)

theorem denominator_pos {q theta : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    0 < 1 + q ^ 2 - 2 * q * Real.cos theta := by
  have hcos : Real.cos theta ≤ 1 := Real.cos_le_one theta
  have hsquare : 0 < (1 - q) ^ 2 := sq_pos_of_pos (sub_pos.mpr hq1)
  nlinarith

theorem numerator_pos {q : ℝ} (hq1 : q < 1) : 0 < (1 - q) ^ 2 :=
  sq_pos_of_pos (sub_pos.mpr hq1)

theorem contraction_pos {q theta : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    0 < contraction q theta := by
  exact div_pos (numerator_pos hq1) (denominator_pos hq0 hq1)

/-- The normalized local factor is a pointwise contraction. -/
theorem contraction_le_one {q theta : ℝ} (hq0 : 0 < q) (hq1 : q < 1) :
    contraction q theta ≤ 1 := by
  unfold contraction
  apply (div_le_one (denominator_pos hq0 hq1)).2
  have hcos : Real.cos theta ≤ 1 := Real.cos_le_one theta
  nlinarith

@[simp] theorem contraction_zero (q : ℝ) (hq : q ≠ 1) :
    contraction q 0 = 1 := by
  unfold contraction
  simp only [Real.cos_zero, mul_one]
  have hden : 1 + q ^ 2 - 2 * q = (1 - q) ^ 2 := by ring
  rw [hden]
  exact div_self (pow_ne_zero 2 (sub_ne_zero.mpr hq.symm))

/-- Exact algebraic source of contractivity. -/
theorem denominator_sub_numerator (q theta : ℝ) :
    (1 + q ^ 2 - 2 * q * Real.cos theta) - (1 - q) ^ 2 =
      2 * q * (1 - Real.cos theta) := by
  ring

/-- Finite logarithmic-generator approximants are manifestly nonnegative. -/
noncomputable def primeDefectPartial (q theta : ℝ) (N : ℕ) : ℝ :=
  ∑ k ∈ Finset.Icc 1 N,
    2 * q ^ k * (1 - Real.cos ((k : ℝ) * theta))

theorem primeDefectPartial_nonneg {q : ℝ} (hq : 0 ≤ q)
    (theta : ℝ) (N : ℕ) : 0 ≤ primeDefectPartial q theta N := by
  unfold primeDefectPartial
  apply Finset.sum_nonneg
  intro k _
  have hcos : 0 ≤ 1 - Real.cos ((k : ℝ) * theta) := by
    linarith [Real.cos_le_one ((k : ℝ) * theta)]
  positivity

end RHBridge.NormalizedLocalContraction
