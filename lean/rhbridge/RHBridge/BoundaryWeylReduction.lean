/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Boundary Weyl reduction

This is the algebraic Schur reduction behind the relative incidence problem.
If `S` is a two-sided inverse for the pole-free operator `T`, a relative zero
mode of `T` modulo the boundary range is equivalent to a zero mode of the
finite-dimensional boundary Weyl map `R ∘ S ∘ L`.
-/

namespace RHBridge.BoundaryWeylReduction

variable {E B : Type*} [AddCommGroup E] [AddCommGroup B]
  [Module ℝ E] [Module ℝ B]

/-- The boundary Weyl map associated to a resolvent `S`, boundary inclusion
`L`, and moment restriction `R`. -/
def boundaryWeyl (S : E →ₗ[ℝ] E) (L : B →ₗ[ℝ] E)
    (R : E →ₗ[ℝ] B) : B →ₗ[ℝ] B :=
  R.comp (S.comp L)

/-- A relative zero mode produces a boundary Weyl zero mode. -/
theorem boundaryWeyl_eq_zero_of_relativeMode
    (T S : E →ₗ[ℝ] E) (L : B →ₗ[ℝ] E) (R : E →ₗ[ℝ] B)
    (f : E) (b : B) (hST : S.comp T = LinearMap.id)
    (hTf : T f = L b) (hRf : R f = 0) :
    boundaryWeyl S L R b = 0 := by
  have hSf : S (T f) = f := by
    simpa using LinearMap.congr_fun hST f
  unfold boundaryWeyl
  simp only [LinearMap.comp_apply]
  rw [← hTf, hSf, hRf]

/-- Conversely, a boundary Weyl zero mode lifts through a right inverse to a
relative zero mode of the pole-free operator. -/
theorem relativeMode_of_boundaryWeyl_eq_zero
    (T S : E →ₗ[ℝ] E) (L : B →ₗ[ℝ] E) (R : E →ₗ[ℝ] B)
    (b : B) (hTS : T.comp S = LinearMap.id)
    (hK : boundaryWeyl S L R b = 0) :
    T (S (L b)) = L b ∧ R (S (L b)) = 0 := by
  constructor
  · simpa using LinearMap.congr_fun hTS (L b)
  · simpa [boundaryWeyl] using hK

end RHBridge.BoundaryWeylReduction
