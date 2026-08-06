/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.LinearPMap

/-!
# Riesz characterization of an energy-space adjoint

This file isolates the functional-analytic step needed in the finite-window
Suzuki construction.  The Hilbert space `V` should be read as the energy/form
space in a Gelfand triple.  A possibly unbounded operator is represented by a
`LinearPMap` `D : V →ₗ.[𝕜] V` with dense domain.

For `y w : V`, the statement

`<w,x>_V = <y,Dx>_V` for every `x` in `Dom(D)`

says that the dual functional obtained by transposing `D` against the Riesz
functional of `y` has Riesz representative `w`.  We prove that this is
equivalent to `y ∈ Dom(D†)` and `D†y=w`.  Consequently a distributional or
dual weak eigen-equation is exactly the corresponding Hilbert-space adjoint
equation, once its weak functional has a Riesz representative.

Mathlib's `LinearPMap.adjoint` already constructs that representative using
Fréchet--Riesz.  The results below expose the construction as an iff suitable
for downstream use and transfer any independently proved one-dimensional
classification of weak solutions to the adjoint eigenspace.

No distributional ODE theorem, density of a particular smooth core, or
identification of an energy completion with a zeta form domain is assumed or
proved here.  Those are analytic inputs in an application.  For a symmetric
operator and nonreal `z`, the adjoint eigenspace is the usual deficiency
space.  The equation predicates below deliberately include the zero solution;
the nonzero generator hypothesis is stated separately when a one-dimensional
eigenspace is concluded.
-/

noncomputable section

namespace RHBridge.GelfandTripleAdjoint

open RCLike
open scoped ComplexConjugate

variable {𝕜 V : Type*}
variable [RCLike 𝕜]
variable [NormedAddCommGroup V] [InnerProductSpace 𝕜 V] [CompleteSpace V]

local notation "⟨" x ", " y "⟩" => inner 𝕜 x y

/-- The vector supplied by Fréchet--Riesz for a continuous functional on the
energy Hilbert space.  In a Gelfand-triple application this is the abstract
`J⁻¹ F`. -/
def rieszVector (F : StrongDual 𝕜 V) : V :=
  (InnerProductSpace.toDual 𝕜 V).symm F

/-- Evaluation of a functional through its explicit Riesz vector. -/
@[simp]
theorem inner_rieszVector (F : StrongDual 𝕜 V) (x : V) :
    ⟨rieszVector F, x⟩ = F x := by
  exact InnerProductSpace.toDual_symm_apply

/-- The explicit Riesz constructor is injective. -/
theorem rieszVector_injective : Function.Injective (rieszVector : StrongDual 𝕜 V → V) :=
  (InnerProductSpace.toDual 𝕜 V).symm.injective

/-- `w` represents, in the energy-space Riesz duality, the functional obtained
by applying the transpose of `D` to the Riesz functional represented by `y`.

The quantifier is over the graph domain of `D`; no value of `D` outside that
domain is mentioned. -/
def HasRieszRepresentative (D : V →ₗ.[𝕜] V) (y w : V) : Prop :=
  ∀ x : D.domain, ⟨w, (x : V)⟩ = ⟨y, D x⟩

/-- A vector belongs to the adjoint domain exactly when its transposed weak
functional has an energy-space Riesz representative. -/
theorem mem_adjoint_domain_iff_exists_rieszRepresentative
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V)) (y : V) :
    y ∈ D.adjoint.domain ↔ ∃ w : V, HasRieszRepresentative D y w := by
  constructor
  · intro hy
    refine ⟨D.adjoint ⟨y, hy⟩, ?_⟩
    exact D.adjoint_isFormalAdjoint hD ⟨y, hy⟩
  · rintro ⟨w, hw⟩
    exact LinearPMap.mem_adjoint_domain_of_exists y ⟨w, hw⟩

/-- Once `y` is known to be in the adjoint domain, the value of the adjoint is
the unique Riesz representative of its transposed weak functional. -/
theorem adjoint_apply_eq_iff_hasRieszRepresentative
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    (y : V) (hy : y ∈ D.adjoint.domain) (w : V) :
    D.adjoint ⟨y, hy⟩ = w ↔ HasRieszRepresentative D y w := by
  constructor
  · intro hadj x
    rw [← hadj]
    exact D.adjoint_isFormalAdjoint hD ⟨y, hy⟩ x
  · intro hw
    exact LinearPMap.adjoint_apply_eq hD ⟨y, hy⟩ hw

