/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.PolyEnclosure
import Glide.DigammaBounds

/-!
# Accelerated `p = 2` digamma-tail enclosures

This module replaces the infinite rational-kernel tail in the canonical
`p = 2` endpoint with a finite polynomial in shifted power tails.  A finite
geometric expansion supplies the polynomial, while an explicit positive
`p`-series controls the complete analytic remainder.

Every error estimate is a theorem over `ℝ`; generated numerical certificates
may instantiate these bounds, but no external numerical evaluation is trusted.
-/

namespace RHP2Bridge

open scoped BigOperators

noncomputable def reciprocalPowerExpansion (K : ℕ) (a c : ℝ) : ℝ :=
  a⁻¹ * ∑ k ∈ Finset.range K, (-(c / a^2))^k

theorem reciprocalPowerExpansion_eq_sum (K : ℕ) (a c : ℝ) (ha : a ≠ 0) :
    reciprocalPowerExpansion K a c =
      ∑ k ∈ Finset.range K,
        (-1 : ℝ)^k * c^k / a^(2*k+1) := by
  unfold reciprocalPowerExpansion
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  rw [neg_pow (c/a^2) k, div_pow,
    show (a^2)^k = a^(2*k) by rw [pow_mul], pow_succ]
  field_simp

lemma rationalKernel_eq_inv_mul (a c : ℝ) (ha : a ≠ 0) :
    a / (a^2+c) = a⁻¹ * (1 + c/a^2)⁻¹ := by
  by_cases hd : a^2+c = 0
  · have hc : c = -a^2 := by linarith
    rw [hc]
    simp [ha]
  · field_simp

