/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreScaledL2

/-!
# Canonical parity coordinates on finite Legendre sections

The first `2m` normalized scaled Legendre vectors are reordered into their
even and odd degree blocks.  This file constructs their canonical Hilbert
coefficients, proves the exact finite-span Parseval identity, and represents
a symmetric parity-preserving bilinear form by its actual basis-entry
matrices.  Thus coordinate isometry and matrix representation need not be
supplied as independent analytic hypotheses.
-/

namespace LegendreParityCoordinates

open Matrix
open scoped RealInnerProductSpace

noncomputable section

/-- Parity ordering of `Fin (m + m)`: the left block is `0,2,...` and the
right block is `1,3,...`. -/
def parityIndex (m : ℕ) : Fin m ⊕ Fin m → Fin (m + m)
  | Sum.inl i => ⟨2 * i.val, by omega⟩
  | Sum.inr i => ⟨2 * i.val + 1, by omega⟩

theorem parityIndex_bijective (m : ℕ) : Function.Bijective (parityIndex m) := by
  constructor
  · intro i j hij
    cases i with
    | inl i =>
      cases j with
      | inl j =>
        congr 1
        apply Fin.ext
        have h := Fin.ext_iff.mp hij
        simp [parityIndex] at h
        omega
      | inr j =>
        have h := Fin.ext_iff.mp hij
        simp [parityIndex] at h
        omega
    | inr i =>
      cases j with
      | inl j =>
        have h := Fin.ext_iff.mp hij
        simp [parityIndex] at h
        omega
      | inr j =>
        congr 1
        apply Fin.ext
        have h := Fin.ext_iff.mp hij
        simp [parityIndex] at h
        omega
  · intro k
    by_cases hk : k.val % 2 = 0
    · refine ⟨Sum.inl ⟨k.val / 2, by omega⟩, ?_⟩
      apply Fin.ext
      simp [parityIndex]
      omega
    · refine ⟨Sum.inr ⟨k.val / 2, by omega⟩, ?_⟩
      apply Fin.ext
      simp [parityIndex]
      omega

def parityEquiv (m : ℕ) : Fin m ⊕ Fin m ≃ Fin (m + m) :=
  Equiv.ofBijective (parityIndex m) (parityIndex_bijective m)

@[simp] theorem parityEquiv_inl_val (m : ℕ) (i : Fin m) :
    (parityEquiv m (Sum.inl i)).val = 2 * i.val := rfl

@[simp] theorem parityEquiv_inr_val (m : ℕ) (i : Fin m) :
    (parityEquiv m (Sum.inr i)).val = 2 * i.val + 1 := rfl

theorem sum_fin_even_odd {A : Type*} [AddCommMonoid A]
    (m : ℕ) (f : Fin (m + m) → A) :
    (∑ k, f k) =
      (∑ i : Fin m, f ⟨2 * i.val, by omega⟩) +
        ∑ i : Fin m, f ⟨2 * i.val + 1, by omega⟩ := by
  rw [← (parityEquiv m).sum_comp f, Fintype.sum_sum_type]
  rfl

/-- Canonical even-degree Hilbert coordinates. -/
def evenCoord (a : ℝ) (m : ℕ) (x : LegendreScaledL2.IntervalL2 a)
    (i : Fin m) : ℝ :=
  inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val)) x

/-- Canonical odd-degree Hilbert coordinates. -/
def oddCoord (a : ℝ) (m : ℕ) (x : LegendreScaledL2.IntervalL2 a)
    (i : Fin m) : ℝ :=
  inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1)) x

/-- Exact even/odd expansion of a vector in the first `2m` Legendre modes. -/
theorem finiteLegendre_expansion_parity
    (a : ℝ) (ha : 0 < a) (m : ℕ)
    (u : LegendreScaledL2.IntervalL2 a)
    (hu : u ∈ LegendreScaledL2.finiteLegendreSubspace a (m + m)) :
    u =
      (∑ i : Fin m, evenCoord a m u i •
        LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val)) +
      ∑ i : Fin m, oddCoord a m u i •
        LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1) := by
  have hproj :
      LegendreScaledL2.finiteLegendreProjection a (m + m) u = u := by
    rw [← LegendreScaledL2.finiteLegendreSubspace_starProjection a ha]
    exact Submodule.starProjection_eq_self_iff.mpr hu
  calc
    u = LegendreScaledL2.finiteLegendreProjection a (m + m) u := hproj.symm
    _ = ∑ k : Fin (m + m),
          inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a k.val) u •
            LegendreScaledL2.scaledNormalizedLegendreL2 a k.val := by
      unfold LegendreScaledL2.finiteLegendreProjection
      exact (Fin.sum_univ_eq_sum_range
        (fun k : ℕ ↦ inner ℝ
            (LegendreScaledL2.scaledNormalizedLegendreL2 a k) u •
              LegendreScaledL2.scaledNormalizedLegendreL2 a k)
        (m + m)).symm
    _ = _ := by
      rw [sum_fin_even_odd]
      rfl

