/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2Parity

/-!
# Scalar entry formulas for the canonical p=2 matrices

This file exposes each same-parity entry of the canonical clipped matrix as
the scalar integral that must be enclosed by a numerical certificate.  It is
the analytic interface between `RHP2Bridge.p2ClippedForm` and the exact
rational interval tables in `FullInfClipped48Real`.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable section

private abbrev FullLineComplexL2 :=
  IntervalZeroExtension.FullLineComplexL2

/-- Cross-term version of the bounded-multiplier integral identity. -/
theorem re_inner_ofSymbol_cross_eq_integral
    (q : ℝ → ℂ)
    (hq : MeasureTheory.AEStronglyMeasurable q
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (M : ℝ)
    (hbound : ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      ‖q ξ‖ ≤ M)
    (f g : FullLineComplexL2) :
    (inner ℂ (BoundedSymbolMultiplier.ofSymbol q hq M hbound f) g).re =
      ∫ ξ, (inner ℂ (q ξ * f ξ) (g ξ)).re := by
  rw [MeasureTheory.L2.inner_def]
  calc
    (∫ ξ : ℝ, inner ℂ
        ((BoundedSymbolMultiplier.ofSymbol q hq M hbound f) ξ) (g ξ)).re =
        ∫ ξ : ℝ, (inner ℂ
          ((BoundedSymbolMultiplier.ofSymbol q hq M hbound f) ξ) (g ξ)).re :=
      (integral_re (MeasureTheory.L2.integrable_inner (𝕜 := ℂ)
        (BoundedSymbolMultiplier.ofSymbol q hq M hbound f) g)).symm
    _ = ∫ ξ, (inner ℂ (q ξ * f ξ) (g ξ)).re := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [BoundedSymbolMultiplier.coeFn_ofSymbol q hq M hbound f]
        with ξ hmul
      rw [hmul]

noncomputable abbrev p2LegendreBasis (n : ℕ) :
    FullInfP2Endpoint.P2IntervalL2 :=
  LegendreScaledL2.scaledNormalizedLegendreL2 (7 / 16) n

noncomputable abbrev p2LegendreCoeff (n : ℕ) (r : ℝ) : ℂ :=
  IntervalFourierL2.intervalFourierCoeff (7 / 16) (p2LegendreBasis n) r

/-- Before exploiting parity, a canonical band entry is the real part of a
scalar Fourier-coefficient integral.  Although written over the full line,
`p2OrdinaryBandDefect` vanishes identically off the certified band. -/
theorem p2_bandOperator_basis_eq_full_integral (m n : ℕ) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
          p2OrdinaryBandDefect_aestronglyMeasurable
          ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
        (FullInfP2CanonicalEndpoint.p2BandMap (p2LegendreBasis m))
        (FullInfP2CanonicalEndpoint.p2BandMap (p2LegendreBasis n)) =
      ∫ ξ : ℝ, (inner ℂ
        (p2OrdinaryBandDefect ξ * p2LegendreCoeff m (2 * Real.pi * ξ))
        (p2LegendreCoeff n (2 * Real.pi * ξ))).re := by
  rw [BandOperatorBilinear.ofOperator_apply,
    re_inner_ofSymbol_cross_eq_integral]
  apply MeasureTheory.integral_congr_ae
  filter_upwards [
      coeFn_angularFourierBandCLM_ae_eq_intervalFourierCoeff
        (7 / 16) 50 (p2LegendreBasis m),
      coeFn_angularFourierBandCLM_ae_eq_intervalFourierCoeff
        (7 / 16) 50 (p2LegendreBasis n)] with ξ hm hn
  rw [hm, hn]
  by_cases hξ : ξ ∈ Set.Icc (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi))
  · simp [Set.indicator_of_mem hξ, p2LegendreCoeff]
  · have habs : ¬ |ξ| ≤ 50 / (2 * Real.pi) := by
      intro habs
      exact hξ (abs_le.mp habs)
    simp [Set.indicator_of_notMem hξ, p2OrdinaryBandDefect,
      SymbolQuadraticComparison.exteriorDefect,
      SymbolQuadraticComparison.exteriorClip, habs]

