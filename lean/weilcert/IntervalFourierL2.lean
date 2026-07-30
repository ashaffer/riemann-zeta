/-
The complex Fourier coefficient of a real `L²` vector on a compact
symmetric interval.

This module packages the two real plane-wave pairings from
`LegendreScaledL2` into one continuous real-linear complex functional and
identifies it with the actual Bochner integral against `exp (-i z x)`.
-/
import LegendrePlaneWaveBand
import Mathlib.Analysis.Fourier.FourierTransform

namespace IntervalFourierL2

open scoped ENNReal InnerProductSpace
open scoped FourierTransform

/-- The (unnormalized) complex Fourier coefficient on `[-a,a]`, first
defined as a continuous functional on the real interval `L²` space. -/
noncomputable def intervalFourierCoeffCLM (a z : ℝ) :
    LegendreScaledL2.IntervalL2 a →L[ℝ] ℂ :=
  Complex.ofRealCLM.comp
      (innerSL ℝ (LegendreScaledL2.planeWaveRealL2 a z)) +
    Complex.I • Complex.ofRealCLM.comp
      (innerSL ℝ (LegendreScaledL2.planeWaveImagL2 a z))

/-- The complex Fourier coefficient of `w` at angular frequency `z`. -/
noncomputable def intervalFourierCoeff
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) : ℂ :=
  intervalFourierCoeffCLM a z w

theorem intervalFourierCoeff_apply
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    intervalFourierCoeff a w z =
      (inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z) : ℝ) +
        Complex.I *
          (inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z) : ℝ) := by
  simp [intervalFourierCoeff, intervalFourierCoeffCLM, real_inner_comm]

/-- The selected `Lp` representative times the unit-modulus Fourier phase
is Bochner integrable on the finite interval. -/
theorem integrable_intervalFourierIntegrand
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    MeasureTheory.Integrable
      (fun x : LegendreScaledL2.Interval a ↦
        ((w x : ℝ) : ℂ) *
          LegendrePlaneWave.fourierPhase z (x : ℝ))
      (LegendreScaledL2.intervalMeasure a) := by
  have hw : MeasureTheory.Integrable
      (fun x : LegendreScaledL2.Interval a ↦ w x)
      (LegendreScaledL2.intervalMeasure a) :=
    (MeasureTheory.Lp.memLp w).integrable (by norm_num)
  have hwC : MeasureTheory.Integrable
      (fun x : LegendreScaledL2.Interval a ↦ ((w x : ℝ) : ℂ))
      (LegendreScaledL2.intervalMeasure a) :=
    Complex.ofRealCLM.integrable_comp hw
  apply hwC.mul_bdd (c := 1)
  · apply Continuous.aestronglyMeasurable
    unfold LegendrePlaneWave.fourierPhase
    fun_prop
  · filter_upwards [] with x
    simp [LegendrePlaneWave.fourierPhase, Complex.norm_exp]

