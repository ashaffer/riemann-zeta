/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreScaled
import LegendreL2
import HilbertBasisTail

/-! # Fourier--Legendre bases on arbitrary real intervals

For `b < c`, translate the symmetric interval of radius `(c-b)/2` by the
center `(b+c)/2`.  Orthogonality is transported by the interval-integral
translation identity; completeness is then proved directly from polynomial
density.  Thus this is a basis of the actual subtype `L²([b,c])`, not an alias
for a symmetric interval.

The current proof reuses the symmetric polynomial normalization but repeats
the short polynomial-density and Hilbert-basis packaging for the new subtype.
A future affine `L²` isometry could remove that duplication; keeping it
explicit here avoids making the public theorem depend on an additional
transport API.
-/

namespace LegendreIntervalL2

open Polynomial
open scoped ENNReal InnerProductSpace

/-- The compact interval `[b,c]`. -/
abbrev Interval (b c : ℝ) := Set.Icc b c

/-- Lebesgue measure transported to the interval subtype. -/
noncomputable def intervalMeasure (b c : ℝ) :
    MeasureTheory.Measure (Interval b c) :=
  MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume

/-- The real Hilbert space `L²([b,c])`. -/
noncomputable abbrev IntervalL2 (b c : ℝ) :=
  MeasureTheory.Lp ℝ 2 (intervalMeasure b c)

instance (b c : ℝ) : MeasureTheory.IsFiniteMeasure (intervalMeasure b c) := by
  constructor
  rw [intervalMeasure, comap_subtype_coe_apply measurableSet_Icc]
  rw [Set.image_univ, Subtype.range_coe_subtype, Set.setOf_mem_eq]
  simp

/-- Center of `[b,c]`. -/
noncomputable def center (b c : ℝ) : ℝ := (b + c) / 2

/-- Half-length of `[b,c]`. -/
noncomputable def radius (b c : ℝ) : ℝ := (c - b) / 2

theorem radius_pos {b c : ℝ} (hbc : b < c) : 0 < radius b c := by
  unfold radius
  linarith

theorem left_sub_center (b c : ℝ) : b - center b c = -radius b c := by
  unfold center radius
  ring

theorem right_sub_center (b c : ℝ) : c - center b c = radius b c := by
  unfold center radius
  ring

/-- The normalized Legendre polynomial on `[b,c]`, obtained by translating
the normalized polynomial on the symmetric interval of radius `(c-b)/2`. -/
noncomputable def normalizedLegendrePolynomial
    (b c : ℝ) (n : ℕ) : ℝ[X] :=
  (LegendreScaled.scaledNormalizedPlainLegendre (radius b c) n).comp
    (X - C (center b c))

@[simp] theorem eval_normalizedLegendrePolynomial
    (b c x : ℝ) (n : ℕ) :
    (normalizedLegendrePolynomial b c n).eval x =
      (LegendreScaled.scaledNormalizedPlainLegendre (radius b c) n).eval
        (x - center b c) := by
  simp [normalizedLegendrePolynomial]

/-- Translation carries the symmetric Legendre pairing exactly to `[b,c]`. -/
theorem normalizedLegendrePolynomial_pair
    (b c : ℝ) (hbc : b < c) (m n : ℕ) :
    LegendreOrthogonality.polynomialPairIntegral
        (normalizedLegendrePolynomial b c m)
        (normalizedLegendrePolynomial b c n) b c =
      if m = n then 1 else 0 := by
  let r := radius b c
  let d := center b c
  let f : ℝ → ℝ := fun x ↦
    (LegendreScaled.scaledNormalizedPlainLegendre r m).eval x *
      (LegendreScaled.scaledNormalizedPlainLegendre r n).eval x
  have hshift :
      (∫ x in b..c, f (x - d)) = ∫ x in b - d..c - d, f x :=
    intervalIntegral.integral_comp_sub_right f d
  rw [LegendreOrthogonality.polynomialPairIntegral]
  calc
    (∫ x in b..c,
        (normalizedLegendrePolynomial b c m).eval x *
          (normalizedLegendrePolynomial b c n).eval x) =
        ∫ x in b..c, f (x - d) := by
          apply intervalIntegral.integral_congr
          intro x _
          simp [f, d, r]
    _ = ∫ x in b - d..c - d, f x := hshift
    _ = LegendreOrthogonality.polynomialPairIntegral
          (LegendreScaled.scaledNormalizedPlainLegendre r m)
          (LegendreScaled.scaledNormalizedPlainLegendre r n) (-r) r := by
            rw [LegendreOrthogonality.polynomialPairIntegral]
            rw [show b - d = -r by
                dsimp [d, r]
                exact left_sub_center b c,
              show c - d = r by
                dsimp [d, r]
                exact right_sub_center b c]
    _ = if m = n then 1 else 0 :=
      LegendreScaled.scaledNormalizedPlainLegendre_orthonormal
        r (by simpa [r] using radius_pos hbc) m n

