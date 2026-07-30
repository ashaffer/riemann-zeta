/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedBoundedCertificateCheck
import RHBridge.AutocorrelationPlancherel

/-!
# The truncated zeta Weil form at `L = 7/4`

This file gives the certified multiplier-plus-pole expression a domain and a
zeta-facing name.  At support `L = 7/4` the only prime-power translation in
the truncated explicit-formula ledger is `n = 2`; its Fourier multiplier is
exactly `GlideKernel.p2Omega`.  The two exponential vectors give the pole
term with the normalization used in `THEOREMS.md`.

The domain below is initially stated by integrability of the exact multiplier
energy.  A subsequent bridge should identify it with the more intrinsic
logarithmically weighted domain

`integral |fourier f r|^2 * log (1 + r^2) dr < infinity`.

No explicit-formula theorem or all-support claim is made here.
-/

namespace RHP2Bridge.ZetaWeilForm

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable section

/-- The real interval space `L^2[-7/16,7/16]`, corresponding to support
`L = 7/4`. -/
abbrev P2Space := FullInfP2Endpoint.P2IntervalL2

/-- Squared Plancherel density of the zero-extended interval vector. -/
def fourierEnergy (f : P2Space) (xi : ℝ) : ℝ :=
  ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
    ℝ → ℂ) xi‖ ^ 2

/-- The Plancherel density of every interval `L²` vector is integrable. -/
theorem fourierEnergy_integrable (f : P2Space) :
    MeasureTheory.Integrable (fourierEnergy f)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  have h := (MeasureTheory.Lp.memLp
    (IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f)).integrable_norm_rpow
      (by norm_num) (by norm_num)
  change MeasureTheory.Integrable
    (fun xi ↦ ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
      ℝ → ℂ) xi‖ ^ 2)
    (MeasureTheory.volume : MeasureTheory.Measure ℝ)
  simpa using h

/-- The bounded prime-`2` oscillation is integrable against every Plancherel
density. -/
theorem primeTwoIntegrand_integrable (f : P2Space) :
    MeasureTheory.Integrable
      (fun xi ↦ GlideKernel.p2PrimeAmplitude *
        Real.cos (2 * Real.pi * xi * Real.log 2) * fourierEnergy f xi)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  apply (fourierEnergy_integrable f).bdd_mul
    (c := |GlideKernel.p2PrimeAmplitude|)
  · fun_prop
  · filter_upwards [] with xi
    rw [Real.norm_eq_abs, abs_mul]
    exact mul_le_of_le_one_right (abs_nonneg GlideKernel.p2PrimeAmplitude)
      (Real.abs_cos_le_one _)

/-- Domain of the exact, unbounded `p = 2` multiplier energy. -/
def InP2Domain (f : P2Space) : Prop :=
  MeasureTheory.Integrable
    (fun xi ↦ GlideKernel.p2Omega (2 * Real.pi * xi) *
      ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
        ℝ → ℂ) xi‖ ^ 2)
    (MeasureTheory.volume : MeasureTheory.Measure ℝ)

/-- The archimedean part in ordinary Fourier frequency. -/
def p2ArchimedeanTerm (f : P2Space) : ℝ :=
  ∫ xi, (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
      Real.log Real.pi) * fourierEnergy f xi

/-- The sole prime-power term visible at support `L = 7/4`. -/
def p2PrimeTwoTerm (f : P2Space) : ℝ :=
  ∫ xi, GlideKernel.p2PrimeAmplitude *
    Real.cos (2 * Real.pi * xi * Real.log 2) * fourierEnergy f xi

/-- The prime-`2` contribution written in the time domain as the translated
autocorrelation at `u = log 2`. -/
def p2TimePrimeTwoTerm (f : P2Space) : ℝ :=
  GlideKernel.p2PrimeAmplitude *
    AutocorrelationPlancherel.intervalAutocorrelation
      (7 / 16) (Real.log 2) f

/-- Plancherel identifies the certified prime-frequency integral with the
actual time-domain autocorrelation term. -/
theorem p2PrimeTwoTerm_eq_timeDomain (f : P2Space) :
    p2PrimeTwoTerm f = p2TimePrimeTwoTerm f := by
  unfold p2PrimeTwoTerm p2TimePrimeTwoTerm
  rw [AutocorrelationPlancherel.intervalAutocorrelation_eq_cos_fourier_energy]
  rw [← MeasureTheory.integral_const_mul]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [] with xi
  rw [show 2 * Real.pi * xi * Real.log 2 =
    2 * Real.pi * Real.log 2 * xi by ring]
  simp only [fourierEnergy]
  ring

/-- The rank-two pole contribution. -/
def p2PoleTerm (f : P2Space) : ℝ :=
  inner ℝ f (PoleProjection.polePlusL2 (7 / 16)) *
      inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) +
    inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) *
      inner ℝ f (PoleProjection.polePlusL2 (7 / 16))

/-- Independent archimedean-minus-prime-plus-pole spelling of the truncated
`p = 2` Weil ledger. -/
def p2ExpandedWeilForm (f : P2Space) : ℝ :=
  p2PoleTerm f + p2ArchimedeanTerm f - p2PrimeTwoTerm f

/-- The truncated Weil form with its prime contribution written directly as
the time-domain autocorrelation from `THEOREMS.md`. -/
def p2TimeDomainWeilForm (f : P2Space) : ℝ :=
  p2PoleTerm f + p2ArchimedeanTerm f - p2TimePrimeTwoTerm f

