/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.P2Symbol
import Mathlib.Analysis.Real.Pi.Bounds

/-!
# Elementary constant certificates for the canonical `p = 2` endpoint

This module gives narrow rational enclosures for the elementary constants in
the scalar entry formula: `log 2`, `π`, reciprocal Fourier normalizations,
and the square roots occurring in the prime amplitude and normalized
Legendre basis.  The logarithmic bounds use finite positive atanh series with
their analytic remainder; the bounds for `π` reuse Mathlib's kernel-checked
20-digit theorem; square-root bounds reduce to exact rational squaring.

No floating-point or native evaluation is used.
-/

namespace RHP2Bridge

open Set

/-- A reusable certificate interface for rational square-root enclosures. -/
theorem sqrt_mem_Ioo_of_sq_lt {x l u : ℝ}
    (hx : 0 ≤ x) (hl : 0 ≤ l) (hu : 0 ≤ u)
    (hlo : l ^ 2 < x) (hhi : x < u ^ 2) :
    Real.sqrt x ∈ Ioo l u := by
  constructor
  · exact (Real.lt_sqrt hl).2 hlo
  · exact (Real.sqrt_lt hx hu).2 hhi

/-- Reciprocation reverses a strictly positive rational enclosure. -/
theorem inv_mem_Ioo_of_mem_Ioo {x l u : ℝ} (hl : 0 < l)
    (hx : x ∈ Ioo l u) : x⁻¹ ∈ Ioo u⁻¹ l⁻¹ := by
  have hx0 : 0 < x := hl.trans hx.1
  constructor
  · simpa only [one_div] using one_div_lt_one_div_of_lt hx0 hx.2
  · simpa only [one_div] using one_div_lt_one_div_of_lt hl hx.1

theorem log_two_gt_6931471805599453e16 :
    (6931471805599453 : ℝ) / 10000000000000000 < Real.log 2 := by
  have h := Real.sum_range_le_log_div
    (by norm_num : (0 : ℝ) ≤ 1 / 3) (by norm_num : (1 : ℝ) / 3 < 1) 18
  norm_num [Finset.sum_range_succ] at h
  linarith

theorem log_two_lt_6931471805599454e16 :
    Real.log 2 < (6931471805599454 : ℝ) / 10000000000000000 := by
  have h := Real.log_div_le_sum_range_add
    (by norm_num : (0 : ℝ) ≤ 1 / 3) (by norm_num : (1 : ℝ) / 3 < 1) 18
  norm_num [Finset.sum_range_succ] at h
  linarith

/-- A width-`10⁻¹⁶` rational enclosure of `log 2`. -/
theorem log_two_mem_Ioo_16 :
    Real.log 2 ∈
      Ioo ((6931471805599453 : ℝ) / 10000000000000000)
        ((6931471805599454 : ℝ) / 10000000000000000) :=
  ⟨log_two_gt_6931471805599453e16,
    log_two_lt_6931471805599454e16⟩

theorem pi_gt_314159265358979323846e20 :
    (314159265358979323846 : ℝ) / 100000000000000000000 < Real.pi := by
  convert Real.pi_gt_d20 using 1
  norm_num

theorem pi_lt_314159265358979323847e20 :
    Real.pi < (314159265358979323847 : ℝ) / 100000000000000000000 := by
  convert Real.pi_lt_d20 using 1
  norm_num

/-- Mathlib's width-`10⁻²⁰` rational enclosure of `π`, in fraction form. -/
theorem pi_mem_Ioo_20 :
    Real.pi ∈
      Ioo ((314159265358979323846 : ℝ) / 100000000000000000000)
        ((314159265358979323847 : ℝ) / 100000000000000000000) :=
  ⟨pi_gt_314159265358979323846e20,
    pi_lt_314159265358979323847e20⟩

