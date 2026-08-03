/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Glide.DigammaVertical
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.PSeries

/-!
# Euler's Gamma limit, Gauss's difference series, and the trigamma series

This file formalizes the complete implication from a locally uniform version
of Euler's limit formula for `Complex.GammaSeq` to the standard trigamma
derivative series on `Re z > 0`.  Mathlib currently proves the Euler limit
pointwise (`Complex.GammaSeq_tendsto_Gamma`); the locally uniform strengthening
is isolated as the sole hypothesis of the main theorem.

The finite logarithmic-derivative identity, absolute convergence of Gauss's
two-point series and the trigamma series, and the passage through locally
uniform derivatives are all proved here without additional axioms.  Fixed
quarter-line consequences are isolated in `Glide.DigammaSeriesQuarter`.
-/

open Filter Set
open scoped Topology

namespace Complex

/-- The absolutely summable term in Gauss's two-point digamma series.  The
order is chosen so that its sum is `digamma z - digamma w`. -/
noncomputable def digammaDifferenceTerm (z w : ℂ) (n : ℕ) : ℂ :=
  1 / (w + (n : ℂ)) - 1 / (z + (n : ℂ))

/-- Gauss's two-point digamma series is absolutely summable in the positive
half-plane. -/
lemma summable_digammaDifferenceTerm {z w : ℂ} (hz : 0 < z.re) (hw : 0 < w.re) :
    Summable (digammaDifferenceTerm z w) := by
  let a : ℝ := min z.re w.re
  have ha : 0 < a := lt_min hz hw
  have hsRpow : Summable (fun n : ℕ => 1 / |(n : ℝ) + a| ^ (2 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow a 2).2 (by norm_num)
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ) + a) ^ 2) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + a)]
    change 1 / (((n : ℝ) + a) ^ (2 : ℕ)) =
      1 / Real.rpow ((n : ℝ) + a) (2 : ℝ)
    exact congrArg (fun x : ℝ => 1 / x)
      (Real.rpow_natCast ((n : ℝ) + a) 2).symm
  have hsmul : Summable (fun n : ℕ => ‖z - w‖ * (1 / ((n : ℝ) + a) ^ 2)) :=
    hs.mul_left _
  refine hsmul.of_norm_bounded (fun n => ?_)
  let Z : ℂ := z + (n : ℂ)
  let W : ℂ := w + (n : ℂ)
  have hna : 0 < (n : ℝ) + a := by positivity
  have hZre : (n : ℝ) + a ≤ Z.re := by
    dsimp [Z, a]
    linarith [min_le_left z.re w.re]
  have hWre : (n : ℝ) + a ≤ W.re := by
    dsimp [W, a]
    linarith [min_le_right z.re w.re]
  have hZnorm : (n : ℝ) + a ≤ ‖Z‖ :=
    hZre.trans (Complex.re_le_norm Z)
  have hWnorm : (n : ℝ) + a ≤ ‖W‖ :=
    hWre.trans (Complex.re_le_norm W)
  have hZpos : 0 < ‖Z‖ := hna.trans_le hZnorm
  have hWpos : 0 < ‖W‖ := hna.trans_le hWnorm
  have hden : ((n : ℝ) + a) ^ 2 ≤ ‖W‖ * ‖Z‖ := by
    nlinarith
  have hZne : Z ≠ 0 := norm_pos_iff.mp hZpos
  have hWne : W ≠ 0 := norm_pos_iff.mp hWpos
  have hterm : digammaDifferenceTerm z w n = (z - w) / (W * Z) := by
    unfold digammaDifferenceTerm
    dsimp [W, Z] at hWne hZne ⊢
    rw [one_div, one_div]
    rw [inv_sub_inv hWne hZne]
    ring
  rw [hterm, norm_div, norm_mul]
  change ‖z - w‖ / (‖W‖ * ‖Z‖) ≤ ‖z - w‖ * (1 / ((n : ℝ) + a) ^ 2)
  rw [div_eq_mul_inv]
  gcongr
  simpa only [one_div] using
    one_div_le_one_div_of_le (sq_pos_of_pos hna) hden

end Complex

namespace GlideKernel

