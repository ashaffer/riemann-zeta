/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2DigammaTail
import RHBridge.P2ElementaryConstants
import RHBridge.P2TailTelescopers

/-!
# A concrete enclosure of the canonical `p = 2` exterior floor

This module evaluates the exact constant `GlideKernel.p2Alpha` with rational,
kernel-checked error bounds.  Euler's constant is enclosed using the directed
fourth-order approximants in `Glide.EulerBounds`; the quarter-line digamma
difference is reduced to the accelerated rational tail certificate; and all
remaining elementary constants use `P2ElementaryConstants`.
-/

namespace RHP2Bridge

open Set

/-- A narrow rational enclosure of Euler's constant obtained from the
directed fourth-order approximants at `n = 1024`. -/
theorem eulerMascheroniConstant_mem_Ioo_14 :
    Real.eulerMascheroniConstant ∈
      Ioo ((57721566490152 : ℝ) / 100000000000000)
        ((57721566490155 : ℝ) / 100000000000000) := by
  have hlower := GlideKernel.refinedEulerLower_le_eulerMascheroni 1024 (by norm_num)
  have hupper := GlideKernel.eulerMascheroni_le_refinedEulerUpper 1024 (by norm_num)
  have hlog := log_two_mem_Ioo_16
  have hlog1024 : Real.log (1024 : ℝ) = 10 * Real.log 2 := by
    rw [show (1024 : ℝ) = 2 ^ 10 by norm_num, Real.log_pow]
    norm_num
  constructor
  · apply lt_of_lt_of_le ?_ hlower
    unfold GlideKernel.refinedEulerLower GlideKernel.refinedEulerUpper
    norm_num only [Nat.cast_ofNat]
    rw [hlog1024]
    norm_num [harmonic, Finset.sum_range_succ]
    linarith [hlog.2]
  · apply lt_of_le_of_lt hupper
    unfold GlideKernel.refinedEulerUpper
    norm_num only [Nat.cast_ofNat]
    rw [hlog1024]
    norm_num [harmonic, Finset.sum_range_succ]
    linarith [hlog.1]

/-- The special value at the real point of the quarter line, exposed in the
form needed to eliminate the remaining digamma term from `p2Alpha`. -/
theorem quarterDigammaReal_zero_eq :
    GlideKernel.quarterDigammaReal 0 =
      -Real.eulerMascheroniConstant - 3 * Real.log 2 - Real.pi / 2 := by
  have h := congrArg Complex.re GlideKernel.digamma_one_quarter
  norm_num [GlideKernel.quarterDigammaReal, Complex.sub_re, Complex.mul_re,
    Complex.div_re, Complex.normSq_apply] at h ⊢
  have hlog2 : Complex.log (2 : ℂ) = (Real.log 2 : ℂ) := by
    calc
      Complex.log (2 : ℂ) = Complex.log ((2 : ℝ) : ℂ) := by norm_num
      _ = (Real.log 2 : ℂ) :=
        (Complex.ofReal_log (by norm_num : (0 : ℝ) ≤ 2)).symm
  rw [hlog2] at h
  simpa only [Complex.ofReal_re] using h

