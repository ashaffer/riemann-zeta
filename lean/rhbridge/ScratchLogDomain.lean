import RHBridge.GeneralZetaWeilForm

open scoped ENNReal InnerProductSpace RealInnerProductSpace ArithmeticFunction
open MeasureTheory

namespace RHP2Bridge.GeneralZetaWeilForm

noncomputable section

theorem test_inLogarithmicDomain_add {a : ℝ}
    (f g : LogarithmicFormDomain a) :
    InLogarithmicDomain a (f.val + g.val) := by
  let F := IntervalZeroExtension.fourierZeroExtensionL2 a f.val
  let G := IntervalZeroExtension.fourierZeroExtensionL2 a g.val
  have hfourier :
      IntervalZeroExtension.fourierZeroExtensionL2 a (f.val + g.val) =
        F + G := by
    dsimp [F, G]
    rw [IntervalZeroExtension.fourierZeroExtensionL2,
      IntervalZeroExtension.zeroExtension_add,
      FourierAdd.fourier_add]
    rfl
  have hcoe :
      (IntervalZeroExtension.fourierZeroExtensionL2 a
        (f.val + g.val) : ℝ → ℂ) =ᵐ[volume]
          fun xi ↦ (F : ℝ → ℂ) xi + (G : ℝ → ℂ) xi := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_add F G
  have hweight : AEStronglyMeasurable
      (fun xi : ℝ ↦ Real.log (1 + (2 * Real.pi * xi) ^ 2)) volume := by
    have harg : Continuous
        (fun xi : ℝ ↦ 1 + (2 * Real.pi * xi) ^ 2) := by fun_prop
    exact (harg.log (fun xi ↦ ne_of_gt (by
      nlinarith [sq_nonneg (2 * Real.pi * xi)]))).aestronglyMeasurable
  have henergy : AEStronglyMeasurable
      (fun xi : ℝ ↦ fourierEnergy a (f.val + g.val) xi) volume := by
    have hnorm := (MeasureTheory.Lp.aestronglyMeasurable
      (IntervalZeroExtension.fourierZeroExtensionL2 a
        (f.val + g.val))).norm
    unfold fourierEnergy
    convert hnorm.pow 2 using 1
    · rfl
    · ext xi
      rfl
  have htarget : AEStronglyMeasurable
      (fun xi : ℝ ↦ Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        fourierEnergy a (f.val + g.val) xi) volume :=
    hweight.mul henergy
  have hmajorant : Integrable
      (fun xi : ℝ ↦
        2 * (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
          fourierEnergy a f.val xi) +
        2 * (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
          fourierEnergy a g.val xi)) volume := by
    exact (f.property.const_mul 2).add (g.property.const_mul 2)
  apply hmajorant.mono' htarget
  filter_upwards [hcoe] with xi hxi
  have hw : 0 ≤ Real.log (1 + (2 * Real.pi * xi) ^ 2) :=
    Real.log_nonneg (by nlinarith [sq_nonneg (2 * Real.pi * xi)])
  have hadd := norm_add_le ((F : ℝ → ℂ) xi) ((G : ℝ → ℂ) xi)
  have hsquare :
      ‖(F : ℝ → ℂ) xi + (G : ℝ → ℂ) xi‖ ^ 2 ≤
        2 * (‖(F : ℝ → ℂ) xi‖ ^ 2 + ‖(G : ℝ → ℂ) xi‖ ^ 2) := by
    have hmul := mul_self_le_mul_self
      (norm_nonneg ((F : ℝ → ℂ) xi + (G : ℝ → ℂ) xi)) hadd
    nlinarith [sq_nonneg (‖(F : ℝ → ℂ) xi‖ - ‖(G : ℝ → ℂ) xi‖)]
  change
    |Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a
          (f.val + g.val) : ℝ → ℂ) xi‖ ^ 2| ≤
      2 * (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        ‖(F : ℝ → ℂ) xi‖ ^ 2) +
      2 * (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        ‖(G : ℝ → ℂ) xi‖ ^ 2)
  rw [hxi, abs_of_nonneg (mul_nonneg hw (sq_nonneg _))]
  nlinarith

theorem test_inLogarithmicDomain_smul {a c : ℝ}
    (f : LogarithmicFormDomain a) :
    InLogarithmicDomain a (c • f.val) := by
  let F := IntervalZeroExtension.fourierZeroExtensionL2 a f.val
  have hfourier :
      IntervalZeroExtension.fourierZeroExtensionL2 a (c • f.val) =
        c • F := by
    dsimp [F]
    unfold IntervalZeroExtension.fourierZeroExtensionL2
    rw [IntervalZeroExtension.zeroExtension_smul]
    rw [RCLike.real_smul_eq_coe_smul (K := ℂ) c
      (IntervalZeroExtension.zeroExtension a f.val),
      RCLike.real_smul_eq_coe_smul (K := ℂ) c
        (FourierTransform.fourier
          (IntervalZeroExtension.zeroExtension a f.val))]
    exact FourierSMul.fourier_smul (c : ℂ)
      (IntervalZeroExtension.zeroExtension a f.val)
  have hcoe :
      (IntervalZeroExtension.fourierZeroExtensionL2 a
        (c • f.val) : ℝ → ℂ) =ᵐ[volume]
          fun xi ↦ c • (F : ℝ → ℂ) xi := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_smul c F
  have hscale :
      (fun xi : ℝ ↦ Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        fourierEnergy a (c • f.val) xi) =ᵐ[volume]
      fun xi : ℝ ↦ c ^ 2 *
        (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
          fourierEnergy a f.val xi) := by
    filter_upwards [hcoe] with xi hxi
    change
      Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a
          (c • f.val) : ℝ → ℂ) xi‖ ^ 2 =
      c ^ 2 * (Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        ‖(F : ℝ → ℂ) xi‖ ^ 2)
    rw [hxi, norm_smul, Real.norm_eq_abs]
    rw [show (|c| * ‖(F : ℝ → ℂ) xi‖) ^ 2 =
      c ^ 2 * ‖(F : ℝ → ℂ) xi‖ ^ 2 by rw [mul_pow, sq_abs]]
    ring
  exact (f.property.const_mul (c ^ 2)).congr hscale.symm

