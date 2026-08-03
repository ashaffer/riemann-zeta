/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.MeasureTheory.Integral.ExpDecay
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FunProp
import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Push
import Mathlib.Tactic.Ring

/-!
# Elementary Laplace and Frullani integrals

Main results (all sorry-free):

* `laplace_sin` :  for a > 0:   ∫ t in Ioi 0, exp (-a*t) * sin (s*t) = s / (a²+s²)
* `frullani_cos` : for a > 0, b ≥ 0:
      ∫ t in Ioi 0, exp (-a*t) * ((1 - cos (b*t)) / t) = (1/2) * log (1 + b²/a²)
The file contains no fixed vertical line or prime/certificate normalization.
The historical quarter-line kernel sandwich is in `Glide.BasicQuarter`.
-/

open Real MeasureTheory Set Filter Topology

namespace GlideKernel

/-! ### Part 0: small facts -/

lemma one_sub_exp_neg_pos {t : ℝ} (ht : 0 < t) : 0 < 1 - exp (-t) := by
  have : exp (-t) < 1 := exp_lt_one_iff.mpr (by linarith)
  linarith

lemma one_sub_exp_neg_le {t : ℝ} : 1 - exp (-t) ≤ t := by
  have := add_one_le_exp (-t)
  linarith

lemma le_exp_sub_one {t : ℝ} : t ≤ exp t - 1 := by
  have := add_one_le_exp t
  linarith

/-- `1 - cos u ≤ |u|` for all real `u`. -/
lemma one_sub_cos_le_abs (u : ℝ) : 1 - cos u ≤ |u| := by
  by_cases h : 2 ≤ |u|
  · have := neg_one_le_cos u
    linarith
  · push Not at h
    have hsq : 1 - cos u = 2 * sin (u / 2) ^ 2 := by
      have h2mul : (2 : ℝ) * (u / 2) = u := by ring
      have hc := cos_two_mul (u / 2)
      rw [h2mul] at hc
      nlinarith [hc, sin_sq_add_cos_sq (u / 2)]
    have h1 : |sin (u / 2)| ≤ |u / 2| := abs_sin_le_abs
    have hs : sin (u / 2) ^ 2 ≤ (u / 2) ^ 2 := by
      calc sin (u / 2) ^ 2 = |sin (u / 2)| ^ 2 := (sq_abs _).symm
        _ ≤ |u / 2| ^ 2 := pow_le_pow_left₀ (abs_nonneg _) h1 2
        _ = (u / 2) ^ 2 := sq_abs _
    have habs : u ^ 2 / 2 ≤ |u| := by
      have h2 : |u| ^ 2 ≤ 2 * |u| := by nlinarith [abs_nonneg u]
      calc u ^ 2 / 2 = |u| ^ 2 / 2 := by rw [sq_abs]
        _ ≤ |u| := by linarith
    calc 1 - cos u = 2 * sin (u / 2) ^ 2 := hsq
      _ ≤ 2 * (u / 2) ^ 2 := by nlinarith
      _ = u ^ 2 / 2 := by ring
      _ ≤ |u| := habs

lemma one_sub_cos_nonneg (u : ℝ) : 0 ≤ 1 - cos u := by
  have := cos_le_one u; linarith

/-! ### Part 1: the Laplace transform of sine -/

