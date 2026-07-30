/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreTail
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Certified polynomial approximations for spherical Bessel integrals

This module gives an explicit finite-sum formula for the moments of the
Rodrigues weight, packages those moments into a computable polynomial model
for the spherical-Bessel integral, and proves a uniform factorial-decay
remainder bound.  The final theorem is intended as the analytic-error bridge
for kernel-checked enclosures of the canonical `p = 2` matrix entries.
-/

namespace RHP2Bridge

open scoped BigOperators

noncomputable def weightMoment (n m : ℕ) : ℝ :=
  ∑ l ∈ Finset.range (n + 1),
    (-1 : ℝ) ^ (l + n) * (n.choose l : ℝ) *
      ((1 : ℝ) ^ (m + 2 * (n - l) + 1) -
        (-1 : ℝ) ^ (m + 2 * (n - l) + 1)) /
          (m + 2 * (n - l) + 1 : ℝ)

theorem integral_pow_mul_weight_eq_weightMoment (n m : ℕ) :
    (∫ t in (-1 : ℝ)..1, t ^ m * (1 - t ^ 2) ^ n) =
      weightMoment n m := by
  have hexpand (t : ℝ) :
      t ^ m * (1 - t ^ 2) ^ n =
        ∑ l ∈ Finset.range (n + 1),
          (-1 : ℝ) ^ (l + n) *
            (t ^ m * (1 ^ l * (t ^ 2) ^ (n-l) * (n.choose l : ℝ))) := by
    rw [sub_pow]
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro l hl
    ring
  rw [intervalIntegral.integral_congr (fun t _ => hexpand t)]
  rw [intervalIntegral.integral_finsetSum]
  · unfold weightMoment
    apply Finset.sum_congr rfl
    intro l hl
    let c : ℝ := (-1 : ℝ) ^ (l+n) * (n.choose l : ℝ)
    let p : ℕ := m + 2 * (n-l)
    calc
      (∫ t in (-1 : ℝ)..1,
          (-1) ^ (l + n) *
            (t ^ m * (1 ^ l * (t ^ 2) ^ (n-l) * (n.choose l : ℝ)))) =
          ∫ t in (-1 : ℝ)..1, c * t^p := by
        apply intervalIntegral.integral_congr
        intro t _
        dsimp [c, p]
        simp only [one_pow, one_mul, pow_mul, pow_add]
        ring
      _ = c * (∫ t in (-1 : ℝ)..1, t^p) := by
        rw [intervalIntegral.integral_const_mul]
      _ = _ := by
        have hln : l ≤ n := by
          simp only [Finset.mem_range] at hl
          omega
        rw [integral_pow]
        dsimp [c, p]
        push_cast
        rw [Nat.cast_sub hln]
        ring
  · intro l hl
    apply Continuous.intervalIntegrable
    fun_prop

