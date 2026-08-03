/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreScaled
import LegendreL2
import HilbertBasisTail
import LegendreIntervalL2

/-!
# Fourier--Legendre bases on symmetric real intervals

`LegendreScaledL2.FourierLegendre` gives a complete normalized basis on the
symmetric interval `[-a,a]`, together with its unitary coefficient transform,
Parseval identity, and exact finite-projection error.

The scalar field is currently `ℝ`.  The corresponding theory on a general
nondegenerate interval `[b,c]` is in `LegendreIntervalL2`.  This module
re-exports that theory to preserve imports written before the physical split;
new interval-only developments may import `LegendreIntervalL2` directly.
-/

namespace LegendreScaledL2

open Polynomial
open scoped ENNReal InnerProductSpace

/-- The symmetric compact interval `[-a,a]`. -/
abbrev Interval (a : ℝ) := Set.Icc (-a) a

/-- Lebesgue measure transported to the interval subtype. -/
noncomputable def intervalMeasure (a : ℝ) :
    MeasureTheory.Measure (Interval a) :=
  MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume

/-- The real Hilbert space `L²([-a,a])`. -/
noncomputable abbrev IntervalL2 (a : ℝ) :=
  MeasureTheory.Lp ℝ 2 (intervalMeasure a)

instance (a : ℝ) : MeasureTheory.IsFiniteMeasure (intervalMeasure a) := by
  constructor
  rw [intervalMeasure,
    comap_subtype_coe_apply measurableSet_Icc]
  rw [Set.image_univ, Subtype.range_coe_subtype, Set.setOf_mem_eq]
  simp

/-- Send a polynomial to its class in `L²([-a,a])`. -/
noncomputable def polynomialToL2 (a : ℝ) : ℝ[X] →ₗ[ℝ] IntervalL2 a :=
  (ContinuousMap.toLp 2 (intervalMeasure a) ℝ).toLinearMap.comp
    (Polynomial.toContinuousMapOnAlgHom (Interval a)).toLinearMap

@[simp] theorem polynomialToL2_apply (a : ℝ) (p : ℝ[X]) :
    polynomialToL2 a p =
      ContinuousMap.toLp 2 (intervalMeasure a) ℝ
        (p.toContinuousMapOn (Interval a)) := rfl

/-- The scaled normalized Legendre family as vectors in `L²([-a,a])`. -/
noncomputable def scaledNormalizedLegendreL2
    (a : ℝ) (n : ℕ) : IntervalL2 a :=
  polynomialToL2 a (LegendreScaled.scaledNormalizedPlainLegendre a n)