lemma laplace_sin {a : ℝ} (ha : 0 < a) (s : ℝ) :
    ∫ t in Ioi (0 : ℝ), exp (-a * t) * sin (s * t) = s / (a ^ 2 + s ^ 2) := by
  have hden : (0 : ℝ) < a ^ 2 + s ^ 2 := by positivity
  set F : ℝ → ℝ :=
    fun t => -(exp (-a * t) * (a * sin (s * t) + s * cos (s * t))) / (a ^ 2 + s ^ 2) with hF
  have hderiv : ∀ t ∈ Ioi (0 : ℝ), HasDerivAt F (exp (-a * t) * sin (s * t)) t := by
    intro t _
    have hlin : HasDerivAt (fun u : ℝ => -a * u) (-a) t := by
      simpa using (hasDerivAt_id t).const_mul (-a)
    have hexp : HasDerivAt (fun u => exp (-a * u)) (exp (-a * t) * -a) t := hlin.exp
    have hlin2 : HasDerivAt (fun u : ℝ => s * u) s t := by
      simpa using (hasDerivAt_id t).const_mul s
    have hsin : HasDerivAt (fun u => sin (s * u)) (cos (s * t) * s) t := hlin2.sin
    have hcos : HasDerivAt (fun u => cos (s * u)) (-sin (s * t) * s) t := hlin2.cos
    have hcomb :
        HasDerivAt (fun u => a * sin (s * u) + s * cos (s * u))
          (a * (cos (s * t) * s) + s * (-sin (s * t) * s)) t :=
      (hsin.const_mul a).add (hcos.const_mul s)
    have hprod := (hexp.mul hcomb).neg.div_const (a ^ 2 + s ^ 2)
    have hval : -(exp (-a * t) * -a * (a * sin (s * t) + s * cos (s * t)) +
          exp (-a * t) * (a * (cos (s * t) * s) + s * (-sin (s * t) * s))) /
        (a ^ 2 + s ^ 2) = exp (-a * t) * sin (s * t) := by
      rw [div_eq_iff (ne_of_gt hden)]
      ring
    rw [hF]
    exact hval ▸ hprod
  have hcont : ContinuousWithinAt F (Ici (0 : ℝ)) 0 := by
    apply Continuous.continuousWithinAt
    fun_prop
  have hint : IntegrableOn (fun t => exp (-a * t) * sin (s * t)) (Ioi (0 : ℝ)) := by
    refine (exp_neg_integrableOn_Ioi 0 ha).mono' ?_ ?_
    · fun_prop
    · filter_upwards with t
      rw [norm_mul, norm_eq_abs, norm_eq_abs, abs_exp]
      calc exp (-a * t) * |sin (s * t)| ≤ exp (-a * t) * 1 :=
            mul_le_mul_of_nonneg_left (abs_sin_le_one _) (le_of_lt (exp_pos _))
        _ = exp (-a * t) := mul_one _
  have hlim : Tendsto F atTop (𝓝 0) := by
    have hb : ∀ t : ℝ, ‖F t‖ ≤ (a + |s|) / (a ^ 2 + s ^ 2) * exp (-a * t) := by
      intro t
      rw [hF]
      have h1 : |a * sin (s * t) + s * cos (s * t)| ≤ a + |s| := by
        calc |a * sin (s * t) + s * cos (s * t)|
            ≤ |a * sin (s * t)| + |s * cos (s * t)| := abs_add_le _ _
          _ ≤ a * 1 + |s| * 1 := by
              rw [abs_mul, abs_mul, abs_of_pos ha]
              gcongr
              · exact abs_sin_le_one _
              · exact abs_cos_le_one _
          _ = a + |s| := by ring
      simp only [norm_eq_abs, abs_div, abs_neg, abs_mul, abs_exp, abs_of_pos hden]
      rw [div_le_iff₀ hden]
      calc exp (-a * t) * |a * sin (s * t) + s * cos (s * t)|
          ≤ exp (-a * t) * (a + |s|) :=
            mul_le_mul_of_nonneg_left h1 (le_of_lt (exp_pos _))
        _ = (a + |s|) / (a ^ 2 + s ^ 2) * exp (-a * t) * (a ^ 2 + s ^ 2) := by
            field_simp
    have hexp0 : Tendsto (fun t : ℝ => exp (-a * t)) atTop (𝓝 0) := by
      have hcomp : Tendsto (fun t : ℝ => a * t) atTop atTop :=
        Tendsto.const_mul_atTop ha tendsto_id
      exact (tendsto_exp_neg_atTop_nhds_zero.comp hcomp).congr
        (fun t => by simp [Function.comp_apply, neg_mul])
    have hlim0 := hexp0.const_mul ((a + |s|) / (a ^ 2 + s ^ 2))
    rw [mul_zero] at hlim0
    exact squeeze_zero_norm hb hlim0
  have key := integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim
  rw [key, hF]
  simp only [mul_zero, sin_zero, cos_zero, mul_one, zero_add,
    exp_zero, one_mul, zero_sub, neg_neg, neg_div]

