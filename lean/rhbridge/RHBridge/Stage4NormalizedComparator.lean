/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4CCMComparatorFamily

/-!
# Normalized Stage-4 comparator energies

This file records the conclusion available after normalizing a certified CCM
comparator family.  Vanishing zero-sample energy forces the diagonal Weil
quadratic values, and hence the Rayleigh values of the normalized vectors, to
tend to zero.  The conclusion is only a failure of a positive uniform
coercivity bound along this family; it is not a Weyl-sequence theorem and has
no direct Riemann-hypothesis conclusion.
-/

namespace RHP2Bridge.Stage4NormalizedComparator

open Filter Topology GeneralZetaWeilForm SupportDecomposition
open Stage4CCMComparatorFamily Stage4SamplingLiterature

noncomputable section

/-- Doubling an interval vector quadruples every weighted integral of its
Fourier-energy density. -/
private theorem integral_weight_fourierEnergy_add_self
    (a : ℝ) (f : TestSpace a) (weight : ℝ → ℝ) :
    (∫ xi, weight xi * fourierEnergy a (f + f) xi) =
      4 * ∫ xi, weight xi * fourierEnergy a f xi := by
  let F := IntervalZeroExtension.fourierZeroExtensionL2 a f
  have hfourier :
      IntervalZeroExtension.fourierZeroExtensionL2 a (f + f) = F + F := by
    dsimp [F]
    rw [IntervalZeroExtension.fourierZeroExtensionL2,
      IntervalZeroExtension.zeroExtension_add,
      FourierAdd.fourier_add]
    rfl
  have hcoe :
      (IntervalZeroExtension.fourierZeroExtensionL2 a (f + f) : ℝ → ℂ) =ᵐ[
        (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
        fun xi ↦ (F : ℝ → ℂ) xi + (F : ℝ → ℂ) xi := by
    rw [hfourier]
    exact MeasureTheory.Lp.coeFn_add F F
  calc
    (∫ xi, weight xi * fourierEnergy a (f + f) xi) =
        ∫ xi, 4 * (weight xi * fourierEnergy a f xi) := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [hcoe] with xi hxi
      simp only [fourierEnergy]
      rw [hxi]
      have hnorm :
          ‖(F : ℝ → ℂ) xi + (F : ℝ → ℂ) xi‖ =
            2 * ‖(F : ℝ → ℂ) xi‖ := by
        rw [← two_mul, norm_mul]
        norm_num
      rw [hnorm]
      ring
    _ = 4 * ∫ xi, weight xi * fourierEnergy a f xi := by
      rw [MeasureTheory.integral_const_mul]

/-- Self-polarization recovers the Weil quadratic form. -/
theorem weilCross_self_eq_weilForm (a : ℝ) (f : TestSpace a) :
    weilCross a f f = weilForm a f := by
  have hpole : poleTerm a (f + f) = 4 * poleTerm a f := by
    simp only [poleTerm, inner_add_left]
    ring
  have harch : archimedeanTerm a (f + f) = 4 * archimedeanTerm a f := by
    exact integral_weight_fourierEnergy_add_self a f
      (fun xi ↦ GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
        Real.log Real.pi)
  have hauto (u : ℝ) :
      AutocorrelationPlancherel.intervalAutocorrelation a u (f + f) =
        4 * AutocorrelationPlancherel.intervalAutocorrelation a u f := by
    rw [AutocorrelationPlancherel.intervalAutocorrelation_eq_cos_fourier_energy,
      AutocorrelationPlancherel.intervalAutocorrelation_eq_cos_fourier_energy]
    exact integral_weight_fourierEnergy_add_self a f
      (fun xi ↦ Real.cos (2 * Real.pi * u * xi))
  have hprimePower (n : ℕ) :
      primePowerTerm a (f + f) n = 4 * primePowerTerm a f n := by
    simp only [primePowerTerm, hauto]
    ring
  have hprime : primeTerm a (f + f) = 4 * primeTerm a f := by
    simp only [primeTerm, hprimePower, Finset.mul_sum]
  unfold weilCross
  rw [show weilForm a (f + f) = 4 * weilForm a f by
    simp only [weilForm, hpole, harch, hprime]
    ring]
  ring

/-- A certified CCM family whose sharp comparators have unit `L²` norm. -/
structure NormalizedCertifiedCCMComparatorFamily extends
    CertifiedCCMComparatorFamily where
  comparator_norm_one : ∀ n, ‖(comparator n).val‖ = 1

/-- Unit normalization in particular makes every comparator nonzero. -/
theorem comparator_ne_zero (K : NormalizedCertifiedCCMComparatorFamily)
    (n : ℕ) : (K.comparator n).val ≠ 0 := by
  intro hzero
  have hnorm := K.comparator_norm_one n
  rw [hzero, norm_zero] at hnorm
  norm_num at hnorm

/-- Rayleigh value of the sharp comparator. -/
def comparatorRayleighValue (K : NormalizedCertifiedCCMComparatorFamily)
    (n : ℕ) : ℝ :=
  weilForm (K.supportRadius n) (K.comparator n).val /
    ‖(K.comparator n).val‖ ^ 2

@[simp] theorem comparatorRayleighValue_eq_weilForm
    (K : NormalizedCertifiedCCMComparatorFamily) (n : ℕ) :
    comparatorRayleighValue K n =
      weilForm (K.supportRadius n) (K.comparator n).val := by
  rw [comparatorRayleighValue, K.comparator_norm_one]
  norm_num

/-- The diagonal Weil values of a certified comparator family tend to zero.
This conclusion itself does not require normalization. -/
theorem comparator_weilForm_tendsto_zero
    (K : CertifiedCCMComparatorFamily) :
    Tendsto (fun n ↦ weilForm (K.supportRadius n) (K.comparator n).val)
      atTop (𝓝 0) := by
  have hsample := sharp_weightedZeroSampleVanishing K
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N, hN⟩ := (Metric.tendsto_atTop.mp hsample.2) ε hε
  refine ⟨N, fun n hn ↦ ?_⟩
  have hnonneg := hsample.1 n
  have hsmall :
      zeroSampleEnergy (K.supportRadius n) (K.comparator n).val < ε := by
    have := hN n hn
    simpa [Real.dist_eq, abs_of_nonneg hnonneg] using this
  have hbound := weilCross_abs_le_zeroSampleEnergy (K.comparator n) (K.comparator n)
  rw [Real.mul_self_sqrt hnonneg, weilCross_self_eq_weilForm] at hbound
  rw [Real.dist_eq, sub_zero]
  exact hbound.trans_lt hsmall

/-- Unit normalization converts the vanishing quadratic values into vanishing
Rayleigh values. -/
theorem comparatorRayleighValue_tendsto_zero
    (K : NormalizedCertifiedCCMComparatorFamily) :
    Tendsto (comparatorRayleighValue K) atTop (𝓝 0) := by
  change Tendsto (fun n ↦ comparatorRayleighValue K n) atTop (𝓝 0)
  simpa only [comparatorRayleighValue_eq_weilForm] using
    comparator_weilForm_tendsto_zero K.toCertifiedCCMComparatorFamily

/-- Consequently this normalized family cannot obey any strictly positive
uniform lower coercivity estimate.  This is weaker than producing a Weyl
sequence: no operator-domain or residual-norm assertion is made. -/
theorem not_uniformly_coercive_on_comparators
    (K : NormalizedCertifiedCCMComparatorFamily) {gamma : ℝ}
    (hgamma : 0 < gamma) :
    ¬ ∀ n, gamma * ‖(K.comparator n).val‖ ^ 2 ≤
      weilForm (K.supportRadius n) (K.comparator n).val := by
  intro hcoercive
  have hlimit := comparator_weilForm_tendsto_zero
    K.toCertifiedCCMComparatorFamily
  have heventually : ∀ᶠ n in atTop,
      weilForm (K.supportRadius n) (K.comparator n).val < gamma :=
    (tendsto_order.1 hlimit).2 gamma hgamma
  obtain ⟨n, hn⟩ := heventually.exists
  have hlower := hcoercive n
  rw [K.comparator_norm_one n] at hlower
  norm_num at hlower
  exact (not_lt_of_ge hlower) hn

end

end RHP2Bridge.Stage4NormalizedComparator