theorem test_inLogarithmicDomain_zero (a : ℝ) :
    InLogarithmicDomain a (0 : TestSpace a) := by
  have hzeroExtension :
      IntervalZeroExtension.zeroExtension a (0 : TestSpace a) = 0 := by
    exact (IntervalZeroExtension.zeroExtensionLinearMap a).map_zero
  have hfourier :
      IntervalZeroExtension.fourierZeroExtensionL2 a (0 : TestSpace a) = 0 := by
    unfold IntervalZeroExtension.fourierZeroExtensionL2
    rw [hzeroExtension, FourierTransform.fourier_zero]
  have hcoe :
      (IntervalZeroExtension.fourierZeroExtensionL2 a
        (0 : TestSpace a) : ℝ → ℂ) =ᵐ[volume]
          fun _ : ℝ ↦ (0 : ℂ) := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_zero ℂ 2 volume
  have hintegrand :
      (fun xi : ℝ ↦ Real.log (1 + (2 * Real.pi * xi) ^ 2) *
        fourierEnergy a (0 : TestSpace a) xi) =ᵐ[volume] 0 := by
    filter_upwards [hcoe] with xi hxi
    simp [fourierEnergy, hxi]
  exact (integrable_zero ℝ ℝ volume).congr hintegrand.symm

def testLogarithmicFormSubmodule (a : ℝ) : Submodule ℝ (TestSpace a) where
  carrier := InLogarithmicDomain a
  zero_mem' := test_inLogarithmicDomain_zero a
  add_mem' := by
    intro f g hf hg
    exact test_inLogarithmicDomain_add ⟨f, hf⟩ ⟨g, hg⟩
  smul_mem' := by
    intro c f hf
    exact test_inLogarithmicDomain_smul (c := c) ⟨f, hf⟩

instance testLogarithmicFormDomainAdd (a : ℝ) :
    Add (LogarithmicFormDomain a) :=
  inferInstanceAs (Add (testLogarithmicFormSubmodule a))

instance testLogarithmicFormDomainAddCommGroup (a : ℝ) :
    AddCommGroup (LogarithmicFormDomain a) :=
  inferInstanceAs (AddCommGroup (testLogarithmicFormSubmodule a))

instance testLogarithmicFormDomainModule (a : ℝ) :
    Module ℝ (LogarithmicFormDomain a) :=
  inferInstanceAs (Module ℝ (testLogarithmicFormSubmodule a))

example {a : ℝ} (f g : LogarithmicFormDomain a) :
    (f + g).val = f.val + g.val := rfl

example {a : ℝ} (c : ℝ) (f : LogarithmicFormDomain a) :
    (c • f).val = c • f.val := rfl

theorem test_weilForm_zero (a : ℝ) :
    weilForm a (0 : TestSpace a) = 0 := by
  have hzeroExtension :
      IntervalZeroExtension.zeroExtension a (0 : TestSpace a) = 0 := by
    exact (IntervalZeroExtension.zeroExtensionLinearMap a).map_zero
  have hfourier :
      IntervalZeroExtension.fourierZeroExtensionL2 a (0 : TestSpace a) = 0 := by
    unfold IntervalZeroExtension.fourierZeroExtensionL2
    rw [hzeroExtension, FourierTransform.fourier_zero]
  have hcoe :
      (IntervalZeroExtension.fourierZeroExtensionL2 a
        (0 : TestSpace a) : ℝ → ℂ) =ᵐ[volume]
          fun _ : ℝ ↦ (0 : ℂ) := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_zero ℂ 2 volume
  have harch : archimedeanTerm a (0 : TestSpace a) = 0 := by
    unfold archimedeanTerm
    calc
      (∫ xi, (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
          Real.log Real.pi) * fourierEnergy a (0 : TestSpace a) xi) =
        ∫ _xi : ℝ, (0 : ℝ) := by
          apply integral_congr_ae
          filter_upwards [hcoe] with xi hxi
          simp [fourierEnergy, hxi]
      _ = 0 := integral_zero
  have hauto (u : ℝ) :
      AutocorrelationPlancherel.intervalAutocorrelation a u
        (0 : TestSpace a) = 0 := by
    unfold AutocorrelationPlancherel.intervalAutocorrelation
      AutocorrelationPlancherel.autocorrelation
    rw [AutocorrelationPlancherel.toFullLineL2_zeroExtensionFn_eq,
      hzeroExtension]
    simp
  simp [weilForm, poleTerm, harch, primeTerm, primePowerTerm, hauto]

end

end RHP2Bridge.GeneralZetaWeilForm
