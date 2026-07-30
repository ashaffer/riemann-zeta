/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact geometric tails for Legendre leakage

The analytic plane-wave identity and the pointwise spherical-Bessel estimate
are deliberately not assumed here.  This file formalizes the purely
algebraic step that turns the resulting double-factorial majorants into the
closed geometric tail used in FULLINF F2.
-/

namespace LegendreTail

open scoped Nat

/-- A nonnegative sequence whose successive terms are bounded by multiplication
by `q` is pointwise bounded by the corresponding geometric sequence. -/
theorem sequence_le_geometric_of_ratio
    (u : ℕ → ℝ) (q : ℝ) (hq : 0 ≤ q)
    (hratio : ∀ n, u (n + 1) ≤ q * u n) :
    ∀ n, u n ≤ u 0 * q ^ n := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
      calc
        u (n + 1) ≤ q * u n := hratio n
        _ ≤ q * (u 0 * q ^ n) := mul_le_mul_of_nonneg_left ih hq
        _ = u 0 * q ^ (n + 1) := by rw [pow_succ]; ring

/-- Geometric domination of an infinite nonnegative tail from a one-step ratio
bound.  The index shift is explicit so this can be applied directly at the
first omitted Legendre mode. -/
theorem tsum_nat_add_le_geometric_of_ratio
    (u : ℕ → ℝ) (m : ℕ) (q : ℝ)
    (hu : ∀ n, 0 ≤ u n) (hq0 : 0 ≤ q) (hq1 : q < 1)
    (hratio : ∀ n, m ≤ n → u (n + 1) ≤ q * u n) :
    Summable (fun n ↦ u (m + n)) ∧
      ∑' n : ℕ, u (m + n) ≤ u m / (1 - q) := by
  let v : ℕ → ℝ := fun n ↦ u (m + n)
  have hv_nonneg : ∀ n, 0 ≤ v n := fun n ↦ hu _
  have hv_ratio : ∀ n, v (n + 1) ≤ q * v n := by
    intro n
    simpa [v, Nat.add_assoc] using hratio (m + n) (Nat.le_add_right m n)
  have hv_le : ∀ n, v n ≤ v 0 * q ^ n :=
    sequence_le_geometric_of_ratio v q hq0 hv_ratio
  have hgeom : Summable (fun n : ℕ ↦ v 0 * q ^ n) :=
    (summable_geometric_of_lt_one hq0 hq1).mul_left _
  have hv_sum : Summable v := hgeom.of_nonneg_of_le hv_nonneg hv_le
  refine ⟨hv_sum, ?_⟩
  have hle := hv_sum.tsum_le_tsum hv_le hgeom
  simpa [v, tsum_mul_left, tsum_geometric_of_lt_one hq0 hq1,
    div_eq_mul_inv] using hle

/-! ## The exact double-factorial majorant used in FULLINF F2 -/

/-- The elementary majorant for the `k`th spherical-Bessel energy term:
`(2k+1) z^(2k) / ((2k+1)!!)^2`. -/
noncomputable def doubleFactorialMajorant (z : ℝ) (k : ℕ) : ℝ :=
  (2 * (k : ℝ) + 1) * z ^ (2 * k) /
    (Nat.doubleFactorial (2 * k + 1) : ℝ) ^ 2

theorem doubleFactorialMajorant_nonneg (z : ℝ) (k : ℕ) :
    0 ≤ doubleFactorialMajorant z k := by
  unfold doubleFactorialMajorant
  have hdf : 0 < (Nat.doubleFactorial (2 * k + 1) : ℝ) := by
    exact_mod_cast Nat.doubleFactorial_pos (2 * k + 1)
  have hzpow : 0 ≤ z ^ (2 * k) := by
    rw [show 2 * k = k + k by omega, pow_add]
    exact mul_self_nonneg _
  exact div_nonneg (mul_nonneg (by positivity) hzpow) (sq_nonneg _)

