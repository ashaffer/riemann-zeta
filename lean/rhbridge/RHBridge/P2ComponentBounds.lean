/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2SphericalReal

/-!
# Uniform bounds for the canonical p=2 Fourier components

The generated panel certificates need stable sup bounds for products of
Fourier--Legendre components.  These bounds are analytic: the interval has
measure `7 / 8`, the plane wave has pointwise norm one, and every canonical
Legendre vector has `L²` norm one.  No sampled maximum enters the proof.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace

theorem p2_intervalMeasure_univ_le_one :
    MeasureTheory.measureUnivNNReal
      (LegendreScaledL2.intervalMeasure (7 / 16)) ≤ 1 := by
  rw [← ENNReal.coe_le_coe]
  rw [MeasureTheory.coe_measureUnivNNReal]
  rw [LegendreScaledL2.intervalMeasure,
    comap_subtype_coe_apply measurableSet_Icc]
  rw [Set.image_univ, Subtype.range_coe_subtype, Set.setOf_mem_eq]
  norm_num

theorem p2_continuousMap_toLp_norm_le_one :
    ‖(ContinuousMap.toLp 2
      (LegendreScaledL2.intervalMeasure (7 / 16)) ℝ :
        C(LegendreScaledL2.Interval (7 / 16), ℝ) →L[ℝ]
          LegendreScaledL2.IntervalL2 (7 / 16))‖ ≤ 1 := by
  calc
    _ ≤ (MeasureTheory.measureUnivNNReal
      (LegendreScaledL2.intervalMeasure (7 / 16)) : ℝ) ^
        (2 : ENNReal).toReal⁻¹ :=
      ContinuousMap.toLp_norm_le _
    _ ≤ 1 := by
      apply Real.rpow_le_one
      · positivity
      · exact_mod_cast p2_intervalMeasure_univ_le_one
      · positivity

theorem norm_p2PlaneWaveRealL2_le_one (z : ℝ) :
    ‖LegendreScaledL2.planeWaveRealL2 (7 / 16) z‖ ≤ 1 := by
  calc
    _ ≤ ‖(ContinuousMap.toLp 2
      (LegendreScaledL2.intervalMeasure (7 / 16)) ℝ :
        C(LegendreScaledL2.Interval (7 / 16), ℝ) →L[ℝ]
          LegendreScaledL2.IntervalL2 (7 / 16))‖ *
        ‖LegendreScaledL2.planeWaveRealContinuous (7 / 16) z‖ :=
      ContinuousLinearMap.le_opNorm _ _
    _ ≤ 1 * 1 := by
      apply mul_le_mul p2_continuousMap_toLp_norm_le_one
      · rw [ContinuousMap.norm_le _ (by norm_num)]
        intro x
        rw [Real.norm_eq_abs]
        exact (Complex.abs_re_le_norm _).trans_eq (by
          simp [LegendrePlaneWave.fourierPhase, Complex.norm_exp])
      · positivity
      · norm_num
    _ = 1 := by norm_num

theorem norm_p2PlaneWaveImagL2_le_one (z : ℝ) :
    ‖LegendreScaledL2.planeWaveImagL2 (7 / 16) z‖ ≤ 1 := by
  calc
    _ ≤ ‖(ContinuousMap.toLp 2
      (LegendreScaledL2.intervalMeasure (7 / 16)) ℝ :
        C(LegendreScaledL2.Interval (7 / 16), ℝ) →L[ℝ]
          LegendreScaledL2.IntervalL2 (7 / 16))‖ *
        ‖LegendreScaledL2.planeWaveImagContinuous (7 / 16) z‖ :=
      ContinuousLinearMap.le_opNorm _ _
    _ ≤ 1 * 1 := by
      apply mul_le_mul p2_continuousMap_toLp_norm_le_one
      · rw [ContinuousMap.norm_le _ (by norm_num)]
        intro x
        rw [Real.norm_eq_abs]
        exact (Complex.abs_im_le_norm _).trans_eq (by
          simp [LegendrePlaneWave.fourierPhase, Complex.norm_exp])
      · positivity
      · norm_num
    _ = 1 := by norm_num

theorem abs_p2LegendreCoeff_re_le_one (n : ℕ) (r : ℝ) :
    |(p2LegendreCoeff n r).re| ≤ 1 := by
  unfold p2LegendreCoeff p2LegendreBasis
  rw [show (IntervalFourierL2.intervalFourierCoeff (7 / 16)
      (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n) r).re =
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n)
        (LegendreScaledL2.planeWaveRealL2 (7 / 16) r) by
    rw [IntervalFourierL2.intervalFourierCoeff_apply]
    norm_num]
  rw [← Real.norm_eq_abs]
  calc
    _ ≤ ‖LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n‖ *
        ‖LegendreScaledL2.planeWaveRealL2 (7 / 16) r‖ :=
      norm_inner_le_norm _ _
    _ ≤ 1 * 1 := by
      apply mul_le_mul
      · rw [(LegendreScaledL2.scaledNormalizedLegendreL2_orthonormal
          (7 / 16) (by norm_num)).norm_eq_one]
      · exact norm_p2PlaneWaveRealL2_le_one r
      · positivity
      · norm_num
    _ = 1 := by norm_num

