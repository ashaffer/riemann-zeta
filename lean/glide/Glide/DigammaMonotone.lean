/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# A positive series for digamma monotonicity

This file proves the positive-series core of the expected monotonicity of
`r ↦ Re (digamma (1/4 + I*r/2))`.

Mathlib currently defines `Complex.digamma`, but does not yet prove Gauss's
integral formula or the corresponding trigamma series. This file isolates
that missing analytic identity: the candidate derivative series is summable
and strictly positive for `r > 0`, and monotonicity follows from an explicit
derivative hypothesis.  `Glide.GammaUniform` and `Glide.DigammaSeries`
discharge that hypothesis unconditionally downstream.
-/

open Real Set
open scoped ComplexConjugate

namespace GlideKernel

/-- The real part of the digamma function on the vertical line `Re z = 1/4`. -/
noncomputable def quarterDigammaReal (r : ℝ) : ℝ :=
  (Complex.digamma ((1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ))).re

/-- Complex conjugation commutes with the derivative of Gamma. -/
lemma deriv_Gamma_conj (z : ℂ) :
    deriv Complex.Gamma (conj z) = conj (deriv Complex.Gamma z) := by
  have hfun : conj ∘ Complex.Gamma ∘ conj = Complex.Gamma := by
    funext w
    simp [Function.comp_apply, Complex.Gamma_conj]
  have h := congrFun (deriv_conj_conj (f := Complex.Gamma)) (conj z)
  rw [hfun] at h
  simpa [Function.comp_apply] using h

/-- The digamma function respects complex conjugation. -/
lemma digamma_conj (z : ℂ) :
    Complex.digamma (conj z) = conj (Complex.digamma z) := by
  rw [Complex.digamma_def]
  simp only [logDeriv_apply, deriv_Gamma_conj, Complex.Gamma_conj, map_div₀]

/-- The real part of digamma on the quarter-line is an even function. -/
lemma quarterDigammaReal_neg (r : ℝ) :
    quarterDigammaReal (-r) = quarterDigammaReal r := by
  unfold quarterDigammaReal
  have hline :
      (1 / 4 : ℂ) + Complex.I * (((-r) / 2 : ℝ) : ℂ) =
        conj ((1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ)) := by
    simp only [map_add, map_mul, map_div₀, map_one, map_ofNat,
      Complex.conj_ofReal, Complex.conj_I]
    push_cast
    ring
  rw [hline, digamma_conj]
  exact Complex.conj_re _

private lemma quarterLine_ne_neg_nat (r : ℝ) (m : ℕ) :
    (1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ) ≠ -(m : ℂ) := by
  intro h
  have hre := congrArg Complex.re h
  norm_num at hre
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
  linarith

/-- The digamma restriction is continuous on the quarter-line. This part does
not need a trigamma formula: it follows from meromorphicity and the fact that
the line has positive real part. -/
lemma continuousAt_quarterDigammaReal (r : ℝ) :
    ContinuousAt quarterDigammaReal r := by
  let line : ℝ → ℂ := fun s ↦ (1 / 4 : ℂ) + Complex.I * ((s / 2 : ℝ) : ℂ)
  have hz : ∀ m : ℕ, line r ≠ -(m : ℂ) := by
    simpa only [line] using quarterLine_ne_neg_nat r
  have hGamma : AnalyticAt ℂ Complex.Gamma (line r) :=
    (Meromorphic.Gamma (line r)).analyticAt (Complex.continuousAt_Gamma (line r) hz)
  have hDigamma : ContinuousAt Complex.digamma (line r) := by
    rw [Complex.digamma_def]
    change ContinuousAt (fun z ↦ logDeriv Complex.Gamma z) (line r)
    simp only [logDeriv_apply]
    exact (hGamma.deriv.div hGamma (Complex.Gamma_ne_zero hz)).continuousAt
  have hline : ContinuousAt line r := by
    unfold line
    fun_prop
  unfold quarterDigammaReal
  change ContinuousAt (fun s ↦ (Complex.digamma (line s)).re) r
  exact Complex.continuous_re.continuousAt.comp (hDigamma.comp hline)

lemma continuous_quarterDigammaReal : Continuous quarterDigammaReal :=
  continuous_iff_continuousAt.2 continuousAt_quarterDigammaReal

