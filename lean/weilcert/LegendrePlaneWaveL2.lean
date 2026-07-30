/-
The complete real `L²` projection-tail estimate for the complex plane wave,
viewed as its real and imaginary components.
-/
import LegendreScaledL2

namespace LegendrePlaneWaveL2

open scoped ENNReal InnerProductSpace

/-- Cauchy--Schwarz after discarding the component of `x` in a subspace
orthogonal to `w`. -/
theorem norm_inner_sq_le_norm_sq_mul_starProjection_residual_sq
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (V : Submodule ℝ E) [V.HasOrthogonalProjection]
    (w x : E) (hw : w ∈ Vᗮ) :
    ‖inner ℝ w x‖ ^ 2 ≤ ‖w‖ ^ 2 * ‖x - V.starProjection x‖ ^ 2 := by
  have hproj : inner ℝ w (V.starProjection x) = 0 :=
    (V.mem_orthogonal' w).1 hw _ (V.starProjection_apply_mem x)
  have hinner : inner ℝ w x = inner ℝ w (x - V.starProjection x) := by
    rw [inner_sub_right, hproj, sub_zero]
  rw [hinner]
  have hcs := norm_inner_le_norm (𝕜 := ℝ) w (x - V.starProjection x)
  have hleft : 0 ≤ ‖inner ℝ w (x - V.starProjection x)‖ := norm_nonneg _
  have hright : 0 ≤ ‖w‖ * ‖x - V.starProjection x‖ :=
    mul_nonneg (norm_nonneg _) (norm_nonneg _)
  have hfactor := mul_nonneg (sub_nonneg.mpr hcs)
    (add_nonneg hright hleft)
  nlinarith

/-- The sum of the squared canonical-projection residuals of the real and
imaginary parts of `exp (-i z x)` is exactly the tail of the squared complex
Fourier--Legendre coefficients. -/
theorem planeWave_projection_residual_energy_eq_coefficient_tsum
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ) :
    ‖LegendreScaledL2.planeWaveRealL2 a z -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
      ‖LegendreScaledL2.planeWaveImagL2 a z -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 =
      ∑' n : ℕ,
        ‖LegendrePlaneWave.polyFourierIntegral
          (LegendreScaled.scaledNormalizedPlainLegendre a (m + n))
            z (-a) a‖ ^ 2 := by
  let realEnergy : ℕ → ℝ := fun n ↦
    ‖inner ℝ
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
      (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2
  let imagEnergy : ℕ → ℝ := fun n ↦
    ‖inner ℝ
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
      (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2
  have hrealAll : Summable (fun n : ℕ ↦
      ‖inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a n)
        (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2) :=
    by
      simpa only [LegendreScaledL2.scaledNormalizedLegendreHilbertBasis_apply]
        using (HilbertBasisTail.hasSum_sq_norm_inner
          (LegendreScaledL2.scaledNormalizedLegendreHilbertBasis a ha)
          (LegendreScaledL2.planeWaveRealL2 a z)).summable
  have himagAll : Summable (fun n : ℕ ↦
      ‖inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a n)
        (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2) :=
    by
      simpa only [LegendreScaledL2.scaledNormalizedLegendreHilbertBasis_apply]
        using (HilbertBasisTail.hasSum_sq_norm_inner
          (LegendreScaledL2.scaledNormalizedLegendreHilbertBasis a ha)
          (LegendreScaledL2.planeWaveImagL2 a z)).summable
  have hreal : Summable realEnergy := by
    rw [show realEnergy = fun n : ℕ ↦
        ‖inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
          (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 by rfl]
    simpa [Nat.add_comm] using (summable_nat_add_iff m).2 hrealAll
  have himag : Summable imagEnergy := by
    rw [show imagEnergy = fun n : ℕ ↦
        ‖inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
          (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 by rfl]
    simpa [Nat.add_comm] using (summable_nat_add_iff m).2 himagAll
  rw [← LegendreScaledL2.tsum_tail_eq_norm_starProjection_residual_sq
      a ha m (LegendreScaledL2.planeWaveRealL2 a z),
    ← LegendreScaledL2.tsum_tail_eq_norm_starProjection_residual_sq
      a ha m (LegendreScaledL2.planeWaveImagL2 a z)]
  change (∑' n : ℕ, realEnergy n) + (∑' n : ℕ, imagEnergy n) = _
  rw [← hreal.tsum_add himag]
  apply tsum_congr
  intro n
  rw [show realEnergy n =
      ‖inner ℝ
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
        (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 by rfl,
    show imagEnergy n =
      ‖inner ℝ
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (m + n))
        (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 by rfl,
    LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveReal a ha,
    LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveImag a ha]
  let c : ℂ := LegendrePlaneWave.polyFourierIntegral
    (LegendreScaled.scaledNormalizedPlainLegendre a (m + n)) z (-a) a
  change ‖c.re‖ ^ 2 + ‖c.im‖ ^ 2 = ‖c‖ ^ 2
  rw [Real.norm_eq_abs, Real.norm_eq_abs, sq_abs, sq_abs,
    Complex.sq_norm, Complex.normSq_apply]
  ring

/-- Explicit geometric bound for the complex plane-wave residual energy after
the first `m` scaled Legendre modes.  This is the full coefficient-to-canonical-
projection bridge on `[-a,a]`. -/
theorem planeWave_projection_residual_energy_le
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ)
    (hq : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    ‖LegendreScaledL2.planeWaveRealL2 a z -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
      ‖LegendreScaledL2.planeWaveImagL2 a z -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 ≤
      2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
        (1 - (a * z) ^ 2 /
          ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)))) := by
  rw [planeWave_projection_residual_energy_eq_coefficient_tsum a ha z m]
  exact
    (LegendreScaled.scaledNormalizedPlainLegendre_coefficient_tsum_tail_le
      a ha z m hq).2

/-- Pointwise leakage bound: a vector orthogonal to the first `m` scaled
Legendre modes sees at most its squared norm times the explicit complex
plane-wave residual energy. -/
theorem planeWave_inner_energy_le_of_mem_orthogonal
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    ‖inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
      ‖inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 ≤
      ‖w‖ ^ 2 *
        (2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
          (1 - (a * z) ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))) := by
  let V := LegendreScaledL2.finiteLegendreSubspace a m
  let realResidual := LegendreScaledL2.planeWaveRealL2 a z -
    V.starProjection (LegendreScaledL2.planeWaveRealL2 a z)
  let imagResidual := LegendreScaledL2.planeWaveImagL2 a z -
    V.starProjection (LegendreScaledL2.planeWaveImagL2 a z)
  have hreal :=
    norm_inner_sq_le_norm_sq_mul_starProjection_residual_sq V w
      (LegendreScaledL2.planeWaveRealL2 a z) hw
  have himag :=
    norm_inner_sq_le_norm_sq_mul_starProjection_residual_sq V w
      (LegendreScaledL2.planeWaveImagL2 a z) hw
  have hresidual := planeWave_projection_residual_energy_le a ha z m hq
  change
    ‖inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
        ‖inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 ≤ _
  calc
    _ ≤ ‖w‖ ^ 2 * ‖realResidual‖ ^ 2 +
        ‖w‖ ^ 2 * ‖imagResidual‖ ^ 2 := add_le_add hreal himag
    _ = ‖w‖ ^ 2 * (‖realResidual‖ ^ 2 + ‖imagResidual‖ ^ 2) := by
      ring
    _ ≤ ‖w‖ ^ 2 *
        (2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
          (1 - (a * z) ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))) := by
      apply mul_le_mul_of_nonneg_left
      · simpa [realResidual, imagResidual, V] using hresidual
      · positivity

end LegendrePlaneWaveL2
