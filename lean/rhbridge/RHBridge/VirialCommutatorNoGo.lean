/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.InnerProductSpace.Basic

/-!
# Algebraic obstructions to a finite positive-commutator proof

This file records the two elementary identities that any virial/Mourre attack
on a compact-resolvent realization of the Weil form must respect.

* A self-adjoint operator has zero commutator expectation on each eigenvector.
* A finite matrix commutator has trace zero, hence at least one nonpositive
  diagonal entry in every nonempty orthonormal coordinate system.

These statements do not rule out a singular conjugate operator with a retained
boundary defect.  They do rule out treating a finite Galerkin commutator as a
strictly positive certificate, and they show that a strict commutator estimate
on a pure-point spectral subspace already proves that the subspace is empty.
-/

namespace RHBridge.VirialCommutatorNoGo

open scoped InnerProductSpace

/-- The algebraic commutator of two linear maps over a real or complex scalar
field. -/
def linearCommutator {𝕜 E : Type*} [RCLike 𝕜]
    [AddCommGroup E] [Module 𝕜 E]
    (H G : E →ₗ[𝕜] E) : E →ₗ[𝕜] E :=
  H.comp G - G.comp H

/-- Virial identity on an eigenvector.  The displayed symmetry hypothesis is
the only self-adjointness fact used by the proof. -/
theorem inner_linearCommutator_eigenvector_eq_zero
    {𝕜 E : Type*} [RCLike 𝕜]
    [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
    (H G : E →ₗ[𝕜] E)
    (hH : ∀ x y, inner 𝕜 x (H y) = inner 𝕜 (H x) y)
    {v : E} {eigenvalue : ℝ}
    (hv : H v = (eigenvalue : 𝕜) • v) :
    inner 𝕜 v (linearCommutator H G v) = 0 := by
  rw [linearCommutator, LinearMap.sub_apply, LinearMap.comp_apply,
    LinearMap.comp_apply, inner_sub_right, hH v (G v), hv]
  simp [map_smul, inner_smul_left, inner_smul_right]

/-- Consequently, no regular self-adjoint conjugate operator can have a
strictly positive commutator expectation on a nonzero eigenvector. -/
theorem not_inner_linearCommutator_eigenvector_pos
    {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (H G : E →ₗ[ℝ] E)
    (hH : ∀ x y, inner ℝ x (H y) = inner ℝ (H x) y)
    {v : E} {eigenvalue : ℝ} (hv : H v = eigenvalue • v) :
    ¬ 0 < inner ℝ v (linearCommutator H G v) := by
  rw [inner_linearCommutator_eigenvector_eq_zero H G hH hv]
  exact lt_irrefl 0

/-- Matrix version of the algebraic commutator. -/
def matrixCommutator {n R : Type*} [Fintype n] [CommRing R]
    (H G : Matrix n n R) : Matrix n n R :=
  H * G - G * H

/-- Every finite matrix commutator has trace zero.  Mathlib also provides the
corresponding Lie-bracket theorem; this explicit wrapper uses the same
`H * G - G * H` convention as the compression identity below. -/
theorem trace_matrixCommutator_zero
    {n R : Type*} [Fintype n] [CommRing R]
    (H G : Matrix n n R) :
    Matrix.trace (matrixCommutator H G) = 0 := by
  rw [matrixCommutator, Matrix.trace_sub, Matrix.trace_mul_comm]
  exact sub_self _

/-- In nonzero finite dimension, a commutator cannot even have every diagonal
entry strictly positive.  In particular it cannot be positive definite. -/
theorem exists_matrixCommutator_diagonal_nonpos
    {n : Type*} [Fintype n] [Nonempty n]
    (H G : Matrix n n ℝ) :
    ∃ i, matrixCommutator H G i i ≤ 0 := by
  classical
  by_contra h
  simp only [not_exists, not_le] at h
  have hsum : 0 < ∑ i, matrixCommutator H G i i :=
    Finset.sum_pos (fun i _ ↦ h i) Finset.univ_nonempty
  have htrace := trace_matrixCommutator_zero H G
  have hsumzero : ∑ i, matrixCommutator H G i i = 0 := by
    simpa [Matrix.trace, Matrix.diag] using htrace
  linarith

/-- Exact compression identity.  The first term on the right is an internal
commutator and therefore has trace zero.  Any nonzero compressed trace must
come from the two off-block leakage terms. -/
theorem compression_matrixCommutator_eq
    {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (H X P : Matrix n n R) (hP : P * P = P) :
    P * matrixCommutator H X * P =
      matrixCommutator (P * H * P) (P * X * P) +
        P * H * (1 - P) * X * P - P * X * (1 - P) * H * P := by
  have hleft (Y : Matrix n n R) : P * (P * Y) = P * Y := by
    rw [← Matrix.mul_assoc, hP]
  simp only [matrixCommutator, mul_sub, sub_mul, Matrix.mul_assoc,
    hleft]
  noncomm_ring

/-! ## A two-dimensional boundary-leakage control -/

/-- Symmetric two-state operator used to exhibit compensating commutator
trace across a compression boundary. -/
def leakageH : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0, 1; 1, 0]

/-- Skew generator for the two-state boundary-leakage example. -/
noncomputable def leakageX : Matrix (Fin 2) (Fin 2) ℝ :=
  !![0, -(1 / 2 : ℝ); 1 / 2, 0]

/-- The apparent positive first-coordinate compression is exactly balanced by
the omitted negative coordinate. -/
theorem leakage_commutator_eq :
    matrixCommutator leakageH leakageX =
      !![1, 0; 0, -1] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [matrixCommutator, leakageH, leakageX, Matrix.mul_apply,
      Fin.sum_univ_two]

/-- The retained coordinate in the leakage control has positive diagonal
commutator value. -/
theorem leakage_commutator_first_diagonal_pos :
    0 < matrixCommutator leakageH leakageX 0 0 := by
  rw [leakage_commutator_eq]
  norm_num

/-- The omitted coordinate exactly supplies a negative diagonal commutator
value. -/
theorem leakage_commutator_second_diagonal_neg :
    matrixCommutator leakageH leakageX 1 1 < 0 := by
  rw [leakage_commutator_eq]
  norm_num

end RHBridge.VirialCommutatorNoGo
