/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SuzukiClosedDomainLiterature
import RHBridge.GuinandWeilLiterature

/-!
# Stage 2: weak defect characterization

The completed Suzuki space need not embed into ordinary `L²`; boundary
distribution data can survive completion.  The invariant characterization is
therefore weak: a first-crossing mode annihilates every form-domain variation.
This module synchronizes that one functional in arithmetic, completed-kernel,
and zero-side coordinates.
-/

namespace RHP2Bridge.Stage2DefectCharacterization

open scoped Topology
open GeneralZetaWeilForm SupportDecomposition GuinandWeilFormula
open SuzukiClosedDomainLiterature

noncomputable section

/-- Backward-compatible name for addition in the now-constructed logarithmic
form-domain vector space. -/
def logarithmicAdd {a : ℝ}
    (f g : LogarithmicFormDomain a) : LogarithmicFormDomain a :=
  f + g

@[simp] theorem logarithmicAdd_val {a : ℝ}
    (f g : LogarithmicFormDomain a) :
    (logarithmicAdd f g).val = f.val + g.val := rfl

/-- Polarized symmetric-disk zero sum.  This is the correct unconditional
zero-side object; no termwise convergence or RH square factorization is used. -/
def zeroCrossInDisk (R : ℝ) {a : ℝ}
    (f g : LogarithmicFormDomain a) : ℂ :=
  (zeroSumInDisk R a (f.val + g.val) -
      zeroSumInDisk R a f.val - zeroSumInDisk R a g.val) / 2

private def zeroCrossSummand (a : ℝ)
    (f g : TestSpace a) (ρ : NontrivialZetaZero) : ℂ :=
  (zeroSummand a (f + g) ρ - zeroSummand a f ρ -
    zeroSummand a g ρ) / 2

private theorem zeroCrossSummand_smul
    (a c : ℝ) (f g : TestSpace a) (ρ : NontrivialZetaZero) :
    zeroCrossSummand a f (c • g) ρ =
      c * zeroCrossSummand a f g ρ := by
  simp only [zeroCrossSummand, zeroSummand,
    bilateralLaplace_add, bilateralLaplace_smul]
  ring

private def zeroCrossSumInDisk (R a : ℝ)
    (f g : TestSpace a) : ℂ :=
  ∑ ρ ∈ nontrivialZerosInDisk R, zeroCrossSummand a f g ρ

private theorem zeroCrossSumInDisk_eq (R a : ℝ)
    (f g : TestSpace a) :
    zeroCrossSumInDisk R a f g =
      (zeroSumInDisk R a (f + g) - zeroSumInDisk R a f -
        zeroSumInDisk R a g) / 2 := by
  unfold zeroCrossSumInDisk zeroCrossSummand zeroSumInDisk
  simp_rw [div_eq_mul_inv]
  rw [← Finset.sum_mul]
  simp only [Finset.sum_sub_distrib]

private theorem zeroCrossSumInDisk_smul (R a c : ℝ)
    (f g : TestSpace a) :
    zeroCrossSumInDisk R a f (c • g) =
      c * zeroCrossSumInDisk R a f g := by
  unfold zeroCrossSumInDisk
  simp_rw [zeroCrossSummand_smul]
  rw [Finset.mul_sum]

/-- The finite polarized zero sum is real-linear in its second argument. -/
theorem zeroCrossInDisk_smul (R c : ℝ) {a : ℝ}
    (f g : LogarithmicFormDomain a) :
    zeroCrossInDisk R f (c • g) = c * zeroCrossInDisk R f g := by
  calc
    zeroCrossInDisk R f (c • g) =
        zeroCrossSumInDisk R a f.val (c • g.val) := by
      rw [zeroCrossInDisk, zeroCrossSumInDisk_eq]
      rfl
    _ = c * zeroCrossSumInDisk R a f.val g.val :=
      zeroCrossSumInDisk_smul R a c f.val g.val
    _ = c * zeroCrossInDisk R f g := by
      rw [zeroCrossInDisk, zeroCrossSumInDisk_eq]

