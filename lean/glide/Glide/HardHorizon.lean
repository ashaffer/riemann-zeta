/-
HardHorizon: Lean formalization of the Hard Horizon Theorem (T1′),
results/experts/T1PRIME.md (§2, §7 ladder).  Complete for the staircase
scope: Theorem 1 (`hard_horizon`) and the selected-radius/raw-bound core of
Corollary 2 (`zero_desert`) are proved, with no sorries and only the three
standard axioms.

Ladder items (Lean name ↔ T1PRIME.md item):

* `lemma0_D_at_eTstar`      ↔ Lemma 0   (count horizon: D(eT*) = −7/8 exactly)
* `lemma1_entire`/`lemma1_growth`(+`_recentered`) ↔ Lemma L1 (F = φ̂ entire,
      ‖F(z)‖ ≤ √(2a)·e^{a·|Im z|}); `lemma1_sinh_le` is the scalar core
* `lemma2_sum_log_eq_integral` ↔ Lemma L2 (Fubini/layer-cake identity;
      finite index set, multiplicity carried by the index set);
      `lemma2_integrableOn` the companion integrability
* `lemma3_rvM_integral`     ↔ Lemma L3 (rvM Jensen mass, closed form)
* `lemma4_rigidity_transfer`↔ Lemma L4 (rigidity transfer)
* `lemma5_radius_selection`/`lemma5_jensen` ↔ Lemma L5 (radius selection —
      including no-zeros-on-circle, which L6 genuinely needs — + Jensen)
* `lemma6_circle_bound`(+`_tau`) ↔ Lemma L6 (circle bound, eq. (L6.1))
* `lemma7_pair_product`     ↔ Lemma L7, arithmetic core (pair-product bound)
* `lemma7_other_mass_nonneg`↔ Lemma L7, last clause
* `lemma7_divisor_lower`    ↔ Lemma L7, divisor side (prescribed multiset
      dominated by the Jensen divisor sum)
* `lemma8_strictMonoOn`/`lemma8_crossing`/`lemma8_tau_bound` ↔ Lemma L8 +
      the §3 endgame extraction
* `hard_horizon`            ↔ **Theorem 1** (staircase form)
* `analyticOrderAt_translate`/`hard_horizon_of_global_orders` ↔ the
      paper-facing (S3) form, with vanishing orders stated directly at `±tₖ`
* `zero_desert`             ↔ selected-radius/raw-bound core of **Corollary 2**

Corollary 1 (ζ without RH, but with its anchor hypothesis) is out of scope —
blocked on a formalized RvM/S(T) with explicit constants (T1PRIME.md §7). See
results/agent-t1prime-lean.md for audits and deviations.
-/
import Mathlib

open Real MeasureTheory Set MeromorphicOn

namespace HardHorizon

/-! ### Definitions (T1PRIME.md §0–§1 notation) -/

/-- The Riemann–von Mangoldt staircase `N̂(s) = (s/2π)·ln(s/(2πe)) + 7/8`. -/
noncomputable def Nhat (s : ℝ) : ℝ :=
  s / (2 * π) * Real.log (s / (2 * π * Real.exp 1)) + 7 / 8

/-- The anchor constant `B = (κ + 4 + 2/π)·a + ½·ln(2a)` of Theorem 1. -/
noncomputable def BConst (a κ : ℝ) : ℝ :=
  (κ + 4 + 2 / π) * a + 1 / 2 * Real.log (2 * a)

/-- `ε*` of Theorem 1, positive-case value (the theorem statement applies
`max 0 ·` to this; Lemma L8 is used exactly when this is positive). -/
noncomputable def epsStar (a R κ : ℝ) : ℝ :=
  (BConst a κ + 2 * R * (2 * a + 1)) / (2 * (Real.exp (2 * a + 2) - R))

/-- `h(τ) = 2e^τ(τ − 2 − 2a) − 2R(τ − 1)` of Lemma L8. -/
noncomputable def hFn (a R τ : ℝ) : ℝ :=
  2 * Real.exp τ * (τ - 2 - 2 * a) - 2 * R * (τ - 1)

/-! ### Lemma 0 (count horizon; calculus identity)

`D(T) = (a/π)T − N̂(T)` satisfies `D(eT*) = −7/8` exactly, where
`eT* = 2πe^{2a+1}`. -/

theorem lemma0_D_at_eTstar (a : ℝ) :
    a / π * (2 * π * Real.exp (2 * a + 1)) - Nhat (2 * π * Real.exp (2 * a + 1))
      = -(7 / 8) := by
  have hπ : (π : ℝ) ≠ 0 := pi_ne_zero
  unfold Nhat
  have hexp : Real.exp (2 * a + 1) = Real.exp (2 * a) * Real.exp 1 := Real.exp_add (2 * a) 1
  have h1 : 2 * π * Real.exp (2 * a + 1) / (2 * π * Real.exp 1) = Real.exp (2 * a) := by
    rw [hexp]
    field_simp
  rw [h1, Real.log_exp]
  field_simp
  ring

/-! ### Lemma L2 (Fubini/layer-cake identity)

For a finite multiset `{tₖ}` of positive reals (multiplicity carried by the
index Finset `ι`) with all `tₖ ≤ T`:
`Σₖ ln(T/tₖ) = ∫_{(0,T]} N(s)/s ds`, where `N(s) = #{k : tₖ ≤ s}`. -/

/-- Each `Ioc`-indicator of `u⁻¹` is integrable on `(0, T]` provided the left
endpoint is positive. -/
lemma indicator_inv_integrable {c T : ℝ} (hc : 0 < c) :
    Integrable ((Ioc c T).indicator (fun u : ℝ => u⁻¹)) (volume.restrict (Ioc 0 T)) := by
  rw [integrable_indicator_iff measurableSet_Ioc]
  change Integrable (fun u : ℝ => u⁻¹) ((volume.restrict (Ioc (0 : ℝ) T)).restrict (Ioc c T))
  rw [Measure.restrict_restrict measurableSet_Ioc,
    inter_eq_left.mpr (Ioc_subset_Ioc_left hc.le)]
  have hcont : IntegrableOn (fun u : ℝ => u⁻¹) (Icc c T) := by
    apply ContinuousOn.integrableOn_Icc
    apply ContinuousOn.inv₀ continuousOn_id
    intro x hx
    exact ne_of_gt (lt_of_lt_of_le hc hx.1)
  exact hcont.mono_set Ioc_subset_Icc_self