/-- The real scalar angular-frequency integrand for two normalized Legendre
basis vectors. -/
noncomputable def p2AngularBandIntegrand (m n : ℕ) (r : ℝ) : ℝ :=
  (inner ℂ
    (((GlideKernel.p2Omega r - GlideKernel.p2Alpha : ℝ) : ℂ) *
      p2LegendreCoeff m r)
    (p2LegendreCoeff n r)).re

private theorem p2_full_integrand_eq_indicator (m n : ℕ) (ξ : ℝ) :
    (inner ℂ
      (p2OrdinaryBandDefect ξ * p2LegendreCoeff m (2 * Real.pi * ξ))
      (p2LegendreCoeff n (2 * Real.pi * ξ))).re =
      (Set.Icc (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi))).indicator
        (fun t ↦ p2AngularBandIntegrand m n (2 * Real.pi * t)) ξ := by
  by_cases hξ : ξ ∈ Set.Icc (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi))
  · have habs : |ξ| ≤ 50 / (2 * Real.pi) := abs_le.mpr hξ
    simp [Set.indicator_of_mem hξ, p2OrdinaryBandDefect,
      SymbolQuadraticComparison.exteriorDefect,
      SymbolQuadraticComparison.exteriorClip, habs,
      p2AngularBandIntegrand]
  · have habs : ¬ |ξ| ≤ 50 / (2 * Real.pi) := by
      intro habs
      exact hξ (abs_le.mp habs)
    simp [Set.indicator_of_notMem hξ, p2OrdinaryBandDefect,
      SymbolQuadraticComparison.exteriorDefect,
      SymbolQuadraticComparison.exteriorClip, habs]

/-- Exact conversion of a band-operator basis entry to a scalar integral in
the Arb driver's angular-frequency normalization. -/
theorem p2_bandOperator_basis_eq_angular_integral (m n : ℕ) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
          p2OrdinaryBandDefect_aestronglyMeasurable
          ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
        (FullInfP2CanonicalEndpoint.p2BandMap (p2LegendreBasis m))
        (FullInfP2CanonicalEndpoint.p2BandMap (p2LegendreBasis n)) =
      (1 / (2 * Real.pi)) *
        ∫ r in (-50 : ℝ)..50, p2AngularBandIntegrand m n r := by
  rw [p2_bandOperator_basis_eq_full_integral]
  calc
    (∫ ξ : ℝ, (inner ℂ
        (p2OrdinaryBandDefect ξ * p2LegendreCoeff m (2 * Real.pi * ξ))
        (p2LegendreCoeff n (2 * Real.pi * ξ))).re) =
        ∫ ξ : ℝ,
          (Set.Icc (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi))).indicator
            (fun t ↦ p2AngularBandIntegrand m n (2 * Real.pi * t)) ξ := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [] with ξ
      exact p2_full_integrand_eq_indicator m n ξ
    _ = ∫ ξ in Set.Icc (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi)),
          p2AngularBandIntegrand m n (2 * Real.pi * ξ) := by
      rw [MeasureTheory.integral_indicator measurableSet_Icc]
    _ = ∫ ξ in -(50 / (2 * Real.pi))..(50 / (2 * Real.pi)),
          p2AngularBandIntegrand m n (2 * Real.pi * ξ) := by
      rw [intervalIntegral.integral_of_le (by
          have hB : 0 ≤ 50 / (2 * Real.pi) := by positivity
          linarith),
        ← MeasureTheory.integral_Icc_eq_integral_Ioc]
    _ = (1 / (2 * Real.pi)) *
          ∫ r in (-50 : ℝ)..50, p2AngularBandIntegrand m n r := by
      rw [intervalIntegral.integral_comp_mul_left
        (p2AngularBandIntegrand m n) (by positivity : 2 * Real.pi ≠ 0)]
      congr 2 <;> field_simp

