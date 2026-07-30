/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.GammaUniform

/-!
# A directed numerical upper bound for Euler's constant

This file proves a rapidly convergent Euler--Maclaurin-style upper enclosure
using only the harmonic limit already in Mathlib and the positive atanh series
for `log ((n+1)/n)`.  The final decimal is a theorem over `ℝ`; no native
evaluation or untrusted numerical oracle is used.
-/

open Filter Set
open scoped Topology

namespace GlideKernel

private lemma log_succ_div_lower_two (n : ℕ) (hn : 1 ≤ n) :
    (2 : ℝ) / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) ≤
      Real.log ((n + 1 : ℝ) / n) := by
  let x : ℝ := 1 / (2 * n + 1)
  have hx0 : 0 ≤ x := by dsimp [x]; positivity
  have hx1 : x < 1 := by
    dsimp [x]
    rw [div_lt_one (by positivity)]
    norm_num
    omega
  have h := Real.sum_range_le_log_div hx0 hx1 2
  norm_num [x, Finset.sum_range_succ] at h
  have hratio :
      ((1 : ℝ) + 1 / (2 * n + 1)) / (1 - 1 / (2 * n + 1)) =
        (n + 1 : ℝ) / n := by
    have hnR : (n : ℝ) ≠ 0 := by positivity
    field_simp
    ring
  have hratio' :
      ((1 : ℝ) + (2 * n + 1 : ℝ)⁻¹) / (1 - (2 * n + 1 : ℝ)⁻¹) =
        (n + 1 : ℝ) / n := by
    simpa only [one_div] using hratio
  rw [hratio'] at h
  have hmul := mul_le_mul_of_nonneg_left h (by norm_num : (0 : ℝ) ≤ 2)
  calc
    (2 : ℝ) / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) =
        2 * ((2 * (n : ℝ) + 1)⁻¹ + ((2 * (n : ℝ) + 1) ^ 3)⁻¹ / 3) := by
      have ha : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
      field_simp
    _ ≤ 2 * (1 / 2 * Real.log ((n + 1 : ℝ) / n)) := hmul
    _ = Real.log ((n + 1 : ℝ) / n) := by ring

private lemma log_succ_div_upper_three (n : ℕ) (hn : 1 ≤ n) :
    Real.log ((n + 1 : ℝ) / n) ≤
      2 / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) +
        2 / (5 * (2 * n + 1) ^ 5) +
          1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5) := by
  let x : ℝ := 1 / (2 * n + 1)
  have hx0 : 0 ≤ x := by dsimp [x]; positivity
  have hx1 : x < 1 := by
    dsimp [x]
    rw [div_lt_one (by positivity)]
    norm_num
    omega
  have h := Real.log_div_le_sum_range_add hx0 hx1 3
  dsimp [x] at h
  have hratio :
      ((1 : ℝ) + 1 / (2 * n + 1)) / (1 - 1 / (2 * n + 1)) =
        (n + 1 : ℝ) / n := by
    have hnR : (n : ℝ) ≠ 0 := by positivity
    field_simp
    ring
  rw [hratio] at h
  have hmul := mul_le_mul_of_nonneg_left h (by norm_num : (0 : ℝ) ≤ 2)
  have hsub :
      0 < 1 - (1 / (2 * (n : ℝ) + 1)) ^ 2 := by
    have hx2 : x ^ 2 < 1 := (sq_lt_one_iff₀ hx0).2 hx1
    simpa [x] using sub_pos.mpr hx2
  have htail :
      2 * ((1 / (2 * (n : ℝ) + 1)) ^ 7 /
        (1 - (1 / (2 * (n : ℝ) + 1)) ^ 2)) =
          1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5) := by
    have hn0 : (n : ℝ) ≠ 0 := by positivity
    field_simp [ne_of_gt hsub]
    rw [show (2 * (n : ℝ) + 1) ^ 2 - 1 =
      4 * (n : ℝ) * (n + 1) by ring]
    convert div_self (by positivity : 4 * (n : ℝ) * (n + 1) ≠ 0) using 1 <;>
      norm_num
  calc
    Real.log ((n + 1 : ℝ) / n) =
        2 * (1 / 2 * Real.log ((n + 1 : ℝ) / n)) := by ring
    _ ≤ 2 *
        ((∑ i ∈ Finset.range 3,
          (1 / (2 * (n : ℝ) + 1)) ^ (2 * i + 1) / (2 * i + 1)) +
            (1 / (2 * (n : ℝ) + 1)) ^ (2 * 3 + 1) /
              (1 - (1 / (2 * (n : ℝ) + 1)) ^ 2)) := hmul
    _ = 2 * (∑ i ∈ Finset.range 3,
          (1 / (2 * (n : ℝ) + 1)) ^ (2 * i + 1) / (2 * i + 1)) +
          1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5) := by
      rw [mul_add, htail]
    _ = 2 / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) +
        2 / (5 * (2 * n + 1) ^ 5) +
          1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5) := by
      have hn0 : (n : ℝ) ≠ 0 := by positivity
      norm_num [Finset.sum_range_succ]
      field_simp