/-- The sum of indicators equals the counting-function integrand a.e. on
`(0, T]` (they differ only on the finite set `{tₖ}`). -/
lemma sum_indicator_ae_eq {α : Type*} (ι : Finset α) (t : α → ℝ) (T : ℝ) :
    (fun s => ∑ k ∈ ι, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s)
      =ᵐ[volume.restrict (Ioc (0 : ℝ) T)]
    (fun s => (({k ∈ ι | t k ≤ s} : Finset α).card : ℝ) / s) := by
  have hE0 : (volume : Measure ℝ) ↑(ι.image t) = 0 :=
    Set.Finite.measure_zero (ι.image t).finite_toSet volume
  have hae : ∀ᵐ s : ℝ ∂volume, s ∉ (↑(ι.image t) : Set ℝ) :=
    measure_eq_zero_iff_ae_notMem.mp hE0
  filter_upwards [ae_restrict_of_ae hae, ae_restrict_mem measurableSet_Ioc] with s hsE hs
  have hsT : s ≤ T := hs.2
  have hterm : ∀ k ∈ ι,
      (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s = if t k ≤ s then s⁻¹ else 0 := by
    intro k hk
    by_cases h : t k ≤ s
    · have hne : t k ≠ s := by
        intro heq
        apply hsE
        rw [← heq]
        exact Finset.mem_coe.mpr (Finset.mem_image_of_mem t hk)
      have hmem : s ∈ Ioc (t k) T := ⟨lt_of_le_of_ne h hne, hsT⟩
      rw [if_pos h, Set.indicator_of_mem hmem]
    · have hmem : s ∉ Ioc (t k) T := fun hmem => h (le_of_lt hmem.1)
      rw [if_neg h, Set.indicator_of_notMem hmem]
  calc ∑ k ∈ ι, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s
      = ∑ k ∈ ι, if t k ≤ s then s⁻¹ else 0 := Finset.sum_congr rfl hterm
    _ = ∑ _k ∈ ι.filter (fun k => t k ≤ s), s⁻¹ := (Finset.sum_filter _ _).symm
    _ = ((ι.filter (fun k => t k ≤ s)).card : ℝ) * s⁻¹ := by
        rw [Finset.sum_const, nsmul_eq_mul]
    _ = ((ι.filter (fun k => t k ≤ s)).card : ℝ) / s := by
        rw [div_eq_mul_inv]

/-- **Lemma L2** (T1PRIME.md, eq. (L2.1)): the Fubini/layer-cake identity. -/
theorem lemma2_sum_log_eq_integral {α : Type*} (ι : Finset α) (t : α → ℝ) {T : ℝ}
    (ht : ∀ k ∈ ι, 0 < t k) (htT : ∀ k ∈ ι, t k ≤ T) :
    ∑ k ∈ ι, Real.log (T / t k)
      = ∫ s in Ioc (0 : ℝ) T, (({k ∈ ι | t k ≤ s} : Finset α).card : ℝ) / s := by
  have hstep : ∀ k ∈ ι, Real.log (T / t k)
      = ∫ s in Ioc (0 : ℝ) T, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s := by
    intro k hk
    have htk := ht k hk
    have hkT := htT k hk
    have h0 : (0 : ℝ) ∉ uIcc (t k) T := by
      rw [uIcc_of_le hkT]
      exact fun h => absurd h.1 (not_le.mpr htk)
    have h1 := integral_inv h0
    rw [← h1, intervalIntegral.integral_of_le hkT,
      setIntegral_indicator measurableSet_Ioc,
      inter_eq_right.mpr (Ioc_subset_Ioc_left htk.le)]
  have hint : ∀ k ∈ ι,
      Integrable ((Ioc (t k) T).indicator (fun u : ℝ => u⁻¹)) (volume.restrict (Ioc 0 T)) :=
    fun k hk => indicator_inv_integrable (ht k hk)
  calc ∑ k ∈ ι, Real.log (T / t k)
      = ∑ k ∈ ι, ∫ s in Ioc (0 : ℝ) T, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s :=
        Finset.sum_congr rfl hstep
    _ = ∫ s in Ioc (0 : ℝ) T, ∑ k ∈ ι, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s :=
        (integral_finsetSum ι hint).symm
    _ = ∫ s in Ioc (0 : ℝ) T, (({k ∈ ι | t k ≤ s} : Finset α).card : ℝ) / s :=
        integral_congr_ae (sum_indicator_ae_eq ι t T)

/-- Companion to L2: the counting-function integrand is integrable on `(0,T]`
(needed to feed L2 into L4). -/
theorem lemma2_integrableOn {α : Type*} (ι : Finset α) (t : α → ℝ) {T : ℝ}
    (ht : ∀ k ∈ ι, 0 < t k) :
    IntegrableOn (fun s => (({k ∈ ι | t k ≤ s} : Finset α).card : ℝ) / s)
      (Ioc (0 : ℝ) T) := by
  have hsum : Integrable (fun s => ∑ k ∈ ι, (Ioc (t k) T).indicator (fun u : ℝ => u⁻¹) s)
      (volume.restrict (Ioc 0 T)) :=
    integrable_finsetSum ι (fun k hk => indicator_inv_integrable (ht k hk))
  exact hsum.congr (sum_indicator_ae_eq ι t T)

/-! ### Lemma L3 (the rvM Jensen mass — closed form)

`∫_{2πe}^{2πe^τ} N̂(s)/s ds = e^τ(τ−2) + (7/8)(τ−1) + e` for `τ ≥ 1`. -/

theorem lemma3_rvM_integral {τ : ℝ} (hτ : 1 ≤ τ) :
    ∫ s in (2 * π * Real.exp 1)..(2 * π * Real.exp τ), Nhat s / s
      = Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 := by
  have hπ : (π : ℝ) ≠ 0 := pi_ne_zero
  have hpos : (0 : ℝ) < 2 * π * Real.exp 1 := by positivity
  have hle : 2 * π * Real.exp 1 ≤ 2 * π * Real.exp τ :=
    mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hτ) (by positivity)
  have hmem : ∀ x ∈ uIcc (2 * π * Real.exp 1) (2 * π * Real.exp τ), (0 : ℝ) < x := by
    intro x hx
    rw [uIcc_of_le hle] at hx
    exact lt_of_lt_of_le hpos hx.1
  set A : ℝ → ℝ := fun s =>
    s * (Real.log s - Real.log (2 * π * Real.exp 1) - 1) / (2 * π) + 7 / 8 * Real.log s
    with hA
  have hderiv : ∀ x ∈ uIcc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      HasDerivAt A (Nhat x / x) x := by
    intro x hx
    have hx0 : (0 : ℝ) < x := hmem x hx
    have hlog : HasDerivAt Real.log x⁻¹ x := Real.hasDerivAt_log (ne_of_gt hx0)
    have hv : HasDerivAt (fun s => Real.log s - Real.log (2 * π * Real.exp 1) - 1) x⁻¹ x :=
      (hlog.sub_const _).sub_const 1
    have hmul : HasDerivAt (fun s => s * (Real.log s - Real.log (2 * π * Real.exp 1) - 1))
        (1 * (Real.log x - Real.log (2 * π * Real.exp 1) - 1) + x * x⁻¹) x :=
      (hasDerivAt_id x).mul hv
    have hsum := (hmul.div_const (2 * π)).add (hlog.const_mul (7 / 8 : ℝ))
    have hval : (1 * (Real.log x - Real.log (2 * π * Real.exp 1) - 1) + x * x⁻¹) / (2 * π)
        + 7 / 8 * x⁻¹ = Nhat x / x := by
      unfold Nhat
      rw [Real.log_div (ne_of_gt hx0) (ne_of_gt (by positivity))]
      field_simp
      ring
    exact hval ▸ hsum
  have hint : IntervalIntegrable (fun s => Nhat s / s) volume
      (2 * π * Real.exp 1) (2 * π * Real.exp τ) := by
    apply ContinuousOn.intervalIntegrable
    apply ContinuousOn.div ?_ continuousOn_id (fun x hx => ne_of_gt (hmem x hx))
    unfold Nhat
    apply ContinuousOn.add ?_ continuousOn_const
    apply ContinuousOn.mul (Continuous.continuousOn (by fun_prop))
    apply ContinuousOn.log (Continuous.continuousOn (by fun_prop))
    intro x hx
    have := hmem x hx
    positivity
  have key := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (f := A) (f' := fun s => Nhat s / s) hderiv hint
  rw [key]
  simp only [hA]
  have hlogτ : Real.log (2 * π * Real.exp τ) = Real.log (2 * π) + τ := by
    rw [Real.log_mul (by positivity) (Real.exp_ne_zero τ), Real.log_exp]
  have hlog1 : Real.log (2 * π * Real.exp 1) = Real.log (2 * π) + 1 := by
    rw [Real.log_mul (by positivity) (Real.exp_ne_zero 1), Real.log_exp]
  rw [hlogτ, hlog1]
  field_simp
  ring

/-! ### Lemma L4 (rigidity transfer)

If `N ≥ 0` on `(0, T̃]` and `N ≥ N̂ − R` on `[2πe, T̃]` (the one-sided
rigidity (S2)), then `∫_{(0,T̃]} N(s)/s ds ≥ e^τ(τ−2) + (7/8)(τ−1) + e − R(τ−1)`. -/

theorem lemma4_rigidity_transfer {N : ℝ → ℝ} {R τ : ℝ} (hτ : 1 ≤ τ)
    (hInt : IntegrableOn (fun s => N s / s) (Ioc 0 (2 * π * Real.exp τ)))
    (hpos : ∀ s ∈ Ioc (0 : ℝ) (2 * π * Real.exp τ), 0 ≤ N s)
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ), Nhat s - R ≤ N s) :
    Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 - R * (τ - 1)
      ≤ ∫ s in Ioc (0 : ℝ) (2 * π * Real.exp τ), N s / s := by
  have hπ : (π : ℝ) ≠ 0 := pi_ne_zero
  have hpos1 : (0 : ℝ) < 2 * π * Real.exp 1 := by positivity
  have hle : 2 * π * Real.exp 1 ≤ 2 * π * Real.exp τ :=
    mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hτ) (by positivity)
  have hunion : Ioc (0 : ℝ) (2 * π * Real.exp τ)
      = Ioc 0 (2 * π * Real.exp 1) ∪ Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ) :=
    (Ioc_union_Ioc_eq_Ioc hpos1.le hle).symm
  have hdisj : Disjoint (Ioc (0 : ℝ) (2 * π * Real.exp 1))
      (Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ)) := by
    rw [Set.disjoint_left]
    rintro x ⟨_, h2⟩ ⟨h3, _⟩
    exact absurd h3 (not_lt.mpr h2)
  have hI1 : IntegrableOn (fun s => N s / s) (Ioc 0 (2 * π * Real.exp 1)) :=
    hInt.mono_set (by rw [hunion]; exact subset_union_left)
  have hI2 : IntegrableOn (fun s => N s / s)
      (Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ)) :=
    hInt.mono_set (by rw [hunion]; exact subset_union_right)
  have hsplit : ∫ s in Ioc (0 : ℝ) (2 * π * Real.exp τ), N s / s
      = (∫ s in Ioc (0 : ℝ) (2 * π * Real.exp 1), N s / s)
        + ∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), N s / s := by
    rw [hunion]
    exact setIntegral_union hdisj measurableSet_Ioc hI1 hI2
  have h1 : 0 ≤ ∫ s in Ioc (0 : ℝ) (2 * π * Real.exp 1), N s / s := by
    apply setIntegral_nonneg measurableSet_Ioc
    intro s hs
    exact div_nonneg (hpos s ⟨hs.1, le_trans hs.2 hle⟩) hs.1.le
  -- integrability of the comparison integrands on the outer window
  have hmemIcc : ∀ x ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ), (0 : ℝ) < x :=
    fun x hx => lt_of_lt_of_le hpos1 hx.1
  have hIa : IntegrableOn (fun s => Nhat s / s)
      (Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ)) := by
    apply IntegrableOn.mono_set ?_ Ioc_subset_Icc_self
    apply ContinuousOn.integrableOn_Icc
    apply ContinuousOn.div ?_ continuousOn_id (fun x hx => ne_of_gt (hmemIcc x hx))
    unfold Nhat
    apply ContinuousOn.add ?_ continuousOn_const
    apply ContinuousOn.mul (Continuous.continuousOn (by fun_prop))
    apply ContinuousOn.log (Continuous.continuousOn (by fun_prop))
    intro x hx
    have := hmemIcc x hx
    positivity
  have hIb : IntegrableOn (fun s : ℝ => R * s⁻¹)
      (Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ)) := by
    apply IntegrableOn.mono_set ?_ Ioc_subset_Icc_self
    apply ContinuousOn.integrableOn_Icc
    apply ContinuousOn.mul continuousOn_const
    apply ContinuousOn.inv₀ continuousOn_id
    intro x hx
    exact ne_of_gt (hmemIcc x hx)
  have hIg : IntegrableOn (fun s => Nhat s / s - R * s⁻¹)
      (Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ)) := hIa.sub hIb
  -- pointwise comparison on the outer window
  have h2 : (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), (Nhat s / s - R * s⁻¹))
      ≤ ∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), N s / s := by
    apply setIntegral_mono_on hIg hI2 measurableSet_Ioc
    intro s hs
    have hs0 : (0 : ℝ) < s := lt_trans hpos1 hs.1
    have hcmp := hrig s (Ioc_subset_Icc_self hs)
    calc Nhat s / s - R * s⁻¹ = (Nhat s - R) * s⁻¹ := by
          rw [sub_mul, div_eq_mul_inv]
      _ ≤ N s * s⁻¹ := mul_le_mul_of_nonneg_right hcmp (inv_nonneg.mpr hs0.le)
      _ = N s / s := (div_eq_mul_inv _ _).symm
  -- exact value of the comparison integral
  have h0uIcc : (0 : ℝ) ∉ uIcc (2 * π * Real.exp 1) (2 * π * Real.exp τ) := by
    rw [uIcc_of_le hle]
    exact fun h => absurd h.1 (not_le.mpr hpos1)
  have hlogratio : Real.log (2 * π * Real.exp τ / (2 * π * Real.exp 1)) = τ - 1 := by
    rw [Real.log_div (by positivity) (by positivity),
      Real.log_mul (by positivity) (Real.exp_ne_zero τ),
      Real.log_mul (by positivity) (Real.exp_ne_zero 1),
      Real.log_exp, Real.log_exp]
    ring
  have h3 : (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), (Nhat s / s - R * s⁻¹))
      = Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 - R * (τ - 1) := by
    have hsub : (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
        (Nhat s / s - R * s⁻¹))
        = (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), Nhat s / s)
          - ∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), R * s⁻¹ :=
      integral_sub hIa hIb
    have hfirst : (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), Nhat s / s)
        = Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 := by
      rw [← intervalIntegral.integral_of_le hle]
      exact lemma3_rvM_integral hτ
    have hsecond : (∫ s in Ioc (2 * π * Real.exp 1) (2 * π * Real.exp τ), R * s⁻¹)
        = R * (τ - 1) := by
      rw [← intervalIntegral.integral_of_le hle, intervalIntegral.integral_const_mul,
        integral_inv h0uIcc, hlogratio]
    rw [hsub, hfirst, hsecond]
  linarith [hsplit, h1, h2, h3]

/-! ### Lemma L6 (circle bound)

If `‖G‖` obeys the L1 growth bound `‖G z‖ ≤ √(2a)·e^{a·|Im z|}` and `G` has
no zeros on the circle `|z| = ρ` (supplied by the L5 radius selection), then
the circle average of `log ‖G ·‖` at radius `ρ` is at most
`½ln(2a) + (2/π)aρ`, hence at most `½ln(2a) + 4a·e^τ + (4 + 2/π)a` once
`ρ ≤ 2πe^τ + 2π + 1`. -/

/-- `∫₀^π |sin| = 2`. -/
lemma integral_abs_sin_zero_pi : ∫ θ in (0 : ℝ)..π, |Real.sin θ| = 2 := by
  have hcongr : EqOn (fun θ : ℝ => |Real.sin θ|) Real.sin (uIcc 0 π) := by
    intro θ hθ
    rw [uIcc_of_le pi_nonneg] at hθ
    exact abs_of_nonneg (Real.sin_nonneg_of_nonneg_of_le_pi hθ.1 hθ.2)
  rw [intervalIntegral.integral_congr hcongr, integral_sin, Real.cos_pi, Real.cos_zero]
  norm_num

/-- `∫_π^{2π} |sin| = 2` (shift the previous lemma by `π`). -/
lemma integral_abs_sin_pi_two_pi : ∫ θ in π..(2 * π), |Real.sin θ| = 2 := by
  have hshift := intervalIntegral.integral_comp_add_right (a := (0 : ℝ)) (b := π)
    (f := fun x => |Real.sin x|) π
  have heq : (fun x : ℝ => |Real.sin (x + π)|) = fun x : ℝ => |Real.sin x| := by
    funext x
    rw [Real.sin_add_pi, abs_neg]
  rw [heq, integral_abs_sin_zero_pi, zero_add, show π + π = 2 * π by ring] at hshift
  exact hshift.symm

/-- `∫₀^{2π} |sin| = 4`. -/
lemma integral_abs_sin_zero_two_pi : ∫ θ in (0 : ℝ)..(2 * π), |Real.sin θ| = 4 := by
  have hint1 : IntervalIntegrable (fun θ : ℝ => |Real.sin θ|) volume 0 π := by
    apply Continuous.intervalIntegrable
    fun_prop
  have hint2 : IntervalIntegrable (fun θ : ℝ => |Real.sin θ|) volume π (2 * π) := by
    apply Continuous.intervalIntegrable
    fun_prop
  rw [← intervalIntegral.integral_add_adjacent_intervals hint1 hint2,
    integral_abs_sin_zero_pi, integral_abs_sin_pi_two_pi]
  norm_num

