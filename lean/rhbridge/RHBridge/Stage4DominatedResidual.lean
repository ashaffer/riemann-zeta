/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4CanonicalResidual
import RHBridge.ZetaZeroCountingLiterature
import Mathlib.Analysis.Normed.Group.Tannery

/-!
# Stage 4 residual by dominated convergence over zeta zeros

This replaces the unnecessarily strong uniform-zero-tail condition by the
natural Tannery criterion: pointwise disappearance at every zero and one
summable majorant for the polarized zero summands.
-/

namespace RHP2Bridge.Stage4DominatedResidual

open Filter Topology GeneralZetaWeilForm GuinandWeilFormula
open Stage2DefectCharacterization NestedSupport
open Stage4CanonicalResidual
open ZetaZeroCountingLiterature

/-- The termwise polarization of the Guinand--Weil zero summand. -/
noncomputable def zeroCrossSummand {a : ℝ}
    (f g : LogarithmicFormDomain a) (ρ : NontrivialZetaZero) : ℂ :=
  (zeroSummand a (f.val + g.val) ρ - zeroSummand a f.val ρ -
    zeroSummand a g.val ρ) / 2

theorem mem_nontrivialZerosInDisk_iff (R : ℝ) (ρ : NontrivialZetaZero) :
    ρ ∈ nontrivialZerosInDisk R ↔ ‖ρ.val‖ ≤ R := by
  have hz : ρ.val ∈ riemannZetaZeros := ρ.property.1
  simp [nontrivialZerosInDisk, Metric.mem_closedBall, hz]

/-- Expanding zero disks are cofinal among finite sets of nontrivial zeros. -/
theorem tendsto_nontrivialZerosInDisk_atTop :
    Tendsto nontrivialZerosInDisk atTop atTop := by
  apply tendsto_atTop.2
  intro s
  let R : ℝ := ∑ ρ ∈ s, ‖ρ.val‖
  apply eventually_atTop.2
  refine ⟨R, fun r hr ρ hρ ↦ ?_⟩
  rw [mem_nontrivialZerosInDisk_iff]
  exact (Finset.single_le_sum (fun _ _ ↦ norm_nonneg _) hρ).trans hr

theorem zeroCrossInDisk_eq_sum_zeroCrossSummand {a R : ℝ}
    (f g : LogarithmicFormDomain a) :
    zeroCrossInDisk R f g =
      ∑ ρ ∈ nontrivialZerosInDisk R, zeroCrossSummand f g ρ := by
  simp only [zeroCrossInDisk, zeroSumInDisk, zeroCrossSummand]
  rw [← Finset.sum_sub_distrib, ← Finset.sum_sub_distrib, Finset.sum_div]

