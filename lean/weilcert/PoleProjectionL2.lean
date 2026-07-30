/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import FullInfLegendreLedger

/-!
# Taylor control of the pole vectors in the finite Legendre section

This file realizes `x ↦ exp (±x/2)` as vectors in the real interval
`L²` space, constructs their `m`-term Taylor competitors, proves that those
competitors lie in the first `m` scaled Legendre modes, and bounds the
canonical orthogonal-projection residual.

At `(a,m) = (7/16,48)`, both signs have residual strictly below the exact
rational `195 / 10^95`.
-/

namespace PoleProjection

open Polynomial
open scoped ENNReal InnerProductSpace

noncomputable def poleContinuous (a s : ℝ) : C(LegendreScaledL2.Interval a, ℝ) where
  toFun x := Real.exp (s * (x : ℝ) / 2)
  continuous_toFun := by fun_prop

noncomputable def poleL2 (a s : ℝ) : LegendreScaledL2.IntervalL2 a :=
  ContinuousMap.toLp 2 (LegendreScaledL2.intervalMeasure a) ℝ (poleContinuous a s)

/-- The positive pole vector `x ↦ exp (x/2)` in interval `L²`. -/
noncomputable def polePlusL2 (a : ℝ) : LegendreScaledL2.IntervalL2 a :=
  poleL2 a 1

/-- The negative pole vector `x ↦ exp (-x/2)` in interval `L²`. -/
noncomputable def poleMinusL2 (a : ℝ) : LegendreScaledL2.IntervalL2 a :=
  poleL2 a (-1)