theorem log_pi_gt_1144729885849400e15 :
    (1144729885849400 : ℝ) / 1000000000000000 < Real.log Real.pi := by
  let q : ℝ := 314159265358979323846 / 100000000000000000000
  let x : ℝ := (q - 1) / (q + 1)
  have hqpi : q < Real.pi := by
    simpa [q] using pi_gt_314159265358979323846e20
  have hq0 : 0 < q := by dsimp [q]; norm_num
  have hlog : Real.log q < Real.log Real.pi :=
    Real.strictMonoOn_log hq0 Real.pi_pos hqpi
  have hx0 : 0 ≤ x := by dsimp [x, q]; norm_num
  have hx1 : x < 1 := by dsimp [x, q]; norm_num
  have hs := Real.sum_range_le_log_div hx0 hx1 28
  have hratio : (1 + x) / (1 - x) = q := by
    dsimp [x]
    have hq1 : q + 1 ≠ 0 := by positivity
    field_simp
    ring
  rw [hratio] at hs
  have hq :
      (1144729885849400 : ℝ) / 1000000000000000 < Real.log q := by
    norm_num [x, q, Finset.sum_range_succ] at hs ⊢
    linarith
  exact hq.trans hlog

theorem log_pi_lt_1144729885849401e15 :
    Real.log Real.pi <
      (1144729885849401 : ℝ) / 1000000000000000 := by
  let q : ℝ := 314159265358979323847 / 100000000000000000000
  let x : ℝ := (q - 1) / (q + 1)
  have hpiq : Real.pi < q := by
    simpa [q] using pi_lt_314159265358979323847e20
  have hq0 : 0 < q := by dsimp [q]; norm_num
  have hlog : Real.log Real.pi < Real.log q :=
    Real.strictMonoOn_log Real.pi_pos hq0 hpiq
  have hx0 : 0 ≤ x := by dsimp [x, q]; norm_num
  have hx1 : x < 1 := by dsimp [x, q]; norm_num
  have hs := Real.log_div_le_sum_range_add hx0 hx1 28
  have hratio : (1 + x) / (1 - x) = q := by
    dsimp [x]
    have hq1 : q + 1 ≠ 0 := by positivity
    field_simp
    ring
  rw [hratio] at hs
  have hq : Real.log q <
      (1144729885849401 : ℝ) / 1000000000000000 := by
    norm_num [x, q, Finset.sum_range_succ] at hs ⊢
    linarith
  exact hlog.trans hq

/-- A width-`10⁻¹⁵` rational enclosure of `log π`. -/
theorem log_pi_mem_Ioo_15 :
    Real.log Real.pi ∈
      Ioo ((1144729885849400 : ℝ) / 1000000000000000)
        ((1144729885849401 : ℝ) / 1000000000000000) :=
  ⟨log_pi_gt_1144729885849400e15,
    log_pi_lt_1144729885849401e15⟩

theorem inv_pi_gt_31830988618379067153e20 :
    (31830988618379067153 : ℝ) / 100000000000000000000 < Real.pi⁻¹ := by
  have hrecip :
      1 / ((314159265358979323847 : ℝ) / 100000000000000000000) <
        1 / Real.pi :=
    one_div_lt_one_div_of_lt Real.pi_pos
      pi_lt_314159265358979323847e20
  rw [one_div] at hrecip
  have hrat :
      (31830988618379067153 : ℝ) / 100000000000000000000 <
        ((314159265358979323847 : ℝ) / 100000000000000000000)⁻¹ := by
    norm_num
  simpa only [one_div] using hrat.trans hrecip

theorem inv_pi_lt_31830988618379067154e20 :
    Real.pi⁻¹ <
      (31830988618379067154 : ℝ) / 100000000000000000000 := by
  have hrecip :
      1 / Real.pi <
        1 / ((314159265358979323846 : ℝ) / 100000000000000000000) :=
    one_div_lt_one_div_of_lt (by norm_num)
      pi_gt_314159265358979323846e20
  rw [one_div] at hrecip
  exact hrecip.trans (by norm_num)

