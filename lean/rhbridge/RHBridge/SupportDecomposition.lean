/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.NestedSupport
import Mathlib.Analysis.InnerProductSpace.Projection.Basic

/-!
# Old-support and boundary-collar decomposition

This file packages the image of a smaller support interval as a closed Hilbert
subspace of a larger one.  Its orthogonal complement is the abstract boundary
collar.  No positivity property of the Weil form is assumed.
-/

namespace RHP2Bridge.SupportDecomposition

open scoped InnerProductSpace RealInnerProductSpace

noncomputable section

open NestedSupport GeneralZetaWeilForm

/-- The embedded copy of `L²[-a,a]` inside `L²[-b,b]`. -/
def oldSupportSubspace (a b : ℝ) (hab : a ≤ b) :
    Submodule ℝ (TestSpace b) :=
  LinearMap.range (nestedSupportLI a b hab).toLinearMap

noncomputable instance oldSupportSubspace_completeSpace
    (a b : ℝ) (hab : a ≤ b) :
    CompleteSpace (oldSupportSubspace a b hab) := by
  let e := (nestedSupportLI a b hab).equivRange
  exact (completeSpace_congr (e := e.toLinearEquiv.toEquiv)
    e.isometry.isUniformEmbedding).mp inferInstance

/-- Orthogonal projection onto the functions supported in the old interval. -/
def oldPart (a b : ℝ) (hab : a ≤ b) (f : TestSpace b) : TestSpace b :=
  (oldSupportSubspace a b hab).starProjection f

/-- The orthogonal residual, representing the newly available boundary
collars `[-b,-a) ∪ (a,b]`. -/
def collarPart (a b : ℝ) (hab : a ≤ b) (f : TestSpace b) : TestSpace b :=
  f - oldPart a b hab f

theorem oldPart_mem (a b : ℝ) (hab : a ≤ b) (f : TestSpace b) :
    oldPart a b hab f ∈ oldSupportSubspace a b hab :=
  (oldSupportSubspace a b hab).starProjection_apply_mem f

