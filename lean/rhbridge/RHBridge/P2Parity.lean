/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2

/-!
# Parity of the actual clipped p=2 form

This file proves that the canonical clipped p=2 form has no mixed
even/odd Legendre entries.  The Fourier multiplier contribution vanishes
because even Legendre modes have real Fourier coefficients and odd modes
have purely imaginary coefficients.  The symmetrized pole contribution
vanishes by reflection of `exp (x/2)` and `exp (-x/2)`.
-/

namespace RHP2Bridge

open scoped ENNReal InnerProductSpace RealInnerProductSpace

noncomputable section

/-- Reflection law for the real-coefficient shifted Legendre polynomial. -/
theorem shiftedLegendreReal_eval_one_sub (n : ℕ) (x : ℝ) :
    (LegendreRodrigues.shiftedLegendreReal n).eval x =
      (-1 : ℝ) ^ n *
        (LegendreRodrigues.shiftedLegendreReal n).eval (1 - x) := by
  simpa [LegendreRodrigues.shiftedLegendreReal, Polynomial.aeval_def,
    Polynomial.eval₂_eq_eval_map] using
    (Polynomial.shiftedLegendre_eval_symm n x)

/-- The analysis-facing Legendre polynomial has its classical parity. -/
theorem plainLegendre_eval_neg (n : ℕ) (x : ℝ) :
    (LegendreRodrigues.plainLegendre n).eval (-x) =
      (-1 : ℝ) ^ n * (LegendreRodrigues.plainLegendre n).eval x := by
  rw [LegendreRodrigues.plainLegendre, Polynomial.eval_comp,
    Polynomial.eval_comp]
  simp only [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_C,
    Polynomial.eval_X]
  rw [shiftedLegendreReal_eval_one_sub]
  congr 2
  ring

/-- Unit normalization preserves Legendre parity. -/
theorem normalizedPlainLegendre_eval_neg (n : ℕ) (x : ℝ) :
    (LegendreOrthogonality.normalizedPlainLegendre n).eval (-x) =
      (-1 : ℝ) ^ n *
        (LegendreOrthogonality.normalizedPlainLegendre n).eval x := by
  rw [LegendreOrthogonality.normalizedPlainLegendre]
  simp only [Polynomial.eval_mul, Polynomial.eval_C]
  rw [plainLegendre_eval_neg]
  ring

/-- Scaling to `[-a,a]` preserves Legendre parity. -/
theorem scaledNormalizedPlainLegendre_eval_neg (a : ℝ) (n : ℕ) (x : ℝ) :
    (LegendreScaled.scaledNormalizedPlainLegendre a n).eval (-x) =
      (-1 : ℝ) ^ n *
        (LegendreScaled.scaledNormalizedPlainLegendre a n).eval x := by
  rw [LegendreScaled.eval_scaledNormalizedPlainLegendre,
    LegendreScaled.eval_scaledNormalizedPlainLegendre]
  rw [show (-x) / a = -(x / a) by ring,
    normalizedPlainLegendre_eval_neg]
  ring

/-- An odd real function has zero interval integral over a symmetric interval. -/
theorem intervalIntegral_eq_zero_of_odd (f : ℝ → ℝ) (a : ℝ)
    (hodd : ∀ x, f (-x) = -f x) :
    (∫ x in -a..a, f x) = 0 := by
  have hreflect := intervalIntegral.integral_comp_neg
    (a := -a) (b := a) f
  simp only [neg_neg] at hreflect
  have hneg : (∫ x in -a..a, f (-x)) = -∫ x in -a..a, f x := by
    calc
      (∫ x in -a..a, f (-x)) = ∫ x in -a..a, -f x := by
        apply intervalIntegral.integral_congr
        intro x _
        exact hodd x
      _ = -∫ x in -a..a, f x := intervalIntegral.integral_neg
  rw [hneg] at hreflect
  linarith

