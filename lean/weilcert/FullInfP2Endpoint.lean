/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import FullInfOperatorLedger
import PoleProjectionL2
import FullInfClipped48Transfer
import FullInfFourierBridge
import BandOperatorBilinear
import BoundedSymbolMultiplier

/-!
# Specialized p=2 endpoint composition

This file installs the actual interval, 48-mode Legendre subspace, and the two
exponential pole vectors into the abstract clipped-operator transfer.  Their
norm and projection-residual obligations are discharged by
`PoleProjectionL2`; the leakage and scalar constants are fixed to the exact
rationals certified elsewhere.

The remaining hypotheses now describe only the zeta-specific clipped form:
its band-factorization, multiplier bound, finite block, leakage realization,
and the directed digamma scalar enclosures.
-/

namespace FullInfP2Endpoint

open Matrix
open scoped RealInnerProductSpace

noncomputable section

/-- The real interval `L²[-7/16,7/16]` used at support `L = 7/4`. -/
abbrev P2IntervalL2 := LegendreScaledL2.IntervalL2 (7 / 16)

/-- The first 48 normalized scaled Legendre modes. -/
abbrev p2LegendreSubspace : Submodule ℝ P2IntervalL2 :=
  LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48

/-- Fully specialized p=2 analytic transfer, including the kernel-checked
pole-vector norm and residual estimates.  The low-band constant `4` is the
elementary finite-band alternative to invoking full-line Plancherel. -/
theorem projection_lower_bound_of_clipped_p2_data
    {K : Type*} [NormedAddCommGroup K] [InnerProductSpace ℝ K]
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (C : P2IntervalL2 →L[ℝ] K)
    (D : K →ₗ[ℝ] K →ₗ[ℝ] ℝ)
    (alpha M : ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hform : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))))
    (hfinite : ∀ u ∈ p2LegendreSubspace,
      (227 / 10 ^ 7 : ℝ) * ‖u‖ ^ 2 ≤ B u u)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hlow : ∀ x, ‖C x‖ ≤ 4 * ‖x‖)
    (hleak : ∀ w ∈ p2LegendreSubspaceᗮ,
      ‖C w‖ ^ 2 ≤ (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  apply FullInfOperatorLedger.p2_projection_lower_bound_of_clipped_operator_ledger_low4
    (B := B) (U := p2LegendreSubspace) (C := C) (D := D)
    (gPlus := PoleProjection.polePlusL2 (7 / 16))
    (gMinus := PoleProjection.poleMinusL2 (7 / 16))
    (alpha := alpha) (M := M) (rho := (81 : ℝ) / 10 ^ 23)
    (G := 1) (delta := (195 : ℝ) / 10 ^ 95)
  · exact hsymm
  · exact hform
  · exact hfinite
  · exact hD
  · exact hlow
  · exact hleak
  · exact PoleProjection.p2_polePlusL2_norm_le_one
  · exact PoleProjection.p2_poleMinusL2_norm_le_one
  · simpa [p2LegendreSubspace] using
      PoleProjection.p2_polePlus_projection_residual_le
  · simpa [p2LegendreSubspace] using
      PoleProjection.p2_poleMinus_projection_residual_le
  · exact halpha
  · exact hM0
  · exact hM
  · norm_num
  · rfl
  · norm_num
  · norm_num
  · norm_num
  · rfl
  · exact hf

/-- Composition with the stored arbitrary-real 48-dimensional interval
certificate.  This theorem no longer assumes a finite-block lower bound: it
derives it from coordinate isometry, matrix representation, and entrywise
containment in the kernel-checked parity-block intervals. -/
theorem projection_lower_bound_of_clipped48_and_p2_data
    {K : Type*} [NormedAddCommGroup K] [InnerProductSpace ℝ K]
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (C : P2IntervalL2 →L[ℝ] K)
    (D : K →ₗ[ℝ] K →ₗ[ℝ] ℝ)
    (alpha M : ℝ)
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : P2IntervalL2 → Fin 24 → ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hdecomp : ∀ x y,
      B x y = alpha * inner ℝ x y + D (C x) (C y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))))
    (hnorm : ∀ u ∈ p2LegendreSubspace,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hmatrixForm : ∀ u ∈ p2LegendreSubspace,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (hlow : ∀ x, ‖C x‖ ≤ 4 * ‖x‖)
    (hleak : ∀ w ∈ p2LegendreSubspaceᗮ,
      ‖C w‖ ^ 2 ≤ (81 / 10 ^ 23 : ℝ) * ‖w‖ ^ 2)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  apply projection_lower_bound_of_clipped_p2_data B C D alpha M
    hsymm hdecomp
  · exact FullInfClipped48Transfer.finite_lower_bound_of_clipped48_intervals
      B p2LegendreSubspace Me Mo coordEven coordOdd hnorm hmatrixForm he ho
  · exact hD
  · exact hlow
  · exact hleak
  · exact halpha
  · exact hM0
  · exact hM
  · exact hf

/-- The strongest current p=2 composition theorem.  It installs the actual
zero-extension/Plancherel band operator as well as the actual pole vectors and
the stored 48-dimensional interval certificate.  Consequently no Fourier
normalization, leakage, pole, complement, cross, or two-block-transfer premise
remains.

The hypotheses left here are precisely the zeta-form identification layer:
construct the clipped form and its band multiplier, prove its finite matrix is
inside the stored intervals, and prove the directed digamma/multiplier scalar
enclosures. -/
theorem projection_lower_bound_of_fourier_clipped48_p2_data
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (D : IntervalZeroExtension.FullLineComplexL2 →ₗ[ℝ]
      IntervalZeroExtension.FullLineComplexL2 →ₗ[ℝ] ℝ)
    (alpha M : ℝ)
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : P2IntervalL2 → Fin 24 → ℝ)
    (hsymm : ∀ x y, B x y = B y x)
    (hdecomp : ∀ x y,
      B x y = alpha * inner ℝ x y +
          D (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 x)
            (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))))
    (hnorm : ∀ u ∈ p2LegendreSubspace,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hmatrixForm : ∀ u ∈ p2LegendreSubspace,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j)
    (hD : ∀ v z, |D v z| ≤ M * ‖v‖ * ‖z‖)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  apply projection_lower_bound_of_clipped48_and_p2_data
    B (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50) D
      alpha M Me Mo coordEven coordOdd hsymm hdecomp hnorm hmatrixForm he ho hD
  · intro x
    calc
      ‖IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 x‖ ≤ ‖x‖ :=
        FullInfFourierBridge.p2_angularFourierBandCLM_norm_le x
      _ ≤ 4 * ‖x‖ := by nlinarith [norm_nonneg x]
  · intro w hw
    exact FullInfFourierBridge.p2_angularFourierBandCLM_norm_sq_le w hw
  · exact halpha
  · exact hM0
  · exact hM
  · exact hf