/-- Polynomial `L²` inner products are ordinary interval integrals. -/
theorem inner_polynomialToL2
    (a : ℝ) (ha : 0 ≤ a) (p q : ℝ[X]) :
    ⟪polynomialToL2 a p, polynomialToL2 a q⟫_ℝ =
      LegendreOrthogonality.polynomialPairIntegral p q (-a) a := by
  rw [polynomialToL2_apply, polynomialToL2_apply,
    MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc (-a) a,
      q.eval (x : ℝ) * p.eval (x : ℝ)
        ∂(MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume)) = _
  rw [MeasureTheory.integral_subtype_comap
    (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
    measurableSet_Icc (fun x : ℝ ↦ q.eval x * p.eval x)]
  rw [LegendreOrthogonality.polynomialPairIntegral,
    intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  simp [mul_comm]

/-! ## Algebraic spanning and density -/

/-- The scaled normalized family has exactly one polynomial in every
degree. -/
noncomputable def scaledNormalizedPlainLegendreSequence
    (a : ℝ) (ha : 0 < a) : Polynomial.Sequence ℝ where
  elems' := LegendreScaled.scaledNormalizedPlainLegendre a
  degree_eq' n := by
    have ha0 : a ≠ 0 := ne_of_gt ha
    have hsqrt : Real.sqrt a ≠ 0 := ne_of_gt (Real.sqrt_pos.2 ha)
    have hnorm :
        Real.sqrt ((2 * (n : ℝ) + 1) / 2) ≠ 0 := by positivity
    have hnat :
        (LegendreScaled.scaledNormalizedPlainLegendre a n).natDegree = n := by
      rw [LegendreScaled.scaledNormalizedPlainLegendre,
        Polynomial.natDegree_C_mul (inv_ne_zero hsqrt),
        Polynomial.natDegree_comp,
        LegendreOrthogonality.normalizedPlainLegendre,
        Polynomial.natDegree_C_mul hnorm,
        LegendreOrthogonality.natDegree_plainLegendre,
        Polynomial.natDegree_C_mul (inv_ne_zero ha0),
        Polynomial.natDegree_X]
      omega
    have hne :
        LegendreScaled.scaledNormalizedPlainLegendre a n ≠ 0 := by
      intro hzero
      have hpair :=
        LegendreScaled.scaledNormalizedPlainLegendre_pair_self a ha n
      rw [hzero, LegendreOrthogonality.polynomialPairIntegral] at hpair
      simp at hpair
    rw [Polynomial.degree_eq_natDegree hne, hnat]

@[simp] theorem scaledNormalizedPlainLegendreSequence_apply
    (a : ℝ) (ha : 0 < a) (n : ℕ) :
    scaledNormalizedPlainLegendreSequence a ha n =
      LegendreScaled.scaledNormalizedPlainLegendre a n := rfl

/-- The scaled normalized family algebraically spans all real
polynomials. -/
theorem scaledNormalizedPlainLegendre_span
    (a : ℝ) (ha : 0 < a) :
    Submodule.span ℝ
        (Set.range (LegendreScaled.scaledNormalizedPlainLegendre a)) = ⊤ := by
  change Submodule.span ℝ
    (Set.range (scaledNormalizedPlainLegendreSequence a ha : ℕ → ℝ[X])) = ⊤
  exact (scaledNormalizedPlainLegendreSequence a ha).span (fun n ↦ by
    rw [isUnit_iff_ne_zero]
    exact Polynomial.leadingCoeff_ne_zero.mpr
      ((scaledNormalizedPlainLegendreSequence a ha).ne_zero n))

/-- Weierstrass density for polynomial evaluation on `[-a,a]`. -/
theorem polynomialToContinuousMap_denseRange (a : ℝ) :
    DenseRange (Polynomial.toContinuousMapOnAlgHom (Interval a)) := by
  rw [DenseRange, ← polynomialFunctions_coe]
  rw [dense_iff_closure_eq,
    ← Subalgebra.topologicalClosure_coe,
    polynomialFunctions_closure_eq_top]
  rfl

/-- Polynomial classes are dense in `L²([-a,a])`. -/
theorem polynomialToL2_denseRange (a : ℝ) :
    DenseRange (polynomialToL2 a) := by
  have hcontinuous :
      DenseRange
        (ContinuousMap.toLp 2 (intervalMeasure a) ℝ :
          C(Interval a, ℝ) →L[ℝ] IntervalL2 a) :=
    ContinuousMap.toLp_denseRange ℝ (intervalMeasure a) ℝ (by norm_num)
  have h := hcontinuous.comp (polynomialToContinuousMap_denseRange a)
    (ContinuousMap.toLp 2 (intervalMeasure a) ℝ).continuous
  simpa [polynomialToL2, Function.comp_def] using h

/-! ## Orthonormality and completeness -/

theorem inner_scaledNormalizedLegendreL2
    (a : ℝ) (ha : 0 < a) (m n : ℕ) :
    ⟪scaledNormalizedLegendreL2 a m,
      scaledNormalizedLegendreL2 a n⟫_ℝ =
        if m = n then 1 else 0 := by
  rw [scaledNormalizedLegendreL2, scaledNormalizedLegendreL2,
    inner_polynomialToL2 a ha.le]
  exact LegendreScaled.scaledNormalizedPlainLegendre_orthonormal a ha m n

/-- The scaled Legendre vectors are orthonormal in the actual interval
`L²` space. -/
theorem scaledNormalizedLegendreL2_orthonormal
    (a : ℝ) (ha : 0 < a) :
    Orthonormal ℝ (scaledNormalizedLegendreL2 a) := by
  rw [orthonormal_iff_ite]
  exact inner_scaledNormalizedLegendreL2 a ha

theorem scaledNormalizedLegendreL2_span_eq_polynomial_range
    (a : ℝ) (ha : 0 < a) :
    Submodule.span ℝ (Set.range (scaledNormalizedLegendreL2 a)) =
      LinearMap.range (polynomialToL2 a) := by
  rw [← Submodule.map_top (polynomialToL2 a),
    ← scaledNormalizedPlainLegendre_span a ha,
    Submodule.map_span]
  congr 1
  rw [← Set.range_comp]
  rfl

/-- The scaled Legendre span is dense in all of `L²([-a,a])`. -/
theorem scaledNormalizedLegendreL2_dense_span
    (a : ℝ) (ha : 0 < a) :
    (Submodule.span ℝ
      (Set.range (scaledNormalizedLegendreL2 a))).topologicalClosure = ⊤ := by
  rw [scaledNormalizedLegendreL2_span_eq_polynomial_range a ha]
  apply Submodule.dense_iff_topologicalClosure_eq_top.mp
  simpa only [LinearMap.coe_range, DenseRange] using
    polynomialToL2_denseRange a

/-- Complete countable Hilbert basis on `[-a,a]`. -/
noncomputable def scaledNormalizedLegendreHilbertBasis
    (a : ℝ) (ha : 0 < a) : HilbertBasis ℕ ℝ (IntervalL2 a) :=
  HilbertBasis.mk (scaledNormalizedLegendreL2_orthonormal a ha)
    (scaledNormalizedLegendreL2_dense_span a ha).ge

@[simp] theorem scaledNormalizedLegendreHilbertBasis_apply
    (a : ℝ) (ha : 0 < a) (n : ℕ) :
    scaledNormalizedLegendreHilbertBasis a ha n =
      scaledNormalizedLegendreL2 a n := by
  exact congrFun
    (HilbertBasis.coe_mk (scaledNormalizedLegendreL2_orthonormal a ha)
      (scaledNormalizedLegendreL2_dense_span a ha).ge) n

/-! ## Parseval and finite-section tails -/

theorem tsum_sq_norm_inner_scaledNormalizedLegendreL2
    (a : ℝ) (ha : 0 < a) (x : IntervalL2 a) :
    ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a n) x‖ ^ 2 = ‖x‖ ^ 2 := by
  simpa using HilbertBasisTail.tsum_sq_norm_inner
    (scaledNormalizedLegendreHilbertBasis a ha) x

/-- The first `m` terms of the scaled Fourier--Legendre expansion. -/
noncomputable def finiteLegendreProjection
    (a : ℝ) (m : ℕ) (x : IntervalL2 a) : IntervalL2 a :=
  ∑ k ∈ Finset.range m,
    inner ℝ (scaledNormalizedLegendreL2 a k) x •
      scaledNormalizedLegendreL2 a k

/-- The subspace generated by the first `m` scaled modes. -/
noncomputable def finiteLegendreSubspace
    (a : ℝ) (m : ℕ) : Submodule ℝ (IntervalL2 a) :=
  Submodule.span ℝ
    (scaledNormalizedLegendreL2 a '' (Finset.range m : Set ℕ))

noncomputable instance finiteLegendreSubspace_finiteDimensional
    (a : ℝ) (m : ℕ) :
    FiniteDimensional ℝ (finiteLegendreSubspace a m) := by
  rw [finiteLegendreSubspace]
  exact FiniteDimensional.span_of_finite ℝ
    ((Finset.finite_toSet (Finset.range m)).image
      (scaledNormalizedLegendreL2 a))

noncomputable instance finiteLegendreSubspace_completeSpace
    (a : ℝ) (m : ℕ) : CompleteSpace (finiteLegendreSubspace a m) :=
  FiniteDimensional.complete ℝ _

/-- The finite sum is the canonical orthogonal projection. -/
theorem finiteLegendreSubspace_starProjection
    (a : ℝ) (ha : 0 < a) (m : ℕ) (x : IntervalL2 a) :
    (finiteLegendreSubspace a m).starProjection x =
      finiteLegendreProjection a m x := by
  classical
  let b := OrthonormalBasis.span
    (scaledNormalizedLegendreL2_orthonormal a ha) (Finset.range m)
  have h := congrArg Subtype.val
    (b.orthogonalProjectionOnto_apply_eq_sum x)
  calc
    (finiteLegendreSubspace a m).starProjection x =
        ∑ k : ↑(Finset.range m),
          inner ℝ (scaledNormalizedLegendreL2 a (k : ℕ)) x •
            scaledNormalizedLegendreL2 a (k : ℕ) := by
      simpa [b, finiteLegendreSubspace] using h
    _ = finiteLegendreProjection a m x := by
      simpa [finiteLegendreProjection] using
        (Finset.sum_attach (Finset.range m)
          (fun k ↦ inner ℝ (scaledNormalizedLegendreL2 a k) x •
            scaledNormalizedLegendreL2 a k))

/-- Exact finite projection energy identity. -/
theorem norm_finiteLegendreProjection_residual_sq
    (a : ℝ) (ha : 0 < a) (m : ℕ) (x : IntervalL2 a) :
    ‖x - finiteLegendreProjection a m x‖ ^ 2 =
      ‖x‖ ^ 2 -
        ∑ k ∈ Finset.range m,
          ‖inner ℝ (scaledNormalizedLegendreL2 a k) x‖ ^ 2 := by
  have h₂ :
      (∑ i ∈ Finset.range m, ∑ j ∈ Finset.range m,
          inner ℝ (scaledNormalizedLegendreL2 a i) x *
            inner ℝ x (scaledNormalizedLegendreL2 a j) *
              inner ℝ (scaledNormalizedLegendreL2 a j)
                (scaledNormalizedLegendreL2 a i)) =
        (∑ k ∈ Finset.range m,
          inner ℝ (scaledNormalizedLegendreL2 a k) x *
            inner ℝ x (scaledNormalizedLegendreL2 a k)) := by
    classical
    exact (scaledNormalizedLegendreL2_orthonormal a ha).inner_left_right_finset
  have h₃ : ∀ z : ℝ,
      RCLike.re (z * starRingEnd ℝ z) = ‖z‖ ^ 2 := by
    intro z
    simp [pow_two]
  rw [finiteLegendreProjection, @norm_sub_sq ℝ, sub_add]
  simp only [@InnerProductSpace.norm_sq_eq_re_inner ℝ (IntervalL2 a),
    inner_sum, sum_inner]
  simp only [inner_smul_right, two_mul, inner_smul_left,
    inner_conj_symm, ← mul_assoc, h₂, add_sub_cancel_right,
    sub_right_inj]
  simp only [map_sum, ← inner_conj_symm x, ← h₃]

/-- The coefficient tail is exactly the finite projection residual. -/
theorem tsum_tail_eq_norm_finiteLegendreProjection_residual_sq
    (a : ℝ) (ha : 0 < a) (m : ℕ) (x : IntervalL2 a) :
    ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a (m + n)) x‖ ^ 2 =
      ‖x - finiteLegendreProjection a m x‖ ^ 2 := by
  rw [norm_finiteLegendreProjection_residual_sq a ha]
  simpa using
    (HilbertBasisTail.tsum_nat_add_sq_norm_inner_eq_sub_sum
      (scaledNormalizedLegendreHilbertBasis a ha) x m)

