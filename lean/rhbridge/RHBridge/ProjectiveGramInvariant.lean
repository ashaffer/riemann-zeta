/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.LinearMap
import Mathlib.Analysis.Complex.Norm

/-!
# Projective Gram invariants of one-dimensional deficiency spaces

Suppose a complex linear isometry carries each vector in one labelled family
to a scalar multiple of the vector with the same label in a second family.
Its preservation of inner products forces the two Gram kernels to differ by
a diagonal gauge.  After the vectors are normalized, the scalars are phases;
hence every pairwise Gram magnitude and every Bargmann triple product is
preserved.

This gives a finite necessary test for a proposed parameter-preserving unitary
intertwiner of two adjoints with one-dimensional eigenspaces.  The theorem is
pure Hilbert-space algebra: it does not assume that a particular Galerkin
matrix converges to an unbounded operator, nor does it infer an intertwiner
from agreement of finitely many invariants.
-/

noncomputable section

namespace RHBridge.ProjectiveGramInvariant

open scoped ComplexConjugate

variable {ι H K : Type*}
variable [SeminormedAddCommGroup H] [InnerProductSpace ℂ H]
variable [SeminormedAddCommGroup K] [InnerProductSpace ℂ K]

/-- The Gram kernel of a labelled vector family. -/
def gram (v : ι → H) (i j : ι) : ℂ :=
  inner ℂ (v i) (v j)

/-- Two kernels are related by the diagonal scalar gauge `c` when the scalar
at the first index is conjugated and the scalar at the second is not.  This
orientation is forced by mathlib's convention that `inner` is conjugate
linear in its first argument. -/
def IsDiagonalGauge (G F : ι → ι → ℂ) (c : ι → ℂ) : Prop :=
  ∀ i j, G i j = conj (c i) * c j * F i j

/-- A line-preserving complex linear isometry forces a diagonal-gauge
relation between the two Gram kernels.  Surjectivity is not needed. -/
theorem gram_isDiagonalGauge_of_linearIsometry
    (U : H →ₗᵢ[ℂ] K) (v : ι → H) (w : ι → K) (c : ι → ℂ)
    (hmap : ∀ i, U (v i) = c i • w i) :
    IsDiagonalGauge (gram v) (gram w) c := by
  intro i j
  have hinner := U.inner_map_map (v i) (v j)
  rw [hmap i, hmap j, inner_smul_left, inner_smul_right] at hinner
  simpa only [gram, mul_assoc] using hinner.symm

/-- If both representatives of a mapped line have norm one, its comparison
scalar has norm one. -/
theorem norm_scalar_eq_one_of_normalized
    (U : H →ₗᵢ[ℂ] K) (v : ι → H) (w : ι → K) (c : ι → ℂ)
    (hmap : ∀ i, U (v i) = c i • w i)
    (hv : ∀ i, ‖v i‖ = 1) (hw : ∀ i, ‖w i‖ = 1) (i : ι) :
    ‖c i‖ = 1 := by
  calc
    ‖c i‖ = ‖c i‖ * ‖w i‖ := by rw [hw i, mul_one]
    _ = ‖c i • w i‖ := (norm_smul (c i) (w i)).symm
    _ = ‖U (v i)‖ := by rw [hmap i]
    _ = ‖v i‖ := U.norm_map (v i)
    _ = 1 := hv i

/-- The squared modulus of every Gram entry is invariant under a unitary
diagonal gauge. -/
theorem normSq_eq_of_isDiagonalGauge
    {G F : ι → ι → ℂ} {c : ι → ℂ}
    (hgauge : IsDiagonalGauge G F c)
    (hphase : ∀ i, ‖c i‖ = 1) (i j : ι) :
    Complex.normSq (G i j) = Complex.normSq (F i j) := by
  rw [hgauge i j, Complex.normSq_mul, Complex.normSq_mul,
    Complex.normSq_conj, Complex.normSq_eq_norm_sq,
    Complex.normSq_eq_norm_sq, hphase i, hphase j]
  ring

/-- Pairwise projective Gram magnitudes are a necessary invariant of a
normalized, line-preserving linear isometry. -/
theorem gram_normSq_eq_of_normalized_linearIsometry
    (U : H →ₗᵢ[ℂ] K) (v : ι → H) (w : ι → K) (c : ι → ℂ)
    (hmap : ∀ i, U (v i) = c i • w i)
    (hv : ∀ i, ‖v i‖ = 1) (hw : ∀ i, ‖w i‖ = 1) (i j : ι) :
    Complex.normSq (gram v i j) = Complex.normSq (gram w i j) := by
  apply normSq_eq_of_isDiagonalGauge
    (gram_isDiagonalGauge_of_linearIsometry U v w c hmap)
  exact fun k ↦ norm_scalar_eq_one_of_normalized U v w c hmap hv hw k

/-- A diagonal gauge by phases preserves every cyclic triple product.  These
are the Bargmann invariants, which retain phase information not visible in
pairwise magnitudes. -/
theorem bargmannTriple_eq_of_isDiagonalGauge
    {G F : ι → ι → ℂ} {c : ι → ℂ}
    (hgauge : IsDiagonalGauge G F c)
    (hphase : ∀ i, ‖c i‖ = 1) (i j k : ι) :
    G i j * G j k * G k i = F i j * F j k * F k i := by
  have hi : conj (c i) * c i = 1 := by
    rw [← Complex.normSq_eq_conj_mul_self,
      Complex.normSq_eq_norm_sq, hphase i]
    norm_num
  have hj : conj (c j) * c j = 1 := by
    rw [← Complex.normSq_eq_conj_mul_self,
      Complex.normSq_eq_norm_sq, hphase j]
    norm_num
  have hk : conj (c k) * c k = 1 := by
    rw [← Complex.normSq_eq_conj_mul_self,
      Complex.normSq_eq_norm_sq, hphase k]
    norm_num
  rw [hgauge i j, hgauge j k, hgauge k i]
  calc
    (conj (c i) * c j * F i j) *
          (conj (c j) * c k * F j k) *
          (conj (c k) * c i * F k i) =
        (conj (c i) * c i) * (conj (c j) * c j) *
          (conj (c k) * c k) * (F i j * F j k * F k i) := by ring
    _ = F i j * F j k * F k i := by rw [hi, hj, hk]; ring

/-- Bargmann triple products are therefore necessary invariants of a
normalized, line-preserving linear isometry. -/
theorem gram_bargmannTriple_eq_of_normalized_linearIsometry
    (U : H →ₗᵢ[ℂ] K) (v : ι → H) (w : ι → K) (c : ι → ℂ)
    (hmap : ∀ i, U (v i) = c i • w i)
    (hv : ∀ i, ‖v i‖ = 1) (hw : ∀ i, ‖w i‖ = 1) (i j k : ι) :
    gram v i j * gram v j k * gram v k i =
      gram w i j * gram w j k * gram w k i := by
  apply bargmannTriple_eq_of_isDiagonalGauge
    (gram_isDiagonalGauge_of_linearIsometry U v w c hmap)
  exact fun l ↦ norm_scalar_eq_one_of_normalized U v w c hmap hv hw l

end RHBridge.ProjectiveGramInvariant