/-- Real scalar integrand for an even-even canonical entry. -/
noncomputable def p2EvenBandIntegrand (i j : ℕ) (r : ℝ) : ℝ :=
  (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
    (p2LegendreCoeff (2 * j) r).re * (p2LegendreCoeff (2 * i) r).re

/-- Real scalar integrand for an odd-odd canonical entry. -/
noncomputable def p2OddBandIntegrand (i j : ℕ) (r : ℝ) : ℝ :=
  (GlideKernel.p2Omega r - GlideKernel.p2Alpha) *
    (p2LegendreCoeff (2 * j + 1) r).im *
      (p2LegendreCoeff (2 * i + 1) r).im

theorem p2AngularBandIntegrand_even (i j : ℕ) (r : ℝ) :
    p2AngularBandIntegrand (2 * j) (2 * i) r =
      p2EvenBandIntegrand i j r := by
  have hj := intervalFourierCoeff_even_im
    (7 / 16) (by norm_num) j r
  have hi := intervalFourierCoeff_even_im
    (7 / 16) (by norm_num) i r
  unfold p2AngularBandIntegrand p2EvenBandIntegrand
  rw [RCLike.inner_apply']
  simp only [Complex.mul_re, Complex.mul_im, Complex.conj_re,
    Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im]
  rw [hj, hi]
  ring

theorem p2AngularBandIntegrand_odd (i j : ℕ) (r : ℝ) :
    p2AngularBandIntegrand (2 * j + 1) (2 * i + 1) r =
      p2OddBandIntegrand i j r := by
  have hj := intervalFourierCoeff_odd_re
    (7 / 16) (by norm_num) j r
  have hi := intervalFourierCoeff_odd_re
    (7 / 16) (by norm_num) i r
  unfold p2AngularBandIntegrand p2OddBandIntegrand
  rw [RCLike.inner_apply']
  simp only [Complex.mul_re, Complex.mul_im, Complex.conj_re,
    Complex.conj_im, Complex.ofReal_re, Complex.ofReal_im]
  rw [hj, hi]
  ring

/-- The positive-pole coefficient of the normalized `n`th Legendre mode. -/
noncomputable def p2PoleCoeff (n : ℕ) : ℝ :=
  inner ℝ (p2LegendreBasis n) (PoleProjection.polePlusL2 (7 / 16))

/-- Scalar integral presented to the pole-part enclosure checker. -/
theorem p2PoleCoeff_eq_integral (n : ℕ) :
    p2PoleCoeff n =
      ∫ x in -(7 / 16 : ℝ)..(7 / 16 : ℝ),
        Real.exp (x / 2) *
          (LegendreScaled.scaledNormalizedPlainLegendre (7 / 16) n).eval x := by
  unfold p2PoleCoeff p2LegendreBasis PoleProjection.polePlusL2
  simpa using inner_scaledNormalizedLegendreL2_poleL2_eq
    (7 / 16) (by norm_num) n 1

private theorem p2PoleTerm_even (i j : ℕ) :
    inner ℝ (p2LegendreBasis (2 * j))
          (PoleProjection.polePlusL2 (7 / 16)) *
        inner ℝ (p2LegendreBasis (2 * i))
          (PoleProjection.poleMinusL2 (7 / 16)) +
      inner ℝ (p2LegendreBasis (2 * j))
          (PoleProjection.poleMinusL2 (7 / 16)) *
        inner ℝ (p2LegendreBasis (2 * i))
          (PoleProjection.polePlusL2 (7 / 16)) =
      2 * p2PoleCoeff (2 * j) * p2PoleCoeff (2 * i) := by
  rw [inner_even_poleMinus_eq_polePlus (7 / 16) (by norm_num) i,
    inner_even_poleMinus_eq_polePlus (7 / 16) (by norm_num) j]
  unfold p2PoleCoeff
  ring

private theorem p2PoleTerm_odd (i j : ℕ) :
    inner ℝ (p2LegendreBasis (2 * j + 1))
          (PoleProjection.polePlusL2 (7 / 16)) *
        inner ℝ (p2LegendreBasis (2 * i + 1))
          (PoleProjection.poleMinusL2 (7 / 16)) +
      inner ℝ (p2LegendreBasis (2 * j + 1))
          (PoleProjection.poleMinusL2 (7 / 16)) *
        inner ℝ (p2LegendreBasis (2 * i + 1))
          (PoleProjection.polePlusL2 (7 / 16)) =
      -2 * p2PoleCoeff (2 * j + 1) * p2PoleCoeff (2 * i + 1) := by
  rw [inner_odd_poleMinus_eq_neg_polePlus (7 / 16) (by norm_num) i,
    inner_odd_poleMinus_eq_neg_polePlus (7 / 16) (by norm_num) j]
  unfold p2PoleCoeff
  ring

/-- Exact scalar target for an entry of the canonical even block.  The first
term is the scalar-floor Kronecker term, the second is precisely the angular
band integral used by the external computation, and the last is the exact
rank-two pole contribution after parity simplification. -/
theorem p2EvenMatrix_entry_eq_scalar_integral (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j =
      GlideKernel.p2Alpha * (if i = j then 1 else 0) +
        (1 / (2 * Real.pi)) *
          (∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand i.val j.val r) +
        2 * p2PoleCoeff (2 * j.val) * p2PoleCoeff (2 * i.val) := by
  change FullInfP2CanonicalEndpoint.p2ClippedOperatorForm
      (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
        p2OrdinaryBandDefect_aestronglyMeasurable
        ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
      GlideKernel.p2Alpha
      (p2LegendreBasis (2 * j.val)) (p2LegendreBasis (2 * i.val)) = _
  rw [FullInfP2CanonicalEndpoint.p2ClippedOperatorForm_decomp,
    p2_bandOperator_basis_eq_angular_integral,
    LegendreScaledL2.inner_scaledNormalizedLegendreL2
      (7 / 16) (by norm_num),
    p2PoleTerm_even]
  have hIntegral :
      (∫ r in (-50 : ℝ)..50,
          p2AngularBandIntegrand (2 * j.val) (2 * i.val) r) =
        ∫ r in (-50 : ℝ)..50, p2EvenBandIntegrand i.val j.val r := by
    apply intervalIntegral.integral_congr
    intro r _
    exact p2AngularBandIntegrand_even i.val j.val r
  rw [hIntegral]
  by_cases hij : i = j
  · subst j
    simp
  · have hdeg : 2 * j.val ≠ 2 * i.val := by
      intro h
      apply hij
      apply Fin.ext
      omega
    simp [hij, hdeg]

/-- Exact scalar target for an entry of the canonical odd block. -/
theorem p2OddMatrix_entry_eq_scalar_integral (i j : Fin 24) :
    FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j =
      GlideKernel.p2Alpha * (if i = j then 1 else 0) +
        (1 / (2 * Real.pi)) *
          (∫ r in (-50 : ℝ)..50, p2OddBandIntegrand i.val j.val r) -
        2 * p2PoleCoeff (2 * j.val + 1) * p2PoleCoeff (2 * i.val + 1) := by
  change FullInfP2CanonicalEndpoint.p2ClippedOperatorForm
      (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
        p2OrdinaryBandDefect_aestronglyMeasurable
        ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
      GlideKernel.p2Alpha
      (p2LegendreBasis (2 * j.val + 1))
      (p2LegendreBasis (2 * i.val + 1)) = _
  rw [FullInfP2CanonicalEndpoint.p2ClippedOperatorForm_decomp,
    p2_bandOperator_basis_eq_angular_integral,
    LegendreScaledL2.inner_scaledNormalizedLegendreL2
      (7 / 16) (by norm_num),
    p2PoleTerm_odd]
  have hIntegral :
      (∫ r in (-50 : ℝ)..50,
          p2AngularBandIntegrand (2 * j.val + 1) (2 * i.val + 1) r) =
        ∫ r in (-50 : ℝ)..50, p2OddBandIntegrand i.val j.val r := by
    apply intervalIntegral.integral_congr
    intro r _
    exact p2AngularBandIntegrand_odd i.val j.val r
  rw [hIntegral]
  by_cases hij : i = j
  · subst j
    simp
    ring
  · have hval : j.val ≠ i.val := by
      intro h
      apply hij
      exact Fin.ext h.symm
    simp [hij, hval]
    ring

end

end RHP2Bridge
