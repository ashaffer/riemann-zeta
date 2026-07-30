/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2TailTelescopers
import RHBridge.P2CosApprox

/-!
# A finite rational approximation to the canonical `p = 2` symbol defect

This module removes the last infinite constants from the accelerated
digamma approximation.  Each shifted power tail is replaced by a rational
center certified by `P2TailTelescopers`; the prime amplitude and logarithm
use rational centers; and cosine is replaced by its finite degree-127 Taylor
polynomial.  The resulting function is finite and rational apart from its
real input.  Its 64 rational-kernel denominators are intentionally retained
for the later panelwise reciprocal certificates.
-/

namespace RHP2Bridge

open Set
open scoped BigOperators

/-- Decimal rational centers for the fifteen shifted power tails used by the
order-16 inverse-power digamma expansion. -/
noncomputable def p2ShiftedPowerTailCenter : ℕ → ℝ
  | 3 => 12302203694272605164 / 10 ^ 23
  | 5 => 1513318071016888708 / 10 ^ 26
  | 7 => 248187933250395478 / 10 ^ 29
  | 9 => 457876177281654 / 10 ^ 30
  | 11 => 9009664018164 / 10 ^ 32
  | 13 => 1846555525330 / 10 ^ 35
  | 15 => 389237872480 / 10 ^ 38
  | 17 => 83750453653 / 10 ^ 41
  | 19 => 18304725494 / 10 ^ 44
  | 21 => 4050409104 / 10 ^ 47
  | 23 => 905240534 / 10 ^ 50
  | 25 => 203984837 / 10 ^ 53
  | 27 => 46283155 / 10 ^ 56
  | 29 => 10563071 / 10 ^ 59
  | 31 => 2422946 / 10 ^ 62
  | _ => 0

/-- Simple decimal radii around `p2ShiftedPowerTailCenter`. -/
noncomputable def p2ShiftedPowerTailRadius : ℕ → ℝ
  | 3 => 1 / 10 ^ 23
  | 5 => 1 / 10 ^ 26
  | 7 => 1 / 10 ^ 29
  | 9 => 1 / 10 ^ 30
  | 11 => 2 / 10 ^ 32
  | 13 => 1 / 10 ^ 35
  | 15 => 1 / 10 ^ 38
  | 17 => 1 / 10 ^ 41
  | 19 => 1 / 10 ^ 44
  | 21 => 1 / 10 ^ 47
  | 23 => 1 / 10 ^ 50
  | 25 => 1 / 10 ^ 53
  | 27 => 1 / 10 ^ 56
  | 29 => 1 / 10 ^ 59
  | 31 => 1 / 10 ^ 62
  | _ => 0

private theorem abs_sub_center_le_of_mem_Icc
    {x lower upper center radius : ℝ}
    (hx : x ∈ Icc lower upper)
    (hlower : center - radius ≤ lower)
    (hupper : upper ≤ center + radius) :
    |x - center| ≤ radius := by
  rw [abs_le]
  constructor <;> linarith [hx.1, hx.2]

/-- Every shifted power tail appearing in the order-16 polynomial lies in
its explicit decimal interval. -/
theorem abs_shiftedPowerTail_sub_center_le
    (k : ℕ) (hk1 : 1 ≤ k) (hk16 : k < 16) :
    |shiftedPowerTail (2 * k + 1) 64 -
        p2ShiftedPowerTailCenter (2 * k + 1)| ≤
      p2ShiftedPowerTailRadius (2 * k + 1) := by
  interval_cases k <;> try omega
  all_goals
    apply abs_sub_center_le_of_mem_Icc
    · first
      | exact shiftedPowerTail_three_mem_Icc
      | exact shiftedPowerTail_five_mem_Icc
      | exact shiftedPowerTail_seven_mem_Icc
      | exact shiftedPowerTail_nine_mem_Icc
      | exact shiftedPowerTail_eleven_mem_Icc
      | exact shiftedPowerTail_thirteen_mem_Icc
      | exact shiftedPowerTail_fifteen_mem_Icc
      | exact shiftedPowerTail_seventeen_mem_Icc
      | exact shiftedPowerTail_nineteen_mem_Icc
      | exact shiftedPowerTail_twenty_one_mem_Icc
      | exact shiftedPowerTail_twenty_three_mem_Icc
      | exact shiftedPowerTail_twenty_five_mem_Icc
      | exact shiftedPowerTail_twenty_seven_mem_Icc
      | exact shiftedPowerTail_twenty_nine_mem_Icc
      | exact shiftedPowerTail_thirty_one_mem_Icc
    · norm_num [p2ShiftedPowerTailCenter, p2ShiftedPowerTailRadius]
    · norm_num [p2ShiftedPowerTailCenter, p2ShiftedPowerTailRadius]