/-- Chain rule from a complex derivative of `digamma` to the real derivative
along the quarter-line. -/
lemma hasDerivAt_quarterDigammaReal_of_complex {r : ℝ} {d : ℂ}
    (h : HasDerivAt Complex.digamma d
      ((1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ))) :
    HasDerivAt quarterDigammaReal (Complex.I / 2 * d).re r := by
  have hline : HasDerivAt
      (fun z : ℂ ↦ (1 / 4 : ℂ) + Complex.I * (z / 2))
      (Complex.I / 2) (r : ℂ) := by
    simpa [div_eq_mul_inv] using
      (((hasDerivAt_id (r : ℂ)).div_const 2).const_mul Complex.I).const_add (1 / 4)
  have h' : HasDerivAt Complex.digamma d
      ((1 / 4 : ℂ) + Complex.I * ((r : ℂ) / 2)) := by
    simpa only [Complex.ofReal_div, Complex.ofReal_ofNat] using h
  have hcomp := h'.comp (r : ℂ) hline
  have hreal := hcomp.real_of_complex
  unfold quarterDigammaReal
  simpa [quarterDigammaReal, Function.comp_def, Complex.ofReal_div,
    mul_comm d (Complex.I / 2)] using hreal

/-- One term in the expected derivative series for `quarterDigammaReal`.

If `a = n + 1/4` and `y = r/2`, this is `a*y/(a²+y²)²`. -/
noncomputable def quarterTrigammaTerm (r : ℝ) (n : ℕ) : ℝ :=
  let a : ℝ := n + 1 / 4
  a * (r / 2) / ((a ^ 2 + (r / 2) ^ 2) ^ 2)

/-- The complex chain-rule term whose real part is
`quarterTrigammaTerm`.  It is `I/2` times one summand of the standard
trigamma series. -/
noncomputable def quarterTrigammaComplexTerm (r : ℝ) (n : ℕ) : ℂ :=
  Complex.I / 2 /
    ((((n : ℝ) + 1 / 4 : ℝ) : ℂ) +
      Complex.I * ((r / 2 : ℝ) : ℂ)) ^ 2

/-- Algebraic check that the real term is the real part produced by applying
the chain-rule factor `I/2` to a trigamma summand. -/
lemma quarterTrigammaTerm_eq_re (r : ℝ) (n : ℕ) :
    quarterTrigammaTerm r n =
      (quarterTrigammaComplexTerm r n).re := by
  unfold quarterTrigammaTerm quarterTrigammaComplexTerm
  norm_num [Complex.div_re, Complex.normSq_apply, Complex.mul_re, Complex.mul_im, pow_two]
  ring

/-- The absolutely convergent positive series which should equal the
derivative of `quarterDigammaReal`. -/
noncomputable def quarterTrigammaSlope (r : ℝ) : ℝ :=
  ∑' n : ℕ, quarterTrigammaTerm r n

private lemma abs_div_sq_add_sq_le (a y : ℝ) (ha : 0 < a) :
    |a * y / ((a ^ 2 + y ^ 2) ^ 2)| ≤ |y| / a ^ 3 := by
  have ha3 : 0 < a ^ 3 := pow_pos ha _
  have hq : 0 < a ^ 2 + y ^ 2 := by nlinarith [sq_pos_of_pos ha, sq_nonneg y]
  have hq2 : 0 < (a ^ 2 + y ^ 2) ^ 2 := pow_pos hq _
  rw [abs_div, abs_mul, abs_of_pos ha, abs_of_pos hq2]
  rw [div_le_div_iff₀ hq2 ha3]
  have haux : 0 ≤ y ^ 2 * (2 * a ^ 2 + y ^ 2) := by positivity
  have hpows : (a ^ 2) ^ 2 ≤ (a ^ 2 + y ^ 2) ^ 2 := by nlinarith
  calc
    a * |y| * a ^ 3 = |y| * (a ^ 2) ^ 2 := by ring
    _ ≤ |y| * (a ^ 2 + y ^ 2) ^ 2 :=
      mul_le_mul_of_nonneg_left hpows (abs_nonneg y)