/-- Real trigonometric form of the Fourier phase. -/
theorem fourierPhase_eq_cos_sub_sin_mul_I (z x : ℝ) :
    LegendrePlaneWave.fourierPhase z x =
      (Real.cos (z * x) : ℂ) - (Real.sin (z * x) : ℂ) * Complex.I := by
  unfold LegendrePlaneWave.fourierPhase
  rw [show (-((z : ℂ) * Complex.I)) * (x : ℂ) =
      ((-(z * x) : ℝ) : ℂ) * Complex.I by push_cast; ring,
    Complex.exp_ofReal_mul_I, Real.cos_neg, Real.sin_neg]
  rw [Complex.ofReal_neg]
  ring

@[simp] theorem fourierPhase_neg_re (z x : ℝ) :
    (LegendrePlaneWave.fourierPhase z (-x)).re =
      (LegendrePlaneWave.fourierPhase z x).re := by
  rw [fourierPhase_eq_cos_sub_sin_mul_I,
    fourierPhase_eq_cos_sub_sin_mul_I]
  simp only [Complex.sub_re, Complex.mul_re, Complex.ofReal_re,
    Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, mul_one,
    sub_zero]
  rw [show z * -x = -(z * x) by ring, Real.cos_neg]

@[simp] theorem fourierPhase_neg_im (z x : ℝ) :
    (LegendrePlaneWave.fourierPhase z (-x)).im =
      -(LegendrePlaneWave.fourierPhase z x).im := by
  rw [fourierPhase_eq_cos_sub_sin_mul_I,
    fourierPhase_eq_cos_sub_sin_mul_I]
  simp only [Complex.sub_im, Complex.mul_im, Complex.ofReal_re,
    Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, mul_one,
    add_zero, zero_sub]
  change -Real.sin (z * -x) = -(-Real.sin (z * x))
  rw [show z * -x = -(z * x) by ring, Real.sin_neg]

/-- An even scaled Legendre mode has a real Fourier coefficient. -/
theorem polyFourierIntegral_even_im
    (a : ℝ) (n : ℕ) (z : ℝ) :
    (LegendrePlaneWave.polyFourierIntegral
      (LegendreScaled.scaledNormalizedPlainLegendre a (2 * n))
      z (-a) a).im = 0 := by
  let p := LegendreScaled.scaledNormalizedPlainLegendre a (2 * n)
  let F : ℝ → ℂ := fun x ↦
    ((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x
  have hF : IntervalIntegrable F MeasureTheory.volume (-a) a := by
    apply Continuous.intervalIntegrable
    dsimp [F, p]
    unfold LegendrePlaneWave.fourierPhase
    fun_prop
  rw [LegendrePlaneWave.polyFourierIntegral]
  change (∫ x in -a..a, F x).im = 0
  change RCLike.im (∫ x in -a..a, F x) = 0
  rw [← intervalIntegral.intervalIntegral_im hF]
  change (∫ x in -a..a,
    (((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x).im) = 0
  apply intervalIntegral_eq_zero_of_odd
  intro x
  simp only [Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im,
    zero_mul, fourierPhase_neg_im]
  have hp : p.eval (-x) = p.eval x := by
    dsimp [p]
    rw [scaledNormalizedPlainLegendre_eval_neg, pow_mul]
    norm_num
  rw [hp]
  ring

/-- An odd scaled Legendre mode has a purely imaginary Fourier coefficient. -/
theorem polyFourierIntegral_odd_re
    (a : ℝ) (n : ℕ) (z : ℝ) :
    (LegendrePlaneWave.polyFourierIntegral
      (LegendreScaled.scaledNormalizedPlainLegendre a (2 * n + 1))
      z (-a) a).re = 0 := by
  let p := LegendreScaled.scaledNormalizedPlainLegendre a (2 * n + 1)
  let F : ℝ → ℂ := fun x ↦
    ((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x
  have hF : IntervalIntegrable F MeasureTheory.volume (-a) a := by
    apply Continuous.intervalIntegrable
    dsimp [F, p]
    unfold LegendrePlaneWave.fourierPhase
    fun_prop
  rw [LegendrePlaneWave.polyFourierIntegral]
  change (∫ x in -a..a, F x).re = 0
  change RCLike.re (∫ x in -a..a, F x) = 0
  rw [← intervalIntegral.intervalIntegral_re hF]
  change (∫ x in -a..a,
    (((p.eval x : ℝ) : ℂ) * LegendrePlaneWave.fourierPhase z x).re) = 0
  apply intervalIntegral_eq_zero_of_odd
  intro x
  simp only [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    zero_mul, sub_zero, fourierPhase_neg_re]
  have hp : p.eval (-x) = -p.eval x := by
    dsimp [p]
    rw [scaledNormalizedPlainLegendre_eval_neg, pow_add, pow_mul]
    norm_num
  rw [hp]
  ring

/-- Even Legendre basis coefficients are real in the genuine interval
Fourier transform. -/
theorem intervalFourierCoeff_even_im
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    (IntervalFourierL2.intervalFourierCoeff a
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n)) z).im = 0 := by
  rw [IntervalFourierL2.intervalFourierCoeff_scaledNormalizedLegendreL2
    a ha]
  exact polyFourierIntegral_even_im a n z

/-- Odd Legendre basis coefficients are purely imaginary in the genuine
interval Fourier transform. -/
theorem intervalFourierCoeff_odd_re
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    (IntervalFourierL2.intervalFourierCoeff a
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n + 1)) z).re = 0 := by
  rw [IntervalFourierL2.intervalFourierCoeff_scaledNormalizedLegendreL2
    a ha]
  exact polyFourierIntegral_odd_re a n z

/-- Even and odd scaled Legendre modes are orthogonal. -/
theorem inner_even_odd_scaledNormalizedLegendreL2
    (a : ℝ) (ha : 0 < a) (i j : ℕ) :
    inner ℝ
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i))
      (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j + 1)) = 0 := by
  rw [LegendreScaledL2.inner_scaledNormalizedLegendreL2 a ha]
  rw [if_neg (by omega)]