/-- The polarized disk exhaustion converges to the closed Weil cross form. -/
theorem zeroCrossInDisk_tendsto_weilCross
    {a : ℝ} (f g : LogarithmicFormDomain a) :
    Filter.Tendsto (fun R : ℝ ↦ zeroCrossInDisk R f g) Filter.atTop
      (𝓝 (weilCross a f.val g.val : ℂ)) := by
  have hfg := GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm
    (logarithmicAdd f g)
  have hf := GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm f
  have hg := GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm g
  have h := ((hfg.sub hf).sub hg).div_const (2 : ℂ)
  simpa only [zeroCrossInDisk, logarithmicAdd_val, logarithmicWeilForm,
    Complex.ofReal_ofNat, Complex.ofReal_sub, Complex.ofReal_div,
    Complex.ofReal_ofNat, weilCross] using h

private theorem zeroSummand_smul (a c : ℝ) (f : TestSpace a)
    (ρ : NontrivialZetaZero) :
    zeroSummand a (c • f) ρ = c ^ 2 * zeroSummand a f ρ := by
  simp only [zeroSummand, bilateralLaplace_smul]
  ring

private theorem zeroSumInDisk_smul (R a c : ℝ) (f : TestSpace a) :
    zeroSumInDisk R a (c • f) = c ^ 2 * zeroSumInDisk R a f := by
  unfold zeroSumInDisk
  simp_rw [zeroSummand_smul]
  rw [Finset.mul_sum]

/-- Quadratic homogeneity of the Weil form on its logarithmic domain, derived
from the finite zero sums and their symmetric-disk limit. -/
theorem weilForm_smul_on_logarithmicDomain {a c : ℝ}
    (f : LogarithmicFormDomain a) :
    weilForm a (c • f.val) = c ^ 2 * weilForm a f.val := by
  have hc := GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm
    (c • f)
  have hf :=
    (GuinandWeilLiterature.logarithmic_zero_disk_limit_eq_weilForm f).const_mul
      (c ^ 2 : ℂ)
  have hf' : Filter.Tendsto
      (fun R : ℝ ↦ zeroSumInDisk R a (c • f.val)) Filter.atTop
        (𝓝 ((c ^ 2 : ℂ) * (weilForm a f.val : ℂ))) := by
    simpa only [zeroSumInDisk_smul, logarithmicWeilForm] using hf
  have heq : (weilForm a (c • f.val) : ℂ) =
      (c ^ 2 : ℂ) * (weilForm a f.val : ℂ) := by
    exact tendsto_nhds_unique
      (by simpa only [logarithmicWeilForm,
        logarithmicFormDomain_smul_val] using hc) hf'
  exact_mod_cast heq

/-- Real-linearity of the polarized Weil cross form on the logarithmic
domain, derived from finite-disk polarization. -/
theorem weilCross_smul_right {a c : ℝ}
    (f g : LogarithmicFormDomain a) :
    weilCross a f.val (c • g.val) = c * weilCross a f.val g.val := by
  have hc := zeroCrossInDisk_tendsto_weilCross f (c • g)
  have hg := (zeroCrossInDisk_tendsto_weilCross f g).const_mul (c : ℂ)
  have hg' : Filter.Tendsto
      (fun R : ℝ ↦ zeroCrossInDisk R f (c • g)) Filter.atTop
        (𝓝 ((c : ℂ) * (weilCross a f.val g.val : ℂ))) := by
    simpa only [zeroCrossInDisk_smul] using hg
  have heq : (weilCross a f.val (c • g.val) : ℂ) =
      (c : ℂ) * (weilCross a f.val g.val : ℂ) := by
    exact tendsto_nhds_unique
      (by simpa only [logarithmicFormDomain_smul_val] using hc) hg'
  exact_mod_cast heq

/-- At a nonnegative window, a zero-energy vector annihilates every
form-domain variation.  This is now a theorem, not a closed-form axiom. -/
theorem firstCrossing_weilCross_eq_zero
    {a : ℝ} (mode : FirstCrossingZeroMode a)
    (g : LogarithmicFormDomain a) :
    weilCross a mode.vector.val g.val = 0 := by
  apply ZeroModeConditions.cross_eq_zero_of_zero_energy_line_nonnegative
    (C := weilCross a mode.vector.val g.val)
    (D := weilForm a g.val)
  intro t
  have hnonneg := mode.window_nonnegative (mode.vector + t • g)
  have hzero : weilForm a mode.vector.val = 0 := by
    simpa only [logarithmicWeilForm] using mode.zero_energy
  simp only [logarithmicWeilForm, logarithmicFormDomain_add_val,
    logarithmicFormDomain_smul_val] at hnonneg
  rw [weilForm_add, weilCross_smul_right,
    weilForm_smul_on_logarithmicDomain] at hnonneg
  rw [hzero] at hnonneg
  nlinarith

