/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.BasicCore
import Glide.GammaUniform

/-!
# Gauss's digamma kernel on positive vertical lines

This file turns Gauss's absolutely convergent two-point series into the
integral identity

`Re ψ(a + I*y) - Re ψ(a) = ∫₀∞ exp(-a*t) (1-cos(y*t))/(1-exp(-t)) dt`

for every `a > 0`.  It also proves a two-sided logarithmic comparison.  This
module contains no fixed vertical-line or prime/certificate normalization;
quarter-line compatibility results live in `Glide.DigammaKernelQuarter`.
-/

namespace GlideKernel

open Set MeasureTheory

noncomputable section

/-- The Gauss kernel for the change in the real part of digamma along the
vertical line `Re z = a`. -/
def gaussVerticalKernel (a y t : ℝ) : ℝ :=
  Real.exp (-a * t) * (1 - Real.cos (y * t)) / (1 - Real.exp (-t))

/-- The real summand in Gauss's vertical-line digamma difference series. -/
def verticalDigammaDifferenceTerm (a y : ℝ) (n : ℕ) : ℝ :=
  (Complex.digammaDifferenceTerm
    ((a : ℂ) + Complex.I * (y : ℂ)) (a : ℂ) n).re

/-- Gauss's vertical-line difference series is absolutely summable. -/
lemma summable_verticalDigammaDifferenceTerm {a : ℝ} (ha : 0 < a) (y : ℝ) :
    Summable (verticalDigammaDifferenceTerm a y) := by
  have hs : Summable (fun n : ℕ => Complex.digammaDifferenceTerm
      ((a : ℂ) + Complex.I * (y : ℂ)) (a : ℂ) n) :=
    Complex.summable_digammaDifferenceTerm (by simpa using ha) (by simpa using ha)
  have hre := hs.map Complex.reCLM Complex.reCLM.continuous
  change Summable (fun n : ℕ =>
    (Complex.digammaDifferenceTerm
      ((a : ℂ) + Complex.I * (y : ℂ)) (a : ℂ) n).re) at hre
  change Summable (fun n : ℕ =>
    (Complex.digammaDifferenceTerm
      ((a : ℂ) + Complex.I * (y : ℂ)) (a : ℂ) n).re)
  exact hre

lemma verticalDigammaDifferenceTerm_eq {a : ℝ} (ha : 0 < a) (y : ℝ) (n : ℕ) :
    verticalDigammaDifferenceTerm a y n =
      1 / ((n : ℝ) + a) -
        ((n : ℝ) + a) / (((n : ℝ) + a) ^ 2 + y ^ 2) := by
  unfold verticalDigammaDifferenceTerm Complex.digammaDifferenceTerm
  have hna : (n : ℝ) + a ≠ 0 := by positivity
  norm_num [Complex.div_re, Complex.normSq_apply, Complex.mul_re,
    Complex.mul_im, pow_two]
  field_simp
  ring

lemma verticalDigammaDifferenceTerm_nonneg {a : ℝ} (ha : 0 < a)
    (y : ℝ) (n : ℕ) : 0 ≤ verticalDigammaDifferenceTerm a y n := by
  rw [verticalDigammaDifferenceTerm_eq ha]
  have hna : 0 < (n : ℝ) + a := by positivity
  have hden : 0 < ((n : ℝ) + a) ^ 2 + y ^ 2 := by positivity
  rw [sub_nonneg, div_le_div_iff₀ hden hna]
  nlinarith [sq_nonneg y]

/-- Gauss's exact series for the change in the real part of digamma along a
positive vertical line. -/
theorem verticalDigammaReal_sub_zero_eq_tsum {a : ℝ} (ha : 0 < a) (y : ℝ) :
    verticalDigammaReal a y - verticalDigammaReal a 0 =
      ∑' n : ℕ, verticalDigammaDifferenceTerm a y n := by
  let z : ℂ := (a : ℂ) + Complex.I * (y : ℂ)
  let w : ℂ := (a : ℂ)
  have hz : 0 < z.re := by simpa [z] using ha
  have hw : 0 < w.re := by simpa [w] using ha
  have hsum := Complex.summable_digammaDifferenceTerm hz hw
  have h := congrArg Complex.re (Complex.digamma_sub_eq_tsum hz hw)
  rw [Complex.re_tsum hsum] at h
  simpa [verticalDigammaReal, verticalDigammaDifferenceTerm, z, w,
    Complex.sub_re] using h

private def gaussVerticalSeriesTerm (a y : ℝ) (n : ℕ) (t : ℝ) : ℝ :=
  Real.exp (-((n : ℝ) + a) * t) * (1 - Real.cos (y * t))

