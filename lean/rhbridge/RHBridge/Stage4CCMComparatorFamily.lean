/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage4ProlateMellinCertificate

/-!
# Canonical moving-support CCM comparator and regularization

The sharp CCM vector is kept distinct from its smooth, moment-corrected
regularization.  The Mellin certificate applies to the regularized family;
logarithmic sampling transfers its vanishing zero energy back to the sharp
family.
-/

namespace RHP2Bridge.Stage4CCMComparatorFamily

open Filter Topology GeneralZetaWeilForm
open Stage4CanonicalResidual Stage4FullDomainResidual NestedSupport
open Stage4ProlateMellinCertificate
open Stage4SamplingLiterature

structure CertifiedCCMComparatorFamily where
  supportRadius : ℕ → ℝ
  /-- The original sharply truncated CCM vectors. -/
  comparator : (n : ℕ) → LogarithmicFormDomain (supportRadius n)
  /-- Smooth flat-cutoff and moment-corrected vectors. -/
  regularized : (n : ℕ) → LogarithmicFormDomain (supportRadius n)
  support_cofinal : Tendsto supportRadius atTop atTop
  prolate_mellin : ProlateMellinTailCertificate regularized
  regularizationError : ℕ → ℝ
  regularizationError_nonneg : ∀ n, 0 ≤ regularizationError n
  regularizationError_tendsto_zero :
    Tendsto regularizationError atTop (𝓝 0)
  /-- Sampling consequence of logarithmic-graph convergence of the
  regularization to the sharp vector. -/
  sharp_zeroSampleEnergy_le : ∀ n,
    zeroSampleEnergy (supportRadius n) (comparator n).val ≤
      2 * zeroSampleEnergy (supportRadius n) (regularized n).val +
        regularizationError n

/-- The regularized Mellin bound and the logarithmic-graph transfer imply
global zero-sample convergence for the original sharp CCM vectors. -/
theorem sharp_weightedZeroSampleVanishing
    (K : CertifiedCCMComparatorFamily) :
    WeightedCCMZeroSampleVanishing K.comparator := by
  obtain ⟨rate, hrate⟩ := hasCCMGlobalZeroBound K.prolate_mellin
  have hreg : WeightedCCMZeroSampleVanishing K.regularized :=
    weightedCCMZeroSampleVanishing_of_globalZeroBound hrate
  refine ⟨?_, ?_⟩
  · intro n
    obtain ⟨C, _, hC⟩ :=
      zeroSampleEnergy_le_logarithmicGraphNormSq (K.supportRadius n)
    exact (hC (K.comparator n)).1
  · have hupper : Tendsto
        (fun n ↦ 2 * zeroSampleEnergy (K.supportRadius n)
          (K.regularized n).val + K.regularizationError n)
        atTop (𝓝 0) := by
      convert (hreg.2.const_mul 2).add K.regularizationError_tendsto_zero
        using 1 <;> simp
    apply squeeze_zero'
    · filter_upwards [] with n
      obtain ⟨C, _, hC⟩ :=
        zeroSampleEnergy_le_logarithmicGraphNormSq (K.supportRadius n)
      exact (hC (K.comparator n)).1
    · filter_upwards [] with n
      exact K.sharp_zeroSampleEnergy_le n
    · exact hupper

/-- Every fixed logarithmic test window is eventually contained in the CCM
windows, and on that tail the full-domain Weil residual tends to zero. -/
theorem full_logarithmic_residual
    (K : CertifiedCCMComparatorFamily) (b : ℝ)
    (g : LogarithmicFormDomain b) :
    ∃ N : ℕ, ∃ hba : ∀ n, b ≤ K.supportRadius (N + n),
      Tendsto
        (movingWeilCross (fun n ↦ K.comparator (N + n)) hba g)
        atTop (𝓝 0) := by
  obtain ⟨N, hN⟩ := eventually_atTop.1 (K.support_cofinal.eventually (eventually_ge_atTop b))
  have hba : ∀ n, b ≤ K.supportRadius (N + n) := fun n ↦ hN (N + n) (Nat.le_add_right N n)
  refine ⟨N, hba, ?_⟩
  have hsharp := sharp_weightedZeroSampleVanishing K
  have hshift : WeightedCCMZeroSampleVanishing
      (fun n ↦ K.comparator (N + n)) := by
    refine ⟨fun n ↦ hsharp.1 (N + n), ?_⟩
    have ht := (tendsto_add_atTop_iff_nat N).2 hsharp.2
    convert ht using 1
    funext n
    rw [Nat.add_comm]
  exact movingWeilCross_tendsto_zero_on_full_logarithmicDomain hshift hba g

end RHP2Bridge.Stage4CCMComparatorFamily
