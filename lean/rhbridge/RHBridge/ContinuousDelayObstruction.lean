/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ZeroModeConditions
import Glide.DigammaKernelBridge

/-!
# The archimedean term is a continuous-delay operator

Gauss's kernel representation shows that the digamma multiplier contains a
continuum of cosine translation defects.  Hence the zero-mode equation is not
a finite-delay recurrence between the discrete prime-shift interfaces.
-/

namespace RHP2Bridge.ContinuousDelayObstruction

noncomputable section

/-- Gauss's kernel in the ordinary Fourier normalization used by RHBridge.
The phase is the translation phase at spatial shift `t / 2`. -/
def ordinaryFrequencyDelayKernel (ξ t : ℝ) : ℝ :=
  Real.exp (-(1 / 4) * t) *
    ((1 - Real.cos (2 * Real.pi * ξ * (t / 2))) /
      (1 - Real.exp (-t)))

/-- Exact continuous-delay representation of the archimedean symbol. -/
theorem quarterDigammaReal_sub_zero_eq_continuousDelayIntegral (ξ : ℝ) :
    GlideKernel.quarterDigammaReal (2 * Real.pi * ξ) -
        GlideKernel.quarterDigammaReal 0 =
      ∫ t in Set.Ioi (0 : ℝ), ordinaryFrequencyDelayKernel ξ t := by
  rw [GlideKernel.quarterDigammaReal_sub_zero_eq_archKernel_integral]
  apply MeasureTheory.setIntegral_congr_fun measurableSet_Ioi
  intro t _
  unfold ordinaryFrequencyDelayKernel GlideKernel.archKernel
  congr 4
  ring

/-- Every positive delay has nonnegative weight.  Thus the representation is
genuinely supported on a continuum rather than only at prime shifts. -/
theorem ordinaryFrequencyDelayKernel_nonneg (ξ : ℝ) {t : ℝ} (ht : 0 < t) :
    0 ≤ ordinaryFrequencyDelayKernel ξ t := by
  unfold ordinaryFrequencyDelayKernel
  have hden : 0 < 1 - Real.exp (-t) := GlideKernel.one_sub_exp_neg_pos ht
  have hcos : 0 ≤ 1 - Real.cos (2 * Real.pi * ξ * (t / 2)) := by
    linarith [Real.cos_le_one (2 * Real.pi * ξ * (t / 2))]
  positivity

end

end RHP2Bridge.ContinuousDelayObstruction
