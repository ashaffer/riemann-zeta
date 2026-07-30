/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedBoundedCertificateCheck

/-!
# Autocorrelation and Plancherel

This file proves the `L¹ ∩ L²` translation/Plancherel identity needed to
identify the prime Fourier multiplier with the time-domain autocorrelation.
-/

namespace RHP2Bridge.AutocorrelationPlancherel

open scoped ENNReal InnerProductSpace FourierTransform ComplexConjugate

noncomputable section

abbrev FullLineL2 := IntervalZeroExtension.FullLineComplexL2

/-- Canonical `L²` vector represented by a square-integrable function. -/
def toFullLineL2 (f : ℝ → ℂ)
    (hf : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) : FullLineL2 :=
  hf.toLp f

/-- For an `L¹ ∩ L²` function, Mathlib's unitary `L²` Fourier transform
agrees almost everywhere with its pointwise Fourier integral. -/
theorem coe_fourier_toFullLineL2_ae_eq_fourierFn
    (f : ℝ → ℂ)
    (hf1 : MeasureTheory.MemLp f 1
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hf2 : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      FourierTransform.fourier f := by
  apply ae_eq_of_integral_contDiff_smul_eq
  · exact (MeasureTheory.Lp.memLp
      (FourierTransform.fourier (toFullLineL2 f hf2))).locallyIntegrable
        (by norm_num)
  · have htop : MeasureTheory.MemLp (FourierTransform.fourier f) ∞
        (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
      rw [← Real.fourierTransform_toLp hf1]
      exact (Real.Lp.fourierTransform (hf1.toLp f)).memLp_top
    exact htop.locallyIntegrable le_top
  · intro g hg hsupp
    let gc : ℝ → ℂ := Complex.ofRealCLM ∘ g
    have hgcSupp : HasCompactSupport (Complex.ofRealCLM ∘ g) :=
      hsupp.comp_left rfl
    have hgcDiff : ContDiff ℝ ((⊤ : ℕ∞) : WithTop ℕ∞)
        (Complex.ofRealCLM ∘ g) := by
      exact (Complex.ofRealCLM.contDiff.of_le le_top).comp hg
    let phi : SchwartzMap ℝ ℂ := hgcSupp.toSchwartzMap hgcDiff
    have hdist := congrArg (fun T : SchwartzMap ℝ ℂ →L[ℂ] ℂ ↦ T phi)
      (MeasureTheory.Lp.fourier_toTemperedDistribution_eq
        (toFullLineL2 f hf2))
    have hdist' :
        (∫ x : ℝ, (FourierTransform.fourier phi) x •
            (toFullLineL2 f hf2 : ℝ → ℂ) x) =
          ∫ x : ℝ, phi x •
            (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) x := by
      change
        (MeasureTheory.Lp.toTemperedDistribution (toFullLineL2 f hf2))
            (FourierTransform.fourier phi) =
          (MeasureTheory.Lp.toTemperedDistribution
            (FourierTransform.fourier (toFullLineL2 f hf2))) phi at hdist
      rw [MeasureTheory.Lp.toTemperedDistribution_apply,
        MeasureTheory.Lp.toTemperedDistribution_apply] at hdist
      exact hdist
    have hdistFn :
        (∫ x : ℝ, (FourierTransform.fourier phi) x • f x) =
          ∫ x : ℝ, phi x •
            (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) x := by
      calc
        _ = ∫ x : ℝ, (FourierTransform.fourier phi) x •
              (toFullLineL2 f hf2 : ℝ → ℂ) x := by
          apply MeasureTheory.integral_congr_ae
          filter_upwards [hf2.coeFn_toLp] with x hx
          have hx' : (toFullLineL2 f hf2 : ℝ → ℂ) x = f x := by
            simpa [toFullLineL2] using hx
          rw [hx']
        _ = _ := hdist'
    have hfub := VectorFourier.integral_fourierIntegral_smul_eq_flip
      (e := Real.fourierChar) (L := innerₗ ℝ)
      (μ := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
      (ν := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
      Real.continuous_fourierChar continuous_inner
      (MeasureTheory.memLp_one_iff_integrable.mp hf1) phi.integrable
    have hinnerFlip : (innerₗ ℝ).flip = innerₗ ℝ := by
      apply LinearMap.ext
      intro x
      apply LinearMap.ext
      intro y
      exact real_inner_comm x y
    rw [hinnerFlip] at hfub
    change
      (∫ xi : ℝ, FourierTransform.fourier f xi • phi xi) =
        ∫ x : ℝ, f x • FourierTransform.fourier (phi : ℝ → ℂ) x at hfub
    have hfub' :
        (∫ x : ℝ, phi x • FourierTransform.fourier f x) =
          ∫ x : ℝ, (FourierTransform.fourier phi) x • f x := by
      simpa only [SchwartzMap.fourier_coe, smul_eq_mul, mul_comm] using hfub
    calc
      (∫ x : ℝ, g x •
          (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) x) =
          ∫ x : ℝ, phi x •
            (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) x := by
        apply MeasureTheory.integral_congr_ae
        filter_upwards [] with x
        rfl
      _ = ∫ x : ℝ, phi x • FourierTransform.fourier f x := by
        exact hdistFn.symm.trans hfub'.symm
      _ = ∫ x : ℝ, g x • FourierTransform.fourier f x := by
        apply MeasureTheory.integral_congr_ae
        filter_upwards [] with x
        rfl

/-- Right translation `x ↦ f (x+u)`. -/
def translateFn (u : ℝ) (f : ℝ → ℂ) : ℝ → ℂ :=
  f ∘ fun x ↦ x + u

theorem translateFn_memLp {p : ℝ≥0∞} (u : ℝ) (f : ℝ → ℂ)
    (hf : MeasureTheory.MemLp f p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    MeasureTheory.MemLp (translateFn u f) p
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  exact hf.comp_measurePreserving
    (MeasureTheory.measurePreserving_add_right
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) u)

/-- The right translate as an `L²` vector. -/
def translateL2 (u : ℝ) (f : ℝ → ℂ)
    (hf : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) : FullLineL2 :=
  toFullLineL2 (translateFn u f) (translateFn_memLp u f hf)

/-- Fourier translation law for the unitary `L²` transform, with Mathlib's
ordinary-frequency phase. -/
theorem coe_fourier_translateL2
    (u : ℝ) (f : ℝ → ℂ)
    (hf1 : MeasureTheory.MemLp f 1
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hf2 : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    (FourierTransform.fourier (translateL2 u f hf2) : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      fun xi ↦ Real.fourierChar (u * xi) •
        (FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) xi := by
  have htranslated := coe_fourier_toFullLineL2_ae_eq_fourierFn
    (translateFn u f) (translateFn_memLp u f hf1)
      (translateFn_memLp u f hf2)
  have horiginal := coe_fourier_toFullLineL2_ae_eq_fourierFn f hf1 hf2
  have hphase : FourierTransform.fourier (translateFn u f) =
      fun xi ↦ Real.fourierChar (xi * u) • FourierTransform.fourier f xi := by
    change VectorFourier.fourierIntegral Real.fourierChar
        (MeasureTheory.volume : MeasureTheory.Measure ℝ) (innerₗ ℝ)
          (translateFn u f) =
      fun xi ↦ Real.fourierChar (xi * u) •
        VectorFourier.fourierIntegral Real.fourierChar
          (MeasureTheory.volume : MeasureTheory.Measure ℝ) (innerₗ ℝ) f xi
    simpa [translateFn] using
      (VectorFourier.fourierIntegral_comp_add_right Real.fourierChar
        (MeasureTheory.volume : MeasureTheory.Measure ℝ) (innerₗ ℝ) f u)
  filter_upwards [htranslated, horiginal] with xi ht ho
  have ht' :
      (FourierTransform.fourier (translateL2 u f hf2) : ℝ → ℂ) xi =
        FourierTransform.fourier (translateFn u f) xi := by
    simpa [translateL2] using ht
  rw [ht', hphase, ho]
  rw [mul_comm]

/-- Time-domain autocorrelation of an `L²` function with its right
translate. -/
def autocorrelation (u : ℝ) (f : ℝ → ℂ)
    (hf2 : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) : ℝ :=
  RCLike.re ⟪toFullLineL2 f hf2, translateL2 u f hf2⟫_ℂ

/-- The `L²` definition is the usual time-domain autocorrelation integral. -/
theorem autocorrelation_eq_integral
    (u : ℝ) (f : ℝ → ℂ)
    (hf2 : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    autocorrelation u f hf2 =
      ∫ x, RCLike.re ⟪f x, f (x + u)⟫_ℂ := by
  unfold autocorrelation
  rw [MeasureTheory.L2.inner_def, ←
    integral_re (MeasureTheory.L2.integrable_inner
      (toFullLineL2 f hf2) (translateL2 u f hf2))]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [hf2.coeFn_toLp,
    (translateFn_memLp u f hf2).coeFn_toLp] with x hx htx
  have hx' : (toFullLineL2 f hf2 : ℝ → ℂ) x = f x := by
    simpa [toFullLineL2] using hx
  have htx' : (translateL2 u f hf2 : ℝ → ℂ) x = f (x + u) := by
    simpa [translateL2, toFullLineL2, translateFn] using htx
  rw [hx', htx']

/-- Plancherel identifies time-domain autocorrelation with the cosine-weighted
Fourier energy. -/
theorem autocorrelation_eq_cos_fourier_energy
    (u : ℝ) (f : ℝ → ℂ)
    (hf1 : MeasureTheory.MemLp f 1
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hf2 : MeasureTheory.MemLp f 2
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    autocorrelation u f hf2 =
      ∫ xi, Real.cos (2 * Real.pi * u * xi) *
        ‖(FourierTransform.fourier (toFullLineL2 f hf2) : ℝ → ℂ) xi‖ ^ 2 := by
  unfold autocorrelation
  rw [← MeasureTheory.Lp.inner_fourier_eq]
  rw [MeasureTheory.L2.inner_def, ←
    integral_re (MeasureTheory.L2.integrable_inner
      (FourierTransform.fourier (toFullLineL2 f hf2))
      (FourierTransform.fourier (translateL2 u f hf2)))]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [coe_fourier_translateL2 u f hf1 hf2] with xi hxi
  rw [hxi]
  simp only [RCLike.inner_apply, Circle.smul_def, Real.fourierChar_apply,
    smul_eq_mul]
  rw [mul_assoc, Complex.mul_conj']
  simp [Complex.exp_re]
  norm_cast
  ring

/-- The generic `L²` representative of the zero-extension function is the
canonical zero-extension vector already used by the certificate. -/
theorem toFullLineL2_zeroExtensionFn_eq
    (a : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    toFullLineL2 (IntervalZeroExtension.zeroExtensionFn a w)
        (IntervalZeroExtension.zeroExtensionFn_memLp a w) =
      IntervalZeroExtension.zeroExtension a w := by
  apply MeasureTheory.Lp.ext
  exact (IntervalZeroExtension.zeroExtensionFn_memLp a w).coeFn_toLp.trans
    (IntervalZeroExtension.coeFn_zeroExtension a w).symm

/-- Autocorrelation of the actual compactly supported interval vector. -/
def intervalAutocorrelation
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) : ℝ :=
  autocorrelation u (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)

/-- Plancherel/Wiener--Khinchin identity for the repository's canonical zero
extension and Fourier transform. -/
theorem intervalAutocorrelation_eq_cos_fourier_energy
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    intervalAutocorrelation a u w =
      ∫ xi, Real.cos (2 * Real.pi * u * xi) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) xi‖ ^ 2 := by
  unfold intervalAutocorrelation
  rw [autocorrelation_eq_cos_fourier_energy u
    (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp_one a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)]
  rw [toFullLineL2_zeroExtensionFn_eq]
  rfl

/-- Time-domain integral spelling for the interval autocorrelation. -/
theorem intervalAutocorrelation_eq_integral
    (a u : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    intervalAutocorrelation a u w =
      ∫ x, RCLike.re
        ⟪IntervalZeroExtension.zeroExtensionFn a w x,
          IntervalZeroExtension.zeroExtensionFn a w (x + u)⟫_ℂ := by
  exact autocorrelation_eq_integral u
    (IntervalZeroExtension.zeroExtensionFn a w)
    (IntervalZeroExtension.zeroExtensionFn_memLp a w)

end

end RHP2Bridge.AutocorrelationPlancherel