omit [CompleteSpace V] in
/-- The Riesz representative, when it exists, is unique.  Density is the
load-bearing hypothesis. -/
theorem rieszRepresentative_unique
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    {y w₁ w₂ : V}
    (h₁ : HasRieszRepresentative D y w₁)
    (h₂ : HasRieszRepresentative D y w₂) :
    w₁ = w₂ := by
  apply hD.eq_of_inner_left 𝕜
  intro x hx
  exact (h₁ ⟨x, hx⟩).trans (h₂ ⟨x, hx⟩).symm

/-- The dual weak eigen-equation at `z`: transposing `D` against the Riesz
functional represented by `y` gives the Riesz functional represented by
`z • y`.

This convention exactly matches mathlib's convention that the inner product
is conjugate-linear in its first variable. -/
def SatisfiesDualWeakEigenEquation (D : V →ₗ.[𝕜] V) (z : 𝕜) (y : V) : Prop :=
  HasRieszRepresentative D y (z • y)

/-- `y` satisfies the eigen-equation for the partially defined adjoint,
including the required adjoint-domain witness.  Zero is allowed, as it is in
the kernel/eigenspace itself. -/
def SatisfiesAdjointEigenEquation (D : V →ₗ.[𝕜] V) (z : 𝕜) (y : V) : Prop :=
  ∃ hy : y ∈ D.adjoint.domain, D.adjoint ⟨y, hy⟩ = z • y

/-- The distributional/dual eigen-equation for a continuous functional.  With
Lean's convention that the inner product is conjugate-linear in its first
argument, eigenvalue `z` on the dual functional corresponds to eigenvalue
`star z` on its Riesz vector. -/
def SatisfiesDualEigenEquation (D : V →ₗ.[𝕜] V) (z : 𝕜)
    (F : StrongDual 𝕜 V) : Prop :=
  ∀ x : D.domain, F (D x) = z * F (x : V)

/-- Dual weak eigen-equations are precisely adjoint eigen-equations.  This is
the abstract topology/domain repair: continuity in the energy topology is
consumed as adjoint-domain membership, rather than incorrectly upgraded to
continuity in a weaker pivot norm. -/
theorem dualWeakEigenEquation_iff_adjointEigenEquation
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V)) (z : 𝕜) (y : V) :
    SatisfiesDualWeakEigenEquation D z y ↔ SatisfiesAdjointEigenEquation D z y := by
  constructor
  · intro hweak
    have hy : y ∈ D.adjoint.domain :=
      (mem_adjoint_domain_iff_exists_rieszRepresentative D hD y).2
        ⟨z • y, hweak⟩
    exact ⟨hy, (adjoint_apply_eq_iff_hasRieszRepresentative D hD y hy (z • y)).2 hweak⟩
  · rintro ⟨hy, heig⟩
    exact (adjoint_apply_eq_iff_hasRieszRepresentative D hD y hy (z • y)).1 heig

/-- A dual eigen-equation is exactly an adjoint eigen-equation after taking its
explicit Riesz representative.  The conjugation on the eigenvalue is forced
by Lean/mathlib's inner-product convention and must not be dropped. -/
theorem dualEigenEquation_iff_rieszVector_adjointEigenEquation
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    (z : 𝕜) (F : StrongDual 𝕜 V) :
    SatisfiesDualEigenEquation D z F ↔
      SatisfiesAdjointEigenEquation D (star z) (rieszVector F) := by
  rw [← dualWeakEigenEquation_iff_adjointEigenEquation D hD (star z) (rieszVector F)]
  constructor
  · intro hF x
    simp only [inner_smul_left, inner_rieszVector, starRingEnd_apply, star_star]
    exact (hF x).symm
  · intro hweak x
    have hx := hweak x
    simp only [inner_smul_left, inner_rieszVector, starRingEnd_apply, star_star] at hx
    exact hx.symm

/-- Functional-level one-dimensional transfer.  If an external theorem
classifies every dual solution of `F ∘ D = z F` as a multiple of one
continuous functional `seed`, then the adjoint eigenspace at `star z` consists
exactly of the scalar multiples of `rieszVector seed`.

