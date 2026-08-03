/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.AutocorrelationPlancherelCore
import IntervalZeroExtension

/-!
# Interval wrappers for autocorrelation and Plancherel

The general real-line correlation theory is in
`RHBridge.AutocorrelationPlancherelCore`.  This file only identifies it with
the canonical zero-extension vectors used by the certificate development.
-/

namespace RHP2Bridge.AutocorrelationPlancherel

open scoped ENNReal InnerProductSpace FourierTransform ComplexConjugate

noncomputable section

/-- The generic `L²` representative of the zero-extension function is the
canonical zero-extension vector already used by the certificate. -/
theorem toFullLineL2_zeroExtensionFn_eq
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    toFullLineL2 (IntervalZeroExtension.zeroExtensionFn a w)
        (IntervalZeroExtension.zeroExtensionFn_memLp a w) =
      IntervalZeroExtension.zeroExtension a w := by
  apply MeasureTheory.Lp.ext
  exact (IntervalZeroExtension.zeroExtensionFn_memLp a w).coeFn_toLp.trans
    (IntervalZeroExtension.coeFn_zeroExtension a w).symm

/-- Autocorrelation of the actual compactly supported interval vector. -/
def intervalAutocorrelation
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) : ℝ :=
  autocorrelation u (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)

/-- Plancherel/Wiener--Khinchin identity for the repository's canonical zero
extension and Fourier transform. -/
theorem intervalAutocorrelation_eq_cos_fourier_energy
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    intervalAutocorrelation a u w =
      ∫ xi, Real.cos (2 * Real.pi * u * xi) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) xi‖ ^ 2 := by
  unfold intervalAutocorrelation
  rw [autocorrelation_eq_cos_fourier_energy u
    (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp_one a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)]
  rw [toFullLineL2_zeroExtensionFn_eq]
  rfl

/-- Time-domain integral spelling for the interval autocorrelation. -/
theorem intervalAutocorrelation_eq_integral
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    intervalAutocorrelation a u w =
      ∫ x, RCLike.re
        ⟪IntervalZeroExtension.zeroExtensionFn a w x,
          IntervalZeroExtension.zeroExtensionFn a w (x + u)⟫_ℂ := by
  exact autocorrelation_eq_integral u
    (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)

end

end RHP2Bridge.AutocorrelationPlancherel