noncomputable def trigammaSeries (z : ℂ) : ℂ :=
  ∑' n : ℕ, 1 / (z + (n : ℂ)) ^ 2

/-- The open half-plane on which Euler's Gamma integral has no poles. -/
def positiveRealHalfPlane : Set ℂ := {z | 0 < z.re}

lemma isOpen_positiveRealHalfPlane : IsOpen positiveRealHalfPlane := by
  exact Complex.continuous_re.isOpen_preimage _ isOpen_Ioi

private lemma positiveRealHalfPlane_ne_neg_nat {z : ℂ}
    (hz : z ∈ positiveRealHalfPlane) (m : ℕ) :
    z ≠ -(m : ℂ) := by
  intro h
  have hre := congrArg Complex.re h
  have hre' : z.re = -(m : ℝ) := by simpa using hre
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg m
  dsimp [positiveRealHalfPlane] at hz
  linarith

private lemma gammaSeq_ne_zero (n : ℕ) (hn : n ≠ 0) {z : ℂ}
    (hz : z ∈ positiveRealHalfPlane) : Complex.GammaSeq z n ≠ 0 := by
  have hnC : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hpow : (n : ℂ) ^ z ≠ 0 := Complex.cpow_ne_zero_iff.mpr (Or.inl hnC)
  have hfac : (Nat.factorial n : ℂ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero n
  have hterm : ∀ j ∈ Finset.range (n + 1), z + (j : ℂ) ≠ 0 := by
    intro j hj hzero
    have hpos : 0 < (z + (j : ℂ)).re := by
      dsimp [positiveRealHalfPlane] at hz
      simp only [Complex.add_re, Complex.natCast_re]
      positivity
    rw [hzero] at hpos
    simp at hpos
  unfold Complex.GammaSeq
  exact div_ne_zero (mul_ne_zero hpow hfac) (Finset.prod_ne_zero_iff.mpr hterm)

private lemma differentiableOn_gammaSeq (n : ℕ) (hn : n ≠ 0) :
    DifferentiableOn ℂ (fun z : ℂ => Complex.GammaSeq z n) positiveRealHalfPlane := by
  intro z hz
  have hnC : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hterm : ∀ j ∈ Finset.range (n + 1), z + (j : ℂ) ≠ 0 := by
    intro j hj hzero
    have hpos : 0 < (z + (j : ℂ)).re := by
      dsimp [positiveRealHalfPlane] at hz
      simp only [Complex.add_re, Complex.natCast_re]
      positivity
    rw [hzero] at hpos
    simp at hpos
  unfold Complex.GammaSeq
  exact (DifferentiableAt.div
    (((hasDerivAt_id z).const_cpow (Or.inl hnC)).differentiableAt.mul_const _)
    (DifferentiableAt.fun_finsetProd (fun j hj => by fun_prop))
    (Finset.prod_ne_zero_iff.mpr hterm)).differentiableWithinAt

lemma summable_trigammaSeries_term {z : ℂ} (hz : 0 < z.re) :
    Summable (fun n : ℕ => 1 / (z + (n : ℂ)) ^ 2) := by
  have hsRpow : Summable (fun n : ℕ => 1 / |(n : ℝ) + z.re| ^ (2 : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow z.re 2).2 (by norm_num)
  have hs : Summable (fun n : ℕ => 1 / ((n : ℝ) + z.re) ^ 2) := by
    convert hsRpow using 1
    ext n
    rw [abs_of_pos (by positivity : 0 < (n : ℝ) + z.re)]
    change
      1 / (((n : ℝ) + z.re) ^ (2 : ℕ)) =
        1 / Real.rpow ((n : ℝ) + z.re) (2 : ℝ)
    exact congrArg (fun x : ℝ => 1 / x)
      (Real.rpow_natCast ((n : ℝ) + z.re) 2).symm
  refine hs.of_norm_bounded (fun n => ?_)
  let a : ℝ := (n : ℝ) + z.re
  let w : ℂ := z + (n : ℂ)
  have ha : 0 < a := by dsimp [a]; positivity
  have haw : a ≤ ‖w‖ := by
    calc
      a = |w.re| := by
        rw [show w.re = z.re + (n : ℝ) by simp [w]]
        rw [abs_of_pos (by positivity : 0 < z.re + (n : ℝ))]
        exact add_comm _ _
      _ ≤ ‖w‖ := Complex.abs_re_le_norm w
  have hw : 0 < ‖w‖ := lt_of_lt_of_le ha haw
  have hsquare : a ^ 2 ≤ ‖w‖ ^ 2 := by nlinarith
  change ‖(1 : ℂ) / w ^ 2‖ ≤ 1 / a ^ 2
  rw [norm_div, norm_one, norm_pow]
  exact one_div_le_one_div_of_le (sq_pos_of_pos ha) hsquare

private lemma gammaSeq_logDeriv_formula (n : ℕ) (hn : n ≠ 0) (z : ℂ)
    (hz : 0 < z.re) :
    logDeriv (fun w : ℂ => Complex.GammaSeq w n) z =
      Complex.log (n : ℂ) - ∑ j ∈ Finset.range (n + 1), 1 / (z + j) := by
  have hnC : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn
  have hpow : (n : ℂ) ^ z ≠ 0 := Complex.cpow_ne_zero_iff.mpr (Or.inl hnC)
  have hfac : (Nat.factorial n : ℂ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero n
  have hnum : (n : ℂ) ^ z * (Nat.factorial n : ℂ) ≠ 0 :=
    mul_ne_zero hpow hfac
  have hterm : ∀ j : ℕ, z + (j : ℂ) ≠ 0 := by
    intro j hzero
    have hpos : 0 < (z + (j : ℂ)).re := by
      simp only [Complex.add_re, Complex.natCast_re]
      positivity
    rw [hzero] at hpos
    simp at hpos
  have hprod : (∏ j ∈ Finset.range (n + 1), (z + (j : ℂ))) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr (fun j _ => hterm j)
  have hdiffpow : DifferentiableAt ℂ (fun w : ℂ => (n : ℂ) ^ w) z :=
    ((hasDerivAt_id z).const_cpow (Or.inl hnC)).differentiableAt
  have hdiffnum : DifferentiableAt ℂ
      (fun w : ℂ => (n : ℂ) ^ w * (Nat.factorial n : ℂ)) z :=
    hdiffpow.mul_const _
  have hdiffterm : ∀ j ∈ Finset.range (n + 1),
      DifferentiableAt ℂ (fun w : ℂ => w + (j : ℂ)) z := by
    intro j hj
    fun_prop
  have hdiffprod : DifferentiableAt ℂ
      (fun w : ℂ => ∏ j ∈ Finset.range (n + 1), (w + (j : ℂ))) z :=
    DifferentiableAt.fun_finsetProd hdiffterm
  unfold Complex.GammaSeq
  rw [logDeriv_div z hnum hprod hdiffnum hdiffprod]
  rw [logDeriv_mul_const z (Nat.factorial n : ℂ) hfac]
  rw [logDeriv_apply, Complex.deriv_const_cpow (by fun_prop)]
  rw [logDeriv_prod (fun j _ => hterm j) hdiffterm]
  simp only [logDeriv_apply, deriv_add_const, deriv_id'', one_div]
  field_simp

private lemma deriv_gammaSeq_logDeriv (n : ℕ) (hn : n ≠ 0) (z : ℂ)
    (hz : 0 < z.re) :
    deriv (fun w : ℂ => logDeriv (fun v : ℂ => Complex.GammaSeq v n) w) z =
      ∑ j ∈ Finset.range (n + 1), 1 / (z + (j : ℂ)) ^ 2 := by
  have hterm : ∀ j : ℕ, z + (j : ℂ) ≠ 0 := by
    intro j hzero
    have hpos : 0 < (z + (j : ℂ)).re := by
      simp only [Complex.add_re, Complex.natCast_re]
      positivity
    rw [hzero] at hpos
    simp at hpos
  have heq :
      (fun w : ℂ => logDeriv (fun v : ℂ => Complex.GammaSeq v n) w) =ᶠ[𝓝 z]
        (fun w : ℂ => Complex.log (n : ℂ) -
          ∑ j ∈ Finset.range (n + 1), 1 / (w + (j : ℂ))) := by
    filter_upwards [isOpen_positiveRealHalfPlane.mem_nhds hz] with w hw
    exact gammaSeq_logDeriv_formula n hn w hw
  rw [heq.deriv_eq]
  rw [deriv_const_sub]
  simp only [one_div]
  rw [deriv_fun_sum (𝕜 := ℂ) (u := Finset.range (n + 1))
    (A := fun j (w : ℂ) => (w + (j : ℂ))⁻¹) (fun j hj =>
      by fun_prop (disch := aesop))]
  have hderiv (j : ℕ) :
      deriv (fun w : ℂ => (w + (j : ℂ))⁻¹) z =
        -((z + (j : ℂ)) ^ 2)⁻¹ := by
    rw [deriv_fun_inv'' (c := fun w : ℂ => w + (j : ℂ)) (by fun_prop) (hterm j)]
    simp only [deriv_add_const, deriv_id'']
    ring
  simp_rw [hderiv]
  rw [Finset.sum_neg_distrib]
  simp

private theorem gammaSeq_logDeriv_tendsto_of_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane)
    {z : ℂ} (hz : 0 < z.re) :
    Tendsto (fun n : ℕ => logDeriv (fun w : ℂ => Complex.GammaSeq w n) z)
      atTop (𝓝 (Complex.digamma z)) := by
  have hdiff : ∀ᶠ n : ℕ in atTop,
      DifferentiableOn ℂ (fun w : ℂ => Complex.GammaSeq w n)
        positiveRealHalfPlane := by
    filter_upwards [eventually_ne_atTop 0] with n hn
    exact differentiableOn_gammaSeq n hn
  simpa only [Complex.digamma_def] using Complex.logDeriv_tendsto
    isOpen_positiveRealHalfPlane hz hGammaSeq hdiff
      (Complex.Gamma_ne_zero_of_re_pos hz)

/-- A locally uniform Euler limit implies Gauss's exact two-point digamma
series on the positive-real half-plane. -/
theorem digamma_sub_eq_tsum_of_gammaSeq_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane)
    {z w : ℂ} (hz : 0 < z.re) (hw : 0 < w.re) :
    Complex.digamma z - Complex.digamma w =
      ∑' n : ℕ, Complex.digammaDifferenceTerm z w n := by
  have hlim := (gammaSeq_logDeriv_tendsto_of_locallyUniform hGammaSeq hz).sub
    (gammaSeq_logDeriv_tendsto_of_locallyUniform hGammaSeq hw)
  have hevent :
      (fun n : ℕ =>
        logDeriv (fun v : ℂ => Complex.GammaSeq v n) z -
          logDeriv (fun v : ℂ => Complex.GammaSeq v n) w) =ᶠ[atTop]
      (fun n : ℕ => ∑ j ∈ Finset.range (n + 1),
        Complex.digammaDifferenceTerm z w j) := by
    filter_upwards [eventually_ne_atTop 0] with n hn
    rw [gammaSeq_logDeriv_formula n hn z hz,
      gammaSeq_logDeriv_formula n hn w hw]
    unfold Complex.digammaDifferenceTerm
    ring_nf
    rw [← Finset.sum_neg_distrib, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro j hj
    ring
  have hseries : Tendsto
      (fun n : ℕ => ∑ j ∈ Finset.range (n + 1),
        Complex.digammaDifferenceTerm z w j)
      atTop (𝓝 (∑' n : ℕ, Complex.digammaDifferenceTerm z w n)) :=
    (Complex.summable_digammaDifferenceTerm hz hw).hasSum.tendsto_sum_nat.comp
      (tendsto_add_atTop_nat 1)
  exact tendsto_nhds_unique (hlim.congr' hevent) hseries

/-- A locally uniform version of Euler's Gamma limit formula implies the
standard trigamma derivative series on the positive-real half-plane. -/
theorem hasDerivAt_digamma_of_gammaSeq_locallyUniform
    (hGammaSeq : TendstoLocallyUniformlyOn
      (fun n z => Complex.GammaSeq z n) Complex.Gamma atTop positiveRealHalfPlane)
    {z : ℂ} (hz : 0 < z.re) :
    HasDerivAt Complex.digamma (trigammaSeries z) z := by
  have hzH : z ∈ positiveRealHalfPlane := hz
  have hGammaDiff : DifferentiableOn ℂ Complex.Gamma positiveRealHalfPlane := by
    intro w hw
    exact (Complex.differentiableAt_Gamma w
      (positiveRealHalfPlane_ne_neg_nat hw)).differentiableWithinAt
  have hGammaNe : ∀ w ∈ positiveRealHalfPlane, Complex.Gamma w ≠ 0 := by
    intro w hw
    exact Complex.Gamma_ne_zero (positiveRealHalfPlane_ne_neg_nat hw)
  have hseqDiff : ∀ᶠ n : ℕ in atTop,
      DifferentiableOn ℂ (fun w : ℂ => Complex.GammaSeq w n) positiveRealHalfPlane := by
    filter_upwards [eventually_ne_atTop 0] with n hn
    exact differentiableOn_gammaSeq n hn
  have hderivGammaSeq := hGammaSeq.deriv hseqDiff isOpen_positiveRealHalfPlane
  have hderivGammaCont : ContinuousOn (deriv Complex.Gamma) positiveRealHalfPlane :=
    (hGammaDiff.deriv isOpen_positiveRealHalfPlane).continuousOn
  have hGammaCont : ContinuousOn Complex.Gamma positiveRealHalfPlane := hGammaDiff.continuousOn
  have hquot := hderivGammaSeq.div₀ hGammaSeq hderivGammaCont hGammaCont hGammaNe
  have hquotDiff : ∀ᶠ n : ℕ in atTop,
      DifferentiableOn ℂ
        (((deriv ∘ fun n z => Complex.GammaSeq z n) /
          (fun n z => Complex.GammaSeq z n)) n)
        positiveRealHalfPlane := by
    filter_upwards [eventually_ne_atTop 0] with n hn
    have hnDiff := differentiableOn_gammaSeq n hn
    exact (hnDiff.deriv isOpen_positiveRealHalfPlane).div hnDiff
      (fun w hw => gammaSeq_ne_zero n hn hw)
  have hquotDeriv := hquot.deriv hquotDiff isOpen_positiveRealHalfPlane
  have htendDeriv : Tendsto
      (fun n => deriv
        (((deriv ∘ fun n z => Complex.GammaSeq z n) /
          (fun n z => Complex.GammaSeq z n)) n) z)
      atTop (𝓝 (deriv Complex.digamma z)) := by
    simpa only [Complex.digamma_def, logDeriv, Function.comp_apply, Pi.div_apply] using
      hquotDeriv.tendsto_at hzH
  have htendFinite : Tendsto
      (fun n => ∑ j ∈ Finset.range (n + 1), 1 / (z + (j : ℂ)) ^ 2)
      atTop (𝓝 (trigammaSeries z)) := by
    unfold trigammaSeries
    exact (summable_trigammaSeries_term hz).hasSum.tendsto_sum_nat.comp
      (tendsto_add_atTop_nat 1)
  have hevent :
      (fun n => deriv
        (((deriv ∘ fun n z => Complex.GammaSeq z n) /
          (fun n z => Complex.GammaSeq z n)) n) z) =ᶠ[atTop]
      (fun n => ∑ j ∈ Finset.range (n + 1), 1 / (z + (j : ℂ)) ^ 2) := by
    filter_upwards [eventually_ne_atTop 0] with n hn
    change deriv
      (fun w => logDeriv (fun v : ℂ => Complex.GammaSeq v n) w) z = _
    exact deriv_gammaSeq_logDeriv n hn z hz
  have hderivEq : deriv Complex.digamma z = trigammaSeries z :=
    tendsto_nhds_unique (htendDeriv.congr' hevent) htendFinite
  have hdiffDigamma : DifferentiableAt ℂ Complex.digamma z := by
    simpa only [Complex.digamma_def, logDeriv] using
      (hquot.differentiableOn hquotDiff isOpen_positiveRealHalfPlane z hzH).differentiableAt
        (isOpen_positiveRealHalfPlane.mem_nhds hzH)
  exact hdiffDigamma.hasDerivAt.congr_deriv hderivEq

end GlideKernel