/-- A corrected harmonic upper approximant to Euler's constant. -/
noncomputable def refinedEulerUpper (n : ℕ) : ℝ :=
  (harmonic n : ℝ) - Real.log n - 1 / (2 * n) + 1 / (12 * n ^ 2)

/-- The fourth-order correction to `refinedEulerUpper`, approaching Euler's
constant from below. -/
noncomputable def refinedEulerLower (n : ℕ) : ℝ :=
  refinedEulerUpper n - 1 / (120 * n ^ 4)

private lemma refined_rational_correction_le (n : ℕ) (hn : 1 ≤ n) :
    (1 : ℝ) / (2 * n) + 1 / (2 * (n + 1)) -
        (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2)) ≤
      2 / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) := by
  have hid :
      (2 : ℝ) / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) -
          (1 / (2 * n) + 1 / (2 * (n + 1)) -
            (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2))) =
        (2 * (n : ℝ) ^ 2 + 2 * n + 1) /
          (12 * n ^ 2 * (n + 1) ^ 2 * (2 * n + 1) ^ 3) := by
    have hn0 : (n : ℝ) ≠ 0 := by positivity
    field_simp
    ring
  rw [← sub_nonneg, hid]
  positivity

private lemma refined_rational_correction_ge (n : ℕ) (hn : 1 ≤ n) :
    (2 : ℝ) / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) +
          2 / (5 * (2 * n + 1) ^ 5) +
            1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5) ≤
      1 / (2 * n) + 1 / (2 * (n + 1)) -
          (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2)) +
            (1 / (120 * n ^ 4) - 1 / (120 * (n + 1) ^ 4)) := by
  have hid :
      (1 / (2 * n) + 1 / (2 * (n + 1)) -
            (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2)) +
              (1 / (120 * n ^ 4) - 1 / (120 * (n + 1) ^ 4))) -
          (2 / (2 * n + 1) + 2 / (3 * (2 * n + 1) ^ 3) +
            2 / (5 * (2 * n + 1) ^ 5) +
              1 / (2 * n * (n + 1) * (2 * n + 1) ^ 5)) =
        (40 * (n : ℝ) ^ 6 + 120 * n ^ 5 + 182 * n ^ 4 + 164 * n ^ 3 +
            76 * n ^ 2 + 14 * n + 1) /
          (120 * n ^ 4 * (n + 1) ^ 4 * (2 * n + 1) ^ 5) := by
    have hn0 : (n : ℝ) ≠ 0 := by positivity
    field_simp
    ring
  rw [← sub_nonneg, hid]
  positivity

private lemma refinedEulerUpper_succ_le (n : ℕ) (hn : 1 ≤ n) :
    refinedEulerUpper (n + 1) ≤ refinedEulerUpper n := by
  have hrat := refined_rational_correction_le n hn
  have hlog := log_succ_div_lower_two n hn
  have hbound := hrat.trans hlog
  have hdiff :
      refinedEulerUpper n - refinedEulerUpper (n + 1) =
        Real.log ((n + 1 : ℝ) / n) -
          (1 / (2 * n) + 1 / (2 * (n + 1)) -
            (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2))) := by
    unfold refinedEulerUpper
    rw [harmonic_succ, Rat.cast_add, Rat.cast_inv, Rat.cast_natCast]
    rw [Real.log_div (by positivity) (by positivity)]
    push_cast
    have hn0 : (n : ℝ) ≠ 0 := by positivity
    field_simp <;> ring
  rw [← sub_nonneg, hdiff]
  exact sub_nonneg.mpr hbound