/-- Once the polarized series is absolutely summable, its ordinary sum agrees
with the symmetric-disk exhaustion used by Guinand--Weil. -/
theorem zeroCrossInDisk_tendsto_tsum_of_summable {a : ℝ}
    (f g : LogarithmicFormDomain a)
    (hsum : Summable (zeroCrossSummand f g)) :
    Tendsto (fun R ↦ zeroCrossInDisk R f g) atTop
      (𝓝 (∑' ρ, zeroCrossSummand f g ρ)) := by
  have h := hsum.hasSum.comp tendsto_nontrivialZerosInDisk_atTop
  rw [show (fun R ↦ zeroCrossInDisk R f g) =
      fun R ↦ ∑ ρ ∈ nontrivialZerosInDisk R, zeroCrossSummand f g ρ by
        funext R
        exact zeroCrossInDisk_eq_sum_zeroCrossSummand f g]
  convert h using 1 <;> rfl

/-- Absolute Guinand--Weil summability identifies the sum of the polarized
zero summands with the full Weil cross form. -/
theorem tsum_zeroCrossSummand_eq_weilCross {a : ℝ}
    (f g : LogarithmicFormDomain a)
    (hfg : Holds a (f.val + g.val)) (hf : Holds a f.val)
    (hg : Holds a g.val) :
    (∑' ρ : NontrivialZetaZero, zeroCrossSummand f g ρ) =
      (SupportDecomposition.weilCross a f.val g.val : ℂ) := by
  have hsum := ((hfg.1.hasSum.sub hf.1.hasSum).sub hg.1.hasSum).div_const (2 : ℂ)
  rw [show (∑' ρ : NontrivialZetaZero, zeroCrossSummand f g ρ) =
      ((∑' ρ, zeroSummand a (f.val + g.val) ρ) -
        (∑' ρ, zeroSummand a f.val ρ) -
        (∑' ρ, zeroSummand a g.val ρ)) / 2 by
        exact (by simpa [zeroCrossSummand] using hsum.tsum_eq)]
  rw [hfg.2, hf.2, hg.2]
  norm_cast

/-- Identification requiring only the ordinary Guinand--Weil disk formula and
absolute summability of the *polarized* series. -/
theorem tsum_zeroCrossSummand_eq_weilCross_of_summable {a : ℝ}
    (f g : LogarithmicFormDomain a)
    (hsum : Summable (zeroCrossSummand f g)) :
    (∑' ρ : NontrivialZetaZero, zeroCrossSummand f g ρ) =
      (SupportDecomposition.weilCross a f.val g.val : ℂ) := by
  exact tendsto_nhds_unique
    (zeroCrossInDisk_tendsto_tsum_of_summable f g hsum)
    (zeroCrossInDisk_tendsto_weilCross f g)

/-- Polarized summand for a growing-support comparator paired with a fixed
compact test embedded into its current window. -/
noncomputable def movingZeroCrossSummand {a : ℕ → ℝ}
    (f : (n : ℕ) → LogarithmicFormDomain (a n)) {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b)
    (n : ℕ) (ρ : NontrivialZetaZero) : ℂ :=
  zeroCrossSummand (f n) (nestedLogarithmicSupport (hba n) g) ρ

/-- The decisive Stage-4 convergence principle.  Unlike a uniform tail
interchange, this accepts the logarithmically growing majorant furnished by
the zero-free region, provided the fixed test transform makes it summable. -/
theorem movingWeilCross_tendsto_zero_of_dominated_zero_summands
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)} {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b)
    (bound : NontrivialZetaZero → ℝ) (hbound : Summable bound)
    (hpoint : ∀ ρ : NontrivialZetaZero,
      Tendsto (fun n ↦ movingZeroCrossSummand f hba g n ρ) atTop (𝓝 0))
    (hdom : ∀ᶠ n in atTop, ∀ ρ,
      ‖movingZeroCrossSummand f hba g n ρ‖ ≤ bound ρ) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) := by
  have ht := tendsto_tsum_of_dominated_convergence hbound hpoint hdom
  simpa only [tsum_zero] using ht.congr' <| by
    filter_upwards [hdom] with n hn
    exact tsum_zeroCrossSummand_eq_weilCross_of_summable _ _
      (hbound.of_norm_bounded hn)

/-- Concrete zero-counting specialization.  Analytic work on the CCM vector
now has exactly one target: dominate its polarized summand by a test-dependent
constant times `residualHeightWeight`. -/
theorem movingWeilCross_tendsto_zero_of_standard_CCM_majorant
    {a : ℕ → ℝ} {f : (n : ℕ) → LogarithmicFormDomain (a n)} {b : ℝ}
    (hba : ∀ n, b ≤ a n) (g : LogarithmicFormDomain b)
    (C : ℝ)
    (hpoint : ∀ ρ : NontrivialZetaZero,
      Tendsto (fun n ↦ movingZeroCrossSummand f hba g n ρ) atTop (𝓝 0))
    (hdom : ∀ᶠ n in atTop, ∀ ρ,
      ‖movingZeroCrossSummand f hba g n ρ‖ ≤
        C * residualHeightWeight ρ) :
    Tendsto (movingWeilCross f hba g) atTop (𝓝 0) := by
  exact movingWeilCross_tendsto_zero_of_dominated_zero_summands hba g
    (C * residualHeightWeight ·)
    (summable_residualHeightWeight.mul_left C) hpoint hdom

end RHP2Bridge.Stage4DominatedResidual
