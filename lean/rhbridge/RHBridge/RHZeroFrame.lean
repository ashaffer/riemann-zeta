/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.RHBranchLedger

/-!
# The zero frame under an explicit RH hypothesis

This file rewrites each Guinand--Weil zero summand as a nonnegative square.
Every result which locates a zero on the critical line carries an explicit
`RiemannHypothesis` argument.  No converse or unconditional RH claim is made.
-/

namespace RHP2Bridge.RHZeroFrame

open scoped ComplexConjugate
open GuinandWeilFormula GeneralZetaWeilForm

noncomputable section

/-- The quotient-level and canonical-representative bilateral transforms
agree.  This is independent of RH. -/
theorem bilateralLaplace_eq_bilateralLaplaceFn (a : ℝ)
    (f : TestSpace a) (s : ℂ) :
    bilateralLaplace a f s = bilateralLaplaceFn a f s := by
  unfold bilateralLaplace bilateralLaplaceFn
  apply MeasureTheory.integral_congr_ae
  filter_upwards [IntervalZeroExtension.coeFn_zeroExtension a f] with x hx
  rw [hx]

/-- Conjugation symmetry of the quotient-level transform of a real test
vector.  This is independent of RH. -/
theorem conj_bilateralLaplace (a : ℝ) (f : TestSpace a) (s : ℂ) :
    conj (bilateralLaplace a f s) = bilateralLaplace a f (conj s) := by
  rw [bilateralLaplace_eq_bilateralLaplaceFn,
    conj_bilateralLaplaceFn,
    bilateralLaplace_eq_bilateralLaplaceFn]

/-- **RH-dependent.** Every nontrivial zero lies on the critical line. -/
theorem nontrivialZero_re_eq_half (hRH : RiemannHypothesis)
    (ρ : NontrivialZetaZero) : ρ.val.re = 1 / 2 := by
  apply hRH ρ.val ρ.property.1
  · rintro ⟨n, hn⟩
    have hre := congrArg Complex.re hn
    norm_num at hre
    have hn0 : (0 : ℝ) ≤ n := Nat.cast_nonneg n
    linarith [ρ.property.2.1]
  · intro hρ
    have hre := congrArg Complex.re hρ
    norm_num at hre
    linarith [ρ.property.2.2]

/-- Critical-line frequency attached to a nontrivial zero. -/
def zeroFrameCoefficient (a : ℝ) (f : TestSpace a)
    (ρ : NontrivialZetaZero) : ℂ :=
  bilateralLaplace a f (ρ.val.im * Complex.I)

/-- **RH-dependent.** The first centered argument is purely imaginary. -/
theorem zero_sub_half_eq_im_mul_I (hRH : RiemannHypothesis)
    (ρ : NontrivialZetaZero) :
    ρ.val - 1 / 2 = ρ.val.im * Complex.I := by
  apply Complex.ext
  · simp [nontrivialZero_re_eq_half hRH ρ]
  · simp

/-- **RH-dependent.** The reflected centered argument is the conjugate of
the first one. -/
theorem half_sub_zero_eq_conj_im_mul_I (hRH : RiemannHypothesis)
    (ρ : NontrivialZetaZero) :
    1 / 2 - ρ.val = conj (ρ.val.im * Complex.I) := by
  apply Complex.ext
  · simp [nontrivialZero_re_eq_half hRH ρ]
  · simp

/-- **RH-dependent zero-frame factorization.** Each multiplicity-weighted
zero summand is a square norm of a transform sample. -/
theorem zeroSummand_eq_multiplicity_mul_normSq
    (hRH : RiemannHypothesis) (a : ℝ) (f : TestSpace a)
    (ρ : NontrivialZetaZero) :
    zeroSummand a f ρ =
      zeroMultiplicity ρ * Complex.normSq (zeroFrameCoefficient a f ρ) := by
  unfold zeroSummand zeroFrameCoefficient
  rw [zero_sub_half_eq_im_mul_I hRH ρ,
    half_sub_zero_eq_conj_im_mul_I hRH ρ,
    ← conj_bilateralLaplace]
  rw [Complex.mul_conj]

/-- **RH-dependent.** Every individual frame contribution is real and
nonnegative. -/
theorem zeroSummand_re_nonneg (hRH : RiemannHypothesis)
    (a : ℝ) (f : TestSpace a) (ρ : NontrivialZetaZero) :
    0 ≤ (zeroSummand a f ρ).re := by
  rw [zeroSummand_eq_multiplicity_mul_normSq hRH]
  simp only [Complex.mul_re, Complex.natCast_re,
    Complex.natCast_im, zero_mul, sub_zero, Complex.ofReal_re]
  exact mul_nonneg (Nat.cast_nonneg _) (Complex.normSq_nonneg _)

/-- **RH-dependent.** Every individual frame contribution has zero imaginary
part. -/
theorem zeroSummand_im_eq_zero (hRH : RiemannHypothesis)
    (a : ℝ) (f : TestSpace a) (ρ : NontrivialZetaZero) :
    (zeroSummand a f ρ).im = 0 := by
  rw [zeroSummand_eq_multiplicity_mul_normSq hRH]
  simp

/-- Finite, multiplicity-weighted zero-frame energy in a closed disk. -/
def zeroFrameEnergyInDisk (R a : ℝ) (f : TestSpace a) : ℝ :=
  ∑ ρ ∈ nontrivialZerosInDisk R,
    zeroMultiplicity ρ * Complex.normSq (zeroFrameCoefficient a f ρ)

/-- **RH-dependent finite frame identity.** Symmetric disk truncation of the
zero sum is exactly the finite frame energy, embedded in `ℂ`. -/
theorem zeroSumInDisk_eq_zeroFrameEnergyInDisk
    (hRH : RiemannHypothesis) (R a : ℝ) (f : TestSpace a) :
    zeroSumInDisk R a f = zeroFrameEnergyInDisk R a f := by
  unfold zeroSumInDisk zeroFrameEnergyInDisk
  push_cast
  apply Finset.sum_congr rfl
  intro ρ hρ
  exact zeroSummand_eq_multiplicity_mul_normSq hRH a f ρ

/-- By definition, every finite frame energy is nonnegative; RH is needed to
identify it with the corresponding zero sum, not for this inequality. -/
theorem zeroFrameEnergyInDisk_nonneg
    (R a : ℝ) (f : TestSpace a) :
    0 ≤ zeroFrameEnergyInDisk R a f := by
  unfold zeroFrameEnergyInDisk
  apply Finset.sum_nonneg
  intro ρ hρ
  exact mul_nonneg (Nat.cast_nonneg _) (Complex.normSq_nonneg _)

/-- **RH-dependent.** Every symmetric finite zero truncation has
nonnegative real part. -/
theorem zeroSumInDisk_re_nonneg
    (hRH : RiemannHypothesis) (R a : ℝ) (f : TestSpace a) :
    0 ≤ (zeroSumInDisk R a f).re := by
  rw [zeroSumInDisk_eq_zeroFrameEnergyInDisk hRH]
  simpa using zeroFrameEnergyInDisk_nonneg R a f

end

end RHP2Bridge.RHZeroFrame
