/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exterior-factorization finite audit

This file records only the elementary algebra used to audit a proposed
exterior factorization.  It proves that

* a genuine factorization through an old operator annihilates its kernel;
* factoring a unit charge through the scalar old block `epsilon` costs
  exactly `1 / epsilon`;
* the positive semidefinite block with old diagonal `r^2`, cross term `r`,
  and new diagonal `1` has square-root-scale coupling, while any linear
  factor through the old diagonal costs `1 / r`; and
* the scalar shifted-resolvent factor has the expected exact pole.

No completed-zeta source identity, localized Weil positivity, zero-free
strip, kernel-null charge theorem, or statement of RH is formalized here.
-/

namespace RHBridge.ExteriorFactorizationAudit

noncomputable section

section AbstractFactorization

variable {X Y Z : Type*}
  [AddCommGroup X] [AddCommGroup Y] [AddCommGroup Z]
  [Module ℝ X] [Module ℝ Y] [Module ℝ Z]

/-- Any exact linear factorization `C = T ∘ A` annihilates `ker A`.
This is the algebraic necessity behind kernel-null charge. -/
theorem factorization_implies_kernel_annihilation
    (A : X →ₗ[ℝ] Y) (C : X →ₗ[ℝ] Z) (T : Y →ₗ[ℝ] Z)
    (hfactor : C = T.comp A) {n : X} (hn : A n = 0) :
    C n = 0 := by
  rw [hfactor, LinearMap.comp_apply, hn, map_zero]

end AbstractFactorization

section ScalarNearContact

/-- Factoring the unit scalar charge through multiplication by a nonzero
`epsilon` forces the factor coefficient to be exactly `1 / epsilon`. -/
theorem scalar_factor_eq_inv {epsilon t : ℝ}
    (hepsilon : epsilon ≠ 0) (hfactor : t * epsilon = 1) :
    t = 1 / epsilon := by
  exact (eq_div_iff hepsilon).2 hfactor

/-- The exact norm cost of the scalar near-contact factorization. -/
theorem scalar_factor_abs_eq_inv {epsilon t : ℝ}
    (hepsilon : 0 < epsilon) (hfactor : t * epsilon = 1) :
    |t| = 1 / epsilon := by
  rw [scalar_factor_eq_inv (ne_of_gt hepsilon) hfactor, abs_div, abs_one,
    abs_of_pos hepsilon]

end ScalarNearContact

section SquareRootBlock

/-- Scalar old/new block with old diagonal `r^2`, cross coefficient `r`,
and new diagonal `1`. -/
def squareRootBlock (r x y : ℝ) : ℝ :=
  r ^ 2 * x ^ 2 + 2 * r * x * y + y ^ 2

/-- The square-root-scale block is an exact square. -/
theorem squareRootBlock_eq_sq (r x y : ℝ) :
    squareRootBlock r x y = (r * x + y) ^ 2 := by
  unfold squareRootBlock
  ring

/-- Hence the full block is positive semidefinite for every real `r`. -/
theorem squareRootBlock_nonnegative (r x y : ℝ) :
    0 ≤ squareRootBlock r x y := by
  rw [squareRootBlock_eq_sq]
  exact sq_nonneg _

/-- If its cross coefficient `r` factors linearly through the old diagonal
`r^2`, then the scalar factor is exactly `1 / r`. -/
theorem squareRoot_cross_factor_eq_inv {r t : ℝ}
    (hr : 0 < r) (hfactor : t * r ^ 2 = r) :
    t = 1 / r := by
  apply (eq_div_iff (ne_of_gt hr)).2
  apply mul_right_cancel₀ (ne_of_gt hr)
  calc
    (t * r) * r = t * r ^ 2 := by ring
    _ = r := hfactor
    _ = 1 * r := by ring

/-- Positive semidefiniteness permits square-root-scale coupling, but no
fixed bound can control a linear factor through all positive old diagonals.
The witness is `r = 1 / (M + 1)`. -/
theorem squareRoot_psd_defeats_fixed_linear_bound
    (M : ℝ) (hM : 0 ≤ M) :
    ∃ r : ℝ, 0 < r ∧
      (∀ x y : ℝ, 0 ≤ squareRootBlock r x y) ∧
      (∀ t : ℝ, t * r ^ 2 = r → M < |t|) := by
  let r : ℝ := 1 / (M + 1)
  have hden : 0 < M + 1 := by linarith
  have hr : 0 < r := by
    dsimp [r]
    exact one_div_pos.mpr hden
  refine ⟨r, hr, ?_, ?_⟩
  · intro x y
    exact squareRootBlock_nonnegative r x y
  · intro t hfactor
    have ht : t = 1 / r := squareRoot_cross_factor_eq_inv hr hfactor
    have hinv : 1 / r = M + 1 := by
      dsimp [r]
      field_simp [ne_of_gt hden]
    have habs : |t| = M + 1 := by
      rw [ht, abs_of_pos (one_div_pos.mpr hr), hinv]
    linarith

end SquareRootBlock

section ShiftedResolvent

/-- Scalar factor for a charged zero mode after shifting the zero old block
by `-sigma`. -/
def shiftedResolventFactor (sigma : ℝ) : ℝ :=
  -1 / sigma

/-- Away from zero, the shifted factor exactly reconstructs the unit charge.
This identity exists independently of any unshifted kernel annihilation. -/
theorem shiftedResolventFactor_identity {sigma x : ℝ}
    (hsigma : sigma ≠ 0) :
    shiftedResolventFactor sigma * ((-sigma) * x) = x := by
  unfold shiftedResolventFactor
  field_simp

/-- Its norm is exactly reciprocal in the shift, exposing the pole at a
charged zero mode. -/
theorem shiftedResolventFactor_abs (sigma : ℝ) :
    |shiftedResolventFactor sigma| = 1 / |sigma| := by
  simp only [shiftedResolventFactor, abs_div, abs_neg, abs_one]

/-- The reciprocal identity is a genuine norm blow-up: every proposed fixed
bound is exceeded at a sufficiently small positive shift. -/
theorem shiftedResolventFactor_unbounded
    (M : ℝ) (hM : 0 ≤ M) :
    ∃ sigma : ℝ, 0 < sigma ∧ M < |shiftedResolventFactor sigma| := by
  let sigma : ℝ := 1 / (M + 1)
  have hden : 0 < M + 1 := by linarith
  have hsigma : 0 < sigma := by
    dsimp [sigma]
    exact one_div_pos.mpr hden
  refine ⟨sigma, hsigma, ?_⟩
  rw [shiftedResolventFactor_abs, abs_of_pos hsigma]
  have hinv : 1 / sigma = M + 1 := by
    dsimp [sigma]
    field_simp [ne_of_gt hden]
  rw [hinv]
  linarith

end ShiftedResolvent

end

end RHBridge.ExteriorFactorizationAudit
