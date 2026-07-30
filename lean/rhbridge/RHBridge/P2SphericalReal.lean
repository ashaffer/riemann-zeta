/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2SphericalApprox
import RHBridge.P2Containment

/-!
# Real polynomial models for canonical p=2 Fourier coefficients

This module converts the complex spherical integral model into the exact real
components used by the even and odd canonical blocks.  On the whole band,
the generated degree-100 model has a kernel-checked error below `10⁻¹⁹` for
each of the 48 Legendre modes.
-/

namespace RHP2Bridge

open scoped BigOperators

noncomputable def sphericalJRealPolynomial (n N : ℕ) : Polynomial ℝ :=
  Polynomial.C (1 / (2 ^ (n + 1) * (n.factorial : ℝ))) * Polynomial.X ^ n *
    ∑ m ∈ Finset.range N,
      Polynomial.C ((Complex.I ^ m).re * weightMoment n m /
        (m.factorial : ℝ)) * Polynomial.X ^ m

theorem eval_sphericalJRealPolynomial (n N : ℕ) (z : ℝ) :
    (sphericalJRealPolynomial n N).eval z =
      (sphericalJPolynomial n N z).re := by
  unfold sphericalJRealPolynomial sphericalJPolynomial
  simp only [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_pow,
    Polynomial.eval_X, Polynomial.eval_finsetSum, Complex.mul_re,
    Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero,
    Complex.re_sum]
  rw [show 1 / (2 ^ (n + 1) * (n.factorial : ℝ)) * z ^ n =
    z ^ n / (2 ^ (n + 1) * (n.factorial : ℝ)) by ring]
  congr 1
  apply Finset.sum_congr rfl
  intro m hm
  rw [mul_pow]
  rw [← Complex.ofReal_pow]
  change _ = ((↑(z ^ m) * Complex.I ^ m) /
    ((m.factorial : ℝ) : ℂ) * (weightMoment n m : ℂ)).re
  rw [div_eq_mul_inv]
  norm_num [Complex.mul_re]
  simp only [← Complex.ofReal_pow, Complex.ofReal_re, Complex.ofReal_im]
  ring_nf

theorem abs_sphericalJReal_sub_polynomial_le
    (n N : ℕ) (z Z : ℝ) (hZ : |z| ≤ Z)
    (hN : Z / (N + 1 : ℝ) ≤ 1 / 2) :
    |(LegendreTail.sphericalJIntegralModel n z).re -
        (sphericalJRealPolynomial n N).eval z| ≤
      2 * Z ^ (n + N) /
        ((2 : ℝ) ^ n * (n.factorial : ℝ) * (N.factorial : ℝ)) := by
  rw [eval_sphericalJRealPolynomial]
  have hre := Complex.abs_re_le_norm
    (LegendreTail.sphericalJIntegralModel n z - sphericalJPolynomial n N z)
  rw [Complex.sub_re] at hre
  exact hre.trans (norm_sphericalJIntegralModel_sub_polynomial_le n N z Z hZ hN)

noncomputable def p2SphericalReal (n : ℕ) (r : ℝ) : ℝ :=
  (LegendreTail.sphericalJIntegralModel n ((7 / 16 : ℝ) * r)).re

theorem sphericalJIntegralModel_neg_re (n : ℕ) (z : ℝ) :
    (LegendreTail.sphericalJIntegralModel n (-z)).re =
      (-1 : ℝ) ^ n * (LegendreTail.sphericalJIntegralModel n z).re := by
  let F : ℝ → ℂ := fun t =>
    Complex.exp ((z * t : ℝ) * Complex.I) *
      (((1 - t ^ 2) ^ n : ℝ) : ℂ)
  let G : ℝ → ℂ := fun t =>
    Complex.exp (((-z) * t : ℝ) * Complex.I) *
      (((1 - t ^ 2) ^ n : ℝ) : ℂ)
  have hF : IntervalIntegrable F MeasureTheory.volume (-1) 1 := by
    apply Continuous.intervalIntegrable
    dsimp [F]
    fun_prop
  have hG : IntervalIntegrable G MeasureTheory.volume (-1) 1 := by
    apply Continuous.intervalIntegrable
    dsimp [G]
    fun_prop
  have hre : (∫ t in (-1 : ℝ)..1, G t).re =
      (∫ t in (-1 : ℝ)..1, F t).re := by
    change RCLike.re (∫ t in (-1 : ℝ)..1, G t) =
      RCLike.re (∫ t in (-1 : ℝ)..1, F t)
    rw [← intervalIntegral.intervalIntegral_re hG,
      ← intervalIntegral.intervalIntegral_re hF]
    apply intervalIntegral.integral_congr
    intro t ht
    dsimp [F, G]
    rw [Complex.mul_re, Complex.mul_re]
    simp only [Complex.ofReal_re, Complex.ofReal_im, mul_zero, sub_zero]
    rw [Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_re]
    rw [show -z * t = -(z * t) by ring, Real.cos_neg]
  unfold LegendreTail.sphericalJIntegralModel
  simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im, zero_mul,
    sub_zero]
  rw [hre, neg_pow]
  ring