/-- Spectral-coordinate radical equation: every polarized symmetric-disk zero
sum tends to zero for a first-crossing mode. -/
theorem zeroCrossInDisk_tendsto_zero
    {a : ℝ} (mode : FirstCrossingZeroMode a)
    (g : LogarithmicFormDomain a) :
    Filter.Tendsto (fun R : ℝ ↦ zeroCrossInDisk R mode.vector g)
      Filter.atTop (𝓝 0) := by
  simpa [firstCrossing_weilCross_eq_zero mode g] using
    zeroCrossInDisk_tendsto_weilCross mode.vector g

/-- Arithmetic-coordinate radical equation. -/
theorem firstCrossing_arithmetic_balance
    {a : ℝ} (mode : FirstCrossingZeroMode a)
    (g : LogarithmicFormDomain a) :
    WeilCrossKernel.poleCross a mode.vector.val g.val +
        WeilCrossKernel.archimedeanCross a mode.vector.val g.val =
      WeilCrossKernel.primeCross a mode.vector.val g.val := by
  exact ZeroModeConditions.pole_add_archimedean_eq_prime_of_weilCross_eq_zero
    (firstCrossing_weilCross_eq_zero mode g)

/-- One parsimonious Stage-2 package retaining the common source mode and all
three synchronized characterizations. -/
structure DefectCharacterization (a shift : ℝ) where
  source : FirstCrossingZeroMode a
  completed : CompletedSuzukiZeroMode a shift
  completed_eq_closedDerivative :
    completed.vector = closedDerivative a shift source.vector
  weak_radical : ∀ g : LogarithmicFormDomain a,
    weilCross a source.vector.val g.val = 0
  arithmetic_balance : ∀ g : LogarithmicFormDomain a,
    WeilCrossKernel.poleCross a source.vector.val g.val +
        WeilCrossKernel.archimedeanCross a source.vector.val g.val =
      WeilCrossKernel.primeCross a source.vector.val g.val
  zero_side_limit : ∀ g : LogarithmicFormDomain a,
    Filter.Tendsto (fun R : ℝ ↦ zeroCrossInDisk R source.vector g)
      Filter.atTop (𝓝 0)

/-- Stage 2 composition from the first-crossing data. -/
noncomputable def characterizeFirstCrossing
    {a shift : ℝ} (hshift : shift < 0)
    (mode : FirstCrossingZeroMode a) :
    DefectCharacterization a shift where
  source := mode
  completed := firstCrossing_to_completedSuzukiZeroMode hshift mode
  completed_eq_closedDerivative := rfl
  weak_radical := firstCrossing_weilCross_eq_zero mode
  arithmetic_balance := firstCrossing_arithmetic_balance mode
  zero_side_limit := zeroCrossInDisk_tendsto_zero mode

/-- Failure of RH produces the complete Stage-2 defect package at some
positive finite support, for every negative completion shift. -/
theorem not_rh_implies_exists_defectCharacterization
    (hnot : ¬ RiemannHypothesis) :
    ∃ a : ℝ, 0 < a ∧ ∀ shift : ℝ, shift < 0 →
      Nonempty (DefectCharacterization a shift) := by
  obtain ⟨a, ha, ⟨mode⟩⟩ :=
    exists_firstCrossingZeroMode_of_not_rh hnot
  exact ⟨a, ha, fun shift hshift ↦
    ⟨characterizeFirstCrossing hshift mode⟩⟩

/-- Parsimonious Stage-2 reduction: excluding the single synchronized defect
package at every positive support suffices for RH. -/
theorem riemannHypothesis_of_no_defectCharacterization
    (hnoDefect : ∀ a : ℝ, 0 < a → ∀ shift : ℝ, shift < 0 →
      IsEmpty (DefectCharacterization a shift)) :
    RiemannHypothesis := by
  by_contra hnot
  obtain ⟨a, ha, hdefect⟩ :=
    not_rh_implies_exists_defectCharacterization hnot
  exact (hnoDefect a ha (-1) (by norm_num)).false
    (hdefect (-1) (by norm_num)).some

end

end RHP2Bridge.Stage2DefectCharacterization
