/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4FormDomainExtension
import RHBridge.Stage4SamplingLiterature

/-!
# Full logarithmic-domain Stage-4 residual

Weighted global zero-sample convergence of the CCM comparators is converted
into weak-residual convergence against every logarithmic-domain test.
-/

namespace RHP2Bridge.Stage4FullDomainResidual

open Filter Topology GeneralZetaWeilForm
open Stage4CanonicalResidual Stage4SamplingLiterature NestedSupport
open GuinandWeilFormula ZetaZeroCountingLiterature

/-- The explicit global transform estimate produced by the prolate moment and
Poisson--Mellin argument. -/
def HasCCMGlobalZeroBound {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) (rate : ℕ → ℝ) : Prop :=
  (∀ n, 0 ≤ rate n) ∧ Tendsto rate atTop (𝓝 0) ∧
  ∀ n (ρ : NontrivialZetaZero),
    ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ +
      ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ≤
        rate n * (Real.log (2 + |ρ.val.im|) / (1 + |ρ.val.im|))

/-- The exact global analytic conclusion of the prolate moment argument. -/
def WeightedCCMZeroSampleVanishing {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) : Prop :=
  (∀ n, 0 ≤ zeroSampleEnergy (a n) (f n).val) ∧
  Tendsto (fun n ↦ zeroSampleEnergy (a n) (f n).val) atTop (𝓝 0)