@[simp] theorem p2SphericalReal_neg (n : ℕ) (r : ℝ) :
    p2SphericalReal n (-r) = (-1 : ℝ) ^ n * p2SphericalReal n r := by
  unfold p2SphericalReal
  rw [show (7 / 16 : ℝ) * -r = -((7 / 16 : ℝ) * r) by ring,
    sphericalJIntegralModel_neg_re]

theorem continuous_p2SphericalReal (n : ℕ) : Continuous (p2SphericalReal n) := by
  unfold p2SphericalReal LegendreTail.sphericalJIntegralModel
  fun_prop

theorem p2LegendreCoeff_eq_model (n : ℕ) (r : ℝ) :
    p2LegendreCoeff n r =
      ((Real.sqrt (7 / 16 : ℝ) : ℝ) : ℂ) *
        (((Real.sqrt ((2 * (n : ℝ) + 1) / 2) : ℝ) : ℂ) *
          (2 * (-Complex.I) ^ n *
            LegendreTail.sphericalJIntegralModel n ((7 / 16 : ℝ) * r))) := by
  change IntervalFourierL2.intervalFourierCoeff (7 / 16)
    (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n) r = _
  rw [IntervalFourierL2.intervalFourierCoeff_scaledNormalizedLegendreL2
    (7 / 16) (by norm_num)]
  exact LegendreScaled.polyFourierIntegral_scaledNormalizedPlainLegendre_eq_model
    (7 / 16) (by norm_num) n r

theorem p2LegendreCoeff_even_re_eq (j : ℕ) (r : ℝ) :
    (p2LegendreCoeff (2 * j) r).re =
      2 * Real.sqrt (7 / 16 : ℝ) *
        Real.sqrt ((4 * (j : ℝ) + 1) / 2) *
        (-1 : ℝ) ^ j * p2SphericalReal (2 * j) r := by
  rw [p2LegendreCoeff_eq_model]
  unfold p2SphericalReal
  rw [pow_mul]
  have hsq : (-Complex.I) ^ 2 = (-1 : ℂ) := by norm_num
  rw [hsq]
  have hphase : (-1 : ℂ) ^ j = (((-1 : ℝ) ^ j : ℝ) : ℂ) := by
    norm_cast
  rw [hphase]
  norm_num [Complex.mul_re]
  simp only [hphase, Complex.ofReal_re, Complex.ofReal_im]
  ring_nf

theorem p2LegendreCoeff_odd_im_eq (j : ℕ) (r : ℝ) :
    (p2LegendreCoeff (2 * j + 1) r).im =
      -(2 * Real.sqrt (7 / 16 : ℝ) *
        Real.sqrt ((4 * (j : ℝ) + 3) / 2) *
        (-1 : ℝ) ^ j * p2SphericalReal (2 * j + 1) r) := by
  rw [p2LegendreCoeff_eq_model]
  unfold p2SphericalReal
  rw [pow_add, pow_mul]
  have hsq : (-Complex.I) ^ 2 = (-1 : ℂ) := by norm_num
  rw [hsq]
  have hphase : (-1 : ℂ) ^ j = (((-1 : ℝ) ^ j : ℝ) : ℂ) := by
    norm_cast
  rw [hphase]
  norm_num [Complex.mul_im, Complex.mul_re]
  simp only [hphase, Complex.ofReal_re, Complex.ofReal_im]
  ring_nf

noncomputable def p2LegendreSphericalScale (n : ℕ) : ℝ :=
  2 * Real.sqrt (7 / 16 : ℝ) *
    Real.sqrt ((2 * (n : ℝ) + 1) / 2)