/-- Canonical-projection form of the exact tail identity. -/
theorem tsum_tail_eq_norm_starProjection_residual_sq
    (a : ℝ) (ha : 0 < a) (m : ℕ) (x : IntervalL2 a) :
    ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a (m + n)) x‖ ^ 2 =
      ‖x - (finiteLegendreSubspace a m).starProjection x‖ ^ 2 := by
  rw [finiteLegendreSubspace_starProjection a ha]
  exact tsum_tail_eq_norm_finiteLegendreProjection_residual_sq a ha m x

/-- Any coefficient-tail estimate bounds the canonical projection
residual. -/
theorem norm_starProjection_residual_sq_le_of_tsum_tail_le
    (a : ℝ) (ha : 0 < a) (m : ℕ) (x : IntervalL2 a) (C : ℝ)
    (h : ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a (m + n)) x‖ ^ 2 ≤ C) :
    ‖x - (finiteLegendreSubspace a m).starProjection x‖ ^ 2 ≤ C := by
  rw [← tsum_tail_eq_norm_starProjection_residual_sq a ha]
  exact h

/-! ## Human-facing Fourier--Legendre API

The declarations above expose every construction step.  The following small
namespace packages their mathematical endpoint: a complete orthonormal basis,
its unitary coefficient transform, Parseval, and the exact finite-section
error.  Keeping these aliases separate preserves all existing callers while
giving downstream developments a stable interface that does not depend on the
construction proof.
-/

