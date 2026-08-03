/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.IncidenceAngleCriterion

/-!
# Contractive dual frames across a support collar

This file isolates the exact block equations hidden by the phrase "extend the
old dual frame to the collar".  A full dual identity has four blocks, not just
the old--old compression.  In particular, a prescribed old column can be
extended only if its pairing with every collar incidence vector already
vanishes.

The final elementary model is a fail-fast warning.  It has a strict global
incidence gap and an explicit contractive global dual, while the natural
Pythagorean propagation of a smaller dual column has a nonzero collar trace.
Thus the shell isometry and the old--old identity alone cannot justify a
recursive dual-frame construction.
-/

namespace RHP2Bridge.DualFrameCollarCompletion

open scoped RealInnerProductSpace

noncomputable section

/-- The full dual identity after decomposing both the incidence differential
and its proposed dual into old and collar columns. -/
def FullDualBlocks
    {H₀ H₁ E : Type*}
    [NormedAddCommGroup H₀] [InnerProductSpace ℝ H₀]
    [NormedAddCommGroup H₁] [InnerProductSpace ℝ H₁]
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B₀ : H₀ →ₗ[ℝ] E) (B₁ : H₁ →ₗ[ℝ] E)
    (C₀ : H₀ →ₗ[ℝ] E) (C₁ : H₁ →ₗ[ℝ] E) (d : ℝ) : Prop :=
  ∀ u₀ u₁ x₀ x₁,
    inner ℝ (B₀ u₀ + B₁ u₁) (C₀ x₀ + C₁ x₁) =
      d * (inner ℝ u₀ x₀ + inner ℝ u₁ x₁)

/-- A full block dual is exactly the two diagonal dual identities together
with both directed old--collar annihilation identities. -/
theorem fullDualBlocks_iff
    {H₀ H₁ E : Type*}
    [NormedAddCommGroup H₀] [InnerProductSpace ℝ H₀]
    [NormedAddCommGroup H₁] [InnerProductSpace ℝ H₁]
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B₀ : H₀ →ₗ[ℝ] E) (B₁ : H₁ →ₗ[ℝ] E)
    (C₀ : H₀ →ₗ[ℝ] E) (C₁ : H₁ →ₗ[ℝ] E) (d : ℝ) :
    FullDualBlocks B₀ B₁ C₀ C₁ d ↔
      (∀ u x, inner ℝ (B₀ u) (C₀ x) = d * inner ℝ u x) ∧
      (∀ v x, inner ℝ (B₁ v) (C₀ x) = 0) ∧
      (∀ u y, inner ℝ (B₀ u) (C₁ y) = 0) ∧
      (∀ v y, inner ℝ (B₁ v) (C₁ y) = d * inner ℝ v y) := by
  constructor
  · intro h
    refine ⟨?_, ?_, ?_, ?_⟩
    · intro u x
      simpa using h u 0 x 0
    · intro v x
      simpa using h 0 v x 0
    · intro u y
      simpa using h u 0 0 y
    · intro v y
      simpa using h 0 v 0 y
  · rintro ⟨hoo, hco, hoc, hcc⟩ u₀ u₁ x₀ x₁
    rw [inner_add_left, inner_add_right, inner_add_right,
      hoo, hco, hoc, hcc]
    ring

