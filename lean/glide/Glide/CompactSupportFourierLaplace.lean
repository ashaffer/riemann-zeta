/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.Analytic.Order
import Mathlib.Analysis.Calculus.ParametricIntegral
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic

/-!
# Fourier–Laplace transforms of functions on a compact interval

This file collects two standard facts about the Fourier–Laplace transform

`transform φ a z = ∫ x in [-a, a], φ x * exp (-i * z * x)`:

* `differentiable_transform`: an integrable function on `[-a, a]` has an entire
  Fourier–Laplace transform;
* `integrableOn_of_integrableOn_norm_sq`: on the finite interval, strong
  measurability and integrability of the squared norm imply `L¹` integrability;
* `norm_transform_le_sqrt_integral_sq_mul_exp`: those intrinsic `L²`
  hypotheses give the usual exponential-type bound.

The normalized bound and its real-translation form are supplied as convenient
corollaries.  The final theorem records the elementary invariance of analytic
order under translation.
-/

open Real MeasureTheory Set

namespace CompactSupportFourierLaplace

/-- The Fourier–Laplace transform of `φ`, integrated over the symmetric interval
`[-a, a]`. -/
noncomputable def transform (φ : ℝ → ℂ) (a : ℝ) (z : ℂ) : ℂ :=
  ∫ x in Icc (-a) a, φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))

lemma exponent_re (z : ℂ) (x : ℝ) : (-(Complex.I * z * (x : ℂ))).re = x * z.im := by
  simp only [Complex.neg_re, Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im,
    Complex.ofReal_re, Complex.ofReal_im]
  ring

lemma norm_integrand (φ : ℝ → ℂ) (z : ℂ) (x : ℝ) :
    ‖φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))‖ = ‖φ x‖ * Real.exp (x * z.im) := by
  rw [norm_mul, Complex.norm_exp, exponent_re]

lemma integrableOn_integrand {φ : ℝ → ℂ} {a : ℝ}
    (hφi : IntegrableOn φ (Icc (-a) a)) (z : ℂ) :
    IntegrableOn (fun x => φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))) (Icc (-a) a) := by
  apply Integrable.mono' (hφi.norm.mul_const (Real.exp (a * |z.im|)))
  · exact hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · rw [ae_restrict_iff' measurableSet_Icc]
    filter_upwards with x hx
    rw [norm_integrand]
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have hxz : x * z.im ≤ a * |z.im| := by
      calc x * z.im ≤ |x * z.im| := le_abs_self _
        _ = |x| * |z.im| := abs_mul _ _
        _ ≤ a * |z.im| := mul_le_mul_of_nonneg_right hxa (abs_nonneg _)
    exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hxz) (norm_nonneg _)

/-- On a finite interval, a strongly measurable function with integrable
squared norm is integrable.  This is the concrete `L² ⊆ L¹` bridge used by
the Fourier–Laplace estimates below. -/
theorem integrableOn_of_integrableOn_norm_sq {φ : ℝ → ℂ} {a : ℝ}
    (hφm : AEStronglyMeasurable φ (volume.restrict (Icc (-a) a)))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a)) :
    IntegrableOn φ (Icc (-a) a) := by
  have hφLp : MemLp φ 2 (volume.restrict (Icc (-a) a)) :=
    (memLp_two_iff_integrable_sq_norm hφm).2 hsq
  exact hφLp.integrable (by norm_num)

