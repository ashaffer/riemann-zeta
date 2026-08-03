/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedBoundedCertificateCheck
import RHBridge.AutocorrelationPlancherel
import Glide.DigammaKernelBridge

/-!
# The truncated zeta Weil form at `L = 7/4`

This file gives the certified multiplier-plus-pole expression a domain and a
zeta-facing name.  At support `L = 7/4` the only prime-power translation in
the truncated explicit-formula ledger is `n = 2`; its Fourier multiplier is
exactly `GlideKernel.p2Omega`.  The two exponential vectors give the pole
term with the normalization used in `THEOREMS.md`.

The domain below is stated both by integrability of the exact multiplier
energy and by the more intrinsic logarithmically weighted domain

`integral |fourier f r|^2 * log (1 + r^2) dr < infinity`.

The two domains are proved equivalent below.  No all-support claim is made here.
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

/-- The manuscript's logarithmic form-domain weight, expressed in Mathlib's
ordinary Fourier frequency `xi`, hence angular frequency `2πxi`. -/
def logarithmicWeight (xi : ℝ) : ℝ :=
  Real.log (1 + (2 * Real.pi * xi) ^ 2)

theorem logarithmicWeight_nonneg (xi : ℝ) :
    0 ≤ logarithmicWeight xi := by
  unfold logarithmicWeight
  apply Real.log_nonneg
  nlinarith [sq_nonneg (2 * Real.pi * xi)]

theorem continuous_logarithmicWeight : Continuous logarithmicWeight := by
  unfold logarithmicWeight
  apply Continuous.log
  · fun_prop
  · intro xi
    positivity

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

theorem fourierEnergy_aestronglyMeasurable (f : P2Space) :
    MeasureTheory.AEStronglyMeasurable (fourierEnergy f)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) := by
  exact ((MeasureTheory.Lp.aestronglyMeasurable
    (IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f)).norm.aemeasurable
      |>.pow_const 2).aestronglyMeasurable

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

/-- The intrinsic logarithmically weighted form domain from `THEOREMS.md`. -/
def InLogarithmicDomain (f : P2Space) : Prop :=
  MeasureTheory.Integrable
    (fun xi ↦ logarithmicWeight xi * fourierEnergy f xi)
    (MeasureTheory.volume : MeasureTheory.Measure ℝ)