/-- **Lemma L6** (T1PRIME.md, eq. (L6.1), first inequality): the circle bound
`(1/2π)∫₀^{2π} ln|G(ρe^{iθ})| dθ ≤ ½ln(2a) + (2/π)aρ`. -/
theorem lemma6_circle_bound {G : ℂ → ℂ} {a ρ : ℝ} (ha : 0 < a) (hρ : 0 ≤ ρ)
    (hint : CircleIntegrable (fun z => Real.log ‖G z‖) 0 ρ)
    (hne : ∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, G z ≠ 0)
    (hgrowth : ∀ z : ℂ, ‖G z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :
    circleAverage (fun z => Real.log ‖G z‖) 0 ρ
      ≤ 1 / 2 * Real.log (2 * a) + 2 / π * (a * ρ) := by
  have hπ : (0 : ℝ) < π := pi_pos
  set M : ℂ → ℝ := fun z => 1 / 2 * Real.log (2 * a) + a * |z.im| with hM
  have hMint : CircleIntegrable M 0 ρ := by
    rw [circleIntegrable_def]
    apply Continuous.intervalIntegrable
    simp only [hM]
    exact continuous_const.add
      (((Complex.continuous_im.comp (continuous_circleMap 0 ρ)).abs).const_mul a)
  have hpt : ∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, Real.log ‖G z‖ ≤ M z := by
    intro z hz
    have hz0 : 0 < ‖G z‖ := norm_pos_iff.mpr (hne z hz)
    calc Real.log ‖G z‖
        ≤ Real.log (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :=
          Real.log_le_log hz0 (hgrowth z)
      _ = Real.log (Real.sqrt (2 * a)) + a * |z.im| := by
          rw [Real.log_mul (by positivity) (Real.exp_ne_zero _), Real.log_exp]
      _ = M z := by
          simp only [hM]
          rw [Real.log_sqrt (by positivity : (0 : ℝ) ≤ 2 * a)]
          ring
  have hmono := circleAverage_mono hint hMint hpt
  have haux : (fun θ : ℝ => M (circleMap 0 ρ θ))
      = fun θ : ℝ => 1 / 2 * Real.log (2 * a) + a * ρ * |Real.sin θ| := by
    funext θ
    simp only [hM, circleMap_zero_im]
    rw [abs_mul, abs_of_nonneg hρ]
    ring
  have hi1 : IntervalIntegrable (fun _ : ℝ => 1 / 2 * Real.log (2 * a)) volume 0 (2 * π) :=
    intervalIntegrable_const
  have hi2 : IntervalIntegrable (fun θ : ℝ => a * ρ * |Real.sin θ|) volume 0 (2 * π) := by
    apply Continuous.intervalIntegrable
    fun_prop
  have hval : (∫ θ in (0 : ℝ)..(2 * π),
        (1 / 2 * Real.log (2 * a) + a * ρ * |Real.sin θ|))
      = 2 * π * (1 / 2 * Real.log (2 * a)) + a * ρ * 4 := by
    rw [intervalIntegral.integral_add hi1 hi2, intervalIntegral.integral_const,
      intervalIntegral.integral_const_mul, integral_abs_sin_zero_two_pi, smul_eq_mul]
    ring
  have havg : circleAverage M 0 ρ = 1 / 2 * Real.log (2 * a) + 2 / π * (a * ρ) := by
    rw [circleAverage_def, haux, hval, smul_eq_mul]
    field_simp
    ring
  linarith [hmono, havg.le, havg.ge]

/-- Lemma L6, final form (T1PRIME.md eq. (L6.1), second inequality): with the
Jensen radius `ρ ≤ T̃ + 2π + 1 = 2πe^τ + 2π + 1`, the circle average is at
most `½ln(2a) + 4a·e^τ + (4 + 2/π)a`. -/
theorem lemma6_circle_bound_tau {G : ℂ → ℂ} {a ρ τ : ℝ} (ha : 0 < a) (hρ : 0 ≤ ρ)
    (hρle : ρ ≤ 2 * π * Real.exp τ + 2 * π + 1)
    (hint : CircleIntegrable (fun z => Real.log ‖G z‖) 0 ρ)
    (hne : ∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, G z ≠ 0)
    (hgrowth : ∀ z : ℂ, ‖G z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :
    circleAverage (fun z => Real.log ‖G z‖) 0 ρ
      ≤ 1 / 2 * Real.log (2 * a) + 4 * a * Real.exp τ + (4 + 2 / π) * a := by
  have hπ : (0 : ℝ) < π := pi_pos
  have h1 := lemma6_circle_bound ha hρ hint hne hgrowth
  have h2 : 2 / π * (a * ρ) ≤ 4 * a * Real.exp τ + (4 + 2 / π) * a := by
    calc 2 / π * (a * ρ)
        ≤ 2 / π * (a * (2 * π * Real.exp τ + 2 * π + 1)) := by
          apply mul_le_mul_of_nonneg_left ?_ (by positivity)
          exact mul_le_mul_of_nonneg_left hρle ha.le
      _ = 4 * a * Real.exp τ + (4 + 2 / π) * a := by
          field_simp
          ring
  linarith

/-! ### Lemma L7, arithmetic core (the pair-product bound)

For a prescribed ordinate pair `±t` (with `t ≤ T̃`) seen from the anchored
center `x₀` (`|x₀| ≤ 2π < t`), the two Jensen masses at any radius
`ρ ≥ T̃ + 2π` together dominate `2·ln(T̃/t)`.  (The divisor-side bookkeeping —
that these masses appear in the Jensen sum with multiplicity `≥ mₖ` — is the
L5/L7 mathlib-divisor rung, next session.) -/

theorem lemma7_pair_product {x₀ t T ρ : ℝ} (hx : |x₀| ≤ 2 * π) (ht : 2 * π < t)
    (htT : t ≤ T) (hρ : T + 2 * π ≤ ρ) :
    2 * Real.log (T / t) ≤ Real.log (ρ / |t - x₀|) + Real.log (ρ / |t + x₀|) := by
  have hπ : (0 : ℝ) < 2 * π := by positivity
  have habs := abs_le.mp hx
  have ht0 : 0 < t := lt_trans hπ ht
  have h1 : 0 < t - x₀ := by linarith [habs.2]
  have h2 : 0 < t + x₀ := by linarith [habs.1]
  have hT0 : 0 < T := lt_of_lt_of_le ht0 htT
  have hρ0 : 0 < ρ := by linarith
  rw [abs_of_pos h1, abs_of_pos h2,
    Real.log_div (ne_of_gt hρ0) (ne_of_gt h1),
    Real.log_div (ne_of_gt hρ0) (ne_of_gt h2),
    Real.log_div (ne_of_gt hT0) (ne_of_gt ht0)]
  have hlogρT : Real.log T ≤ Real.log ρ := Real.log_le_log hT0 (by linarith)
  have hprod : Real.log (t - x₀) + Real.log (t + x₀) ≤ 2 * Real.log t := by
    rw [← Real.log_mul (ne_of_gt h1) (ne_of_gt h2)]
    have hmul : (t - x₀) * (t + x₀) ≤ t * t := by nlinarith [sq_nonneg x₀]
    calc Real.log ((t - x₀) * (t + x₀)) ≤ Real.log (t * t) :=
          Real.log_le_log (mul_pos h1 h2) hmul
      _ = 2 * Real.log t := by
          rw [Real.log_mul (ne_of_gt ht0) (ne_of_gt ht0)]
          ring
  linarith

/-- Lemma L7, last clause: any other zero strictly inside the disk contributes
a nonnegative Jensen mass `ln(ρ/d) ≥ 0` (here `d = |zⱼ|`, `0 < d ≤ ρ`). -/
theorem lemma7_other_mass_nonneg {d ρ : ℝ} (hd : 0 < d) (hdρ : d ≤ ρ) :
    0 ≤ Real.log (ρ / d) :=
  Real.log_nonneg ((one_le_div hd).mpr hdρ)

/-! ### Lemma L8 (monotone crossing) -/

/-- **Lemma L8**, monotonicity half: for `R < e^{2a+2}`, the function
`h(τ) = 2e^τ(τ − 2 − 2a) − 2R(τ−1)` is strictly increasing on `[2a+2, ∞)`. -/
theorem lemma8_strictMonoOn {a R : ℝ} (hR : R < Real.exp (2 * a + 2)) :
    StrictMonoOn (hFn a R) (Ici (2 * a + 2)) := by
  have hcont : ContinuousOn (hFn a R) (Ici (2 * a + 2)) := by
    apply Continuous.continuousOn
    unfold hFn
    fun_prop
  apply strictMonoOn_of_hasDerivWithinAt_pos (convex_Ici _) hcont
    (f' := fun x => 2 * Real.exp x * (x - 1 - 2 * a) - 2 * R)
  · intro x hx
    have hexp : HasDerivAt (fun u : ℝ => 2 * Real.exp u) (2 * Real.exp x) x :=
      (Real.hasDerivAt_exp x).const_mul 2
    have hg : HasDerivAt (fun u : ℝ => u - 2 - 2 * a) 1 x := by
      simpa using ((hasDerivAt_id x).sub_const 2).sub_const (2 * a)
    have hlin : HasDerivAt (fun u : ℝ => 2 * R * (u - 1)) (2 * R) x := by
      have h := ((hasDerivAt_id x).sub_const 1).const_mul (2 * R)
      simpa using h
    have hsum := (hexp.mul hg).sub hlin
    have hval : 2 * Real.exp x * 1 + 2 * Real.exp x * (x - 2 - 2 * a) - 2 * R
        = 2 * Real.exp x * (x - 1 - 2 * a) - 2 * R := by ring
    have hval2 : 2 * Real.exp x * (x - 2 - 2 * a) + 2 * Real.exp x * 1 - 2 * R
        = 2 * Real.exp x * (x - 1 - 2 * a) - 2 * R := by ring
    exact (hval2 ▸ hsum).hasDerivWithinAt
  · intro x hx
    rw [interior_Ici] at hx
    have hx' : 2 * a + 2 < x := hx
    have h1 : Real.exp (2 * a + 2) < Real.exp x := Real.exp_lt_exp.mpr hx'
    have h2 : (0 : ℝ) < Real.exp x := Real.exp_pos x
    nlinarith [mul_pos h2 (show (0 : ℝ) < x - 2 - 2 * a by linarith)]

/-- **Lemma L8**, eq. (L8.1): in the case `ε* > 0`,
`h(2a + 2 + ε*) ≥ B`.  (Requires `0 ≤ R < e^{2a+2}`, i.e. the standing
`R ≤ e^{2a+1}` of (S2) is more than enough.) -/
theorem lemma8_crossing {a R κ : ℝ} (_hR0 : 0 ≤ R) (hR : R < Real.exp (2 * a + 2))
    (hε : 0 < epsStar a R κ) :
    BConst a κ ≤ hFn a R (2 * a + 2 + epsStar a R κ) := by
  set ε := epsStar a R κ with hεdef
  have hden : (0 : ℝ) < 2 * (Real.exp (2 * a + 2) - R) := by linarith
  have hid : 2 * ε * (Real.exp (2 * a + 2) - R) = BConst a κ + 2 * R * (2 * a + 1) := by
    have h : ε * (2 * (Real.exp (2 * a + 2) - R)) = BConst a κ + 2 * R * (2 * a + 1) := by
      rw [hεdef]
      unfold epsStar
      exact div_mul_cancel₀ _ (ne_of_gt hden)
    linear_combination h
  have hexp : Real.exp (2 * a + 2 + ε) = Real.exp (2 * a + 2) * Real.exp ε :=
    Real.exp_add _ _
  have hone : (1 : ℝ) ≤ Real.exp ε := Real.one_le_exp hε.le
  unfold hFn
  rw [hexp]
  nlinarith [mul_nonneg (mul_nonneg (sub_nonneg.mpr hone) hε.le)
    (Real.exp_pos (2 * a + 2)).le]

/-- Theorem 1 endgame (§3 of T1PRIME.md): if `τ ≥ 2a+2` and the Jensen chain
has produced `h(τ) ≤ B`, then `τ ≤ 2a + 2 + ε*` with `ε* = max 0 (epsStar)`.
This is the L8-powered extraction step; the remaining work for Theorem 1 is
to produce the hypothesis `hFn a R τ ≤ BConst a κ` from L4–L7. -/
theorem lemma8_tau_bound {a R κ τ : ℝ} (hR0 : 0 ≤ R) (hR : R < Real.exp (2 * a + 2))
    (hτ : 2 * a + 2 ≤ τ) (hh : hFn a R τ ≤ BConst a κ) :
    τ ≤ 2 * a + 2 + max 0 (epsStar a R κ) := by
  by_contra hcon
  push_neg at hcon
  have hmono := lemma8_strictMonoOn (a := a) hR
  rcases le_or_gt (epsStar a R κ) 0 with hle | hpos
  · -- case ε* ≤ 0: already τ ≤ 2a+2 must hold
    rw [max_eq_left hle, add_zero] at hcon
    have h1 : hFn a R (2 * a + 2) < hFn a R τ :=
      hmono (mem_Ici.mpr le_rfl) (mem_Ici.mpr hτ) hcon
    have h2 : hFn a R (2 * a + 2) = -(2 * R * (2 * a + 1)) := by
      unfold hFn
      ring
    have hden : (0 : ℝ) < 2 * (Real.exp (2 * a + 2) - R) := by linarith
    have hnum : BConst a κ + 2 * R * (2 * a + 1) ≤ 0 := by
      by_contra hn
      push_neg at hn
      have : 0 < epsStar a R κ := div_pos hn hden
      linarith
    linarith
  · -- case ε* > 0: use the crossing bound (L8.1)
    rw [max_eq_right hpos.le] at hcon
    have hcross := lemma8_crossing hR0 hR hpos
    have h1 : hFn a R (2 * a + 2 + epsStar a R κ) < hFn a R τ :=
      hmono (mem_Ici.mpr (by linarith)) (mem_Ici.mpr hτ) hcon
    linarith

/-! ### Lemma L1, scalar core

The growth estimate (L1.1) reduces to `sinh y ≤ y·e^y` (valid for all real
`y`); the entirety/Cauchy–Schwarz packaging is the remaining L1 work. -/

theorem lemma1_sinh_le (y : ℝ) : Real.sinh y ≤ y * Real.exp y := by
  rw [Real.sinh_eq]
  have hexpney : Real.exp (-y) = Real.exp y * Real.exp (-(2 * y)) := by
    rw [← Real.exp_add]
    ring_nf
  nlinarith [Real.add_one_le_exp (-(2 * y)), Real.exp_pos y]

/-! ### Lemma L1, full (entirety and growth of the Fourier–Laplace transform)

`F(z) = ∫_{−a}^{a} φ(x)·e^{−izx} dx` under (S1) (here packaged as: `φ`
integrable on `[−a,a]`, `‖φ‖²` integrable with mass ≤ 1): `F` is entire and
`‖F(z)‖ ≤ √(2a)·e^{a·|Im z|}` — eq. (L1.1), in the exact `hgrowth` input
shape of `lemma6_circle_bound`. -/

/-- The Fourier–Laplace transform `F(z) = ∫_{−a}^{a} φ(x)·e^{−izx} dx` of (S1). -/
noncomputable def FL (φ : ℝ → ℂ) (a : ℝ) (z : ℂ) : ℂ :=
  ∫ x in Icc (-a) a, φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))

lemma FL_exponent_re (z : ℂ) (x : ℝ) : (-(Complex.I * z * (x : ℂ))).re = x * z.im := by
  simp only [Complex.neg_re, Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im,
    Complex.ofReal_re, Complex.ofReal_im]
  ring

lemma FL_integrand_norm (φ : ℝ → ℂ) (z : ℂ) (x : ℝ) :
    ‖φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))‖ = ‖φ x‖ * Real.exp (x * z.im) := by
  rw [norm_mul, Complex.norm_exp, FL_exponent_re]