namespace FourierLegendre

/-- The normalized Legendre Hilbert basis of real `L²([-a,a])`. -/
noncomputable abbrev basis (a : ℝ) (ha : 0 < a) :
    HilbertBasis ℕ ℝ (IntervalL2 a) :=
  scaledNormalizedLegendreHilbertBasis a ha

/-- The unitary Fourier--Legendre coefficient transform. -/
noncomputable def transform (a : ℝ) (ha : 0 < a) :=
  (basis a ha).repr

@[simp] theorem basis_apply (a : ℝ) (ha : 0 < a) (n : ℕ) :
    basis a ha n = scaledNormalizedLegendreL2 a n := by
  exact scaledNormalizedLegendreHilbertBasis_apply a ha n

@[simp] theorem transform_apply (a : ℝ) (ha : 0 < a)
    (x : IntervalL2 a) (n : ℕ) :
    transform a ha x n =
      inner ℝ (scaledNormalizedLegendreL2 a n) x := by
  change (basis a ha).repr x n = _
  rw [(basis a ha).repr_apply_apply, basis_apply]

/-- Parseval's identity for the Fourier--Legendre transform. -/
theorem parseval (a : ℝ) (ha : 0 < a) (x : IntervalL2 a) :
    ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a n) x‖ ^ 2 = ‖x‖ ^ 2 :=
  tsum_sq_norm_inner_scaledNormalizedLegendreL2 a ha x