noncomputable def sphericalJPolynomial (n N : ℕ) (z : ℝ) : ℂ :=
  ((z ^ n / (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ) *
    ∑ m ∈ Finset.range N,
      (((z : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)) *
        (weightMoment n m : ℂ)

theorem sphericalJPolynomial_eq_integral (n N : ℕ) (z : ℝ) :
    sphericalJPolynomial n N z =
      ((z ^ n / (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ) *
        ∫ t in (-1 : ℝ)..1,
          (∑ m ∈ Finset.range N,
            (((z * t : ℝ) : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)) *
              (((1 - t ^ 2) ^ n : ℝ) : ℂ) := by
  unfold sphericalJPolynomial
  congr 1
  have hexpand (t : ℝ) :
      (∑ m ∈ Finset.range N,
        (((z * t : ℝ) : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)) *
          (((1 - t ^ 2) ^ n : ℝ) : ℂ) =
        ∑ m ∈ Finset.range N,
          ((((z * t : ℝ) : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)) *
            (((1 - t ^ 2) ^ n : ℝ) : ℂ) := by
    rw [Finset.sum_mul]
  rw [intervalIntegral.integral_congr (fun t _ => hexpand t)]
  rw [intervalIntegral.integral_finsetSum]
  · apply Finset.sum_congr rfl
    intro m hm
    let c : ℂ := ((z : ℂ) * Complex.I)^m / (m.factorial : ℂ)
    calc
      ((z : ℂ) * Complex.I)^m / (m.factorial : ℂ) *
          (weightMoment n m : ℂ) =
        c * ((∫ t in (-1 : ℝ)..1, t^m * (1-t^2)^n : ℝ) : ℂ) := by
          rw [integral_pow_mul_weight_eq_weightMoment]
      _ = c * (∫ t in (-1 : ℝ)..1,
          (((t^m * (1-t^2)^n : ℝ) : ℂ))) := by
          rw [intervalIntegral.integral_ofReal]
      _ = ∫ t in (-1 : ℝ)..1,
          c * (((t^m * (1-t^2)^n : ℝ) : ℂ)) := by
          rw [intervalIntegral.integral_const_mul]
      _ = _ := by
        apply intervalIntegral.integral_congr
        intro t _
        dsimp [c]
        push_cast
        ring
  · intro m hm
    apply Continuous.intervalIntegrable
    fun_prop

set_option maxHeartbeats 1000000 in
-- The uniform pointwise-to-integral remainder calculation exceeds the default budget.
theorem norm_sphericalJIntegralModel_sub_polynomial_le
    (n N : ℕ) (z Z : ℝ) (hZ : |z| ≤ Z)
    (hN : Z / (N + 1 : ℝ) ≤ 1 / 2) :
    ‖LegendreTail.sphericalJIntegralModel n z - sphericalJPolynomial n N z‖ ≤
      2 * Z ^ (n + N) /
        ((2 : ℝ) ^ n * (n.factorial : ℝ) * (N.factorial : ℝ)) := by
  rw [LegendreTail.sphericalJIntegralModel,
    sphericalJPolynomial_eq_integral]
  rw [← mul_sub]
  rw [← intervalIntegral.integral_sub]
  · rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_div,
      abs_pow, abs_of_pos (by positivity : 0 < (2 : ℝ) ^ (n+1) * n.factorial)]
    have hpoint (t : ℝ) (ht : t ∈ Set.uIcc (-1 : ℝ) 1) :
        ‖(Complex.exp ((z * t : ℝ) * Complex.I) *
              (((1 - t ^ 2) ^ n : ℝ) : ℂ) -
            (∑ m ∈ Finset.range N,
              (((z * t : ℝ) : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)) *
              (((1 - t ^ 2) ^ n : ℝ) : ℂ))‖ ≤
          (2 * Z ^ N / (N.factorial : ℝ)) * (1 - t ^ 2) ^ n := by
      rw [← sub_mul, norm_mul, Complex.norm_real, Real.norm_eq_abs]
      rw [Set.uIcc_of_le (by norm_num)] at ht
      have ht_abs : |t| ≤ 1 := abs_le.mpr ⟨by linarith [ht.1], ht.2⟩
      have hweight : 0 ≤ (1 - t ^ 2) ^ n := by
        have ht_sq : t^2 ≤ (1 : ℝ) := by
          calc
            t^2 = |t|^2 := (sq_abs t).symm
            _ ≤ (1 : ℝ)^2 := pow_le_pow_left₀ (abs_nonneg t) ht_abs 2
            _ = 1 := by norm_num
        positivity
      rw [abs_of_nonneg hweight]
      have hxnorm : ‖((z * t : ℝ) : ℂ) * Complex.I‖ ≤ Z := by
        simp only [Complex.norm_mul, Complex.norm_real, Real.norm_eq_abs,
          abs_mul, Complex.norm_I, mul_one]
        calc
          |z| * |t| ≤ |z| * 1 := mul_le_mul_of_nonneg_left ht_abs (abs_nonneg z)
          _ = |z| := mul_one _
          _ ≤ Z := hZ
      have hx : ‖((z * t : ℝ) : ℂ) * Complex.I‖ /
          (N.succ : ℝ) ≤ 1 / 2 := by
        calc
          _ ≤ Z / (N.succ : ℝ) := div_le_div_of_nonneg_right hxnorm (by positivity)
          _ ≤ _ := by simpa [Nat.cast_succ] using hN
      have he := Complex.exp_bound' (x := (((z * t : ℝ) : ℂ) * Complex.I))
        (n := N) hx
      calc
        ‖Complex.exp (((z * t : ℝ) : ℂ) * Complex.I) -
            ∑ m ∈ Finset.range N,
              (((z * t : ℝ) : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)‖ *
              (1 - t ^ 2) ^ n ≤
            (‖(((z * t : ℝ) : ℂ) * Complex.I)‖ ^ N /
              (N.factorial : ℝ) * 2) * (1 - t ^ 2) ^ n :=
          mul_le_mul_of_nonneg_right he hweight
        _ ≤ (2 * Z ^ N / (N.factorial : ℝ)) * (1 - t ^ 2) ^ n := by
          have hp := pow_le_pow_left₀ (norm_nonneg _) hxnorm N
          have hfac : 0 < (N.factorial : ℝ) := by positivity
          have hcoef :
            ‖(((z*t : ℝ) : ℂ) * Complex.I)‖^N / (N.factorial : ℝ) * 2 ≤
                2 * Z^N / (N.factorial : ℝ) := by
            calc
              _ ≤ Z^N / (N.factorial : ℝ) * 2 := by gcongr
              _ = 2 * Z^N / (N.factorial : ℝ) := by ring
          exact mul_le_mul_of_nonneg_right hcoef hweight
    have hint := intervalIntegral.norm_integral_le_of_norm_le_const
      (f := fun t : ℝ =>
        Complex.exp ((z * t : ℝ) * Complex.I) * (((1-t^2)^n : ℝ) : ℂ) -
          (∑ m ∈ Finset.range N,
            (((z*t : ℝ) : ℂ) * Complex.I)^m / (m.factorial : ℂ)) *
              (((1-t^2)^n : ℝ) : ℂ))
      (C := 2 * Z^N / (N.factorial : ℝ)) (a := -1) (b := 1) (by
        intro t ht
        have ht' : t ∈ Set.uIcc (-1 : ℝ) 1 := by
          rw [Set.uIoc_of_le (by norm_num)] at ht
          rw [Set.uIcc_of_le (by norm_num)]
          exact ⟨ht.1.le, ht.2⟩
        exact (hpoint t ht').trans (by
          have hw : (1-t^2)^n ≤ 1 := by
            rw [Set.uIcc_of_le (by norm_num)] at ht'
            have ht_abs : |t| ≤ 1 := abs_le.mpr ⟨by linarith [ht'.1], ht'.2⟩
            have ht2 : 0 ≤ 1-t^2 := by
              have ht_sq : t^2 ≤ (1 : ℝ) := by
                calc
                  t^2 = |t|^2 := (sq_abs t).symm
                  _ ≤ (1 : ℝ)^2 := pow_le_pow_left₀ (abs_nonneg t) ht_abs 2
                  _ = 1 := by norm_num
              linarith
            have ht2one : 1-t^2 ≤ 1 := by nlinarith [sq_nonneg t]
            exact pow_le_one₀ ht2 ht2one
          have hZ0 : 0 ≤ Z := (abs_nonneg z).trans hZ
          have hc : 0 ≤ 2 * Z^N / (N.factorial : ℝ) := by positivity
          nlinarith))
    norm_num at hint
    have hint' :
        ‖∫ t in (-1 : ℝ)..1,
          (Complex.exp ((z * t : ℝ) * Complex.I) * (((1-t^2)^n : ℝ) : ℂ) -
            (∑ m ∈ Finset.range N,
              (((z*t : ℝ) : ℂ) * Complex.I)^m / (m.factorial : ℂ)) *
                (((1-t^2)^n : ℝ) : ℂ))‖ ≤ 4 * Z^N / N.factorial := by
      have hrhs : 2 * Z^N / (N.factorial : ℝ) * 2 =
          4 * Z^N / (N.factorial : ℝ) := by ring
      simpa [Complex.ofReal_mul, Complex.ofReal_sub, Complex.ofReal_pow,
        mul_assoc] using hint.trans_eq hrhs
    calc
      |z| ^ n / ((2 : ℝ) ^ (n+1) * n.factorial) *
          ‖∫ t in (-1 : ℝ)..1,
            (Complex.exp ((z * t : ℝ) * Complex.I) * (((1-t^2)^n : ℝ) : ℂ) -
              (∑ m ∈ Finset.range N,
                (((z*t : ℝ) : ℂ) * Complex.I)^m / (m.factorial : ℂ)) *
                  (((1-t^2)^n : ℝ) : ℂ))‖ ≤
        |z| ^ n / ((2 : ℝ) ^ (n+1) * n.factorial) *
          (4 * Z^N / N.factorial) :=
        mul_le_mul_of_nonneg_left hint' (by positivity)
      _ ≤ 2 * Z ^ (n+N) /
          ((2 : ℝ)^n * n.factorial * N.factorial) := by
        have hZ0 : 0 ≤ Z := (abs_nonneg z).trans hZ
        have hp := pow_le_pow_left₀ (abs_nonneg z) hZ n
        calc
          |z| ^ n / ((2 : ℝ) ^ (n+1) * n.factorial) *
              (4 * Z^N / N.factorial) ≤
            Z^n / ((2 : ℝ) ^ (n+1) * n.factorial) *
              (4 * Z^N / N.factorial) := by
                gcongr
          _ = 2 * Z^(n+N) /
              ((2 : ℝ)^n * n.factorial * N.factorial) := by
                field_simp
                rw [pow_add, pow_succ]
                ring
  all_goals
    apply Continuous.intervalIntegrable
    fun_prop

end RHP2Bridge