lemma FL_integrand_integrableOn {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a)) (z : ℂ) :
    IntegrableOn (fun x => φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))) (Icc (-a) a) := by
  apply Integrable.mono' (hφi.norm.mul_const (Real.exp (a * |z.im|)))
  · exact hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · rw [ae_restrict_iff' measurableSet_Icc]
    filter_upwards with x hx
    rw [FL_integrand_norm]
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have hxz : x * z.im ≤ a * |z.im| := by
      calc x * z.im ≤ |x * z.im| := le_abs_self _
        _ = |x| * |z.im| := abs_mul _ _
        _ ≤ a * |z.im| := mul_le_mul_of_nonneg_right hxa (abs_nonneg _)
    exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hxz) (norm_nonneg _)

/-- **Lemma L1**, entirety half: under (S1), `F` is entire. -/
theorem lemma1_entire {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a)) :
    Differentiable ℂ (FL φ a) := by
  intro z₀
  have key := hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (μ := volume.restrict (Icc (-a) a))
    (F := fun (z : ℂ) (x : ℝ) => φ x * Complex.exp (-(Complex.I * z * (x : ℂ))))
    (F' := fun (z : ℂ) (x : ℝ) =>
      φ x * (Complex.exp (-(Complex.I * z * (x : ℂ))) * -(Complex.I * (x : ℂ))))
    (bound := fun x => ‖φ x‖ * (Real.exp (a * (|z₀.im| + 1)) * a))
    (Metric.ball_mem_nhds z₀ one_pos) ?_ ?_ ?_ ?_ ?_ ?_
  · exact key.2.differentiableAt
  · exact Filter.Eventually.of_forall fun z =>
      hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · exact FL_integrand_integrableOn ha hφi z₀
  · exact hφi.aestronglyMeasurable.mul (Continuous.aestronglyMeasurable (by fun_prop))
  · rw [ae_restrict_iff' measurableSet_Icc]
    filter_upwards with x hx
    intro z hz
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have him : |z.im| ≤ |z₀.im| + 1 := by
      have h2 : |(z - z₀).im| ≤ ‖z - z₀‖ := Complex.abs_im_le_norm _
      have h3 : ‖z - z₀‖ ≤ 1 := by
        rw [← dist_eq_norm]
        exact le_of_lt (Metric.mem_ball.mp hz)
      have h4 : z.im = z₀.im + (z - z₀).im := by simp
      rw [h4]
      calc |z₀.im + (z - z₀).im| ≤ |z₀.im| + |(z - z₀).im| := abs_add_le _ _
        _ ≤ |z₀.im| + 1 := by linarith
    have hxz : x * z.im ≤ a * (|z₀.im| + 1) := by
      calc x * z.im ≤ |x * z.im| := le_abs_self _
        _ = |x| * |z.im| := abs_mul _ _
        _ ≤ a * (|z₀.im| + 1) := mul_le_mul hxa him (abs_nonneg _) ha.le
    calc ‖φ x * (Complex.exp (-(Complex.I * z * (x : ℂ))) * -(Complex.I * (x : ℂ)))‖
        = ‖φ x‖ * (Real.exp (x * z.im) * |x|) := by
          rw [norm_mul, norm_mul, Complex.norm_exp, FL_exponent_re, norm_neg, norm_mul,
            Complex.norm_I, one_mul, Complex.norm_real, Real.norm_eq_abs]
      _ ≤ ‖φ x‖ * (Real.exp (a * (|z₀.im| + 1)) * a) := by
          apply mul_le_mul_of_nonneg_left ?_ (norm_nonneg _)
          exact mul_le_mul (Real.exp_le_exp.mpr hxz) hxa (abs_nonneg _) (Real.exp_pos _).le
  · exact hφi.norm.mul_const _
  · apply Filter.Eventually.of_forall
    intro x z _
    have h1 : HasDerivAt (fun w : ℂ => Complex.I * w) Complex.I z := by
      simpa using (hasDerivAt_id z).const_mul Complex.I
    have h2 : HasDerivAt (fun w : ℂ => Complex.I * w * (x : ℂ)) (Complex.I * (x : ℂ)) z :=
      h1.mul_const _
    exact ((h2.neg).cexp).const_mul (φ x)

/-- Translation preserves the analytic order of an entire function.  This
bridges the paper's vanishing-order hypothesis on `F` at `c + z₀` to the
recentered function `z ↦ F (c + z)` used by Jensen's formula below. -/
theorem analyticOrderAt_translate (F : ℂ → ℂ) (hF : Differentiable ℂ F) (c z₀ : ℂ) :
    analyticOrderAt (fun z => F (c + z)) z₀ = analyticOrderAt F (c + z₀) := by
  have hf : AnalyticAt ℂ F (c + z₀) := hF.analyticAt (c + z₀)
  have hg : AnalyticAt ℂ (fun z : ℂ => c + z) z₀ := by fun_prop
  have hderiv : deriv (fun z : ℂ => c + z) z₀ = 1 := by
    simpa only [id_eq] using ((hasDerivAt_id z₀).const_add c).deriv
  have hgderiv : deriv (fun z : ℂ => c + z) z₀ ≠ 0 := by
    rw [hderiv]
    exact one_ne_zero
  have horder : analyticOrderAt ((fun z : ℂ => c + z) · - (c + z₀)) z₀ = 1 :=
    hg.analyticOrderAt_sub_eq_one_of_deriv_ne_zero hgderiv
  rw [show (fun z => F (c + z)) = F ∘ (fun z => c + z) by rfl,
    hf.analyticOrderAt_comp hg, horder, mul_one]

/-- **Lemma L1**, growth half (eq. (L1.1)): `‖F(z)‖ ≤ √(2a)·e^{a·|Im z|}`. -/
theorem lemma1_growth {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1) (z : ℂ) :
    ‖FL φ a z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
  have hg2 : IntegrableOn (fun x : ℝ => Real.exp (x * z.im) ^ 2) (Icc (-a) a) :=
    ((by fun_prop : Continuous fun x : ℝ => Real.exp (x * z.im) ^ 2).continuousOn).integrableOn_Icc
  -- Step 1: pull the norm inside
  have h1 : ‖FL φ a z‖ ≤ ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := by
    calc ‖FL φ a z‖
        ≤ ∫ x in Icc (-a) a, ‖φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))‖ :=
          norm_integral_le_integral_norm _
      _ = ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := by
          apply setIntegral_congr_fun measurableSet_Icc
          intro x _
          show ‖φ x * Complex.exp (-(Complex.I * z * (x : ℂ)))‖ = ‖φ x‖ * Real.exp (x * z.im)
          exact FL_integrand_norm φ z x
  -- Step 2: Cauchy–Schwarz
  have hfLp : MemLp (fun x => ‖φ x‖) (ENNReal.ofReal 2) (volume.restrict (Icc (-a) a)) := by
    rw [ENNReal.ofReal_ofNat]
    exact (memLp_two_iff_integrable_sq hφi.aestronglyMeasurable.norm).mpr hsq
  have hgLp : MemLp (fun x : ℝ => Real.exp (x * z.im)) (ENNReal.ofReal 2)
      (volume.restrict (Icc (-a) a)) := by
    rw [ENNReal.ofReal_ofNat]
    exact (memLp_two_iff_integrable_sq
      (Continuous.aestronglyMeasurable (by fun_prop))).mpr hg2
  have hCS := integral_mul_le_Lp_mul_Lq_of_nonneg Real.HolderConjugate.two_two
    (Filter.Eventually.of_forall fun x => norm_nonneg (φ x))
    (Filter.Eventually.of_forall fun x => (Real.exp_pos (x * z.im)).le) hfLp hgLp
  -- Step 3: the φ factor is ≤ 1
  have hf_fac : (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) ≤ 1 := by
    have hconv : (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) = ∫ x in Icc (-a) a, ‖φ x‖ ^ 2 :=
      setIntegral_congr_fun measurableSet_Icc fun x _ => Real.rpow_two _
    rw [hconv, ← Real.sqrt_eq_rpow]
    calc Real.sqrt (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ Real.sqrt 1 := Real.sqrt_le_sqrt hφ2
      _ = 1 := Real.sqrt_one
  -- Step 4: the exponential factor is ≤ √(2a)·e^{a|Im z|}
  have hpt : ∀ x ∈ Icc (-a) a, Real.exp (x * z.im) ^ 2 ≤ Real.exp (2 * a * |z.im|) := by
    intro x hx
    have hxa : |x| ≤ a := abs_le.mpr ⟨hx.1, hx.2⟩
    have h2 : Real.exp (x * z.im) ^ 2 = Real.exp (2 * (x * z.im)) := by
      rw [sq, ← Real.exp_add]
      ring_nf
    rw [h2]
    apply Real.exp_le_exp.mpr
    calc 2 * (x * z.im) ≤ 2 * |x * z.im| := by linarith [le_abs_self (x * z.im)]
      _ = 2 * (|x| * |z.im|) := by rw [abs_mul]
      _ ≤ 2 * (a * |z.im|) := by
          have := mul_le_mul_of_nonneg_right hxa (abs_nonneg z.im)
          linarith
      _ = 2 * a * |z.im| := by ring
  have hgbd : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
      ≤ 2 * a * Real.exp (2 * a * |z.im|) := by
    calc (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
        ≤ ∫ _x in Icc (-a) a, Real.exp (2 * a * |z.im|) :=
          setIntegral_mono_on hg2 (integrableOn_const measure_Icc_lt_top.ne)
            measurableSet_Icc hpt
      _ = 2 * a * Real.exp (2 * a * |z.im|) := by
          rw [setIntegral_const, smul_eq_mul, Measure.real, Real.volume_Icc,
            ENNReal.toReal_ofReal (by linarith : (0 : ℝ) ≤ a - -a)]
          ring
  have hg_fac : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ))
      ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
    have hconv : (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ))
        = ∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2 :=
      setIntegral_congr_fun measurableSet_Icc fun x _ => Real.rpow_two _
    rw [hconv, ← Real.sqrt_eq_rpow]
    calc Real.sqrt (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ 2)
        ≤ Real.sqrt (2 * a * Real.exp (2 * a * |z.im|)) := Real.sqrt_le_sqrt hgbd
      _ = Real.sqrt (2 * a) * Real.sqrt (Real.exp (2 * a * |z.im|)) :=
          Real.sqrt_mul (by positivity) _
      _ = Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
          congr 1
          have h : Real.exp (2 * a * |z.im|) = Real.exp (a * |z.im|) ^ 2 := by
            rw [sq, ← Real.exp_add]
            congr 1
            ring
          rw [h, Real.sqrt_sq (Real.exp_pos _).le]
  -- Combine
  have hg_nonneg : (0 : ℝ) ≤ (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) :=
    Real.rpow_nonneg
      (setIntegral_nonneg measurableSet_Icc fun x _ => Real.rpow_nonneg (Real.exp_pos _).le _) _
  calc ‖FL φ a z‖ ≤ ∫ x in Icc (-a) a, ‖φ x‖ * Real.exp (x * z.im) := h1
    _ ≤ (∫ x in Icc (-a) a, ‖φ x‖ ^ (2 : ℝ)) ^ (1 / (2 : ℝ))
        * (∫ x in Icc (-a) a, Real.exp (x * z.im) ^ (2 : ℝ)) ^ (1 / (2 : ℝ)) := hCS
    _ ≤ 1 * (Real.sqrt (2 * a) * Real.exp (a * |z.im|)) :=
        mul_le_mul hf_fac hg_fac hg_nonneg zero_le_one
    _ = Real.sqrt (2 * a) * Real.exp (a * |z.im|) := one_mul _