/-- The exact squared error after retaining the first `m` coefficients. -/
theorem projection_error (a : ℝ) (ha : 0 < a) (m : ℕ)
    (x : IntervalL2 a) :
    ‖x - (finiteLegendreSubspace a m).starProjection x‖ ^ 2 =
      ∑' n : ℕ,
        ‖inner ℝ (scaledNormalizedLegendreL2 a (m + n)) x‖ ^ 2 := by
  exact (tsum_tail_eq_norm_starProjection_residual_sq a ha m x).symm

end FourierLegendre

/-! ## The complex plane wave as two real `L²` vectors -/

/-- Real part of `exp (-i z x)` on the interval. -/
noncomputable def planeWaveRealContinuous
    (a z : ℝ) : C(Interval a, ℝ) where
  toFun x := (LegendrePlaneWave.fourierPhase z (x : ℝ)).re
  continuous_toFun := by
    unfold LegendrePlaneWave.fourierPhase
    fun_prop

/-- Imaginary part of `exp (-i z x)` on the interval. -/
noncomputable def planeWaveImagContinuous
    (a z : ℝ) : C(Interval a, ℝ) where
  toFun x := (LegendrePlaneWave.fourierPhase z (x : ℝ)).im
  continuous_toFun := by
    unfold LegendrePlaneWave.fourierPhase
    fun_prop