/-- The accelerated tail polynomial with all infinite shifted power tails
replaced by rational centers. -/
noncomputable def p2RationalQuarterTailPolynomial (r : ℝ) : ℝ :=
  ∑ k ∈ Finset.range 16,
    (-1 : ℝ) ^ k * (625 ^ k - (r / 2) ^ (2 * k)) *
      p2ShiftedPowerTailCenter (2 * k + 1)

/-- The same rational tail approximation as an actual polynomial in `r`. -/
noncomputable def p2RationalQuarterTailPoly : Polynomial ℝ :=
  ∑ k ∈ Finset.range 16,
    (Polynomial.C
        ((-1 : ℝ) ^ k * 625 ^ k *
          p2ShiftedPowerTailCenter (2 * k + 1)) -
      Polynomial.C
          ((-1 : ℝ) ^ k * p2ShiftedPowerTailCenter (2 * k + 1) /
            2 ^ (2 * k)) * Polynomial.X ^ (2 * k))

@[simp] theorem eval_p2RationalQuarterTailPoly (r : ℝ) :
    p2RationalQuarterTailPoly.eval r =
      p2RationalQuarterTailPolynomial r := by
  unfold p2RationalQuarterTailPoly p2RationalQuarterTailPolynomial
  rw [Polynomial.eval_finsetSum]
  apply Finset.sum_congr rfl
  intro k hk
  simp only [Polynomial.eval_sub, Polynomial.eval_C, Polynomial.eval_mul,
    Polynomial.eval_pow, Polynomial.eval_X]
  ring_nf
  rw [show (2 : ℝ)⁻¹ = 1 / 2 by norm_num]
  ring

/-- Finite rational approximation to the complete quarter-line digamma
difference.  The first summand contains exactly 64 rational functions of
`r`; the second is a rational polynomial. -/
noncomputable def p2RationalQuarterDifferenceApprox (r : ℝ) : ℝ :=
  (∑ n ∈ Finset.range 64, GlideKernel.quarterDifferenceTerm r 50 n) +
    p2RationalQuarterTailPolynomial r

private theorem abs_tail_coefficient_le {r : ℝ} (hr : |r| ≤ 50) (k : ℕ) :
    |(-1 : ℝ) ^ k * (625 ^ k - (r / 2) ^ (2 * k))| ≤
      2 * 625 ^ k := by
  have hrhalf : |r / 2| ≤ 25 := by
    rw [abs_div]
    norm_num
    linarith
  rw [abs_mul, abs_pow, abs_neg, abs_one, one_pow, one_mul]
  calc
    |(625 : ℝ) ^ k - (r / 2) ^ (2 * k)| ≤
        |(625 : ℝ) ^ k| + |(r / 2) ^ (2 * k)| := abs_sub _ _
    _ = (625 : ℝ) ^ k + |r / 2| ^ (2 * k) := by
      rw [abs_pow, abs_pow]
      norm_num
    _ ≤ (625 : ℝ) ^ k + 25 ^ (2 * k) := by gcongr
    _ = 2 * 625 ^ k := by
      rw [pow_mul]
      norm_num
      ring

/-- Rationalizing all fifteen shifted power tails costs less than `10⁻¹⁷`
uniformly on the canonical band. -/
theorem abs_quarterDifferenceApprox_sub_rational_lt
    {r : ℝ} (hr : |r| ≤ 50) :
    |quarterDifferenceApprox r 16 64 -
        p2RationalQuarterDifferenceApprox r| < 1 / 10 ^ 17 := by
  unfold quarterDifferenceApprox p2RationalQuarterDifferenceApprox
  unfold quarterTailPolynomial p2RationalQuarterTailPolynomial
  rw [add_sub_add_left_eq_sub, ← Finset.sum_sub_distrib]
  simp_rw [← mul_sub]
  calc
    |∑ k ∈ Finset.range 16,
        (-1 : ℝ) ^ k * (625 ^ k - (r / 2) ^ (2 * k)) *
          (shiftedPowerTail (2 * k + 1) 64 -
            p2ShiftedPowerTailCenter (2 * k + 1))| ≤
        ∑ k ∈ Finset.range 16,
          |(-1 : ℝ) ^ k * (625 ^ k - (r / 2) ^ (2 * k)) *
            (shiftedPowerTail (2 * k + 1) 64 -
              p2ShiftedPowerTailCenter (2 * k + 1))| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ k ∈ Finset.range 16,
          (2 * 625 ^ k) * p2ShiftedPowerTailRadius (2 * k + 1) := by
      apply Finset.sum_le_sum
      intro k hk
      have hk16 : k < 16 := Finset.mem_range.mp hk
      by_cases hk0 : k = 0
      · subst k
        norm_num [p2ShiftedPowerTailRadius]
      · rw [abs_mul]
        exact mul_le_mul (abs_tail_coefficient_le hr k)
          (abs_shiftedPowerTail_sub_center_le k (by omega) hk16)
          (abs_nonneg _) (by positivity)
    _ < 1 / 10 ^ 17 := by
      norm_num [p2ShiftedPowerTailRadius, Finset.sum_range_succ]

