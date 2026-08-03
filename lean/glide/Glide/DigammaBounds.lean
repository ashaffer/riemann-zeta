/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.P2Symbol
import Glide.EulerBounds
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SumIntegralComparisons

/-!
# Directed digamma enclosures for the p=2 endpoint

This file evaluates the needed digamma difference as an exact positive
rational series. Integral-test tails then give kernel-checked directed bounds
for both the exterior floor `p2Alpha` and its multiplier constant.

The proofs use only kernel-checked exact arithmetic and analytic theorems.
-/

open Filter Set
open scoped Topology ComplexConjugate

namespace GlideKernel

private lemma digamma_quarter_reflection :
    Complex.digamma (1 / 4 : ℂ) - Complex.digamma (3 / 4 : ℂ) =
      -(Real.pi : ℂ) := by
  let z : ℂ := 1 / 4
  have hz : 0 < z.re := by norm_num [z]
  have h1z : 0 < (1 - z).re := by norm_num [z]
  have hGz : Complex.Gamma z ≠ 0 := Complex.Gamma_ne_zero_of_re_pos hz
  have hG1z : Complex.Gamma (1 - z) ≠ 0 := Complex.Gamma_ne_zero_of_re_pos h1z
  have hzpole : ∀ m : ℕ, z ≠ -(m : ℂ) := by
    intro m h
    have hre := congrArg Complex.re h
    norm_num [z] at hre
    have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  have h1zpole : ∀ m : ℕ, 1 - z ≠ -(m : ℂ) := by
    intro m h
    have hre := congrArg Complex.re h
    norm_num [z] at hre
    have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  have hsin : Complex.sin ((Real.pi : ℂ) * z) ≠ 0 := by
    rw [show (Real.pi : ℂ) * z = (Real.pi / 4 : ℝ) by
      dsimp [z]
      push_cast
      ring]
    rw [← Complex.ofReal_sin, Real.sin_pi_div_four]
    exact Complex.ofReal_ne_zero.mpr (by positivity)
  have hfun :
      (fun w : ℂ => Complex.Gamma w * Complex.Gamma (1 - w)) =
        (fun w : ℂ => (Real.pi : ℂ) / Complex.sin ((Real.pi : ℂ) * w)) := by
    funext w
    exact Complex.Gamma_mul_Gamma_one_sub w
  have hld := congrFun (congrArg logDeriv hfun) z
  have hmul := logDeriv_mul (f := Complex.Gamma)
    (g := fun w : ℂ => Complex.Gamma (1 - w)) z hGz hG1z
    (Complex.differentiableAt_Gamma z hzpole)
    ((Complex.differentiableAt_Gamma (1 - z) h1zpole).comp z (by fun_prop))
  rw [hmul] at hld
  have hcompGamma :
      logDeriv (fun w : ℂ => Complex.Gamma (1 - w)) z =
        -Complex.digamma (1 - z) := by
    change deriv (fun w : ℂ => Complex.Gamma (1 - w)) z / Complex.Gamma (1 - z) = _
    rw [show (fun w : ℂ => Complex.Gamma (1 - w)) =
      Complex.Gamma ∘ (fun w : ℂ => 1 - w) by rfl]
    rw [deriv_comp z (Complex.differentiableAt_Gamma (1 - z) h1zpole) (by fun_prop)]
    rw [deriv_const_sub, deriv_id'']
    rw [Complex.digamma_def, logDeriv_apply]
    ring
  rw [hcompGamma] at hld
  rw [logDeriv_div z (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero) hsin
    (by fun_prop) (by fun_prop)] at hld
  rw [logDeriv_const] at hld
  have hsincomp :
      logDeriv (fun w : ℂ => Complex.sin ((Real.pi : ℂ) * w)) z =
        (Real.pi : ℂ) * Complex.cot ((Real.pi : ℂ) * z) := by
    have h := logDeriv_comp (f := Complex.sin)
      (g := fun w : ℂ => (Real.pi : ℂ) * w)
      Complex.differentiableAt_sin (by fun_prop :
        DifferentiableAt ℂ (fun w : ℂ => (Real.pi : ℂ) * w) z)
    rw [Complex.logDeriv_sin, deriv_const_mul_id] at h
    simpa [Function.comp_def, mul_comm] using h
  rw [hsincomp] at hld
  simp only [Pi.zero_apply, zero_sub] at hld
  simp only [Complex.digamma_def] at hld
  have hcot : Complex.cot ((Real.pi : ℂ) * z) = 1 := by
    rw [show (Real.pi : ℂ) * z = (Real.pi / 4 : ℝ) by
      dsimp [z]
      push_cast
      ring]
    rw [Complex.cot, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
      Real.cos_pi_div_four, Real.sin_pi_div_four]
    field_simp
  rw [hcot] at hld
  dsimp [z] at hld
  norm_num at hld
  simpa [Complex.digamma_def, sub_eq_add_neg] using hld