/-- A width-`10⁻²⁰` enclosure of `π⁻¹`. -/
theorem inv_pi_mem_Ioo_20 :
    Real.pi⁻¹ ∈
      Ioo ((31830988618379067153 : ℝ) / 100000000000000000000)
        ((31830988618379067154 : ℝ) / 100000000000000000000) :=
  ⟨inv_pi_gt_31830988618379067153e20,
    inv_pi_lt_31830988618379067154e20⟩

theorem inv_two_pi_gt_15915494309189533576e20 :
    (15915494309189533576 : ℝ) / 100000000000000000000 <
      1 / (2 * Real.pi) := by
  have hrecip :
      1 / (2 * ((314159265358979323847 : ℝ) /
          100000000000000000000)) < 1 / (2 * Real.pi) :=
    one_div_lt_one_div_of_lt (by positivity)
      (mul_lt_mul_of_pos_left pi_lt_314159265358979323847e20 (by norm_num))
  have hrat :
      (15915494309189533576 : ℝ) / 100000000000000000000 <
        1 / (2 * ((314159265358979323847 : ℝ) /
          100000000000000000000)) := by
    norm_num
  exact hrat.trans hrecip

theorem inv_two_pi_lt_15915494309189533577e20 :
    1 / (2 * Real.pi) <
      (15915494309189533577 : ℝ) / 100000000000000000000 := by
  have hrecip :
      1 / (2 * Real.pi) <
        1 / (2 * ((314159265358979323846 : ℝ) /
          100000000000000000000)) :=
    one_div_lt_one_div_of_lt (by norm_num)
      (mul_lt_mul_of_pos_left pi_gt_314159265358979323846e20 (by norm_num))
  exact hrecip.trans (by norm_num)

/-- The exact Fourier factor in the scalar entry formula, enclosed to
`10⁻²⁰`. -/
theorem inv_two_pi_mem_Ioo_20 :
    1 / (2 * Real.pi) ∈
      Ioo ((15915494309189533576 : ℝ) / 100000000000000000000)
        ((15915494309189533577 : ℝ) / 100000000000000000000) :=
  ⟨inv_two_pi_gt_15915494309189533576e20,
    inv_two_pi_lt_15915494309189533577e20⟩

/-- A width-`10⁻¹⁵` rational enclosure of `√2`. -/
theorem sqrt_two_mem_Ioo_15 :
    Real.sqrt 2 ∈
      Ioo ((1414213562373095 : ℝ) / 1000000000000000)
        ((1414213562373096 : ℝ) / 1000000000000000) := by
  apply sqrt_mem_Ioo_of_sq_lt <;> norm_num

/-- A width-`10⁻¹⁵` enclosure of `1 / √2`. -/
theorem inv_sqrt_two_mem_Ioo_15 :
    (Real.sqrt 2)⁻¹ ∈
      Ioo ((707106781186547 : ℝ) / 1000000000000000)
        ((707106781186548 : ℝ) / 1000000000000000) := by
  have h := inv_mem_Ioo_of_mem_Ioo (by norm_num)
    sqrt_two_mem_Ioo_15
  constructor
  · calc
      (707106781186547 : ℝ) / 1000000000000000 <
          ((1414213562373096 : ℝ) / 1000000000000000)⁻¹ := by norm_num
      _ < (Real.sqrt 2)⁻¹ := h.1
  · calc
      (Real.sqrt 2)⁻¹ <
          ((1414213562373095 : ℝ) / 1000000000000000)⁻¹ := h.2
      _ < (707106781186548 : ℝ) / 1000000000000000 := by norm_num

/-- A width-`10⁻¹⁵` enclosure of the interval-scale square root `√(7/16)`. -/
theorem sqrt_seven_sixteenths_mem_Ioo_15 :
    Real.sqrt (7 / 16 : ℝ) ∈
      Ioo ((661437827766147 : ℝ) / 1000000000000000)
        ((661437827766148 : ℝ) / 1000000000000000) := by
  apply sqrt_mem_Ioo_of_sq_lt <;> norm_num

