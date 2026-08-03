/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/

import Glide.BasicCore

/-! # Fixed quarter-line kernel estimates -/

open Real MeasureTheory Set Filter Topology

namespace GlideKernel

/-! ### Part 4: the kernel sandwich -/

/-- The archimedean kernel integrand: by Gauss's digamma formula its integral
over `Ioi 0` equals
`Re (digamma (1/4 + I r/2)) - Re (digamma (1/4))`. -/
noncomputable def archKernel (r t : ℝ) : ℝ :=
  exp (-(1 / 4) * t) * ((1 - cos ((r / 2) * t)) / (1 - exp (-t)))

noncomputable def lowerFn (r t : ℝ) : ℝ :=
  exp (-(1 / 4) * t) * ((1 - cos ((r / 2) * t)) / t)

lemma archKernel_nonneg (r : ℝ) {t : ℝ} (ht : 0 < t) : 0 ≤ archKernel r t := by
  unfold archKernel
  have h1 := one_sub_exp_neg_pos ht
  have h2 := one_sub_cos_nonneg ((r / 2) * t)
  positivity

lemma lowerFn_le_archKernel (r : ℝ) {t : ℝ} (ht : 0 < t) : lowerFn r t ≤ archKernel r t := by
  unfold lowerFn archKernel
  have h1 := one_sub_exp_neg_pos ht
  have h2 := one_sub_cos_nonneg ((r / 2) * t)
  have h3 := one_sub_exp_neg_le (t := t)
  gcongr

lemma archKernel_le (r : ℝ) {t : ℝ} (ht : 0 < t) :
    archKernel r t ≤ lowerFn r t + exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) := by
  unfold archKernel lowerFn
  have h1 := one_sub_exp_neg_pos ht
  have h2 := one_sub_cos_nonneg ((r / 2) * t)
  have hrecip : 1 / (1 - exp (-t)) ≤ 1 / t + 1 := by
    rw [div_add' _ _ _ (ne_of_gt ht), div_le_div_iff₀ h1 ht]
    have key : t * exp (-t) ≤ 1 - exp (-t) := by
      have ha1 : t ≤ exp t - 1 := le_exp_sub_one
      have ha2 : (exp t - 1) * exp (-t) = 1 - exp (-t) := by
        rw [sub_mul, ← exp_add]
        simp
      nlinarith [exp_pos (-t)]
    nlinarith [key]
  calc exp (-(1 / 4) * t) * ((1 - cos ((r / 2) * t)) / (1 - exp (-t)))
      = exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) * (1 / (1 - exp (-t))) := by ring
    _ ≤ exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) * (1 / t + 1) := by
        gcongr
    _ = _ := by ring

lemma lowerFn_bound (r : ℝ) {t : ℝ} (ht : 0 < t) :
    ‖lowerFn r t‖ ≤ |r / 2| * exp (-(1 / 4) * t) := by
  unfold lowerFn
  have h2 := one_sub_cos_nonneg ((r / 2) * t)
  have hcos := one_sub_cos_le_abs ((r / 2) * t)
  rw [norm_eq_abs, abs_of_nonneg (by positivity)]
  have h3 : (1 - cos ((r / 2) * t)) / t ≤ |r / 2| := by
    rw [div_le_iff₀ ht]
    calc 1 - cos ((r / 2) * t) ≤ |(r / 2) * t| := hcos
      _ = |r / 2| * t := by rw [abs_mul, abs_of_pos ht]
  calc exp (-(1 / 4) * t) * ((1 - cos ((r / 2) * t)) / t)
      ≤ exp (-(1 / 4) * t) * |r / 2| :=
        mul_le_mul_of_nonneg_left h3 (le_of_lt (exp_pos _))
    _ = |r / 2| * exp (-(1 / 4) * t) := by ring

lemma lowerFn_integrable (r : ℝ) : IntegrableOn (lowerFn r) (Ioi (0 : ℝ)) := by
  refine (((exp_neg_integrableOn_Ioi 0 (by norm_num : (0:ℝ) < 1/4)).const_mul
    |r / 2|)).mono' ?_ ?_
  · unfold lowerFn
    apply ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioi
    apply ContinuousOn.mul (Continuous.continuousOn (by fun_prop))
    apply ContinuousOn.div (Continuous.continuousOn (by fun_prop)) continuousOn_id
    intro t ht
    exact ne_of_gt ht
  · rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with t ht
    exact lowerFn_bound r ht

