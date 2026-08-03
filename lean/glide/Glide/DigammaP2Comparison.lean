/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.DigammaKernelQuarter
import Glide.P2Symbol

/-!
# Compatibility bounds for the p=2 zeta symbol

This file is deliberately separate from the general Gauss digamma-kernel API.
-/

namespace GlideKernel

/-- A fixed coarse constant for comparing the exact p=2 symbol with its
logarithmic growth weight. -/
noncomputable def p2LogComparisonConstant : ℝ :=
  |quarterDigammaReal 0 - Real.log Real.pi| + p2PrimeAmplitude + 8

theorem p2LogComparisonConstant_nonneg : 0 ≤ p2LogComparisonConstant := by
  unfold p2LogComparisonConstant
  exact add_nonneg
    (add_nonneg (abs_nonneg _) p2PrimeAmplitude_nonneg) (by norm_num)

theorem abs_p2Omega_le_log_add (r : ℝ) :
    |p2Omega r| ≤
      Real.log (1 + 4 * r ^ 2) + p2LogComparisonConstant := by
  have hlo := quarterDigammaReal_log_lower r
  have hup := quarterDigammaReal_log_upper r
  have hlog : 0 ≤ Real.log (1 + 4 * r ^ 2) := by
    apply Real.log_nonneg
    nlinarith [sq_nonneg r]
  have hprime :
      |p2PrimeAmplitude * Real.cos (r * Real.log 2)| ≤ p2PrimeAmplitude := by
    rw [abs_mul, abs_of_nonneg p2PrimeAmplitude_nonneg]
    exact mul_le_of_le_one_right p2PrimeAmplitude_nonneg
      (Real.abs_cos_le_one _)
  have hprimeBounds := (abs_le.mp hprime)
  have hbaseBounds := (abs_le.mp
    (le_refl |quarterDigammaReal 0 - Real.log Real.pi|))
  rw [abs_le]
  constructor <;> unfold p2Omega p2LogComparisonConstant at * <;> linarith

theorem log_le_two_abs_p2Omega_add (r : ℝ) :
    Real.log (1 + 4 * r ^ 2) ≤
      2 * |p2Omega r| + 2 * p2LogComparisonConstant := by
  have hlo := quarterDigammaReal_log_lower r
  have hprime :
      |p2PrimeAmplitude * Real.cos (r * Real.log 2)| ≤ p2PrimeAmplitude := by
    rw [abs_mul, abs_of_nonneg p2PrimeAmplitude_nonneg]
    exact mul_le_of_le_one_right p2PrimeAmplitude_nonneg
      (Real.abs_cos_le_one _)
  have hprimeBounds := (abs_le.mp hprime)
  have habs := le_abs_self (p2Omega r)
  have hbaseBounds := (abs_le.mp
    (le_refl |quarterDigammaReal 0 - Real.log Real.pi|))
  unfold p2Omega p2LogComparisonConstant at *
  linarith

end GlideKernel