/-- Exact finite-span Parseval identity in parity-reordered coordinates. -/
theorem norm_sq_eq_evenCoord_dot_add_oddCoord_dot
    (a : ℝ) (ha : 0 < a) (m : ℕ)
    (u : LegendreScaledL2.IntervalL2 a)
    (hu : u ∈ LegendreScaledL2.finiteLegendreSubspace a (m + m)) :
    ‖u‖ ^ 2 = evenCoord a m u ⬝ᵥ evenCoord a m u +
      oddCoord a m u ⬝ᵥ oddCoord a m u := by
  have hres := LegendreScaledL2.norm_finiteLegendreProjection_residual_sq
    a ha (m + m) u
  have hproj : LegendreScaledL2.finiteLegendreProjection a (m + m) u = u := by
    rw [← LegendreScaledL2.finiteLegendreSubspace_starProjection a ha]
    exact Submodule.starProjection_eq_self_iff.mpr hu
  rw [hproj, sub_self, norm_zero, zero_pow (by norm_num)] at hres
  have hsum :
      (∑ k ∈ Finset.range (m + m),
          ‖inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a k) u‖ ^ 2) =
        evenCoord a m u ⬝ᵥ evenCoord a m u +
          oddCoord a m u ⬝ᵥ oddCoord a m u := by
    rw [← Fin.sum_univ_eq_sum_range, sum_fin_even_odd]
    simp only [Real.norm_eq_abs, sq_abs]
    simp [dotProduct, evenCoord, oddCoord, pow_two]
  rw [hsum] at hres
  linarith

/-- The actual even-even basis-entry matrix of `B`, transposed to match
`Matrix.mulVec`'s row convention.  For symmetric `B` the transpose is
invisible. -/
def evenMatrix (a : ℝ) (B : LegendreScaledL2.IntervalL2 a →ₗ[ℝ]
    LegendreScaledL2.IntervalL2 a →ₗ[ℝ] ℝ) (m : ℕ) :
    Matrix (Fin m) (Fin m) ℝ := fun i j ↦
  B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val))
    (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val))

/-- The actual odd-odd basis-entry matrix of `B`, with the same row
convention as `evenMatrix`. -/
def oddMatrix (a : ℝ) (B : LegendreScaledL2.IntervalL2 a →ₗ[ℝ]
    LegendreScaledL2.IntervalL2 a →ₗ[ℝ] ℝ) (m : ℕ) :
    Matrix (Fin m) (Fin m) ℝ := fun i j ↦
  B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1))
    (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1))

/-- For a symmetric form, `evenMatrix` has the conventional `(i,j)` basis
entry despite its implementation-level transpose. -/
theorem evenMatrix_apply_of_symmetric
    (a : ℝ) (B : LegendreScaledL2.IntervalL2 a →ₗ[ℝ]
      LegendreScaledL2.IntervalL2 a →ₗ[ℝ] ℝ) (m : ℕ)
    (hsymm : ∀ x y, B x y = B y x) (i j : Fin m) :
    evenMatrix a B m i j =
      B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) := by
  exact hsymm _ _

/-- Conventional basis-entry form of `oddMatrix` for symmetric forms. -/
theorem oddMatrix_apply_of_symmetric
    (a : ℝ) (B : LegendreScaledL2.IntervalL2 a →ₗ[ℝ]
      LegendreScaledL2.IntervalL2 a →ₗ[ℝ] ℝ) (m : ℕ)
    (hsymm : ∀ x y, B x y = B y x) (i j : Fin m) :
    oddMatrix a B m i j =
      B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1))
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) := by
  exact hsymm _ _

/-- A symmetric form with zero even-odd basis entries is represented on the
finite Legendre section by its canonical two parity-block matrices. -/
theorem bilinear_eq_parity_matrices
    (a : ℝ) (B : LegendreScaledL2.IntervalL2 a →ₗ[ℝ]
      LegendreScaledL2.IntervalL2 a →ₗ[ℝ] ℝ)
    (ha : 0 < a) (m : ℕ)
    (hsymm : ∀ x y, B x y = B y x)
    (hparity : ∀ i j : Fin m,
      B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val))
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) = 0)
    (u : LegendreScaledL2.IntervalL2 a)
    (hu : u ∈ LegendreScaledL2.finiteLegendreSubspace a (m + m)) :
    B u u = evenCoord a m u ⬝ᵥ evenMatrix a B m *ᵥ evenCoord a m u +
      oddCoord a m u ⬝ᵥ oddMatrix a B m *ᵥ oddCoord a m u := by
  conv_lhs => rw [finiteLegendre_expansion_parity a ha m u hu]
  simp only [map_add, map_sum, LinearMap.map_smul, smul_eq_mul]
  simp only [dotProduct, Matrix.mulVec, evenCoord, oddCoord, evenMatrix, oddMatrix]
  have hparity' : ∀ i j : Fin m,
      B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1))
        (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) = 0 := by
    intro i j
    rw [hsymm]
    exact hparity j i
  simp only [LinearMap.add_apply, LinearMap.sum_apply, LinearMap.smul_apply,
    smul_eq_mul]
  simp_rw [hparity, hparity']
  simp only [mul_zero, Finset.sum_const_zero, add_zero, zero_add]
  have hmulEven (i j : Fin m) :
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) u *
          B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val)) =
        B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val)) *
          inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) u := by
    ring
  have hmulOdd (i j : Fin m) :
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) u *
          B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1)) =
        B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1)) *
          inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) u := by
    ring
  have hevenSum (i : Fin m) :
      (∑ j : Fin m,
        inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) u *
          B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val))) =
      ∑ j : Fin m,
        B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val)) *
          inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val)) u := by
    apply Finset.sum_congr rfl
    intro j _
    exact hmulEven i j
  have hoddSum (i : Fin m) :
      (∑ j : Fin m,
        inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) u *
          B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1))) =
      ∑ j : Fin m,
        B (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1))
            (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i.val + 1)) *
          inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j.val + 1)) u := by
    apply Finset.sum_congr rfl
    intro j _
    exact hmulOdd i j
  simp_rw [hevenSum, hoddSum]

end

end LegendreParityCoordinates