lemma extra_integrable (r : ℝ) :
    IntegrableOn (fun t => exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t))) (Ioi (0 : ℝ)) := by
  refine (((exp_neg_integrableOn_Ioi 0 (by norm_num : (0:ℝ) < 1/4)).const_mul
    2)).mono' ?_ ?_
  · fun_prop
  · filter_upwards with t
    rw [norm_eq_abs]
    have h2 := one_sub_cos_nonneg ((r / 2) * t)
    have h3 : 1 - cos ((r / 2) * t) ≤ 2 := by
      have := neg_one_le_cos ((r / 2) * t); linarith
    rw [abs_of_nonneg (by positivity)]
    calc exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) ≤ exp (-(1 / 4) * t) * 2 :=
          mul_le_mul_of_nonneg_left h3 (le_of_lt (exp_pos _))
      _ = 2 * exp (-(1 / 4 : ℝ) * t) := by ring

lemma archKernel_integrable (r : ℝ) : IntegrableOn (archKernel r) (Ioi (0 : ℝ)) := by
  refine ((lowerFn_integrable r).add (extra_integrable r)).mono' ?_ ?_
  · unfold archKernel
    apply ContinuousOn.aestronglyMeasurable ?_ measurableSet_Ioi
    apply ContinuousOn.mul (Continuous.continuousOn (by fun_prop))
    apply ContinuousOn.div (Continuous.continuousOn (by fun_prop))
      (Continuous.continuousOn (by fun_prop))
    intro t ht
    exact ne_of_gt (one_sub_exp_neg_pos ht)
  · rw [ae_restrict_iff' measurableSet_Ioi]
    filter_upwards with t ht
    rw [norm_eq_abs, abs_of_nonneg (archKernel_nonneg r ht), Pi.add_apply]
    exact archKernel_le r ht

/-- The Frullani value at the kernel's parameters. -/
lemma frullani_kernel (r : ℝ) :
    ∫ t in Ioi (0 : ℝ), lowerFn r t = (1 / 2) * log (1 + 4 * r ^ 2) := by
  have habs : ∀ t, lowerFn r t = exp (-(1/4) * t) * ((1 - cos (|r / 2| * t)) / t) := by
    intro t
    unfold lowerFn
    rcases abs_choice (r / 2) with h | h
    · rw [h]
    · rw [h]
      simp only [neg_mul, Real.cos_neg]
  have hval : (1 : ℝ) + |r / 2| ^ 2 / (1/4 : ℝ) ^ 2 = 1 + 4 * r ^ 2 := by
    rw [sq_abs, show ((1/4 : ℝ)) ^ 2 = 1/16 from by norm_num, div_div_eq_mul_div]
    ring
  calc ∫ t in Ioi (0 : ℝ), lowerFn r t
      = ∫ t in Ioi (0 : ℝ), exp (-(1/4) * t) * ((1 - cos (|r / 2| * t)) / t) := by
        apply setIntegral_congr_fun measurableSet_Ioi
        intro t _
        exact habs t
    _ = (1 / 2) * log (1 + |r / 2| ^ 2 / (1/4 : ℝ) ^ 2) :=
        frullani_cos (by norm_num : (0:ℝ) < 1/4) (abs_nonneg _)
    _ = (1 / 2) * log (1 + 4 * r ^ 2) := by rw [hval]

lemma integral_exp_quarter : ∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) = 4 := by
  have hderiv : ∀ t ∈ Ioi (0 : ℝ),
      HasDerivAt (fun u : ℝ => -4 * exp (-(1 / 4) * u)) (exp (-(1 / 4) * t)) t := by
    intro t _
    have hlin : HasDerivAt (fun u : ℝ => -(1/4 : ℝ) * u) (-(1/4)) t := by
      simpa using (hasDerivAt_id t).const_mul (-(1/4 : ℝ))
    have h2 := (hlin.exp).const_mul (-4 : ℝ)
    have hval : (-4 : ℝ) * (exp (-(1/4 : ℝ) * t) * -(1/4)) = exp (-(1/4) * t) := by
      ring
    exact hval ▸ h2
  have hcont : ContinuousWithinAt (fun u : ℝ => -4 * exp (-(1 / 4) * u)) (Ici (0 : ℝ)) 0 := by
    apply Continuous.continuousWithinAt; fun_prop
  have hint : IntegrableOn (fun t : ℝ => exp (-(1 / 4) * t)) (Ioi (0 : ℝ)) :=
    exp_neg_integrableOn_Ioi 0 (by norm_num)
  have hlim : Tendsto (fun u : ℝ => -4 * exp (-(1 / 4) * u)) atTop (𝓝 0) := by
    have hexp0 : Tendsto (fun t : ℝ => exp (-(1/4 : ℝ) * t)) atTop (𝓝 0) := by
      have hcomp : Tendsto (fun t : ℝ => (1/4 : ℝ) * t) atTop atTop :=
        Tendsto.const_mul_atTop (by norm_num) tendsto_id
      exact (tendsto_exp_neg_atTop_nhds_zero.comp hcomp).congr
        (fun t => by simp [Function.comp_apply, neg_mul])
    have h3 := hexp0.const_mul (-4 : ℝ)
    simpa using h3
  have key := integral_Ioi_of_hasDerivAt_of_tendsto hcont hderiv hint hlim
  rw [key]
  simp