/-- Squaring the standard pointwise estimate
`|j_k(z)| ≤ |z|^k / (2k+1)!!` produces exactly the energy majorant used
below.  This lemma keeps that elementary order calculation separate from any
future definition of the spherical Bessel function. -/
theorem weighted_sq_le_doubleFactorialMajorant
    (z j : ℝ) (k : ℕ)
    (hj : |j| ≤ |z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ)) :
    (2 * (k : ℝ) + 1) * j ^ 2 ≤ doubleFactorialMajorant z k := by
  have hdf : 0 < (Nat.doubleFactorial (2 * k + 1) : ℝ) := by
    exact_mod_cast Nat.doubleFactorial_pos (2 * k + 1)
  have hquot : 0 ≤
      |z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ) := by positivity
  have hsq : j ^ 2 ≤
      (|z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ)) ^ 2 := by
    rw [sq_le_sq]
    simpa [abs_of_nonneg hquot] using hj
  calc
    (2 * (k : ℝ) + 1) * j ^ 2 ≤
        (2 * (k : ℝ) + 1) *
          (|z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ)) ^ 2 :=
      mul_le_mul_of_nonneg_left hsq (by positivity)
    _ = doubleFactorialMajorant z k := by
      unfold doubleFactorialMajorant
      have hzpow : 0 ≤ z ^ (2 * k) := by
        rw [show 2 * k = k + k by omega, pow_add]
        exact mul_self_nonneg _
      have habspow : |z| ^ (2 * k) = z ^ (2 * k) := by
        rw [← abs_pow, abs_of_nonneg hzpow]
      rw [div_pow, ← pow_mul, Nat.mul_comm k 2, habspow]
      ring

/-- Exact quotient of two consecutive double-factorial majorants. -/
theorem doubleFactorialMajorant_succ (z : ℝ) (k : ℕ) :
    doubleFactorialMajorant z (k + 1) =
      doubleFactorialMajorant z k * z ^ 2 /
        ((2 * (k : ℝ) + 1) * (2 * (k : ℝ) + 3)) := by
  unfold doubleFactorialMajorant
  rw [show 2 * (k + 1) + 1 = (2 * k + 1) + 2 by omega,
    Nat.doubleFactorial_add_two]
  push_cast
  have hodd : (2 * (k : ℝ) + 1) ≠ 0 := by positivity
  have hnext : (2 * (k : ℝ) + 3) ≠ 0 := by positivity
  field_simp [hodd, hnext]
  ring

/-- The odd quadratic denominator occurring in the consecutive-term quotient
is monotone in the mode number. -/
theorem oddDenominator_mono {m n : ℕ} (hmn : m ≤ n) :
    (2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3) ≤
      (2 * (n : ℝ) + 1) * (2 * (n : ℝ) + 3) := by
  have hmn' : (m : ℝ) ≤ n := by exact_mod_cast hmn
  nlinarith [show 0 ≤ (m : ℝ) by positivity,
    show 0 ≤ (n : ℝ) by positivity]

/-- **Exact factorial/geometric tail used in FULLINF F2.**

Once the elementary spherical-Bessel estimate has replaced its `k`th energy
term by `doubleFactorialMajorant z k`, this theorem sums every omitted mode.
It is the formal counterpart of

`t_m(z) / (1 - z² / ((2m+1)(2m+3)))`.

No transcendental function or numerical approximation occurs in the proof. -/
theorem doubleFactorialMajorant_tsum_tail_le
    (z : ℝ) (m : ℕ)
    (hq : z ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦ doubleFactorialMajorant z (m + n)) ∧
      ∑' n : ℕ, doubleFactorialMajorant z (m + n) ≤
        doubleFactorialMajorant z m /
          (1 - z ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) := by
  let q : ℝ := z ^ 2 /
    ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))
  have hden_m : 0 < (2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3) := by
    positivity
  have hq0 : 0 ≤ q := by
    exact div_nonneg (sq_nonneg z) hden_m.le
  have hratio : ∀ n, m ≤ n →
      doubleFactorialMajorant z (n + 1) ≤
        q * doubleFactorialMajorant z n := by
    intro n hmn
    have hden_n : 0 <
        (2 * (n : ℝ) + 1) * (2 * (n : ℝ) + 3) := by positivity
    have hden_le := oddDenominator_mono hmn
    have hquot : z ^ 2 /
          ((2 * (n : ℝ) + 1) * (2 * (n : ℝ) + 3)) ≤ q := by
      dsimp [q]
      exact div_le_div_of_nonneg_left (sq_nonneg z) hden_m hden_le
    rw [doubleFactorialMajorant_succ]
    calc
      doubleFactorialMajorant z n * z ^ 2 /
            ((2 * (n : ℝ) + 1) * (2 * (n : ℝ) + 3)) =
          doubleFactorialMajorant z n *
            (z ^ 2 / ((2 * (n : ℝ) + 1) * (2 * (n : ℝ) + 3))) := by
              ring
      _ ≤ doubleFactorialMajorant z n * q :=
        mul_le_mul_of_nonneg_left hquot (doubleFactorialMajorant_nonneg z n)
      _ = q * doubleFactorialMajorant z n := mul_comm _ _
  simpa [q] using tsum_nat_add_le_geometric_of_ratio
    (doubleFactorialMajorant z) m q
    (doubleFactorialMajorant_nonneg z) hq0 hq hratio

