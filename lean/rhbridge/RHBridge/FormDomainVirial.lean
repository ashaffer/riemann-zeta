/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.Dual

/-!
# A form-domain virial identity through the Riesz map

Let `V` be a Hilbert form domain, let `H` be the pivot Hilbert space, and let
`j : V →L[𝕜] H` be the continuous inclusion.  The bounded operator

`J = j† j : V →L[𝕜] V`

is the Riesz representative on `V` of the pivot inner product.  A bounded
Hermitian form on `V` likewise has a bounded Riesz representative `B`.

This file proves the following weak virial fact.  If

* `B u = λ J u` (the weak eigenvalue equation),
* `B† = B`, and
* `G† J + J G = 0` (the form-domain generator preserves the pivot metric),

then the expectation of the form commutator

`G† B + B G`

on `u` is zero.  In particular, neither `u` nor `G u` has to belong to the
operator domain of the unbounded operator associated to the form.

The theorem is deliberately more general than a Gelfand triple: injectivity
and dense range of `j` are not used by this algebraic conclusion.  Those
properties matter when identifying an analytic form realization, not when
proving the weak virial cancellation.
-/

noncomputable section

namespace RHBridge.FormDomainVirial

open scoped ComplexConjugate

variable {𝕜 V H : Type*}
variable [RCLike 𝕜]
variable [NormedAddCommGroup V] [InnerProductSpace 𝕜 V] [CompleteSpace V]
variable [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]

local notation "⟨" x ", " y "⟩_H" => inner 𝕜 x y
local notation "⟨" x ", " y "⟩_V" => inner 𝕜 x y

/-- The Riesz representative on the form space of the pivot inner product. -/
def pivotRiesz (j : V →L[𝕜] H) : V →L[𝕜] V :=
  j.adjoint.comp j

/-- Evaluation of the pivot Riesz map is exactly the pulled-back pivot inner
product. -/
theorem inner_pivotRiesz (j : V →L[𝕜] H) (u v : V) :
    ⟨pivotRiesz j u, v⟩_V = ⟨j u, j v⟩_H := by
  exact ContinuousLinearMap.adjoint_inner_left j v (j u)

/-- The pivot Riesz map is self-adjoint. -/
theorem adjoint_pivotRiesz (j : V →L[𝕜] H) :
    (pivotRiesz j).adjoint = pivotRiesz j := by
  simp [pivotRiesz, ContinuousLinearMap.adjoint_comp]

/-- The bounded form commutator on the form Hilbert space.  This is the Riesz
representative of the derivative of a Hermitian form along the flow generated
by `G`. -/
def formVirial (B G : V →L[𝕜] V) : V →L[𝕜] V :=
  G.adjoint.comp B + B.comp G

/-- `G` is skew with respect to the pivot inner product pulled back by `j`. -/
def IsPivotSkew (j : V →L[𝕜] H) (G : V →L[𝕜] V) : Prop :=
  G.adjoint.comp (pivotRiesz j) + (pivotRiesz j).comp G = 0

/-- The weak eigenvalue equation after applying the Riesz representation on
the form Hilbert space.  The eigenvalue is real, as it is for a Hermitian
form. -/
def IsWeakEigenvector (j : V →L[𝕜] H) (B : V →L[𝕜] V)
    (u : V) (lambda : ℝ) : Prop :=
  B u = (lambda : 𝕜) • pivotRiesz j u

/-- The form-domain virial expectation vanishes on every weak eigenvector.

This is the domain-safe replacement for the usual calculation
`<u,[A,G]u>=0`: only the bounded Riesz representatives on `V` occur. -/
theorem inner_formVirial_eq_zero
    (j : V →L[𝕜] H) (B G : V →L[𝕜] V) (u : V) (lambda : ℝ)
    (hB : B.adjoint = B)
    (hG : IsPivotSkew j G)
    (hu : IsWeakEigenvector j B u lambda) :
    ⟨formVirial B G u, u⟩_V = 0 := by
  have hJ : (pivotRiesz j).adjoint = pivotRiesz j := adjoint_pivotRiesz j
  calc
    ⟨formVirial B G u, u⟩_V =
        ⟨B u, G u⟩_V + ⟨G u, B u⟩_V := by
      simp only [formVirial, add_apply, ContinuousLinearMap.comp_apply, inner_add_left]
      apply congrArg₂ (· + ·)
      · exact ContinuousLinearMap.adjoint_inner_left G u (B u)
      · calc
          ⟨B (G u), u⟩_V = ⟨G u, B.adjoint u⟩_V :=
            (ContinuousLinearMap.adjoint_inner_right B (G u) u).symm
          _ = ⟨G u, B u⟩_V := by rw [hB]
    _ = (lambda : 𝕜) *
        (⟨pivotRiesz j u, G u⟩_V + ⟨G u, pivotRiesz j u⟩_V) := by
      rw [hu]
      simp [inner_smul_left, inner_smul_right, mul_add]
    _ = (lambda : 𝕜) *
        ⟨(G.adjoint.comp (pivotRiesz j) +
          (pivotRiesz j).comp G) u, u⟩_V := by
      congr 1
      simp only [add_apply, ContinuousLinearMap.comp_apply,
        inner_add_left]
      apply congrArg₂ (· + ·)
      · exact (ContinuousLinearMap.adjoint_inner_left G u (pivotRiesz j u)).symm
      · calc
          ⟨G u, pivotRiesz j u⟩_V =
              ⟨G u, (pivotRiesz j).adjoint u⟩_V := by rw [hJ]
          _ = ⟨pivotRiesz j (G u), u⟩_V :=
            ContinuousLinearMap.adjoint_inner_right (pivotRiesz j) (G u) u
    _ = 0 := by
      rw [hG]
      simp

/-- A strict positive lower bound for a form virial cannot hold on a nonzero
weak eigenvector. -/
theorem not_pos_re_inner_formVirial
    (j : V →L[𝕜] H) (B G : V →L[𝕜] V) (u : V) (lambda c : ℝ)
    (hB : B.adjoint = B)
    (hG : IsPivotSkew j G)
    (hu : IsWeakEigenvector j B u lambda)
    (hc : 0 < c) (hju : j u ≠ 0) :
    ¬ c * ‖j u‖ ^ 2 ≤ RCLike.re ⟨formVirial B G u, u⟩_V := by
  rw [inner_formVirial_eq_zero j B G u lambda hB hG hu]
  simp only [map_zero]
  have hnormpos : 0 < ‖j u‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr hju)
  nlinarith

/-- Version of `not_pos_re_inner_formVirial` for an injective Gelfand-triple
embedding and a nonzero weak eigenvector. -/
theorem not_pos_re_inner_formVirial_of_injective
    (j : V →L[𝕜] H) (B G : V →L[𝕜] V) (u : V) (lambda c : ℝ)
    (hj : Function.Injective j)
    (hB : B.adjoint = B)
    (hG : IsPivotSkew j G)
    (hu : IsWeakEigenvector j B u lambda)
    (hc : 0 < c) (hu0 : u ≠ 0) :
    ¬ c * ‖j u‖ ^ 2 ≤ RCLike.re ⟨formVirial B G u, u⟩_V := by
  exact not_pos_re_inner_formVirial j B G u lambda c hB hG hu hc
    (fun hju ↦ hu0 (hj (hju.trans (map_zero j).symm)))

end RHBridge.FormDomainVirial