/-- Send a polynomial to its class in `L²([b,c])`. -/
noncomputable def polynomialToL2 (b c : ℝ) :
    ℝ[X] →ₗ[ℝ] IntervalL2 b c :=
  (ContinuousMap.toLp 2 (intervalMeasure b c) ℝ).toLinearMap.comp
    (Polynomial.toContinuousMapOnAlgHom (Interval b c)).toLinearMap

@[simp] theorem polynomialToL2_apply (b c : ℝ) (p : ℝ[X]) :
    polynomialToL2 b c p =
      ContinuousMap.toLp 2 (intervalMeasure b c) ℝ
        (p.toContinuousMapOn (Interval b c)) := rfl

/-- The normalized interval Legendre polynomials as vectors in `L²([b,c])`. -/
noncomputable def normalizedLegendreL2
    (b c : ℝ) (n : ℕ) : IntervalL2 b c :=
  polynomialToL2 b c (normalizedLegendrePolynomial b c n)

/-- Polynomial `L²` inner products are ordinary interval pairings. -/
theorem inner_polynomialToL2
    (b c : ℝ) (hbc : b ≤ c) (p q : ℝ[X]) :
    ⟪polynomialToL2 b c p, polynomialToL2 b c q⟫_ℝ =
      LegendreOrthogonality.polynomialPairIntegral p q b c := by
  rw [polynomialToL2_apply, polynomialToL2_apply,
    MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc b c,
      q.eval (x : ℝ) * p.eval (x : ℝ)
        ∂(MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume)) = _
  rw [MeasureTheory.integral_subtype_comap
    (s := Set.Icc b c) (μ := MeasureTheory.volume)
    measurableSet_Icc (fun x : ℝ ↦ q.eval x * p.eval x)]
  rw [LegendreOrthogonality.polynomialPairIntegral,
    intervalIntegral.integral_of_le hbc,
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  simp [mul_comm]

/-! ## Algebraic spanning and density -/

/-- The interval-normalized family contains exactly one polynomial of every
degree. -/
noncomputable def normalizedLegendreSequence
    (b c : ℝ) (hbc : b < c) : Polynomial.Sequence ℝ where
  elems' := normalizedLegendrePolynomial b c
  degree_eq' n := by
    rw [normalizedLegendrePolynomial,
      Polynomial.degree_comp (by
        rw [Polynomial.degree_X_sub_C]
        decide)]
    have hr0 : radius b c ≠ 0 := ne_of_gt (radius_pos hbc)
    have hsqrt : Real.sqrt (radius b c) ≠ 0 :=
      ne_of_gt (Real.sqrt_pos.2 (radius_pos hbc))
    have hnorm :
        Real.sqrt ((2 * (n : ℝ) + 1) / 2) ≠ 0 := by positivity
    have hnat :
        (LegendreScaled.scaledNormalizedPlainLegendre
          (radius b c) n).natDegree = n := by
      rw [LegendreScaled.scaledNormalizedPlainLegendre,
        Polynomial.natDegree_C_mul (inv_ne_zero hsqrt),
        Polynomial.natDegree_comp,
        LegendreOrthogonality.normalizedPlainLegendre,
        Polynomial.natDegree_C_mul hnorm,
        LegendreOrthogonality.natDegree_plainLegendre,
        Polynomial.natDegree_C_mul (inv_ne_zero hr0),
        Polynomial.natDegree_X]
      omega
    have hne :
        LegendreScaled.scaledNormalizedPlainLegendre (radius b c) n ≠ 0 := by
      intro hzero
      have hpair :=
        LegendreScaled.scaledNormalizedPlainLegendre_pair_self
          (radius b c) (radius_pos hbc) n
      rw [hzero, LegendreOrthogonality.polynomialPairIntegral] at hpair
      simp at hpair
    rw [Polynomial.degree_eq_natDegree hne, hnat,
      Polynomial.degree_X_sub_C, mul_one]

@[simp] theorem normalizedLegendreSequence_apply
    (b c : ℝ) (hbc : b < c) (n : ℕ) :
    normalizedLegendreSequence b c hbc n =
      normalizedLegendrePolynomial b c n := rfl

/-- The arbitrary-interval normalized Legendre family spans all real
polynomials. -/
theorem normalizedLegendrePolynomial_span
    (b c : ℝ) (hbc : b < c) :
    Submodule.span ℝ (Set.range (normalizedLegendrePolynomial b c)) = ⊤ := by
  change Submodule.span ℝ
    (Set.range (normalizedLegendreSequence b c hbc : ℕ → ℝ[X])) = ⊤
  exact (normalizedLegendreSequence b c hbc).span (fun n ↦ by
    rw [isUnit_iff_ne_zero]
    exact Polynomial.leadingCoeff_ne_zero.mpr
      ((normalizedLegendreSequence b c hbc).ne_zero n))

/-- Polynomial evaluation is dense in the continuous functions on `[b,c]`. -/
theorem polynomialToContinuousMap_denseRange (b c : ℝ) :
    DenseRange (Polynomial.toContinuousMapOnAlgHom (Interval b c)) := by
  rw [DenseRange, ← polynomialFunctions_coe]
  rw [dense_iff_closure_eq,
    ← Subalgebra.topologicalClosure_coe,
    polynomialFunctions_closure_eq_top]
  rfl

/-- Polynomial classes are dense in `L²([b,c])`. -/
theorem polynomialToL2_denseRange (b c : ℝ) :
    DenseRange (polynomialToL2 b c) := by
  have hcontinuous :
      DenseRange
        (ContinuousMap.toLp 2 (intervalMeasure b c) ℝ :
          C(Interval b c, ℝ) →L[ℝ] IntervalL2 b c) :=
    ContinuousMap.toLp_denseRange ℝ (intervalMeasure b c) ℝ (by norm_num)
  have h := hcontinuous.comp (polynomialToContinuousMap_denseRange b c)
    (ContinuousMap.toLp 2 (intervalMeasure b c) ℝ).continuous
  simpa [polynomialToL2, Function.comp_def] using h

/-! ## Orthonormality and completeness -/

theorem inner_normalizedLegendreL2
    (b c : ℝ) (hbc : b < c) (m n : ℕ) :
    ⟪normalizedLegendreL2 b c m, normalizedLegendreL2 b c n⟫_ℝ =
      if m = n then 1 else 0 := by
  rw [normalizedLegendreL2, normalizedLegendreL2,
    inner_polynomialToL2 b c hbc.le]
  exact normalizedLegendrePolynomial_pair b c hbc m n

/-- The arbitrary-interval Legendre vectors are orthonormal. -/
theorem normalizedLegendreL2_orthonormal
    (b c : ℝ) (hbc : b < c) :
    Orthonormal ℝ (normalizedLegendreL2 b c) := by
  rw [orthonormal_iff_ite]
  exact inner_normalizedLegendreL2 b c hbc

theorem normalizedLegendreL2_span_eq_polynomial_range
    (b c : ℝ) (hbc : b < c) :
    Submodule.span ℝ (Set.range (normalizedLegendreL2 b c)) =
      LinearMap.range (polynomialToL2 b c) := by
  rw [← Submodule.map_top (polynomialToL2 b c),
    ← normalizedLegendrePolynomial_span b c hbc,
    Submodule.map_span]
  congr 1
  rw [← Set.range_comp]
  rfl

/-- Completeness of the arbitrary-interval Legendre family. -/
theorem normalizedLegendreL2_dense_span
    (b c : ℝ) (hbc : b < c) :
    (Submodule.span ℝ
      (Set.range (normalizedLegendreL2 b c))).topologicalClosure = ⊤ := by
  rw [normalizedLegendreL2_span_eq_polynomial_range b c hbc]
  apply Submodule.dense_iff_topologicalClosure_eq_top.mp
  simpa only [LinearMap.coe_range, DenseRange] using
    polynomialToL2_denseRange b c

/-- Complete normalized Legendre Hilbert basis of `L²([b,c])`. -/
noncomputable def normalizedLegendreHilbertBasis
    (b c : ℝ) (hbc : b < c) : HilbertBasis ℕ ℝ (IntervalL2 b c) :=
  HilbertBasis.mk (normalizedLegendreL2_orthonormal b c hbc)
    (normalizedLegendreL2_dense_span b c hbc).ge

@[simp] theorem normalizedLegendreHilbertBasis_apply
    (b c : ℝ) (hbc : b < c) (n : ℕ) :
    normalizedLegendreHilbertBasis b c hbc n =
      normalizedLegendreL2 b c n := by
  exact congrFun
    (HilbertBasis.coe_mk (normalizedLegendreL2_orthonormal b c hbc)
      (normalizedLegendreL2_dense_span b c hbc).ge) n

/-! ## Human-facing arbitrary-interval API -/

namespace FourierLegendre

/-- The complete normalized Legendre basis of real `L²([b,c])`. -/
noncomputable abbrev basis (b c : ℝ) (hbc : b < c) :
    HilbertBasis ℕ ℝ (IntervalL2 b c) :=
  normalizedLegendreHilbertBasis b c hbc

/-- The unitary Fourier--Legendre coefficient transform on `[b,c]`. -/
noncomputable def transform (b c : ℝ) (hbc : b < c) :=
  (basis b c hbc).repr

@[simp] theorem basis_apply (b c : ℝ) (hbc : b < c) (n : ℕ) :
    basis b c hbc n = normalizedLegendreL2 b c n :=
  normalizedLegendreHilbertBasis_apply b c hbc n

@[simp] theorem transform_apply (b c : ℝ) (hbc : b < c)
    (x : IntervalL2 b c) (n : ℕ) :
    transform b c hbc x n =
      inner ℝ (normalizedLegendreL2 b c n) x := by
  change (basis b c hbc).repr x n = _
  rw [(basis b c hbc).repr_apply_apply, basis_apply]

/-- Parseval's identity on an arbitrary nondegenerate interval. -/
theorem parseval (b c : ℝ) (hbc : b < c) (x : IntervalL2 b c) :
    ∑' n : ℕ, ‖inner ℝ (normalizedLegendreL2 b c n) x‖ ^ 2 =
      ‖x‖ ^ 2 := by
  simpa using HilbertBasisTail.tsum_sq_norm_inner (basis b c hbc) x

/-- The first `m` terms of the arbitrary-interval Fourier--Legendre
expansion. -/
noncomputable def finiteProjection
    (b c : ℝ) (m : ℕ) (x : IntervalL2 b c) : IntervalL2 b c :=
  ∑ k ∈ Finset.range m,
    inner ℝ (normalizedLegendreL2 b c k) x •
      normalizedLegendreL2 b c k

/-- Subspace generated by the first `m` interval Legendre modes. -/
noncomputable def finiteSubspace
    (b c : ℝ) (m : ℕ) : Submodule ℝ (IntervalL2 b c) :=
  Submodule.span ℝ
    (normalizedLegendreL2 b c '' (Finset.range m : Set ℕ))

noncomputable instance finiteSubspace_finiteDimensional
    (b c : ℝ) (m : ℕ) :
    FiniteDimensional ℝ (finiteSubspace b c m) := by
  rw [finiteSubspace]
  exact FiniteDimensional.span_of_finite ℝ
    ((Finset.finite_toSet (Finset.range m)).image
      (normalizedLegendreL2 b c))

noncomputable instance finiteSubspace_completeSpace
    (b c : ℝ) (m : ℕ) : CompleteSpace (finiteSubspace b c m) :=
  FiniteDimensional.complete ℝ _

/-- The explicit finite Fourier--Legendre sum is the canonical projection. -/
theorem finiteSubspace_starProjection
    (b c : ℝ) (hbc : b < c) (m : ℕ) (x : IntervalL2 b c) :
    (finiteSubspace b c m).starProjection x = finiteProjection b c m x := by
  classical
  let B := OrthonormalBasis.span
    (normalizedLegendreL2_orthonormal b c hbc) (Finset.range m)
  have h := congrArg Subtype.val
    (B.orthogonalProjectionOnto_apply_eq_sum x)
  calc
    (finiteSubspace b c m).starProjection x =
        ∑ k : ↑(Finset.range m),
          inner ℝ (normalizedLegendreL2 b c (k : ℕ)) x •
            normalizedLegendreL2 b c (k : ℕ) := by
      simpa [B, finiteSubspace] using h
    _ = finiteProjection b c m x := by
      simpa [finiteProjection] using
        (Finset.sum_attach (Finset.range m)
          (fun k ↦ inner ℝ (normalizedLegendreL2 b c k) x •
            normalizedLegendreL2 b c k))

/-- Exact finite-section projection error on `[b,c]`. -/
theorem projection_error
    (b c : ℝ) (hbc : b < c) (m : ℕ) (x : IntervalL2 b c) :
    ‖x - (finiteSubspace b c m).starProjection x‖ ^ 2 =
      ∑' n : ℕ,
        ‖inner ℝ (normalizedLegendreL2 b c (m + n)) x‖ ^ 2 := by
  rw [finiteSubspace_starProjection b c hbc]
  have htail := HilbertBasisTail.tsum_nat_add_sq_norm_inner_eq_sub_sum
    (basis b c hbc) x m
  have hresidual :
      ‖x - finiteProjection b c m x‖ ^ 2 =
        ‖x‖ ^ 2 - ∑ k ∈ Finset.range m,
          ‖inner ℝ (normalizedLegendreL2 b c k) x‖ ^ 2 := by
    have h₂ :
        (∑ i ∈ Finset.range m, ∑ j ∈ Finset.range m,
            inner ℝ (normalizedLegendreL2 b c i) x *
              inner ℝ x (normalizedLegendreL2 b c j) *
                inner ℝ (normalizedLegendreL2 b c j)
                  (normalizedLegendreL2 b c i)) =
          (∑ k ∈ Finset.range m,
            inner ℝ (normalizedLegendreL2 b c k) x *
              inner ℝ x (normalizedLegendreL2 b c k)) := by
      classical
      exact (normalizedLegendreL2_orthonormal b c hbc).inner_left_right_finset
    have h₃ : ∀ z : ℝ,
        RCLike.re (z * starRingEnd ℝ z) = ‖z‖ ^ 2 := by
      intro z
      simp [pow_two]
    rw [finiteProjection, @norm_sub_sq ℝ, sub_add]
    simp only [@InnerProductSpace.norm_sq_eq_re_inner ℝ (IntervalL2 b c),
      inner_sum, sum_inner]
    simp only [inner_smul_right, two_mul, inner_smul_left,
      inner_conj_symm, ← mul_assoc, h₂, add_sub_cancel_right,
      sub_right_inj]
    simp only [map_sum, ← inner_conj_symm x, ← h₃]
  rw [hresidual]
  simpa using htail.symm

end FourierLegendre

end LegendreIntervalL2
