/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreOrthogonality
import HilbertBasisTail
import Mathlib.Algebra.Polynomial.Sequence
import Mathlib.Topology.ContinuousMap.Weierstrass
import Mathlib.MeasureTheory.Function.ContinuousMapDense
import Mathlib.MeasureTheory.Function.L2Space
import Mathlib.MeasureTheory.Measure.Restrict
import Mathlib.Analysis.InnerProductSpace.l2Space

/-!
# The Legendre Hilbert basis on `[-1,1]`

The normalized Legendre polynomials form a complete Hilbert basis of the real
`L²` space on `[-1,1]`.  This file also gives Parseval and exact finite-section
residual formulas.
-/

namespace LegendreL2

open Polynomial
open scoped ENNReal InnerProductSpace

/-- The compact interval on which the Legendre family is orthogonal. -/
abbrev Interval := Set.Icc (-1 : ℝ) 1

/-- Lebesgue measure transported to the subtype `[-1,1]`. -/
noncomputable def intervalMeasure : MeasureTheory.Measure Interval :=
  MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume

/-- The real Hilbert space `L²([-1,1])`. -/
noncomputable abbrev IntervalL2 :=
  MeasureTheory.Lp ℝ 2 intervalMeasure

instance : MeasureTheory.IsFiniteMeasure intervalMeasure := by
  constructor
  rw [intervalMeasure,
    comap_subtype_coe_apply
      measurableSet_Icc]
  rw [Set.image_univ, Subtype.range_coe_subtype, Set.setOf_mem_eq]
  simp

/-- Send a polynomial to its `L²([-1,1])` class. -/
noncomputable def polynomialToL2 : ℝ[X] →ₗ[ℝ] IntervalL2 :=
  (ContinuousMap.toLp 2 intervalMeasure ℝ).toLinearMap.comp
    (Polynomial.toContinuousMapOnAlgHom Interval).toLinearMap

@[simp] theorem polynomialToL2_apply (p : ℝ[X]) :
    polynomialToL2 p =
      ContinuousMap.toLp 2 intervalMeasure ℝ
        (p.toContinuousMapOn Interval) := rfl

/-- The normalized Legendre family, now bundled as vectors in the interval
`L²` space. -/
noncomputable def normalizedLegendreL2 (n : ℕ) : IntervalL2 :=
  polynomialToL2 (LegendreOrthogonality.normalizedPlainLegendre n)

