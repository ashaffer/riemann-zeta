/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import FullInfP2Endpoint
import LegendreParityCoordinates

/-!
# Canonical p=2 clipped-symbol endpoint

This module defines the clipped bilinear form itself from the scalar floor,
the actual Fourier-band multiplier, and the two pole vectors.  Its strongest
theorem uses canonical parity-reordered Legendre coordinates and actual basis
entry matrices.  Consequently the arbitrary form/decomposition, coordinate
isometry, and matrix-representation premises of `FullInfP2Endpoint` disappear;
only parity decoupling and entrywise analytic matrix containment remain.
-/

namespace FullInfP2CanonicalEndpoint

open Matrix
open scoped RealInnerProductSpace
open FullInfP2Endpoint

noncomputable section

abbrev p2BandMap :=
  IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50

@[simp] theorem p2BandMap_toLinearMap_apply (x : P2IntervalL2) :
    p2BandMap.toLinearMap x = p2BandMap x := rfl

noncomputable def p2ClippedOperatorForm
    (T : IntervalZeroExtension.FullLineComplexL2 →L[ℂ]
      IntervalZeroExtension.FullLineComplexL2)
    (alpha : ℝ) : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ :=
  alpha • innerₗ P2IntervalL2 +
    (BandOperatorBilinear.ofOperator T).compl₁₂
      p2BandMap.toLinearMap p2BandMap.toLinearMap +
    (LinearMap.mul ℝ ℝ).compl₁₂
      ((innerₗ P2IntervalL2).flip
        (PoleProjection.polePlusL2 (7 / 16)))
      ((innerₗ P2IntervalL2).flip
        (PoleProjection.poleMinusL2 (7 / 16))) +
    (LinearMap.mul ℝ ℝ).compl₁₂
      ((innerₗ P2IntervalL2).flip
        (PoleProjection.poleMinusL2 (7 / 16)))
      ((innerₗ P2IntervalL2).flip
        (PoleProjection.polePlusL2 (7 / 16)))

@[simp] theorem p2ClippedOperatorForm_apply_raw
    (T : IntervalZeroExtension.FullLineComplexL2 →L[ℂ]
      IntervalZeroExtension.FullLineComplexL2)
    (alpha : ℝ) (x y : P2IntervalL2) :
    p2ClippedOperatorForm T alpha x y =
      alpha * inner ℝ x y +
          BandOperatorBilinear.ofOperator T
            (p2BandMap.toLinearMap x) (p2BandMap.toLinearMap y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))) := by
  simp only [p2ClippedOperatorForm, LinearMap.add_apply,
    LinearMap.smul_apply, smul_eq_mul, LinearMap.compl₁₂_apply,
    LinearMap.flip_apply, innerₗ_apply_apply, LinearMap.mul_apply']
  ac_rfl

theorem p2ClippedOperatorForm_decomp
    (T : IntervalZeroExtension.FullLineComplexL2 →L[ℂ]
      IntervalZeroExtension.FullLineComplexL2)
    (alpha : ℝ) (x y : P2IntervalL2) :
    p2ClippedOperatorForm T alpha x y =
      alpha * inner ℝ x y +
          BandOperatorBilinear.ofOperator T (p2BandMap x) (p2BandMap y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))) := by
  rw [p2ClippedOperatorForm_apply_raw]
  rw [p2BandMap_toLinearMap_apply x, p2BandMap_toLinearMap_apply y]

theorem p2ClippedOperatorForm_symmetric
    (T : IntervalZeroExtension.FullLineComplexL2 →L[ℂ]
      IntervalZeroExtension.FullLineComplexL2)
    (alpha : ℝ)
    (hT : ∀ x y, inner ℂ (T x) y = inner ℂ x (T y)) :
    ∀ x y, p2ClippedOperatorForm T alpha x y =
      p2ClippedOperatorForm T alpha y x := by
  intro x y
  rw [p2ClippedOperatorForm_decomp, p2ClippedOperatorForm_decomp,
    real_inner_comm x y]
  rw [BandOperatorBilinear.symmetric_of_inner T hT]
  ring

noncomputable def p2ClippedSymbolForm
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (alpha : ℝ) : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ :=
  p2ClippedOperatorForm (BoundedSymbolMultiplier.ofSymbol q hq M hbound) alpha