private lemma gaussVerticalSeriesTerm_nonneg (a y : ℝ) (n : ℕ) (t : ℝ) :
    0 ≤ gaussVerticalSeriesTerm a y n t := by
  unfold gaussVerticalSeriesTerm
  exact mul_nonneg (Real.exp_pos _).le (one_sub_cos_nonneg _)

private lemma laplace_cos {a : ℝ} (ha : 0 < a) (y : ℝ) :
    ∫ t in Ioi (0 : ℝ), Real.exp (-a * t) * Real.cos (y * t) =
      a / (a ^ 2 + y ^ 2) := by
  let z : ℂ := (-a : ℝ) + Complex.I * y
  have hz : z.re < 0 := by simp [z, ha]
  have hint := integrableOn_exp_mul_complex_Ioi hz 0
  have hval := integral_exp_mul_complex_Ioi hz 0
  have hre := congrArg Complex.re hval
  have hre' : (∫ t in Ioi (0 : ℝ), (Complex.exp (z * t)).re) =
      (-Complex.exp (z * (0 : ℝ)) / z).re :=
    (integral_re hint).trans hre
  have hfun : (fun t : ℝ ↦ (Complex.exp (z * t)).re) =
      fun t ↦ Real.exp (-a * t) * Real.cos (y * t) := by
    funext t
    simp [z, Complex.exp_re, Complex.mul_re, Complex.mul_im]
  rw [hfun] at hre'
  convert hre' using 1
  simp [z, Complex.div_re, Complex.normSq_apply]
  field_simp

private lemma laplace_one_sub_cos {a : ℝ} (ha : 0 < a) (y : ℝ) :
    ∫ t in Ioi (0 : ℝ), Real.exp (-a * t) * (1 - Real.cos (y * t)) =
      1 / a - a / (a ^ 2 + y ^ 2) := by
  have hexp : IntegrableOn (fun t : ℝ ↦ Real.exp (-a * t)) (Ioi 0) := by
    simpa [neg_mul] using exp_neg_integrableOn_Ioi 0 ha
  have hcos : IntegrableOn
      (fun t : ℝ ↦ Real.exp (-a * t) * Real.cos (y * t)) (Ioi 0) := by
    apply hexp.mul_bdd
    · fun_prop
    · filter_upwards [] with t
      simpa [Real.norm_eq_abs] using Real.abs_cos_le_one (y * t)
  calc
    _ = (∫ t in Ioi (0 : ℝ), Real.exp (-a * t)) -
        ∫ t in Ioi (0 : ℝ),
          Real.exp (-a * t) * Real.cos (y * t) := by
      rw [← integral_sub hexp hcos]
      apply setIntegral_congr_fun measurableSet_Ioi
      intro t _
      ring
    _ = 1 / a - a / (a ^ 2 + y ^ 2) := by
      rw [laplace_cos ha y]
      have h := integral_exp_mul_Ioi (a := -a) (by linarith) 0
      simpa using h

private lemma integral_gaussVerticalSeriesTerm {a : ℝ} (ha : 0 < a)
    (y : ℝ) (n : ℕ) :
    ∫ t in Ioi (0 : ℝ), gaussVerticalSeriesTerm a y n t =
      verticalDigammaDifferenceTerm a y n := by
  have hna : 0 < (n : ℝ) + a := by positivity
  change (∫ t in Ioi (0 : ℝ),
    Real.exp (-((n : ℝ) + a) * t) * (1 - Real.cos (y * t))) = _
  rw [laplace_one_sub_cos hna y, verticalDigammaDifferenceTerm_eq ha]

private lemma integrable_gaussVerticalSeriesTerm {a : ℝ} (ha : 0 < a)
    (y : ℝ) (n : ℕ) :
    IntegrableOn (gaussVerticalSeriesTerm a y n) (Ioi (0 : ℝ)) := by
  let b : ℝ := (n : ℝ) + a
  have hb : 0 < b := by dsimp [b]; positivity
  have hexp : IntegrableOn (fun t : ℝ ↦ Real.exp (-b * t)) (Ioi 0) := by
    simpa [neg_mul] using exp_neg_integrableOn_Ioi 0 hb
  apply (hexp.const_mul 2).mono'
  · unfold gaussVerticalSeriesTerm
    fun_prop
  · filter_upwards [] with t
    rw [Real.norm_eq_abs, abs_of_nonneg (gaussVerticalSeriesTerm_nonneg a y n t)]
    have hc : 1 - Real.cos (y * t) ≤ 2 := by
      linarith [Real.neg_one_le_cos (y * t)]
    dsimp [gaussVerticalSeriesTerm, b]
    simpa [mul_comm] using
      mul_le_mul_of_nonneg_left hc (Real.exp_pos _).le