private theorem sqrt_seven_sixteenths_mem_Ioo_17 :
    Real.sqrt (7 / 16 : ℝ) ∈
      Ioo ((66143782776614764 : ℝ) / 100000000000000000)
        ((66143782776614765 : ℝ) / 100000000000000000) := by
  apply sqrt_mem_Ioo_of_sq_lt <;> norm_num

/-- A width-`10⁻¹⁵` enclosure of the unitary dilation factor
`√(7/16)⁻¹` used by every canonical basis mode. -/
theorem inv_sqrt_seven_sixteenths_mem_Ioo_15 :
    (Real.sqrt (7 / 16 : ℝ))⁻¹ ∈
      Ioo ((1511857892036908 : ℝ) / 1000000000000000)
        ((1511857892036909 : ℝ) / 1000000000000000) := by
  have h := inv_mem_Ioo_of_mem_Ioo (by norm_num)
    sqrt_seven_sixteenths_mem_Ioo_17
  constructor
  · calc
      (1511857892036908 : ℝ) / 1000000000000000 <
          ((66143782776614765 : ℝ) / 100000000000000000)⁻¹ := by norm_num
      _ < (Real.sqrt (7 / 16 : ℝ))⁻¹ := h.1
  · calc
      (Real.sqrt (7 / 16 : ℝ))⁻¹ <
          ((66143782776614764 : ℝ) / 100000000000000000)⁻¹ := h.2
      _ < (1511857892036909 : ℝ) / 1000000000000000 := by norm_num

/-- A width-`10⁻¹⁵` enclosure of the prime oscillation amplitude in
`GlideKernel.p2Omega`. -/
theorem p2PrimeAmplitude_mem_Ioo_15 :
    GlideKernel.p2PrimeAmplitude ∈
      Ioo ((980258143468547 : ℝ) / 1000000000000000)
        ((980258143468548 : ℝ) / 1000000000000000) := by
  have hs := sqrt_two_mem_Ioo_15
  have hl := log_two_mem_Ioo_16
  have hs0 : 0 < Real.sqrt 2 := Real.sqrt_pos.2 (by norm_num)
  have hl0 : 0 < Real.log 2 := Real.log_pos (by norm_num)
  unfold GlideKernel.p2PrimeAmplitude
  constructor
  · have hprod :
        ((1414213562373095 : ℝ) / 1000000000000000) *
            ((6931471805599453 : ℝ) / 10000000000000000) <
          Real.sqrt 2 * Real.log 2 := by
      calc
        ((1414213562373095 : ℝ) / 1000000000000000) *
              ((6931471805599453 : ℝ) / 10000000000000000) ≤
            Real.sqrt 2 *
              ((6931471805599453 : ℝ) / 10000000000000000) :=
          mul_le_mul_of_nonneg_right hs.1.le (by norm_num)
        _ < Real.sqrt 2 * Real.log 2 :=
          mul_lt_mul_of_pos_left hl.1 hs0
    calc
      (980258143468547 : ℝ) / 1000000000000000 <
          ((1414213562373095 : ℝ) / 1000000000000000) *
            ((6931471805599453 : ℝ) / 10000000000000000) := by norm_num
      _ < Real.sqrt 2 * Real.log 2 := hprod
  · have hprod : Real.sqrt 2 * Real.log 2 <
        ((1414213562373096 : ℝ) / 1000000000000000) *
          ((6931471805599454 : ℝ) / 10000000000000000) := by
      calc
        Real.sqrt 2 * Real.log 2 ≤
            ((1414213562373096 : ℝ) / 1000000000000000) * Real.log 2 :=
          mul_le_mul_of_nonneg_right hs.2.le hl0.le
        _ < ((1414213562373096 : ℝ) / 1000000000000000) *
              ((6931471805599454 : ℝ) / 10000000000000000) :=
          mul_lt_mul_of_pos_left hl.2 (by norm_num)
    exact hprod.trans (by norm_num)

end RHP2Bridge