/-- Real part of the plane wave as an `L²([-a,a])` vector. -/
noncomputable def planeWaveRealL2 (a z : ℝ) : IntervalL2 a :=
  ContinuousMap.toLp 2 (intervalMeasure a) ℝ
    (planeWaveRealContinuous a z)

/-- Imaginary part of the plane wave as an `L²([-a,a])` vector. -/
noncomputable def planeWaveImagL2 (a z : ℝ) : IntervalL2 a :=
  ContinuousMap.toLp 2 (intervalMeasure a) ℝ
    (planeWaveImagContinuous a z)

/-- The real part of the complex plane-wave coefficient is the Hilbert
coefficient of its real component. -/
theorem inner_scaledNormalizedLegendreL2_planeWaveReal
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    inner ℝ (scaledNormalizedLegendreL2 a n) (planeWaveRealL2 a z) =
      (LegendrePlaneWave.polyFourierIntegral
        (LegendreScaled.scaledNormalizedPlainLegendre a n)
          z (-a) a).re := by
  let p : ℝ[X] := LegendreScaled.scaledNormalizedPlainLegendre a n
  let F : ℝ → ℂ := fun x ↦
    ((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x
  have hF : IntervalIntegrable F MeasureTheory.volume (-a) a := by
    apply Continuous.intervalIntegrable
    dsimp [F]
    unfold LegendrePlaneWave.fourierPhase
    fun_prop
  rw [scaledNormalizedLegendreL2, polynomialToL2_apply,
    planeWaveRealL2, MeasureTheory.ContinuousMap.inner_toLp]
  rw [LegendrePlaneWave.polyFourierIntegral]
  change (∫ x : Set.Icc (-a) a,
      (LegendrePlaneWave.fourierPhase z (x : ℝ)).re *
        p.eval (x : ℝ) ∂intervalMeasure a) =
    RCLike.re (∫ x in -a..a, F x)
  rw [← intervalIntegral.intervalIntegral_re hF]
  rw [intervalMeasure,
    MeasureTheory.integral_subtype_comap
      (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
      measurableSet_Icc
      (fun x : ℝ ↦
        (LegendrePlaneWave.fourierPhase z x).re * p.eval x)]
  rw [intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  dsimp [F]
  simp [mul_comm]

/-- The imaginary part of the complex plane-wave coefficient is the
Hilbert coefficient of its imaginary component. -/
theorem inner_scaledNormalizedLegendreL2_planeWaveImag
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    inner ℝ (scaledNormalizedLegendreL2 a n) (planeWaveImagL2 a z) =
      (LegendrePlaneWave.polyFourierIntegral
        (LegendreScaled.scaledNormalizedPlainLegendre a n)
          z (-a) a).im := by
  let p : ℝ[X] := LegendreScaled.scaledNormalizedPlainLegendre a n
  let F : ℝ → ℂ := fun x ↦
    ((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x
  have hF : IntervalIntegrable F MeasureTheory.volume (-a) a := by
    apply Continuous.intervalIntegrable
    dsimp [F]
    unfold LegendrePlaneWave.fourierPhase
    fun_prop
  rw [scaledNormalizedLegendreL2, polynomialToL2_apply,
    planeWaveImagL2, MeasureTheory.ContinuousMap.inner_toLp]
  rw [LegendrePlaneWave.polyFourierIntegral]
  change (∫ x : Set.Icc (-a) a,
      (LegendrePlaneWave.fourierPhase z (x : ℝ)).im *
        p.eval (x : ℝ) ∂intervalMeasure a) =
    RCLike.im (∫ x in -a..a, F x)
  rw [← intervalIntegral.intervalIntegral_im hF]
  rw [intervalMeasure,
    MeasureTheory.integral_subtype_comap
      (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
      measurableSet_Icc
      (fun x : ℝ ↦
        (LegendrePlaneWave.fourierPhase z x).im * p.eval x)]
  rw [intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  dsimp [F]
  simp [mul_comm]

end LegendreScaledL2