private lemma digamma_quarter_duplication :
    Complex.digamma (1 / 4 : ℂ) + Complex.digamma (3 / 4 : ℂ) =
      2 * Complex.digamma (1 / 2 : ℂ) - 2 * Real.log 2 := by
  let z : ℂ := 1 / 4
  have hz : 0 < z.re := by norm_num [z]
  have hz2 : 0 < (z + 1 / 2).re := by norm_num [z]
  have h2z : 0 < (2 * z).re := by norm_num [z]
  have hGz : Complex.Gamma z ≠ 0 := Complex.Gamma_ne_zero_of_re_pos hz
  have hGz2 : Complex.Gamma (z + 1 / 2) ≠ 0 :=
    Complex.Gamma_ne_zero_of_re_pos hz2
  have hG2z : Complex.Gamma (2 * z) ≠ 0 := Complex.Gamma_ne_zero_of_re_pos h2z
  have hpow : (2 : ℂ) ^ (1 - 2 * z) ≠ 0 :=
    Complex.cpow_ne_zero_iff.mpr (Or.inl (by norm_num))
  have hsqrt : ((Real.sqrt Real.pi : ℝ) : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (Real.sqrt_pos.2 Real.pi_pos).ne'
  have hzpole : ∀ m : ℕ, z ≠ -(m : ℂ) := by
    intro m h
    have hre := congrArg Complex.re h
    norm_num [z] at hre
    have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  have hz2pole : ∀ m : ℕ, z + 1 / 2 ≠ -(m : ℂ) := by
    intro m h
    have hre := congrArg Complex.re h
    norm_num [z] at hre
    have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  have h2zpole : ∀ m : ℕ, 2 * z ≠ -(m : ℂ) := by
    intro m h
    have hre := congrArg Complex.re h
    norm_num [z] at hre
    have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
    linarith
  have hfun :
      (fun w : ℂ => Complex.Gamma w * Complex.Gamma (w + 1 / 2)) =
        (fun w : ℂ =>
          Complex.Gamma (2 * w) * (2 : ℂ) ^ (1 - 2 * w) * (Real.sqrt Real.pi : ℝ)) := by
    funext w
    exact Complex.Gamma_mul_Gamma_add_half w
  have hld := congrFun (congrArg logDeriv hfun) z
  have hlhs := logDeriv_mul (f := Complex.Gamma)
    (g := fun w : ℂ => Complex.Gamma (w + 1 / 2)) z hGz hGz2
    (Complex.differentiableAt_Gamma z hzpole)
    ((Complex.differentiableAt_Gamma (z + 1 / 2) hz2pole).comp z (by fun_prop))
  rw [hlhs] at hld
  have hcompAdd :
      logDeriv (fun w : ℂ => Complex.Gamma (w + 1 / 2)) z =
        Complex.digamma (z + 1 / 2) := by
    have h := logDeriv_comp (f := Complex.Gamma)
      (g := fun w : ℂ => w + 1 / 2)
      (Complex.differentiableAt_Gamma (z + 1 / 2) hz2pole) (by fun_prop)
    rw [deriv_add_const, deriv_id''] at h
    simpa [Function.comp_def, Complex.digamma_def] using h
  rw [hcompAdd] at hld
  have hrhsOuter := logDeriv_mul_const (f := fun w : ℂ =>
      Complex.Gamma (2 * w) * (2 : ℂ) ^ (1 - 2 * w)) z
    (Real.sqrt Real.pi : ℂ) hsqrt
  rw [hrhsOuter] at hld
  have hrhsMul := logDeriv_mul
    (f := fun w : ℂ => Complex.Gamma (2 * w))
    (g := fun w : ℂ => (2 : ℂ) ^ (1 - 2 * w)) z hG2z hpow
    ((Complex.differentiableAt_Gamma (2 * z) h2zpole).comp z (by fun_prop))
    ((by fun_prop : DifferentiableAt ℂ (fun w : ℂ => 1 - 2 * w) z).const_cpow
      (Or.inl (by norm_num)))
  rw [hrhsMul] at hld
  have hcompDouble :
      logDeriv (fun w : ℂ => Complex.Gamma (2 * w)) z =
        2 * Complex.digamma (2 * z) := by
    have h := logDeriv_comp (f := Complex.Gamma) (g := fun w : ℂ => 2 * w)
      (Complex.differentiableAt_Gamma (2 * z) h2zpole) (by fun_prop)
    rw [deriv_const_mul_id] at h
    simpa [Function.comp_def, Complex.digamma_def, mul_comm] using h
  rw [hcompDouble] at hld
  have hpowld :
      logDeriv (fun w : ℂ => (2 : ℂ) ^ (1 - 2 * w)) z =
        -2 * (Real.log 2 : ℂ) := by
    rw [logDeriv_apply, Complex.deriv_const_cpow (by fun_prop)]
    rw [deriv_const_sub, deriv_const_mul_id]
    have hlog2 : Complex.log (2 : ℂ) = (Real.log 2 : ℂ) := by
      calc
        Complex.log (2 : ℂ) = Complex.log ((2 : ℝ) : ℂ) := by norm_num
        _ = (Real.log 2 : ℂ) :=
          (Complex.ofReal_log (by norm_num : (0 : ℝ) ≤ 2)).symm
    rw [hlog2]
    field_simp [hpow]
  rw [hpowld] at hld
  dsimp [z] at hld
  norm_num at hld
  simpa [Complex.digamma_def, sub_eq_add_neg] using hld

lemma digamma_one_quarter :
    Complex.digamma (1 / 4 : ℂ) =
      -(Real.eulerMascheroniConstant : ℂ) - 3 * Real.log 2 - Real.pi / 2 := by
  have href := digamma_quarter_reflection
  have hdup := digamma_quarter_duplication
  rw [Complex.digamma_one_half] at hdup
  have hlog2 : Complex.log (2 : ℂ) = (Real.log 2 : ℂ) := by
    calc
      Complex.log (2 : ℂ) = Complex.log ((2 : ℝ) : ℂ) := by norm_num
      _ = (Real.log 2 : ℂ) :=
        (Complex.ofReal_log (by norm_num : (0 : ℝ) ≤ 2)).symm
  rw [hlog2] at hdup
  linear_combination (href + hdup) / 2

/-! ## An exact two-frequency digamma-difference series -/

/-- The real summand in the exact difference between two values on the
quarter line.  It is written so that all constants cancel before numerical
enclosure: only rational functions of the two real frequencies remain. -/
noncomputable def quarterDifferenceTerm (r s : ℝ) (n : ℕ) : ℝ :=
  let a : ℝ := n + 1 / 4
  a / (a ^ 2 + (s / 2) ^ 2) - a / (a ^ 2 + (r / 2) ^ 2)

lemma quarterDifferenceTerm_eq (r s : ℝ) (n : ℕ) :
    quarterDifferenceTerm r s n =
      (((r / 2) ^ 2 - (s / 2) ^ 2) * ((n : ℝ) + 1 / 4)) /
        ((((n : ℝ) + 1 / 4) ^ 2 + (s / 2) ^ 2) *
          (((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2)) := by
  unfold quarterDifferenceTerm
  have ha : (n : ℝ) + 1 / 4 ≠ 0 := by positivity
  have hs : ((n : ℝ) + 1 / 4) ^ 2 + (s / 2) ^ 2 ≠ 0 := by positivity
  have hr : ((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2 ≠ 0 := by positivity
  field_simp
  ring

lemma abs_quarterDifferenceTerm_le (r s : ℝ) (n : ℕ) :
    |quarterDifferenceTerm r s n| ≤
      |(r / 2) ^ 2 - (s / 2) ^ 2| /
        (((n : ℝ) + 1 / 4) ^ 3) := by
  rw [quarterDifferenceTerm_eq]
  let a : ℝ := (n : ℝ) + 1 / 4
  have ha : 0 < a := by dsimp [a]; positivity
  have hden : a ^ 4 ≤
      (a ^ 2 + (s / 2) ^ 2) * (a ^ 2 + (r / 2) ^ 2) := by
    nlinarith [sq_nonneg (s / 2), sq_nonneg (r / 2), sq_nonneg (a ^ 2)]
  rw [abs_div, abs_mul, abs_of_pos ha]
  have hdenpos : 0 <
      (a ^ 2 + (s / 2) ^ 2) * (a ^ 2 + (r / 2) ^ 2) := by positivity
  rw [abs_of_pos hdenpos]
  have hc : 0 ≤ |(r / 2) ^ 2 - (s / 2) ^ 2| := abs_nonneg _
  change |(r / 2) ^ 2 - (s / 2) ^ 2| * a /
      ((a ^ 2 + (s / 2) ^ 2) * (a ^ 2 + (r / 2) ^ 2)) ≤
    |(r / 2) ^ 2 - (s / 2) ^ 2| / a ^ 3
  rw [div_le_div_iff₀ hdenpos (pow_pos ha 3)]
  nlinarith

/-- Absolute convergence of the exact two-frequency difference series. -/
lemma summable_quarterDifferenceTerm (r s : ℝ) :
    Summable (quarterDifferenceTerm r s) := by
  have hsRpow : Summable (fun n : ℕ =>
      1 / |(n : ℝ) + 1 / 4| ^ (3 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow (1 / 4) 3).2 (by norm_num)
  have hs : Summable (fun n : ℕ => 1 / (((n : ℝ) + 1 / 4) ^ 3)) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + 1 / 4)]
    change 1 / (((n : ℝ) + 1 / 4) ^ (3 : ℕ)) =
      1 / Real.rpow ((n : ℝ) + 1 / 4) (3 : ℝ)
    exact congrArg (fun x : ℝ => 1 / x)
      (Real.rpow_natCast ((n : ℝ) + 1 / 4) 3).symm
  have hsmul : Summable (fun n : ℕ =>
      |(r / 2) ^ 2 - (s / 2) ^ 2| *
        (1 / (((n : ℝ) + 1 / 4) ^ 3))) := hs.mul_left _
  apply Summable.of_norm_bounded hsmul
  intro n
  rw [Real.norm_eq_abs]
  calc
    |quarterDifferenceTerm r s n| ≤
        |(r / 2) ^ 2 - (s / 2) ^ 2| /
          (((n : ℝ) + 1 / 4) ^ 3) := abs_quarterDifferenceTerm_le r s n
    _ = |(r / 2) ^ 2 - (s / 2) ^ 2| *
          (1 / (((n : ℝ) + 1 / 4) ^ 3)) := by ring

private lemma complex_quarterDifference_re (r s : ℝ) (n : ℕ) :
    (1 / ((((n : ℝ) + 1 / 4 : ℝ) : ℂ) + Complex.I * (s / 2)) -
      1 / ((((n : ℝ) + 1 / 4 : ℝ) : ℂ) + Complex.I * (r / 2))).re =
      quarterDifferenceTerm r s n := by
  unfold quarterDifferenceTerm
  norm_num [Complex.div_re, Complex.normSq_apply, Complex.mul_re,
    Complex.mul_im, pow_two]

/-- Exact kernel-facing series for an arbitrary difference on the quarter
line.  This is the analytic bridge needed by a kernel-checked enclosure of
the clipped p=2 multiplier; it removes Euler's constant and `log pi` before
any certificate arithmetic begins. -/
theorem quarterDifference_tsum_eq (r s : ℝ) :
    ∑' n : ℕ, quarterDifferenceTerm r s n =
      quarterDigammaReal r - quarterDigammaReal s := by
  let zr : ℂ := (1 / 4 : ℂ) + Complex.I * (r / 2)
  let zs : ℂ := (1 / 4 : ℂ) + Complex.I * (s / 2)
  have hzr : 0 < zr.re := by norm_num [zr]
  have hzs : 0 < zs.re := by norm_num [zs]
  have hsum := Complex.summable_digammaDifferenceTerm hzr hzs
  calc
    ∑' n : ℕ, quarterDifferenceTerm r s n =
        ∑' n : ℕ, (Complex.digammaDifferenceTerm zr zs n).re := by
      apply tsum_congr
      intro n
      dsimp [Complex.digammaDifferenceTerm, zr, zs]
      norm_num
      simpa [add_comm, add_left_comm, add_assoc] using
        (complex_quarterDifference_re r s n).symm
    _ = (∑' n : ℕ, Complex.digammaDifferenceTerm zr zs n).re :=
      (Complex.re_tsum hsum).symm
    _ = (Complex.digamma zr - Complex.digamma zs).re := by
      rw [← Complex.digamma_sub_eq_tsum hzr hzs]
    _ = quarterDigammaReal r - quarterDigammaReal s := by
      norm_num [quarterDigammaReal, zr, zs, Complex.sub_re]

/-- The exact p=2 in-band defect after cancellation of Euler's constant and
`log pi`.  This is the form consumed by numerical certificates: a convergent
rational series plus one elementary cosine term. -/
theorem p2Omega_sub_alpha_eq_series (r : ℝ) :
    p2Omega r - p2Alpha =
      (∑' n : ℕ, quarterDifferenceTerm r 50 n) +
        p2PrimeAmplitude * (1 - Real.cos (r * Real.log 2)) := by
  rw [quarterDifference_tsum_eq]
  unfold p2Omega p2Alpha
  ring

noncomputable def quarterIncrementTerm (n : ℕ) : ℝ :=
  let a : ℝ := n + 1 / 4
  625 / (a * (a ^ 2 + 625))

private lemma quarterIncrementTerm_pos (n : ℕ) : 0 < quarterIncrementTerm n := by
  unfold quarterIncrementTerm
  positivity

private lemma quarterIncrementTerm_le (n : ℕ) :
    quarterIncrementTerm n ≤ 625 * (1 / ((n : ℝ) + 1 / 4) ^ 3) := by
  unfold quarterIncrementTerm
  have ha : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hden : 0 < ((n : ℝ) + 1 / 4) * (((n : ℝ) + 1 / 4) ^ 2 + 625) := by
    positivity
  rw [div_le_iff₀ hden]
  field_simp
  nlinarith [sq_nonneg ((n : ℝ) + 1 / 4)]

lemma summable_quarterIncrementTerm : Summable quarterIncrementTerm := by
  have hsRpow : Summable (fun n : ℕ => 1 / |(n : ℝ) + 1 / 4| ^ (3 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow (1 / 4) 3).2 (by norm_num)
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ) + 1 / 4) ^ 3) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + 1 / 4)]
    change 1 / (((n : ℝ) + 1 / 4) ^ (3 : ℕ)) =
      1 / Real.rpow ((n : ℝ) + 1 / 4) (3 : ℝ)
    exact congrArg (fun x : ℝ => 1 / x)
      (Real.rpow_natCast ((n : ℝ) + 1 / 4) 3).symm
  have hsmul : Summable (fun n : ℕ => 625 * (1 / ((n : ℝ) + 1 / 4) ^ 3)) :=
    Summable.mul_left _ hs
  exact hsmul.of_nonneg_of_le (fun n => (quarterIncrementTerm_pos n).le)
    quarterIncrementTerm_le

private lemma quarterIncrementTerm_eq_quarterDifferenceTerm (n : ℕ) :
    quarterIncrementTerm n = quarterDifferenceTerm 50 0 n := by
  unfold quarterIncrementTerm quarterDifferenceTerm
  have ha : (n : ℝ) + 1 / 4 ≠ 0 := by positivity
  norm_num
  field_simp
  ring

theorem quarterIncrement_tsum_eq :
    ∑' n : ℕ, quarterIncrementTerm n = quarterDigammaReal 50 - quarterDigammaReal 0 := by
  rw [show (∑' n : ℕ, quarterIncrementTerm n) =
      ∑' n : ℕ, quarterDifferenceTerm 50 0 n by
    apply tsum_congr
    exact quarterIncrementTerm_eq_quarterDifferenceTerm]
  exact quarterDifference_tsum_eq 50 0

noncomputable def quarterTailMajorant (x : ℝ) : ℝ := 625 * x ^ (-3 : ℝ)

private lemma quarterTailMajorant_antitone :
    AntitoneOn quarterTailMajorant (Ici (149 : ℝ)) := by
  intro x hx y hy hxy
  simp only [mem_Ici] at hx hy
  unfold quarterTailMajorant
  apply mul_le_mul_of_nonneg_left _ (by norm_num)
  exact Real.antitoneOn_rpow_Ioi_of_exponent_nonpos (by norm_num)
    (show x ∈ Ioi (0 : ℝ) by simp only [mem_Ioi]; linarith)
    (show y ∈ Ioi (0 : ℝ) by simp only [mem_Ioi]; linarith) hxy

private lemma quarterTailMajorant_integrable :
    MeasureTheory.IntegrableOn quarterTailMajorant (Ioi (149 : ℝ)) := by
  exact (integrableOn_Ioi_rpow_of_lt (a := (-3 : ℝ)) (by norm_num) (by norm_num)).const_mul 625

private lemma quarterTailMajorant_nonneg (x : ℝ) (hx : x ∈ Ioi (149 : ℝ)) :
    0 ≤ quarterTailMajorant x := by
  simp only [mem_Ioi] at hx
  unfold quarterTailMajorant
  exact mul_nonneg (by norm_num) (Real.rpow_nonneg (by linarith [hx]) _)

private lemma quarterIncrement_tail_le (n : ℕ) :
    quarterIncrementTerm (n + 150) ≤ quarterTailMajorant (n + 150 : ℝ) := by
  refine (quarterIncrementTerm_le (n + 150)).trans ?_
  have hx : 0 < (n + 150 : ℝ) := by positivity
  have hpow : (n + 150 : ℝ) ^ 3 ≤ ((n + 150 : ℝ) + 1 / 4) ^ 3 := by
    apply pow_le_pow_left₀ hx.le
    norm_num
  have hinv :
      1 / (((n + 150 : ℝ) + 1 / 4) ^ 3) ≤ 1 / ((n + 150 : ℝ) ^ 3) := by
    exact one_div_le_one_div_of_le (by positivity) hpow
  unfold quarterTailMajorant
  rw [Real.rpow_neg hx.le]
  norm_num [Nat.cast_add, one_div] at hinv ⊢
  exact hinv

private lemma quarterIncrement_tail_le_integral :
    ∑' n : ℕ, quarterIncrementTerm (n + 150) ≤
      ∫ x in Ioi (149 : ℝ), quarterTailMajorant x := by
  have hsumMajorant : Summable (fun n : ℕ => quarterTailMajorant n) :=
    quarterTailMajorant_antitone.summable_of_integrableOn_Ioi
      quarterTailMajorant_integrable quarterTailMajorant_nonneg
  have hcompare :
      ∑' n : ℕ, quarterIncrementTerm (n + 150) ≤
        ∑' n : ℕ, quarterTailMajorant (n + 150 : ℝ) := by
    have hsTail : Summable (fun n : ℕ => quarterIncrementTerm (n + 150)) := by
      change Summable (quarterIncrementTerm ∘ fun n : ℕ => n + 150)
      exact summable_quarterIncrementTerm.comp_injective
        (show Function.Injective (fun n : ℕ => n + 150) by
          intro a b h
          exact Nat.add_right_cancel h)
    have hsMajorTail : Summable (fun n : ℕ => quarterTailMajorant (n + 150 : ℝ)) := by
      have hs : Summable ((fun n : ℕ => quarterTailMajorant n) ∘
          fun n : ℕ => n + 150) :=
        hsumMajorant.comp_injective
            (show Function.Injective (fun n : ℕ => n + 150) by
              intro a b h
              exact Nat.add_right_cancel h)
      convert hs using 1
      ext n
      norm_num [Function.comp_apply, Nat.cast_add]
    exact Summable.tsum_le_tsum quarterIncrement_tail_le hsTail hsMajorTail
  refine hcompare.trans ?_
  simpa only [Nat.cast_add, Nat.cast_ofNat, Nat.add_assoc, Nat.reduceAdd] using
    quarterTailMajorant_antitone.tsum_comp_add_le_integral 149
      quarterTailMajorant_integrable quarterTailMajorant_nonneg

private lemma quarterTailMajorant_integral :
    ∫ x in Ioi (149 : ℝ), quarterTailMajorant x = 625 / (2 * 149 ^ 2) := by
  unfold quarterTailMajorant
  rw [MeasureTheory.integral_const_mul]
  rw [integral_Ioi_rpow_of_lt (by norm_num) (by norm_num)]
  norm_num [Real.rpow_neg, Real.rpow_natCast]

theorem quarterIncrement_tsum_le_7447e3 :
    ∑' n : ℕ, quarterIncrementTerm n ≤ (7447 : ℝ) / 1000 := by
  rw [← summable_quarterIncrementTerm.sum_add_tsum_nat_add 150]
  calc
    (∑ n ∈ Finset.range 150, quarterIncrementTerm n) +
        ∑' n : ℕ, quarterIncrementTerm (n + 150) ≤
        (∑ n ∈ Finset.range 150, quarterIncrementTerm n) +
          ∫ x in Ioi (149 : ℝ), quarterTailMajorant x :=
      add_le_add le_rfl quarterIncrement_tail_le_integral
    _ ≤ (7447 : ℝ) / 1000 := by
      rw [quarterTailMajorant_integral]
      norm_num [quarterIncrementTerm, Finset.sum_range_succ]

theorem quarterDigammaReal_difference_le_7447e3 :
    quarterDigammaReal 50 - quarterDigammaReal 0 ≤ (7447 : ℝ) / 1000 := by
  rw [← quarterIncrement_tsum_eq]
  exact quarterIncrement_tsum_le_7447e3

private lemma log_pi_lt_11447299e7 :
    Real.log Real.pi < (11447299 : ℝ) / 10000000 := by
  let q : ℝ := 314159265358979323847 / 100000000000000000000
  let x : ℝ := (q - 1) / (q + 1)
  have hpi : Real.pi < q := by
    dsimp [q]
    convert Real.pi_lt_d20 using 1
    norm_num
  have hq0 : 0 < q := by dsimp [q]; norm_num
  have hlog : Real.log Real.pi < Real.log q :=
    Real.strictMonoOn_log Real.pi_pos hq0 hpi
  have hx0 : 0 ≤ x := by dsimp [x, q]; norm_num
  have hx1 : x < 1 := by dsimp [x, q]; norm_num
  have hs := Real.log_div_le_sum_range_add hx0 hx1 16
  have hratio : (1 + x) / (1 - x) = q := by
    dsimp [x]
    have hq1 : q + 1 ≠ 0 := by positivity
    field_simp
    ring
  rw [hratio] at hs
  have hq : Real.log q < (11447299 : ℝ) / 10000000 := by
    norm_num [x, q, Finset.sum_range_succ] at hs ⊢
    linarith
  exact hlog.trans hq

private lemma sqrt_two_le_141421357e8 :
    Real.sqrt 2 ≤ (141421357 : ℝ) / 100000000 := by
  rw [Real.sqrt_le_iff]
  constructor <;> norm_num

noncomputable def quarterTailMinorant (x : ℝ) : ℝ :=
  (31207 / 50 : ℝ) * x ^ (-3 : ℝ)

private lemma quarterTailMinorant_antitone :
    AntitoneOn quarterTailMinorant (Ici (1000 : ℝ)) := by
  intro x hx y hy hxy
  simp only [mem_Ici] at hx hy
  unfold quarterTailMinorant
  apply mul_le_mul_of_nonneg_left
  · exact Real.antitoneOn_rpow_Ioi_of_exponent_nonpos (by norm_num)
      (show x ∈ Ioi (0 : ℝ) by simp only [mem_Ioi]; linarith)
      (show y ∈ Ioi (0 : ℝ) by simp only [mem_Ioi]; linarith) hxy
  · norm_num

private lemma quarterTailMinorant_summable :
    Summable (fun n : ℕ => quarterTailMinorant n) := by
  apply quarterTailMinorant_antitone.summable_of_integrableOn_Ioi
  · exact (integrableOn_Ioi_rpow_of_lt (a := (-3 : ℝ))
      (by norm_num) (by norm_num)).const_mul (31207 / 50 : ℝ)
  · intro x hx
    simp only [mem_Ioi] at hx
    unfold quarterTailMinorant
    exact mul_nonneg (by norm_num) (Real.rpow_nonneg (by linarith) _)

private lemma quarterTailMinorant_le_increment (n : ℕ) :
    quarterTailMinorant (n + 1000 : ℝ) ≤ quarterIncrementTerm (n + 1000) := by
  let x : ℝ := n + 1000
  let a : ℝ := x + 1 / 4
  have hx : 0 < x := by dsimp [x]; positivity
  have ha : 0 < a := by dsimp [a]; positivity
  have hden : 0 < a * (a ^ 2 + 625) := by positivity
  have hpoly :
      (31207 / 50 : ℝ) * (a * (a ^ 2 + 625)) ≤ 625 * x ^ 3 := by
    have hid :
        625 * x ^ 3 - (31207 / 50 : ℝ) * (a * (a ^ 2 + 625)) =
          (43 / 50 : ℝ) * (n : ℝ) ^ 3 +
            (422379 / 200 : ℝ) * (n : ℝ) ^ 2 +
            (1002868379 / 800 : ℝ) * n + 5097414793 / 3200 := by
      dsimp [x, a]
      ring
    rw [← sub_nonneg, hid]
    positivity
  unfold quarterTailMinorant quarterIncrementTerm
  dsimp [x, a] at hx ha hden hpoly ⊢
  rw [Real.rpow_neg hx.le]
  norm_num [Nat.cast_add, one_div] at hpoly ⊢
  exact (div_le_div_iff₀ (pow_pos hx 3) hden).2 hpoly

private lemma quarterTailMinorant_integral :
    ∫ x in Ioi (1000 : ℝ), quarterTailMinorant x =
      (31207 / 50 : ℝ) / (2 * 1000 ^ 2) := by
  unfold quarterTailMinorant
  rw [MeasureTheory.integral_const_mul]
  rw [integral_Ioi_rpow_of_lt (by norm_num) (by norm_num)]
  norm_num [Real.rpow_neg, Real.rpow_natCast]

private lemma quarterTailMinorant_integral_le_increment_tail :
    ∫ x in Ioi (1000 : ℝ), quarterTailMinorant x ≤
      ∑' n : ℕ, quarterIncrementTerm (n + 1000) := by
  have hminor := quarterTailMinorant_antitone.integral_le_tsum_comp_add 1000
    quarterTailMinorant_summable (fun x hx => by
      simp only [mem_Ioi] at hx
      unfold quarterTailMinorant
      exact mul_nonneg (by norm_num) (Real.rpow_nonneg (by linarith) _))
  have hsMinorTail : Summable (fun n : ℕ => quarterTailMinorant (n + 1000 : ℝ)) := by
    have hs : Summable ((fun n : ℕ => quarterTailMinorant n) ∘
        fun n : ℕ => n + 1000) :=
      quarterTailMinorant_summable.comp_injective
        (show Function.Injective (fun n : ℕ => n + 1000) by
          intro a b h
          exact Nat.add_right_cancel h)
    convert hs using 1
    ext n
    norm_num [Function.comp_apply, Nat.cast_add]
  have hsIncrementTail : Summable (fun n : ℕ => quarterIncrementTerm (n + 1000)) := by
    change Summable (quarterIncrementTerm ∘ fun n : ℕ => n + 1000)
    exact summable_quarterIncrementTerm.comp_injective
      (show Function.Injective (fun n : ℕ => n + 1000) by
        intro a b h
        exact Nat.add_right_cancel h)
  have hcompare :
      ∑' n : ℕ, quarterTailMinorant (n + 1000 : ℝ) ≤
        ∑' n : ℕ, quarterIncrementTerm (n + 1000) :=
    Summable.tsum_le_tsum quarterTailMinorant_le_increment
      hsMinorTail hsIncrementTail
  have hminor' :
      ∫ x in Ioi (1000 : ℝ), quarterTailMinorant x ≤
        ∑' n : ℕ, quarterTailMinorant (n + 1000 : ℝ) := by
    simpa only [Nat.cast_add, Nat.cast_ofNat] using hminor
  exact hminor'.trans hcompare

private lemma quarterIncrement_tsum_lower_split :
    (∑ n ∈ Finset.range 1000, quarterIncrementTerm n) +
        (31207 / 50 : ℝ) / (2 * 1000 ^ 2) ≤
      ∑' n : ℕ, quarterIncrementTerm n := by
  rw [← summable_quarterIncrementTerm.sum_add_tsum_nat_add 1000]
  rw [← quarterTailMinorant_integral]
  exact add_le_add le_rfl quarterTailMinorant_integral_le_increment_tail

private lemma quarterDigammaReal_zero :
    quarterDigammaReal 0 =
      -Real.eulerMascheroniConstant - 3 * Real.log 2 - Real.pi / 2 := by
  have h := congrArg Complex.re digamma_one_quarter
  norm_num [quarterDigammaReal, Complex.sub_re, Complex.mul_re, Complex.div_re,
    Complex.normSq_apply] at h ⊢
  have hlog2 : Complex.log (2 : ℂ) = (Real.log 2 : ℂ) := by
    calc
      Complex.log (2 : ℂ) = Complex.log ((2 : ℝ) : ℂ) := by norm_num
      _ = (Real.log 2 : ℂ) :=
        (Complex.ofReal_log (by norm_num : (0 : ℝ) ≤ 2)).symm
  rw [hlog2] at h
  simpa only [Complex.ofReal_re] using h

theorem p2Alpha_lower_bound :
    (109387 : ℝ) / 100000 ≤ p2Alpha := by
  have hM := quarterIncrement_tsum_lower_split
  have hgamma := eulerMascheroniConstant_lt_5772161e7.le
  have hlog2 : Real.log 2 ≤ (6931471808 : ℝ) / 10000000000 := by
    calc
      Real.log 2 ≤ (0.6931471808 : ℝ) := Real.log_two_lt_d9.le
      _ = (6931471808 : ℝ) / 10000000000 := by norm_num
  have hlogpi := log_pi_lt_11447299e7.le
  have hpi := Real.pi_lt_d20.le
  have hsqrt := sqrt_two_le_141421357e8
  have hlog2nonneg : 0 ≤ Real.log 2 := Real.log_nonneg (by norm_num)
  have hprime :
      Real.sqrt 2 * Real.log 2 ≤
        ((141421357 : ℝ) / 100000000) * (6931471808 / 10000000000) :=
    mul_le_mul hsqrt hlog2 hlog2nonneg (by norm_num)
  rw [quarterIncrement_tsum_eq, quarterDigammaReal_zero] at hM
  unfold p2Alpha p2PrimeAmplitude
  norm_num [quarterIncrementTerm, Finset.sum_range_succ] at hM ⊢
  linarith

/-- The exact positive multiplier constant associated with the digamma
difference is nonnegative. -/
theorem quarterDigammaReal_difference_nonneg :
    0 ≤ quarterDigammaReal 50 - quarterDigammaReal 0 := by
  exact sub_nonneg.mpr <| quarterDigammaReal_strictMonoOn.monotoneOn
    (by norm_num) (by norm_num) (by norm_num)

/-- On the clipped band, the complete p=2 symbol defect is bounded by the
same rational used by the endpoint operator theorem. -/
theorem p2Omega_sub_alpha_abs_le {r : ℝ} (hr : |r| ≤ 50) :
    |p2Omega r - p2Alpha| ≤ (7447 : ℝ) / 1000 := by
  have habs : quarterDigammaReal |r| = quarterDigammaReal r := by
    rcases le_total 0 r with hr0 | hr0
    · rw [abs_of_nonneg hr0]
    · rw [abs_of_nonpos hr0, quarterDigammaReal_neg]
  have hpsiLower : quarterDigammaReal 0 ≤ quarterDigammaReal r := by
    rw [← habs]
    exact quarterDigammaReal_strictMonoOn.monotoneOn
      (by simp) (by simp) (abs_nonneg r)
  have hpsiUpper : quarterDigammaReal r ≤ quarterDigammaReal 50 := by
    rw [← habs]
    exact quarterDigammaReal_strictMonoOn.monotoneOn
      (by simp) (by norm_num) hr
  have hcosLower : 0 ≤ 1 - Real.cos (r * Real.log 2) := by
    linarith [Real.cos_le_one (r * Real.log 2)]
  have hcosUpper : 1 - Real.cos (r * Real.log 2) ≤ 2 := by
    linarith [Real.neg_one_le_cos (r * Real.log 2)]
  have hprimeNonneg : 0 ≤ p2PrimeAmplitude := p2PrimeAmplitude_nonneg
  have hprimeLower :
      0 ≤ p2PrimeAmplitude * (1 - Real.cos (r * Real.log 2)) :=
    mul_nonneg hprimeNonneg hcosLower
  have hsqrt : Real.sqrt 2 ≤ 2 := by
    rw [Real.sqrt_le_iff]
    norm_num
  have hlog : Real.log 2 ≤ 1 := Real.log_two_lt_d9.le.trans (by norm_num)
  have hprimeAmplitude : p2PrimeAmplitude ≤ 2 := by
    unfold p2PrimeAmplitude
    exact (mul_le_mul hsqrt hlog (Real.log_nonneg (by norm_num)) (by norm_num)).trans_eq
      (by norm_num)
  have hprimeUpper :
      p2PrimeAmplitude * (1 - Real.cos (r * Real.log 2)) ≤ 4 :=
    calc
      _ ≤ p2PrimeAmplitude * 2 :=
        mul_le_mul_of_nonneg_left hcosUpper hprimeNonneg
      _ ≤ 4 := by linarith
  rw [abs_le]
  constructor
  · have hM := quarterDigammaReal_difference_le_7447e3
    unfold p2Omega p2Alpha
    linarith
  · unfold p2Omega p2Alpha
    linarith

end GlideKernel
