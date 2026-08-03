/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendrePlaneWaveL2

/-!
Band-uniform and band-integrated forms of the real `L²` Legendre leakage
estimate.  The frequency integral below is ordinary, unnormalized Lebesgue
integration in `z`; no Fourier/Plancherel normalization is asserted here.
-/

namespace LegendrePlaneWaveBand

open scoped ENNReal InnerProductSpace

/-- The sum of the real and imaginary plane-wave coefficient energies seen by
`w`.  This is the squared modulus of the corresponding complex coefficient,
represented without introducing a complex `L²` space. -/
noncomputable def planeWaveInnerEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (z : ℝ) : ℝ :=
  ‖inner ℝ w (LegendreScaledL2.planeWaveRealL2 a z)‖ ^ 2 +
    ‖inner ℝ w (LegendreScaledL2.planeWaveImagL2 a z)‖ ^ 2

/-- The explicit endpoint majorant used on the symmetric frequency band
`[-b,b]`. -/
noncomputable def bandLeakageMajorant (a b : ℝ) (m : ℕ) : ℝ :=
  2 * a * (LegendreTail.doubleFactorialMajorant (a * b) m /
    (1 - (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))

/-- The double-factorial majorant is monotone in the squared argument. -/
theorem doubleFactorialMajorant_le_of_sq_le
    {x y : ℝ} (m : ℕ) (hxy : x ^ 2 ≤ y ^ 2) :
    LegendreTail.doubleFactorialMajorant x m ≤
      LegendreTail.doubleFactorialMajorant y m := by
  unfold LegendreTail.doubleFactorialMajorant
  have hpow : x ^ (2 * m) ≤ y ^ (2 * m) := by
    rw [show 2 * m = 2 * m by rfl, pow_mul, pow_mul]
    exact pow_le_pow_left₀ (sq_nonneg x) hxy m
  exact div_le_div_of_nonneg_right
    (mul_le_mul_of_nonneg_left hpow (by positivity)) (sq_nonneg _)

/-- The closed geometric-tail expression is monotone in the squared
frequency argument as long as its endpoint ratio is strictly below one. -/
theorem geometricTailMajorant_le_of_sq_le
    {x y : ℝ} (m : ℕ) (hxy : x ^ 2 ≤ y ^ 2)
    (hy : y ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    LegendreTail.doubleFactorialMajorant x m /
        (1 - x ^ 2 /
          ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) ≤
      LegendreTail.doubleFactorialMajorant y m /
        (1 - y ^ 2 /
          ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) := by
  let D : ℝ := (2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)
  have hD : 0 < D := by positivity
  have hratio : x ^ 2 / D ≤ y ^ 2 / D :=
    div_le_div_of_nonneg_right hxy hD.le
  have hyden : 0 < 1 - y ^ 2 / D := sub_pos.mpr hy
  have hden : 1 - y ^ 2 / D ≤ 1 - x ^ 2 / D := by linarith
  have hnum := doubleFactorialMajorant_le_of_sq_le m hxy
  change LegendreTail.doubleFactorialMajorant x m / (1 - x ^ 2 / D) ≤
    LegendreTail.doubleFactorialMajorant y m / (1 - y ^ 2 / D)
  exact div_le_div₀ (LegendreTail.doubleFactorialMajorant_nonneg y m)
    hnum hyden hden

/-- Every frequency in `[-b,b]` is controlled by the explicit endpoint
majorant at `b`. -/
theorem planeWave_inner_energy_le_on_band
    (a : ℝ) (ha : 0 < a) (b : ℝ) (hb : 0 ≤ b) (z : ℝ) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hz : z ∈ Set.Icc (-b) b)
    (hq : (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    planeWaveInnerEnergy a w z ≤
      ‖w‖ ^ 2 * bandLeakageMajorant a b m := by
  have habs : |z| ≤ b := abs_le.mpr hz
  have hza : (a * z) ^ 2 ≤ (a * b) ^ 2 := by
    have hsquare : z ^ 2 ≤ b ^ 2 := by
      rw [sq_le_sq]
      simpa [abs_of_nonneg hb] using habs
    nlinarith [sq_nonneg a]
  have hqz : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1 :=
    lt_of_le_of_lt
      (div_le_div_of_nonneg_right hza (by positivity)) hq
  have hpoint :=
    LegendrePlaneWaveL2.planeWave_inner_energy_le_of_mem_orthogonal
      a ha z m w hw hqz
  have htail := geometricTailMajorant_le_of_sq_le m hza hq
  calc
    planeWaveInnerEnergy a w z ≤
        ‖w‖ ^ 2 *
          (2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
            (1 - (a * z) ^ 2 /
              ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))))) := hpoint
    _ ≤ ‖w‖ ^ 2 * bandLeakageMajorant a b m := by
      apply mul_le_mul_of_nonneg_left
      · dsimp [bandLeakageMajorant]
        exact mul_le_mul_of_nonneg_left htail (by positivity)
      · positivity

/-! ## Continuity in the frequency parameter -/

theorem continuous_planeWaveRealContinuous (a : ℝ) :
    Continuous (LegendreScaledL2.planeWaveRealContinuous a) := by
  apply ContinuousMap.continuous_of_continuous_uncurry
  change Continuous (fun p : ℝ × LegendreScaledL2.Interval a ↦
    (LegendrePlaneWave.fourierPhase p.1 (p.2 : ℝ)).re)
  unfold LegendrePlaneWave.fourierPhase
  fun_prop

