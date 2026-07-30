/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2ElementaryConstants

/-!
# Certified cosine polynomial for the canonical p=2 band

The p=2 prime term contains `cos (r * log 2)`.  This module exposes a
finite rational-coefficient polynomial and a uniform factorial remainder.
It is deliberately independent of numerical quadrature.
-/

namespace RHP2Bridge

open scoped BigOperators

noncomputable def cosTaylor (N : ℕ) (x : ℝ) : ℝ :=
  ∑ m ∈ Finset.range N,
    (Complex.I ^ m).re * x ^ m / (m.factorial : ℝ)

noncomputable def cosTaylorPolynomial (N : ℕ) (L : ℝ) : Polynomial ℝ :=
  ∑ m ∈ Finset.range N,
    Polynomial.C ((Complex.I ^ m).re * L ^ m / (m.factorial : ℝ)) *
      Polynomial.X ^ m

@[simp] theorem eval_cosTaylorPolynomial (N : ℕ) (L r : ℝ) :
    (cosTaylorPolynomial N L).eval r = cosTaylor N (r * L) := by
  unfold cosTaylorPolynomial cosTaylor
  simp only [Polynomial.eval_finsetSum, Polynomial.eval_mul,
    Polynomial.eval_C, Polynomial.eval_pow, Polynomial.eval_X]
  apply Finset.sum_congr rfl
  intro m hm
  rw [mul_pow]
  ring

lemma re_expPartialSum_eq_cosTaylor (N : ℕ) (x : ℝ) :
    (∑ m ∈ Finset.range N,
      (((x : ℂ) * Complex.I) ^ m / (m.factorial : ℂ))).re =
      cosTaylor N x := by
  rw [Complex.re_sum]
  unfold cosTaylor
  apply Finset.sum_congr rfl
  intro m hm
  rw [mul_pow, ← Complex.ofReal_pow]
  change ((↑(x ^ m) * Complex.I ^ m) / ((m.factorial : ℝ) : ℂ)).re = _
  rw [Complex.div_ofReal_re, Complex.mul_re]
  simp only [Complex.ofReal_re, Complex.ofReal_im, zero_mul, sub_zero]
  ring

theorem abs_cos_sub_cosTaylor_le (N : ℕ) (x Z : ℝ)
    (hx : |x| ≤ Z) (hN : Z / (N + 1 : ℝ) ≤ 1 / 2) :
    |Real.cos x - cosTaylor N x| ≤ 2 * Z ^ N / (N.factorial : ℝ) := by
  have hZ0 : 0 ≤ Z := (abs_nonneg x).trans hx
  have hxnorm : ‖(x : ℂ) * Complex.I‖ = |x| := by simp
  have hratio : ‖(x : ℂ) * Complex.I‖ / (N.succ : ℝ) ≤ 1 / 2 := by
    rw [hxnorm]
    exact (div_le_div_of_nonneg_right hx (by positivity)).trans
      (by simpa [Nat.cast_succ] using hN)
  have he := Complex.exp_bound' (x := (x : ℂ) * Complex.I) (n := N) hratio
  have hre := Complex.abs_re_le_norm
    (Complex.exp ((x : ℂ) * Complex.I) -
      ∑ m ∈ Finset.range N,
        (((x : ℂ) * Complex.I) ^ m / (m.factorial : ℂ)))
  calc
    |Real.cos x - cosTaylor N x| =
        |(Complex.exp ((x : ℂ) * Complex.I) -
          ∑ m ∈ Finset.range N,
            (((x : ℂ) * Complex.I) ^ m / (m.factorial : ℂ))).re| := by
      rw [Complex.exp_mul_I]
      simp only [Complex.sub_re, Complex.add_re, Complex.cos_ofReal_re,
        Complex.mul_re, Complex.sin_ofReal_re, Complex.sin_ofReal_im,
        Complex.I_re, Complex.I_im, mul_zero, mul_one, sub_zero,
        re_expPartialSum_eq_cosTaylor]
      ring_nf
    _ ≤ ‖Complex.exp ((x : ℂ) * Complex.I) -
          ∑ m ∈ Finset.range N,
            (((x : ℂ) * Complex.I) ^ m / (m.factorial : ℂ))‖ := hre
    _ ≤ ‖(x : ℂ) * Complex.I‖ ^ N / (N.factorial : ℝ) * 2 := he
    _ ≤ 2 * Z ^ N / (N.factorial : ℝ) := by
      rw [hxnorm]
      have hp := pow_le_pow_left₀ (abs_nonneg x) hx N
      have hfac : 0 < (N.factorial : ℝ) := by positivity
      calc
        |x| ^ N / (N.factorial : ℝ) * 2 ≤
            Z ^ N / (N.factorial : ℝ) * 2 := by gcongr
        _ = _ := by ring