private theorem scaledLog_le_logarithmicWeight_add (xi : ℝ) :
    Real.log (1 + 4 * (2 * Real.pi * xi) ^ 2) ≤
      logarithmicWeight xi + Real.log 4 := by
  have hx : 0 < 1 + (2 * Real.pi * xi) ^ 2 := by positivity
  have hle : 1 + 4 * (2 * Real.pi * xi) ^ 2 ≤
      4 * (1 + (2 * Real.pi * xi) ^ 2) := by
    nlinarith [sq_nonneg (2 * Real.pi * xi)]
  calc
    _ ≤ Real.log (4 * (1 + (2 * Real.pi * xi) ^ 2)) :=
      Real.log_le_log (by positivity) hle
    _ = logarithmicWeight xi + Real.log 4 := by
      rw [Real.log_mul (by norm_num : (4 : ℝ) ≠ 0) hx.ne']
      unfold logarithmicWeight
      ring

private theorem logarithmicWeight_le_scaledLog (xi : ℝ) :
    logarithmicWeight xi ≤
      Real.log (1 + 4 * (2 * Real.pi * xi) ^ 2) := by
  apply Real.log_le_log
  · positivity
  · nlinarith [sq_nonneg (2 * Real.pi * xi)]

private theorem abs_p2Omega_ordinary_le (xi : ℝ) :
    |GlideKernel.p2Omega (2 * Real.pi * xi)| ≤
      logarithmicWeight xi +
        (Real.log 4 + GlideKernel.p2LogComparisonConstant) := by
  calc
    _ ≤ Real.log (1 + 4 * (2 * Real.pi * xi) ^ 2) +
        GlideKernel.p2LogComparisonConstant :=
      GlideKernel.abs_p2Omega_le_log_add (2 * Real.pi * xi)
    _ ≤ _ := by
      linarith [scaledLog_le_logarithmicWeight_add xi]

private theorem logarithmicWeight_le_abs_p2Omega_ordinary (xi : ℝ) :
    logarithmicWeight xi ≤
      2 * |GlideKernel.p2Omega (2 * Real.pi * xi)| +
        2 * GlideKernel.p2LogComparisonConstant :=
  (logarithmicWeight_le_scaledLog xi).trans
    (GlideKernel.log_le_two_abs_p2Omega_add (2 * Real.pi * xi))

theorem inP2Domain_of_inLogarithmicDomain
    (f : P2Space) (hlog : InLogarithmicDomain f) : InP2Domain f := by
  let C : ℝ := Real.log 4 + GlideKernel.p2LogComparisonConstant
  have hC : 0 ≤ C := by
    dsimp [C]
    exact add_nonneg (Real.log_nonneg (by norm_num))
      GlideKernel.p2LogComparisonConstant_nonneg
  have henergy := fourierEnergy_integrable f
  have hmajorant : MeasureTheory.Integrable
      (fun xi ↦ logarithmicWeight xi * fourierEnergy f xi +
        C * fourierEnergy f xi)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    hlog.add (henergy.const_mul C)
  apply hmajorant.mono'
  · exact (GlideKernel.continuous_p2Omega.comp
      (continuous_const.mul continuous_id)).aestronglyMeasurable.mul
        (fourierEnergy_aestronglyMeasurable f)
  · filter_upwards [] with xi
    have hE : 0 ≤ fourierEnergy f xi := sq_nonneg _
    have hW : 0 ≤ logarithmicWeight xi := logarithmicWeight_nonneg xi
    rw [Real.norm_eq_abs, abs_mul]
    change |GlideKernel.p2Omega (2 * Real.pi * xi)| *
        |fourierEnergy f xi| ≤ _
    rw [abs_of_nonneg hE]
    calc
      |GlideKernel.p2Omega (2 * Real.pi * xi)| * fourierEnergy f xi ≤
          (logarithmicWeight xi + C) * fourierEnergy f xi :=
        mul_le_mul_of_nonneg_right (abs_p2Omega_ordinary_le xi) hE
      _ = logarithmicWeight xi * fourierEnergy f xi +
          C * fourierEnergy f xi := by ring

theorem inLogarithmicDomain_of_inP2Domain
    (f : P2Space) (hdom : InP2Domain f) : InLogarithmicDomain f := by
  let C : ℝ := GlideKernel.p2LogComparisonConstant
  have hC : 0 ≤ C := GlideKernel.p2LogComparisonConstant_nonneg
  have henergy := fourierEnergy_integrable f
  have hmajorant : MeasureTheory.Integrable
      (fun xi ↦ 2 *
          ‖GlideKernel.p2Omega (2 * Real.pi * xi) * fourierEnergy f xi‖ +
        (2 * C) * fourierEnergy f xi)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ) :=
    (hdom.norm.const_mul 2).add (henergy.const_mul (2 * C))
  apply hmajorant.mono'
  · exact (continuous_logarithmicWeight.aestronglyMeasurable.mul
      (fourierEnergy_aestronglyMeasurable f))
  · filter_upwards [] with xi
    have hE : 0 ≤ fourierEnergy f xi := sq_nonneg _
    have hW : 0 ≤ logarithmicWeight xi := logarithmicWeight_nonneg xi
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hW hE),
      Real.norm_eq_abs]
    have homega := logarithmicWeight_le_abs_p2Omega_ordinary xi
    calc
      logarithmicWeight xi * fourierEnergy f xi ≤
          (2 * |GlideKernel.p2Omega (2 * Real.pi * xi)| + 2 * C) *
            fourierEnergy f xi := mul_le_mul_of_nonneg_right homega hE
      _ = 2 * |GlideKernel.p2Omega (2 * Real.pi * xi) * fourierEnergy f xi| +
          2 * C * fourierEnergy f xi := by
        rw [abs_mul, abs_of_nonneg hE]
        ring

theorem inP2Domain_iff_inLogarithmicDomain (f : P2Space) :
    InP2Domain f ↔ InLogarithmicDomain f :=
  ⟨inLogarithmicDomain_of_inP2Domain f,
    inP2Domain_of_inLogarithmicDomain f⟩

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

/-- The certified time-domain Weil bound on the intrinsic logarithmically
weighted form domain. -/
theorem p2TimeDomainWeilForm_strict_lower_bound_on_logarithmicDomain
    (f : P2Space) (hf : f ≠ 0) (hlog : InLogarithmicDomain f) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2TimeDomainWeilForm f := by
  exact p2TimeDomainWeilForm_strict_lower_bound f hf
    (inP2Domain_of_inLogarithmicDomain f hlog)

end

end RHP2Bridge.ZetaWeilForm
