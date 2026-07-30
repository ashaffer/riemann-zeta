/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import IntervalZeroExtension
import FullInfLegendreLedger

/-!
# The p2 Fourier band operator

This file specializes the canonical zero-extension/Plancherel construction
to the p2 parameters and transfers the exact Legendre band ledger to its
Hilbert-space norm.
-/

namespace FullInfFourierBridge

open scoped ENNReal InnerProductSpace

/-- The p2 band operator is globally contractive. -/
theorem p2_angularFourierBandCLM_norm_le
    (w : LegendreScaledL2.IntervalL2 (7 / 16)) :
    ‖IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 w‖ ≤ ‖w‖ :=
  IntervalZeroExtension.norm_angularFourierBandCLM_apply_le
    (7 / 16) 50 w

/-- Exact high-block F2 estimate for the actual Plancherel band operator.
The target is the rational endpoint constant consumed by the operator
ledger. -/
theorem p2_angularFourierBandCLM_norm_sq_le
    (w : LegendreScaledL2.IntervalL2 (7 / 16))
    (hw : w ∈
      (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48)ᗮ) :
    ‖IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 w‖ ^ 2 ≤
      (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2 := by
  rw [
    IntervalZeroExtension.norm_angularFourierBandCLM_apply_sq_eq_normalizedIntervalFourierBandEnergy
      (7 / 16) 50 (by norm_num) w]
  exact FullInfLegendreLedger.p2_normalizedIntervalFourierBandEnergy_le w hw

end FullInfFourierBridge