/-- The Fourier–Laplace transform of an integrable function on `[-a, a]` is entire. -/
theorem differentiable_transform {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a)) :
    Differentiable ℂ (transform φ a) := by
  intro z₀
  have key := hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (μ := volume.restrict (Icc (-a) a))
    (F := fun (z : ℂ) (x : ℝ) => φ x * Complex.exp (-(Complex.I * z * (x : ℂ))))
    (F' := fun (z : ℂ) (x : ℝ) =>
      φ x * (Complex.exp (-(Complex.I * z * (x : ℂ))) * -(Complex.I * (x : ℂ))))
    (bound := fun x => ‖φ x‖ * (Real.exp (a * (|z₀.im| + 1)) * a))
    (Metric.ball_mem_nhds z₀ one_pos) ?_ ?_ ?_ ?_ ?_ ?_
  · exact key.2.differentiableAt
  · exact Filter.Eventually.of_forall fun z =>
      hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · exact integrableOn_integrand hφi z₀
  · exact hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · rw [ae_restrict_iff' measurableSet_Icc]
    filter_upwards with x hx
    intro z hz
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have him : |z.im| ≤ |z₀.im| + 1 := by
      have h2 : |(z - z₀).im| ≤ ‖z - z₀‖ := Complex.abs_im_le_norm _
      have h3 : ‖z - z₀‖ ≤ 1 := by
        rw [← dist_eq_norm]
        exact le_of_lt (Metric.mem_ball.mp hz)
      have h4 : z.im = z₀.im + (z - z₀).im := by simp
      rw [h4]
      calc |z₀.im + (z - z₀).im| ≤ |z₀.im| + |(z - z₀).im| := abs_add_le _ _
        _ ≤ |z₀.im| + 1 := by linarith
    have hxz : x * z.im ≤ a * (|z₀.im| + 1) := by
      calc x * z.im ≤ |x * z.im| := le_abs_self _
        _ = |x| * |z.im| := abs_mul _ _
        _ ≤ a * (|z₀.im| + 1) := mul_le_mul hxa him (abs_nonneg _) ha.le
    calc ‖φ x * (Complex.exp (-(Complex.I * z * (x : ℂ))) * -(Complex.I * (x : ℂ)))‖
        = ‖φ x‖ * (Real.exp (x * z.im) * |x|) := by
          rw [norm_mul, norm_mul, Complex.norm_exp, exponent_re, norm_neg, norm_mul,
            Complex.norm_I, one_mul, Complex.norm_real, Real.norm_eq_abs]
      _ ≤ ‖φ x‖ * (Real.exp (a * (|z₀.im| + 1)) * a) := by
          apply mul_le_mul_of_nonneg_left ?_ (norm_nonneg _)
          exact mul_le_mul (Real.exp_le_exp.mpr hxz) hxa (abs_nonneg _) (Real.exp_pos _).le
  · exact hφi.norm.mul_const _
  · apply Filter.Eventually.of_forall
    intro x z _
    have h1 : HasDerivAt (fun w : ℂ => Complex.I * w) Complex.I z := by
      simpa using (hasDerivAt_id z).const_mul Complex.I
    have h2 : HasDerivAt (fun w : ℂ => Complex.I * w * (x : ℂ)) (Complex.I * (x : ℂ)) z :=
      h1.mul_const _
    exact ((h2.neg).cexp).const_mul (φ x)

/-- The Fourier–Laplace transform is entire directly from the intrinsic `L²`
hypotheses on the finite interval. -/
theorem differentiable_transform_of_integrableOn_norm_sq {φ : ℝ → ℂ} {a : ℝ}
    (ha : 0 < a)
    (hφm : AEStronglyMeasurable φ (volume.restrict (Icc (-a) a)))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a)) :
    Differentiable ℂ (transform φ a) :=
  differentiable_transform ha (integrableOn_of_integrableOn_norm_sq hφm hsq)

/-- `L²` exponential-type bound for the Fourier–Laplace transform on `[-a, a]`.