theorem continuous_planeWaveImagContinuous (a : ℝ) :
    Continuous (LegendreScaledL2.planeWaveImagContinuous a) := by
  apply ContinuousMap.continuous_of_continuous_uncurry
  change Continuous (fun p : ℝ × LegendreScaledL2.Interval a ↦
    (LegendrePlaneWave.fourierPhase p.1 (p.2 : ℝ)).im)
  unfold LegendrePlaneWave.fourierPhase
  fun_prop

theorem continuous_planeWaveRealL2 (a : ℝ) :
    Continuous (LegendreScaledL2.planeWaveRealL2 a) := by
  exact (ContinuousMap.toLp 2 (LegendreScaledL2.intervalMeasure a) ℝ).continuous.comp
    (continuous_planeWaveRealContinuous a)

theorem continuous_planeWaveImagL2 (a : ℝ) :
    Continuous (LegendreScaledL2.planeWaveImagL2 a) := by
  exact (ContinuousMap.toLp 2 (LegendreScaledL2.intervalMeasure a) ℝ).continuous.comp
    (continuous_planeWaveImagContinuous a)

/-- The real-form squared plane-wave coefficient is continuous in frequency. -/
theorem continuous_planeWaveInnerEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    Continuous (planeWaveInnerEnergy a w) := by
  apply Continuous.add
  · apply Continuous.pow
    apply Continuous.norm
    exact continuous_const.inner (continuous_planeWaveRealL2 a)
  · apply Continuous.pow
    apply Continuous.norm
    exact continuous_const.inner (continuous_planeWaveImagL2 a)

/-- Unnormalized Lebesgue-frequency band integral of the real-form
plane-wave energy. -/
noncomputable def planeWaveBandEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) : ℝ :=
  ∫ z in -b..b, planeWaveInnerEnergy a w z

/-- Integrated leakage on `[-b,b]`.  The factor `2*b` is the Lebesgue length
of the frequency band.  A Fourier convention carrying a factor such as
`1 / (2π)` must apply that normalization separately. -/
theorem planeWave_bandEnergy_le
    (a : ℝ) (ha : 0 < a) (b : ℝ) (hb : 0 ≤ b) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    planeWaveBandEnergy a w b ≤
      (2 * b) * (‖w‖ ^ 2 * bandLeakageMajorant a b m) := by
  rw [planeWaveBandEnergy]
  calc
    (∫ z in -b..b, planeWaveInnerEnergy a w z) ≤
        ∫ _z in -b..b, ‖w‖ ^ 2 * bandLeakageMajorant a b m := by
      apply intervalIntegral.integral_mono_on (by linarith)
      · exact Continuous.intervalIntegrable
          (continuous_planeWaveInnerEnergy a w) (-b) b
      · exact Continuous.intervalIntegrable
          (continuous_const : Continuous
            (fun _z : ℝ ↦ ‖w‖ ^ 2 * bandLeakageMajorant a b m)) (-b) b
      · intro z hz
        exact planeWave_inner_energy_le_on_band a ha b hb z m w hw hz hq
    _ = (2 * b) * (‖w‖ ^ 2 * bandLeakageMajorant a b m) := by
      rw [intervalIntegral.integral_const]
      change (b - -b) * (‖w‖ ^ 2 * bandLeakageMajorant a b m) = _
      ring

/-! ## An explicit Fourier normalization convention -/

/-- The same band energy with the conventional scalar factor `1 / (2π)`.
This is only a definition of the normalization used here; it does not assert
a Fourier--Plancherel theorem for an independently defined transform. -/
noncomputable def fourierNormalizedPlaneWaveBandEnergy
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) (b : ℝ) : ℝ :=
  (1 / (2 * Real.pi)) * planeWaveBandEnergy a w b

/-- The dimensionless leakage ratio corresponding to
`fourierNormalizedPlaneWaveBandEnergy`.  Expanding `bandLeakageMajorant`, this
is exactly `(2*a*b/π) * t_m(a*b)/(1-q_m(a*b))`. -/
noncomputable def fourierNormalizedBandLeakageMajorant
    (a b : ℝ) (m : ℕ) : ℝ :=
  (b / Real.pi) * bandLeakageMajorant a b m

/-- Integrated leakage with the explicitly chosen `1 / (2π)` scalar
normalization. -/
theorem fourierNormalizedPlaneWave_bandEnergy_le
    (a : ℝ) (ha : 0 < a) (b : ℝ) (hb : 0 ≤ b) (m : ℕ)
    (w : LegendreScaledL2.IntervalL2 a)
    (hw : w ∈ (LegendreScaledL2.finiteLegendreSubspace a m)ᗮ)
    (hq : (a * b) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    fourierNormalizedPlaneWaveBandEnergy a w b ≤
      ‖w‖ ^ 2 * fourierNormalizedBandLeakageMajorant a b m := by
  have h := mul_le_mul_of_nonneg_left
    (planeWave_bandEnergy_le a ha b hb m w hw hq)
    (show 0 ≤ 1 / (2 * Real.pi) by positivity)
  rw [fourierNormalizedPlaneWaveBandEnergy,
    fourierNormalizedBandLeakageMajorant]
  calc
    (1 / (2 * Real.pi)) * planeWaveBandEnergy a w b ≤
        (1 / (2 * Real.pi)) *
          ((2 * b) * (‖w‖ ^ 2 * bandLeakageMajorant a b m)) := h
    _ = ‖w‖ ^ 2 * ((b / Real.pi) * bandLeakageMajorant a b m) := by
      field_simp [Real.pi_ne_zero]

end LegendrePlaneWaveBand
