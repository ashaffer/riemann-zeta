/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.Normed.Operator.Basic
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# Real bilinear forms induced by complex Hilbert-space operators

A bounded complex-linear band multiplier `T` contributes the real bilinear
form `Re ⟨T x,y⟩`.  This module packages that form and derives the exact
operator-norm bound consumed by `FullInfOperatorLedger`.
-/

namespace BandOperatorBilinear

open scoped RealInnerProductSpace

variable {K : Type*} [NormedAddCommGroup K] [InnerProductSpace ℂ K]

/-- The real bilinear form induced by a complex continuous linear operator. -/
noncomputable def ofOperator (T : K →L[ℂ] K) : K →ₗ[ℝ] K →ₗ[ℝ] ℝ where
  toFun x :=
    { toFun := fun y ↦ (inner ℂ (T x) y).re
      map_add' := fun y z ↦ by simp [inner_add_right]
      map_smul' := fun r y ↦ by
        rw [RCLike.real_smul_eq_coe_smul (K := ℂ), inner_smul_right]
        simp }
  map_add' x y := by
    ext z
    simp [inner_add_left]
  map_smul' r x := by
    ext y
    change (inner ℂ (T (r • x)) y).re = r * (inner ℂ (T x) y).re
    rw [RCLike.real_smul_eq_coe_smul (K := ℂ), map_smul,
      inner_smul_left]
    simp

@[simp] theorem ofOperator_apply (T : K →L[ℂ] K) (x y : K) :
    ofOperator T x y = (inner ℂ (T x) y).re := rfl

/-- Operator norm plus Hilbert-space Cauchy--Schwarz gives the required real
bilinear bound. -/
theorem abs_ofOperator_le_of_opNorm_le
    (T : K →L[ℂ] K) {M : ℝ} (hT : ‖T‖ ≤ M) (x y : K) :
    |ofOperator T x y| ≤ M * ‖x‖ * ‖y‖ := by
  calc
    |ofOperator T x y| = |(inner ℂ (T x) y).re| := rfl
    _ ≤ ‖inner ℂ (T x) y‖ := Complex.abs_re_le_norm _
    _ ≤ ‖T x‖ * ‖y‖ := norm_inner_le_norm _ _
    _ ≤ (M * ‖x‖) * ‖y‖ := by
      gcongr
      exact ContinuousLinearMap.le_of_opNorm_le T hT x
    _ = M * ‖x‖ * ‖y‖ := rfl

/-- A Hermitian operator induces a symmetric real bilinear form. -/
theorem symmetric_of_inner
    (T : K →L[ℂ] K)
    (hT : ∀ x y, inner ℂ (T x) y = inner ℂ x (T y)) :
    ∀ x y, ofOperator T x y = ofOperator T y x := by
  intro x y
  rw [ofOperator_apply, ofOperator_apply, hT]
  rw [← inner_conj_symm x (T y), Complex.conj_re]

end BandOperatorBilinear