/-- Rational center of the prime oscillation amplitude. -/
noncomputable def p2PrimeAmplitudeCenter : ℝ :=
  9802581434685475 / 10000000000000000

theorem abs_p2PrimeAmplitude_sub_center_lt :
    |GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter| <
      1 / (2 * 10 ^ 15) := by
  have h := p2PrimeAmplitude_mem_Ioo_15
  rw [abs_lt]
  constructor <;>
    norm_num [p2PrimeAmplitudeCenter] at h ⊢ <;> linarith

/-- Completely finite rational approximation to
`p2Omega r - p2Alpha` on the canonical band. -/
noncomputable def p2RationalDefectApprox (r : ℝ) : ℝ :=
  p2RationalQuarterDifferenceApprox r +
    p2PrimeAmplitudeCenter *
      (1 - cosTaylor 128 (r * p2LogTwoCenter))

/-- Polynomial part of `p2RationalDefectApprox`; only the 64 rational-kernel
prefix terms remain outside this polynomial. -/
noncomputable def p2RationalNonPrefixPoly : Polynomial ℝ :=
  p2RationalQuarterTailPoly +
    Polynomial.C p2PrimeAmplitudeCenter *
      (1 - cosTaylorPolynomial 128 p2LogTwoCenter)

@[simp] theorem eval_p2RationalNonPrefixPoly (r : ℝ) :
    p2RationalNonPrefixPoly.eval r =
      p2RationalQuarterTailPolynomial r +
        p2PrimeAmplitudeCenter *
          (1 - cosTaylor 128 (r * p2LogTwoCenter)) := by
  unfold p2RationalNonPrefixPoly
  rw [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_C,
    Polynomial.eval_sub, Polynomial.eval_one,
    eval_p2RationalQuarterTailPoly, eval_cosTaylorPolynomial]

/-- Explicit split into the retained finite rational prefix and one rational
polynomial. -/
theorem p2RationalDefectApprox_eq_prefix_add_polynomial (r : ℝ) :
    p2RationalDefectApprox r =
      (∑ n ∈ Finset.range 64,
        GlideKernel.quarterDifferenceTerm r 50 n) +
        p2RationalNonPrefixPoly.eval r := by
  rw [eval_p2RationalNonPrefixPoly]
  unfold p2RationalDefectApprox p2RationalQuarterDifferenceApprox
  ring

private theorem abs_one_sub_cos_le_two (x : ℝ) :
    |1 - Real.cos x| ≤ 2 := by
  rw [abs_le]
  constructor
  · linarith [Real.cos_le_one x]
  · linarith [Real.neg_one_le_cos x]