abbrev p2EvenCoord : P2IntervalL2 → Fin 24 → ℝ :=
  LegendreParityCoordinates.evenCoord (7 / 16) 24

abbrev p2OddCoord : P2IntervalL2 → Fin 24 → ℝ :=
  LegendreParityCoordinates.oddCoord (7 / 16) 24

noncomputable def p2EvenMatrix
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ) :
    Matrix (Fin 24) (Fin 24) ℝ :=
  LegendreParityCoordinates.evenMatrix (7 / 16) B 24

noncomputable def p2OddMatrix
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ) :
    Matrix (Fin 24) (Fin 24) ℝ :=
  LegendreParityCoordinates.oddMatrix (7 / 16) B 24

theorem p2_norm_coordinates (u : P2IntervalL2)
    (hu : u ∈ p2LegendreSubspace) :
    ‖u‖ ^ 2 = p2EvenCoord u ⬝ᵥ p2EvenCoord u +
      p2OddCoord u ⬝ᵥ p2OddCoord u := by
  simpa [p2LegendreSubspace] using
    LegendreParityCoordinates.norm_sq_eq_evenCoord_dot_add_oddCoord_dot
      (7 / 16) (by norm_num) 24 u hu

theorem p2_matrix_form
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hparity : ∀ i j : Fin 24,
      B (LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2
          (7 / 16) (2 * j.val + 1)) = 0)
    (u : P2IntervalL2) (hu : u ∈ p2LegendreSubspace) :
    B u u = p2EvenCoord u ⬝ᵥ p2EvenMatrix B *ᵥ p2EvenCoord u +
      p2OddCoord u ⬝ᵥ p2OddMatrix B *ᵥ p2OddCoord u := by
  simpa [p2LegendreSubspace, p2EvenMatrix, p2OddMatrix] using
    LegendreParityCoordinates.bilinear_eq_parity_matrices
      (7 / 16) B (by norm_num) 24 hsymm hparity u hu

/-- Canonical clipped-symbol endpoint.  All form, Fourier, pole, coordinate,
and matrix-representation data are definitions; the remaining finite analytic
premises are parity decoupling and containment of the actual basis matrices in
the stored intervals. -/
theorem projection_lower_bound_of_canonical_clipped_symbol
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (alpha M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (hreal : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (q ξ).im = 0)
    (hparity : ∀ i j : Fin 24,
      p2ClippedSymbolForm q hq M hbound alpha
          (LegendreScaledL2.scaledNormalizedLegendreL2
            (7 / 16) (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2
          (7 / 16) (2 * j.val + 1)) = 0)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          p2EvenMatrix (p2ClippedSymbolForm q hq M hbound alpha) i j ∧
        p2EvenMatrix (p2ClippedSymbolForm q hq M hbound alpha) i j ≤
          FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          p2OddMatrix (p2ClippedSymbolForm q hq M hbound alpha) i j ∧
        p2OddMatrix (p2ClippedSymbolForm q hq M hbound alpha) i j ≤
          FullInfClipped48Real.oddUpperReal i j)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 <
      p2ClippedSymbolForm q hq M hbound alpha f f := by
  let B := p2ClippedSymbolForm q hq M hbound alpha
  have hHermitian := BoundedSymbolMultiplier.inner_ofSymbol_eq
    q hq M hbound hreal
  have hM0 : 0 ≤ M := by
    obtain ⟨ξ, hξ⟩ := hbound.exists
    exact (norm_nonneg (q ξ)).trans hξ
  have hsymm : ∀ x y, B x y = B y x :=
    p2ClippedOperatorForm_symmetric _ alpha hHermitian
  apply FullInfP2Endpoint.projection_lower_bound_of_fourier_clipped48_p2_symbol
    B q hq alpha M hbound hreal (p2EvenMatrix B) (p2OddMatrix B)
      p2EvenCoord p2OddCoord
  · intro x y
    simp [B, p2ClippedSymbolForm]
  · exact p2_norm_coordinates
  · exact p2_matrix_form B hsymm hparity
  · exact he
  · exact ho
  · exact halpha
  · exact hM0
  · exact hM
  · exact hf

end

end FullInfP2CanonicalEndpoint
