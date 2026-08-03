/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Glide.BasicQuarter
import Glide.DigammaKernel
import Glide.GammaUniformQuarter

/-!
# Quarter-line compatibility for Gauss's digamma kernel

These are fixed-normalization specializations of the general positive
vertical-line results in `Glide.DigammaKernel`.
-/

namespace GlideKernel

open Set MeasureTheory

noncomputable section

/-- The Gauss-kernel representation of the quarter-line digamma difference. -/
theorem quarterDigammaReal_sub_zero_eq_archKernel_integral (r : ℝ) :
    quarterDigammaReal r - quarterDigammaReal 0 =
      ∫ t in Ioi (0 : ℝ), archKernel r t := by
  simpa [quarterDigammaReal_eq_vertical, gaussVerticalKernel, archKernel,
    div_eq_mul_inv, mul_assoc] using
    verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral
      (by norm_num : (0 : ℝ) < 1 / 4) (r / 2)

theorem quarterDigammaReal_log_lower (r : ℝ) :
    (1 / 2 : ℝ) * Real.log (1 + 4 * r ^ 2) ≤
      quarterDigammaReal r - quarterDigammaReal 0 := by
  have h := verticalDigammaReal_log_lower
    (by norm_num : (0 : ℝ) < 1 / 4) (r / 2)
  rw [← quarterDigammaReal_eq_vertical r] at h
  have hzero : quarterDigammaReal 0 = verticalDigammaReal (1 / 4) 0 := by
    unfold quarterDigammaReal verticalDigammaReal
    norm_num
  rw [← hzero] at h
  have harg : (1 : ℝ) + (r / 2) ^ 2 / (1 / 4) ^ 2 = 1 + 4 * r ^ 2 := by
    norm_num
    ring
  rw [harg] at h
  exact h

/-- A sharper quarter-line upper bound than the historical `+8` estimate. -/
theorem quarterDigammaReal_log_upper_four (r : ℝ) :
    quarterDigammaReal r - quarterDigammaReal 0 ≤
      (1 / 2 : ℝ) * Real.log (1 + 4 * r ^ 2) + 4 := by
  have h := verticalDigammaReal_log_upper
    (by norm_num : (0 : ℝ) < 1 / 4) (r / 2)
  rw [← quarterDigammaReal_eq_vertical r] at h
  have hzero : quarterDigammaReal 0 = verticalDigammaReal (1 / 4) 0 := by
    unfold quarterDigammaReal verticalDigammaReal
    norm_num
  rw [← hzero] at h
  have harg : (1 : ℝ) + (r / 2) ^ 2 / (1 / 4) ^ 2 = 1 + 4 * r ^ 2 := by
    norm_num
    ring
  rw [harg] at h
  have hcorr :
      (1 / (1 / 4 : ℝ) - (1 / 4 : ℝ) /
        ((1 / 4 : ℝ) ^ 2 + (r / 2) ^ 2)) ≤ 4 := by
    have hnonneg : 0 ≤ (1 / 4 : ℝ) /
        ((1 / 4 : ℝ) ^ 2 + (r / 2) ^ 2) := by positivity
    norm_num
    linarith
  linarith

theorem quarterDigammaReal_log_upper (r : ℝ) :
    quarterDigammaReal r - quarterDigammaReal 0 ≤
      (1 / 2 : ℝ) * Real.log (1 + 4 * r ^ 2) + 8 := by
  linarith [quarterDigammaReal_log_upper_four r]

end

end GlideKernel