/-- A single rational polynomial controls cosine throughout the whole
canonical frequency window. -/
theorem abs_cos_sub_cosTaylor128_lt_1e17 {x : ℝ} (hx : |x| ≤ 35) :
    |Real.cos x - cosTaylor 128 x| < 1 / 10 ^ 17 := by
  have h := abs_cos_sub_cosTaylor_le 128 x 35 hx (by norm_num)
  refine h.trans_lt ?_
  norm_num [Nat.factorial]

/-- Rational midpoint of the certified `log 2` interval. -/
noncomputable def p2LogTwoCenter : ℝ :=
  69314718055994535 / 100000000000000000

theorem abs_log_two_sub_center_lt :
    |Real.log 2 - p2LogTwoCenter| < 1 / (2 * 10 ^ 16) := by
  have h := log_two_mem_Ioo_16
  rw [abs_lt]
  constructor <;> norm_num [p2LogTwoCenter] at h ⊢ <;> linarith

/-- After rationalizing `log 2`, the prime cosine still has a uniform
`3·10⁻¹⁵` enclosure on `[-50,50]`. -/
theorem abs_primeCos_sub_rationalTaylor_lt
    {r : ℝ} (hr : |r| ≤ 50) :
    |Real.cos (r * Real.log 2) -
        cosTaylor 128 (r * p2LogTwoCenter)| < 3 / 10 ^ 15 := by
  have hcenter : |r * p2LogTwoCenter| ≤ 35 := by
    have hc0 : 0 ≤ p2LogTwoCenter := by norm_num [p2LogTwoCenter]
    rw [abs_mul, abs_of_nonneg hc0]
    calc
      |r| * p2LogTwoCenter ≤ 50 * p2LogTwoCenter := by gcongr
      _ ≤ 35 := by norm_num [p2LogTwoCenter]
  have htaylor := abs_cos_sub_cosTaylor128_lt_1e17 hcenter
  have hlip := Real.abs_cos_sub_cos_le
    (r * Real.log 2) (r * p2LogTwoCenter)
  have harg :
      |r * Real.log 2 - r * p2LogTwoCenter| < 5 / (2 * 10 ^ 15) := by
    rw [← mul_sub, abs_mul]
    by_cases hr0 : r = 0
    · subst r
      norm_num
    calc
      |r| * |Real.log 2 - p2LogTwoCenter| <
          50 * (1 / (2 * 10 ^ 16)) :=
        (by
          rw [mul_comm, mul_comm 50]
          exact mul_lt_mul abs_log_two_sub_center_lt hr
            (abs_pos.mpr hr0) (by positivity))
      _ = 5 / (2 * 10 ^ 15) := by norm_num
  calc
    |Real.cos (r * Real.log 2) -
        cosTaylor 128 (r * p2LogTwoCenter)| ≤
      |Real.cos (r * Real.log 2) -
          Real.cos (r * p2LogTwoCenter)| +
        |Real.cos (r * p2LogTwoCenter) -
          cosTaylor 128 (r * p2LogTwoCenter)| := by
      exact abs_sub_le _ _ _
    _ < 5 / (2 * 10 ^ 15) + 1 / 10 ^ 17 :=
      add_lt_add (hlip.trans_lt harg) htaylor
    _ < 3 / 10 ^ 15 := by norm_num

end RHP2Bridge