theorem abs_p2LegendreCoeff_im_le_one (n : ℕ) (r : ℝ) :
    |(p2LegendreCoeff n r).im| ≤ 1 := by
  unfold p2LegendreCoeff p2LegendreBasis
  rw [show (IntervalFourierL2.intervalFourierCoeff (7 / 16)
      (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n) r).im =
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n)
        (LegendreScaledL2.planeWaveImagL2 (7 / 16) r) by
    rw [IntervalFourierL2.intervalFourierCoeff_apply]
    norm_num]
  rw [← Real.norm_eq_abs]
  calc
    _ ≤ ‖LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n‖ *
        ‖LegendreScaledL2.planeWaveImagL2 (7 / 16) r‖ :=
      norm_inner_le_norm _ _
    _ ≤ 1 * 1 := by
      apply mul_le_mul
      · rw [(LegendreScaledL2.scaledNormalizedLegendreL2_orthonormal
          (7 / 16) (by norm_num)).norm_eq_one]
      · exact norm_p2PlaneWaveImagL2_le_one r
      · positivity
      · norm_num
    _ = 1 := by norm_num

theorem p2LegendreSphericalScale_nonneg (n : ℕ) :
    0 ≤ p2LegendreSphericalScale n := by
  unfold p2LegendreSphericalScale
  positivity

theorem p2LegendreSphericalScale_sq (n : ℕ) :
    p2LegendreSphericalScale n ^ 2 =
      7 * (2 * (n : ℝ) + 1) / 8 := by
  unfold p2LegendreSphericalScale
  rw [mul_pow, mul_pow,
    Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 7 / 16),
    Real.sq_sqrt (by positivity : (0 : ℝ) ≤ (2 * (n : ℝ) + 1) / 2)]
  ring

theorem p2LegendreSphericalScale_ge_half (n : ℕ) :
    (1 : ℝ) / 2 ≤ p2LegendreSphericalScale n := by
  let s := p2LegendreSphericalScale n
  have hs0 : 0 ≤ s := p2LegendreSphericalScale_nonneg n
  have hs2 : s ^ 2 = 7 * (2 * (n : ℝ) + 1) / 8 :=
    p2LegendreSphericalScale_sq n
  by_contra h
  have hslt : s < 1 / 2 := lt_of_not_ge h
  have hprod : 0 ≤ s * (1 / 2 - s) :=
    mul_nonneg hs0 (sub_nonneg.mpr hslt.le)
  have hn : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  nlinarith

theorem p2LegendreSphericalScale_le_ten (n : Fin 48) :
    p2LegendreSphericalScale n.val ≤ 10 := by
  let s := p2LegendreSphericalScale n.val
  have hs0 : 0 ≤ s := p2LegendreSphericalScale_nonneg n.val
  have hs2 : s ^ 2 = 7 * (2 * (n.val : ℝ) + 1) / 8 :=
    p2LegendreSphericalScale_sq n.val
  have hnNat : n.val ≤ 47 := by omega
  have hn : (n.val : ℝ) ≤ 47 := by exact_mod_cast hnNat
  by_contra h
  have hslt : 10 < s := lt_of_not_ge h
  have hprod : 0 < (s - 10) * (s + 10) := by positivity
  nlinarith

theorem abs_p2SphericalReal_even_le_two (j : ℕ) (r : ℝ) :
    |p2SphericalReal (2 * j) r| ≤ 2 := by
  have hc := abs_p2LegendreCoeff_re_le_one (2 * j) r
  have hmodel : (p2LegendreCoeff (2 * j) r).re =
      p2LegendreSphericalScale (2 * j) * (-1 : ℝ) ^ j *
        p2SphericalReal (2 * j) r := by
    rw [p2LegendreCoeff_even_re_eq]
    unfold p2LegendreSphericalScale
    congr 3
    · congr 2
      push_cast
      ring
  rw [hmodel] at hc
  rw [abs_mul, abs_mul, abs_pow, abs_neg, abs_one, one_pow, mul_one] at hc
  have hs0 := p2LegendreSphericalScale_nonneg (2 * j)
  rw [abs_of_nonneg hs0] at hc
  have hs := p2LegendreSphericalScale_ge_half (2 * j)
  have habs := abs_nonneg (p2SphericalReal (2 * j) r)
  nlinarith [mul_le_mul_of_nonneg_right hs habs]

theorem abs_p2SphericalReal_odd_le_two (j : ℕ) (r : ℝ) :
    |p2SphericalReal (2 * j + 1) r| ≤ 2 := by
  have hc := abs_p2LegendreCoeff_im_le_one (2 * j + 1) r
  have hmodel : (p2LegendreCoeff (2 * j + 1) r).im =
      -(p2LegendreSphericalScale (2 * j + 1) * (-1 : ℝ) ^ j *
        p2SphericalReal (2 * j + 1) r) := by
    rw [p2LegendreCoeff_odd_im_eq]
    unfold p2LegendreSphericalScale
    congr 4
    congr 2
    push_cast
    ring
  rw [hmodel] at hc
  rw [abs_neg, abs_mul, abs_mul, abs_pow, abs_neg, abs_one, one_pow,
    mul_one] at hc
  have hs0 := p2LegendreSphericalScale_nonneg (2 * j + 1)
  rw [abs_of_nonneg hs0] at hc
  have hs := p2LegendreSphericalScale_ge_half (2 * j + 1)
  have habs := abs_nonneg (p2SphericalReal (2 * j + 1) r)
  nlinarith [mul_le_mul_of_nonneg_right hs habs]

end RHP2Bridge