/-! ### Part 2: the elementary log integral -/

lemma integral_s_div {a : ℝ} (ha : 0 < a) (b : ℝ) :
    ∫ s in (0 : ℝ)..b, s / (a ^ 2 + s ^ 2) = (1 / 2) * log (1 + b ^ 2 / a ^ 2) := by
  have hderiv : ∀ x ∈ uIcc (0 : ℝ) b,
      HasDerivAt (fun s => (1 / 2) * log (a ^ 2 + s ^ 2)) (x / (a ^ 2 + x ^ 2)) x := by
    intro x _
    have hne : a ^ 2 + x ^ 2 ≠ 0 := by positivity
    have h1 : HasDerivAt (fun s : ℝ => a ^ 2 + s ^ 2) (2 * x) x := by
      have := (hasDerivAt_pow 2 x).const_add (a ^ 2)
      simpa using this
    have h2 := (h1.log hne).const_mul (1 / 2 : ℝ)
    have hval : (1 / 2 : ℝ) * (2 * x / (a ^ 2 + x ^ 2)) = x / (a ^ 2 + x ^ 2) := by
      rw [← mul_div_assoc]
      congr 1
      ring
    exact hval ▸ h2
  have hcont : IntervalIntegrable (fun s => s / (a ^ 2 + s ^ 2)) volume 0 b := by
    apply Continuous.intervalIntegrable
    exact continuous_id.div (by fun_prop) (fun x => by positivity)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont]
  have ha2 : (0 : ℝ) < a ^ 2 := by positivity
  have hab : (0 : ℝ) < a ^ 2 + b ^ 2 := by positivity
  have h0 : (1 : ℝ) + b ^ 2 / a ^ 2 = (a ^ 2 + b ^ 2) / a ^ 2 := by field_simp
  rw [h0, log_div (ne_of_gt hab) (ne_of_gt ha2)]
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, add_zero]
  ring

/-! ### Part 3: the Frullani-type integral via Fubini -/

lemma inner_sin_integral {t : ℝ} (ht : 0 < t) (b : ℝ) :
    ∫ s in (0 : ℝ)..b, sin (s * t) = (1 - cos (b * t)) / t := by
  have hderiv : ∀ x ∈ uIcc (0 : ℝ) b,
      HasDerivAt (fun s => -cos (s * t) / t) (sin (x * t)) x := by
    intro x _
    have hlin : HasDerivAt (fun s : ℝ => s * t) t x := by
      simpa using (hasDerivAt_id x).mul_const t
    have h2 := (hlin.cos.neg).div_const t
    have hval : -(-sin (x * t) * t) / t = sin (x * t) := by
      rw [div_eq_iff (ne_of_gt ht)]
      ring
    exact hval ▸ h2
  have hcont : IntervalIntegrable (fun s => sin (s * t)) volume 0 b := by
    apply Continuous.intervalIntegrable; fun_prop
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont]
  rw [zero_mul, cos_zero]
  field_simp
  ring