/-- Pairing a scaled Legendre basis vector with a pole vector is the
corresponding ordinary interval integral. -/
theorem inner_scaledNormalizedLegendreL2_poleL2_eq
    (a : ℝ) (ha : 0 ≤ a) (n : ℕ) (s : ℝ) :
    inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a n)
        (PoleProjection.poleL2 a s) =
      ∫ x in -a..a,
        Real.exp (s * x / 2) *
          (LegendreScaled.scaledNormalizedPlainLegendre a n).eval x := by
  rw [LegendreScaledL2.scaledNormalizedLegendreL2,
    LegendreScaledL2.polynomialToL2_apply, PoleProjection.poleL2,
    MeasureTheory.ContinuousMap.inner_toLp]
  change (∫ x : Set.Icc (-a) a,
      Real.exp (s * (x : ℝ) / 2) *
        (LegendreScaled.scaledNormalizedPlainLegendre a n).eval (x : ℝ)
      ∂(LegendreScaledL2.intervalMeasure a)) = _
  rw [LegendreScaledL2.intervalMeasure,
    MeasureTheory.integral_subtype_comap
      (s := Set.Icc (-a) a) (μ := MeasureTheory.volume)
      measurableSet_Icc
      (fun x : ℝ ↦ Real.exp (s * x / 2) *
        (LegendreScaled.scaledNormalizedPlainLegendre a n).eval x)]
  rw [intervalIntegral.integral_of_le (by linarith),
    ← MeasureTheory.integral_Icc_eq_integral_Ioc]

/-- Reflection exchanges the two pole vectors on even Legendre modes. -/
theorem inner_even_poleMinus_eq_polePlus
    (a : ℝ) (ha : 0 ≤ a) (n : ℕ) :
    inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n))
        (PoleProjection.poleMinusL2 a) =
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n))
        (PoleProjection.polePlusL2 a) := by
  rw [PoleProjection.poleMinusL2, PoleProjection.polePlusL2,
    inner_scaledNormalizedLegendreL2_poleL2_eq a ha,
    inner_scaledNormalizedLegendreL2_poleL2_eq a ha]
  let p := LegendreScaled.scaledNormalizedPlainLegendre a (2 * n)
  let f : ℝ → ℝ := fun x ↦ Real.exp ((1 : ℝ) * x / 2) * p.eval x
  have hp (x : ℝ) : p.eval (-x) = p.eval x := by
    dsimp [p]
    rw [scaledNormalizedPlainLegendre_eval_neg, pow_mul]
    norm_num
  have hreflect := intervalIntegral.integral_comp_neg
    (a := -a) (b := a) f
  simp only [neg_neg] at hreflect
  calc
    (∫ x in -a..a,
        Real.exp ((-1 : ℝ) * x / 2) * p.eval x) =
        ∫ x in -a..a, f (-x) := by
      apply intervalIntegral.integral_congr
      intro x _
      dsimp [f]
      rw [hp]
      rw [show (1 : ℝ) * -x / 2 = (-1 : ℝ) * x / 2 by ring]
    _ = ∫ x in -a..a, f x := hreflect
    _ = ∫ x in -a..a,
        Real.exp ((1 : ℝ) * x / 2) * p.eval x := by
      apply intervalIntegral.integral_congr
      intro x _
      rfl

