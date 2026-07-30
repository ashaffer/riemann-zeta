/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import BoundedSymbolMultiplier
import BandOperatorBilinear

/-!
# Pointwise order and multiplier quadratic forms

This file turns an almost-everywhere pointwise order between scalar symbols
into an order between their `L²` multiplier quadratic forms.  It also exposes
the quadratic form as the real integral of the symbol against `‖f‖²`; this
second formulation can compare a bounded clipped multiplier with an original
symbol that is not itself bounded, provided the original weighted energy is
integrable.
-/

namespace SymbolQuadraticComparison

open scoped ENNReal InnerProductSpace

noncomputable abbrev FullLineComplexL2 :=
  IntervalZeroExtension.FullLineComplexL2

/-- Replace a real symbol by the constant `alpha` outside the closed band
`|r| ≤ S`. -/
noncomputable def exteriorClip
    (omega : ℝ → ℝ) (alpha S r : ℝ) : ℝ :=
  if |r| ≤ S then omega r else alpha

/-- The bounded band correction in the decomposition
`exteriorClip = alpha + exteriorDefect`.  It vanishes off the band. -/
noncomputable def exteriorDefect
    (omega : ℝ → ℝ) (alpha S r : ℝ) : ℂ :=
  (exteriorClip omega alpha S r - alpha : ℝ)

@[simp] theorem exteriorClip_of_abs_le
    (omega : ℝ → ℝ) (alpha S r : ℝ) (hr : |r| ≤ S) :
    exteriorClip omega alpha S r = omega r := by
  simp [exteriorClip, hr]

@[simp] theorem exteriorClip_of_lt_abs
    (omega : ℝ → ℝ) (alpha S r : ℝ) (hr : S < |r|) :
    exteriorClip omega alpha S r = alpha := by
  simp [exteriorClip, not_le_of_gt hr]

/-- An exterior lower bound for the original symbol is exactly the pointwise
order saying that exterior clipping can only decrease it. -/
theorem exteriorClip_le
    (omega : ℝ → ℝ) (alpha S : ℝ)
    (hExterior : ∀ r, S ≤ |r| → alpha ≤ omega r) :
    ∀ r, exteriorClip omega alpha S r ≤ omega r := by
  intro r
  by_cases hr : |r| ≤ S
  · simp [exteriorClip, hr]
  · rw [exteriorClip_of_lt_abs omega alpha S r (lt_of_not_ge hr)]
    exact hExterior r (le_of_lt (lt_of_not_ge hr))

/-- Clipping a continuous real symbol along a closed band gives a measurable
complex symbol, even though the clip may jump at the band endpoints. -/
theorem exteriorClip_aestronglyMeasurable_of_continuous
    (omega : ℝ → ℝ) (alpha S : ℝ) (homega : Continuous omega) :
    MeasureTheory.AEStronglyMeasurable
      (fun r ↦ (exteriorClip omega alpha S r : ℂ))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  have hband : MeasurableSet {r : ℝ | |r| ≤ S} :=
    (isClosed_le continuous_abs continuous_const).measurableSet
  have hclip : Measurable (fun r ↦ exteriorClip omega alpha S r) := by
    exact Measurable.ite hband homega.measurable measurable_const
  exact hclip.complex_ofReal.aestronglyMeasurable

/-- A band bound and a bound for the exterior constant give a global bound
for the clipped complex symbol. -/
theorem norm_exteriorClip_le
    (omega : ℝ → ℝ) (alpha S M r : ℝ)
    (hband : ∀ x, |x| ≤ S → |omega x| ≤ M)
    (halpha : |alpha| ≤ M) :
    ‖(exteriorClip omega alpha S r : ℂ)‖ ≤ M := by
  by_cases hr : |r| ≤ S
  · rw [exteriorClip_of_abs_le omega alpha S r hr, Complex.norm_real]
    exact hband r hr
  · rw [exteriorClip_of_lt_abs omega alpha S r (lt_of_not_ge hr),
      Complex.norm_real]
    exact halpha

/-- Continuity of the original symbol is enough to make the band defect
strongly measurable. -/
theorem exteriorDefect_aestronglyMeasurable_of_continuous
    (omega : ℝ → ℝ) (alpha S : ℝ) (homega : Continuous omega) :
    MeasureTheory.AEStronglyMeasurable (exteriorDefect omega alpha S)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  have hclip :=
    exteriorClip_aestronglyMeasurable_of_continuous omega alpha S homega
  have halpha : MeasureTheory.AEStronglyMeasurable
      (fun _ : ℝ ↦ (alpha : ℂ))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    MeasureTheory.aestronglyMeasurable_const
  apply (hclip.sub halpha).congr
  filter_upwards [] with r
  simp [exteriorDefect, Complex.ofReal_sub]