/-- The continuous functional is the actual, unnormalized Bochner Fourier
integral of the selected `Lp` representative.  Thus this definition is
independent of the representative, while retaining the usual integral
formula. -/
theorem intervalFourierCoeff_eq_integral
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    intervalFourierCoeff a w z =
      ∫ x : LegendreScaledL2.Interval a,
        ((w x : ℝ) : ℂ) *
          LegendrePlaneWave.fourierPhase z (x : ℝ)
        ∂(LegendreScaledL2.intervalMeasure a) := by
  have hint := integrable_intervalFourierIntegrand a w z
  have hreal :
      (LegendreScaledL2.planeWaveRealL2 a z :
          LegendreScaledL2.Interval a → ℝ) =ᵐ[
            LegendreScaledL2.intervalMeasure a]
        LegendreScaledL2.planeWaveRealContinuous a z :=
    ContinuousMap.coeFn_toLp
      (LegendreScaledL2.intervalMeasure a)
      (LegendreScaledL2.planeWaveRealContinuous a z)
  have himag :
      (LegendreScaledL2.planeWaveImagL2 a z :
          LegendreScaledL2.Interval a → ℝ) =ᵐ[
            LegendreScaledL2.intervalMeasure a]
        LegendreScaledL2.planeWaveImagContinuous a z :=
    ContinuousMap.coeFn_toLp
      (LegendreScaledL2.intervalMeasure a)
      (LegendreScaledL2.planeWaveImagContinuous a z)
  apply Complex.ext
  · calc
      (intervalFourierCoeff a w z).re =
          inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z) := by
            rw [intervalFourierCoeff_apply]
            simp
      _ = ∫ x : LegendreScaledL2.Interval a,
          w x * (LegendrePlaneWave.fourierPhase z (x : ℝ)).re
          ∂(LegendreScaledL2.intervalMeasure a) := by
            rw [MeasureTheory.L2.inner_def]
            apply MeasureTheory.integral_congr_ae
            filter_upwards [hreal] with x hx
            rw [hx]
            simp [LegendreScaledL2.planeWaveRealContinuous, mul_comm]
      _ = ∫ x : LegendreScaledL2.Interval a,
          (((w x : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z (x : ℝ)).re
          ∂(LegendreScaledL2.intervalMeasure a) := by
            apply MeasureTheory.integral_congr_ae
            filter_upwards [] with x
            simp
      _ = (∫ x : LegendreScaledL2.Interval a,
          ((w x : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z (x : ℝ)
          ∂(LegendreScaledL2.intervalMeasure a)).re := by
            exact integral_re hint
  · calc
      (intervalFourierCoeff a w z).im =
          inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z) := by
            rw [intervalFourierCoeff_apply]
            simp
      _ = ∫ x : LegendreScaledL2.Interval a,
          w x * (LegendrePlaneWave.fourierPhase z (x : ℝ)).im
          ∂(LegendreScaledL2.intervalMeasure a) := by
            rw [MeasureTheory.L2.inner_def]
            apply MeasureTheory.integral_congr_ae
            filter_upwards [himag] with x hx
            rw [hx]
            simp [LegendreScaledL2.planeWaveImagContinuous, mul_comm]
      _ = ∫ x : LegendreScaledL2.Interval a,
          (((w x : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z (x : ℝ)).im
          ∂(LegendreScaledL2.intervalMeasure a) := by
            apply MeasureTheory.integral_congr_ae
            filter_upwards [] with x
            simp
      _ = (∫ x : LegendreScaledL2.Interval a,
          ((w x : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z (x : ℝ)
          ∂(LegendreScaledL2.intervalMeasure a)).im := by
            exact integral_im hint

/-- The squared complex modulus is exactly the sum of the two real
plane-wave pairing energies used by `LegendrePlaneWaveL2`. -/
theorem norm_intervalFourierCoeff_sq
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) :
    ‖intervalFourierCoeff a w z‖ ^ 2 =
      ‖inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
        ‖inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2 := by
  rw [intervalFourierCoeff_apply]
  rw [Complex.sq_norm, Complex.normSq_apply]
  simp [pow_two]

/-- Exact normalization bridge to Mathlib's Fourier convention.  Mathlib
uses `exp (-2 π i x ξ)`, so angular frequency `z` is ordinary frequency
`z / (2 π)`.  Restricting Lebesgue measure to `[-a,a]` makes this exactly
the polynomial interval integral used throughout the Rodrigues chain. -/
theorem polyFourierIntegral_eq_mathlib_fourierIntegral
    (a : ℝ) (ha : 0 ≤ a) (p : Polynomial ℝ) (z : ℝ) :
    LegendrePlaneWave.polyFourierIntegral p z (-a) a =
      Fourier.fourierIntegral Real.fourierChar
        (MeasureTheory.volume.restrict (Set.Icc (-a) a))
        (fun x : ℝ ↦ ((p.eval x : ℝ) : ℂ))
        (z / (2 * Real.pi)) := by
  rw [LegendrePlaneWave.polyFourierIntegral,
    intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  rw [Fourier.fourierIntegral_def]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  rw [Circle.smul_def, Real.fourierChar_apply]
  unfold LegendrePlaneWave.fourierPhase
  have hpi : 2 * Real.pi ≠ 0 := by positivity
  have hscalar :
      2 * Real.pi * (-(x * (z / (2 * Real.pi)))) = -(z * x) := by
    field_simp
  have hexp :
      ((2 * Real.pi * (-(x * (z / (2 * Real.pi))) : ℝ) : ℝ) : ℂ) *
          Complex.I =
        (-((z : ℂ) * Complex.I)) * (x : ℂ) := by
    rw [hscalar]
    push_cast
    ring
  rw [hexp]
  ring

/-- On the normalized scaled Legendre basis, the abstract `L²` coefficient
is exactly the polynomial Fourier integral already computed by the
Rodrigues chain. -/
theorem intervalFourierCoeff_scaledNormalizedLegendreL2
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    intervalFourierCoeff a
        (LegendreScaledL2.scaledNormalizedLegendreL2 a n) z =
      LegendrePlaneWave.polyFourierIntegral
        (LegendreScaled.scaledNormalizedPlainLegendre a n) z (-a) a := by
  apply Complex.ext
  · simpa [intervalFourierCoeff_apply] using
      (LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveReal
        a ha n z)
  · simpa [intervalFourierCoeff_apply] using
      (LegendreScaledL2.inner_scaledNormalizedLegendreL2_planeWaveImag
        a ha n z)

/-- The same basis coefficient, expressed directly with Mathlib's Fourier
integral and its `2 π` frequency convention. -/
theorem intervalFourierCoeff_scaledNormalizedLegendreL2_eq_mathlib
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    intervalFourierCoeff a
        (LegendreScaledL2.scaledNormalizedLegendreL2 a n) z =
      Fourier.fourierIntegral Real.fourierChar
        (MeasureTheory.volume.restrict (Set.Icc (-a) a))
        (fun x : ℝ ↦
          (((LegendreScaled.scaledNormalizedPlainLegendre a n).eval x : ℝ) : ℂ))
        (z / (2 * Real.pi)) := by
  rw [intervalFourierCoeff_scaledNormalizedLegendreL2 a ha]
  exact polyFourierIntegral_eq_mathlib_fourierIntegral a ha.le _ z

/-- The existing pointwise Legendre leakage theorem, now stated directly
for the squared modulus of the genuine complex Fourier coefficient. -/
theorem norm_intervalFourierCoeff_sq_le_of_mem_orthogonal
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    ‖intervalFourierCoeff a w z‖ ^ 2 ≤
      ‖w‖ ^ 2 *
        (2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
          (1 - (a * z) ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))) := by
  rw [norm_intervalFourierCoeff_sq]
  exact LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal
    a ha z m w hw hq

/-- Integral form of the same result: this is a bound for the actual
Fourier integral, with no remaining real/imaginary bookkeeping premise. -/
theorem norm_intervalFourierIntegral_sq_le_of_mem_orthogonal
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    ‖∫ x : LegendreScaledL2.Interval a,
        ((w x : ℝ) : ℂ) *
          LegendrePlaneWave.fourierPhase z (x : ℝ)
        ∂(LegendreScaledL2.intervalMeasure a)‖ ^ 2 ≤
      ‖w‖ ^ 2 *
        (2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
          (1 - (a * z) ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))) := by
  rw [← intervalFourierCoeff_eq_integral]
  exact norm_intervalFourierCoeff_sq_le_of_mem_orthogonal
    a ha z m w hw hq

/-! ## Repackaging the existing band theorem as genuine complex energy -/

/-- The normalized band energy of the genuine complex coefficient.  The
factor `1 / (2 π)` is the angular-frequency Plancherel normalization. -/
noncomputable def normalizedIntervalFourierBandEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) : ℝ :=
  (1 / (2 * Real.pi)) *
    ∫ z in -b..b, ‖intervalFourierCoeff a w z‖ ^ 2

/-- The complex-coefficient band energy is definitionally the real-form
energy bounded in `LegendrePlaneWaveBand`.  This removes the final
real/imaginary bookkeeping layer without reproving its integration result. -/
theorem normalizedIntervalFourierBandEnergy_eq_realForm
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) :
    normalizedIntervalFourierBandEnergy a w b =
      LegendrePlaneWaveBand.fourierNormalizedPlaneWaveBandEnergy a w b := by
  unfold normalizedIntervalFourierBandEnergy
    LegendrePlaneWaveBand.fourierNormalizedPlaneWaveBandEnergy
    LegendrePlaneWaveBand.planeWaveBandEnergy
    LegendrePlaneWaveBand.planeWaveInnerEnergy
  congr 1
  apply intervalIntegral.integral_congr
  intro z _hz
  exact norm_intervalFourierCoeff_sq a w z

/-- The same band energy written entirely as an iterated Bochner-integral
Fourier expression. -/
theorem normalizedIntervalFourierBandEnergy_eq_integral
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) :
    normalizedIntervalFourierBandEnergy a w b =
      (1 / (2 * Real.pi)) *
        ∫ z in -b..b,
          ‖∫ x : LegendreScaledL2.Interval a,
              ((w x : ℝ) : ℂ) *
                LegendrePlaneWave.fourierPhase z (x : ℝ)
              ∂(LegendreScaledL2.intervalMeasure a)‖ ^ 2 := by
  unfold normalizedIntervalFourierBandEnergy
  congr 1
  apply intervalIntegral.integral_congr
  intro z _hz
  change ‖intervalFourierCoeff a w z‖ ^ 2 = _
  rw [intervalFourierCoeff_eq_integral]

/-- The band-integrated F2 estimate, now stated for the actual complex
Fourier coefficient rather than its two real components. -/
theorem normalizedIntervalFourierBandEnergy_le_of_mem_orthogonal
    (a : ℝ) (ha : 0 < a) (b : ℝ) (hb : 0 ≤ b) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    normalizedIntervalFourierBandEnergy a w b ≤
      ‖w‖ ^ 2 *
        LegendrePlaneWaveBand.fourierNormalizedBandLeakageMajorant a b m := by
  rw [normalizedIntervalFourierBandEnergy_eq_realForm]
  exact LegendrePlaneWaveBand.fourierNormalizedPlaneWave_bandEnergy_le
    a ha b hb m w hw hq

end IntervalFourierL2