/-- Reflection exchanges the two pole vectors with a minus sign on odd
Legendre modes. -/
theorem inner_odd_poleMinus_eq_neg_polePlus
    (a : ℝ) (ha : 0 ≤ a) (n : ℕ) :
    inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n + 1))
        (PoleProjection.poleMinusL2 a) =
      -inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * n + 1))
        (PoleProjection.polePlusL2 a) := by
  rw [PoleProjection.poleMinusL2, PoleProjection.polePlusL2,
    inner_scaledNormalizedLegendreL2_poleL2_eq a ha,
    inner_scaledNormalizedLegendreL2_poleL2_eq a ha]
  let p := LegendreScaled.scaledNormalizedPlainLegendre a (2 * n + 1)
  let f : ℝ → ℝ := fun x ↦ Real.exp ((1 : ℝ) * x / 2) * p.eval x
  let g : ℝ → ℝ := fun x ↦ Real.exp ((-1 : ℝ) * x / 2) * p.eval x
  have hp (x : ℝ) : p.eval (-x) = -p.eval x := by
    dsimp [p]
    rw [scaledNormalizedPlainLegendre_eval_neg, pow_add, pow_mul]
    norm_num
  have hreflect := intervalIntegral.integral_comp_neg
    (a := -a) (b := a) f
  simp only [neg_neg] at hreflect
  have hneg : (∫ x in -a..a, f (-x)) = -∫ x in -a..a, g x := by
    calc
      (∫ x in -a..a, f (-x)) = ∫ x in -a..a, -g x := by
        apply intervalIntegral.integral_congr
        intro x _
        dsimp [f, g]
        rw [hp]
        rw [show (1 : ℝ) * -x / 2 = (-1 : ℝ) * x / 2 by ring]
        ring
      _ = -∫ x in -a..a, g x := intervalIntegral.integral_neg
  change (∫ x in -a..a, g x) = -∫ x in -a..a, f x
  linarith

/-- Pointwise representative of the genuine angular-frequency band map. -/
theorem coeFn_angularFourierBandCLM_ae_eq_intervalFourierCoeff
    (a b : ℝ) (w : LegendreScaledL2.IntervalL2 a) :
    (IntervalZeroExtension.angularFourierBandCLM a b w : ℝ → ℂ) =ᵐ[
      (MeasureTheory.volume : MeasureTheory.Measure ℝ)]
      (Set.Icc (-(b / (2 * Real.pi))) (b / (2 * Real.pi))).indicator
        (fun ξ ↦ IntervalFourierL2.intervalFourierCoeff a w
          (2 * Real.pi * ξ)) := by
  filter_upwards [IntervalZeroExtension.coeFn_restrictToBand
      (b / (2 * Real.pi))
      (IntervalZeroExtension.fourierZeroExtensionL2 a w),
    IntervalZeroExtension.coeFn_fourierZeroExtensionL2_ae_eq_intervalFourierCoeff
      a w] with ξ hband hfourier
  change (IntervalZeroExtension.angularFourierBandL2 a w b : ℝ → ℂ) ξ = _
  rw [IntervalZeroExtension.angularFourierBandL2, hband]
  by_cases hξ : ξ ∈ Set.Icc (-(b / (2 * Real.pi))) (b / (2 * Real.pi))
  · simp only [Set.indicator_of_mem hξ]
    exact hfourier
  · simp only [Set.indicator_of_notMem hξ]

