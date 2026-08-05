/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# Higher-differential obstruction for the completed incidence complex

The completed prime--archimedean incidence construction places the test vector
in degree zero and its translation defects in degree one.  One possible repair
of the remaining scalar deficit is to add a further differential out of the
edge space and hope that a two-step Hodge complex pairs the unwanted odd
sector.

This file records the elementary obstruction to that repair.  Once the
degree-zero differential is fixed, its Hodge energy is exactly `‖d₀ x‖²` and
is independent of every higher differential.  Consequently positivity of the
shifted degree-zero form remains precisely the original relative Poincare
inequality.  A higher differential can reorganize degree-one cohomology, but
it cannot improve degree-zero coercivity without changing `d₀` itself.
-/

namespace RHP2Bridge.CompletedIncidenceComplexNoGo

open scoped RealInnerProductSpace

variable {C₀ C₁ C₂ : Type*}
  [NormedAddCommGroup C₀] [InnerProductSpace ℝ C₀]
  [NormedAddCommGroup C₁] [InnerProductSpace ℝ C₁]
  [NormedAddCommGroup C₂] [InnerProductSpace ℝ C₂]

/-- The square-zero condition for a two-step continuous Hilbert complex. -/
def IsTwoStepComplex (d₀ : C₀ →L[ℝ] C₁) (d₁ : C₁ →L[ℝ] C₂) : Prop :=
  d₁.comp d₀ = 0

/-- The degree-zero Hodge energy.  The higher differential is retained as an
argument to make its irrelevance explicit in the public API. -/
def degreeZeroHodgeEnergy
    (d₀ : C₀ →L[ℝ] C₁) (_d₁ : C₁ →L[ℝ] C₂) (x : C₀) : ℝ :=
  ‖d₀ x‖ ^ 2

@[simp] theorem degreeZeroHodgeEnergy_eq
    (d₀ : C₀ →L[ℝ] C₁) (d₁ : C₁ →L[ℝ] C₂) (x : C₀) :
    degreeZeroHodgeEnergy d₀ d₁ x = ‖d₀ x‖ ^ 2 := rfl

/-- Changing the higher differential cannot change degree-zero Hodge energy. -/
theorem degreeZeroHodgeEnergy_independent
    (d₀ : C₀ →L[ℝ] C₁) (d₁ d₁' : C₁ →L[ℝ] C₂) (x : C₀) :
    degreeZeroHodgeEnergy d₀ d₁ x =
      degreeZeroHodgeEnergy d₀ d₁' x := rfl

/-- The completed incidence energy after subtracting its scalar degree
deficit. -/
def shiftedDegreeZeroForm
    (d₀ : C₀ →L[ℝ] C₁) (d₁ : C₁ →L[ℝ] C₂)
    (degree : ℝ) (x : C₀) : ℝ :=
  degreeZeroHodgeEnergy d₀ d₁ x - degree * ‖x‖ ^ 2

/-- The relative Poincare inequality left by the completed incidence
construction after its boundary moment classes have been removed. -/
def HasRelativePoincare (d₀ : C₀ →L[ℝ] C₁) (degree : ℝ) : Prop :=
  ∀ x, degree * ‖x‖ ^ 2 ≤ ‖d₀ x‖ ^ 2

/-- Positivity of the shifted degree-zero Hodge form is exactly the relative
Poincare inequality, regardless of the next differential. -/
theorem shiftedDegreeZeroForm_nonnegative_iff
    (d₀ : C₀ →L[ℝ] C₁) (d₁ : C₁ →L[ℝ] C₂) (degree : ℝ) :
    (∀ x, 0 ≤ shiftedDegreeZeroForm d₀ d₁ degree x) ↔
      HasRelativePoincare d₀ degree := by
  simp only [shiftedDegreeZeroForm, degreeZeroHodgeEnergy_eq,
    HasRelativePoincare, sub_nonneg]

/-- Even among genuine square-zero extensions, replacing the higher
differential cannot repair or destroy degree-zero positivity. -/
theorem no_higherDifferential_repair
    (d₀ : C₀ →L[ℝ] C₁) (d₁ d₁' : C₁ →L[ℝ] C₂) (degree : ℝ)
    (_hcomplex : IsTwoStepComplex d₀ d₁)
    (_hcomplex' : IsTwoStepComplex d₀ d₁') :
    (∀ x, 0 ≤ shiftedDegreeZeroForm d₀ d₁ degree x) ↔
      ∀ x, 0 ≤ shiftedDegreeZeroForm d₀ d₁' degree x := by
  rw [shiftedDegreeZeroForm_nonnegative_iff,
    shiftedDegreeZeroForm_nonnegative_iff]

/-- A two-step completed incidence complex closes the degree-zero form if and
only if its original incidence differential already has the required sharp
gap.  The square-zero law contributes no additional degree-zero estimate. -/
theorem twoStepComplex_closes_iff_relativePoincare
    (d₀ : C₀ →L[ℝ] C₁) (d₁ : C₁ →L[ℝ] C₂) (degree : ℝ)
    (_hcomplex : IsTwoStepComplex d₀ d₁) :
    (∀ x, 0 ≤ shiftedDegreeZeroForm d₀ d₁ degree x) ↔
      HasRelativePoincare d₀ degree :=
  shiftedDegreeZeroForm_nonnegative_iff d₀ d₁ degree

end RHP2Bridge.CompletedIncidenceComplexNoGo
