/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.AutocorrelationPlancherel

/-!
# Compact-support cutoff for interval autocorrelation

The canonical zero extension of a vector in `L²([-a,a])` has zero
autocorrelation once the translation magnitude reaches the interval diameter.
At equality the two supports can meet only at an endpoint, a null set for
Lebesgue measure.
-/

namespace RHP2Bridge.AutocorrelationPlancherel

open scoped InnerProductSpace

noncomputable section

/-- A translate by at least the diameter of `[-a,a]` has zero
autocorrelation. The equality case is handled almost everywhere by removing
the two interval endpoints. -/
theorem intervalAutocorrelation_eq_zero_of_two_mul_le
    {a u : ℝ} (w : LegendreScaledL2.IntervalL2 a) (h : 2 * a ≤ |u|) :
    intervalAutocorrelation a u w = 0 := by
  rw [intervalAutocorrelation_eq_integral]
  calc
    (∫ x, RCLike.re
        ⟪IntervalZeroExtension.zeroExtensionFn a w x,
          IntervalZeroExtension.zeroExtensionFn a w (x + u)⟫_ℂ) =
        ∫ _x : ℝ, (0 : ℝ) := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [
        MeasureTheory.Measure.ae_ne
          (MeasureTheory.volume : MeasureTheory.Measure ℝ) a,
        MeasureTheory.Measure.ae_ne
          (MeasureTheory.volume : MeasureTheory.Measure ℝ) (-a)
      ] with x hxa hxna
      by_cases hx : x ∈ LegendreScaledL2.Interval a
      · by_cases hxu : x + u ∈ LegendreScaledL2.Interval a
        · rcases hx with ⟨hxlo, hxhi⟩
          rcases hxu with ⟨hxulo, hxuhi⟩
          have hxlo' : -a < x := lt_of_le_of_ne hxlo (Ne.symm hxna)
          have hxhi' : x < a := lt_of_le_of_ne hxhi hxa
          have hulower : -(2 * a) < u := by linarith
          have huupper : u < 2 * a := by linarith
          have huabs : |u| < 2 * a := (abs_lt).2 ⟨hulower, huupper⟩
          exact (not_lt_of_ge h huabs).elim
        · rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a w hxu]
          simp
      · rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a w hx]
        simp
    _ = 0 := by simp

end

end RHP2Bridge.AutocorrelationPlancherel
