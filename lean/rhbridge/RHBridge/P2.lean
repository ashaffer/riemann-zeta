/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Glide.DigammaBounds
import FullInfP2CanonicalEndpoint
import SymbolQuadraticComparison

/-!
# Composed p=2 symbol bridge

This file instantiates the generic full-line multiplier comparison with the
actual p=2 zeta symbol.  In particular, it discharges measurability, the tight
band-defect bound, the exterior comparison, and the `2π` frequency scaling.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable section

/-- The p=2 band defect in Mathlib's ordinary Fourier-frequency variable.
It is zero outside the ordinary-frequency image of `[-50,50]`. -/
noncomputable abbrev p2OrdinaryBandDefect (ξ : ℝ) : ℂ :=
  SymbolQuadraticComparison.exteriorDefect
    (fun t ↦ GlideKernel.p2Omega (2 * Real.pi * t))
    GlideKernel.p2Alpha (50 / (2 * Real.pi)) ξ

private theorem continuous_p2Omega_ordinary :
    Continuous (fun ξ : ℝ ↦ GlideKernel.p2Omega (2 * Real.pi * ξ)) := by
  exact GlideKernel.continuous_p2Omega.comp (continuous_const.mul continuous_id)

/-- The actual ordinary-frequency defect is strongly measurable. -/
theorem p2OrdinaryBandDefect_aestronglyMeasurable :
    MeasureTheory.AEStronglyMeasurable p2OrdinaryBandDefect
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  simpa [p2OrdinaryBandDefect] using
    SymbolQuadraticComparison.exteriorDefect_aestronglyMeasurable_of_continuous
      (fun ξ : ℝ ↦ GlideKernel.p2Omega (2 * Real.pi * ξ))
      GlideKernel.p2Alpha (50 / (2 * Real.pi)) continuous_p2Omega_ordinary

/-- The directed digamma enclosure gives the exact global multiplier bound
used by the p=2 endpoint theorem. -/
theorem norm_p2OrdinaryBandDefect_le (ξ : ℝ) :
    ‖p2OrdinaryBandDefect ξ‖ ≤ (7447 : ℝ) / 1000 := by
  unfold p2OrdinaryBandDefect
  apply SymbolQuadraticComparison.norm_exteriorDefect_le
  · norm_num
  · intro x hx
    apply GlideKernel.p2Omega_sub_alpha_abs_le
    have htwoPi : 0 < 2 * Real.pi := by positivity
    calc
      |2 * Real.pi * x| = (2 * Real.pi) * |x| := by
        rw [abs_mul, abs_of_pos htwoPi]
      _ ≤ (2 * Real.pi) * (50 / (2 * Real.pi)) :=
        mul_le_mul_of_nonneg_left hx htwoPi.le
      _ = 50 := by field_simp [ne_of_gt htwoPi]

theorem p2OrdinaryBandDefect_bound_ae :
    ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖p2OrdinaryBandDefect ξ‖ ≤ (7447 : ℝ) / 1000 :=
  Filter.Eventually.of_forall norm_p2OrdinaryBandDefect_le

/-- The defect is pointwise real, hence its multiplier is Hermitian. -/
theorem p2OrdinaryBandDefect_real_ae :
    ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (p2OrdinaryBandDefect ξ).im = 0 := by
  filter_upwards [] with ξ
  simp [p2OrdinaryBandDefect, SymbolQuadraticComparison.exteriorDefect]

/-- The actual clipped p=2 form: scalar exterior floor, bounded in-band
defect multiplier, and the two pole vectors. -/
noncomputable abbrev p2ClippedForm :
    FullInfP2Endpoint.P2IntervalL2 →ₗ[ℝ]
      FullInfP2Endpoint.P2IntervalL2 →ₗ[ℝ] ℝ :=
  FullInfP2CanonicalEndpoint.p2ClippedSymbolForm
    p2OrdinaryBandDefect p2OrdinaryBandDefect_aestronglyMeasurable
    ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae
    GlideKernel.p2Alpha