/-- The `L²` inner product of two polynomial classes is their ordinary
interval pairing. -/
theorem inner_polynomialToL2 (p q : ℝ[X]) :
    ⟪polynomialToL2 p, polynomialToL2 q⟫_ℝ =
      LegendreOrthogonality.polynomialPairIntegral p q (-1) 1 := by
  rw [polynomialToL2_apply, polynomialToL2_apply,
    MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc (-1 : ℝ) 1,
      q.eval (x : ℝ) * p.eval (x : ℝ)
        ∂(MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume)) = _
  rw [MeasureTheory.integral_subtype_comap
    (s := Set.Icc (-1 : ℝ) 1) (μ := MeasureTheory.volume)
    measurableSet_Icc (fun x : ℝ ↦ q.eval x * p.eval x)]
  rw [LegendreOrthogonality.polynomialPairIntegral,
    intervalIntegral.integral_of_le (by norm_num : (-1 : ℝ) ≤ 1),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  simp [mul_comm]

/-! ## Algebraic spanning -/

/-- The normalized Legendre polynomials form a polynomial sequence: their
`n`th member has degree exactly `n`. -/
noncomputable def normalizedPlainLegendreSequence :
    Polynomial.Sequence ℝ where
  elems' := LegendreOrthogonality.normalizedPlainLegendre
  degree_eq' n := by
    have hsqrt : Real.sqrt ((2 * (n : ℝ) + 1) / 2) ≠ 0 := by
      positivity
    have hplain : LegendreRodrigues.plainLegendre n ≠ 0 := by
      apply Polynomial.leadingCoeff_ne_zero.mp
      rw [LegendreOrthogonality.leadingCoeff_plainLegendre]
      apply div_ne_zero
      · exact_mod_cast Nat.centralBinom_ne_zero n
      · positivity
    rw [LegendreOrthogonality.normalizedPlainLegendre,
      Polynomial.degree_C_mul hsqrt,
      Polynomial.degree_eq_natDegree hplain,
      LegendreOrthogonality.natDegree_plainLegendre]

@[simp] theorem normalizedPlainLegendreSequence_apply (n : ℕ) :
    normalizedPlainLegendreSequence n =
      LegendreOrthogonality.normalizedPlainLegendre n := rfl

/-- Algebraically, the normalized Legendre family spans every real
polynomial. -/
theorem normalizedPlainLegendre_span :
    Submodule.span ℝ
        (Set.range LegendreOrthogonality.normalizedPlainLegendre) = ⊤ := by
  change Submodule.span ℝ
    (Set.range (normalizedPlainLegendreSequence : ℕ → ℝ[X])) = ⊤
  exact normalizedPlainLegendreSequence.span (fun n ↦ by
      rw [isUnit_iff_ne_zero]
      exact Polynomial.leadingCoeff_ne_zero.mpr
        (normalizedPlainLegendreSequence.ne_zero n))

/-! ## Density in the interval `L²` space -/

/-- Weierstrass approximation, expressed as dense range of polynomial
evaluation into continuous functions on `[-1,1]`. -/
theorem polynomialToContinuousMap_denseRange :
    DenseRange (Polynomial.toContinuousMapOnAlgHom Interval) := by
  rw [DenseRange, ← polynomialFunctions_coe]
  rw [dense_iff_closure_eq,
    ← Subalgebra.topologicalClosure_coe,
    polynomialFunctions_closure_eq_top]
  rfl

/-- Polynomial classes are dense in `L²([-1,1])`. -/
theorem polynomialToL2_denseRange : DenseRange polynomialToL2 := by
  have hcontinuous :
      DenseRange
        (ContinuousMap.toLp 2 intervalMeasure ℝ :
          C(Interval, ℝ) →L[ℝ] IntervalL2) :=
    ContinuousMap.toLp_denseRange ℝ intervalMeasure ℝ (by norm_num)
  have h := hcontinuous.comp polynomialToContinuousMap_denseRange
    (ContinuousMap.toLp 2 intervalMeasure ℝ).continuous
  simpa [polynomialToL2, Function.comp_def] using h

/-! ## Orthonormality and completeness -/

theorem inner_normalizedLegendreL2 (m n : ℕ) :
    ⟪normalizedLegendreL2 m, normalizedLegendreL2 n⟫_ℝ =
      if m = n then 1 else 0 := by
  rw [normalizedLegendreL2, normalizedLegendreL2,
    inner_polynomialToL2]
  exact LegendreOrthogonality.normalizedPlainLegendre_orthonormal m n

/-- The normalized Legendre vectors are an orthonormal family in the
actual interval `L²` space. -/
theorem normalizedLegendreL2_orthonormal :
    Orthonormal ℝ normalizedLegendreL2 := by
  rw [orthonormal_iff_ite]
  exact inner_normalizedLegendreL2

/-- The algebraic span of the interval Legendre vectors is exactly the
range of all polynomial classes. -/
theorem normalizedLegendreL2_span_eq_polynomial_range :
    Submodule.span ℝ (Set.range normalizedLegendreL2) =
      LinearMap.range polynomialToL2 := by
  rw [← Submodule.map_top polynomialToL2,
    ← normalizedPlainLegendre_span,
    Submodule.map_span]
  congr 1
  rw [← Set.range_comp]
  rfl

/-- Completeness: the span of the normalized Legendre vectors is dense in
all of `L²([-1,1])`. -/
theorem normalizedLegendreL2_dense_span :
    (Submodule.span ℝ
      (Set.range normalizedLegendreL2)).topologicalClosure = ⊤ := by
  rw [normalizedLegendreL2_span_eq_polynomial_range]
  apply Submodule.dense_iff_topologicalClosure_eq_top.mp
  simpa only [LinearMap.coe_range, DenseRange] using
    polynomialToL2_denseRange

/-- The complete countable Hilbert basis furnished by the normalized
Legendre polynomials. -/
noncomputable def normalizedLegendreHilbertBasis :
    HilbertBasis ℕ ℝ IntervalL2 :=
  HilbertBasis.mk normalizedLegendreL2_orthonormal
    normalizedLegendreL2_dense_span.ge

@[simp] theorem normalizedLegendreHilbertBasis_apply (n : ℕ) :
    normalizedLegendreHilbertBasis n = normalizedLegendreL2 n := by
  exact congrFun
    (HilbertBasis.coe_mk normalizedLegendreL2_orthonormal
      normalizedLegendreL2_dense_span.ge) n

/-! ## Parseval and finite-section tails -/

/-- Parseval's identity for the complete interval Legendre family. -/
theorem hasSum_sq_norm_inner_normalizedLegendreL2 (x : IntervalL2) :
    HasSum
      (fun n : ℕ ↦ ‖inner ℝ (normalizedLegendreL2 n) x‖ ^ 2)
      (‖x‖ ^ 2) := by
  simpa using HilbertBasisTail.hasSum_sq_norm_inner
    normalizedLegendreHilbertBasis x

/-- `tsum` form of Parseval's identity. -/
theorem tsum_sq_norm_inner_normalizedLegendreL2 (x : IntervalL2) :
    ∑' n : ℕ, ‖inner ℝ (normalizedLegendreL2 n) x‖ ^ 2 =
      ‖x‖ ^ 2 :=
  (hasSum_sq_norm_inner_normalizedLegendreL2 x).tsum_eq

/-- The first `m` terms of the Fourier--Legendre projection. -/
noncomputable def finiteLegendreProjection (m : ℕ) (x : IntervalL2) :
    IntervalL2 :=
  ∑ k ∈ Finset.range m,
    inner ℝ (normalizedLegendreL2 k) x • normalizedLegendreL2 k

/-- The subspace generated by the first `m` interval Legendre modes. -/
noncomputable def finiteLegendreSubspace (m : ℕ) :
    Submodule ℝ IntervalL2 :=
  Submodule.span ℝ
    (normalizedLegendreL2 '' (Finset.range m : Set ℕ))

noncomputable instance finiteLegendreSubspace_finiteDimensional (m : ℕ) :
    FiniteDimensional ℝ (finiteLegendreSubspace m) := by
  rw [finiteLegendreSubspace]
  exact FiniteDimensional.span_of_finite ℝ
    ((Finset.finite_toSet (Finset.range m)).image
      normalizedLegendreL2)

noncomputable instance finiteLegendreSubspace_completeSpace (m : ℕ) :
    CompleteSpace (finiteLegendreSubspace m) :=
  FiniteDimensional.complete ℝ _

/-- The explicit finite Fourier--Legendre sum is the canonical orthogonal
projection onto the first `m` modes. -/
theorem finiteLegendreSubspace_starProjection (m : ℕ)
    (x : IntervalL2) :
    (finiteLegendreSubspace m).starProjection x =
      finiteLegendreProjection m x := by
  classical
  let b := OrthonormalBasis.span normalizedLegendreL2_orthonormal
    (Finset.range m)
  have h := congrArg Subtype.val
    (b.orthogonalProjectionOnto_apply_eq_sum x)
  calc
    (finiteLegendreSubspace m).starProjection x =
        ∑ k : ↑(Finset.range m),
          inner ℝ (normalizedLegendreL2 (k : ℕ)) x •
            normalizedLegendreL2 (k : ℕ) := by
      simpa [b, finiteLegendreSubspace] using h
    _ = finiteLegendreProjection m x := by
      simpa [finiteLegendreProjection] using
        (Finset.sum_attach (Finset.range m)
          (fun k ↦ inner ℝ (normalizedLegendreL2 k) x •
            normalizedLegendreL2 k))

/-- Exact Pythagorean energy identity for the finite Legendre projection. -/
theorem norm_finiteLegendreProjection_residual_sq (m : ℕ)
    (x : IntervalL2) :
    ‖x - finiteLegendreProjection m x‖ ^ 2 =
      ‖x‖ ^ 2 -
        ∑ k ∈ Finset.range m,
          ‖inner ℝ (normalizedLegendreL2 k) x‖ ^ 2 := by
  have h₂ :
      (∑ i ∈ Finset.range m, ∑ j ∈ Finset.range m,
          inner ℝ (normalizedLegendreL2 i) x *
            inner ℝ x (normalizedLegendreL2 j) *
              inner ℝ (normalizedLegendreL2 j)
                (normalizedLegendreL2 i)) =
        (∑ k ∈ Finset.range m,
          inner ℝ (normalizedLegendreL2 k) x *
            inner ℝ x (normalizedLegendreL2 k)) := by
    classical
    exact normalizedLegendreL2_orthonormal.inner_left_right_finset
  have h₃ : ∀ z : ℝ,
      RCLike.re (z * starRingEnd ℝ z) = ‖z‖ ^ 2 := by
    intro z
    simp [pow_two]
  rw [finiteLegendreProjection, @norm_sub_sq ℝ, sub_add]
  simp only [@InnerProductSpace.norm_sq_eq_re_inner ℝ IntervalL2,
    inner_sum, sum_inner]
  simp only [inner_smul_right, two_mul, inner_smul_left,
    inner_conj_symm, ← mul_assoc, h₂, add_sub_cancel_right,
    sub_right_inj]
  simp only [map_sum, ← inner_conj_symm x, ← h₃]

/-- The coefficient tail is exactly the squared `L²` residual after the
first `m` Legendre modes.  This is the projection-tail bridge used by the
analytic leakage estimate. -/
theorem tsum_tail_eq_norm_finiteLegendreProjection_residual_sq
    (m : ℕ) (x : IntervalL2) :
    ∑' n : ℕ,
        ‖inner ℝ (normalizedLegendreL2 (m + n)) x‖ ^ 2 =
      ‖x - finiteLegendreProjection m x‖ ^ 2 := by
  rw [norm_finiteLegendreProjection_residual_sq]
  simpa using
    (HilbertBasisTail.tsum_nat_add_sq_norm_inner_eq_sub_sum
      normalizedLegendreHilbertBasis x m)

/-- Canonical-projection form of the exact tail identity. -/
theorem tsum_tail_eq_norm_starProjection_residual_sq
    (m : ℕ) (x : IntervalL2) :
    ∑' n : ℕ,
        ‖inner ℝ (normalizedLegendreL2 (m + n)) x‖ ^ 2 =
      ‖x - (finiteLegendreSubspace m).starProjection x‖ ^ 2 := by
  rw [finiteLegendreSubspace_starProjection]
  exact tsum_tail_eq_norm_finiteLegendreProjection_residual_sq m x

/-- Any proved coefficient-tail bound immediately becomes the same bound
for the squared norm of the canonical projection residual. -/
theorem norm_starProjection_residual_sq_le_of_tsum_tail_le
    (m : ℕ) (x : IntervalL2) (C : ℝ)
    (h : ∑' n : ℕ,
        ‖inner ℝ (normalizedLegendreL2 (m + n)) x‖ ^ 2 ≤ C) :
    ‖x - (finiteLegendreSubspace m).starProjection x‖ ^ 2 ≤ C := by
  rw [← tsum_tail_eq_norm_starProjection_residual_sq]
  exact h

end LegendreL2