/-- A nonzero collar trace of a prescribed old column rules out every full
dual completion, independently of how much norm budget remains for the new
column. -/
theorem no_fullDual_completion_of_nonzero_collarTrace
    {H₀ H₁ E : Type*}
    [NormedAddCommGroup H₀] [InnerProductSpace ℝ H₀]
    [NormedAddCommGroup H₁] [InnerProductSpace ℝ H₁]
    [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (B₀ : H₀ →ₗ[ℝ] E) (B₁ : H₁ →ₗ[ℝ] E)
    (C₀ : H₀ →ₗ[ℝ] E) (d : ℝ) {v : H₁} {x : H₀}
    (hcross : inner ℝ (B₁ v) (C₀ x) ≠ 0) :
    ¬ ∃ C₁ : H₁ →ₗ[ℝ] E, FullDualBlocks B₀ B₁ C₀ C₁ d := by
  rintro ⟨C₁, hfull⟩
  have hzero := (fullDualBlocks_iff B₀ B₁ C₀ C₁ d).mp hfull |>.2.1 v x
  exact hcross hzero

/-- The old-edge and shell-edge collar traces split into the forcing
`alpha * (P + r Q)` and the shell-return trace `Q - r P`.  This is the exact
event-specific cancellation equation; no positivity premise occurs in it. -/
theorem shellTrace_decomposition
    {H K E₀ Eₛ : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    [NormedAddCommGroup K] [InnerProductSpace ℝ K]
    [NormedAddCommGroup E₀] [InnerProductSpace ℝ E₀]
    [NormedAddCommGroup Eₛ] [InnerProductSpace ℝ Eₛ]
    (C : H →ₗ[ℝ] E₀) (V : H →ₗ[ℝ] Eₛ)
    (F : K →ₗ[ℝ] E₀) (G : K →ₗ[ℝ] Eₛ)
    (alpha beta r : ℝ) (hbeta : beta = alpha * r)
    (y : K) (x z : H) :
    inner ℝ (F y) (alpha • C x - r • C z) +
        inner ℝ (G y) (beta • V x + V z) =
      alpha * (inner ℝ (F y) (C x) +
          r * inner ℝ (G y) (V x)) +
        (inner ℝ (G y) (V z) - r * inner ℝ (F y) (C z)) := by
  rw [hbeta]
  simp only [inner_sub_right, inner_add_right, real_inner_smul_right]
  ring

/-- The shell-return direction `(-r C z, V z)` is invisible to the old
incidence column whenever `r * oldDegree = shellDegree`.  Consequently every
correction preserves the old--old dual equation. -/
theorem oldDual_preserved_by_shellReturn
    {H E₀ Eₛ : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    [NormedAddCommGroup E₀] [InnerProductSpace ℝ E₀]
    [NormedAddCommGroup Eₛ] [InnerProductSpace ℝ Eₛ]
    (A : H →ₗ[ℝ] E₀) (C : H →ₗ[ℝ] E₀) (V : H →ₗ[ℝ] Eₛ)
    (oldDegree shellDegree targetDegree alpha beta r : ℝ)
    (hAC : ∀ u x, inner ℝ (A u) (C x) =
      oldDegree * inner ℝ u x)
    (hV : ∀ u x, inner ℝ (V u) (V x) = inner ℝ u x)
    (hshell : r * oldDegree = shellDegree)
    (htarget : alpha * oldDegree + beta * shellDegree = targetDegree)
    (u x z : H) :
    inner ℝ (A u) (alpha • C x - r • C z) +
        inner ℝ (shellDegree • V u) (beta • V x + V z) =
      targetDegree * inner ℝ u x := by
  rw [← hshell] at htarget ⊢
  simp only [inner_sub_right, inner_add_right, real_inner_smul_right,
    real_inner_smul_left, hAC, hV]
  rw [← htarget]
  ring

/-- Exact norm ledger for the shell-return ansatz.  Its only available budget
is the old dual slack at `alpha*x-r*z`; the correction costs
`(1+r^2)||z||^2`. -/
theorem shellReturn_energy_identity
    {H E₀ Eₛ : Type*}
    [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    [NormedAddCommGroup E₀] [InnerProductSpace ℝ E₀]
    [NormedAddCommGroup Eₛ] [InnerProductSpace ℝ Eₛ]
    (C : H →ₗ[ℝ] E₀) (V : H →ₗ[ℝ] Eₛ)
    (alpha beta r : ℝ)
    (hbeta : beta = alpha * r) (hunit : alpha ^ 2 + beta ^ 2 = 1)
    (hV : ∀ u x, inner ℝ (V u) (V x) = inner ℝ u x)
    (x z : H) :
    inner ℝ (alpha • C x - r • C z) (alpha • C x - r • C z) +
        inner ℝ (beta • V x + V z) (beta • V x + V z) =
      inner ℝ x x + (1 + r ^ 2) * inner ℝ z z -
        (inner ℝ (alpha • x - r • z) (alpha • x - r • z) -
          inner ℝ (C (alpha • x - r • z))
            (C (alpha • x - r • z))) := by
  rw [hbeta] at hunit ⊢
  simp only [map_sub, map_smul, inner_sub_left, inner_sub_right,
    inner_add_left, inner_add_right, real_inner_smul_left,
    real_inner_smul_right, hV]
  rw [real_inner_comm (C z) (C x), real_inner_comm z x]
  linear_combination (inner ℝ x x) * hunit

/-- The scalar defect budget forced by the shell-return correction.  When the
old dual is saturated (`slack = 0`), every admissible correction vanishes. -/
theorem correction_eq_zero_of_saturated_old_dual
    {r correctionSq slack : ℝ}
    (hcorrection : 0 ≤ correctionSq)
    (hbudget : (1 + r ^ 2) * correctionSq ≤ slack)
    (hsaturated : slack = 0) :
    correctionSq = 0 := by
  rw [hsaturated] at hbudget
  nlinarith [sq_nonneg r]

/-- Two-coordinate dot product used only for the explicit finite-dimensional
fail-fast model below. -/
def dot₂ (u v : ℝ × ℝ) : ℝ := u.1 * v.1 + u.2 * v.2

/-- Squared Euclidean length used only for the explicit model. -/
def normSq₂ (u : ℝ × ℝ) : ℝ := dot₂ u u

/-- Old incidence column in the model. -/
def modelB₀ (x : ℝ) : ℝ × ℝ := (5 * x, 4 * x)

/-- Collar incidence column in the model.  It is orthogonal to `modelB₀`. -/
def modelB₁ (y : ℝ) : ℝ × ℝ := (-4 * y, 5 * y)

/-- Pythagorean propagation of the old dual for the `3-4-5` degree split. -/
def propagatedC₀ (x : ℝ) : ℝ × ℝ := ((9 / 25 : ℝ) * x, (4 / 5 : ℝ) * x)

/-- A genuine global contractive dual for the model. -/
def modelGlobalC (x y : ℝ) : ℝ × ℝ :=
  ((25 / 41 : ℝ) * x - (20 / 41 : ℝ) * y,
    (20 / 41 : ℝ) * x + (25 / 41 : ℝ) * y)

theorem model_degree_split : (5 : ℝ) ^ 2 = 3 ^ 2 + 4 ^ 2 := by
  norm_num

theorem model_propagated_old_dual (u x : ℝ) :
    dot₂ (modelB₀ u) (propagatedC₀ x) = 5 * u * x := by
  simp [dot₂, modelB₀, propagatedC₀]
  ring

theorem model_propagated_contractive (x : ℝ) :
    normSq₂ (propagatedC₀ x) ≤ x ^ 2 := by
  simp [normSq₂, dot₂, propagatedC₀]
  nlinarith [sq_nonneg x]

/-- The full model has a strict incidence gap: in fact its Gram matrix is
`41 I`, whereas the target degree is `25 I`. -/
theorem model_global_gap (x y : ℝ) :
    normSq₂
        ((modelB₀ x).1 + (modelB₁ y).1,
          (modelB₀ x).2 + (modelB₁ y).2) =
      41 * (x ^ 2 + y ^ 2) := by
  simp [normSq₂, dot₂, modelB₀, modelB₁]
  ring

theorem model_global_lower_bound (x y : ℝ) :
    25 * (x ^ 2 + y ^ 2) ≤
      normSq₂
        ((modelB₀ x).1 + (modelB₁ y).1,
          (modelB₀ x).2 + (modelB₁ y).2) := by
  rw [model_global_gap]
  nlinarith [sq_nonneg x, sq_nonneg y]

theorem model_global_dual (u₀ u₁ x₀ x₁ : ℝ) :
    dot₂
        ((modelB₀ u₀).1 + (modelB₁ u₁).1,
          (modelB₀ u₀).2 + (modelB₁ u₁).2)
        (modelGlobalC x₀ x₁) =
      5 * (u₀ * x₀ + u₁ * x₁) := by
  simp [dot₂, modelB₀, modelB₁, modelGlobalC]
  ring

theorem model_global_dual_contractive (x y : ℝ) :
    normSq₂ (modelGlobalC x y) = (25 / 41 : ℝ) * (x ^ 2 + y ^ 2) := by
  simp [normSq₂, dot₂, modelGlobalC]
  ring

theorem model_globalC_is_contractive (x y : ℝ) :
    normSq₂ (modelGlobalC x y) ≤ x ^ 2 + y ^ 2 := by
  rw [model_global_dual_contractive]
  nlinarith [sq_nonneg x, sq_nonneg y]

/-- Despite the strict global gap, the propagated old column has a nonzero
collar trace. -/
theorem model_propagated_collarTrace :
    dot₂ (modelB₁ 1) (propagatedC₀ 1) = (64 / 25 : ℝ) := by
  norm_num [dot₂, modelB₁, propagatedC₀]

/-- Therefore no choice of a collar column can turn the propagated old column
into a full dual, even though `modelGlobalC` proves that a contractive full dual
exists after changing that old column. -/
theorem model_no_completion_with_propagated_column :
    ¬ ∃ c₁ c₂ : ℝ,
      ∀ u₀ u₁ x₀ x₁ : ℝ,
        dot₂
            ((modelB₀ u₀).1 + (modelB₁ u₁).1,
              (modelB₀ u₀).2 + (modelB₁ u₁).2)
            ((propagatedC₀ x₀).1 + c₁ * x₁,
              (propagatedC₀ x₀).2 + c₂ * x₁) =
          5 * (u₀ * x₀ + u₁ * x₁) := by
  rintro ⟨c₁, c₂, h⟩
  have hcross := h 0 1 1 0
  norm_num [dot₂, modelB₀, modelB₁, propagatedC₀] at hcross

end

end RHP2Bridge.DualFrameCollarCompletion