theorem frullani_cos {a : ℝ} (ha : 0 < a) {b : ℝ} (hb : 0 ≤ b) :
    ∫ t in Ioi (0 : ℝ), exp (-a * t) * ((1 - cos (b * t)) / t)
      = (1 / 2) * log (1 + b ^ 2 / a ^ 2) := by
  rcases eq_or_lt_of_le hb with hb0 | hb0
  · simp [← hb0]
  set G : ℝ × ℝ → ℝ := fun p => exp (-a * p.1) * sin (p.2 * p.1) with hG
  have hGcont : Continuous G := by fun_prop
  set μ : Measure ℝ := volume.restrict (Ioi 0) with hμ
  set ν : Measure ℝ := volume.restrict (Ioc 0 b) with hν
  have hmeas : AEStronglyMeasurable G (μ.prod ν) := hGcont.aestronglyMeasurable
  have hint : Integrable G (μ.prod ν) := by
    rw [integrable_prod_iff hmeas]
    constructor
    · filter_upwards with t
      exact ((hGcont.comp (Continuous.prodMk continuous_const continuous_id)).integrableOn_Ioc)
    · have hbound : ∀ t : ℝ, (∫ s, ‖G (t, s)‖ ∂ν) ≤ b * exp (-a * t) := by
        intro t
        have h1 : ∀ s, ‖G (t, s)‖ ≤ exp (-a * t) := by
          intro s
          rw [hG]
          simp only [norm_mul, norm_eq_abs, abs_exp]
          calc exp (-a * t) * |sin (s * t)| ≤ exp (-a * t) * 1 :=
                mul_le_mul_of_nonneg_left (abs_sin_le_one _) (le_of_lt (exp_pos _))
            _ = exp (-a * t) := mul_one _
        calc (∫ s, ‖G (t, s)‖ ∂ν) ≤ ∫ _ in Ioc (0 : ℝ) b, exp (-a * t) := by
              rw [hν]
              apply setIntegral_mono_on
              · exact ((hGcont.comp
                  (Continuous.prodMk continuous_const continuous_id)).norm).integrableOn_Ioc
              · exact integrableOn_const measure_Ioc_lt_top.ne
              · exact measurableSet_Ioc
              · intro s _; exact h1 s
          _ = b * exp (-a * t) := by
              rw [setIntegral_const, smul_eq_mul]
              congr 1
              rw [Measure.real, Real.volume_Ioc, sub_zero,
                  ENNReal.toReal_ofReal (le_of_lt hb0)]
      refine Integrable.mono' ((exp_neg_integrableOn_Ioi 0 ha).const_mul b) ?_ ?_
      · exact (hGcont.norm.aestronglyMeasurable).integral_prod_right'
      · filter_upwards with t
        rw [norm_eq_abs, abs_of_nonneg (integral_nonneg fun s => norm_nonneg _)]
        exact hbound t
  have hswap := integral_integral_swap (f := fun t s => G (t, s)) hint
  have hleft : (∫ t, ∫ s, G (t, s) ∂ν ∂μ)
      = ∫ t in Ioi (0 : ℝ), exp (-a * t) * ((1 - cos (b * t)) / t) := by
    rw [hμ]
    apply setIntegral_congr_fun measurableSet_Ioi
    intro t ht
    change (∫ s in Ioc (0 : ℝ) b, G (t, s)) =
      exp (-a * t) * ((1 - cos (b * t)) / t)
    have hfun : (fun s => G (t, s)) = fun s => exp (-a * t) * sin (s * t) := rfl
    rw [← intervalIntegral.integral_of_le (le_of_lt hb0), hfun,
        intervalIntegral.integral_const_mul, inner_sin_integral ht b]
  have hright : (∫ s, ∫ t, G (t, s) ∂μ ∂ν)
      = (1 / 2) * log (1 + b ^ 2 / a ^ 2) := by
    have h1 : (∫ s, ∫ t, G (t, s) ∂μ ∂ν) = ∫ s in Ioc (0 : ℝ) b, s / (a ^ 2 + s ^ 2) := by
      rw [hν]
      apply setIntegral_congr_fun measurableSet_Ioc
      intro s _
      change (∫ t in Ioi (0 : ℝ), G (t, s)) = s / (a ^ 2 + s ^ 2)
      have hfun : (fun t => G (t, s)) = fun t => exp (-a * t) * sin (s * t) := rfl
      rw [hfun]
      exact laplace_sin ha s
    rw [h1, ← intervalIntegral.integral_of_le (le_of_lt hb0)]
    exact integral_s_div ha b
  calc ∫ t in Ioi (0 : ℝ), exp (-a * t) * ((1 - cos (b * t)) / t)
      = ∫ t, ∫ s, G (t, s) ∂ν ∂μ := hleft.symm
    _ = ∫ s, ∫ t, G (t, s) ∂μ ∂ν := hswap
    _ = (1 / 2) * log (1 + b ^ 2 / a ^ 2) := hright


end GlideKernel