/-- Lemma L1 growth, recentered form: for real `x₀` the function
`G(z) = F(x₀ + z)` obeys the same bound with `|Im z|` — the exact `hgrowth`
hypothesis of `lemma6_circle_bound`. -/
theorem lemma1_growth_recentered {φ : ℝ → ℂ} {a : ℝ} (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1) (x₀ : ℝ) (z : ℂ) :
    ‖FL φ a ((x₀ : ℂ) + z)‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) := by
  have h := lemma1_growth ha hφi hsq hφ2 ((x₀ : ℂ) + z)
  simpa using h

/-! ### Lemma L5 (radius selection and Jensen's formula)

An entire `G` with `G 0 ≠ 0` has finitely many zeros in any closed ball, so
a radius `ρ ∈ [T + 2π, T + 2π + 1]` avoiding all zero-moduli exists; at such
a radius mathlib's Jensen formula applies.  NOTE (session-1 finding): the
no-zeros-on-circle property is required by `lemma6_circle_bound` (mathlib's
`Real.log 0 = 0` junk value), so the selection is *not* optional. -/

/-- An entire function that is nonzero somewhere has finite analytic order
everywhere (identity theorem). -/
lemma analyticOrderAt_ne_top_of_ne {G : ℂ → ℂ} (hG : Differentiable ℂ G)
    (hG0 : G 0 ≠ 0) (u : ℂ) : analyticOrderAt G u ≠ ⊤ := by
  intro htop
  have hana : AnalyticOnNhd ℂ G univ := Complex.analyticOnNhd_univ_iff_differentiable.mpr hG
  have hev : G =ᶠ[nhds u] 0 := analyticOrderAt_eq_top.mp htop
  have heq := hana.eqOn_zero_of_preconnected_of_eventuallyEq_zero
    isPreconnected_univ (mem_univ u) hev
  exact hG0 (heq (mem_univ 0))

/-- Prescribed vanishing order forces a divisor lower bound. -/
lemma le_divisor_of_le_analyticOrderAt {G : ℂ → ℂ} {S : Set ℂ}
    (hana : AnalyticOnNhd ℂ G S) (hne : ∀ u, analyticOrderAt G u ≠ ⊤)
    {u : ℂ} (hu : u ∈ S) {m : ℕ} (hm : (m : ℕ∞) ≤ analyticOrderAt G u) :
    (m : ℤ) ≤ MeromorphicOn.divisor G S u := by
  obtain ⟨n, hn⟩ : ∃ n : ℕ, analyticOrderAt G u = (n : ℕ∞) := by
    cases h : analyticOrderAt G u using WithTop.recTopCoe with
    | top => exact absurd h (hne u)
    | coe n => exact ⟨n, rfl⟩
  rw [hn] at hm
  have hmn : m ≤ n := by exact_mod_cast hm
  rw [hana.divisor_apply hu, hn, ENat.map_coe, WithTop.untop₀_coe]
  exact_mod_cast hmn

/-- **Lemma L5**, selection half: a radius in `[c, d]` whose circle carries no
zeros of `G` exists. -/
lemma lemma5_radius_selection {G : ℂ → ℂ} (hG : Differentiable ℂ G) (hG0 : G 0 ≠ 0)
    {c d : ℝ} (hcd : c < d) (hc : 0 ≤ c) :
    ∃ ρ ∈ Icc c d, ∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, G z ≠ 0 := by
  have hana : AnalyticOnNhd ℂ G (Metric.closedBall (0 : ℂ) d) :=
    (Complex.analyticOnNhd_univ_iff_differentiable.mpr hG).mono (subset_univ _)
  have hfin : ((MeromorphicOn.divisor G (Metric.closedBall (0 : ℂ) d)).support).Finite :=
    (MeromorphicOn.divisor G _).finiteSupport (isCompact_closedBall _ _)
  have hzsub : {z : ℂ | z ∈ Metric.closedBall (0 : ℂ) d ∧ G z = 0}
      ⊆ (MeromorphicOn.divisor G (Metric.closedBall (0 : ℂ) d)).support := by
    rintro z ⟨hzd, hz0⟩
    rw [Function.mem_support]
    have h1 : (1 : ℤ) ≤ MeromorphicOn.divisor G (Metric.closedBall (0 : ℂ) d) z := by
      apply le_divisor_of_le_analyticOrderAt hana (analyticOrderAt_ne_top_of_ne hG hG0) hzd
      rw [Nat.cast_one, Order.one_le_iff_ne_zero]
      exact (hana z hzd).analyticOrderAt_ne_zero.mpr hz0
    intro h
    rw [h] at h1
    omega
  have hzfin : ({z : ℂ | z ∈ Metric.closedBall (0 : ℂ) d ∧ G z = 0}).Finite :=
    hfin.subset hzsub
  have hnorms : ((fun z : ℂ => ‖z‖) '' {z | z ∈ Metric.closedBall (0 : ℂ) d ∧ G z = 0}).Finite :=
    hzfin.image _
  obtain ⟨ρ, hρmem, hρnot⟩ := (Set.Icc_infinite hcd).exists_notMem_finite hnorms
  refine ⟨ρ, hρmem, ?_⟩
  intro z hz hGz
  apply hρnot
  have hρ0 : 0 ≤ ρ := le_trans hc hρmem.1
  have hznorm : ‖z‖ = ρ := by
    rw [mem_sphere_zero_iff_norm] at hz
    rw [hz, abs_of_nonneg hρ0]
  exact ⟨z, ⟨mem_closedBall_zero_iff.mpr (by rw [hznorm]; exact hρmem.2), hGz⟩, hznorm⟩

/-- **Lemma L5** (T1PRIME.md, eq. (L5.1)): radius selection in
`[T + 2π, T + 2π + 1]` plus Jensen's formula at the selected radius. -/
theorem lemma5_jensen {G : ℂ → ℂ} (hG : Differentiable ℂ G) (hG0 : G 0 ≠ 0)
    {T : ℝ} (hT : 0 ≤ T) :
    ∃ ρ ∈ Icc (T + 2 * π) (T + 2 * π + 1),
      (∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, G z ≠ 0) ∧
      circleAverage (fun z => Real.log ‖G z‖) 0 ρ
        = (∑ᶠ u, (MeromorphicOn.divisor G (Metric.closedBall 0 |ρ|) u : ℝ)
            * Real.log (ρ * ‖u‖⁻¹)) + Real.log ‖G 0‖ := by
  have hπ : (0 : ℝ) < π := pi_pos
  obtain ⟨ρ, hρmem, hρsphere⟩ := lemma5_radius_selection hG hG0
    (lt_add_one (T + 2 * π)) (by positivity)
  have hρpos : 0 < ρ := lt_of_lt_of_le (by positivity) hρmem.1
  refine ⟨ρ, hρmem, hρsphere, ?_⟩
  have hana : AnalyticOnNhd ℂ G (Metric.closedBall (0 : ℂ) |ρ|) :=
    (Complex.analyticOnNhd_univ_iff_differentiable.mpr hG).mono (subset_univ _)
  rw [hana.circleAverage_log_norm (ne_of_gt hρpos) hG0]
  congr 1
  apply finsum_congr
  intro u
  rw [zero_sub, norm_neg]

/-! ### Lemma L7, divisor side

The Jensen divisor sum dominates the prescribed masses: if `G` vanishes to
order `≥ m u` at each point `u` of a finite prescribed set `P` inside the
closed disk, then `Σ_{u∈P} m(u)·ln(ρ/|u|) ≤ Σᶠ_u div(u)·ln(ρ/|u|)`. -/