The conjugate-linearity of the Riesz equivalence only conjugates the scalar
coefficient; because the coefficient ranges over all of `𝕜`, the resulting
one-dimensional span is unchanged. -/
theorem adjointEigenEquation_iff_mem_rieszSpan_of_dualEquation
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    (z : 𝕜) (seed : StrongDual 𝕜 V)
    (hclass : ∀ F : StrongDual 𝕜 V,
      SatisfiesDualEigenEquation D z F ↔ ∃ c : 𝕜, F = c • seed)
    (y : V) :
    SatisfiesAdjointEigenEquation D (star z) y ↔
      ∃ c : 𝕜, y = c • rieszVector seed := by
  have hyRiesz :
      rieszVector ((InnerProductSpace.toDual 𝕜 V) y) = y := by
    simp [rieszVector]
  have hyiff :=
    dualEigenEquation_iff_rieszVector_adjointEigenEquation
      D hD z ((InnerProductSpace.toDual 𝕜 V) y)
  rw [hyRiesz] at hyiff
  constructor
  · intro hy
    obtain ⟨c, hc⟩ := (hclass ((InnerProductSpace.toDual 𝕜 V) y)).1 (hyiff.2 hy)
    refine ⟨star c, ?_⟩
    have hc' := congrArg rieszVector hc
    rw [show rieszVector ((InnerProductSpace.toDual 𝕜 V) y) = y by
      simp [rieszVector]] at hc'
    exact hc'.trans (by
      simpa only [rieszVector, starRingEnd_apply] using
        (InnerProductSpace.toDual 𝕜 V).symm.map_smulₛₗ c seed)
  · rintro ⟨c, rfl⟩
    apply hyiff.1
    apply (hclass ((InnerProductSpace.toDual 𝕜 V) (c • rieszVector seed))).2
    refine ⟨star c, ?_⟩
    calc
      (InnerProductSpace.toDual 𝕜 V) (c • rieszVector seed) =
          star c • (InnerProductSpace.toDual 𝕜 V) (rieszVector seed) :=
        (InnerProductSpace.toDual 𝕜 V).map_smulₛₗ c (rieszVector seed)
      _ = star c • seed := by simp [rieszVector]

/-- Transfer of a complete scalar-multiple classification of dual weak
solutions to the Hilbert-space adjoint eigenspace.  For differentiation on a
connected interval, the external analytic input is the distributional ODE
classification saying that all weak solutions are multiples of one
exponential. -/
theorem adjointEigenEquation_iff_mem_span_of_dualWeak
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    (z : 𝕜) (generator : V)
    (hclass : ∀ y : V,
      SatisfiesDualWeakEigenEquation D z y ↔ ∃ c : 𝕜, y = c • generator)
    (y : V) :
    SatisfiesAdjointEigenEquation D z y ↔ ∃ c : 𝕜, y = c • generator := by
  rw [← dualWeakEigenEquation_iff_adjointEigenEquation D hD z y]
  exact hclass y

/-- If the independently identified weak generator is nonzero, the adjoint
eigenspace is nontrivial and every one of its vectors is a scalar multiple of
that generator.  For a symmetric operator at nonreal `z`, this is the precise
abstract content of a one-dimensional deficiency-space transfer. -/
theorem oneDimensional_adjoint_eigenspace_of_dualWeak
    (D : V →ₗ.[𝕜] V) (hD : Dense (D.domain : Set V))
    (z : 𝕜) (generator : V) (hgenerator : generator ≠ 0)
    (hclass : ∀ y : V,
      SatisfiesDualWeakEigenEquation D z y ↔ ∃ c : 𝕜, y = c • generator) :
    generator ≠ 0 ∧ SatisfiesAdjointEigenEquation D z generator ∧
      ∀ y : V, SatisfiesAdjointEigenEquation D z y ↔
        ∃ c : 𝕜, y = c • generator := by
  refine ⟨hgenerator, ?_, ?_⟩
  · rw [← dualWeakEigenEquation_iff_adjointEigenEquation D hD z generator]
    exact (hclass generator).2 ⟨1, by simp⟩
  · exact adjointEigenEquation_iff_mem_span_of_dualWeak D hD z generator hclass

end RHBridge.GelfandTripleAdjoint