/-- A real scalar times a real Fourier coefficient is real-orthogonal to a
purely imaginary coefficient. -/
theorem real_inner_mul_eq_zero_of_im_re_zero
    (q e o : ℂ) (hq : q.im = 0) (he : e.im = 0) (ho : o.re = 0) :
    (inner ℂ (q * e) o).re = 0 := by
  rw [RCLike.inner_apply', starRingEnd_apply, Complex.star_def]
  rw [Complex.mul_re]
  rw [Complex.conj_re, Complex.conj_im]
  rw [Complex.mul_re, Complex.mul_im]
  rw [hq, he, ho]
  ring

/-- The bounded p=2 multiplier has no mixed even/odd Legendre entry. -/
theorem p2_bandOperator_even_odd_zero (i j : ℕ) :
    BandOperatorBilinear.ofOperator
        (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
          p2OrdinaryBandDefect_aestronglyMeasurable
          ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
        (FullInfP2CanonicalEndpoint.p2BandMap
          (LegendreScaledL2.scaledNormalizedLegendreL2
            (7 / 16) (2 * i)))
        (FullInfP2CanonicalEndpoint.p2BandMap
          (LegendreScaledL2.scaledNormalizedLegendreL2
            (7 / 16) (2 * j + 1))) = 0 := by
  let e := LegendreScaledL2.scaledNormalizedLegendreL2
    (7 / 16) (2 * i)
  let o := LegendreScaledL2.scaledNormalizedLegendreL2
    (7 / 16) (2 * j + 1)
  let fe := FullInfP2CanonicalEndpoint.p2BandMap e
  let fo := FullInfP2CanonicalEndpoint.p2BandMap o
  let T := BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
    p2OrdinaryBandDefect_aestronglyMeasurable
    ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae
  change (inner ℂ (T fe) fo).re = 0
  rw [MeasureTheory.L2.inner_def]
  have hint : MeasureTheory.Integrable (fun ξ : ℝ ↦
      inner ℂ ((T fe : IntervalZeroExtension.FullLineComplexL2) ξ)
        ((fo : IntervalZeroExtension.FullLineComplexL2) ξ)) :=
    MeasureTheory.L2.integrable_inner (T fe) fo
  calc
    (∫ ξ : ℝ, inner ℂ ((T fe : IntervalZeroExtension.FullLineComplexL2) ξ)
        ((fo : IntervalZeroExtension.FullLineComplexL2) ξ)).re =
        ∫ ξ : ℝ,
          (inner ℂ ((T fe : IntervalZeroExtension.FullLineComplexL2) ξ)
            ((fo : IntervalZeroExtension.FullLineComplexL2) ξ)).re := by
      exact integral_re hint |>.symm
    _ = ∫ _ξ : ℝ, 0 := by
      apply MeasureTheory.integral_congr_ae
      filter_upwards [BoundedSymbolMultiplier.coeFn_ofSymbol
          p2OrdinaryBandDefect p2OrdinaryBandDefect_aestronglyMeasurable
          ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae fe,
        coeFn_angularFourierBandCLM_ae_eq_intervalFourierCoeff
          (7 / 16) 50 e,
        coeFn_angularFourierBandCLM_ae_eq_intervalFourierCoeff
          (7 / 16) 50 o,
        p2OrdinaryBandDefect_real_ae] with ξ hmul he ho hqreal
      rw [hmul]
      change (fe : ℝ → ℂ) ξ = _ at he
      change (fo : ℝ → ℂ) ξ = _ at ho
      rw [he, ho]
      by_cases hξ : ξ ∈ Set.Icc
          (-(50 / (2 * Real.pi))) (50 / (2 * Real.pi))
      · simp only [Set.indicator_of_mem hξ]
        have heIm := intervalFourierCoeff_even_im
          (7 / 16) (by norm_num) i (2 * Real.pi * ξ)
        have hoRe := intervalFourierCoeff_odd_re
          (7 / 16) (by norm_num) j (2 * Real.pi * ξ)
        change (IntervalFourierL2.intervalFourierCoeff
          (7 / 16) e (2 * Real.pi * ξ)).im = 0 at heIm
        change (IntervalFourierL2.intervalFourierCoeff
          (7 / 16) o (2 * Real.pi * ξ)).re = 0 at hoRe
        exact real_inner_mul_eq_zero_of_im_re_zero _ _ _ hqreal heIm hoRe
      · simp only [Set.indicator_of_notMem hξ]
        simp only [mul_zero, RCLike.inner_apply', map_zero,
          Complex.zero_re]
    _ = 0 := by simp only [MeasureTheory.integral_zero]

/-- The symmetrized pair of pole vectors has no mixed even/odd Legendre
entry. -/
theorem poleTerm_even_odd_eq_zero
    (a : ℝ) (ha : 0 ≤ a) (i j : ℕ) :
    inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i))
          (PoleProjection.polePlusL2 a) *
        inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j + 1))
          (PoleProjection.poleMinusL2 a) +
      inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * i))
          (PoleProjection.poleMinusL2 a) *
        inner ℝ (LegendreScaledL2.scaledNormalizedLegendreL2 a (2 * j + 1))
          (PoleProjection.polePlusL2 a) = 0 := by
  rw [inner_odd_poleMinus_eq_neg_polePlus a ha,
    inner_even_poleMinus_eq_polePlus a ha]
  ring