/-- With the reusable analytic and scalar work discharged, positivity of the
actual clipped p=2 form depends only on parity decoupling and entrywise
containment of its canonical Legendre matrices in the stored intervals. -/
theorem p2_clipped_endpoint_of_matrix_containment
    (hparity : ∀ i j : Fin 24,
      p2ClippedForm
          (LegendreScaledL2.scaledNormalizedLegendreL2
            (7 / 16) (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2
          (7 / 16) (2 * j.val + 1)) = 0)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact
    FullInfP2CanonicalEndpoint.projection_lower_bound_of_canonical_clipped_symbol
      p2OrdinaryBandDefect p2OrdinaryBandDefect_aestronglyMeasurable
      GlideKernel.p2Alpha ((7447 : ℝ) / 1000)
      p2OrdinaryBandDefect_bound_ae p2OrdinaryBandDefect_real_ae
      hparity he ho GlideKernel.p2Alpha_lower_bound le_rfl hf

/-- The fully specialized analytic comparison `A₅₀(w) ≤ Q(w)` for the
archimedean-plus-prime multiplier part.  Only integrability of the original
unbounded weighted energy remains as a domain hypothesis. -/
theorem p2_clipped_bandForm_le_original_integral
    (w : LegendreScaledL2.IntervalL2 (7 / 16))
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun ξ ↦ GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) w :
          ℝ → ℂ) ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)) :
    GlideKernel.p2Alpha * ‖w‖ ^ 2 +
        BandOperatorBilinear.ofOperator
          (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
            p2OrdinaryBandDefect_aestronglyMeasurable
            ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
          (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 w)
          (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 w) ≤
      ∫ ξ, GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) w :
          ℝ → ℂ) ξ‖ ^ 2 := by
  simpa [p2OrdinaryBandDefect] using
    SymbolQuadraticComparison.interval_clipped_bandForm_le_original_integral
      (7 / 16) 50 GlideKernel.p2Omega GlideKernel.p2Alpha
      ((7447 : ℝ) / 1000)
      p2OrdinaryBandDefect_aestronglyMeasurable
      p2OrdinaryBandDefect_bound_ae w hOriginalIntegrable
      (fun _ hr ↦ GlideKernel.p2Omega_exterior_lower_bound hr)

/-- Positivity transferred from the certified clipped form to the original
unbounded p=2 Fourier energy, with the exact pole term.  Besides the finite
matrix facts, the sole hypothesis is the natural weighted-integrability
condition defining the original multiplier energy. -/
theorem p2_original_integral_lower_bound_of_matrix_containment
    (f : FullInfP2Endpoint.P2IntervalL2)
    (hf : f ≠ 0)
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun ξ ↦ GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
          ℝ → ℂ) ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (hparity : ∀ i j : Fin 24,
      p2ClippedForm
          (LegendreScaledL2.scaledNormalizedLegendreL2
            (7 / 16) (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2
          (7 / 16) (2 * j.val + 1)) = 0)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 <
      (∫ ξ, GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
          ℝ → ℂ) ξ‖ ^ 2) +
        (inner ℝ f (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ f (PoleProjection.polePlusL2 (7 / 16))) := by
  have hclip := p2_clipped_endpoint_of_matrix_containment
    hparity he ho hf
  have hcompare := p2_clipped_bandForm_le_original_integral
    f hOriginalIntegrable
  change (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 <
    FullInfP2CanonicalEndpoint.p2ClippedOperatorForm
      (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
        p2OrdinaryBandDefect_aestronglyMeasurable
        ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
      GlideKernel.p2Alpha f f at hclip
  rw [FullInfP2CanonicalEndpoint.p2ClippedOperatorForm_decomp] at hclip
  apply lt_of_lt_of_le hclip
  simpa [FullInfP2CanonicalEndpoint.p2BandMap,
    real_inner_self_eq_norm_sq] using
    add_le_add_left hcompare
      (inner ℝ f (PoleProjection.polePlusL2 (7 / 16)) *
          inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) +
        inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) *
          inner ℝ f (PoleProjection.polePlusL2 (7 / 16)))

end

end RHP2Bridge