/-- A bound on `omega-alpha` inside the band is a global bound on the
zero-extended exterior defect. -/
theorem norm_exteriorDefect_le
    (omega : ℝ → ℝ) (alpha S M r : ℝ)
    (hM : 0 ≤ M)
    (hband : ∀ x, |x| ≤ S → |omega x - alpha| ≤ M) :
    ‖exteriorDefect omega alpha S r‖ ≤ M := by
  by_cases hr : |r| ≤ S
  · rw [exteriorDefect, exteriorClip_of_abs_le omega alpha S r hr,
      Complex.norm_real]
    exact hband r hr
  · rw [exteriorDefect,
      exteriorClip_of_lt_abs omega alpha S r (lt_of_not_ge hr)]
    simpa using hM

private theorem pointwise_re_inner_mul_self
    (q z : ℂ) :
    (inner ℂ (q * z) z).re = q.re * ‖z‖ ^ 2 := by
  rw [RCLike.inner_apply']
  simp only [map_mul, Complex.mul_re, Complex.mul_im,
    Complex.conj_re, Complex.conj_im,
    Complex.sq_norm, Complex.normSq_apply]
  ring

/-- The real integrand of a bounded multiplier quadratic form is integrable. -/
theorem integrable_symbol_re_mul_norm_sq
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (f : FullLineComplexL2) :
    MeasureTheory.Integrable (fun ξ ↦ (q ξ).re * ‖f ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  have hiComplex : MeasureTheory.Integrable
      (fun ξ : ℝ ↦ inner ℂ
        ((BoundedSymbolMultiplier.ofSymbol q hq M hbound f) ξ) (f ξ))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    MeasureTheory.L2.integrable_inner (𝕜 := ℂ)
      (BoundedSymbolMultiplier.ofSymbol q hq M hbound f) f
  have hi := hiComplex.re
  apply hi.congr
  filter_upwards [BoundedSymbolMultiplier.coeFn_ofSymbol q hq M hbound f]
    with ξ hmul
  rw [hmul]
  exact pointwise_re_inner_mul_self (q ξ) (f ξ)

/-- Exact integral representation of a bounded multiplier quadratic form. -/
theorem re_inner_ofSymbol_self_eq_integral
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (f : FullLineComplexL2) :
    (inner ℂ (BoundedSymbolMultiplier.ofSymbol q hq M hbound f) f).re =
      ∫ ξ, (q ξ).re * ‖f ξ‖ ^ 2 := by
  rw [MeasureTheory.L2.inner_def]
  calc
    (∫ ξ : ℝ, inner ℂ
        ((BoundedSymbolMultiplier.ofSymbol q hq M hbound f) ξ) (f ξ)).re =
        ∫ ξ : ℝ, (inner ℂ
          ((BoundedSymbolMultiplier.ofSymbol q hq M hbound f) ξ) (f ξ)).re :=
      (integral_re (MeasureTheory.L2.integrable_inner (𝕜 := ℂ)
        (BoundedSymbolMultiplier.ofSymbol q hq M hbound f) f)).symm
    _ = ∫ ξ : ℝ, (q ξ).re * ‖f ξ‖ ^ 2 := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [BoundedSymbolMultiplier.coeFn_ofSymbol q hq M hbound f]
        with ξ hmul
      rw [hmul]
      exact pointwise_re_inner_mul_self (q ξ) (f ξ)

/-- Exact identity between the endpoint's `alpha·I + band defect`
decomposition and the single full-line clipped-symbol integral. -/
theorem alpha_norm_sq_add_exteriorDefect_bandForm_eq_integral
    (omega : ℝ → ℝ) (alpha S M : ℝ)
    (hqDefect : MeasureTheory.AEStronglyMeasurable
      (exteriorDefect omega alpha S)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hbound : ∀ᵐ r ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖exteriorDefect omega alpha S r‖ ≤ M)
    (f : FullLineComplexL2) :
    alpha * ‖f‖ ^ 2 +
        BandOperatorBilinear.ofOperator
          (BoundedSymbolMultiplier.ofSymbol
            (exteriorDefect omega alpha S) hqDefect M hbound)
          (IntervalZeroExtension.restrictToBand S f)
          (IntervalZeroExtension.restrictToBand S f) =
      ∫ r, exteriorClip omega alpha S r * ‖f r‖ ^ 2 := by
  rw [BandOperatorBilinear.ofOperator_apply,
    re_inner_ofSymbol_self_eq_integral,
    IntervalZeroExtension.norm_sq_eq_integral_norm_sq,
    ← MeasureTheory.integral_const_mul]
  have hnorm : MeasureTheory.Integrable (fun r : ℝ ↦ ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    (MeasureTheory.Lp.memLp f).integrable_norm_pow (by norm_num)
  have halpha : MeasureTheory.Integrable (fun r : ℝ ↦ alpha * ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    hnorm.const_mul alpha
  have hdefect : MeasureTheory.Integrable
      (fun r : ℝ ↦ (exteriorDefect omega alpha S r).re *
        ‖(IntervalZeroExtension.restrictToBand S f : ℝ → ℂ) r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    integrable_symbol_re_mul_norm_sq
      (exteriorDefect omega alpha S) hqDefect M hbound
      (IntervalZeroExtension.restrictToBand S f)
  rw [← MeasureTheory.integral_add halpha hdefect]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [IntervalZeroExtension.coeFn_restrictToBand S f] with r hrBand
  by_cases hr : |r| ≤ S
  · have hrIcc : r ∈ Set.Icc (-S) S := (abs_le.mp hr)
    rw [hrBand, Set.indicator_of_mem hrIcc]
    simp [exteriorDefect, exteriorClip, hr]
    ring
  · have hrIcc : r ∉ Set.Icc (-S) S := by
      intro hmem
      exact hr (abs_le.mpr hmem)
    rw [hrBand, Set.indicator_of_notMem hrIcc]
    simp [exteriorDefect, exteriorClip, hr]

/-- The clipped-symbol energy is integrable whenever its band defect is a
bounded multiplier. -/
theorem integrable_exteriorClip_mul_norm_sq
    (omega : ℝ → ℝ) (alpha S M : ℝ)
    (hqDefect : MeasureTheory.AEStronglyMeasurable
      (exteriorDefect omega alpha S)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hbound : ∀ᵐ r ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖exteriorDefect omega alpha S r‖ ≤ M)
    (f : FullLineComplexL2) :
    MeasureTheory.Integrable
      (fun r ↦ exteriorClip omega alpha S r * ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  have hnorm : MeasureTheory.Integrable (fun r : ℝ ↦ ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    (MeasureTheory.Lp.memLp f).integrable_norm_pow (by norm_num)
  have halpha : MeasureTheory.Integrable (fun r : ℝ ↦ alpha * ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    hnorm.const_mul alpha
  have hdefect : MeasureTheory.Integrable
      (fun r : ℝ ↦ (exteriorDefect omega alpha S r).re *
        ‖(IntervalZeroExtension.restrictToBand S f : ℝ → ℂ) r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    integrable_symbol_re_mul_norm_sq
      (exteriorDefect omega alpha S) hqDefect M hbound
      (IntervalZeroExtension.restrictToBand S f)
  apply (halpha.add hdefect).congr
  filter_upwards [IntervalZeroExtension.coeFn_restrictToBand S f] with r hrBand
  simp only [Pi.add_apply]
  by_cases hr : |r| ≤ S
  · have hrIcc : r ∈ Set.Icc (-S) S := abs_le.mp hr
    rw [hrBand, Set.indicator_of_mem hrIcc]
    simp [exteriorDefect, exteriorClip, hr]
    ring
  · have hrIcc : r ∉ Set.Icc (-S) S := by
      intro hmem
      exact hr (abs_le.mpr hmem)
    rw [hrBand, Set.indicator_of_notMem hrIcc]
    simp [exteriorDefect, exteriorClip, hr]

/-- Angular-frequency exterior bounds transfer exactly to Mathlib's ordinary
Fourier-frequency scaling. -/
theorem angular_exteriorClip_le
    (omega : ℝ → ℝ) (alpha b : ℝ)
    (hExterior : ∀ r, b ≤ |r| → alpha ≤ omega r) :
    ∀ ξ, exteriorClip (fun t ↦ omega (2 * Real.pi * t)) alpha
        (b / (2 * Real.pi)) ξ ≤ omega (2 * Real.pi * ξ) := by
  apply exteriorClip_le
  intro ξ hξ
  apply hExterior (2 * Real.pi * ξ)
  have htwoPi : 0 < 2 * Real.pi := by positivity
  calc
    b = (2 * Real.pi) * (b / (2 * Real.pi)) := by
      field_simp [ne_of_gt htwoPi]
    _ ≤ (2 * Real.pi) * |ξ| :=
      mul_le_mul_of_nonneg_left hξ htwoPi.le
    _ = |2 * Real.pi * ξ| := by
      rw [abs_mul, abs_of_pos htwoPi]

/-- Interval/Fourier spelling of the preceding identity.  This is exactly
the normalization used by `FullInfP2Endpoint`: `omega` is in angular
frequency, while Mathlib's Plancherel vector uses ordinary frequency
`ξ = r/(2π)`. -/
theorem interval_alpha_norm_sq_add_exteriorDefect_bandForm_eq_integral
    (a b : ℝ) (omega : ℝ → ℝ) (alpha M : ℝ)
    (hqDefect : MeasureTheory.AEStronglyMeasurable
      (exteriorDefect (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha
        (b / (2 * Real.pi)))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖exteriorDefect (fun t ↦ omega (2 * Real.pi * t)) alpha
        (b / (2 * Real.pi)) ξ‖ ≤ M)
    (w : LegendreScaledL2.IntervalL2 a) :
    alpha * ‖w‖ ^ 2 +
        BandOperatorBilinear.ofOperator
          (BoundedSymbolMultiplier.ofSymbol
            (exteriorDefect (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha
              (b / (2 * Real.pi))) hqDefect M hbound)
          (IntervalZeroExtension.angularFourierBandCLM a b w)
          (IntervalZeroExtension.angularFourierBandCLM a b w) =
      ∫ ξ, exteriorClip (fun t ↦ omega (2 * Real.pi * t)) alpha
        (b / (2 * Real.pi)) ξ *
          ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) ξ‖ ^ 2 := by
  rw [← IntervalZeroExtension.norm_fourierZeroExtensionL2 a w]
  simpa only [IntervalZeroExtension.angularFourierBandCLM_apply,
    IntervalZeroExtension.angularFourierBandL2] using
      alpha_norm_sq_add_exteriorDefect_bandForm_eq_integral
        (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha (b / (2 * Real.pi)) M
        hqDefect hbound (IntervalZeroExtension.fourierZeroExtensionL2 a w)

/-- The complete analytic comparison for the endpoint decomposition.  The
original angular symbol may be unbounded; the theorem only asks that its
weighted energy for this Fourier vector be integrable. -/
theorem interval_clipped_bandForm_le_original_integral
    (a b : ℝ) (omega : ℝ → ℝ) (alpha M : ℝ)
    (hqDefect : MeasureTheory.AEStronglyMeasurable
      (exteriorDefect (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha
        (b / (2 * Real.pi)))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖exteriorDefect (fun t ↦ omega (2 * Real.pi * t)) alpha
        (b / (2 * Real.pi)) ξ‖ ≤ M)
    (w : LegendreScaledL2.IntervalL2 a)
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun ξ ↦ omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hExterior : ∀ r, b ≤ |r| → alpha ≤ omega r) :
    alpha * ‖w‖ ^ 2 +
        BandOperatorBilinear.ofOperator
          (BoundedSymbolMultiplier.ofSymbol
            (exteriorDefect (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha
              (b / (2 * Real.pi))) hqDefect M hbound)
          (IntervalZeroExtension.angularFourierBandCLM a b w)
          (IntervalZeroExtension.angularFourierBandCLM a b w) ≤
      ∫ ξ, omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) ξ‖ ^ 2 := by
  rw [interval_alpha_norm_sq_add_exteriorDefect_bandForm_eq_integral
    a b omega alpha M hqDefect hbound w]
  apply MeasureTheory.integral_mono_ae
    (integrable_exteriorClip_mul_norm_sq
      (fun ξ ↦ omega (2 * Real.pi * ξ)) alpha (b / (2 * Real.pi)) M
      hqDefect hbound (IntervalZeroExtension.fourierZeroExtensionL2 a w))
    hOriginalIntegrable
  filter_upwards [] with ξ
  exact mul_le_mul_of_nonneg_right
    (angular_exteriorClip_le omega alpha b hExterior ξ)
    (sq_nonneg ‖(IntervalZeroExtension.fourierZeroExtensionL2 a w : ℝ → ℂ) ξ‖)

/-- Almost-everywhere order of the real parts of two bounded symbols gives
the same order on all multiplier quadratic forms. -/
theorem re_inner_ofSymbol_self_mono
    (qLower qUpper : ℝ → ℂ)
    (hqLower : MeasureTheory.AEStronglyMeasurable qLower
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hqUpper : MeasureTheory.AEStronglyMeasurable qUpper
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (MLower MUpper : ℝ)
    (hboundLower : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖qLower ξ‖ ≤ MLower)
    (hboundUpper : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖qUpper ξ‖ ≤ MUpper)
    (hle : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (qLower ξ).re ≤ (qUpper ξ).re)
    (f : FullLineComplexL2) :
    (inner ℂ
      (BoundedSymbolMultiplier.ofSymbol qLower hqLower MLower hboundLower f) f).re ≤
    (inner ℂ
      (BoundedSymbolMultiplier.ofSymbol qUpper hqUpper MUpper hboundUpper f) f).re := by
  rw [re_inner_ofSymbol_self_eq_integral,
    re_inner_ofSymbol_self_eq_integral]
  apply MeasureTheory.integral_mono_ae
    (integrable_symbol_re_mul_norm_sq qLower hqLower MLower hboundLower f)
    (integrable_symbol_re_mul_norm_sq qUpper hqUpper MUpper hboundUpper f)
  filter_upwards [hle] with ξ hleξ
  exact mul_le_mul_of_nonneg_right hleξ (sq_nonneg ‖f ξ‖)

/-- Bilinear-form spelling of `re_inner_ofSymbol_self_mono`, matching the
operator API used by the FULLINF endpoint. -/
theorem ofSymbol_quadratic_mono
    (qLower qUpper : ℝ → ℂ)
    (hqLower : MeasureTheory.AEStronglyMeasurable qLower
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hqUpper : MeasureTheory.AEStronglyMeasurable qUpper
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (MLower MUpper : ℝ)
    (hboundLower : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖qLower ξ‖ ≤ MLower)
    (hboundUpper : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖qUpper ξ‖ ≤ MUpper)
    (hle : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (qLower ξ).re ≤ (qUpper ξ).re)
    (f : FullLineComplexL2) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol qLower hqLower MLower hboundLower) f f ≤
      BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol qUpper hqUpper MUpper hboundUpper) f f := by
  exact re_inner_ofSymbol_self_mono qLower qUpper hqLower hqUpper
    MLower MUpper hboundLower hboundUpper hle f

/-- Comparison with a possibly unbounded original real symbol.  Only its
energy density for the particular vector must be integrable; no bounded
multiplier operator for the original symbol is required. -/
theorem ofSymbol_quadratic_le_integral
    (qClipped : ℝ → ℂ)
    (hqClipped : MeasureTheory.AEStronglyMeasurable qClipped
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖qClipped ξ‖ ≤ M)
    (qOriginal : ℝ → ℝ)
    (f : FullLineComplexL2)
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun ξ ↦ qOriginal ξ * ‖f ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hle : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (qClipped ξ).re ≤ qOriginal ξ) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol qClipped hqClipped M hbound) f f ≤
      ∫ ξ, qOriginal ξ * ‖f ξ‖ ^ 2 := by
  rw [BandOperatorBilinear.ofOperator_apply,
    re_inner_ofSymbol_self_eq_integral]
  apply MeasureTheory.integral_mono_ae
    (integrable_symbol_re_mul_norm_sq qClipped hqClipped M hbound f)
    hOriginalIntegrable
  filter_upwards [hle] with ξ hleξ
  exact mul_le_mul_of_nonneg_right hleξ (sq_nonneg ‖f ξ‖)

/-- Exterior clipping comparison with a possibly unbounded original symbol.
This is the direct abstract shape of the FULLINF step `Q ≥ A_S`: the
pointwise exterior floor proves the order, while boundedness is required only
for the clipped multiplier. -/
theorem exteriorClip_quadratic_le_integral
    (omega : ℝ → ℝ) (alpha S : ℝ)
    (hqClipped : MeasureTheory.AEStronglyMeasurable
      (fun r ↦ (exteriorClip omega alpha S r : ℂ))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ r ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖(exteriorClip omega alpha S r : ℂ)‖ ≤ M)
    (f : FullLineComplexL2)
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun r ↦ omega r * ‖f r‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hExterior : ∀ r, S ≤ |r| → alpha ≤ omega r) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol
          (fun r ↦ (exteriorClip omega alpha S r : ℂ))
          hqClipped M hbound) f f ≤
      ∫ r, omega r * ‖f r‖ ^ 2 := by
  apply ofSymbol_quadratic_le_integral
    (fun r ↦ (exteriorClip omega alpha S r : ℂ))
      hqClipped M hbound omega f hOriginalIntegrable
  filter_upwards [] with r
  simpa using exteriorClip_le omega alpha S hExterior r

end SymbolQuadraticComparison