private lemma refinedEulerLower_le_succ (n : ℕ) (hn : 1 ≤ n) :
    refinedEulerLower n ≤ refinedEulerLower (n + 1) := by
  have hlog := log_succ_div_upper_three n hn
  have hrat := refined_rational_correction_ge n hn
  have hbound := hlog.trans hrat
  have hdiff :
      refinedEulerLower (n + 1) - refinedEulerLower n =
        (1 / (2 * n) + 1 / (2 * (n + 1)) -
              (1 / (12 * n ^ 2) - 1 / (12 * (n + 1) ^ 2)) +
                (1 / (120 * n ^ 4) - 1 / (120 * (n + 1) ^ 4))) -
          Real.log ((n + 1 : ℝ) / n) := by
    unfold refinedEulerLower refinedEulerUpper
    rw [harmonic_succ, Rat.cast_add, Rat.cast_inv, Rat.cast_natCast]
    rw [Real.log_div (by positivity) (by positivity)]
    push_cast
    have hn0 : (n : ℝ) ≠ 0 := by positivity
    field_simp <;> ring
  rw [← sub_nonneg, hdiff]
  exact sub_nonneg.mpr hbound

private lemma antitone_refinedEulerUpper_shift :
    Antitone (fun n : ℕ => refinedEulerUpper (n + 1)) := by
  apply antitone_nat_of_succ_le
  intro n
  convert refinedEulerUpper_succ_le (n + 1) (by omega) using 1 <;> omega

private lemma monotone_refinedEulerLower_shift :
    Monotone (fun n : ℕ => refinedEulerLower (n + 1)) := by
  apply monotone_nat_of_le_succ
  intro n
  convert refinedEulerLower_le_succ (n + 1) (by omega) using 1 <;> omega

private lemma tendsto_refinedEulerUpper_shift :
    Tendsto (fun n : ℕ => refinedEulerUpper (n + 1)) atTop
      (nhds Real.eulerMascheroniConstant) := by
  have hmain := Real.tendsto_harmonic_sub_log.comp (tendsto_add_atTop_nat 1)
  have hbase : Tendsto (fun n : ℕ => (1 / (((n : ℝ) + 1)) : ℝ)) atTop
      (nhds 0) := by
    exact tendsto_const_nhds.div_atTop
      (tendsto_atTop_add_const_right atTop (1 : ℝ)
        (tendsto_natCast_atTop_atTop (R := ℝ)))
  have hc2 : Tendsto (fun _ : ℕ => (1 / 2 : ℝ)) atTop (nhds (1 / 2)) :=
    tendsto_const_nhds
  have hc12 : Tendsto (fun _ : ℕ => (1 / 12 : ℝ)) atTop (nhds (1 / 12)) :=
    tendsto_const_nhds
  have hhalf := hbase.mul hc2
  have htwelfth := (hbase.pow 2).mul hc12
  have hlim := hmain.sub hhalf |>.add htwelfth
  convert hlim using 1
  · funext n
    unfold refinedEulerUpper
    norm_num [Nat.cast_add, div_eq_mul_inv]
  · norm_num

private lemma tendsto_refinedEulerLower_shift :
    Tendsto (fun n : ℕ => refinedEulerLower (n + 1)) atTop
      (nhds Real.eulerMascheroniConstant) := by
  have hbase : Tendsto (fun n : ℕ => (1 / (((n : ℝ) + 1)) : ℝ)) atTop
      (nhds 0) := by
    exact tendsto_const_nhds.div_atTop
      (tendsto_atTop_add_const_right atTop (1 : ℝ)
        (tendsto_natCast_atTop_atTop (R := ℝ)))
  have hc120 : Tendsto (fun _ : ℕ => (1 / 120 : ℝ)) atTop
      (nhds (1 / 120)) := tendsto_const_nhds
  have hcorr0 := hc120.mul (hbase.pow 4)
  have hcorr :
      Tendsto (fun n : ℕ => (1 / (120 * ((n : ℝ) + 1) ^ 4) : ℝ)) atTop
        (nhds 0) := by
    convert hcorr0 using 1
    · funext n
      have hn1 : (n : ℝ) + 1 ≠ 0 := by positivity
      field_simp
    · norm_num
  have hlim := tendsto_refinedEulerUpper_shift.sub hcorr
  convert hlim using 1
  · funext n
    unfold refinedEulerLower
    norm_num [Nat.cast_add]
  · norm_num