theorem lemma7_divisor_lower {G : ℂ → ℂ} {ρ : ℝ} (hρ : 0 < ρ)
    (hG : Differentiable ℂ G) (hG0 : G 0 ≠ 0)
    (P : Finset ℂ) (m : ℂ → ℕ)
    (hPball : ∀ u ∈ P, u ∈ Metric.closedBall (0 : ℂ) |ρ|)
    (hPord : ∀ u ∈ P, (m u : ℕ∞) ≤ analyticOrderAt G u) :
    ∑ u ∈ P, (m u : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      ≤ ∑ᶠ u, (MeromorphicOn.divisor G (Metric.closedBall 0 |ρ|) u : ℝ)
          * Real.log (ρ * ‖u‖⁻¹) := by
  classical
  have hana : AnalyticOnNhd ℂ G (Metric.closedBall (0 : ℂ) |ρ|) :=
    (Complex.analyticOnNhd_univ_iff_differentiable.mpr hG).mono (subset_univ _)
  set D := MeromorphicOn.divisor G (Metric.closedBall (0 : ℂ) |ρ|) with hDdef
  have hfin : (D.support).Finite := D.finiteSupport (isCompact_closedBall _ _)
  -- log(ρ/|u|) ≥ 0 anywhere in the closed disk
  have hlog : ∀ u : ℂ, u ∈ Metric.closedBall (0 : ℂ) |ρ| → 0 ≤ Real.log (ρ * ‖u‖⁻¹) := by
    intro u hu
    rcases eq_or_ne u 0 with h0 | h0
    · simp [h0]
    · have hn0 : 0 < ‖u‖ := norm_pos_iff.mpr h0
      have hle : ‖u‖ ≤ ρ := by
        have h := mem_closedBall_zero_iff.mp hu
        rwa [abs_of_pos hρ] at h
      apply Real.log_nonneg
      rw [← div_eq_mul_inv]
      exact (one_le_div hn0).mpr hle
  -- express the finsum as a sum over a finite superset of the support
  set s : Finset ℂ := hfin.toFinset ∪ P with hs
  have hsub : (Function.support fun u => (D u : ℝ) * Real.log (ρ * ‖u‖⁻¹)) ⊆ ↑s := by
    intro u hu
    rw [Function.mem_support] at hu
    have hDu : D u ≠ 0 := by
      intro h
      apply hu
      rw [h]
      simp
    exact Finset.mem_coe.mpr (Finset.mem_union_left _ (hfin.mem_toFinset.mpr hDu))
  rw [finsum_eq_sum_of_support_subset _ hsub]
  have hterm_nonneg : ∀ u ∈ s, 0 ≤ (D u : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
    intro u hu
    apply mul_nonneg
    · exact_mod_cast hana.divisor_nonneg u
    · rcases Finset.mem_union.mp hu with h | h
      · exact hlog u (D.supportWithinDomain (hfin.mem_toFinset.mp h))
      · exact hlog u (hPball u h)
  calc ∑ u ∈ P, (m u : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      ≤ ∑ u ∈ P, (D u : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
        apply Finset.sum_le_sum
        intro u hu
        apply mul_le_mul_of_nonneg_right ?_ (hlog u (hPball u hu))
        exact_mod_cast le_divisor_of_le_analyticOrderAt hana
          (analyticOrderAt_ne_top_of_ne hG hG0) (hPball u hu) (hPord u hu)
    _ ≤ ∑ u ∈ s, (D u : ℝ) * Real.log (ρ * ‖u‖⁻¹) :=
        Finset.sum_le_sum_of_subset_of_nonneg Finset.subset_union_right
          (fun u hu _ => hterm_nonneg u hu)

/-! ### The shared Jensen chain (core of Theorem 1 and of the anchor collapse)

T1PRIME.md §3, stopped one step before the L8 extraction: under (S1), the
ordinate-head hypotheses, (S2)-rigidity and (S3)-vanishing — but NO anchor
hypothesis, only `F(x₀) ≠ 0` — the chain L4 → L2 → L7 → L5 → L6 yields
`h(τ) ≤ B₀ − ln‖F(x₀)‖`, where `B₀ = BConst a 0` is the κ-free anchor
constant.  Theorem 1 (`hard_horizon`) follows by feeding in Hypothesis A and
extracting with L8; the annihilating-pair form (`anchor_collapse`, QC-2)
follows by rearranging.  Note: neither `0 ≤ R` nor `R < e^{2a+2}` is needed
here, and `1 ≤ τ` suffices (not `2a + 2 ≤ τ`). -/

theorem log_anchor_bound {φ : ℝ → ℂ} {a x₀ R τ : ℝ} {α : Type*} (ι : Finset α) (t : α → ℝ)
    (ha : 0 < a)
    -- (S1)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    -- the ordinate head below the horizon 2πe^τ
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    -- (S2)
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    -- (S3), recentered vanishing orders
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - (x₀ : ℂ)))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - (x₀ : ℂ)))
    -- low-band position and nonvanishing there (all that survives of Hyp. A)
    (hx₀ : |x₀| ≤ 2 * π)
    (hz : FL φ a ((x₀ : ℂ)) ≠ 0)
    (hτ1 : 1 ≤ τ) :
    hFn a R τ ≤ BConst a 0 - Real.log ‖FL φ a ((x₀ : ℂ))‖ := by
  have hπ : (0 : ℝ) < π := pi_pos
  have htpos : ∀ k ∈ ι, 0 < t k :=
    fun k hk => lt_trans (by positivity) (ht k hk)
  -- the recentered transform
  set G : ℂ → ℂ := fun z => FL φ a ((x₀ : ℂ) + z) with hGdef
  have hGdiff : Differentiable ℂ G :=
    (lemma1_entire ha hφi).comp ((differentiable_const _).add differentiable_id)
  have hG0 : G 0 ≠ 0 := by
    simp only [hGdef]
    simpa using hz
  -- L5: radius selection + Jensen
  obtain ⟨ρ, hρmem, hρsphere, hjensen⟩ :=
    lemma5_jensen hGdiff hG0 (T := 2 * π * Real.exp τ) (by positivity)
  have hρT : 2 * π * Real.exp τ + 2 * π ≤ ρ := hρmem.1
  have hρpos : (0 : ℝ) < ρ := lt_of_lt_of_le (by positivity) hρmem.1
  -- L6: circle bound at the selected radius
  have hint6 : CircleIntegrable (fun z => Real.log ‖G z‖) 0 ρ :=
    MeromorphicOn.circleIntegrable_log_norm
      (((Complex.analyticOnNhd_univ_iff_differentiable.mpr hGdiff).mono
        (subset_univ _)).meromorphicOn)
  have hgrowth : ∀ z : ℂ, ‖G z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) :=
    fun z => lemma1_growth_recentered ha hφi hsq hφ2 x₀ z
  have h6 := lemma6_circle_bound_tau ha hρpos.le hρmem.2 hint6 hρsphere hgrowth
  -- the prescribed points, recentered
  set pp : α → ℂ := fun k => ((t k : ℂ)) - (x₀ : ℂ) with hppdef
  set pm : α → ℂ := fun k => -((t k : ℂ)) - (x₀ : ℂ) with hpmdef
  set P : Finset ℂ := ι.image pp ∪ ι.image pm with hPdef
  set m : ℂ → ℕ := fun u =>
    (ι.filter fun k => pp k = u).card + (ι.filter fun k => pm k = u).card with hmdef
  -- norms of prescribed points
  have hnorm_pp : ∀ k ∈ ι, ‖pp k‖ = |t k - x₀| := by
    intro k hk
    simp only [hppdef]
    rw [show ((t k : ℂ)) - (x₀ : ℂ) = (((t k - x₀ : ℝ)) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs]
  have hnorm_pm : ∀ k ∈ ι, ‖pm k‖ = |t k + x₀| := by
    intro k hk
    simp only [hpmdef]
    rw [show -((t k : ℂ)) - (x₀ : ℂ) = (((-(t k + x₀) : ℝ)) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs, abs_neg]
  -- prescribed distances stay inside the Jensen disk
  have habs_pp : ∀ k ∈ ι, |t k - x₀| ≤ 2 * π * Real.exp τ + 2 * π := by
    intro k hk
    have h1 := abs_le.mp hx₀
    have h2 := ht k hk
    have h3 := htT k hk
    rw [abs_le]
    constructor <;> nlinarith [Real.exp_pos τ]
  have habs_pm : ∀ k ∈ ι, |t k + x₀| ≤ 2 * π * Real.exp τ + 2 * π := by
    intro k hk
    have h1 := abs_le.mp hx₀
    have h2 := ht k hk
    have h3 := htT k hk
    rw [abs_le]
    constructor <;> nlinarith [Real.exp_pos τ]
  have hPball : ∀ u ∈ P, u ∈ Metric.closedBall (0 : ℂ) |ρ| := by
    intro u hu
    rw [mem_closedBall_zero_iff, abs_of_pos hρpos]
    rcases Finset.mem_union.mp hu with h | h
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      rw [hnorm_pp k hk]
      linarith [habs_pp k hk]
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      rw [hnorm_pm k hk]
      linarith [habs_pm k hk]
  -- fibers of the point maps are the ordinate fibers
  have hfiber_pp : ∀ k ∈ ι, (ι.filter fun j => pp j = pp k) = ι.filter fun j => t j = t k := by
    intro k _
    apply Finset.filter_congr
    intro j _
    simp only [hppdef]
    constructor
    · intro he
      exact_mod_cast sub_left_inj.mp he
    · intro he
      rw [he]
  have hfiber_pm : ∀ k ∈ ι, (ι.filter fun j => pm j = pm k) = ι.filter fun j => t j = t k := by
    intro k _
    apply Finset.filter_congr
    intro j _
    simp only [hpmdef]
    constructor
    · intro he
      have h2 : -((t j : ℝ) : ℂ) = -((t k : ℝ) : ℂ) := sub_left_inj.mp he
      exact_mod_cast neg_inj.mp h2
    · intro he
      rw [he]
  have hcross_mp : ∀ k ∈ ι, (ι.filter fun j => pm j = pp k) = ∅ := by
    intro k hk
    rw [Finset.filter_eq_empty_iff]
    intro j hj he
    simp only [hppdef, hpmdef] at he
    have h2 : -((t j : ℝ) : ℂ) = ((t k : ℝ) : ℂ) := sub_left_inj.mp he
    have h3 : -(t j) = t k := by exact_mod_cast h2
    have h4 := ht j hj
    have h5 := ht k hk
    linarith
  have hcross_pm : ∀ k ∈ ι, (ι.filter fun j => pp j = pm k) = ∅ := by
    intro k hk
    rw [Finset.filter_eq_empty_iff]
    intro j hj he
    simp only [hppdef, hpmdef] at he
    have h2 : ((t j : ℝ) : ℂ) = -((t k : ℝ) : ℂ) := sub_left_inj.mp he
    have h3 : t j = -(t k) := by exact_mod_cast h2
    have h4 := ht j hj
    have h5 := ht k hk
    linarith
  -- prescribed multiplicities are dominated by the vanishing orders
  have hPord : ∀ u ∈ P, (m u : ℕ∞) ≤ analyticOrderAt G u := by
    intro u hu
    rcases Finset.mem_union.mp hu with h | h
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      have hm_eq : m (pp k) = (ι.filter fun j => t j = t k).card := by
        simp only [hmdef]
        rw [hfiber_pp k hk, hcross_mp k hk]
        simp
      rw [hm_eq]
      exact hordp k hk
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      have hm_eq : m (pm k) = (ι.filter fun j => t j = t k).card := by
        simp only [hmdef]
        rw [hfiber_pm k hk, hcross_pm k hk]
        simp
      rw [hm_eq]
      exact hordm k hk
  -- L7, divisor side
  have h7 := lemma7_divisor_lower hρpos hGdiff hG0 P m hPball hPord
  -- the prescribed Jensen mass splits into the two ordinate families
  have e_pp : ∑ u ∈ P, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = ∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹) := by
    have h1 : ∑ u ∈ ι.image pp, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
        = ∑ u ∈ P, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
      apply Finset.sum_subset Finset.subset_union_left
      intro u _ hnot
      have hempty : (ι.filter fun k => pp k = u) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        intro k hk he
        exact hnot (Finset.mem_image.mpr ⟨k, hk, he⟩)
      rw [hempty]
      simp
    have h2 : ∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)
        = ∑ u ∈ ι.image pp, (ι.filter fun k => pp k = u).card • Real.log (ρ * ‖u‖⁻¹) :=
      Finset.sum_comp (fun u : ℂ => Real.log (ρ * ‖u‖⁻¹)) pp
    rw [← h1, h2]
    apply Finset.sum_congr rfl
    intro u _
    rw [nsmul_eq_mul]
  have e_pm : ∑ u ∈ P, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    have h1 : ∑ u ∈ ι.image pm, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
        = ∑ u ∈ P, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
      apply Finset.sum_subset Finset.subset_union_right
      intro u _ hnot
      have hempty : (ι.filter fun k => pm k = u) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        intro k hk he
        exact hnot (Finset.mem_image.mpr ⟨k, hk, he⟩)
      rw [hempty]
      simp
    have h2 : ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹)
        = ∑ u ∈ ι.image pm, (ι.filter fun k => pm k = u).card • Real.log (ρ * ‖u‖⁻¹) :=
      Finset.sum_comp (fun u : ℂ => Real.log (ρ * ‖u‖⁻¹)) pm
    rw [← h1, h2]
    apply Finset.sum_congr rfl
    intro u _
    rw [nsmul_eq_mul]
  have hsplit : ∑ u ∈ P, (m u : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = (∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)) + ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    rw [← e_pp, ← e_pm, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro u _
    simp only [hmdef]
    push_cast
    ring
  -- L7, pair-product side: each ordinate pair pays ≥ 2·ln(T̃/tₖ)
  have hpair : ∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp τ / t k)
      ≤ (∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)) + ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro k hk
    rw [hnorm_pp k hk, hnorm_pm k hk, ← div_eq_mul_inv, ← div_eq_mul_inv]
    exact lemma7_pair_product hx₀ (ht k hk) (htT k hk) hρT
  -- L2 + L4: the counting-function lower bound
  set I : ℝ := ∫ s in Ioc (0 : ℝ) (2 * π * Real.exp τ),
    ((ι.filter fun k => t k ≤ s).card : ℝ) / s with hIdef
  have hcount : ∑ k ∈ ι, Real.log (2 * π * Real.exp τ / t k) = I := by
    rw [hIdef]
    exact lemma2_sum_log_eq_integral ι t htpos htT
  have h4 : Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 - R * (τ - 1) ≤ I := by
    rw [hIdef]
    exact lemma4_rigidity_transfer hτ1 (lemma2_integrableOn ι t htpos)
      (fun s _ => Nat.cast_nonneg _) hrig
  have hdouble : ∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp τ / t k) = 2 * I := by
    rw [← hcount, Finset.mul_sum]
  -- final chain, stopped at the log form
  have hg0eq : G 0 = FL φ a ((x₀ : ℂ)) := by
    simp [hGdef]
  have hlogeq : Real.log ‖G 0‖ = Real.log ‖FL φ a ((x₀ : ℂ))‖ := by
    rw [hg0eq]
  unfold hFn BConst
  have hexpτ := Real.exp_pos τ
  have hexp1 := Real.exp_pos 1
  linarith [h4, hdouble, hpair, hsplit, h7, hjensen, h6, hlogeq]

/-! ### Theorem 1: the Hard Horizon Theorem

T1PRIME.md §1.2, for the abstract staircase-rigid multiset.  Hypotheses:
(S1) as `hφi`/`hsq`/`hφ2`; the ordinate head as a Finset with multiplicity
carried by the index set; (S2) as `hrig` (+ `hR0`, `hRe`); (S3) as
`hordp`/`hordm` (recentered vanishing orders, ≥ the fiber multiplicity);
Hypothesis A as `hx₀`/`hanchor`.  Conclusion: `τ ≤ 2a + 2 + ε*` with
`ε* = max 0 (epsStar a R κ)`.  Proof: the shared chain `log_anchor_bound`
plus Hypothesis A, extracted through L8 (`lemma8_tau_bound`). -/