theorem p2EvenBandIntegrand_eq_spherical (i j : ℕ) (r : ℝ) :
    p2EvenBandIntegrand i j r =
      (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
        p2LegendreSphericalScale (2 * j) *
        p2LegendreSphericalScale (2 * i) * (-1 : ℝ) ^ (i + j) *
        p2SphericalReal (2 * j) r * p2SphericalReal (2 * i) r := by
  unfold p2EvenBandIntegrand
  rw [p2LegendreCoeff_even_re_eq, p2LegendreCoeff_even_re_eq]
  unfold p2LegendreSphericalScale
  rw [pow_add]
  push_cast
  ring_nf

theorem p2OddBandIntegrand_eq_spherical (i j : ℕ) (r : ℝ) :
    p2OddBandIntegrand i j r =
      (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
        p2LegendreSphericalScale (2 * j + 1) *
        p2LegendreSphericalScale (2 * i + 1) * (-1 : ℝ) ^ (i + j) *
        p2SphericalReal (2 * j + 1) r * p2SphericalReal (2 * i + 1) r := by
  unfold p2OddBandIntegrand
  rw [p2LegendreCoeff_odd_im_eq, p2LegendreCoeff_odd_im_eq]
  unfold p2LegendreSphericalScale
  rw [pow_add]
  push_cast
  ring_nf

@[simp] theorem p2EvenBandIntegrand_neg (i j : ℕ) (r : ℝ) :
    p2EvenBandIntegrand i j (-r) = p2EvenBandIntegrand i j r := by
  rw [p2EvenBandIntegrand_eq_spherical,
    p2EvenBandIntegrand_eq_spherical, GlideKernel.p2Omega_neg,
    p2SphericalReal_neg, p2SphericalReal_neg]
  simp only [pow_mul, neg_one_sq, one_pow, one_mul]

@[simp] theorem p2OddBandIntegrand_neg (i j : ℕ) (r : ℝ) :
    p2OddBandIntegrand i j (-r) = p2OddBandIntegrand i j r := by
  rw [p2OddBandIntegrand_eq_spherical,
    p2OddBandIntegrand_eq_spherical, GlideKernel.p2Omega_neg,
    p2SphericalReal_neg, p2SphericalReal_neg]
  simp only [pow_add, pow_mul, neg_one_sq, one_pow]
  ring

theorem continuous_p2EvenBandIntegrand (i j : ℕ) :
    Continuous (p2EvenBandIntegrand i j) := by
  rw [show p2EvenBandIntegrand i j = fun r =>
      (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
        p2LegendreSphericalScale (2 * j) *
        p2LegendreSphericalScale (2 * i) * (-1 : ℝ) ^ (i + j) *
        p2SphericalReal (2 * j) r * p2SphericalReal (2 * i) r by
    funext r
    exact p2EvenBandIntegrand_eq_spherical i j r]
  have hq : Continuous (fun r => GlideKernel.p2Omega r - GlideKernel.p2Alpha) :=
    GlideKernel.continuous_p2Omega.sub continuous_const
  exact (((((hq.mul continuous_const).mul continuous_const).mul continuous_const).mul
    (continuous_p2SphericalReal (2 * j))).mul
      (continuous_p2SphericalReal (2 * i)))

theorem continuous_p2OddBandIntegrand (i j : ℕ) :
    Continuous (p2OddBandIntegrand i j) := by
  rw [show p2OddBandIntegrand i j = fun r =>
      (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
        p2LegendreSphericalScale (2 * j + 1) *
        p2LegendreSphericalScale (2 * i + 1) * (-1 : ℝ) ^ (i + j) *
        p2SphericalReal (2 * j + 1) r * p2SphericalReal (2 * i + 1) r by
    funext r
    exact p2OddBandIntegrand_eq_spherical i j r]
  have hq : Continuous (fun r => GlideKernel.p2Omega r - GlideKernel.p2Alpha) :=
    GlideKernel.continuous_p2Omega.sub continuous_const
  exact (((((hq.mul continuous_const).mul continuous_const).mul continuous_const).mul
    (continuous_p2SphericalReal (2 * j + 1))).mul
      (continuous_p2SphericalReal (2 * i + 1)))

theorem integral_p2EvenBandIntegrand_symmetric (i j : ℕ) :
    (∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand i j r) =
      2 * ∫ r in (0 : ℝ)..50, p2EvenBandIntegrand i j r := by
  have hneg : IntervalIntegrable (p2EvenBandIntegrand i j)
      MeasureTheory.volume (-50) 0 :=
    (continuous_p2EvenBandIntegrand i j).intervalIntegrable (-50) 0
  have hpos : IntervalIntegrable (p2EvenBandIntegrand i j)
      MeasureTheory.volume 0 50 :=
    (continuous_p2EvenBandIntegrand i j).intervalIntegrable 0 50
  rw [← intervalIntegral.integral_add_adjacent_intervals hneg hpos]
  have hreflect := intervalIntegral.integral_comp_neg
    (a := (0 : ℝ)) (b := 50) (p2EvenBandIntegrand i j)
  simp only [neg_zero] at hreflect
  simp_rw [p2EvenBandIntegrand_neg] at hreflect
  rw [← hreflect]
  ring

theorem integral_p2OddBandIntegrand_symmetric (i j : ℕ) :
    (∫ r in (-50 : ℝ)..50, p2OddBandIntegrand i j r) =
      2 * ∫ r in (0 : ℝ)..50, p2OddBandIntegrand i j r := by
  have hneg : IntervalIntegrable (p2OddBandIntegrand i j)
      MeasureTheory.volume (-50) 0 :=
    (continuous_p2OddBandIntegrand i j).intervalIntegrable (-50) 0
  have hpos : IntervalIntegrable (p2OddBandIntegrand i j)
      MeasureTheory.volume 0 50 :=
    (continuous_p2OddBandIntegrand i j).intervalIntegrable 0 50
  rw [← intervalIntegral.integral_add_adjacent_intervals hneg hpos]
  have hreflect := intervalIntegral.integral_comp_neg
    (a := (0 : ℝ)) (b := 50) (p2OddBandIntegrand i j)
  simp only [neg_zero] at hreflect
  simp_rw [p2OddBandIntegrand_neg] at hreflect
  rw [← hreflect]
  ring

noncomputable def p2SphericalRealPolynomial (n N : ℕ) : Polynomial ℝ :=
  (sphericalJRealPolynomial n N).comp
    (Polynomial.C (7 / 16) * Polynomial.X)

@[simp] theorem eval_p2SphericalRealPolynomial (n N : ℕ) (r : ℝ) :
    (p2SphericalRealPolynomial n N).eval r =
      (sphericalJPolynomial n N ((7 / 16 : ℝ) * r)).re := by
  unfold p2SphericalRealPolynomial
  rw [Polynomial.eval_comp, Polynomial.eval_mul, Polynomial.eval_C,
    Polynomial.eval_X, eval_sphericalJRealPolynomial]

theorem abs_p2SphericalReal_sub_polynomial_le
    (n N : ℕ) (r Z : ℝ) (hZ : |(7 / 16 : ℝ) * r| ≤ Z)
    (hN : Z / (N + 1 : ℝ) ≤ 1 / 2) :
    |p2SphericalReal n r - (p2SphericalRealPolynomial n N).eval r| ≤
      2 * Z ^ (n + N) /
        ((2 : ℝ) ^ n * (n.factorial : ℝ) * (N.factorial : ℝ)) := by
  unfold p2SphericalReal
  rw [eval_p2SphericalRealPolynomial]
  have h := abs_sphericalJReal_sub_polynomial_le n N _ Z hZ hN
  rw [eval_sphericalJRealPolynomial] at h
  exact h

set_option maxRecDepth 10000 in
set_option maxHeartbeats 2000000 in
-- The uniform 48-case exact factorial comparison exceeds the default budget.
theorem abs_p2SphericalReal_sub_polynomial100_lt_1e19
    (n : Fin 48) {r : ℝ} (hr : |r| ≤ 50) :
    |p2SphericalReal n.val r -
        (p2SphericalRealPolynomial n.val 100).eval r| < 1 / 10 ^ 19 := by
  have hZ : |(7 / 16 : ℝ) * r| ≤ 175 / 8 := by
    rw [abs_mul, abs_of_nonneg (by norm_num : (0 : ℝ) ≤ 7 / 16)]
    calc
      (7 / 16 : ℝ) * |r| ≤ (7 / 16) * 50 := by gcongr
      _ = 175 / 8 := by norm_num
  have h := abs_p2SphericalReal_sub_polynomial_le
    n.val 100 r (175 / 8) hZ (by norm_num)
  refine h.trans_lt ?_
  fin_cases n <;> norm_num [Nat.factorial]

end RHP2Bridge