/-- The squared `L²` norm of a pole vector is its elementary exponential
integral. -/
theorem norm_poleL2_sq_eq_integral (a s : ℝ) (ha : 0 ≤ a) :
    ‖poleL2 a s‖ ^ 2 = ∫ x in -a..a, Real.exp (s * x) := by
  rw [@InnerProductSpace.norm_sq_eq_re_inner ℝ
    (LegendreScaledL2.IntervalL2 a)]
  simp only [RCLike.re_to_real]
  rw [poleL2, MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc (-a) a,
      Real.exp (s * (x : ℝ) / 2) * Real.exp (s * (x : ℝ) / 2)
        ∂(LegendreScaledL2.intervalMeasure a)) = _
  rw [LegendreScaledL2.intervalMeasure]
  rw [MeasureTheory.integral_subtype_comap
      (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
      measurableSet_Icc
      (fun x : ℝ ↦
        Real.exp (s * x / 2) * Real.exp (s * x / 2))]
  rw [intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  rw [← Real.exp_add]
  congr 1
  ring

theorem norm_polePlusL2_sq (a : ℝ) (ha : 0 ≤ a) :
    ‖polePlusL2 a‖ ^ 2 = Real.exp a - Real.exp (-a) := by
  rw [polePlusL2, norm_poleL2_sq_eq_integral _ _ ha]
  simp only [one_mul]
  exact integral_exp

theorem norm_poleMinusL2_sq (a : ℝ) (ha : 0 ≤ a) :
    ‖poleMinusL2 a‖ ^ 2 = Real.exp a - Real.exp (-a) := by
  rw [poleMinusL2, norm_poleL2_sq_eq_integral _ _ ha]
  have hreflect :
      (∫ x in -a..a, Real.exp (-x)) = ∫ x in -a..a, Real.exp x := by
    convert (intervalIntegral.integral_comp_neg
      (f := fun x : ℝ ↦ Real.exp x) (a := -a) (b := a)) using 1
    all_goals simp
  rw [show (fun x : ℝ ↦ Real.exp ((-1 : ℝ) * x)) =
      fun x : ℝ ↦ Real.exp (-x) by funext x; ring_nf]
  rw [hreflect]
  exact integral_exp

/-- Exact elementary norm ledger needed by the complement/cross-block
operator estimate. -/
theorem p2_polePlusL2_norm_le_one :
    ‖polePlusL2 (7 / 16)‖ ≤ 1 := by
  have hexp : Real.exp (7 / 32) < (249 : ℝ) / 200 :=
    FullInfLegendreLedger.exp_seven_div_32_lt
  have hu : Real.exp (7 / 16) < ((249 : ℝ) / 200) ^ 2 := by
    rw [show (7 : ℝ) / 16 = 7 / 32 + 7 / 32 by norm_num,
      Real.exp_add, pow_two]
    gcongr
  have hl : (9 : ℝ) / 16 ≤ Real.exp (-(7 / 16)) := by
    convert Real.add_one_le_exp (-(7 / 16 : ℝ)) using 1
    all_goals norm_num
  have hsq := norm_polePlusL2_sq (7 / 16) (by norm_num)
  have hn := norm_nonneg (polePlusL2 (7 / 16))
  nlinarith

theorem p2_poleMinusL2_norm_le_one :
    ‖poleMinusL2 (7 / 16)‖ ≤ 1 := by
  have hsqPlus := norm_polePlusL2_sq (7 / 16) (by norm_num)
  have hsqMinus := norm_poleMinusL2_sq (7 / 16) (by norm_num)
  have hplus := p2_polePlusL2_norm_le_one
  have hnplus := norm_nonneg (polePlusL2 (7 / 16))
  have hn := norm_nonneg (poleMinusL2 (7 / 16))
  nlinarith

noncomputable def poleTaylorPolynomial (s : ℝ) (m : ℕ) : ℝ[X] :=
  ∑ k ∈ Finset.range m, Polynomial.monomial k ((s / 2) ^ k / k.factorial)

theorem poleTaylorPolynomial_eval (s x : ℝ) (m : ℕ) :
    (poleTaylorPolynomial s m).eval x =
      ∑ k ∈ Finset.range m, (s * x / 2) ^ k / k.factorial := by
  simp only [poleTaylorPolynomial, eval_finsetSum, eval_monomial]
  apply Finset.sum_congr rfl
  intro k hk
  rw [div_pow, div_pow, mul_pow]
  ring

theorem poleTaylorPolynomial_coeff (s : ℝ) (m k : ℕ) (hk : k < m) :
    (poleTaylorPolynomial s m).coeff k =
      (s / 2) ^ k / k.factorial := by
  classical
  rw [poleTaylorPolynomial]
  change Polynomial.lcoeff ℝ k (∑ b ∈ Finset.range m,
    Polynomial.monomial b ((s / 2) ^ b / b.factorial)) = _
  rw [map_sum]
  simp only [Polynomial.lcoeff_apply]
  rw [Finset.sum_eq_single k]
  · rw [coeff_monomial]
    simp
  · intro b hb hbk
    rw [coeff_monomial]
    simp [hbk]
  · intro hknot
    exact (hknot (Finset.mem_range.mpr hk)).elim

theorem poleTaylorPolynomial_mem_degreeLT (s : ℝ) (m : ℕ) :
    poleTaylorPolynomial s m ∈ Polynomial.degreeLT ℝ m := by
  rw [poleTaylorPolynomial]
  apply Submodule.sum_mem
  intro k hk
  rw [Finset.mem_range] at hk
  rw [Polynomial.mem_degreeLT]
  by_cases hc : (s / 2) ^ k / (k.factorial : ℝ) = 0
  · simp [hc]
  · simp [Polynomial.degree_monomial, hc, hk]

/-- For a nonzero sign and `m > 0`, the `m`-term competitor has exact
degree `m - 1`. -/
theorem poleTaylorPolynomial_natDegree
    (s : ℝ) (hs : s ≠ 0) (m : ℕ) (hm : 0 < m) :
    (poleTaylorPolynomial s m).natDegree = m - 1 := by
  have hkm : m - 1 < m := by omega
  have hcoeff : (poleTaylorPolynomial s m).coeff (m - 1) ≠ 0 := by
    rw [poleTaylorPolynomial_coeff s m (m - 1) hkm]
    exact div_ne_zero (pow_ne_zero _ (div_ne_zero hs (by norm_num))) (by positivity)
  have hne : poleTaylorPolynomial s m ≠ 0 := by
    intro hzero
    rw [hzero, coeff_zero] at hcoeff
    exact hcoeff rfl
  have hlower : m - 1 ≤ (poleTaylorPolynomial s m).natDegree :=
    Polynomial.le_natDegree_of_ne_zero hcoeff
  have hdegree := poleTaylorPolynomial_mem_degreeLT s m
  rw [Polynomial.mem_degreeLT] at hdegree
  have hupper : (poleTaylorPolynomial s m).natDegree < m :=
    (Polynomial.natDegree_lt_iff_degree_lt hne).2 hdegree
  omega

theorem polynomialToL2_mem_finiteLegendreSubspace_of_mem_degreeLT
    (a : ℝ) (ha : 0 < a) (m : ℕ) (p : ℝ[X])
    (hp : p ∈ Polynomial.degreeLT ℝ m) :
    LegendreScaledL2.polynomialToL2 a p ∈
      LegendreScaledL2.finiteLegendreSubspace a m := by
  let S := LegendreScaledL2.scaledNormalizedPlainLegendreSequence a ha
  have hspan : Submodule.span ℝ (S '' Set.Iio m) = Polynomial.degreeLT ℝ m :=
    S.span_degreeLT (fun i hi => by
      rw [isUnit_iff_ne_zero]
      exact Polynomial.leadingCoeff_ne_zero.mpr (S.ne_zero i))
  rw [← hspan] at hp
  rw [LegendreScaledL2.finiteLegendreSubspace]
  refine Submodule.span_induction
    (p := fun q _ ↦ LegendreScaledL2.polynomialToL2 a q ∈
      Submodule.span ℝ
        (LegendreScaledL2.scaledNormalizedLegendreL2 a ''
          (Finset.range m : Set ℕ)))
    ?_ ?_ ?_ ?_ hp
  · intro q hq
    rcases hq with ⟨i, hi, rfl⟩
    apply Submodule.subset_span
    refine ⟨i, ?_, ?_⟩
    · simpa only [Finset.mem_coe, Finset.mem_range, Set.mem_Iio] using hi
    · rfl
  · rw [map_zero]
    exact Submodule.zero_mem _
  · intro x y hx hy hx' hy'
    rw [map_add]
    exact Submodule.add_mem _ hx' hy'
  · intro r q hq hq'
    rw [map_smul]
    exact Submodule.smul_mem _ r hq'

theorem poleTaylorL2_mem_finiteLegendreSubspace
    (a : ℝ) (ha : 0 < a) (s : ℝ) (m : ℕ) :
    LegendreScaledL2.polynomialToL2 a (poleTaylorPolynomial s m) ∈
      LegendreScaledL2.finiteLegendreSubspace a m :=
  polynomialToL2_mem_finiteLegendreSubspace_of_mem_degreeLT a ha m _
    (poleTaylorPolynomial_mem_degreeLT s m)

theorem pole_projection_residual_le_taylor_competitor
    (a : ℝ) (ha : 0 < a) (s : ℝ) (m : ℕ) :
    ‖poleL2 a s -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (poleL2 a s)‖ ≤
      ‖poleL2 a s -
        LegendreScaledL2.polynomialToL2 a (poleTaylorPolynomial s m)‖ := by
  let U := LegendreScaledL2.finiteLegendreSubspace a m
  let c : U :=
    ⟨LegendreScaledL2.polynomialToL2 a (poleTaylorPolynomial s m),
      poleTaylorL2_mem_finiteLegendreSubspace a ha s m⟩
  have hb : BddBelow (Set.range (fun x : U ↦ ‖poleL2 a s - (x :
      LegendreScaledL2.IntervalL2 a)‖)) := by
    refine ⟨0, ?_⟩
    rintro _ ⟨x, rfl⟩
    exact norm_nonneg _
  change ‖poleL2 a s - U.starProjection (poleL2 a s)‖ ≤
    ‖poleL2 a s - (c : LegendreScaledL2.IntervalL2 a)‖
  rw [Submodule.starProjection_minimal]
  exact ciInf_le hb c

theorem norm_poleL2_sub_taylor_sq_eq_integral
    (a : ℝ) (ha : 0 ≤ a) (s : ℝ) (m : ℕ) :
    ‖poleL2 a s -
        LegendreScaledL2.polynomialToL2 a (poleTaylorPolynomial s m)‖ ^ 2 =
      ∫ x in -a..a,
        (Real.exp (s * x / 2) - (poleTaylorPolynomial s m).eval x) ^ 2 := by
  rw [@InnerProductSpace.norm_sq_eq_re_inner ℝ
    (LegendreScaledL2.IntervalL2 a)]
  simp only [RCLike.re_to_real]
  rw [poleL2, LegendreScaledL2.polynomialToL2_apply, ← map_sub,
    MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc (-a) a,
      ((poleContinuous a s -
          (poleTaylorPolynomial s m).toContinuousMapOn
            (LegendreScaledL2.Interval a)) x) *
        ((poleContinuous a s -
          (poleTaylorPolynomial s m).toContinuousMapOn
            (LegendreScaledL2.Interval a)) x)
        ∂(LegendreScaledL2.intervalMeasure a)) = _
  rw [LegendreScaledL2.intervalMeasure]
  change (∫ x : Set.Icc (-a) a,
      (Real.exp (s * (x : ℝ) / 2) -
          (poleTaylorPolynomial s m).eval (x : ℝ)) *
        (Real.exp (s * (x : ℝ) / 2) -
          (poleTaylorPolynomial s m).eval (x : ℝ))
        ∂(MeasureTheory.Measure.comap Subtype.val MeasureTheory.volume)) = _
  rw [MeasureTheory.integral_subtype_comap
      (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
      measurableSet_Icc
      (fun x : ℝ ↦
        (Real.exp (s * x / 2) - (poleTaylorPolynomial s m).eval x) *
          (Real.exp (s * x / 2) - (poleTaylorPolynomial s m).eval x))]
  rw [intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with x
  simp only [pow_two]

theorem poleTaylor_pointwise_remainder
    (a : ℝ) (_ha : 0 ≤ a) (ha2 : a / 2 ≤ 1)
    (s : ℝ) (hs : |s| ≤ 1) (m : ℕ) (hm : 0 < m)
    (x : LegendreScaledL2.Interval a) :
    |Real.exp (s * (x : ℝ) / 2) -
        (poleTaylorPolynomial s m).eval (x : ℝ)| ≤
      (a / 2) ^ m * (m.succ / (m.factorial * m : ℝ)) := by
  have hxabs : |(x : ℝ)| ≤ a := by
    rw [abs_le]
    exact x.property
  have harg : |s * (x : ℝ) / 2| ≤ 1 := by
    calc
      |s * (x : ℝ) / 2| = |s| * |(x : ℝ)| / 2 := by rw [abs_div, abs_mul]; norm_num
      _ ≤ 1 * a / 2 := by gcongr
      _ = a / 2 := by ring
      _ ≤ 1 := ha2
  rw [poleTaylorPolynomial_eval]
  refine (Real.exp_bound harg hm).trans ?_
  have hargA : |s * (x : ℝ) / 2| ≤ a / 2 := by
    calc
      |s * (x : ℝ) / 2| = |s| * |(x : ℝ)| / 2 := by rw [abs_div, abs_mul]; norm_num
      _ ≤ 1 * a / 2 := by gcongr
      _ = a / 2 := by ring
  gcongr

theorem norm_poleL2_sub_taylor_sq_le
    (a : ℝ) (ha : 0 ≤ a) (ha2 : a / 2 ≤ 1)
    (s : ℝ) (hs : |s| ≤ 1) (m : ℕ) (hm : 0 < m) :
    ‖poleL2 a s -
        LegendreScaledL2.polynomialToL2 a (poleTaylorPolynomial s m)‖ ^ 2 ≤
      2 * a *
        ((a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))) ^ 2 := by
  rw [norm_poleL2_sub_taylor_sq_eq_integral a ha]
  let M : ℝ := (a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))
  have hM : 0 ≤ M := by
    dsimp [M]
    positivity
  have hint :
      IntervalIntegrable
        (fun x : ℝ ↦
          (Real.exp (s * x / 2) - (poleTaylorPolynomial s m).eval x) ^ 2)
        MeasureTheory.volume (-a) a := by
    apply Continuous.intervalIntegrable
    fun_prop
  have hmono := intervalIntegral.integral_mono_on
    (show -a ≤ a by linarith) hint (intervalIntegrable_const :
      IntervalIntegrable (fun _ : ℝ ↦ M ^ 2) MeasureTheory.volume (-a) a)
    (fun x hx ↦ by
      have hrem := poleTaylor_pointwise_remainder a ha ha2 s hs m hm
        ⟨x, hx⟩
      change |Real.exp (s * x / 2) -
          (poleTaylorPolynomial s m).eval x| ≤ M at hrem
      rw [← sq_abs]
      exact pow_le_pow_left₀ (abs_nonneg _) hrem 2)
  rw [intervalIntegral.integral_const] at hmono
  change _ ≤ (a - -a) * M ^ 2 at hmono
  calc
    _ ≤ (a - -a) * M ^ 2 := hmono
    _ = 2 * a *
        ((a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))) ^ 2 := by
      dsimp [M]
      ring

theorem pole_projection_residual_sq_le
    (a : ℝ) (ha : 0 < a) (ha2 : a / 2 ≤ 1)
    (s : ℝ) (hs : |s| ≤ 1) (m : ℕ) (hm : 0 < m) :
    ‖poleL2 a s -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (poleL2 a s)‖ ^ 2 ≤
      2 * a *
        ((a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))) ^ 2 := by
  have hmin := pole_projection_residual_le_taylor_competitor a ha s m
  exact (pow_le_pow_left₀ (norm_nonneg _) hmin 2).trans
    (norm_poleL2_sub_taylor_sq_le a ha.le ha2 s hs m hm)