theorem hard_horizon {φ : ℝ → ℂ} {a x₀ κ R τ : ℝ} {α : Type*} (ι : Finset α) (t : α → ℝ)
    (ha : 0 < a)
    -- (S1)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    -- the ordinate head below the horizon 2πe^τ
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    -- (S2)
    (hR0 : 0 ≤ R) (hRe : R < Real.exp (2 * a + 2))
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    -- (S3), recentered vanishing orders
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - (x₀ : ℂ)))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - (x₀ : ℂ)))
    -- Hypothesis A
    (hx₀ : |x₀| ≤ 2 * π)
    (hanchor : Real.exp (-(κ * a)) ≤ ‖FL φ a ((x₀ : ℂ))‖) :
    τ ≤ 2 * a + 2 + max 0 (epsStar a R κ) := by
  by_cases hcase : 2 * a + 2 ≤ τ
  swap
  · push_neg at hcase
    have hmax := le_max_left (0 : ℝ) (epsStar a R κ)
    linarith
  have hτ1 : (1 : ℝ) ≤ τ := by linarith
  have hz : FL φ a ((x₀ : ℂ)) ≠ 0 :=
    norm_pos_iff.mp (lt_of_lt_of_le (Real.exp_pos _) hanchor)
  have hcore := log_anchor_bound ι t ha hφi hsq hφ2 ht htT hrig hordp hordm hx₀ hz hτ1
  have hanchor2 : -Real.log ‖FL φ a ((x₀ : ℂ))‖ ≤ κ * a := by
    have hlog := Real.log_le_log (Real.exp_pos _) hanchor
    rw [Real.log_exp] at hlog
    linarith
  apply lemma8_tau_bound hR0 hRe hcase
  unfold hFn BConst at hcore ⊢
  linarith [hcore, hanchor2]

/-- Paper-facing form of `hard_horizon`: (S3) is stated directly as the
vanishing order of `F` at `±tₖ`, independently of the anchor point `x₀`.
`analyticOrderAt_translate` supplies the recentered orders needed by the
Jensen proof. -/
theorem hard_horizon_of_global_orders {φ : ℝ → ℂ} {a x₀ κ R τ : ℝ} {α : Type*}
    (ι : Finset α) (t : α → ℝ)
    (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    (hR0 : 0 ≤ R) (hRe : R < Real.exp (2 * a + 2))
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (FL φ a) (t k : ℂ))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (FL φ a) (-(t k : ℂ)))
    (hx₀ : |x₀| ≤ 2 * π)
    (hanchor : Real.exp (-(κ * a)) ≤ ‖FL φ a (x₀ : ℂ)‖) :
    τ ≤ 2 * a + 2 + max 0 (epsStar a R κ) := by
  apply hard_horizon ι t ha hφi hsq hφ2 ht htT hR0 hRe hrig
  · intro k hk
    rw [analyticOrderAt_translate (FL φ a) (lemma1_entire ha hφi)]
    simpa [sub_eq_add_neg] using hordp k hk
  · intro k hk
    rw [analyticOrderAt_translate (FL φ a) (lemma1_entire ha hφi)]
    simpa [sub_eq_add_neg] using hordm k hk
  · exact hx₀
  · exact hanchor

/-! ### Corollary 2: the zero desert

T1PRIME.md §1.3/§4.2.  Under the hypotheses of Theorem 1, at any radius
parameter `ρ' ≥ τ` there is a Jensen radius
`ρ ∈ [2πe^{ρ'} + 2π, 2πe^{ρ'} + 2π + 1]` free of zeros on its circle, and
the non-prescribed Jensen mass (`Other(ρ') =` divisor finsum minus the
prescribed pair masses — an upper bound for the paper's `Other`, since it
also counts excess multiplicity at prescribed points) satisfies
`Other(ρ') ≤ Φ(ρ') = 4a·e^{ρ'} − 2e^τ[(τ−2) + (ρ'−τ)(τ−1)] + 2R(ρ'−1) + B'`.
(`R ≥ 0` and `R < e^{2a+2}` are not needed here — no L8 step.) -/