lemma eulerMascheroni_le_refinedEulerUpper (n : ℕ) (hn : 1 ≤ n) :
    Real.eulerMascheroniConstant ≤ refinedEulerUpper n := by
  have h := antitone_refinedEulerUpper_shift.le_of_tendsto
    tendsto_refinedEulerUpper_shift (n - 1)
  simpa [Nat.sub_add_cancel hn] using h

lemma refinedEulerLower_le_eulerMascheroni (n : ℕ) (hn : 1 ≤ n) :
    refinedEulerLower n ≤ Real.eulerMascheroniConstant := by
  have h := monotone_refinedEulerLower_shift.ge_of_tendsto
    tendsto_refinedEulerLower_shift (n - 1)
  simpa [Nat.sub_add_cancel hn] using h

private lemma log_two_gt_69314718055994e14 :
    (69314718055994 : ℝ) / 100000000000000 < Real.log 2 := by
  have h := Real.sum_range_le_log_div
    (by norm_num : (0 : ℝ) ≤ 1 / 3) (by norm_num : (1 : ℝ) / 3 < 1) 16
  norm_num [Finset.sum_range_succ] at h
  linarith

private lemma log_two_lt_69314718055995e14 :
    Real.log 2 < (69314718055995 : ℝ) / 100000000000000 := by
  have h := Real.log_div_le_sum_range_add
    (by norm_num : (0 : ℝ) ≤ 1 / 3) (by norm_num : (1 : ℝ) / 3 < 1) 16
  norm_num [Finset.sum_range_succ] at h
  linarith

/-- A kernel-checked two-sided enclosure of width `4e-11` for Euler's
constant.  All finite arithmetic and logarithmic remainder bounds are checked
by Lean. -/
theorem eulerMascheroniConstant_mem_Ioo_57721566490_57721566494e11 :
    Real.eulerMascheroniConstant ∈
      Ioo ((57721566490 : ℝ) / 100000000000)
        ((57721566494 : ℝ) / 100000000000) := by
  have hlower := refinedEulerLower_le_eulerMascheroni 128 (by norm_num)
  have hupper := eulerMascheroni_le_refinedEulerUpper 128 (by norm_num)
  constructor
  · apply lt_of_lt_of_le ?_ hlower
    unfold refinedEulerLower refinedEulerUpper
    norm_num only [Nat.cast_ofNat]
    rw [show (128 : ℝ) = 2 ^ 7 by norm_num, Real.log_pow]
    norm_num [harmonic, Finset.sum_range_succ]
    linarith [log_two_lt_69314718055995e14]
  · apply lt_of_le_of_lt hupper
    unfold refinedEulerUpper
    norm_num only [Nat.cast_ofNat]
    rw [show (128 : ℝ) = 2 ^ 7 by norm_num, Real.log_pow]
    norm_num [harmonic, Finset.sum_range_succ]
    linarith [log_two_gt_69314718055994e14]

/-- Directed rational upper enclosure for Euler's constant. -/
theorem eulerMascheroniConstant_lt_5772161e7 :
    Real.eulerMascheroniConstant < (5772161 : ℝ) / 10000000 := by
  have h := eulerMascheroni_le_refinedEulerUpper 15 (by norm_num)
  have h3 := Real.log_three_gt_d9
  have h5 := Real.log_five_gt_d9
  have hlog : (27080502008 : ℝ) / 10000000000 < Real.log (15 : ℝ) := by
    rw [show (15 : ℝ) = 3 * 5 by norm_num,
      Real.log_mul (by norm_num) (by norm_num)]
    linarith
  unfold refinedEulerUpper at h
  norm_num [harmonic, Finset.sum_range_succ] at h ⊢
  linarith

end GlideKernel