/-- **Lower half of the sandwich** (Lemma A(ii) of THEOREMS.md). -/
theorem kernel_lower (r : ℝ) :
    (1 / 2) * log (1 + 4 * r ^ 2) ≤ ∫ t in Ioi (0 : ℝ), archKernel r t := by
  rw [← frullani_kernel r]
  apply setIntegral_mono_on (lowerFn_integrable r) (archKernel_integrable r) measurableSet_Ioi
  intro t ht
  exact lowerFn_le_archKernel r ht

/-- **Upper half of the sandwich** (Lemma A(iv) of THEOREMS.md). -/
theorem kernel_upper (r : ℝ) :
    ∫ t in Ioi (0 : ℝ), archKernel r t ≤ (1 / 2) * log (1 + 4 * r ^ 2) + 8 := by
  have step1 : (∫ t in Ioi (0 : ℝ), archKernel r t)
      ≤ ∫ t in Ioi (0 : ℝ),
          (lowerFn r t + exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t))) := by
    apply setIntegral_mono_on (archKernel_integrable r)
      ((lowerFn_integrable r).add (extra_integrable r)) measurableSet_Ioi
    intro t ht
    exact archKernel_le r ht
  have step2 : (∫ t in Ioi (0 : ℝ),
        (lowerFn r t + exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t))))
      = (∫ t in Ioi (0 : ℝ), lowerFn r t)
        + ∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) :=
    integral_add (lowerFn_integrable r) (extra_integrable r)
  have step3 : (∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t))) ≤ 8 := by
    calc (∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)))
        ≤ ∫ t in Ioi (0 : ℝ), 2 * exp (-(1 / 4) * t) := by
          apply setIntegral_mono_on (extra_integrable r)
            ((exp_neg_integrableOn_Ioi 0 (by norm_num : (0:ℝ) < 1/4)).const_mul 2)
            measurableSet_Ioi
          intro t _
          have h3 : 1 - cos ((r / 2) * t) ≤ 2 := by
            have := neg_one_le_cos ((r / 2) * t); linarith
          calc exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) ≤ exp (-(1 / 4) * t) * 2 :=
                mul_le_mul_of_nonneg_left h3 (le_of_lt (exp_pos _))
            _ = 2 * exp (-(1 / 4) * t) := by ring
      _ = 2 * ∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) := integral_const_mul 2 _
      _ = 8 := by rw [integral_exp_quarter]; norm_num
  calc (∫ t in Ioi (0 : ℝ), archKernel r t)
      ≤ (∫ t in Ioi (0 : ℝ), lowerFn r t)
        + ∫ t in Ioi (0 : ℝ), exp (-(1 / 4) * t) * (1 - cos ((r / 2) * t)) := by
        rw [← step2]; exact step1
    _ ≤ (1 / 2) * log (1 + 4 * r ^ 2) + 8 := by
        rw [frullani_kernel r]
        linarith [step3]


end GlideKernel