theorem p2TimeDomainWeilForm_eq_p2ExpandedWeilForm (f : P2Space) :
    p2TimeDomainWeilForm f = p2ExpandedWeilForm f := by
  unfold p2TimeDomainWeilForm p2ExpandedWeilForm
  rw [p2PrimeTwoTerm_eq_timeDomain]

/-- The truncated zeta Weil ledger at support `L = 7/4`: the exact
archimedean-minus-`p=2` multiplier energy plus the rank-two pole term. -/
def p2TruncatedZetaWeilForm (f : P2Space) : ℝ :=
  (∫ xi, GlideKernel.p2Omega (2 * Real.pi * xi) *
      ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
        ℝ → ℂ) xi‖ ^ 2) +
    (inner ℝ f (PoleProjection.polePlusL2 (7 / 16)) *
        inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) +
      inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) *
        inner ℝ f (PoleProjection.polePlusL2 (7 / 16)))

/-- On the exact multiplier domain, expanding `p2Omega` recovers the
archimedean-minus-prime-plus-pole ledger term by term. -/
theorem p2ExpandedWeilForm_eq_p2TruncatedZetaWeilForm
    (f : P2Space) (hdom : InP2Domain f) :
    p2ExpandedWeilForm f = p2TruncatedZetaWeilForm f := by
  have hprime := primeTwoIntegrand_integrable f
  have hsplit :
      (fun xi ↦ (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
          Real.log Real.pi) * fourierEnergy f xi) =
        (fun xi ↦ GlideKernel.p2Omega (2 * Real.pi * xi) *
          fourierEnergy f xi) +
        (fun xi ↦ GlideKernel.p2PrimeAmplitude *
          Real.cos (2 * Real.pi * xi * Real.log 2) * fourierEnergy f xi) := by
    funext xi
    simp only [GlideKernel.p2Omega]
    ring_nf
    simp only [Pi.add_apply]
    rw [show Real.pi * xi * Real.log 2 * 2 =
      Real.pi * Real.log 2 * xi * 2 by ring]
    ring
  have harch : MeasureTheory.Integrable
      (fun xi ↦ (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
        Real.log Real.pi) * fourierEnergy f xi)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
    rw [hsplit]
    exact hdom.add hprime
  have hintegral :
      (∫ xi, (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
          Real.log Real.pi) * fourierEnergy f xi) =
        (∫ xi, GlideKernel.p2Omega (2 * Real.pi * xi) * fourierEnergy f xi) +
        ∫ xi, GlideKernel.p2PrimeAmplitude *
          Real.cos (2 * Real.pi * xi * Real.log 2) * fourierEnergy f xi := by
    rw [hsplit]
    exact MeasureTheory.integral_add hdom hprime
  unfold InP2Domain at hdom
  change MeasureTheory.Integrable
    (fun xi ↦ GlideKernel.p2Omega (2 * Real.pi * xi) * fourierEnergy f xi)
    (MeasureTheory.volume : MeasureTheory.Measure ℝ) at hdom
  unfold p2ExpandedWeilForm p2TruncatedZetaWeilForm p2ArchimedeanTerm
    p2PrimeTwoTerm p2PoleTerm
  rw [hintegral]
  simp only [fourierEnergy]
  ring

/-- Kernel-checked strict positivity of the truncated zeta Weil ledger at
`L = 7/4` on its exact multiplier domain. -/
theorem p2TruncatedZetaWeilForm_strict_lower_bound
    (f : P2Space) (hf : f ≠ 0) (hdom : InP2Domain f) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2TruncatedZetaWeilForm f := by
  exact RHP2Bridge.p2_original_integral_lower_bound_of_matrix_containment_no_parity
    f hf hdom
      RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment.1
      RHP2Bridge.P2RoundedBoundedCertificate.p2_canonical_matrix_containment.2

/-- In particular, the ledger is positive on every nonzero vector in its
exact multiplier domain. -/
theorem p2TruncatedZetaWeilForm_pos
    (f : P2Space) (hf : f ≠ 0) (hdom : InP2Domain f) :
    0 < p2TruncatedZetaWeilForm f := by
  have h := p2TruncatedZetaWeilForm_strict_lower_bound f hf hdom
  have hnorm : 0 ≤ ‖f‖ ^ 2 := sq_nonneg ‖f‖
  nlinarith

/-- The same certified bound in the independently expanded
archimedean-minus-prime-plus-pole spelling. -/
theorem p2ExpandedWeilForm_strict_lower_bound
    (f : P2Space) (hf : f ≠ 0) (hdom : InP2Domain f) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ExpandedWeilForm f := by
  rw [p2ExpandedWeilForm_eq_p2TruncatedZetaWeilForm f hdom]
  exact p2TruncatedZetaWeilForm_strict_lower_bound f hf hdom

/-- Certified positivity of the archimedean-plus-pole-minus-autocorrelation
time-domain Weil form at `L = 7/4`. -/
theorem p2TimeDomainWeilForm_strict_lower_bound
    (f : P2Space) (hf : f ≠ 0) (hdom : InP2Domain f) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2TimeDomainWeilForm f := by
  rw [p2TimeDomainWeilForm_eq_p2ExpandedWeilForm]
  exact p2ExpandedWeilForm_strict_lower_bound f hf hdom

end

end RHP2Bridge.ZetaWeilForm