theorem abs_rationalKernel_sub_reciprocalPowerExpansion_le
    (K : ℕ) (a c : ℝ) (ha : 0 < a) (hc : 0 ≤ c) :
    |a / (a^2+c) - reciprocalPowerExpansion K a c| ≤
      c^K / a^(2*K+1) := by
  let u := c/a^2
  have hu : 0 ≤ u := by dsimp [u]; positivity
  have hden : 1+u ≠ 0 := by positivity
  rw [rationalKernel_eq_inv_mul a c ha.ne']
  unfold reciprocalPowerExpansion
  change |a⁻¹ * (1+u)⁻¹ - a⁻¹ * ∑ k ∈ Finset.range K, (-u)^k| ≤ _
  rw [← mul_sub, abs_mul]
  rw [PolyEnclosure.scalar_geometric_reciprocal_identity u K hden]
  rw [abs_inv, abs_of_pos ha, abs_div, abs_pow, abs_neg,
    abs_of_nonneg hu, abs_of_pos (by positivity : 0 < 1+u)]
  have hfrac : u^K / (1+u) ≤ u^K := by
    rw [div_le_iff₀ (by positivity : 0 < 1+u)]
    nlinarith [pow_nonneg hu K]
  calc
    a⁻¹ * (u^K / (1+u)) ≤ a⁻¹ * u^K :=
      mul_le_mul_of_nonneg_left hfrac (by positivity)
    _ = c^K / a^(2*K+1) := by
      dsimp [u]
      rw [div_pow, show (a^2)^K = a^(2*K) by rw [pow_mul], pow_succ]
      field_simp

noncomputable def quarterTailExpansionTerm (r : ℝ) (K N n : ℕ) : ℝ :=
  let a : ℝ := (N+n : ℕ) + 1/4
  reciprocalPowerExpansion K a 625 -
    reciprocalPowerExpansion K a ((r/2)^2)

theorem quarterTailExpansionTerm_eq_sum (r : ℝ) (K N n : ℕ) :
    quarterTailExpansionTerm r K N n =
      ∑ k ∈ Finset.range K,
        (-1 : ℝ)^k * (625^k - (r/2)^(2*k)) /
          ((((N+n : ℕ) : ℝ) + 1/4)^(2*k+1)) := by
  let a : ℝ := ((N+n : ℕ) : ℝ) + 1/4
  have ha : a ≠ 0 := by dsimp [a]; positivity
  unfold quarterTailExpansionTerm
  dsimp only
  rw [reciprocalPowerExpansion_eq_sum K a 625 ha,
    reciprocalPowerExpansion_eq_sum K a ((r/2)^2) ha,
    ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro k hk
  rw [show ((r/2)^2)^k = (r/2)^(2*k) by rw [pow_mul]]
  ring

theorem abs_quarterDifferenceTerm_sub_tailExpansionTerm_le
    (r : ℝ) (K N n : ℕ) :
    |GlideKernel.quarterDifferenceTerm r 50 (N+n) -
      quarterTailExpansionTerm r K N n| ≤
      (625^K + (r/2)^(2*K)) /
        (((N+n : ℕ) : ℝ) + 1/4)^(2*K+1) := by
  let a : ℝ := (N : ℝ) + (n : ℝ) + 1/4
  have ha : 0 < a := by dsimp [a]; positivity
  have h625 := abs_rationalKernel_sub_reciprocalPowerExpansion_le
    K a 625 ha (by norm_num)
  have hr := abs_rationalKernel_sub_reciprocalPowerExpansion_le
    K a ((r/2)^2) ha (sq_nonneg _)
  unfold GlideKernel.quarterDifferenceTerm quarterTailExpansionTerm
  dsimp only
  norm_num
  change |(a/(a^2+625) - a/(a^2+(r/2)^2)) - _| ≤ _
  have hrearrange :
      (a/(a^2+625) - a/(a^2+(r/2)^2)) -
          (reciprocalPowerExpansion K a 625 -
            reciprocalPowerExpansion K a ((r/2)^2)) =
        (a/(a^2+625) - reciprocalPowerExpansion K a 625) -
          (a/(a^2+(r/2)^2) -
            reciprocalPowerExpansion K a ((r/2)^2)) := by ring
  rw [hrearrange]
  calc
    |_ - _| ≤
        |a/(a^2+625) - reciprocalPowerExpansion K a 625| +
          |a/(a^2+(r/2)^2) -
            reciprocalPowerExpansion K a ((r/2)^2)| := abs_sub _ _
    _ ≤ 625^K/a^(2*K+1) + ((r/2)^2)^K/a^(2*K+1) :=
      add_le_add h625 hr
    _ = (625^K+(r/2)^(2*K))/a^(2*K+1) := by
      rw [← pow_mul]
      ring

noncomputable def shiftedPowerTail (p N : ℕ) : ℝ :=
  ∑' n : ℕ, 1 / ((((N+n : ℕ) : ℝ) + 1/4)^p)

lemma summable_shiftedPowerTail (p N : ℕ) (hp : 1 < p) :
    Summable (fun n : ℕ => 1 / ((((N+n : ℕ) : ℝ) + 1/4)^p)) := by
  have hsRpow : Summable (fun n : ℕ =>
      1 / |(n : ℝ) + ((N : ℝ) + 1/4)| ^ (p : ℝ)) :=
    (Real.summable_one_div_nat_add_rpow ((N : ℝ) + 1/4) p).2
      (by exact_mod_cast hp)
  convert hsRpow using 1
  ext n
  have hpos : 0 < (n : ℝ) + ((N : ℝ) + 1/4) := by positivity
  rw [abs_of_pos hpos]
  rw [← Real.rpow_natCast]
  norm_num [Nat.cast_add]
  ring

lemma summable_quarterDifferenceTail (r : ℝ) (N : ℕ) :
    Summable (fun n : ℕ => GlideKernel.quarterDifferenceTerm r 50 (N+n)) := by
  have hs := (GlideKernel.summable_quarterDifferenceTerm r 50).comp_injective
    (show Function.Injective (fun n : ℕ => N+n) by
      intro a b h
      exact Nat.add_left_cancel h)
  exact hs

noncomputable def quarterTailPolynomial (r : ℝ) (K N : ℕ) : ℝ :=
  ∑ k ∈ Finset.range K,
    (-1 : ℝ)^k * (625^k - (r/2)^(2*k)) *
      shiftedPowerTail (2*k+1) N

theorem quarterTailExpansion_tsum_eq_polynomial
    (r : ℝ) (K N : ℕ) :
    ∑' n : ℕ, quarterTailExpansionTerm r K N n =
      quarterTailPolynomial r K N := by
  have hs (k : ℕ) (hk : k ∈ Finset.range K) : Summable (fun n : ℕ =>
      ((-1 : ℝ)^k * (625^k - (r/2)^(2*k))) *
        (1 / ((((N+n : ℕ) : ℝ) + 1/4)^(2*k+1)))) := by
    by_cases hk0 : k = 0
    · subst k
      simp
    · have hp : 1 < 2*k+1 := by omega
      exact (summable_shiftedPowerTail (2*k+1) N hp).mul_left _
  rw [show (fun n : ℕ => quarterTailExpansionTerm r K N n) =
      (fun n : ℕ => ∑ k ∈ Finset.range K,
        ((-1 : ℝ)^k * (625^k - (r/2)^(2*k))) *
          (1 / ((((N+n : ℕ) : ℝ) + 1/4)^(2*k+1)))) by
    funext n
    rw [quarterTailExpansionTerm_eq_sum]
    apply Finset.sum_congr rfl
    intro k hk
    ring]
  rw [Summable.tsum_finsetSum hs]
  unfold quarterTailPolynomial shiftedPowerTail
  apply Finset.sum_congr rfl
  intro k hk
  rw [tsum_mul_left]

theorem abs_quarterDifference_tail_tsum_sub_expansion_le
    (r : ℝ) (K N : ℕ) (hK : 1 ≤ K) :
    |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 (N+n)) -
        ∑' n : ℕ, quarterTailExpansionTerm r K N n| ≤
      (625^K + (r/2)^(2*K)) * shiftedPowerTail (2*K+1) N := by
  let actual : ℕ → ℝ := fun n =>
    GlideKernel.quarterDifferenceTerm r 50 (N+n)
  let approx : ℕ → ℝ := fun n => quarterTailExpansionTerm r K N n
  let major : ℕ → ℝ := fun n =>
    (625^K + (r/2)^(2*K)) /
      ((((N+n : ℕ) : ℝ) + 1/4)^(2*K+1))
  have hp : 1 < 2*K+1 := by omega
  have hpow := summable_shiftedPowerTail (2*K+1) N hp
  have hC : 0 ≤ 625^K + (r/2)^(2*K) := by
    have heven : 0 ≤ (r/2)^(2*K) := by
      rw [show 2*K=K+K by omega, pow_add]
      exact mul_self_nonneg _
    positivity
  have hmajor : Summable major := by
    unfold major
    simp only [div_eq_mul_inv]
    simpa only [one_div, one_mul, div_eq_mul_inv] using
      hpow.mul_left (625^K + (r/2)^(2*K))
  have hpoint (n : ℕ) : |actual n - approx n| ≤ major n := by
    exact abs_quarterDifferenceTerm_sub_tailExpansionTerm_le r K N n
  have hdiff : Summable (fun n => actual n - approx n) := by
    apply Summable.of_norm_bounded hmajor
    intro n
    rw [Real.norm_eq_abs]
    exact hpoint n
  have hactual : Summable actual := summable_quarterDifferenceTail r N
  have happrox : Summable approx := by
    have hs := hactual.sub hdiff
    have heq : (fun n => actual n - (actual n - approx n)) = approx := by
      funext n
      ring
    rwa [heq] at hs
  have htsub := hactual.tsum_sub happrox
  rw [← htsub]
  rw [← Real.norm_eq_abs]
  calc
    ‖∑' n : ℕ, (actual n - approx n)‖ ≤
        ∑' n : ℕ, ‖actual n - approx n‖ :=
      norm_tsum_le_tsum_norm hdiff.norm
    _ ≤ ∑' n : ℕ, major n :=
      hdiff.norm.tsum_le_tsum (fun n => by
        rw [Real.norm_eq_abs]
        exact hpoint n) hmajor
    _ = (625^K + (r/2)^(2*K)) * shiftedPowerTail (2*K+1) N := by
      unfold shiftedPowerTail major
      simp_rw [div_eq_mul_inv]
      rw [tsum_mul_left]
      simp only [one_mul]

theorem abs_quarterDifference_tail_tsum_sub_polynomial_le
    (r : ℝ) (K N : ℕ) (hK : 1 ≤ K) :
    |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 (N+n)) -
        quarterTailPolynomial r K N| ≤
      (625^K + (r/2)^(2*K)) * shiftedPowerTail (2*K+1) N := by
  rw [← quarterTailExpansion_tsum_eq_polynomial]
  exact abs_quarterDifference_tail_tsum_sub_expansion_le r K N hK