/-- The explicit CCM zero bound implies vanishing global sample energy by
Riemann--von Mangoldt summability. -/
theorem weightedCCMZeroSampleVanishing_of_globalZeroBound
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)}
    {rate : ℕ → ℝ} (h : HasCCMGlobalZeroBound f rate) :
    WeightedCCMZeroSampleVanishing f := by
  let term : ℕ → NontrivialZetaZero → ℝ := fun n ρ ↦
    (zeroMultiplicity ρ : ℝ) *
      (‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ ^ 2 +
        ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ^ 2)
  have hterm_nonneg (n : ℕ) (ρ : NontrivialZetaZero) : 0 ≤ term n ρ := by
    dsimp [term]
    positivity
  have hterm (n : ℕ) (ρ : NontrivialZetaZero) :
      term n ρ ≤ rate n ^ 2 * squareSampleHeightWeight ρ := by
    have hm : 0 ≤ (zeroMultiplicity ρ : ℝ) := by positivity
    have hr := h.2.2 n ρ
    have hright : 0 ≤ rate n * (Real.log (2 + |ρ.val.im|) /
        (1 + |ρ.val.im|)) := by
      exact le_trans (by positivity) hr
    have hsquares :
        ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ ^ 2 +
          ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ^ 2 ≤
        (rate n * (Real.log (2 + |ρ.val.im|) /
          (1 + |ρ.val.im|))) ^ 2 := by
      have hab : 0 ≤
          ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ +
            ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ := by positivity
      have hsumSq :
          ‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ ^ 2 +
            ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ^ 2 ≤
          (‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ +
            ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖) ^ 2 := by
        nlinarith [mul_nonneg
          (norm_nonneg (bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)))
          (norm_nonneg (bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)))]
      exact hsumSq.trans ((sq_le_sq₀ hab hright).2 hr)
    dsimp [term, squareSampleHeightWeight]
    calc
      (zeroMultiplicity ρ : ℝ) *
          (‖bilateralLaplace (a n) (f n).val (ρ.val - 1 / 2)‖ ^ 2 +
            ‖bilateralLaplace (a n) (f n).val (1 / 2 - ρ.val)‖ ^ 2) ≤
          (zeroMultiplicity ρ : ℝ) *
            (rate n * (Real.log (2 + |ρ.val.im|) /
              (1 + |ρ.val.im|))) ^ 2 :=
        mul_le_mul_of_nonneg_left hsquares hm
      _ = rate n ^ 2 * ((zeroMultiplicity ρ : ℝ) *
          (Real.log (2 + |ρ.val.im|) ^ 2 /
            (1 + |ρ.val.im|) ^ 2)) := by
        have hden : 1 + |ρ.val.im| ≠ 0 := by positivity
        field_simp
  have hsum (n : ℕ) : Summable (term n) :=
    (summable_squareSampleHeightWeight.mul_left (rate n ^ 2)).of_nonneg_of_le
      (hterm_nonneg n) (hterm n)
  have henergy (n : ℕ) :
      zeroSampleEnergy (a n) (f n).val = ∑' ρ, term n ρ := rfl
  have hupper (n : ℕ) :
      zeroSampleEnergy (a n) (f n).val ≤
        rate n ^ 2 * ∑' ρ, squareSampleHeightWeight ρ := by
    rw [henergy]
    rw [← tsum_mul_left]
    exact Summable.tsum_le_tsum (hterm n) (hsum n)
      (summable_squareSampleHeightWeight.mul_left (rate n ^ 2))
  refine ⟨fun n ↦ ?_, ?_⟩
  · rw [henergy]
    exact tsum_nonneg (hterm_nonneg n)
  · have hr2 : Tendsto (fun n ↦ rate n ^ 2) atTop (𝓝 0) := by
      simpa using h.2.1.pow 2
    have hu : Tendsto
        (fun n ↦ rate n ^ 2 * ∑' ρ, squareSampleHeightWeight ρ)
        atTop (𝓝 0) := by
      simpa using hr2.mul_const (∑' ρ, squareSampleHeightWeight ρ)
    apply squeeze_zero'
    · filter_upwards [] with n
      rw [henergy]
      exact tsum_nonneg (hterm_nonneg n)
    · filter_upwards [] with n
      exact hupper n
    · exact hu

/-- Completion of Stage 4: vanishing global CCM zero-sample energy forces the
moving-support Weil residual to vanish against the full logarithmic form
domain, not merely its smooth core. -/
theorem movingWeilCross_tendsto_zero_on_full_logarithmicDomain
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)}
    (hzero : WeightedCCMZeroSampleVanishing f) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) := by
  have hEg_nonneg : 0 ≤ zeroSampleEnergy b g.val := by
    obtain ⟨C, _, hC⟩ := zeroSampleEnergy_le_logarithmicGraphNormSq b
    exact (hC g).1
  have hsqrt : Tendsto
      (fun n ↦ Real.sqrt (zeroSampleEnergy (a n) (f n).val) *
        Real.sqrt (zeroSampleEnergy b g.val)) atTop (𝓝 0) := by
    have hs := (Real.continuous_sqrt.tendsto 0).comp hzero.2
    simpa using hs.mul_const (Real.sqrt (zeroSampleEnergy b g.val))
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ := (Metric.tendsto_atTop.mp hsqrt) ε hε
  refine ⟨N, fun n hn ↦ ?_⟩
  have hbound := weilCross_abs_le_zeroSampleEnergy
    (f n) (nestedLogarithmicSupport (hba n) g)
  rw [zeroSampleEnergy_nestedLogarithmicSupport (hba n) g] at hbound
  have hsmall := hN n hn
  rw [Real.dist_eq, sub_zero, abs_of_nonneg
    (mul_nonneg (Real.sqrt_nonneg _) (Real.sqrt_nonneg _))] at hsmall
  change dist
    (↑(SupportDecomposition.weilCross (a n) (f n).val
      (nestedLogarithmicSupport (hba n) g).val) : ℂ) 0 < ε
  rw [dist_zero_right, Complex.norm_real, Real.norm_eq_abs]
  exact hbound.trans_lt hsmall

/-- End-to-end Stage-4 theorem from the explicit prolate--Mellin zero bound. -/
theorem movingWeilCross_tendsto_zero_of_CCM_globalZeroBound
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)}
    {rate : ℕ → ℝ} (hglobal : HasCCMGlobalZeroBound f rate) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) :=
  movingWeilCross_tendsto_zero_on_full_logarithmicDomain
    (weightedCCMZeroSampleVanishing_of_globalZeroBound hglobal) hba g

end RHP2Bridge.Stage4FullDomainResidual
