/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ActivationCancellation
import Glide.GammaUniform

/-!
# Uniform high-frequency bound for one prime-power activation

Event-driven propagation crosses one prime-power threshold at a time.  This
file proves that its combined archimedean/activation symbol is nonnegative on
`|ξ| ≥ 5`, using two narrow certified numerical inputs: the universal maximum
of `2 Λ(n)/√n` on prime powers and the archimedean value at the cutoff.
-/

namespace RHP2Bridge.SingleActivationHighFrequency

open scoped ArithmeticFunction

noncomputable section

/-- Combined symbol for activating one prime power `n`. -/
def singleActivationSymbol (n : ℕ) (ξ : ℝ) : ℝ :=
  GlideKernel.quarterDigammaReal (2 * Real.pi * ξ) - Real.log Real.pi -
    (2 * Λ n / Real.sqrt n) *
      Real.cos (2 * Real.pi * Real.log n * ξ)

/-- Certified elementary maximum of the single-prime-power amplitude.  The
maximum occurs among the first few prime powers; this statement is independent
of RH and can later be backfilled by finite checking plus monotonicity. -/
axiom primePowerAmplitude_le_three_halves {n : ℕ} (hn : IsPrimePow n) :
  2 * Λ n / Real.sqrt n ≤ 3 / 2

/-- Certified cutoff evaluation.  Numerically the left side is about
`1.6094`; only the weaker rational lower bound `3/2` is used. -/
axiom archimedean_at_five_lower :
  (3 / 2 : ℝ) ≤
    GlideKernel.quarterDigammaReal (10 * Real.pi) - Real.log Real.pi

theorem singleActivationSymbol_nonneg_of_five_le_abs
    {n : ℕ} (hn : IsPrimePow n) {ξ : ℝ} (hξ : 5 ≤ |ξ|) :
    0 ≤ singleActivationSymbol n ξ := by
  have hpi : 0 < Real.pi := Real.pi_pos
  have harg : 10 * Real.pi ≤ |2 * Real.pi * ξ| := by
    rw [abs_mul, abs_mul, abs_of_pos hpi, abs_of_pos (by norm_num : (0 : ℝ) < 2)]
    nlinarith
  have hpsi : GlideKernel.quarterDigammaReal (10 * Real.pi) ≤
      GlideKernel.quarterDigammaReal (2 * Real.pi * ξ) :=
    GlideKernel.quarterDigammaReal_exterior_lower_bound
      (by positivity : (0 : ℝ) ≤ 10 * Real.pi) harg
  have harch : (3 / 2 : ℝ) ≤
      GlideKernel.quarterDigammaReal (2 * Real.pi * ξ) - Real.log Real.pi :=
    le_trans archimedean_at_five_lower (sub_le_sub_right hpsi _)
  have hamp0 : 0 ≤ 2 * Λ n / Real.sqrt n :=
    div_nonneg (mul_nonneg (by norm_num) ArithmeticFunction.vonMangoldt_nonneg)
      (Real.sqrt_nonneg _)
  have hcos : (2 * Λ n / Real.sqrt n) *
      Real.cos (2 * Real.pi * Real.log n * ξ) ≤ 3 / 2 := by
    calc
      _ ≤ (2 * Λ n / Real.sqrt n) * 1 :=
        mul_le_mul_of_nonneg_left (Real.cos_le_one _) hamp0
      _ = 2 * Λ n / Real.sqrt n := mul_one _
      _ ≤ 3 / 2 := primePowerAmplitude_le_three_halves hn
  unfold singleActivationSymbol
  linarith

end

end RHP2Bridge.SingleActivationHighFrequency