/-- Comparison form of the F2 tail theorem.  An analytic development of
spherical Bessel functions only needs to prove the pointwise hypothesis
`energy k ≤ doubleFactorialMajorant z k`; all infinite summation is then
handled here. -/
theorem dominated_energy_tsum_tail_le
    (energy : ℕ → ℝ) (z : ℝ) (m : ℕ)
    (henergy_nonneg : ∀ k, 0 ≤ energy k)
    (henergy_le : ∀ k, energy k ≤ doubleFactorialMajorant z k)
    (hq : z ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦ energy (m + n)) ∧
      ∑' n : ℕ, energy (m + n) ≤
        doubleFactorialMajorant z m /
          (1 - z ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) := by
  obtain ⟨hmajorant_sum, hmajorant_bound⟩ :=
    doubleFactorialMajorant_tsum_tail_le z m hq
  have hpoint : ∀ n,
      energy (m + n) ≤ doubleFactorialMajorant z (m + n) :=
    fun n ↦ henergy_le _
  have henergy_sum : Summable (fun n ↦ energy (m + n)) :=
    hmajorant_sum.of_nonneg_of_le (fun n ↦ henergy_nonneg _) hpoint
  refine ⟨henergy_sum, ?_⟩
  exact (henergy_sum.tsum_le_tsum hpoint hmajorant_sum).trans hmajorant_bound

/-- Ready-to-use F2 tail bound for any real sequence satisfying the standard
pointwise spherical-Bessel inequality.  To instantiate this with `j_k(z)`, the
only missing analytic input is the hypothesis `hj`; the weighted square,
double-factorial recurrence, convergence, and infinite sum are all proved. -/
theorem weighted_sq_tsum_tail_le
    (j : ℕ → ℝ) (z : ℝ) (m : ℕ)
    (hj : ∀ k, |j k| ≤
      |z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ))
    (hq : z ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦
      (2 * ((m + n : ℕ) : ℝ) + 1) * (j (m + n)) ^ 2) ∧
      ∑' n : ℕ, (2 * ((m + n : ℕ) : ℝ) + 1) * (j (m + n)) ^ 2 ≤
        doubleFactorialMajorant z m /
          (1 - z ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) := by
  apply dominated_energy_tsum_tail_le
    (fun k ↦ (2 * (k : ℝ) + 1) * (j k) ^ 2) z m
  · intro k
    positivity
  · intro k
    exact weighted_sq_le_doubleFactorialMajorant z (j k) k (hj k)
  · exact hq

/-! ## Integral representation majorant -/

/-- The polynomial weight integral appearing in the standard integral model
for the spherical Bessel function. -/
noncomputable def weightIntegral (k : ℕ) : ℝ :=
  ∫ t in (-1 : ℝ)..1, (1 - t ^ 2) ^ k

@[simp] theorem weightIntegral_zero : weightIntegral 0 = 2 := by
  norm_num [weightIntegral]