lemma quarterTrigammaTerm_nonneg {r : ℝ} (hr : 0 ≤ r) (n : ℕ) :
    0 ≤ quarterTrigammaTerm r n := by
  unfold quarterTrigammaTerm
  have ha : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hden : 0 ≤ ((((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2) ^ 2) := by positivity
  positivity

lemma quarterTrigammaTerm_pos {r : ℝ} (hr : 0 < r) (n : ℕ) :
    0 < quarterTrigammaTerm r n := by
  unfold quarterTrigammaTerm
  have ha : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hden : 0 < ((((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2) ^ 2) := by positivity
  positivity

lemma summable_quarterTrigammaTerm (r : ℝ) :
    Summable (quarterTrigammaTerm r) := by
  have hsRpow : Summable (fun n : ℕ ↦ 1 / |(n : ℝ) + 1 / 4| ^ (3 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow (1 / 4) 3).2 (by norm_num)
  have hs : Summable (fun n : ℕ ↦ 1 / ((n : ℝ) + 1 / 4) ^ 3) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + 1 / 4)]
    change
      1 / (((n : ℝ) + 1 / 4) ^ (3 : ℕ)) =
        1 / Real.rpow ((n : ℝ) + 1 / 4) (3 : ℝ)
    exact congrArg (fun x : ℝ ↦ 1 / x)
      (Real.rpow_natCast ((n : ℝ) + 1 / 4) 3).symm
  have hsmul :
      Summable (fun n : ℕ ↦ |r / 2| * (1 / ((n : ℝ) + 1 / 4) ^ 3)) :=
    Summable.mul_left _ hs
  refine hsmul.of_norm_bounded (fun n ↦ ?_)
  have ha : 0 < (n : ℝ) + 1 / 4 := by positivity
  have hbound := abs_div_sq_add_sq_le ((n : ℝ) + 1 / 4) (r / 2) ha
  rw [Real.norm_eq_abs]
  change
    |((n : ℝ) + 1 / 4) * (r / 2) /
        ((((n : ℝ) + 1 / 4) ^ 2 + (r / 2) ^ 2) ^ 2)| ≤
      |r / 2| * (1 / ((n : ℝ) + 1 / 4) ^ 3)
  calc
    _ ≤ |r / 2| / ((n : ℝ) + 1 / 4) ^ 3 := hbound
    _ = _ := by simp only [div_eq_mul_inv, one_mul]

/-- Absolute summability of the complex chain-rule series. -/
lemma summable_quarterTrigammaComplexTerm (r : ℝ) :
    Summable (quarterTrigammaComplexTerm r) := by
  have hsRpow : Summable (fun n : ℕ ↦ 1 / |(n : ℝ) + 1 / 4| ^ (2 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow (1 / 4) 2).2 (by norm_num)
  have hs : Summable (fun n : ℕ ↦ 1 / ((n : ℝ) + 1 / 4) ^ 2) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + 1 / 4)]
    change
      1 / (((n : ℝ) + 1 / 4) ^ (2 : ℕ)) =
        1 / Real.rpow ((n : ℝ) + 1 / 4) (2 : ℝ)
    exact congrArg (fun x : ℝ ↦ 1 / x)
      (Real.rpow_natCast ((n : ℝ) + 1 / 4) 2).symm
  refine hs.of_norm_bounded (fun n ↦ ?_)
  let a : ℝ := (n : ℝ) + 1 / 4
  let w : ℂ := (a : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ)
  have ha : 0 < a := by dsimp [a]; positivity
  have haw : a ≤ ‖w‖ := by
    calc
      a = |w.re| := by simp [w, abs_of_pos ha]
      _ ≤ ‖w‖ := Complex.abs_re_le_norm w
  have hw : 0 < ‖w‖ := lt_of_lt_of_le ha haw
  have hsquare : a ^ 2 ≤ ‖w‖ ^ 2 := by nlinarith
  have hhalf : ‖(Complex.I / 2 : ℂ)‖ = (1 / 2 : ℝ) := by norm_num
  change ‖Complex.I / 2 / w ^ 2‖ ≤ 1 / a ^ 2
  rw [norm_div, norm_pow, hhalf]
  rw [div_le_div_iff₀ (pow_pos hw 2) (pow_pos ha 2)]
  nlinarith

/-- The real candidate slope is exactly the real part of the absolutely
convergent complex chain-rule series. -/
theorem quarterTrigammaSlope_eq_re_tsum (r : ℝ) :
    quarterTrigammaSlope r =
      (∑' n : ℕ, quarterTrigammaComplexTerm r n).re := by
  have hre :
      (∑' n : ℕ, quarterTrigammaComplexTerm r n).re =
        ∑' n : ℕ, (quarterTrigammaComplexTerm r n).re := by
    exact RCLike.re_tsum ℂ (summable_quarterTrigammaComplexTerm r)
  rw [hre]
  unfold quarterTrigammaSlope
  congr 1
  funext n
  exact quarterTrigammaTerm_eq_re r n

/-- The standard complex trigamma derivative series implies the exact real
derivative identity used below.  Thus the only substantive missing F7 input
can be stated directly as the usual derivative series for `Complex.digamma`. -/
theorem hasDerivAt_quarterDigammaReal_of_trigammaSeries
    {r : ℝ}
    (h : HasDerivAt Complex.digamma
      (∑' n : ℕ, 1 /
        ((((n : ℝ) + 1 / 4 : ℝ) : ℂ) +
          Complex.I * ((r / 2 : ℝ) : ℂ)) ^ 2)
      ((1 / 4 : ℂ) + Complex.I * ((r / 2 : ℝ) : ℂ))) :
    HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r := by
  have hchain := hasDerivAt_quarterDigammaReal_of_complex h
  convert hchain using 1
  rw [quarterTrigammaSlope_eq_re_tsum]
  congr 1
  rw [← tsum_mul_left]
  apply tsum_congr
  intro n
  simp only [quarterTrigammaComplexTerm, div_eq_mul_inv, one_mul]

lemma quarterTrigammaSlope_nonneg {r : ℝ} (hr : 0 ≤ r) :
    0 ≤ quarterTrigammaSlope r := by
  unfold quarterTrigammaSlope
  exact tsum_nonneg (fun n ↦ quarterTrigammaTerm_nonneg hr n)

lemma quarterTrigammaSlope_pos {r : ℝ} (hr : 0 < r) :
    0 < quarterTrigammaSlope r := by
  unfold quarterTrigammaSlope
  exact (summable_quarterTrigammaTerm r).tsum_pos
    (fun n ↦ quarterTrigammaTerm_nonneg hr.le n) 0
    (quarterTrigammaTerm_pos hr 0)

/-- Once the trigamma-series derivative identity is supplied, strict
monotonicity on the nonnegative real axis is automatic.

The hypothesis is the precise bridge not currently available in mathlib. -/
theorem quarterDigammaReal_strictMonoOn_of_hasDerivAt
    (hderiv : ∀ r : ℝ, 0 < r →
      HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r) :
    StrictMonoOn quarterDigammaReal (Ici 0) := by
  apply strictMonoOn_of_deriv_pos (convex_Ici 0) continuous_quarterDigammaReal.continuousOn
  · intro r hr
    have hr' : 0 < r := by simpa only [interior_Ici, mem_Ioi] using hr
    rw [(hderiv r hr').deriv]
    apply quarterTrigammaSlope_pos
    exact hr'

/-- Conditional F7 exterior comparison in the form used by the certificate:
once the trigamma derivative identity is known, the value at a nonnegative
cutoff is a lower bound everywhere outside the symmetric band. -/
theorem quarterDigammaReal_exterior_lower_bound_of_hasDerivAt
    (hderiv : ∀ r : ℝ, 0 < r →
      HasDerivAt quarterDigammaReal (quarterTrigammaSlope r) r)
    {S r : ℝ} (hS : 0 ≤ S) (hr : S ≤ |r|) :
    quarterDigammaReal S ≤ quarterDigammaReal r := by
  have hmono :=
    (quarterDigammaReal_strictMonoOn_of_hasDerivAt hderiv).monotoneOn
  have habs_nonneg : |r| ∈ Ici (0 : ℝ) := abs_nonneg r
  have hcut : quarterDigammaReal S ≤ quarterDigammaReal |r| :=
    hmono hS habs_nonneg hr
  have heven : quarterDigammaReal |r| = quarterDigammaReal r := by
    by_cases hnonneg : 0 ≤ r
    · rw [abs_of_nonneg hnonneg]
    · have hnonpos : r ≤ 0 := le_of_not_ge hnonneg
      rw [abs_of_nonpos hnonpos, quarterDigammaReal_neg]
  exact hcut.trans_eq heven

end GlideKernel