The first factor on the right is the `L²` norm, written directly as a square root so the
statement does not require constructing an `L²` element. -/
theorem norm_transform_le_sqrt_integral_sq_mul_exp {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφm : AEStronglyMeasurable φ (volume.restrict (Icc (-a) a)))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a)) (z : ℂ) :
    ‖transform φ a z‖ ≤ Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) *
      (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) := by
  have hg2 : IntegrableOn (fun x : ℝ => Real.exp (x * z.im) ^ 2) (Icc (-a) a) :=
    ((by fun_prop : Continuous fun x : ℝ => Real.exp (x * z.im) ^ 2).continuousOn).integrableOn_Icc
  have h1 : ‖transform φ a z‖ ≤ ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := by
    calc ‖transform φ a z‖
        ≤ ∫ x in Icc (-a) a, ‖φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))‖ :=
          norm_integral_le_integral_norm _
      _ = ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := by
          apply setIntegral_congr_fun measurableSet_Icc
          intro x _
          exact norm_integrand φ z x
  have hfLp : MemLp (fun x => ‖φ x‖) (ENNReal.ofReal 2) (volume.restrict (Icc (-a) a)) := by
    rw [ENNReal.ofReal_ofNat]
    exact (memLp_two_iff_integrable_sq hφm.norm).mpr hsq
  have hgLp : MemLp (fun x : ℝ => Real.exp (x * z.im)) (ENNReal.ofReal 2)
      (volume.restrict (Icc (-a) a)) := by
    rw [ENNReal.ofReal_ofNat]
    exact (memLp_two_iff_integrable_sq
      (Continuous.aestronglyMeasurable (by fun_prop))).mpr hg2
  have hCS := integral_mul_le_Lp_mul_Lq_of_nonneg Real.HolderConjugate.two_two
    (Filter.Eventually.of_forall fun x => norm_nonneg (φ x))
    (Filter.Eventually.of_forall fun x => (Real.exp_pos (x * z.im)).le) hfLp hgLp
  have hpt : ∀ x ∈ Icc (-a) a, Real.exp (x * z.im) ^ 2 ≤ Real.exp (2 * a * |z.im|) := by
    intro x hx
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have h2 : Real.exp (x * z.im) ^ 2 = Real.exp (2 * (x * z.im)) := by
      rw [sq, ← Real.exp_add]
      ring_nf
    rw [h2]
    apply Real.exp_le_exp.mpr
    calc 2 * (x * z.im) ≤ 2 * |x * z.im| := by linarith [le_abs_self (x * z.im)]
      _ = 2 * (|x| * |z.im|) := by rw [abs_mul]
      _ ≤ 2 * (a * |z.im|) := by
          have := mul_le_mul_of_nonneg_right hxa (abs_nonneg z.im)
          linarith
      _ = 2 * a * |z.im| := by ring
  have hgbd : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
      ≤ 2 * a * Real.exp (2 * a * |z.im|) := by
    calc (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
        ≤ ∫ _x in Icc (-a) a, Real.exp (2 * a * |z.im|) :=
          setIntegral_mono_on hg2 (integrableOn_const measure_Icc_lt_top.ne)
            measurableSet_Icc hpt
      _ = 2 * a * Real.exp (2 * a * |z.im|) := by
          rw [setIntegral_const, smul_eq_mul, Measure.real, Real.volume_Icc,
            ENNReal.toReal_ofReal (by linarith : (0 : ℝ) ≤ a - -a)]
          ring
  have hg_fac : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ))
      ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
    have hconv : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ))
        = ∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2 :=
      setIntegral_congr_fun measurableSet_Icc fun x _ => Real.rpow_two _
    rw [hconv, ← Real.sqrt_eq_rpow]
    calc Real.sqrt (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
        ≤ Real.sqrt (2 * a * Real.exp (2 * a * |z.im|)) := Real.sqrt_le_sqrt hgbd
      _ = Real.sqrt (2 * a) * Real.sqrt (Real.exp (2 * a * |z.im|)) :=
          Real.sqrt_mul (by positivity) _
      _ = Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
          congr 1
          have h : Real.exp (2 * a * |z.im|) = Real.exp (a * |z.im|) ^ 2 := by
            rw [sq, ← Real.exp_add]
            congr 1
            ring
          rw [h, Real.sqrt_sq (Real.exp_pos _).le]
  have hf_conv : (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) =
      Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) := by
    have hconv : (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) =
        ∫ x in Icc (-a) a, ‖φ x‖ ^ 2 :=
      setIntegral_congr_fun measurableSet_Icc fun x _ => Real.rpow_two _
    rw [hconv, Real.sqrt_eq_rpow]
  have hf_nonneg : 0 ≤ Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) := Real.sqrt_nonneg _
  calc ‖transform φ a z‖ ≤ ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := h1
    _ ≤ (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) *
        (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) := hCS
    _ = Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) *
        (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) := by
          rw [hf_conv]
    _ ≤ Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) *
        (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :=
          mul_le_mul_of_nonneg_left hg_fac hf_nonneg

/-- Normalized form of the `L²` exponential-type bound. -/
theorem norm_transform_le_exp_of_integral_sq_le_one {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφm : AEStronglyMeasurable φ (volume.restrict (Icc (-a) a)))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1) (z : ℂ) :
    ‖transform φ a z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
  have h := norm_transform_le_sqrt_integral_sq_mul_exp ha hφm hsq z
  have hsqrt : Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1 := by
    calc Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ Real.sqrt 1 :=
          Real.sqrt_le_sqrt hφ2
      _ = 1 := Real.sqrt_one
  have hnonneg : 0 ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by positivity
  calc ‖transform φ a z‖ ≤ Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) *
        (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) := h
    _ ≤ 1 * (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :=
      mul_le_mul_of_nonneg_right hsqrt hnonneg
    _ = Real.sqrt (2 * a) * Real.exp (a * |z.im|) := one_mul _

/-- Real translation does not change the imaginary part in the exponential-type bound. -/
theorem norm_transform_translate_le_exp_of_integral_sq_le_one {φ : ℝ → ℂ} {a : ℝ}
    (ha : 0 < a)
    (hφm : AEStronglyMeasurable φ (volume.restrict (Icc (-a) a)))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1) (x₀ : ℝ) (z : ℂ) :
    ‖transform φ a ((x₀ : ℂ) + z)‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
  simpa using norm_transform_le_exp_of_integral_sq_le_one ha hφm hsq hφ2 ((x₀ : ℂ) + z)

/-- Translation preserves the analytic order of an entire function. -/
theorem analyticOrderAt_translate (F : ℂ → ℂ) (hF : Differentiable ℂ F) (c z₀ : ℂ) :
    analyticOrderAt (fun z => F (c + z)) z₀ = analyticOrderAt F (c + z₀) := by
  have hf : AnalyticAt ℂ F (c + z₀) := hF.analyticAt (c + z₀)
  have hg : AnalyticAt ℂ (fun z : ℂ => c + z) z₀ := by fun_prop
  have hderiv : deriv (fun z : ℂ => c + z) z₀ = 1 := by
    simpa only [id_eq] using ((hasDerivAt_id z₀).const_add c).deriv
  have hgderiv : deriv (fun z : ℂ => c + z) z₀ ≠ 0 := by
    rw [hderiv]
    exact one_ne_zero
  have horder : analyticOrderAt ((fun z : ℂ => c + z) · - (c + z₀)) z₀ = 1 :=
    hg.analyticOrderAt_sub_eq_one_of_deriv_ne_zero hgderiv
  rw [show (fun z => F (c + z)) = F ∘ (fun z => c + z) by rfl,
    hf.analyticOrderAt_comp hg, horder, mul_one]

end CompactSupportFourierLaplace
