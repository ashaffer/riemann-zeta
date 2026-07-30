/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import IntervalZeroExtension
import Mathlib.MeasureTheory.Function.Holder

/-!
# Bounded measurable multipliers on full-line complex `L²`

A measurable scalar symbol with an almost-everywhere uniform bound defines
a continuous complex-linear multiplication operator on `L²(ℝ, ℂ)`.  Real
symbols give Hermitian operators.
-/

namespace BoundedSymbolMultiplier

open scoped ENNReal InnerProductSpace

noncomputable abbrev FullLineComplexL2 :=
  IntervalZeroExtension.FullLineComplexL2

/-- A bounded symbol regarded as an `L∞` vector. -/
noncomputable def symbolLp
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M) :
    MeasureTheory.Lp ℂ ∞
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
  (MeasureTheory.memLp_top_of_bound hq M hbound).toLp q

/-- Complex-linear multiplication by a bounded measurable symbol. -/
noncomputable def ofSymbol
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M) :
    FullLineComplexL2 →L[ℂ] FullLineComplexL2 :=
  (ContinuousLinearMap.lsmul ℂ ℂ).holderL
    (MeasureTheory.volume : MeasureTheory.Measure ℝ) ∞ 2 2
    (symbolLp q hq M hbound)

/-- The operator acts by pointwise multiplication, almost everywhere. -/
theorem coeFn_ofSymbol
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (f : FullLineComplexL2) :
    (ofSymbol q hq M hbound f : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      fun ξ ↦ q ξ * f ξ := by
  have hholder := ContinuousLinearMap.coeFn_holder
    (r := (2 : ℝ≥0∞))
    (ContinuousLinearMap.lsmul ℂ ℂ)
    (symbolLp q hq M hbound) f
  have hsymbol :
      (symbolLp q hq M hbound : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)] q := by
    exact (MeasureTheory.memLp_top_of_bound hq M hbound).coeFn_toLp
  filter_upwards [hholder, hsymbol] with ξ hholderξ hsymbolξ
  calc
    (ofSymbol q hq M hbound f : ℝ → ℂ) ξ =
        (symbolLp q hq M hbound : ℝ → ℂ) ξ * f ξ := by
      simpa [ofSymbol] using hholderξ
    _ = q ξ * f ξ := by rw [hsymbolξ]

/-- Pointwise norm bound for the multiplication operator. -/
theorem norm_ofSymbol_apply_le
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (f : FullLineComplexL2) :
    ‖ofSymbol q hq M hbound f‖ ≤ M * ‖f‖ := by
  apply MeasureTheory.Lp.norm_le_mul_norm_of_ae_le_mul
  filter_upwards [coeFn_ofSymbol q hq M hbound f, hbound] with ξ hmul hqξ
  rw [hmul, norm_mul]
  exact mul_le_mul_of_nonneg_right hqξ (norm_nonneg _)

/-- The operator norm is at most the supplied essential bound. -/
theorem norm_ofSymbol_le
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ) (hM : 0 ≤ M)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M) :
    ‖ofSymbol q hq M hbound‖ ≤ M := by
  exact ContinuousLinearMap.opNorm_le_bound _ hM
    (norm_ofSymbol_apply_le q hq M hbound)

/-- Multiplication by an almost-everywhere real symbol is Hermitian. -/
theorem inner_ofSymbol_eq
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (hreal : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (q ξ).im = 0)
    (f g : FullLineComplexL2) :
    inner ℂ (ofSymbol q hq M hbound f) g =
      inner ℂ f (ofSymbol q hq M hbound g) := by
  rw [MeasureTheory.L2.inner_def, MeasureTheory.L2.inner_def]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [coeFn_ofSymbol q hq M hbound f,
    coeFn_ofSymbol q hq M hbound g, hreal] with ξ hmulF hmulG hrealξ
  rw [hmulF, hmulG, RCLike.inner_apply', RCLike.inner_apply']
  rw [map_mul, Complex.conj_eq_iff_im.mpr hrealξ]
  ring

end BoundedSymbolMultiplier