/-- Exact decomposition of `p2Alpha` into the rational digamma-difference
series and the elementary constants enclosed in this module's dependencies. -/
theorem p2Alpha_eq_constants_sub_quarterDifference :
    GlideKernel.p2Alpha =
      -Real.eulerMascheroniConstant - 3 * Real.log 2 - Real.pi / 2 -
        (∑' n : ℕ, GlideKernel.quarterDifferenceTerm 0 50 n) -
        Real.log Real.pi - GlideKernel.p2PrimeAmplitude := by
  have hdiff := GlideKernel.quarterDifference_tsum_eq 0 50
  unfold GlideKernel.p2Alpha
  rw [show GlideKernel.quarterDigammaReal 50 =
      GlideKernel.quarterDigammaReal 0 -
        ∑' n : ℕ, GlideKernel.quarterDifferenceTerm 0 50 n by linarith]
  rw [quarterDigammaReal_zero_eq]

/-- Rational lower endpoint for `p2Alpha`, parameterized only by an upper
endpoint for the quarter-line digamma-difference series. -/
noncomputable def p2AlphaLowerOfDifferenceUpper (tailUpper : ℝ) : ℝ :=
  -(57721566490155 / 100000000000000 : ℝ) -
    3 * (6931471805599454 / 10000000000000000 : ℝ) -
    (314159265358979323847 / 100000000000000000000 : ℝ) / 2 -
    tailUpper - (1144729885849401 / 1000000000000000 : ℝ) -
    (980258143468548 / 1000000000000000 : ℝ)

/-- Rational upper endpoint for `p2Alpha`, parameterized only by a lower
endpoint for the quarter-line digamma-difference series. -/
noncomputable def p2AlphaUpperOfDifferenceLower (tailLower : ℝ) : ℝ :=
  -(57721566490152 / 100000000000000 : ℝ) -
    3 * (6931471805599453 / 10000000000000000 : ℝ) -
    (314159265358979323846 / 100000000000000000000 : ℝ) / 2 -
    tailLower - (1144729885849400 / 1000000000000000 : ℝ) -
    (980258143468547 / 1000000000000000 : ℝ)

/-- Any rational enclosure of the sole digamma-difference series transfers
directly to a rational enclosure of the exact exterior floor. -/
theorem p2Alpha_mem_Ioo_of_quarterDifference_mem_Ioo
    {tailLower tailUpper : ℝ}
    (htail : (∑' n : ℕ, GlideKernel.quarterDifferenceTerm 0 50 n) ∈
      Ioo tailLower tailUpper) :
    GlideKernel.p2Alpha ∈
      Ioo (p2AlphaLowerOfDifferenceUpper tailUpper)
        (p2AlphaUpperOfDifferenceLower tailLower) := by
  have hgamma := eulerMascheroniConstant_mem_Ioo_14
  have hlog2 := log_two_mem_Ioo_16
  have hpi := pi_mem_Ioo_20
  have hlogpi := log_pi_mem_Ioo_15
  have hprime := p2PrimeAmplitude_mem_Ioo_15
  rcases htail with ⟨htailLower, htailUpper⟩
  rcases hgamma with ⟨hgammaLower, hgammaUpper⟩
  rcases hlog2 with ⟨hlog2Lower, hlog2Upper⟩
  rcases hpi with ⟨hpiLower, hpiUpper⟩
  rcases hlogpi with ⟨hlogpiLower, hlogpiUpper⟩
  rcases hprime with ⟨hprimeLower, hprimeUpper⟩
  rw [p2Alpha_eq_constants_sub_quarterDifference]
  unfold p2AlphaLowerOfDifferenceUpper p2AlphaUpperOfDifferenceLower
  constructor <;> linarith

/-- A fully rational enclosure of the quarter-line digamma difference used
by `p2Alpha`.  The width includes the complete analytic remainder of the
accelerated inverse-power expansion. -/
theorem quarterDifference_zero_mem_Ioo_14 :
    (∑' n : ℕ, GlideKernel.quarterDifferenceTerm 0 50 n) ∈
      Ioo (-(744631269041090 : ℝ) / 100000000000000)
        (-(744631269041087 : ℝ) / 100000000000000) := by
  have happ := quarterDifferenceApprox_zero_mem_Icc_15
  have herr := abs_quarterDifference_tsum_sub_approx_lt_1e14
    (r := (0 : ℝ)) (by norm_num)
  rw [abs_lt] at herr
  constructor <;> linarith [happ.1, happ.2, herr.1, herr.2]

/-- The canonical `p = 2` exterior floor lies in a rational interval of
width `2 · 10⁻¹³`.  In particular, its uncertainty is comfortably below the
`10⁻¹²` radius of every stored matrix-entry interval. -/
theorem p2Alpha_mem_Ioo_13 :
    GlideKernel.p2Alpha ∈
      Ioo ((10938711277166 : ℝ) / 10000000000000)
        ((10938711277168 : ℝ) / 10000000000000) := by
  have h := p2Alpha_mem_Ioo_of_quarterDifference_mem_Ioo
    quarterDifference_zero_mem_Ioo_14
  constructor
  · exact (show (10938711277166 : ℝ) / 10000000000000 <
        p2AlphaLowerOfDifferenceUpper
          (-(744631269041087 : ℝ) / 100000000000000) by
          norm_num [p2AlphaLowerOfDifferenceUpper]).trans h.1
  · exact h.2.trans (show
        p2AlphaUpperOfDifferenceLower
            (-(744631269041090 : ℝ) / 100000000000000) <
          (10938711277168 : ℝ) / 10000000000000 by
          norm_num [p2AlphaUpperOfDifferenceLower])

end RHP2Bridge