/-- Operator form of the strongest endpoint theorem.  A Hermitian complex
band operator `T` supplies both symmetry and the multiplier bilinear bound;
only its operator norm enclosure is required. -/
theorem projection_lower_bound_of_fourier_clipped48_p2_operator
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (T : IntervalZeroExtension.FullLineComplexL2 →L[ℂ]
      IntervalZeroExtension.FullLineComplexL2)
    (alpha M : ℝ)
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : P2IntervalL2 → Fin 24 → ℝ)
    (hdecomp : ∀ x y,
      B x y = alpha * inner ℝ x y +
          BandOperatorBilinear.ofOperator T
            (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 x)
            (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))))
    (hHermitian : ∀ x y, inner ℂ (T x) y = inner ℂ x (T y))
    (hTnorm : ‖T‖ ≤ M)
    (hnorm : ∀ u ∈ p2LegendreSubspace,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hmatrixForm : ∀ u ∈ p2LegendreSubspace,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  have hDsym := BandOperatorBilinear.symmetric_of_inner T hHermitian
  have hsymm : ∀ x y, B x y = B y x := by
    intro x y
    rw [hdecomp x y, hdecomp y x, real_inner_comm x y]
    rw [hDsym]
    ring
  apply projection_lower_bound_of_fourier_clipped48_p2_data
    B (BandOperatorBilinear.ofOperator T) alpha M Me Mo coordEven coordOdd
      hsymm hdecomp hnorm hmatrixForm he ho
  · intro v z
    exact BandOperatorBilinear.abs_ofOperator_le_of_opNorm_le T hTnorm v z
  · exact halpha
  · exact hM0
  · exact hM
  · exact hf

/-- Bounded-symbol form of the endpoint theorem.  The multiplier operator,
its norm bound, and its Hermitian property are all constructed from an a.e.
real measurable symbol `q` with `‖q‖ ≤ M`. -/
theorem projection_lower_bound_of_fourier_clipped48_p2_symbol
    (B : P2IntervalL2 →ₗ[ℝ] P2IntervalL2 →ₗ[ℝ] ℝ)
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (alpha M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (hreal : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      (q ξ).im = 0)
    (Me Mo : Matrix (Fin 24) (Fin 24) ℝ)
    (coordEven coordOdd : P2IntervalL2 → Fin 24 → ℝ)
    (hdecomp : ∀ x y,
      B x y = alpha * inner ℝ x y +
          BandOperatorBilinear.ofOperator
            (BoundedSymbolMultiplier.ofSymbol q hq M hbound)
            (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 x)
            (IntervalZeroExtension.angularFourierBandCLM (7 / 16) 50 y) +
        (inner ℝ x (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ x (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ y (PoleProjection.polePlusL2 (7 / 16))))
    (hnorm : ∀ u ∈ p2LegendreSubspace,
      ‖u‖ ^ 2 = coordEven u ⬝ᵥ coordEven u +
        coordOdd u ⬝ᵥ coordOdd u)
    (hmatrixForm : ∀ u ∈ p2LegendreSubspace,
      B u u = coordEven u ⬝ᵥ Me *ᵥ coordEven u +
        coordOdd u ⬝ᵥ Mo *ᵥ coordOdd u)
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤ Me i j ∧
        Me i j ≤ FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤ Mo i j ∧
        Mo i j ≤ FullInfClipped48Real.oddUpperReal i j)
    (halpha : (109387 : ℝ) / 100000 ≤ alpha)
    (hM0 : 0 ≤ M) (hM : M ≤ (7447 : ℝ) / 1000)
    {f : P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < B f f := by
  apply projection_lower_bound_of_fourier_clipped48_p2_operator
    B (BoundedSymbolMultiplier.ofSymbol q hq M hbound) alpha M
      Me Mo coordEven coordOdd hdecomp
  · exact BoundedSymbolMultiplier.inner_ofSymbol_eq
      q hq M hbound hreal
  · exact BoundedSymbolMultiplier.norm_ofSymbol_le
      q hq M hM0 hbound
  · exact hnorm
  · exact hmatrixForm
  · exact he
  · exact ho
  · exact halpha
  · exact hM0
  · exact hM
  · exact hf

end

end FullInfP2Endpoint
