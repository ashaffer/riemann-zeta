/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ActivationCancellation
import RHBridge.GuinandWeilLiterature
import RHBridge.LogarithmicWeight
import Mathlib.Analysis.Distribution.SchwartzSpace.Fourier

/-!
# Positivity on the certified base interval

The fixed-window certificate at `a = 7 / 16` propagates down to every nested
support without loss in its quantitative constant: zero extension is an
isometry and the not-yet-active prime terms have disjoint support.  This file
also puts globally smooth compact-support representatives in the logarithmic
form domain and records the corresponding local zero-sum consequence of the
classical Guinand--Weil formula.

The support propagation uses the exact activation-cancellation theorem.  Its
standard autocorrelation inputs remain visible through `#print axioms`.
-/

namespace RHP2Bridge.CertifiedBaseInterval

open scoped ENNReal InnerProductSpace RealInnerProductSpace Topology

noncomputable section

open GeneralZetaWeilForm GuinandWeilFormula

/-- The lower-bound constant supplied by the certified `7 / 16` window. -/
def certifiedLowerBound : ℝ := 22699 / 10 ^ 9

theorem certifiedLowerBound_pos : 0 < certifiedLowerBound := by
  norm_num [certifiedLowerBound]

/-- The endpoint certificate propagates to every smaller support with exactly
the same quantitative constant. -/
theorem logarithmicWeilForm_strict_lower_bound
    {a : ℝ} (_ha0 : 0 ≤ a) (ha : a ≤ 7 / 16)
    (f : LogarithmicFormDomain a) (hf : f.val ≠ 0) :
    certifiedLowerBound * ‖f.val‖ ^ 2 < logarithmicWeilForm a f := by
  let F : TestSpace (7 / 16) :=
    NestedSupport.nestedSupport a (7 / 16) f.val
  have hFlog : InLogarithmicDomain (7 / 16) F :=
    (NestedSupport.inLogarithmicDomain_nestedSupport_iff ha f.val).2 f.property
  have hFne : F ≠ 0 := by
    intro hzero
    apply hf
    have hnorm : ‖F‖ = ‖f.val‖ := by
      simpa only [F] using NestedSupport.norm_nestedSupport ha f.val
    rw [hzero, norm_zero] at hnorm
    exact norm_eq_zero.mp hnorm.symm
  have hcert :=
    GeneralZetaWeilForm.weilForm_seven_sixteenths_strict_lower_bound
      F hFne hFlog
  have hform : weilForm (7 / 16) F = logarithmicWeilForm a f := by
    simpa only [F] using
      ActivationCancellation.weilForm_nestedSupport_eq ha f
  have hnorm : ‖F‖ = ‖f.val‖ := by
    simpa only [F] using NestedSupport.norm_nestedSupport ha f.val
  rw [hform, hnorm] at hcert
  simpa only [certifiedLowerBound] using hcert

private theorem weilForm_zero (a : ℝ) :
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
        (0 : TestSpace a) : ℝ → ℂ) =ᵐ[MeasureTheory.volume]
          fun _ : ℝ ↦ (0 : ℂ) := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_zero ℂ 2 MeasureTheory.volume
  have harch : archimedeanTerm a (0 : TestSpace a) = 0 := by
    unfold archimedeanTerm
    calc
      (∫ xi, (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
          Real.log Real.pi) * fourierEnergy a (0 : TestSpace a) xi) =
        ∫ _xi : ℝ, (0 : ℝ) := by
          apply MeasureTheory.integral_congr_ae
          filter_upwards [hcoe] with xi hxi
          simp [fourierEnergy, hxi]
      _ = 0 := by simp
  have hauto (u : ℝ) :
      AutocorrelationPlancherel.intervalAutocorrelation a u
        (0 : TestSpace a) = 0 := by
    unfold AutocorrelationPlancherel.intervalAutocorrelation
      AutocorrelationPlancherel.autocorrelation
    rw [AutocorrelationPlancherel.toFullLineL2_zeroExtensionFn_eq,
      hzeroExtension]
    simp
  simp [weilForm, poleTerm, harch, primeTerm, primePowerTerm, hauto]

/-- Positivity of the Weil form on every logarithmic-domain test supported in
`[-a,a]`, for `0 ≤ a ≤ 7/16`. -/
theorem positiveAt {a : ℝ} (ha0 : 0 ≤ a) (ha : a ≤ 7 / 16) :
    UniformPropagationToRH.PositiveAt a := by
  intro f
  by_cases hf : f.val = 0
  · have hzero : f = 0 := Subtype.ext hf
    subst f
    change 0 ≤ weilForm a (0 : TestSpace a)
    rw [weilForm_zero]
  · exact (logarithmicWeilForm_strict_lower_bound ha0 ha f hf).le.trans' <|
      mul_nonneg certifiedLowerBound_pos.le (sq_nonneg ‖f.val‖)

namespace SmoothCompactSupportData

/-- The canonical Schwartz representative of globally smooth compact-support
data, before passage to the interval `L²` quotient. -/
def toSchwartzMap {a : ℝ} (phi : SmoothCompactSupportData a) :
    SchwartzMap ℝ ℂ :=
  phi.hasCompactSupport_ofReal.toSchwartzMap
    (Complex.ofRealCLM.contDiff.comp phi.smooth)

@[simp] theorem toSchwartzMap_apply {a : ℝ}
    (phi : SmoothCompactSupportData a) (x : ℝ) :
    toSchwartzMap phi x = (phi x : ℂ) := rfl

/-- The selected interval quotient representative, extended by zero, agrees
almost everywhere with the original globally smooth function. -/
theorem zeroExtensionFn_ae_eq {a : ℝ}
    (phi : SmoothCompactSupportData a) :
    IntervalZeroExtension.zeroExtensionFn a phi.toTestSpace =ᵐ[
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
        fun x : ℝ ↦ (phi x : ℂ) := by
  let s : Set ℝ := LegendreScaledL2.Interval a
  have hs : MeasurableSet s := measurableSet_Icc
  apply MeasureTheory.ae_of_ae_restrict_of_ae_restrict_compl s
  · rw [ae_restrict_iff_subtype hs]
    filter_upwards [phi.coe_toTestSpace_ae] with x hx
    rw [IntervalZeroExtension.zeroExtensionFn_coe, hx]
  · apply (MeasureTheory.ae_restrict_iff' hs.compl).2
    filter_upwards [] with x hx
    have hx' : x ∉ LegendreScaledL2.Interval a := hx
    rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem
      a phi.toTestSpace hx']
    by_contra hne
    have hmem : x ∈ Function.support phi.toFun := by
      intro hzero
      apply hne
      simp [hzero]
    exact hx' (phi.support_subset hmem)

/-- The pointwise Fourier transform used by the interval form agrees with the
Fourier transform of the canonical Schwartz representative. -/
theorem fourier_zeroExtensionFn_eq {a : ℝ}
    (phi : SmoothCompactSupportData a) (xi : ℝ) :
    FourierTransform.fourier
        (IntervalZeroExtension.zeroExtensionFn a phi.toTestSpace) xi =
      FourierTransform.fourier (toSchwartzMap phi) xi := by
  exact Real.fourier_congr_ae (zeroExtensionFn_ae_eq phi) xi

end SmoothCompactSupportData

end

end RHP2Bridge.CertifiedBaseInterval