theorem zero_desert {φ : ℝ → ℂ} {a x₀ κ R τ ρ' : ℝ} {α : Type*} (ι : Finset α) (t : α → ℝ)
    (ha : 0 < a)
    -- (S1)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    -- the ordinate head below the horizon 2πe^τ
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    -- (S2)
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    -- (S3), recentered vanishing orders
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - (x₀ : ℂ)))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - (x₀ : ℂ)))
    -- Hypothesis A
    (hx₀ : |x₀| ≤ 2 * π)
    (hanchor : Real.exp (-(κ * a)) ≤ ‖FL φ a ((x₀ : ℂ))‖)
    -- radius parameter
    (hτ1 : 1 ≤ τ) (hρ' : τ ≤ ρ') :
    ∃ ρ ∈ Icc (2 * π * Real.exp ρ' + 2 * π) (2 * π * Real.exp ρ' + 2 * π + 1),
      (∀ z ∈ Metric.sphere (0 : ℂ) |ρ|, FL φ a ((x₀ : ℂ) + z) ≠ 0) ∧
      (∑ᶠ u, (MeromorphicOn.divisor (fun z => FL φ a ((x₀ : ℂ) + z))
            (Metric.closedBall 0 |ρ|) u : ℝ) * Real.log (ρ * ‖u‖⁻¹))
        - (∑ k ∈ ι, (Real.log (ρ * ‖(t k : ℂ) - (x₀ : ℂ)‖⁻¹)
            + Real.log (ρ * ‖-(t k : ℂ) - (x₀ : ℂ)‖⁻¹)))
        ≤ 4 * a * Real.exp ρ' - 2 * Real.exp τ * ((τ - 2) + (ρ' - τ) * (τ - 1))
          + 2 * R * (ρ' - 1) + BConst a κ := by
  have hπ : (0 : ℝ) < π := pi_pos
  have htpos : ∀ k ∈ ι, 0 < t k :=
    fun k hk => lt_trans (by positivity) (ht k hk)
  have hexpmono : 2 * π * Real.exp τ ≤ 2 * π * Real.exp ρ' :=
    mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hρ') (by positivity)
  have htT' : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp ρ' :=
    fun k hk => le_trans (htT k hk) hexpmono
  -- the recentered transform
  set G : ℂ → ℂ := fun z => FL φ a ((x₀ : ℂ) + z) with hGdef
  have hGdiff : Differentiable ℂ G :=
    (lemma1_entire ha hφi).comp ((differentiable_const _).add differentiable_id)
  have hanchor_pos : (0 : ℝ) < ‖FL φ a ((x₀ : ℂ))‖ :=
    lt_of_lt_of_le (Real.exp_pos _) hanchor
  have hG0 : G 0 ≠ 0 := by
    simp only [hGdef]
    simpa using norm_pos_iff.mp hanchor_pos
  -- L5 at the enlarged radius parameter
  obtain ⟨ρ, hρmem, hρsphere, hjensen⟩ :=
    lemma5_jensen hGdiff hG0 (T := 2 * π * Real.exp ρ') (by positivity)
  have hρT : 2 * π * Real.exp ρ' + 2 * π ≤ ρ := hρmem.1
  have hρpos : (0 : ℝ) < ρ := lt_of_lt_of_le (by positivity) hρmem.1
  refine ⟨ρ, hρmem, hρsphere, ?_⟩
  -- L6 at the enlarged radius
  have hint6 : CircleIntegrable (fun z => Real.log ‖G z‖) 0 ρ :=
    MeromorphicOn.circleIntegrable_log_norm
      (((Complex.analyticOnNhd_univ_iff_differentiable.mpr hGdiff).mono
        (subset_univ _)).meromorphicOn)
  have hgrowth : ∀ z : ℂ, ‖G z‖ ≤ Real.sqrt (2 * a) * Real.exp (a * |z.im|) :=
    fun z => lemma1_growth_recentered ha hφi hsq hφ2 x₀ z
  have h6 := lemma6_circle_bound_tau ha hρpos.le hρmem.2 hint6 hρsphere hgrowth
  have hanchor2 : -Real.log ‖G 0‖ ≤ κ * a := by
    have hg0 : Real.exp (-(κ * a)) ≤ ‖G 0‖ := by
      simp only [hGdef]
      simpa using hanchor
    have hlog := Real.log_le_log (Real.exp_pos _) hg0
    rw [Real.log_exp] at hlog
    linarith
  -- prescribed points (as in Theorem 1)
  set pp : α → ℂ := fun k => ((t k : ℂ)) - (x₀ : ℂ) with hppdef
  set pm : α → ℂ := fun k => -((t k : ℂ)) - (x₀ : ℂ) with hpmdef
  set P : Finset ℂ := ι.image pp ∪ ι.image pm with hPdef
  set m : ℂ → ℕ := fun u =>
    (ι.filter fun k => pp k = u).card + (ι.filter fun k => pm k = u).card with hmdef
  have hnorm_pp : ∀ k ∈ ι, ‖pp k‖ = |t k - x₀| := by
    intro k hk
    simp only [hppdef]
    rw [show ((t k : ℂ)) - (x₀ : ℂ) = (((t k - x₀ : ℝ)) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs]
  have hnorm_pm : ∀ k ∈ ι, ‖pm k‖ = |t k + x₀| := by
    intro k hk
    simp only [hpmdef]
    rw [show -((t k : ℂ)) - (x₀ : ℂ) = (((-(t k + x₀) : ℝ)) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs, abs_neg]
  have habs_pp : ∀ k ∈ ι, |t k - x₀| ≤ 2 * π * Real.exp ρ' + 2 * π := by
    intro k hk
    have h1 := abs_le.mp hx₀
    have h2 := ht k hk
    have h3 := htT' k hk
    rw [abs_le]
    constructor <;> nlinarith [Real.exp_pos ρ']
  have habs_pm : ∀ k ∈ ι, |t k + x₀| ≤ 2 * π * Real.exp ρ' + 2 * π := by
    intro k hk
    have h1 := abs_le.mp hx₀
    have h2 := ht k hk
    have h3 := htT' k hk
    rw [abs_le]
    constructor <;> nlinarith [Real.exp_pos ρ']
  have hPball : ∀ u ∈ P, u ∈ Metric.closedBall (0 : ℂ) |ρ| := by
    intro u hu
    rw [mem_closedBall_zero_iff, abs_of_pos hρpos]
    rcases Finset.mem_union.mp hu with h | h
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      rw [hnorm_pp k hk]
      linarith [habs_pp k hk]
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      rw [hnorm_pm k hk]
      linarith [habs_pm k hk]
  have hfiber_pp : ∀ k ∈ ι, (ι.filter fun j => pp j = pp k) = ι.filter fun j => t j = t k := by
    intro k _
    apply Finset.filter_congr
    intro j _
    simp only [hppdef]
    constructor
    · intro he
      exact_mod_cast sub_left_inj.mp he
    · intro he
      rw [he]
  have hfiber_pm : ∀ k ∈ ι, (ι.filter fun j => pm j = pm k) = ι.filter fun j => t j = t k := by
    intro k _
    apply Finset.filter_congr
    intro j _
    simp only [hpmdef]
    constructor
    · intro he
      have h2 : -((t j : ℝ) : ℂ) = -((t k : ℝ) : ℂ) := sub_left_inj.mp he
      exact_mod_cast neg_inj.mp h2
    · intro he
      rw [he]
  have hcross_mp : ∀ k ∈ ι, (ι.filter fun j => pm j = pp k) = ∅ := by
    intro k hk
    rw [Finset.filter_eq_empty_iff]
    intro j hj he
    simp only [hppdef, hpmdef] at he
    have h2 : -((t j : ℝ) : ℂ) = ((t k : ℝ) : ℂ) := sub_left_inj.mp he
    have h3 : -(t j) = t k := by exact_mod_cast h2
    have h4 := ht j hj
    have h5 := ht k hk
    linarith
  have hcross_pm : ∀ k ∈ ι, (ι.filter fun j => pp j = pm k) = ∅ := by
    intro k hk
    rw [Finset.filter_eq_empty_iff]
    intro j hj he
    simp only [hppdef, hpmdef] at he
    have h2 : ((t j : ℝ) : ℂ) = -((t k : ℝ) : ℂ) := sub_left_inj.mp he
    have h3 : t j = -(t k) := by exact_mod_cast h2
    have h4 := ht j hj
    have h5 := ht k hk
    linarith
  have hPord : ∀ u ∈ P, (m u : ℕ∞) ≤ analyticOrderAt G u := by
    intro u hu
    rcases Finset.mem_union.mp hu with h | h
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      have hm_eq : m (pp k) = (ι.filter fun j => t j = t k).card := by
        simp only [hmdef]
        rw [hfiber_pp k hk, hcross_mp k hk]
        simp
      rw [hm_eq]
      exact hordp k hk
    · obtain ⟨k, hk, rfl⟩ := Finset.mem_image.mp h
      have hm_eq : m (pm k) = (ι.filter fun j => t j = t k).card := by
        simp only [hmdef]
        rw [hfiber_pm k hk, hcross_pm k hk]
        simp
      rw [hm_eq]
      exact hordm k hk
  have h7 := lemma7_divisor_lower hρpos hGdiff hG0 P m hPball hPord
  -- the prescribed mass splits (as in Theorem 1)
  have e_pp : ∑ u ∈ P, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = ∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹) := by
    have h1 : ∑ u ∈ ι.image pp, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
        = ∑ u ∈ P, ((ι.filter fun k => pp k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
      apply Finset.sum_subset Finset.subset_union_left
      intro u _ hnot
      have hempty : (ι.filter fun k => pp k = u) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        intro k hk he
        exact hnot (Finset.mem_image.mpr ⟨k, hk, he⟩)
      rw [hempty]
      simp
    have h2 : ∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)
        = ∑ u ∈ ι.image pp, (ι.filter fun k => pp k = u).card • Real.log (ρ * ‖u‖⁻¹) :=
      Finset.sum_comp (fun u : ℂ => Real.log (ρ * ‖u‖⁻¹)) pp
    rw [← h1, h2]
    apply Finset.sum_congr rfl
    intro u _
    rw [nsmul_eq_mul]
  have e_pm : ∑ u ∈ P, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    have h1 : ∑ u ∈ ι.image pm, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹)
        = ∑ u ∈ P, ((ι.filter fun k => pm k = u).card : ℝ) * Real.log (ρ * ‖u‖⁻¹) := by
      apply Finset.sum_subset Finset.subset_union_right
      intro u _ hnot
      have hempty : (ι.filter fun k => pm k = u) = ∅ := by
        rw [Finset.filter_eq_empty_iff]
        intro k hk he
        exact hnot (Finset.mem_image.mpr ⟨k, hk, he⟩)
      rw [hempty]
      simp
    have h2 : ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹)
        = ∑ u ∈ ι.image pm, (ι.filter fun k => pm k = u).card • Real.log (ρ * ‖u‖⁻¹) :=
      Finset.sum_comp (fun u : ℂ => Real.log (ρ * ‖u‖⁻¹)) pm
    rw [← h1, h2]
    apply Finset.sum_congr rfl
    intro u _
    rw [nsmul_eq_mul]
  have hsplit : ∑ u ∈ P, (m u : ℝ) * Real.log (ρ * ‖u‖⁻¹)
      = (∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)) + ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    rw [← e_pp, ← e_pm, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro u _
    simp only [hmdef]
    push_cast
    ring
  -- strengthened pair bound at the enlarged radius (T := 2πe^{ρ'})
  have hpair : ∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp ρ' / t k)
      ≤ (∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)) + ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_le_sum
    intro k hk
    rw [hnorm_pp k hk, hnorm_pm k hk, ← div_eq_mul_inv, ← div_eq_mul_inv]
    exact lemma7_pair_product hx₀ (ht k hk) (htT' k hk) hρT
  -- L2 + L4 at the τ-horizon
  set I : ℝ := ∫ s in Ioc (0 : ℝ) (2 * π * Real.exp τ),
    ((ι.filter fun k => t k ≤ s).card : ℝ) / s with hIdef
  have hcount : ∑ k ∈ ι, Real.log (2 * π * Real.exp τ / t k) = I := by
    rw [hIdef]
    exact lemma2_sum_log_eq_integral ι t htpos htT
  have h4 : Real.exp τ * (τ - 2) + 7 / 8 * (τ - 1) + Real.exp 1 - R * (τ - 1) ≤ I := by
    rw [hIdef]
    exact lemma4_rigidity_transfer hτ1 (lemma2_integrableOn ι t htpos)
      (fun s _ => Nat.cast_nonneg _) hrig
  -- shift the pair sum from the τ- to the ρ'-horizon
  have hlogshift : ∀ k ∈ ι, Real.log (2 * π * Real.exp ρ' / t k)
      = Real.log (2 * π * Real.exp τ / t k) + (ρ' - τ) := by
    intro k hk
    have htk := htpos k hk
    rw [Real.log_div (by positivity) (ne_of_gt htk),
      Real.log_div (by positivity) (ne_of_gt htk),
      Real.log_mul (by positivity) (Real.exp_ne_zero _),
      Real.log_mul (by positivity) (Real.exp_ne_zero _),
      Real.log_exp, Real.log_exp]
    ring
  have hshiftsum : ∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp ρ' / t k)
      = 2 * I + (ι.card : ℝ) * (2 * (ρ' - τ)) := by
    calc ∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp ρ' / t k)
        = ∑ k ∈ ι, (2 * Real.log (2 * π * Real.exp τ / t k) + 2 * (ρ' - τ)) := by
          apply Finset.sum_congr rfl
          intro k hk
          rw [hlogshift k hk]
          ring
      _ = (∑ k ∈ ι, 2 * Real.log (2 * π * Real.exp τ / t k)) + ι.card • (2 * (ρ' - τ)) := by
          rw [Finset.sum_add_distrib, Finset.sum_const]
      _ = 2 * I + (ι.card : ℝ) * (2 * (ρ' - τ)) := by
          rw [← hcount, Finset.mul_sum, nsmul_eq_mul]
  -- the head count at the τ-horizon (from (S2) at s = 2πe^τ)
  have hfull : (ι.filter fun k => t k ≤ 2 * π * Real.exp τ) = ι :=
    Finset.filter_true_of_mem htT
  have hcard : Nhat (2 * π * Real.exp τ) - R ≤ (ι.card : ℝ) := by
    have h := hrig (2 * π * Real.exp τ)
      ⟨mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hτ1) (by positivity), le_refl _⟩
    rwa [hfull] at h
  have hNhat : Nhat (2 * π * Real.exp τ) = Real.exp τ * (τ - 1) + 7 / 8 := by
    unfold Nhat
    have h1 : 2 * π * Real.exp τ / (2 * π * Real.exp 1) = Real.exp (τ - 1) := by
      rw [Real.exp_sub]
      field_simp
    rw [h1, Real.log_exp]
    field_simp
  have hmul : 2 * (ρ' - τ) * (Real.exp τ * (τ - 1) + 7 / 8 - R)
      ≤ 2 * (ρ' - τ) * (ι.card : ℝ) := by
    apply mul_le_mul_of_nonneg_left ?_ (by linarith)
    rw [← hNhat]
    exact hcard
  -- bridge the conclusion's explicit prescribed sum to the pp/pm form
  have hgoalsum : ∑ k ∈ ι, (Real.log (ρ * ‖(t k : ℂ) - (x₀ : ℂ)‖⁻¹)
        + Real.log (ρ * ‖-(t k : ℂ) - (x₀ : ℂ)‖⁻¹))
      = (∑ k ∈ ι, Real.log (ρ * ‖pp k‖⁻¹)) + ∑ k ∈ ι, Real.log (ρ * ‖pm k‖⁻¹) := by
    rw [← Finset.sum_add_distrib]
  -- final chain
  have hexpτ := Real.exp_pos τ
  have hexp1 := Real.exp_pos 1
  rw [hgoalsum]
  unfold BConst
  linarith [h4, hpair, hsplit, h7, hjensen, h6, hanchor2, hshiftsum, hmul]

/-! ### QC-2: the anchor collapse (annihilating-pair form of Theorem 1)

results/ias/SEAT-quasicrystal.md, Round-2 C-9 spec.  Hypothesis A is dropped
entirely (`by_cases` on `F(x₀) = 0`); the conclusion bounds `‖F(x₀)‖` for
EVERY low-band point `|x₀| ≤ 2π`: past the hard horizon, anchor mass dies at
the scale `exp(B₀ − h(τ))` — de-anchoring costs `2e²δ·e^{2a}` per unit `δ`
of dodging beyond `e²T*` (`anchor_collapse_of_deep`).  `_hR0`/`_hRe` are
kept from the spec for (S2)-fidelity but are not needed by the proof of
`anchor_collapse` (they ARE needed for `_of_deep`'s monotonicity step). -/

/-- QC-2 (anchored-pair rearrangement of Theorem 1): past the hard
horizon, low-band values collapse at the envelope scale.  Same hypotheses
as `hard_horizon` MINUS the anchor; conclusion bounds `‖F(x₀)‖` for every
`|x₀| ≤ 2π`.  `BConst a 0 = (4 + 2/π)·a + ½·ln(2a)` is the κ-free anchor
constant. -/
theorem anchor_collapse {φ : ℝ → ℂ} {a x₀ R τ : ℝ} {α : Type*}
    (ι : Finset α) (t : α → ℝ) (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    (_hR0 : 0 ≤ R) (_hRe : R < Real.exp (2 * a + 2))
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - (x₀ : ℂ)))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - (x₀ : ℂ)))
    (hx₀ : |x₀| ≤ 2 * π)
    (hτ : 2 * a + 2 ≤ τ) :
    ‖FL φ a (x₀ : ℂ)‖ ≤ Real.exp (BConst a 0 - hFn a R τ) := by
  by_cases hz : FL φ a ((x₀ : ℂ)) = 0
  · rw [hz, norm_zero]
    exact (Real.exp_pos _).le
  · have hτ1 : (1 : ℝ) ≤ τ := by linarith
    have hcore := log_anchor_bound ι t ha hφi hsq hφ2 ht htT hrig hordp hordm hx₀ hz hτ1
    have hpos : (0 : ℝ) < ‖FL φ a ((x₀ : ℂ))‖ := norm_pos_iff.mpr hz
    rw [← Real.log_le_iff_le_exp hpos]
    linarith [hcore]

/-- The L8 evaluation exposed (C-9 proof-plan item 3): at `τ = 2a + 2 + δ`,
`h(τ) ≥ 2δ·e^{2a+2} − 2R(2a + 1 + δ)`.  (Inside `lemma8_crossing`'s proof
this is exact with `e^{2a+2+δ}`; the `e^{2a+2}` form is what
`anchor_collapse_of_deep` states.) -/
lemma hFn_lower_at {a R δ : ℝ} (hδ : 0 ≤ δ) :
    2 * δ * Real.exp (2 * a + 2) - 2 * R * (2 * a + 1 + δ)
      ≤ hFn a R (2 * a + 2 + δ) := by
  unfold hFn
  have hexp : Real.exp (2 * a + 2) ≤ Real.exp (2 * a + 2 + δ) :=
    Real.exp_le_exp.mpr (by linarith)
  nlinarith [mul_le_mul_of_nonneg_left hexp hδ]

/-- Deep form: at `τ ≥ 2a + 2 + δ` the bound reads
`exp(B₀ + 2R(2a+1+δ) − 2δ·e^{2a+2})` — anchor mass dies at the
envelope's super-exponential scale (`2e² vs 4π` per unit `e^{2a}`). -/
theorem anchor_collapse_of_deep {φ : ℝ → ℂ} {a x₀ R τ δ : ℝ} {α : Type*}
    (ι : Finset α) (t : α → ℝ) (ha : 0 < a)
    (hφi : IntegrableOn φ (Icc (-a) a))
    (hsq : IntegrableOn (fun x => ‖φ x‖ ^ 2) (Icc (-a) a))
    (hφ2 : (∫ x in Icc (-a) a, ‖φ x‖ ^ 2) ≤ 1)
    (ht : ∀ k ∈ ι, 2 * π < t k)
    (htT : ∀ k ∈ ι, t k ≤ 2 * π * Real.exp τ)
    (_hR0 : 0 ≤ R) (hRe : R < Real.exp (2 * a + 2))
    (hrig : ∀ s ∈ Icc (2 * π * Real.exp 1) (2 * π * Real.exp τ),
      Nhat s - R ≤ ((ι.filter fun k => t k ≤ s).card : ℝ))
    (hordp : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) ((t k : ℂ) - (x₀ : ℂ)))
    (hordm : ∀ k ∈ ι, ((ι.filter fun j => t j = t k).card : ℕ∞)
      ≤ analyticOrderAt (fun z => FL φ a ((x₀ : ℂ) + z)) (-(t k : ℂ) - (x₀ : ℂ)))
    (hx₀ : |x₀| ≤ 2 * π)
    (hδ : 0 < δ) (hτδ : 2 * a + 2 + δ ≤ τ) :
    ‖FL φ a (x₀ : ℂ)‖
      ≤ Real.exp (BConst a 0 + 2 * R * (2 * a + 1 + δ)
          - 2 * δ * Real.exp (2 * a + 2)) := by
  have h1 := anchor_collapse ι t ha hφi hsq hφ2 ht htT _hR0 hRe hrig hordp hordm hx₀
    (by linarith : 2 * a + 2 ≤ τ)
  have h2 : hFn a R (2 * a + 2 + δ) ≤ hFn a R τ := by
    rcases eq_or_lt_of_le hτδ with he | hlt
    · exact le_of_eq (by rw [he])
    · exact le_of_lt ((lemma8_strictMonoOn hRe)
        (mem_Ici.mpr (by linarith)) (mem_Ici.mpr (by linarith)) hlt)
  have h3 := hFn_lower_at (a := a) (R := R) hδ.le
  calc ‖FL φ a (x₀ : ℂ)‖
      ≤ Real.exp (BConst a 0 - hFn a R τ) := h1
    _ ≤ Real.exp (BConst a 0 + 2 * R * (2 * a + 1 + δ)
          - 2 * δ * Real.exp (2 * a + 2)) := by
        apply Real.exp_le_exp.mpr
        linarith

end HardHorizon
