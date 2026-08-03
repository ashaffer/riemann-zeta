/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.SmoothTransition
import Mathlib.Analysis.Calculus.LocalExtr.Basic

/-!
# A quantitative two-sided smooth cutoff

This file constructs a smooth cutoff which is one on `[-r, r]`, vanishes
outside `(-a, a)`, and has derivative bounded by a universal constant divided
by the transition width `a - r`.

The construction is independent of the zeta application.  Application-specific
wrappers live in `RHBridge.ExplicitSmoothCutoff`.
-/

namespace RHP2Bridge.ExplicitSmoothCutoff

noncomputable section

/-- A two-sided cutoff with transition width `a - r`. -/
def explicitCutoff (r a x : ℝ) : ℝ :=
  Real.smoothTransition ((x + a) / (a - r)) *
    Real.smoothTransition ((a - x) / (a - r))

theorem explicitCutoff_smooth {r a : ℝ} :
    ContDiff ℝ (⊤ : ℕ∞) (explicitCutoff r a) := by
  unfold explicitCutoff
  fun_prop

theorem explicitCutoff_nonneg (r a x : ℝ) :
    0 ≤ explicitCutoff r a x := by
  exact mul_nonneg (Real.smoothTransition.nonneg _)
    (Real.smoothTransition.nonneg _)

theorem explicitCutoff_le_one (r a x : ℝ) :
    explicitCutoff r a x ≤ 1 := by
  calc
    explicitCutoff r a x ≤
        1 * Real.smoothTransition ((a - x) / (a - r)) := by
      unfold explicitCutoff
      gcongr
      · exact Real.smoothTransition.nonneg _
      · exact Real.smoothTransition.le_one _
    _ ≤ 1 := by simpa using
      Real.smoothTransition.le_one ((a - x) / (a - r))

theorem explicitCutoff_eq_one {r a x : ℝ} (hra : r < a)
    (hx : x ∈ Set.Icc (-r) r) : explicitCutoff r a x = 1 := by
  have hw : 0 < a - r := sub_pos.mpr hra
  have hleft : 1 ≤ (x + a) / (a - r) := by
    rw [le_div_iff₀ hw]
    linarith [hx.1]
  have hright : 1 ≤ (a - x) / (a - r) := by
    rw [le_div_iff₀ hw]
    linarith [hx.2]
  simp [explicitCutoff, Real.smoothTransition.one_of_one_le hleft,
    Real.smoothTransition.one_of_one_le hright]

theorem explicitCutoff_eq_zero_of_le_neg {r a x : ℝ} (hra : r < a)
    (hx : x ≤ -a) : explicitCutoff r a x = 0 := by
  have hw : 0 < a - r := sub_pos.mpr hra
  have hleft : (x + a) / (a - r) ≤ 0 :=
    div_nonpos_of_nonpos_of_nonneg (by linarith) hw.le
  simp [explicitCutoff, Real.smoothTransition.zero_of_nonpos hleft]

theorem explicitCutoff_eq_zero_of_pos {r a x : ℝ} (hra : r < a)
    (hx : a ≤ x) : explicitCutoff r a x = 0 := by
  have hw : 0 < a - r := sub_pos.mpr hra
  have hright : (a - x) / (a - r) ≤ 0 :=
    div_nonpos_of_nonpos_of_nonneg (by linarith) hw.le
  simp [explicitCutoff, Real.smoothTransition.zero_of_nonpos hright]

/-- The cutoff has support contained in the open outer interval. -/
theorem support_explicitCutoff_subset {r a : ℝ} (hra : r < a) :
    Function.support (explicitCutoff r a) ⊆ Set.Ioo (-a) a := by
  intro x hx
  constructor
  · by_contra hleft
    exact hx (explicitCutoff_eq_zero_of_le_neg hra (le_of_not_gt hleft))
  · by_contra hright
    exact hx (explicitCutoff_eq_zero_of_pos hra (le_of_not_gt hright))

/-- Exact chain/product-rule formula for the derivative of `explicitCutoff`. -/
theorem deriv_explicitCutoff {r a x : ℝ} (hra : r < a) :
    deriv (explicitCutoff r a) x =
      deriv Real.smoothTransition ((x + a) / (a - r)) /
          (a - r) * Real.smoothTransition ((a - x) / (a - r)) -
        Real.smoothTransition ((x + a) / (a - r)) *
          deriv Real.smoothTransition ((a - x) / (a - r)) /
            (a - r) := by
  have hw : a - r ≠ 0 := (sub_pos.mpr hra).ne'
  have hleft : HasDerivAt
      (fun z : ℝ => Real.smoothTransition ((z + a) / (a - r)))
      (deriv Real.smoothTransition ((x + a) / (a - r)) / (a - r)) x := by
    convert (((Real.smoothTransition.contDiff (n := 1)).differentiable (by norm_num)
        ((x + a) / (a - r))).hasDerivAt.comp x
        (((hasDerivAt_id x).add_const a).div_const (a - r))) using 1 <;>
      first | rfl | ring
  have hright : HasDerivAt
      (fun z : ℝ => Real.smoothTransition ((a - z) / (a - r)))
      (-deriv Real.smoothTransition ((a - x) / (a - r)) / (a - r)) x := by
    convert (((Real.smoothTransition.contDiff (n := 1)).differentiable (by norm_num)
        ((a - x) / (a - r))).hasDerivAt.comp x
      (((hasDerivAt_const x a).sub (hasDerivAt_id x)).div_const (a - r))) using 1 <;>
      first | rfl | ring
  change deriv
      ((fun z : ℝ => Real.smoothTransition ((z + a) / (a - r))) *
        fun z : ℝ => Real.smoothTransition ((a - z) / (a - r))) x = _
  rw [(hleft.mul hright).deriv]
  ring