private theorem abs_prime_term_sub_rational_lt
    {r : ℝ} (hr : |r| ≤ 50) :
    |GlideKernel.p2PrimeAmplitude *
          (1 - Real.cos (r * Real.log 2)) -
        p2PrimeAmplitudeCenter *
          (1 - cosTaylor 128 (r * p2LogTwoCenter))| <
      1 / 10 ^ 15 + 3 / 10 ^ 15 := by
  have hamp := abs_p2PrimeAmplitude_sub_center_lt
  have hcos := abs_primeCos_sub_rationalTaylor_lt hr
  have hcenter0 : 0 ≤ p2PrimeAmplitudeCenter := by
    norm_num [p2PrimeAmplitudeCenter]
  have hcenter1 : p2PrimeAmplitudeCenter ≤ 1 := by
    norm_num [p2PrimeAmplitudeCenter]
  rw [show
      GlideKernel.p2PrimeAmplitude * (1 - Real.cos (r * Real.log 2)) -
          p2PrimeAmplitudeCenter *
            (1 - cosTaylor 128 (r * p2LogTwoCenter)) =
        (GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter) *
            (1 - Real.cos (r * Real.log 2)) +
          p2PrimeAmplitudeCenter *
            (cosTaylor 128 (r * p2LogTwoCenter) -
              Real.cos (r * Real.log 2)) by ring]
  calc
    |(GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter) *
          (1 - Real.cos (r * Real.log 2)) +
        p2PrimeAmplitudeCenter *
          (cosTaylor 128 (r * p2LogTwoCenter) -
            Real.cos (r * Real.log 2))| ≤
      |GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter| *
          |1 - Real.cos (r * Real.log 2)| +
        |p2PrimeAmplitudeCenter| *
          |cosTaylor 128 (r * p2LogTwoCenter) -
            Real.cos (r * Real.log 2)| := by
        simpa only [abs_mul] using abs_add_le
          ((GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter) *
            (1 - Real.cos (r * Real.log 2)))
          (p2PrimeAmplitudeCenter *
            (cosTaylor 128 (r * p2LogTwoCenter) -
              Real.cos (r * Real.log 2)))
    _ < (1 / (2 * 10 ^ 15)) * 2 + 1 * (3 / 10 ^ 15) := by
      apply add_lt_add
      · calc
          |GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter| *
              |1 - Real.cos (r * Real.log 2)| ≤
            |GlideKernel.p2PrimeAmplitude - p2PrimeAmplitudeCenter| * 2 :=
              mul_le_mul_of_nonneg_left (abs_one_sub_cos_le_two _)
                (abs_nonneg _)
          _ < (1 / (2 * 10 ^ 15)) * 2 :=
            mul_lt_mul_of_pos_right hamp (by norm_num)
      · rw [abs_of_nonneg hcenter0, abs_sub_comm]
        exact (mul_le_mul_of_nonneg_right hcenter1 (abs_nonneg _)).trans_lt
          (by simpa using hcos)
    _ = 1 / 10 ^ 15 + 3 / 10 ^ 15 := by norm_num

/-- Uniform kernel-checked analytic error for the fully rationalized defect.
The `2·10⁻¹⁴` budget includes the infinite digamma remainder, rational tail
centers, prime-amplitude center, logarithm center, and cosine Taylor tail. -/
theorem abs_p2Omega_sub_alpha_sub_rationalDefectApprox_lt
    {r : ℝ} (hr : |r| ≤ 50) :
    |(GlideKernel.p2Omega r - GlideKernel.p2Alpha) -
        p2RationalDefectApprox r| < 2 / 10 ^ 14 := by
  have hseries := abs_quarterDifference_tsum_sub_approx_lt_1e14 hr
  have hrational := abs_quarterDifferenceApprox_sub_rational_lt hr
  have hquarter :
      |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
          p2RationalQuarterDifferenceApprox r| <
        1 / 10 ^ 14 + 1 / 10 ^ 17 := by
    calc
      |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
          p2RationalQuarterDifferenceApprox r| ≤
        |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
            quarterDifferenceApprox r 16 64| +
          |quarterDifferenceApprox r 16 64 -
            p2RationalQuarterDifferenceApprox r| := abs_sub_le _ _ _
      _ < 1 / 10 ^ 14 + 1 / 10 ^ 17 := add_lt_add hseries hrational
  have hprime := abs_prime_term_sub_rational_lt hr
  rw [GlideKernel.p2Omega_sub_alpha_eq_series]
  unfold p2RationalDefectApprox
  rw [show
      ((∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) +
          GlideKernel.p2PrimeAmplitude *
            (1 - Real.cos (r * Real.log 2))) -
          (p2RationalQuarterDifferenceApprox r +
            p2PrimeAmplitudeCenter *
              (1 - cosTaylor 128 (r * p2LogTwoCenter))) =
        ((∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
          p2RationalQuarterDifferenceApprox r) +
        (GlideKernel.p2PrimeAmplitude *
            (1 - Real.cos (r * Real.log 2)) -
          p2PrimeAmplitudeCenter *
            (1 - cosTaylor 128 (r * p2LogTwoCenter))) by ring]
  calc
    |((∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
          p2RationalQuarterDifferenceApprox r) +
        (GlideKernel.p2PrimeAmplitude *
            (1 - Real.cos (r * Real.log 2)) -
          p2PrimeAmplitudeCenter *
            (1 - cosTaylor 128 (r * p2LogTwoCenter)))| ≤
      |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
          p2RationalQuarterDifferenceApprox r| +
        |GlideKernel.p2PrimeAmplitude *
            (1 - Real.cos (r * Real.log 2)) -
          p2PrimeAmplitudeCenter *
            (1 - cosTaylor 128 (r * p2LogTwoCenter))| := abs_add_le _ _
    _ < (1 / 10 ^ 14 + 1 / 10 ^ 17) +
        (1 / 10 ^ 15 + 3 / 10 ^ 15) := add_lt_add hquarter hprime
    _ < 2 / 10 ^ 14 := by norm_num

end RHP2Bridge