private lemma tsum_gaussVerticalSeriesTerm {a y t : ℝ} (ht : 0 < t) :
    ∑' n : ℕ, gaussVerticalSeriesTerm a y n t = gaussVerticalKernel a y t := by
  have hq : |Real.exp (-t)| < 1 := by
    rw [abs_of_pos (Real.exp_pos _), Real.exp_lt_one_iff]
    linarith
  have hgeom : ∑' n : ℕ, (Real.exp (-t)) ^ n =
      1 / (1 - Real.exp (-t)) := by
    simpa [one_div] using tsum_geometric_of_norm_lt_one hq
  unfold gaussVerticalSeriesTerm gaussVerticalKernel
  have hterm : ∀ n : ℕ,
      Real.exp (-((n : ℝ) + a) * t) * (1 - Real.cos (y * t)) =
        (Real.exp (-a * t) * (1 - Real.cos (y * t))) *
          (Real.exp (-t)) ^ n := by
    intro n
    rw [← Real.exp_nat_mul]
    have hexp : -((n : ℝ) + a) * t = -a * t + (n : ℝ) * (-t) := by ring
    rw [hexp, Real.exp_add]
    ring
  simp_rw [hterm]
  rw [tsum_mul_left, hgeom]
  ring

/-- Gauss's integral representation for the change in the real part of
digamma along any vertical line in the positive half-plane. -/
theorem verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral
    {a : ℝ} (ha : 0 < a) (y : ℝ) :
    verticalDigammaReal a y - verticalDigammaReal a 0 =
      ∫ t in Ioi (0 : ℝ), gaussVerticalKernel a y t := by
  have hsum : Summable (fun n : ℕ ↦
      ∫ t in Ioi (0 : ℝ), ‖gaussVerticalSeriesTerm a y n t‖) := by
    apply (summable_verticalDigammaDifferenceTerm ha y).congr
    intro n
    rw [← integral_gaussVerticalSeriesTerm ha y n]
    apply setIntegral_congr_fun measurableSet_Ioi
    intro t ht
    change gaussVerticalSeriesTerm a y n t = ‖gaussVerticalSeriesTerm a y n t‖
    rw [Real.norm_eq_abs,
      abs_of_nonneg (gaussVerticalSeriesTerm_nonneg a y n t)]
  have hinterchange := integral_tsum_of_summable_integral_norm
    (fun n : ℕ ↦ integrable_gaussVerticalSeriesTerm ha y n) hsum
  rw [verticalDigammaReal_sub_zero_eq_tsum ha y]
  rw [show (∑' n : ℕ, verticalDigammaDifferenceTerm a y n) =
      ∑' n : ℕ, ∫ t in Ioi (0 : ℝ), gaussVerticalSeriesTerm a y n t by
    apply tsum_congr
    intro n
    exact (integral_gaussVerticalSeriesTerm ha y n).symm]
  rw [hinterchange]
  apply setIntegral_congr_fun measurableSet_Ioi
  intro t ht
  exact tsum_gaussVerticalSeriesTerm ht

private def gaussLowerKernel (a y t : ℝ) : ℝ :=
  Real.exp (-a * t) * (1 - Real.cos (y * t)) / t

private lemma gaussVerticalKernel_nonneg (a y : ℝ) {t : ℝ} (ht : 0 < t) :
    0 ≤ gaussVerticalKernel a y t := by
  unfold gaussVerticalKernel
  have hden := one_sub_exp_neg_pos ht
  have hcos := one_sub_cos_nonneg (y * t)
  positivity

private lemma gaussLowerKernel_le (a y : ℝ) {t : ℝ} (ht : 0 < t) :
    gaussLowerKernel a y t ≤ gaussVerticalKernel a y t := by
  unfold gaussLowerKernel gaussVerticalKernel
  have hden := one_sub_exp_neg_pos ht
  have hcos := one_sub_cos_nonneg (y * t)
  have hden_le := one_sub_exp_neg_le (t := t)
  gcongr

private lemma gaussVerticalKernel_le_lower_add (a y : ℝ) {t : ℝ} (ht : 0 < t) :
    gaussVerticalKernel a y t ≤
      gaussLowerKernel a y t + Real.exp (-a * t) * (1 - Real.cos (y * t)) := by
  unfold gaussVerticalKernel gaussLowerKernel
  have hden := one_sub_exp_neg_pos ht
  have hcos := one_sub_cos_nonneg (y * t)
  have hrecip : 1 / (1 - Real.exp (-t)) ≤ 1 / t + 1 := by
    rw [div_add' _ _ _ (ne_of_gt ht), div_le_div_iff₀ hden ht]
    have key : t * Real.exp (-t) ≤ 1 - Real.exp (-t) := by
      have h₁ : t ≤ Real.exp t - 1 := le_exp_sub_one
      have h₂ : (Real.exp t - 1) * Real.exp (-t) = 1 - Real.exp (-t) := by
        rw [sub_mul, ← Real.exp_add]
        simp
      nlinarith [Real.exp_pos (-t)]
    nlinarith [key]
  calc
    Real.exp (-a * t) * (1 - Real.cos (y * t)) / (1 - Real.exp (-t)) =
        Real.exp (-a * t) * (1 - Real.cos (y * t)) *
          (1 / (1 - Real.exp (-t))) := by ring
    _ ≤ Real.exp (-a * t) * (1 - Real.cos (y * t)) * (1 / t + 1) := by
      gcongr
    _ = _ := by ring

private lemma gaussLowerKernel_bound (a y : ℝ) {t : ℝ} (ht : 0 < t) :
    ‖gaussLowerKernel a y t‖ ≤ |y| * Real.exp (-a * t) := by
  unfold gaussLowerKernel
  have hcos_nonneg := one_sub_cos_nonneg (y * t)
  have hcos := one_sub_cos_le_abs (y * t)
  rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
  have hquot : (1 - Real.cos (y * t)) / t ≤ |y| := by
    rw [div_le_iff₀ ht]
    calc
      1 - Real.cos (y * t) ≤ |y * t| := hcos
      _ = |y| * t := by rw [abs_mul, abs_of_pos ht]
  calc
    Real.exp (-a * t) * (1 - Real.cos (y * t)) / t =
        Real.exp (-a * t) * ((1 - Real.cos (y * t)) / t) := by ring
    _ ≤ Real.exp (-a * t) * |y| :=
      mul_le_mul_of_nonneg_left hquot (Real.exp_pos _).le
    _ = |y| * Real.exp (-a * t) := by ring

private lemma integrable_gaussLowerKernel {a : ℝ} (ha : 0 < a) (y : ℝ) :
    IntegrableOn (gaussLowerKernel a y) (Ioi (0 : ℝ)) := by
  refine (((exp_neg_integrableOn_Ioi 0 ha).const_mul |y|)).mono' ?_ ?_
  · unfold gaussLowerKernel
    apply ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioi
    apply ContinuousOn.div (Continuous.continuousOn (by fun_prop)) continuousOn_id
    intro t ht
    exact ne_of_gt ht
  · rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with t ht
    exact gaussLowerKernel_bound a y ht

private lemma integrable_gaussVerticalKernel {a : ℝ} (ha : 0 < a) (y : ℝ) :
    IntegrableOn (gaussVerticalKernel a y) (Ioi (0 : ℝ)) := by
  have hextra : IntegrableOn
      (fun t : ℝ => Real.exp (-a * t) * (1 - Real.cos (y * t))) (Ioi 0) := by
    have hfun : gaussVerticalSeriesTerm a y 0 =
        fun t : ℝ => Real.exp (-a * t) * (1 - Real.cos (y * t)) := by
      funext t
      simp [gaussVerticalSeriesTerm]
    rw [← hfun]
    exact integrable_gaussVerticalSeriesTerm ha y 0
  refine ((integrable_gaussLowerKernel ha y).add hextra).mono' ?_ ?_
  · unfold gaussVerticalKernel
    apply ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioi
    apply ContinuousOn.div (Continuous.continuousOn (by fun_prop))
      (Continuous.continuousOn (by fun_prop))
    intro t ht
    exact ne_of_gt (one_sub_exp_neg_pos ht)
  · rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with t ht
    rw [Real.norm_eq_abs, abs_of_nonneg (gaussVerticalKernel_nonneg a y ht),
      Pi.add_apply]
    exact gaussVerticalKernel_le_lower_add a y ht

private lemma integral_gaussLowerKernel {a : ℝ} (ha : 0 < a) (y : ℝ) :
    ∫ t in Ioi (0 : ℝ), gaussLowerKernel a y t =
      (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) := by
  have habs : ∀ t, gaussLowerKernel a y t =
      Real.exp (-a * t) * ((1 - Real.cos (|y| * t)) / t) := by
    intro t
    unfold gaussLowerKernel
    rcases abs_choice y with h | h
    · rw [h]
      ring
    · rw [h]
      simp only [neg_mul, Real.cos_neg]
      ring
  calc
    ∫ t in Ioi (0 : ℝ), gaussLowerKernel a y t =
        ∫ t in Ioi (0 : ℝ),
          Real.exp (-a * t) * ((1 - Real.cos (|y| * t)) / t) := by
      apply setIntegral_congr_fun measurableSet_Ioi
      intro t ht
      exact habs t
    _ = (1 / 2 : ℝ) * Real.log (1 + |y| ^ 2 / a ^ 2) :=
      frullani_cos ha (abs_nonneg y)
    _ = (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) := by rw [sq_abs]

/-- The real part of digamma on a positive vertical line has at least its
Frullani logarithmic growth. -/
theorem verticalDigammaReal_log_lower {a : ℝ} (ha : 0 < a) (y : ℝ) :
    (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) ≤
      verticalDigammaReal a y - verticalDigammaReal a 0 := by
  rw [verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral ha y,
    ← integral_gaussLowerKernel ha y]
  exact setIntegral_mono_on (integrable_gaussLowerKernel ha y)
    (integrable_gaussVerticalKernel ha y) measurableSet_Ioi
      (fun t ht => gaussLowerKernel_le a y ht)

/-- A quantitative upper companion to `verticalDigammaReal_log_lower`.  The
remainder is the exact elementary Laplace correction. -/
theorem verticalDigammaReal_log_upper {a : ℝ} (ha : 0 < a) (y : ℝ) :
    verticalDigammaReal a y - verticalDigammaReal a 0 ≤
      (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) +
        (1 / a - a / (a ^ 2 + y ^ 2)) := by
  rw [verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral ha y]
  have hextra : IntegrableOn
      (fun t : ℝ => Real.exp (-a * t) * (1 - Real.cos (y * t))) (Ioi 0) := by
    have hfun : gaussVerticalSeriesTerm a y 0 =
        fun t : ℝ => Real.exp (-a * t) * (1 - Real.cos (y * t)) := by
      funext t
      simp [gaussVerticalSeriesTerm]
    rw [← hfun]
    exact integrable_gaussVerticalSeriesTerm ha y 0
  calc
    (∫ t in Ioi (0 : ℝ), gaussVerticalKernel a y t) ≤
        ∫ t in Ioi (0 : ℝ),
          (gaussLowerKernel a y t +
            Real.exp (-a * t) * (1 - Real.cos (y * t))) := by
      exact setIntegral_mono_on (integrable_gaussVerticalKernel ha y)
        ((integrable_gaussLowerKernel ha y).add hextra) measurableSet_Ioi
          (fun t ht => gaussVerticalKernel_le_lower_add a y ht)
    _ = (∫ t in Ioi (0 : ℝ), gaussLowerKernel a y t) +
        ∫ t in Ioi (0 : ℝ), Real.exp (-a * t) * (1 - Real.cos (y * t)) :=
      integral_add (integrable_gaussLowerKernel ha y) hextra
    _ = _ := by rw [integral_gaussLowerKernel ha y, laplace_one_sub_cos ha y]

end

end GlideKernel

namespace Complex

noncomputable section

/-- Gauss's integral representation for the change in the real part of
digamma along a vertical line in the positive half-plane. -/
theorem re_digamma_add_mul_I_sub_eq_integral {a : ℝ} (ha : 0 < a) (y : ℝ) :
    (digamma ((a : ℂ) + I * (y : ℂ))).re - (digamma (a : ℂ)).re =
      ∫ t in Set.Ioi (0 : ℝ),
        Real.exp (-a * t) * (1 - Real.cos (y * t)) /
          (1 - Real.exp (-t)) := by
  simpa [GlideKernel.verticalDigammaReal, GlideKernel.gaussVerticalKernel] using
    GlideKernel.verticalDigammaReal_sub_zero_eq_gaussVerticalKernel_integral ha y

theorem re_digamma_add_mul_I_log_lower {a : ℝ} (ha : 0 < a) (y : ℝ) :
    (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) ≤
      (digamma ((a : ℂ) + I * (y : ℂ))).re - (digamma (a : ℂ)).re := by
  simpa [GlideKernel.verticalDigammaReal] using
    GlideKernel.verticalDigammaReal_log_lower ha y

theorem re_digamma_add_mul_I_log_upper {a : ℝ} (ha : 0 < a) (y : ℝ) :
    (digamma ((a : ℂ) + I * (y : ℂ))).re - (digamma (a : ℂ)).re ≤
      (1 / 2 : ℝ) * Real.log (1 + y ^ 2 / a ^ 2) +
        (1 / a - a / (a ^ 2 + y ^ 2)) := by
  simpa [GlideKernel.verticalDigammaReal] using
    GlideKernel.verticalDigammaReal_log_upper ha y

end

end Complex