theorem collarPart_mem_orthogonal (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    collarPart a b hab f ∈ (oldSupportSubspace a b hab)ᗮ :=
  (oldSupportSubspace a b hab).sub_starProjection_mem_orthogonal f

/-- The collar residual is orthogonal to every zero-extended old-support
vector.  This is the precise abstract meaning of being boundary-supported. -/
theorem inner_collarPart_nestedSupport_eq_zero (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) (u : TestSpace a) :
    inner ℝ (collarPart a b hab f) (nestedSupport a b u) = 0 := by
  apply (Submodule.mem_orthogonal' _ _).mp
    (collarPart_mem_orthogonal a b hab f)
  exact ⟨u, rfl⟩

theorem oldPart_add_collarPart (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    oldPart a b hab f + collarPart a b hab f = f := by
  unfold collarPart
  abel

theorem inner_oldPart_collarPart_eq_zero (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    inner ℝ (oldPart a b hab f) (collarPart a b hab f) = 0 := by
  have hc := collarPart_mem_orthogonal a b hab f
  rw [real_inner_comm]
  exact (Submodule.mem_orthogonal' _ _).mp hc _ (oldPart_mem a b hab f)

theorem norm_sq_eq_oldPart_add_collarPart (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    ‖f‖ ^ 2 = ‖oldPart a b hab f‖ ^ 2 +
      ‖collarPart a b hab f‖ ^ 2 := by
  have h := norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero
    (𝕜 := ℝ) (oldPart a b hab f) (collarPart a b hab f)
      (inner_oldPart_collarPart_eq_zero a b hab f)
  calc
    ‖f‖ ^ 2 = ‖oldPart a b hab f + collarPart a b hab f‖ ^ 2 := by
      rw [oldPart_add_collarPart]
    _ = ‖oldPart a b hab f‖ ^ 2 + ‖collarPart a b hab f‖ ^ 2 := by
      simpa [pow_two] using h

/-- Every old component is the nested-support image of a unique smaller
interval vector. -/
theorem exists_unique_oldPart_preimage (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    ∃! u : TestSpace a, nestedSupport a b u = oldPart a b hab f := by
  obtain ⟨u, hu⟩ := oldPart_mem a b hab f
  refine ⟨u, ?_, ?_⟩
  · exact hu
  · intro v hv
    exact (nestedSupportLI a b hab).injective (hv.trans hu.symm)

/-- The old diagonal block is governed exactly by the smaller-support Weil
form plus the finite shell of prime powers activated between the supports. -/
theorem exists_unique_oldPart_weilFormula (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    ∃! u : TestSpace a,
      nestedSupport a b u = oldPart a b hab f ∧
      weilForm b (oldPart a b hab f) = weilForm a u -
        ∑ n ∈ activePrimePowers b \ activePrimePowers a,
          primePowerTerm a u n := by
  obtain ⟨u, hu, huniq⟩ := exists_unique_oldPart_preimage a b hab f
  refine ⟨u, ⟨hu, ?_⟩, ?_⟩
  · rw [← hu]
    exact weilForm_nestedSupport hab u
  · intro v hv
    exact huniq v hv.1

/-- Polarized cross term of the quadratic Weil functional.  This definition
is valid before a separate bilinear realization of the logarithmic form has
been constructed. -/
def weilCross (b : ℝ) (u v : TestSpace b) : ℝ :=
  (weilForm b (u + v) - weilForm b u - weilForm b v) / 2

theorem weilForm_add (b : ℝ) (u v : TestSpace b) :
    weilForm b (u + v) =
      weilForm b u + 2 * weilCross b u v + weilForm b v := by
  unfold weilCross
  ring

theorem weilCross_comm (b : ℝ) (u v : TestSpace b) :
    weilCross b u v = weilCross b v u := by
  unfold weilCross
  rw [add_comm u v]
  ring

/-- Exact block expansion into old-support, cross, and collar contributions. -/
theorem weilForm_eq_old_cross_collar (a b : ℝ) (hab : a ≤ b)
    (f : TestSpace b) :
    weilForm b f =
      weilForm b (oldPart a b hab f) +
        2 * weilCross b (oldPart a b hab f) (collarPart a b hab f) +
          weilForm b (collarPart a b hab f) := by
  calc
    weilForm b f =
        weilForm b (oldPart a b hab f + collarPart a b hab f) := by
      rw [oldPart_add_collarPart]
    _ = _ := weilForm_add b _ _

/-- The sharp two-block (Schur determinant) positivity lemma.  Unlike an
estimate through absolute spectral floors, this compares the cross term to
the actual energies of the two vectors. -/
theorem add_two_mul_nonneg_of_cross_sq_le
    {A C D : ℝ} (hA : 0 ≤ A) (hD : 0 ≤ D) (hdet : C ^ 2 ≤ A * D) :
    0 ≤ A + 2 * C + D := by
  by_contra h
  have hsum : A + D < -2 * C := by linarith
  have hC : C < 0 := by nlinarith
  have hsquare : (-2 * C) ^ 2 < (A + D) ^ 2 := by
    nlinarith [sq_nonneg (A - D)]
  nlinarith [sq_nonneg (A - D)]

/-- Positivity at the enlarged support follows pointwise from positivity of
the old and collar diagonal energies and the relative-energy determinant
bound on their cross interaction.  Thus the remaining propagation problem is
precisely to prove `cross² ≤ oldEnergy * collarEnergy` uniformly in support. -/
theorem weilForm_nonneg_of_relative_cross_bound
    (a b : ℝ) (hab : a ≤ b) (f : TestSpace b)
    (hold : 0 ≤ weilForm b (oldPart a b hab f))
    (hcollar : 0 ≤ weilForm b (collarPart a b hab f))
    (hcross : (weilCross b (oldPart a b hab f) (collarPart a b hab f)) ^ 2 ≤
      weilForm b (oldPart a b hab f) *
        weilForm b (collarPart a b hab f)) :
    0 ≤ weilForm b f := by
  rw [weilForm_eq_old_cross_collar a b hab f]
  exact add_two_mul_nonneg_of_cross_sq_le hold hcollar hcross

end

end RHP2Bridge.SupportDecomposition
