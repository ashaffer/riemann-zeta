/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GeneralZetaWeilForm

/-!
# Canonical embeddings between nested compact-support spaces

The embedding is defined by taking the canonical full-line zero extension at
the smaller support and restricting that same real-valued representative to
the larger interval.
-/

namespace RHP2Bridge.NestedSupport

open scoped ENNReal InnerProductSpace

noncomputable section

/-- The smaller-support vector, viewed pointwise on the larger interval. -/
def nestedSupportFn (a b : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    LegendreScaledL2.Interval b → ℝ :=
  fun x ↦ RCLike.re (IntervalZeroExtension.zeroExtensionFn a w (x : ℝ))

theorem nestedSupportFn_memLp (a b : ℝ)
    (w : LegendreScaledL2.IntervalL2 a) :
    MeasureTheory.MemLp (nestedSupportFn a b w) 2
      (LegendreScaledL2.intervalMeasure b) := by
  let s : Set ℝ := LegendreScaledL2.Interval b
  have hs : MeasurableSet s := measurableSet_Icc
  have hcoe : MeasurableEmbedding (fun x : s ↦ (x : ℝ)) :=
    MeasurableEmbedding.subtype_coe hs
  have hrestrict :=
    (IntervalZeroExtension.zeroExtensionFn_memLp a w).restrict s
  have hreal := hrestrict.re
  change MeasureTheory.MemLp
    ((fun x : ℝ ↦ RCLike.re
      (IntervalZeroExtension.zeroExtensionFn a w x)) ∘
        (fun x : s ↦ (x : ℝ))) 2
    (MeasureTheory.Measure.comap (fun x : s ↦ (x : ℝ))
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
  rw [← hcoe.memLp_map_measure_iff]
  rw [map_comap_subtype_coe hs]
  simpa [Function.comp_def, s] using hreal

/-- Canonical inclusion of `L²[-a,a]` into `L²[-b,b]` by zero extension. -/
def nestedSupport (a b : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    LegendreScaledL2.IntervalL2 b :=
  (nestedSupportFn_memLp a b w).toLp (nestedSupportFn a b w)

theorem coe_nestedSupport (a b : ℝ)
    (w : LegendreScaledL2.IntervalL2 a) :
    (nestedSupport a b w : LegendreScaledL2.Interval b → ℝ) =ᵐ[
      LegendreScaledL2.intervalMeasure b] nestedSupportFn a b w :=
  (nestedSupportFn_memLp a b w).coeFn_toLp

theorem ofReal_re_zeroExtensionFn (a : ℝ)
    (w : LegendreScaledL2.IntervalL2 a) (x : ℝ) :
    ((RCLike.re (IntervalZeroExtension.zeroExtensionFn a w x) : ℝ) : ℂ) =
      IntervalZeroExtension.zeroExtensionFn a w x := by
  by_cases hx : x ∈ LegendreScaledL2.Interval a
  · let y : LegendreScaledL2.Interval a := ⟨x, hx⟩
    change ((RCLike.re
      (IntervalZeroExtension.zeroExtensionFn a w (y : ℝ)) : ℝ) : ℂ) = _
    rw [IntervalZeroExtension.zeroExtensionFn_coe]
    simp
  · rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a w hx]
    simp

/-- The defining compatibility: embedding into a larger interval and then
zero-extending to the line gives exactly the original full-line `L²` vector. -/
theorem zeroExtension_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    IntervalZeroExtension.zeroExtension b (nestedSupport a b w) =
      IntervalZeroExtension.zeroExtension a w := by
  let s : Set ℝ := LegendreScaledL2.Interval b
  have hs : MeasurableSet s := measurableSet_Icc
  have hfn :
      IntervalZeroExtension.zeroExtensionFn b (nestedSupport a b w) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
        IntervalZeroExtension.zeroExtensionFn a w := by
    apply MeasureTheory.ae_of_ae_restrict_of_ae_restrict_compl s
    · rw [ae_restrict_iff_subtype hs]
      filter_upwards [coe_nestedSupport a b w] with x hx
      rw [IntervalZeroExtension.zeroExtensionFn_coe, hx]
      exact ofReal_re_zeroExtensionFn a w (x : ℝ)
    · apply (MeasureTheory.ae_restrict_iff' hs.compl).2
      filter_upwards [] with x hx
      have hxb : x ∉ LegendreScaledL2.Interval b := hx
      have hxa : x ∉ LegendreScaledL2.Interval a := by
        intro hxa
        exact hxb ⟨(by linarith [hxa.1]), (by linarith [hxa.2])⟩
      rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem
        b (nestedSupport a b w) hxb]
      rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem a w hxa]
  apply MeasureTheory.Lp.ext
  exact (IntervalZeroExtension.coeFn_zeroExtension b
      (nestedSupport a b w)).trans <|
    hfn.trans (IntervalZeroExtension.coeFn_zeroExtension a w).symm

/-- Nested zero extension preserves the `L²` norm exactly. -/
theorem norm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    ‖nestedSupport a b w‖ = ‖w‖ := by
  rw [← IntervalZeroExtension.norm_zeroExtension b,
    zeroExtension_nestedSupport hab,
    IntervalZeroExtension.norm_zeroExtension]

/-- The canonical nested-support inclusion as a real-linear map. -/
def nestedSupportLinearMap (a b : ℝ) (hab : a ≤ b) :
    LegendreScaledL2.IntervalL2 a →ₗ[ℝ] LegendreScaledL2.IntervalL2 b where
  toFun := nestedSupport a b
  map_add' w v := by
    apply (IntervalZeroExtension.zeroExtensionLI b).injective
    change IntervalZeroExtension.zeroExtension b (nestedSupport a b (w + v)) =
      IntervalZeroExtension.zeroExtension b
        (nestedSupport a b w + nestedSupport a b v)
    rw [IntervalZeroExtension.zeroExtension_add b
      (nestedSupport a b w) (nestedSupport a b v)]
    rw [zeroExtension_nestedSupport hab, zeroExtension_nestedSupport hab,
      zeroExtension_nestedSupport hab,
      IntervalZeroExtension.zeroExtension_add]
  map_smul' c w := by
    apply (IntervalZeroExtension.zeroExtensionLI b).injective
    change IntervalZeroExtension.zeroExtension b (nestedSupport a b (c • w)) =
      IntervalZeroExtension.zeroExtension b (c • nestedSupport a b w)
    rw [IntervalZeroExtension.zeroExtension_smul b c (nestedSupport a b w)]
    rw [zeroExtension_nestedSupport hab, zeroExtension_nestedSupport hab,
      IntervalZeroExtension.zeroExtension_smul]

@[simp] theorem nestedSupportLinearMap_apply (a b : ℝ) (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    nestedSupportLinearMap a b hab w = nestedSupport a b w := rfl

/-- The canonical nested-support inclusion as a linear isometry. -/
def nestedSupportLI (a b : ℝ) (hab : a ≤ b) :
    LegendreScaledL2.IntervalL2 a →ₗᵢ[ℝ] LegendreScaledL2.IntervalL2 b where
  toLinearMap := nestedSupportLinearMap a b hab
  norm_map' := norm_nestedSupport hab

@[simp] theorem nestedSupportLI_apply (a b : ℝ) (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    nestedSupportLI a b hab w = nestedSupport a b w := rfl

/-- The Plancherel Fourier vector is unchanged by enlarging the support of a
vector that is still zero outside the smaller interval. -/
theorem fourierZeroExtensionL2_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) :
    IntervalZeroExtension.fourierZeroExtensionL2 b (nestedSupport a b w) =
      IntervalZeroExtension.fourierZeroExtensionL2 a w := by
  unfold IntervalZeroExtension.fourierZeroExtensionL2
  rw [zeroExtension_nestedSupport hab]

/-- Consequently every Fourier-energy density is exactly preserved. -/
theorem fourierEnergy_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) (xi : ℝ) :
    GeneralZetaWeilForm.fourierEnergy b (nestedSupport a b w) xi =
      GeneralZetaWeilForm.fourierEnergy a w xi := by
  unfold GeneralZetaWeilForm.fourierEnergy
  rw [fourierZeroExtensionL2_nestedSupport hab]

/-- Interval autocorrelation is likewise independent of which containing
interval is used to represent the same full-line vector. -/
theorem intervalAutocorrelation_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (u : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    AutocorrelationPlancherel.intervalAutocorrelation b u
        (nestedSupport a b w) =
      AutocorrelationPlancherel.intervalAutocorrelation a u w := by
  rw [AutocorrelationPlancherel.intervalAutocorrelation_eq_cos_fourier_energy,
    AutocorrelationPlancherel.intervalAutocorrelation_eq_cos_fourier_energy]
  simp_rw [fourierZeroExtensionL2_nestedSupport hab]

/-- Each old prime-power summand is unchanged under the nested-support
inclusion; only activation of additional indices can change the prime sum. -/
theorem primePowerTerm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) (n : ℕ) :
    GeneralZetaWeilForm.primePowerTerm b (nestedSupport a b w) n =
      GeneralZetaWeilForm.primePowerTerm a w n := by
  unfold GeneralZetaWeilForm.primePowerTerm
  rw [intervalAutocorrelation_nestedSupport hab]

theorem archimedeanTerm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.archimedeanTerm b (nestedSupport a b w) =
      GeneralZetaWeilForm.archimedeanTerm a w := by
  unfold GeneralZetaWeilForm.archimedeanTerm
  simp_rw [fourierEnergy_nestedSupport hab]

theorem inLogarithmicDomain_nestedSupport_iff {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.InLogarithmicDomain b (nestedSupport a b w) ↔
      GeneralZetaWeilForm.InLogarithmicDomain a w := by
  unfold GeneralZetaWeilForm.InLogarithmicDomain
  simp_rw [fourierEnergy_nestedSupport hab]

theorem primeTerm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.primeTerm b (nestedSupport a b w) =
      GeneralZetaWeilForm.primeTerm a w +
        ∑ n ∈ GeneralZetaWeilForm.activePrimePowers b \
            GeneralZetaWeilForm.activePrimePowers a,
          GeneralZetaWeilForm.primePowerTerm a w n := by
  rw [GeneralZetaWeilForm.primeTerm_eq_old_add_new hab]
  unfold GeneralZetaWeilForm.primeTerm
  congr 1 <;>
    apply Finset.sum_congr rfl <;>
    intro n hn <;>
    exact primePowerTerm_nestedSupport hab w n

/-- Pairing with either exponential pole vector is unchanged by enlarging the
containing interval. -/
theorem inner_nestedSupport_poleL2 {a b : ℝ} (hab : a ≤ b)
    (w : LegendreScaledL2.IntervalL2 a) (s : ℝ) :
    inner ℝ (nestedSupport a b w) (PoleProjection.poleL2 b s) =
      inner ℝ w (PoleProjection.poleL2 a s) := by
  let F : ℝ → ℝ := fun x ↦
    RCLike.re (IntervalZeroExtension.zeroExtensionFn a w x) *
      Real.exp (s * x / 2)
  have hsubset : LegendreScaledL2.Interval a ⊆
      LegendreScaledL2.Interval b := by
    intro x hx
    exact ⟨by linarith [hx.1], by linarith [hx.2]⟩
  have hlarge :
      inner ℝ (nestedSupport a b w) (PoleProjection.poleL2 b s) =
        ∫ x in LegendreScaledL2.Interval b, F x := by
    rw [MeasureTheory.L2.inner_def]
    calc
      (∫ x : LegendreScaledL2.Interval b,
          inner ℝ ((nestedSupport a b w :
            LegendreScaledL2.Interval b → ℝ) x)
            ((PoleProjection.poleL2 b s :
              LegendreScaledL2.Interval b → ℝ) x)
          ∂(LegendreScaledL2.intervalMeasure b)) =
          ∫ x : LegendreScaledL2.Interval b,
            nestedSupportFn a b w x *
              Real.exp (s * (x : ℝ) / 2)
            ∂(LegendreScaledL2.intervalMeasure b) := by
        apply MeasureTheory.integral_congr_ae
        have hpole := (PoleProjection.poleContinuous b s).coeFn_toLp
          (p := 2) (𝕜 := ℝ) (LegendreScaledL2.intervalMeasure b)
        filter_upwards [coe_nestedSupport a b w, hpole] with x hx hp
        rw [hx]
        rw [show (PoleProjection.poleL2 b s :
          LegendreScaledL2.Interval b → ℝ) x =
            PoleProjection.poleContinuous b s x by
              simpa [PoleProjection.poleL2] using hp]
        simp [PoleProjection.poleContinuous, mul_comm]
      _ = ∫ x in LegendreScaledL2.Interval b, F x := by
        simpa [nestedSupportFn, F, LegendreScaledL2.intervalMeasure] using
          (MeasureTheory.integral_subtype_comap
            (μ := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
            measurableSet_Icc F)
  have hsmall :
      inner ℝ w (PoleProjection.poleL2 a s) =
        ∫ x in LegendreScaledL2.Interval a, F x := by
    rw [MeasureTheory.L2.inner_def]
    calc
      (∫ x : LegendreScaledL2.Interval a,
          inner ℝ ((w : LegendreScaledL2.Interval a → ℝ) x)
            ((PoleProjection.poleL2 a s :
              LegendreScaledL2.Interval a → ℝ) x)
          ∂(LegendreScaledL2.intervalMeasure a)) =
          ∫ x : LegendreScaledL2.Interval a,
            RCLike.re (IntervalZeroExtension.zeroExtensionFn a w (x : ℝ)) *
              Real.exp (s * (x : ℝ) / 2)
            ∂(LegendreScaledL2.intervalMeasure a) := by
        apply MeasureTheory.integral_congr_ae
        have hpole := (PoleProjection.poleContinuous a s).coeFn_toLp
          (p := 2) (𝕜 := ℝ) (LegendreScaledL2.intervalMeasure a)
        filter_upwards [hpole] with x hp
        rw [show (PoleProjection.poleL2 a s :
          LegendreScaledL2.Interval a → ℝ) x =
            PoleProjection.poleContinuous a s x by
              simpa [PoleProjection.poleL2] using hp]
        simp [PoleProjection.poleContinuous,
          IntervalZeroExtension.zeroExtensionFn_coe, mul_comm]
      _ = ∫ x in LegendreScaledL2.Interval a, F x := by
        rw [LegendreScaledL2.intervalMeasure]
        trans ∫ x : LegendreScaledL2.Interval a, F (x : ℝ)
          ∂MeasureTheory.Measure.comap Subtype.val
            (MeasureTheory.volume : MeasureTheory.Measure ℝ)
        · apply MeasureTheory.integral_congr_ae
          filter_upwards [] with x
          simp [F, IntervalZeroExtension.zeroExtensionFn_coe]
        · exact MeasureTheory.integral_subtype_comap
            (μ := (MeasureTheory.volume : MeasureTheory.Measure ℝ))
            measurableSet_Icc F
  rw [hlarge, hsmall]
  apply MeasureTheory.setIntegral_eq_of_subset_of_forall_sdiff_eq_zero
    measurableSet_Icc hsubset
  intro x hx
  unfold F
  rw [IntervalZeroExtension.zeroExtensionFn_eq_zero_of_not_mem]
  · simp
  · exact hx.2

theorem poleTerm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.poleTerm b (nestedSupport a b w) =
      GeneralZetaWeilForm.poleTerm a w := by
  unfold GeneralZetaWeilForm.poleTerm PoleProjection.polePlusL2
    PoleProjection.poleMinusL2
  rw [inner_nestedSupport_poleL2 hab, inner_nestedSupport_poleL2 hab]

/-- Exact support-growth formula on the embedded old space.  Enlarging the
ambient interval changes the Weil form only through newly activated prime
powers.  Their autocorrelations are signed, so this is an identity rather
than a monotonicity assertion. -/
theorem weilForm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.weilForm b (nestedSupport a b w) =
      GeneralZetaWeilForm.weilForm a w -
        ∑ n ∈ GeneralZetaWeilForm.activePrimePowers b \
            GeneralZetaWeilForm.activePrimePowers a,
          GeneralZetaWeilForm.primePowerTerm a w n := by
  unfold GeneralZetaWeilForm.weilForm
  rw [poleTerm_nestedSupport hab, archimedeanTerm_nestedSupport hab,
    primeTerm_nestedSupport hab]
  ring

/-- Between prime-power activation thresholds the Weil form is exactly
unchanged on the embedded old-support subspace. -/
theorem weilForm_nestedSupport_of_active_eq {a b : ℝ} (hab : a ≤ b)
    (hactive : GeneralZetaWeilForm.activePrimePowers b =
      GeneralZetaWeilForm.activePrimePowers a)
    (w : GeneralZetaWeilForm.TestSpace a) :
    GeneralZetaWeilForm.weilForm b (nestedSupport a b w) =
      GeneralZetaWeilForm.weilForm a w := by
  rw [weilForm_nestedSupport hab, hactive]
  simp

/-- Canonical inclusion on the logarithmic form domains. -/
def nestedLogarithmicSupport {a b : ℝ} (hab : a ≤ b)
    (f : GeneralZetaWeilForm.LogarithmicFormDomain a) :
    GeneralZetaWeilForm.LogarithmicFormDomain b :=
  ⟨nestedSupport a b f.val,
    (inLogarithmicDomain_nestedSupport_iff hab f.val).2 f.property⟩

@[simp] theorem nestedLogarithmicSupport_val {a b : ℝ} (hab : a ≤ b)
    (f : GeneralZetaWeilForm.LogarithmicFormDomain a) :
    (nestedLogarithmicSupport hab f).val = nestedSupport a b f.val := rfl

theorem logarithmicWeilForm_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (f : GeneralZetaWeilForm.LogarithmicFormDomain a) :
    GeneralZetaWeilForm.logarithmicWeilForm b
        (nestedLogarithmicSupport hab f) =
      GeneralZetaWeilForm.logarithmicWeilForm a f -
        ∑ n ∈ GeneralZetaWeilForm.activePrimePowers b \
            GeneralZetaWeilForm.activePrimePowers a,
          GeneralZetaWeilForm.primePowerTerm a f.val n := by
  exact weilForm_nestedSupport hab f.val

end


end RHP2Bridge.NestedSupport