noncomputable def quarterDifferenceApprox (r : ℝ) (K N : ℕ) : ℝ :=
  (∑ n ∈ Finset.range N, GlideKernel.quarterDifferenceTerm r 50 n) +
    quarterTailPolynomial r K N

/-- Accelerated finite-plus-polynomial enclosure of the complete rational
digamma-difference series.  The only residual constant is one rapidly
decaying positive p-series tail. -/
theorem abs_quarterDifference_tsum_sub_approx_le
    (r : ℝ) (K N : ℕ) (hK : 1 ≤ K) :
    |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
        quarterDifferenceApprox r K N| ≤
      (625^K + (r/2)^(2*K)) * shiftedPowerTail (2*K+1) N := by
  rw [← (GlideKernel.summable_quarterDifferenceTerm r 50).sum_add_tsum_nat_add N]
  unfold quarterDifferenceApprox
  have htail := abs_quarterDifference_tail_tsum_sub_polynomial_le r K N hK
  convert htail using 1
  simp only [add_sub_add_left_eq_sub, Nat.add_comm]

noncomputable def inversePowerMajorant (p : ℕ) (x : ℝ) : ℝ :=
  x ^ (-(p : ℝ))

private lemma inversePowerMajorant_antitone (p N : ℕ) (hN : 2 ≤ N) :
    AntitoneOn (inversePowerMajorant p) (Set.Ici ((N - 1 : ℕ) : ℝ)) := by
  unfold inversePowerMajorant
  refine (Real.antitoneOn_rpow_Ioi_of_exponent_nonpos
    (neg_nonpos.mpr (Nat.cast_nonneg p))).mono ?_
  intro x hx
  have hpos : (0 : ℝ) < ((N - 1 : ℕ) : ℝ) := by
    exact_mod_cast (show 0 < N - 1 by omega)
  exact hpos.trans_le hx