/-- Integration-by-parts recurrence for the polynomial weight. -/
theorem weightIntegral_succ_recurrence (k : ℕ) :
    (2 * (k : ℝ) + 3) * weightIntegral (k + 1) =
      2 * (k + 1) * weightIntegral k := by
  let F : ℝ → ℝ := fun t ↦ t * (1 - t ^ 2) ^ (k + 1)
  let F' : ℝ → ℝ := fun t ↦
    (1 - t ^ 2) ^ (k + 1) -
      2 * (k + 1) * t ^ 2 * (1 - t ^ 2) ^ k
  have hinner (t : ℝ) : HasDerivAt (fun x : ℝ ↦ 1 - x ^ 2) (-2 * t) t := by
    convert! (hasDerivAt_pow 2 t).const_sub 1 using 1
    norm_num
  have hF (t : ℝ) : HasDerivAt F (F' t) t := by
    convert! (hasDerivAt_id' t).fun_mul ((hinner t).fun_pow (k + 1)) using 1
    simp only [F', Nat.cast_add_one]
    have hk : k + 1 - 1 = k := by omega
    rw [hk]
    ring
  have hFint : ∫ t in (-1 : ℝ)..1, F' t = 0 := by
    have h := intervalIntegral.integral_eq_sub_of_hasDerivAt
      (a := (-1 : ℝ)) (b := 1) (f := F) (f' := F')
      (fun t _ ↦ hF t) (by
        apply Continuous.intervalIntegrable
        fun_prop)
    simpa [F] using h
  have hdiff :
      (∫ t in (-1 : ℝ)..1, t ^ 2 * (1 - t ^ 2) ^ k) =
        weightIntegral k - weightIntegral (k + 1) := by
    rw [weightIntegral, weightIntegral, ← intervalIntegral.integral_sub]
    · apply intervalIntegral.integral_congr
      intro t _
      change t ^ 2 * (1 - t ^ 2) ^ k =
        (1 - t ^ 2) ^ k - (1 - t ^ 2) ^ (k + 1)
      rw [pow_succ]
      ring
    all_goals
      apply Continuous.intervalIntegrable
      fun_prop
  dsimp [F'] at hFint
  rw [intervalIntegral.integral_sub] at hFint
  · have hconst :
        (∫ t in (-1 : ℝ)..1,
          2 * ((k : ℝ) + 1) * t ^ 2 * (1 - t ^ 2) ^ k) =
            2 * ((k : ℝ) + 1) *
              (∫ t in (-1 : ℝ)..1, t ^ 2 * (1 - t ^ 2) ^ k) := by
        calc
          _ = ∫ t in (-1 : ℝ)..1,
              (2 * ((k : ℝ) + 1)) *
                (t ^ 2 * (1 - t ^ 2) ^ k) := by
                  apply intervalIntegral.integral_congr
                  intro t _
                  ring
          _ = _ := by rw [intervalIntegral.integral_const_mul]
    rw [hconst] at hFint
    change weightIntegral (k + 1) -
      2 * (k + 1) *
        (∫ t in (-1 : ℝ)..1, t ^ 2 * (1 - t ^ 2) ^ k) = 0 at hFint
    rw [hdiff] at hFint
    linarith
  all_goals
    apply Continuous.intervalIntegrable
    fun_prop

/-- A denominator-free exact evaluation of the polynomial weight integral. -/
theorem weightIntegral_mul_doubleFactorial (k : ℕ) :
    weightIntegral k * (Nat.doubleFactorial (2 * k + 1) : ℝ) =
      2 ^ (k + 1) * (k ! : ℝ) := by
  induction k with
  | zero => norm_num
  | succ k ih =>
      have hrec := weightIntegral_succ_recurrence k
      rw [show 2 * (k + 1) + 1 = (2 * k + 1) + 2 by omega,
        Nat.doubleFactorial_add_two]
      push_cast
      have hsimp : 2 * (k : ℝ) + 1 + 2 = 2 * (k : ℝ) + 3 := by ring
      rw [hsimp]
      calc
        weightIntegral (k + 1) *
              ((2 * (k : ℝ) + 3) *
                (Nat.doubleFactorial (2 * k + 1) : ℝ)) =
            ((2 * (k : ℝ) + 3) * weightIntegral (k + 1)) *
              (Nat.doubleFactorial (2 * k + 1) : ℝ) := by ring
        _ = (2 * (k + 1) * weightIntegral k) *
              (Nat.doubleFactorial (2 * k + 1) : ℝ) := by rw [hrec]
        _ = 2 * (k + 1) *
              (weightIntegral k *
                (Nat.doubleFactorial (2 * k + 1) : ℝ)) := by ring
        _ = 2 * (k + 1) * (2 ^ (k + 1) * (k ! : ℝ)) := by rw [ih]
        _ = 2 ^ (k + 1 + 1) * ((k + 1)! : ℝ) := by
          rw [Nat.factorial_succ, pow_succ]
          push_cast
          ring

/-- Closed form of the weight integral, in the exact double-factorial shape
needed by the spherical-Bessel majorant. -/
theorem weightIntegral_eq (k : ℕ) :
    weightIntegral k =
      2 ^ (k + 1) * (k ! : ℝ) /
        (Nat.doubleFactorial (2 * k + 1) : ℝ) := by
  apply (eq_div_iff ?_).2
  · exact weightIntegral_mul_doubleFactorial k
  · positivity

/-- The standard oscillatory integral *model* for spherical `j_k` on the real
axis.  This definition is intentionally local: no identification with a
library Bessel function is asserted. -/
noncomputable def sphericalJIntegralModel (k : ℕ) (z : ℝ) : ℂ :=
  ((z ^ k / (2 ^ (k + 1) * (k ! : ℝ)) : ℝ) : ℂ) *
    ∫ t in (-1 : ℝ)..1,
      Complex.exp ((z * t : ℝ) * Complex.I) *
        (((1 - t ^ 2) ^ k : ℝ) : ℂ)

/-- The integral model satisfies the exact pointwise majorant required by the
geometric F2 tail theorem. -/
theorem norm_sphericalJIntegralModel_le (k : ℕ) (z : ℝ) :
    ‖sphericalJIntegralModel k z‖ ≤
      |z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ) := by
  let oscilland : ℝ → ℂ := fun t ↦
    Complex.exp ((z * t : ℝ) * Complex.I) *
      (((1 - t ^ 2) ^ k : ℝ) : ℂ)
  have hnorm_integrand :
      (∫ t in (-1 : ℝ)..1, ‖oscilland t‖) = weightIntegral k := by
    rw [weightIntegral]
    apply intervalIntegral.integral_congr
    intro t ht
    rw [Set.uIcc_of_le (by norm_num)] at ht
    have habs : |t| ≤ 1 := abs_le.mpr ⟨by linarith [ht.1], ht.2⟩
    have hsquare : t ^ 2 ≤ 1 := by
      have := (sq_le_sq (a := t) (b := 1)).2 (by simpa using habs)
      simpa using this
    have hweight : 0 ≤ (1 - t ^ 2) ^ k := pow_nonneg (by linarith) k
    simp only [oscilland, Complex.norm_mul,
      Complex.norm_exp_ofReal_mul_I, one_mul, Complex.norm_real,
      Real.norm_eq_abs, abs_of_nonneg hweight]
  have hintegral :
      ‖∫ t in (-1 : ℝ)..1, oscilland t‖ ≤ weightIntegral k := by
    calc
      _ ≤ ∫ t in (-1 : ℝ)..1, ‖oscilland t‖ :=
        intervalIntegral.norm_integral_le_integral_norm (by norm_num)
      _ = weightIntegral k := hnorm_integrand
  have hden : 0 < (2 : ℝ) ^ (k + 1) * (k ! : ℝ) := by positivity
  have hcoef : 0 ≤ |z| ^ k / ((2 : ℝ) ^ (k + 1) * (k ! : ℝ)) := by
    positivity
  change ‖((z ^ k / (2 ^ (k + 1) * (k ! : ℝ)) : ℝ) : ℂ) *
      (∫ t in (-1 : ℝ)..1, oscilland t)‖ ≤ _
  calc
    _ = (|z| ^ k / ((2 : ℝ) ^ (k + 1) * (k ! : ℝ))) *
          ‖∫ t in (-1 : ℝ)..1, oscilland t‖ := by
      rw [Complex.norm_mul, Complex.norm_real, Real.norm_eq_abs,
        abs_div, abs_pow, abs_of_pos hden]
    _ ≤ (|z| ^ k / ((2 : ℝ) ^ (k + 1) * (k ! : ℝ))) *
          weightIntegral k := mul_le_mul_of_nonneg_left hintegral hcoef
    _ = |z| ^ k / (Nat.doubleFactorial (2 * k + 1) : ℝ) := by
      rw [weightIntegral_eq]
      have hdf : (Nat.doubleFactorial (2 * k + 1) : ℝ) ≠ 0 := by positivity
      field_simp

/-- Complete geometric coefficient-tail bound for the integral model.  This
is the factorial-tail estimate with no remaining pointwise model hypothesis;
the plane-wave and Parseval identifications are separate. -/
theorem sphericalJIntegralModel_tsum_tail_le
    (z : ℝ) (m : ℕ)
    (hq : z ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦
      (2 * ((m + n : ℕ) : ℝ) + 1) *
        ‖sphericalJIntegralModel (m + n) z‖ ^ 2) ∧
      ∑' n : ℕ, (2 * ((m + n : ℕ) : ℝ) + 1) *
          ‖sphericalJIntegralModel (m + n) z‖ ^ 2 ≤
        doubleFactorialMajorant z m /
          (1 - z ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3))) := by
  apply weighted_sq_tsum_tail_le
    (fun k ↦ ‖sphericalJIntegralModel k z‖) z m
  · intro k
    simpa [abs_of_nonneg (norm_nonneg _)] using
      norm_sphericalJIntegralModel_le k z
  · exact hq

end LegendreTail