theorem pole_projection_residual_le
    (a : ℝ) (ha : 0 < a) (ha2 : a / 2 ≤ 1)
    (s : ℝ) (hs : |s| ≤ 1) (m : ℕ) (hm : 0 < m) :
    ‖poleL2 a s -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (poleL2 a s)‖ ≤
      Real.sqrt (2 * a) *
        ((a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))) := by
  let M : ℝ := (a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))
  have hM : 0 ≤ M := by
    dsimp [M]
    positivity
  have hsq := pole_projection_residual_sq_le a ha ha2 s hs m hm
  change ‖poleL2 a s -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (poleL2 a s)‖ ^ 2 ≤ 2 * a * M ^ 2 at hsq
  calc
    ‖poleL2 a s -
        (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
          (poleL2 a s)‖ =
        Real.sqrt (‖poleL2 a s -
          (LegendreScaledL2.finiteLegendreSubspace a m).starProjection
            (poleL2 a s)‖ ^ 2) := by
          rw [Real.sqrt_sq_eq_abs, abs_of_nonneg (norm_nonneg _)]
    _ ≤ Real.sqrt (2 * a * M ^ 2) := Real.sqrt_le_sqrt hsq
    _ = Real.sqrt (2 * a) * M := by
      rw [Real.sqrt_mul (by positivity), Real.sqrt_sq_eq_abs,
        abs_of_nonneg hM]
    _ = Real.sqrt (2 * a) *
        ((a / 2) ^ m * (m.succ / (m.factorial * m : ℝ))) := rfl

theorem p2_pole_projection_residual_le_majorant
    (s : ℝ) (hs : |s| ≤ 1) :
    ‖poleL2 (7 / 16) s -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (poleL2 (7 / 16) s)‖ ≤
      FullInfLegendreLedger.p2PoleTaylorMajorant := by
  have hres := pole_projection_residual_le
    (7 / 16) (by norm_num) (by norm_num) s hs 48 (by norm_num)
  calc
    ‖poleL2 (7 / 16) s -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (poleL2 (7 / 16) s)‖ ≤
        Real.sqrt (7 / 8) *
          ((7 / 32) ^ 48 *
            ((49 : ℝ) / (Nat.factorial 48 * 48 : ℝ))) := by
      convert hres using 1
      all_goals norm_num
    _ ≤ FullInfLegendreLedger.p2PoleTaylorMajorant := by
      have hexpLower : (49 : ℝ) / 48 ≤ Real.exp (7 / 32) := by
        calc
          (49 : ℝ) / 48 ≤ 1 + 7 / 32 := by norm_num
          _ ≤ Real.exp (7 / 32) := by
            simpa [add_comm] using Real.add_one_le_exp (7 / 32)
      unfold FullInfLegendreLedger.p2PoleTaylorMajorant
      calc
        Real.sqrt (7 / 8) *
              ((7 / 32) ^ 48 *
                ((49 : ℝ) / (Nat.factorial 48 * 48 : ℝ))) =
            (Real.sqrt (7 / 8) * (7 / 32) ^ 48 /
                Nat.factorial 48) * ((49 : ℝ) / 48) := by ring
        _ ≤ (Real.sqrt (7 / 8) * (7 / 32) ^ 48 /
                Nat.factorial 48) * Real.exp (7 / 32) := by
          gcongr
        _ = Real.sqrt (7 / 8) * Real.exp (7 / 32) *
              (7 / 32) ^ 48 / Nat.factorial 48 := by ring

theorem p2_pole_projection_residual_lt
    (s : ℝ) (hs : |s| ≤ 1) :
    ‖poleL2 (7 / 16) s -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (poleL2 (7 / 16) s)‖ <
      (195 : ℝ) / 10 ^ 95 :=
  (p2_pole_projection_residual_le_majorant s hs).trans_lt
    FullInfLegendreLedger.p2PoleTaylorMajorant_lt

theorem p2_polePlus_projection_residual_lt :
    ‖polePlusL2 (7 / 16) -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (polePlusL2 (7 / 16))‖ <
      (195 : ℝ) / 10 ^ 95 := by
  simpa [polePlusL2] using p2_pole_projection_residual_lt 1 (by norm_num)

theorem p2_poleMinus_projection_residual_lt :
    ‖poleMinusL2 (7 / 16) -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (poleMinusL2 (7 / 16))‖ <
      (195 : ℝ) / 10 ^ 95 := by
  simpa [poleMinusL2] using p2_pole_projection_residual_lt (-1) (by norm_num)

theorem p2_polePlus_projection_residual_le :
    ‖polePlusL2 (7 / 16) -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (polePlusL2 (7 / 16))‖ ≤
      (195 : ℝ) / 10 ^ 95 :=
  p2_polePlus_projection_residual_lt.le

theorem p2_poleMinus_projection_residual_le :
    ‖poleMinusL2 (7 / 16) -
        (LegendreScaledL2.finiteLegendreSubspace (7 / 16) 48).starProjection
          (poleMinusL2 (7 / 16))‖ ≤
      (195 : ℝ) / 10 ^ 95 :=
  p2_poleMinus_projection_residual_lt.le

end PoleProjection
