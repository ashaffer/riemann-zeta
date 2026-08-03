/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GeneralZetaWeilForm

/-!
# The relative incidence subspace and the pole boundary sector

The two classical Weil moment conditions are orthogonality to the two pole
vectors.  On this codimension-two relative subspace the rank-two pole term
vanishes exactly.  The elementary polarization below also exhibits the pole
sector's signature `(1,1)` before it is quotiented out.
-/

namespace RHP2Bridge.RelativeIncidenceComplex

open scoped RealInnerProductSpace
open GeneralZetaWeilForm

noncomputable section

/-- The two Mellin moment conditions in logarithmic coordinates. -/
def InRelativeMomentSubspace (a : ℝ) (f : TestSpace a) : Prop :=
  inner ℝ f (PoleProjection.polePlusL2 a) = 0 ∧
    inner ℝ f (PoleProjection.poleMinusL2 a) = 0

/-- The pole pairing has one positive and one negative boundary coordinate. -/
theorem pole_signature_identity (p m : ℝ) :
    p * m + m * p = ((p + m) ^ 2 - (p - m) ^ 2) / 2 := by
  ring

/-- Both relative moment conditions annihilate the pole boundary form. -/
theorem poleTerm_eq_zero_of_relativeMoments {a : ℝ} {f : TestSpace a}
    (hf : InRelativeMomentSubspace a f) : poleTerm a f = 0 := by
  unfold InRelativeMomentSubspace at hf
  unfold poleTerm
  rw [hf.1, hf.2]
  ring

/-- On the relative complex, the completed form consists only of the
archimedean continuum and the finite prime incidence terms. -/
theorem weilForm_eq_archimedean_sub_prime_of_relativeMoments
    {a : ℝ} {f : TestSpace a} (hf : InRelativeMomentSubspace a f) :
    weilForm a f = archimedeanTerm a f - primeTerm a f := by
  unfold weilForm
  rw [poleTerm_eq_zero_of_relativeMoments hf]
  ring

end

end RHP2Bridge.RelativeIncidenceComplex