/-- The base transition has a finite universal slope bound. -/
theorem exists_transitionSlopeBound :
    ∃ M : ℝ, 0 ≤ M ∧ ∀ y : ℝ,
      |deriv Real.smoothTransition y| ≤ M := by
  have hcont : Continuous (fun y : ℝ =>
      |deriv Real.smoothTransition y|) :=
    ((Real.smoothTransition.contDiff (n := 2)).continuous_deriv
      (by norm_num)).abs
  obtain ⟨z, hz, hmax⟩ := isCompact_Icc.exists_isMaxOn
    (Set.nonempty_Icc.mpr (by norm_num : (0 : ℝ) ≤ 1)) hcont.continuousOn
  refine ⟨|deriv Real.smoothTransition z|, abs_nonneg _, ?_⟩
  intro y
  by_cases hy0 : y < 0
  · have hy : Real.smoothTransition y = 0 :=
      Real.smoothTransition.zero_of_nonpos hy0.le
    have hmin : IsLocalMin Real.smoothTransition y :=
      Filter.Eventually.of_forall fun q => by
        rw [hy]
        exact Real.smoothTransition.nonneg q
    rw [hmin.deriv_eq_zero, abs_zero]
    exact abs_nonneg _
  · by_cases hy1 : 1 < y
    · have hy : Real.smoothTransition y = 1 :=
        Real.smoothTransition.one_of_one_le hy1.le
      have hmaxLocal : IsLocalMax Real.smoothTransition y :=
        Filter.Eventually.of_forall fun q => by
          rw [hy]
          exact Real.smoothTransition.le_one q
      rw [hmaxLocal.deriv_eq_zero, abs_zero]
      exact abs_nonneg _
    · exact hmax ⟨le_of_not_gt hy0, le_of_not_gt hy1⟩

/-- A fixed universal slope constant for `Real.smoothTransition`. -/
def transitionSlopeBound : ℝ := Classical.choose exists_transitionSlopeBound

theorem transitionSlopeBound_nonneg : 0 ≤ transitionSlopeBound :=
  (Classical.choose_spec exists_transitionSlopeBound).1

theorem abs_deriv_smoothTransition_le (y : ℝ) :
    |deriv Real.smoothTransition y| ≤ transitionSlopeBound :=
  (Classical.choose_spec exists_transitionSlopeBound).2 y

/-- A bound `M` for the base transition gives the scaled bound
`2 * M / (a - r)` for the two-sided cutoff. -/
theorem abs_deriv_explicitCutoff_le {r a x M : ℝ} (hra : r < a)
    (hM : 0 ≤ M)
    (hslope : ∀ y, |deriv Real.smoothTransition y| ≤ M) :
    |deriv (explicitCutoff r a) x| ≤ 2 * M / (a - r) := by
  rw [deriv_explicitCutoff hra]
  have hw : 0 < a - r := sub_pos.mpr hra
  have hL0 := Real.smoothTransition.nonneg ((x + a) / (a - r))
  have hL1 := Real.smoothTransition.le_one ((x + a) / (a - r))
  have hR0 := Real.smoothTransition.nonneg ((a - x) / (a - r))
  have hR1 := Real.smoothTransition.le_one ((a - x) / (a - r))
  have hfirst :
      |deriv Real.smoothTransition ((x + a) / (a - r)) /
          (a - r) * Real.smoothTransition ((a - x) / (a - r))| ≤
        M / (a - r) := by
    rw [abs_mul, abs_div, abs_of_pos hw, abs_of_nonneg hR0]
    calc
      _ ≤ (M / (a - r)) * 1 :=
        mul_le_mul (div_le_div_of_nonneg_right (hslope _) hw.le)
          hR1 hR0 (div_nonneg hM hw.le)
      _ = _ := mul_one _
  have hsecond :
      |Real.smoothTransition ((x + a) / (a - r)) *
          deriv Real.smoothTransition ((a - x) / (a - r)) /
            (a - r)| ≤ M / (a - r) := by
    rw [abs_div, abs_mul, abs_of_pos hw, abs_of_nonneg hL0]
    have hm : Real.smoothTransition ((x + a) / (a - r)) *
        |deriv Real.smoothTransition ((a - x) / (a - r))| ≤ 1 * M :=
      mul_le_mul hL1 (hslope _) (abs_nonneg _) (by norm_num)
    simpa using div_le_div_of_nonneg_right hm hw.le
  calc
    |_ / (a - r) * _ - _ * _ / (a - r)| ≤
        |deriv Real.smoothTransition ((x + a) / (a - r)) /
            (a - r) * Real.smoothTransition ((a - x) / (a - r))| +
          |Real.smoothTransition ((x + a) / (a - r)) *
            deriv Real.smoothTransition ((a - x) / (a - r)) /
              (a - r)| := abs_sub _ _
    _ ≤ M / (a - r) + M / (a - r) := add_le_add hfirst hsecond
    _ = 2 * M / (a - r) := by ring

/-- Unconditional transition-width slope estimate for `explicitCutoff`. -/
theorem abs_deriv_explicitCutoff_le_universal {r a x : ℝ} (hra : r < a) :
    |deriv (explicitCutoff r a) x| ≤
      2 * transitionSlopeBound / (a - r) :=
  abs_deriv_explicitCutoff_le hra transitionSlopeBound_nonneg
    abs_deriv_smoothTransition_le

end

end RHP2Bridge.ExplicitSmoothCutoff