private lemma inversePowerMajorant_integrable (p N : ℕ)
    (hp : 1 < p) (hN : 2 ≤ N) :
    MeasureTheory.IntegrableOn (inversePowerMajorant p)
      (Set.Ioi ((N - 1 : ℕ) : ℝ)) := by
  unfold inversePowerMajorant
  apply integrableOn_Ioi_rpow_of_lt
  · have hp' : (1 : ℝ) < (p : ℝ) := by exact_mod_cast hp
    linarith
  · exact_mod_cast (show 0 < N - 1 by omega)

private lemma inversePowerMajorant_nonneg (p N : ℕ) (hN : 2 ≤ N)
    (x : ℝ) (hx : x ∈ Set.Ioi ((N - 1 : ℕ) : ℝ)) :
    0 ≤ inversePowerMajorant p x := by
  unfold inversePowerMajorant
  exact Real.rpow_nonneg (le_of_lt ((show (0 : ℝ) < ((N - 1 : ℕ) : ℝ) by
    exact_mod_cast (show 0 < N - 1 by omega)).trans hx)) _

/-- Explicit integral-test bound for the sole infinite residual in
`quarterDifferenceApprox`. -/
theorem shiftedPowerTail_le (p N : ℕ) (hp : 1 < p) (hN : 2 ≤ N) :
    shiftedPowerTail p N ≤
      1 / ((p - 1 : ℕ) * (N - 1 : ℕ) ^ (p - 1) : ℕ) := by
  have hanti := inversePowerMajorant_antitone p N hN
  have hint := inversePowerMajorant_integrable p N hp hN
  have hnonneg := inversePowerMajorant_nonneg p N hN
  have hsumMajor : Summable (fun n : ℕ => inversePowerMajorant p (n + N : ℕ)) := by
    have hsRpow : Summable (fun n : ℕ =>
        1 / |(n : ℝ) + (N : ℝ)| ^ (p : ℝ)) :=
      (Real.summable_one_div_nat_add_rpow N p).2 (by exact_mod_cast hp)
    apply hsRpow.congr
    intro n
    symm
    unfold inversePowerMajorant
    have hb : 0 < (n : ℝ) + N := by positivity
    rw [Nat.cast_add, Real.rpow_neg hb.le, Real.rpow_natCast, abs_of_pos hb,
      Real.rpow_natCast]
    simp only [one_div]
  have hpoint (n : ℕ) :
      1 / ((((N + n : ℕ) : ℝ) + 1 / 4) ^ p) ≤
        inversePowerMajorant p ((n + N : ℕ) : ℝ) := by
    unfold inversePowerMajorant
    have hb : 0 < ((n + N : ℕ) : ℝ) := by
      exact_mod_cast (show 0 < n + N by omega)
    rw [Real.rpow_neg hb.le, Real.rpow_natCast]
    have hbase : ((n + N : ℕ) : ℝ) ≤ ((N + n : ℕ) : ℝ) + 1 / 4 := by
      push_cast
      linarith
    simpa only [one_div] using
      one_div_le_one_div_of_le (pow_pos hb p) (pow_le_pow_left₀ hb.le hbase p)
  have hcompare : shiftedPowerTail p N ≤
      ∑' n : ℕ, inversePowerMajorant p ((n + N : ℕ) : ℝ) := by
    unfold shiftedPowerTail
    exact (summable_shiftedPowerTail p N hp).tsum_le_tsum hpoint hsumMajor
  have hintegral := hanti.tsum_comp_add_le_integral (N - 1) hint hnonneg
  have htail : (∑' n : ℕ, inversePowerMajorant p ((n + N : ℕ) : ℝ)) ≤
      ∫ x in Set.Ioi (((N - 1 : ℕ) : ℝ)), inversePowerMajorant p x := by
    calc
      _ = ∑' n : ℕ,
          inversePowerMajorant p (((n + (N - 1) + 1 : ℕ) : ℝ)) := by
        congr 1
        funext n
        congr 2
        omega
      _ ≤ _ := hintegral
  refine hcompare.trans (htail.trans ?_)
  unfold inversePowerMajorant
  rw [integral_Ioi_rpow_of_lt]
  · have hpCast : ((p - 1 : ℕ) : ℝ) = (p : ℝ) - 1 := by
      rw [Nat.cast_sub (show 1 ≤ p by omega)]
      norm_num
    have hbase : (0 : ℝ) < ((N - 1 : ℕ) : ℝ) := by
      exact_mod_cast (show 0 < N - 1 by omega)
    rw [show (-(p : ℝ) + 1) = -((p - 1 : ℕ) : ℝ) by linarith,
      Real.rpow_neg hbase.le, Real.rpow_natCast]
    push_cast
    have hpbase : (0 : ℝ) < ((p - 1 : ℕ) : ℝ) := by
      exact_mod_cast (show 0 < p - 1 by omega)
    have hpownz : ((N - 1 : ℕ) : ℝ) ^ (p - 1) ≠ 0 :=
      pow_ne_zero _ hbase.ne'
    field_simp
    exact le_rfl
  · have hp' : (1 : ℝ) < (p : ℝ) := by exact_mod_cast hp
    linarith
  · exact_mod_cast (show 0 < N - 1 by omega)

lemma shiftedPowerTail_nonneg (p N : ℕ) : 0 ≤ shiftedPowerTail p N := by
  unfold shiftedPowerTail
  exact tsum_nonneg fun n => by positivity

/-- A summable discrete derivative telescopes exactly.  This packages the
kernel argument used by generated Euler--Maclaurin tail certificates. -/
theorem tsum_telescope_eq_of_summable (g : ℕ → ℝ) (hg : Summable g) :
    (∑' n : ℕ, (g n - g (n + 1))) = g 0 := by
  have hgshift : Summable (fun n : ℕ => g (n + 1)) :=
    hg.comp_injective Nat.succ_injective
  have hdiff : Summable (fun n : ℕ => g n - g (n + 1)) := hg.sub hgshift
  have hpartial : Filter.Tendsto
      (fun N : ℕ => ∑ n ∈ Finset.range N, (g n - g (n + 1)))
      Filter.atTop (nhds (g 0)) := by
    simp_rw [Finset.sum_range_sub']
    simpa only [sub_zero] using
      tendsto_const_nhds.sub hg.tendsto_atTop_zero
  exact tendsto_nhds_unique hdiff.hasSum.tendsto_sum_nat hpartial

theorem tsum_le_of_telescope
    (f g : ℕ → ℝ) (hf : Summable f) (hg : Summable g)
    (h : ∀ n, f n ≤ g n - g (n + 1)) :
    ∑' n, f n ≤ g 0 := by
  have hgshift : Summable (fun n : ℕ => g (n + 1)) :=
    hg.comp_injective Nat.succ_injective
  have hdiff : Summable (fun n : ℕ => g n - g (n + 1)) := hg.sub hgshift
  calc
    ∑' n, f n ≤ ∑' n, (g n - g (n + 1)) :=
      hf.tsum_le_tsum h hdiff
    _ = g 0 := tsum_telescope_eq_of_summable g hg

theorem telescope_le_tsum
    (f g : ℕ → ℝ) (hf : Summable f) (hg : Summable g)
    (h : ∀ n, g n - g (n + 1) ≤ f n) :
    g 0 ≤ ∑' n, f n := by
  have hgshift : Summable (fun n : ℕ => g (n + 1)) :=
    hg.comp_injective Nat.succ_injective
  have hdiff : Summable (fun n : ℕ => g n - g (n + 1)) := hg.sub hgshift
  calc
    g 0 = ∑' n, (g n - g (n + 1)) :=
      (tsum_telescope_eq_of_summable g hg).symm
    _ ≤ ∑' n, f n := hdiff.tsum_le_tsum h hf

/-- On the full canonical frequency window, a 64-term rational prefix and
16-term inverse-power tail polynomial approximate the digamma-difference
series to strictly better than `10⁻¹⁴`.  Every constant in this statement is
rational and is checked by the kernel. -/
theorem abs_quarterDifference_tsum_sub_approx_lt_1e14
    {r : ℝ} (hr : |r| ≤ 50) :
    |(∑' n : ℕ, GlideKernel.quarterDifferenceTerm r 50 n) -
        quarterDifferenceApprox r 16 64| < 1 / 10 ^ 14 := by
  have hmain :=
    abs_quarterDifference_tsum_sub_approx_le r 16 64 (by norm_num)
  have htail := shiftedPowerTail_le 33 64 (by norm_num) (by norm_num)
  have habs : |r / 2| ≤ 25 := by
    rw [abs_div]
    norm_num
    linarith
  have hrpow : (r / 2) ^ 32 ≤ 625 ^ 16 := by
    calc
      (r / 2) ^ 32 = |r / 2| ^ 32 :=
        ((by norm_num : Even 32).pow_abs (r / 2)).symm
      _ ≤ 25 ^ 32 := pow_le_pow_left₀ (abs_nonneg _) habs 32
      _ = 625 ^ 16 := by norm_num
  have hcoeff : 625 ^ 16 + (r / 2) ^ 32 ≤ (2 * 625 ^ 16 : ℝ) := by
    norm_num at hrpow ⊢
    linarith
  have htail' : shiftedPowerTail 33 64 ≤ (1 : ℝ) / (32 * 63 ^ 32) := by
    norm_num at htail ⊢
    exact htail
  calc
    _ ≤ (625 ^ 16 + (r / 2) ^ 32) * shiftedPowerTail 33 64 := hmain
    _ ≤ (2 * 625 ^ 16) * ((1 : ℝ) / (32 * 63 ^ 32)) :=
      mul_le_mul hcoeff htail' (shiftedPowerTail_nonneg 33 64) (by positivity)
    _ < 1 / 10 ^ 14 := by norm_num

end RHP2Bridge