/-- The actual clipped p=2 form preserves Legendre parity. -/
theorem p2ClippedForm_even_odd (i j : Fin 24) :
    p2ClippedForm
        (LegendreScaledL2.scaledNormalizedLegendreL2
          (7 / 16) (2 * i.val))
      (LegendreScaledL2.scaledNormalizedLegendreL2
        (7 / 16) (2 * j.val + 1)) = 0 := by
  change FullInfP2CanonicalEndpoint.p2ClippedOperatorForm
      (BoundedSymbolMultiplier.ofSymbol p2OrdinaryBandDefect
        p2OrdinaryBandDefect_aestronglyMeasurable
        ((7447 : ℝ) / 1000) p2OrdinaryBandDefect_bound_ae)
      GlideKernel.p2Alpha
      (LegendreScaledL2.scaledNormalizedLegendreL2
        (7 / 16) (2 * i.val))
      (LegendreScaledL2.scaledNormalizedLegendreL2
        (7 / 16) (2 * j.val + 1)) = 0
  rw [FullInfP2CanonicalEndpoint.p2ClippedOperatorForm_decomp]
  rw [inner_even_odd_scaledNormalizedLegendreL2 (7 / 16) (by norm_num),
    p2_bandOperator_even_odd_zero,
    poleTerm_even_odd_eq_zero (7 / 16) (by norm_num)]
  ring

/-- Endpoint positivity with parity now discharged: only the two certified
matrix-containment statements remain. -/
theorem p2_clipped_endpoint_of_matrix_containment_no_parity
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j)
    {f : FullInfP2Endpoint.P2IntervalL2} (hf : f ≠ 0) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < p2ClippedForm f f := by
  exact p2_clipped_endpoint_of_matrix_containment
    p2ClippedForm_even_odd he ho hf

/-- Original p=2 Fourier-energy lower bound with parity discharged.  Apart
from weighted integrability, only containment of the two actual finite
Legendre matrices remains. -/
theorem p2_original_integral_lower_bound_of_matrix_containment_no_parity
    (f : FullInfP2Endpoint.P2IntervalL2)
    (hf : f ≠ 0)
    (hOriginalIntegrable : MeasureTheory.Integrable
      (fun ξ ↦ GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
          ℝ → ℂ) ξ‖ ^ 2)
      (MeasureTheory.volume : MeasureTheory.Measure ℝ))
    (he : ∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j)
    (ho : ∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 <
      (∫ ξ, GlideKernel.p2Omega (2 * Real.pi * ξ) *
        ‖(IntervalZeroExtension.fourierZeroExtensionL2 (7 / 16) f :
          ℝ → ℂ) ξ‖ ^ 2) +
        (inner ℝ f (PoleProjection.polePlusL2 (7 / 16)) *
            inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) +
          inner ℝ f (PoleProjection.poleMinusL2 (7 / 16)) *
            inner ℝ f (PoleProjection.polePlusL2 (7 / 16))) := by
  exact p2_original_integral_lower_bound_of_matrix_containment
    f hf hOriginalIntegrable p2ClippedForm_even_odd he ho

end

end RHP2Bridge
