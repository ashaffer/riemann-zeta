/-
Scaling of the normalized Legendre modes from `[-1,1]` to a symmetric
interval `[-a,a]`.
-/
import LegendreCoefficientTail

namespace LegendreScaled

open Polynomial

/-- Rescaling both the frequency and the coordinate leaves the Fourier
phase unchanged. -/
theorem fourierPhase_mul_div
    (a : ℝ) (ha : a ≠ 0) (z x : ℝ) :
    LegendrePlaneWave.fourierPhase (a * z) (x / a) =
      LegendrePlaneWave.fourierPhase z x := by
  rw [LegendrePlaneWave.fourierPhase, LegendrePlaneWave.fourierPhase]
  congr 1
  have haC : (a : ℂ) ≠ 0 := by exact_mod_cast ha
  push_cast
  field_simp [haC]

/-- The unit-normalized Legendre mode transported from `[-1,1]` to
`[-a,a]`.  The factor `a^{-1/2}` is the unitary dilation factor. -/
noncomputable def scaledNormalizedPlainLegendre
    (a : ℝ) (n : ℕ) : ℝ[X] :=
  C (Real.sqrt a)⁻¹ *
    (LegendreOrthogonality.normalizedPlainLegendre n).comp
      (C a⁻¹ * X)

@[simp] theorem eval_scaledNormalizedPlainLegendre
    (a x : ℝ) (n : ℕ) :
    (scaledNormalizedPlainLegendre a n).eval x =
      (Real.sqrt a)⁻¹ *
        (LegendreOrthogonality.normalizedPlainLegendre n).eval (x / a) := by
  rw [scaledNormalizedPlainLegendre]
  simp only [eval_mul, eval_C, eval_comp, eval_X]
  congr 2
  rw [div_eq_mul_inv]
  ring

/-- Unitary dilation preserves every pair integral. -/
theorem scaledNormalizedPlainLegendre_pair
    (a : ℝ) (ha : 0 < a) (m n : ℕ) :
    LegendreOrthogonality.polynomialPairIntegral
        (scaledNormalizedPlainLegendre a m)
        (scaledNormalizedPlainLegendre a n) (-a) a =
      LegendreOrthogonality.polynomialPairIntegral
        (LegendreOrthogonality.normalizedPlainLegendre m)
        (LegendreOrthogonality.normalizedPlainLegendre n) (-1) 1 := by
  let f : ℝ → ℝ := fun t ↦
    (LegendreOrthogonality.normalizedPlainLegendre m).eval t *
      (LegendreOrthogonality.normalizedPlainLegendre n).eval t
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hsqrt :
      (Real.sqrt a)⁻¹ * (Real.sqrt a)⁻¹ = a⁻¹ := by
    rw [← mul_inv, Real.mul_self_sqrt ha.le]
  rw [LegendreOrthogonality.polynomialPairIntegral,
    LegendreOrthogonality.polynomialPairIntegral]
  calc
    (∫ x in -a..a,
        (scaledNormalizedPlainLegendre a m).eval x *
          (scaledNormalizedPlainLegendre a n).eval x) =
      ∫ x in -a..a, a⁻¹ * f (x / a) := by
        apply intervalIntegral.integral_congr
        intro x _
        change
          (scaledNormalizedPlainLegendre a m).eval x *
              (scaledNormalizedPlainLegendre a n).eval x =
            a⁻¹ * f (x / a)
        rw [eval_scaledNormalizedPlainLegendre,
          eval_scaledNormalizedPlainLegendre]
        dsimp [f]
        rw [← hsqrt]
        ring
    _ = a⁻¹ * ∫ x in -a..a, f (x / a) := by
      rw [intervalIntegral.integral_const_mul]
    _ = a⁻¹ * (a * ∫ t in (-1 : ℝ)..1, f t) := by
      rw [intervalIntegral.integral_comp_div f ha0]
      congr 2
      field_simp
    _ = ∫ t in (-1 : ℝ)..1, f t := by field_simp
    _ = _ := rfl

/-- Exact Kronecker-delta orthonormality on every nondegenerate symmetric
interval. -/
theorem scaledNormalizedPlainLegendre_orthonormal
    (a : ℝ) (ha : 0 < a) (m n : ℕ) :
    LegendreOrthogonality.polynomialPairIntegral
        (scaledNormalizedPlainLegendre a m)
        (scaledNormalizedPlainLegendre a n) (-a) a =
      if m = n then 1 else 0 := by
  rw [scaledNormalizedPlainLegendre_pair a ha m n,
    LegendreOrthogonality.normalizedPlainLegendre_orthonormal]

/-- Exact diagonal unit norm on `[-a,a]`. -/
theorem scaledNormalizedPlainLegendre_pair_self
    (a : ℝ) (ha : 0 < a) (n : ℕ) :
    LegendreOrthogonality.polynomialPairIntegral
        (scaledNormalizedPlainLegendre a n)
        (scaledNormalizedPlainLegendre a n) (-a) a = 1 := by
  simpa using scaledNormalizedPlainLegendre_orthonormal a ha n n

/-- Distinct scaled modes are exactly orthogonal on `[-a,a]`. -/
theorem scaledNormalizedPlainLegendre_pairwise_orthogonal
    (a : ℝ) (ha : 0 < a) {m n : ℕ} (hmn : m ≠ n) :
    LegendreOrthogonality.polynomialPairIntegral
        (scaledNormalizedPlainLegendre a m)
        (scaledNormalizedPlainLegendre a n) (-a) a = 0 := by
  simpa [hmn] using scaledNormalizedPlainLegendre_orthonormal a ha m n

/-! ## Scaled plane-wave coefficients -/

/-- Fourier coefficients transform equivariantly under the unitary
dilation from `[-1,1]` to `[-a,a]`. -/
theorem polyFourierIntegral_scaledNormalizedPlainLegendre
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a n) z (-a) a =
      ((Real.sqrt a : ℝ) : ℂ) *
        LegendrePlaneWave.polyFourierIntegral
          (LegendreOrthogonality.normalizedPlainLegendre n)
          (a * z) (-1) 1 := by
  let P : ℝ[X] := LegendreOrthogonality.normalizedPlainLegendre n
  let g : ℝ → ℂ := fun t ↦
    ((P.eval t : ℝ) : ℂ) *
      LegendrePlaneWave.fourierPhase (a * z) t
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hsqrt0 : Real.sqrt a ≠ 0 := ne_of_gt (Real.sqrt_pos.2 ha)
  have hsqrt_sq : Real.sqrt a * Real.sqrt a = a :=
    Real.mul_self_sqrt ha.le
  have hscaleR : (Real.sqrt a)⁻¹ * a = Real.sqrt a := by
    calc
      (Real.sqrt a)⁻¹ * a =
          (Real.sqrt a)⁻¹ * (Real.sqrt a * Real.sqrt a) := by rw [hsqrt_sq]
      _ = Real.sqrt a := by field_simp
  have hscaleC :
      (((Real.sqrt a)⁻¹ : ℝ) : ℂ) * (a : ℂ) =
        (Real.sqrt a : ℂ) := by
    exact_mod_cast hscaleR
  rw [LegendrePlaneWave.polyFourierIntegral,
    LegendrePlaneWave.polyFourierIntegral]
  change
    (∫ x in -a..a,
      (((scaledNormalizedPlainLegendre a n).eval x : ℝ) : ℂ) *
        LegendrePlaneWave.fourierPhase z x) =
      ((Real.sqrt a : ℝ) : ℂ) *
        ∫ t in (-1 : ℝ)..1,
          ((P.eval t : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase (a * z) t
  calc
    (∫ x in -a..a,
      (((scaledNormalizedPlainLegendre a n).eval x : ℝ) : ℂ) *
        LegendrePlaneWave.fourierPhase z x) =
      ((((Real.sqrt a)⁻¹ : ℝ) : ℂ)) *
        ∫ x in -a..a,
          ((P.eval (x / a) : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z x := by
      rw [← intervalIntegral.integral_const_mul]
      apply intervalIntegral.integral_congr
      intro x _
      change
        (((scaledNormalizedPlainLegendre a n).eval x : ℝ) : ℂ) *
            LegendrePlaneWave.fourierPhase z x =
          (((Real.sqrt a)⁻¹ : ℝ) : ℂ) *
            (((P.eval (x / a) : ℝ) : ℂ) *
              LegendrePlaneWave.fourierPhase z x)
      rw [eval_scaledNormalizedPlainLegendre]
      push_cast
      ring
    _ = ((((Real.sqrt a)⁻¹ : ℝ) : ℂ)) *
        ∫ x in -a..a, g (x / a) := by
      congr 1
      apply intervalIntegral.integral_congr
      intro x _
      dsimp [g]
      rw [fourierPhase_mul_div a ha0 z x]
    _ = ((((Real.sqrt a)⁻¹ : ℝ) : ℂ)) *
        (a • ∫ t in (-1 : ℝ)..1, g t) := by
      rw [intervalIntegral.integral_comp_div g ha0]
      simp [ha0]
    _ = ((Real.sqrt a : ℝ) : ℂ) *
        ∫ t in (-1 : ℝ)..1, g t := by
      rw [Complex.real_smul]
      rw [← mul_assoc, hscaleC]
    _ = _ := rfl

/-- Closed form of the scaled normalized Legendre plane-wave coefficient. -/
theorem polyFourierIntegral_scaledNormalizedPlainLegendre_eq_model
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a n) z (-a) a =
      ((Real.sqrt a : ℝ) : ℂ) *
        (((Real.sqrt ((2 * (n : ℝ) + 1) / 2) : ℝ) : ℂ) *
          (2 * (-Complex.I) ^ n *
            LegendreTail.sphericalJIntegralModel n (a * z))) := by
  rw [polyFourierIntegral_scaledNormalizedPlainLegendre a ha n z,
    LegendreCoefficientTail.polyFourierIntegral_normalizedPlainLegendre]

/-- Squared modulus of a scaled coefficient. -/
theorem norm_polyFourierIntegral_scaledNormalizedPlainLegendre_sq
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    ‖LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a n) z (-a) a‖ ^ 2 =
      2 * a * (2 * (n : ℝ) + 1) *
        ‖LegendreTail.sphericalJIntegralModel n (a * z)‖ ^ 2 := by
  rw [polyFourierIntegral_scaledNormalizedPlainLegendre a ha n z,
    norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg a), mul_pow,
    Real.sq_sqrt ha.le,
    LegendreCoefficientTail.norm_polyFourierIntegral_normalizedPlainLegendre_sq]
  ring

/-- Unitary interval scaling multiplies every squared Fourier coefficient
by the interval scale. -/
theorem norm_polyFourierIntegral_scaled_eq_scale_mul
    (a : ℝ) (ha : 0 < a) (n : ℕ) (z : ℝ) :
    ‖LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a n) z (-a) a‖ ^ 2 =
      a * ‖LegendrePlaneWave.polyFourierIntegral
        (LegendreOrthogonality.normalizedPlainLegendre n)
          (a * z) (-1) 1‖ ^ 2 := by
  rw [polyFourierIntegral_scaledNormalizedPlainLegendre a ha n z,
    norm_mul, Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg a), mul_pow,
    Real.sq_sqrt ha.le]

/-- Complete geometric bound for the squared coefficient tail on
`[-a,a]`.  As on the unit interval, turning this coefficient sum into a
projection residual requires the separate L²/Parseval bridge. -/
theorem scaledNormalizedPlainLegendre_coefficient_tsum_tail_le
    (a : ℝ) (ha : 0 < a) (z : ℝ) (m : ℕ)
    (hq : (a * z) ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦
      ‖LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a (m + n)) z (-a) a‖ ^ 2) ∧
      ∑' n : ℕ,
          ‖LegendrePlaneWave.polyFourierIntegral
            (scaledNormalizedPlainLegendre a (m + n)) z (-a) a‖ ^ 2 ≤
        2 * a * (LegendreTail.doubleFactorialMajorant (a * z) m /
          (1 - (a * z) ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)))) := by
  obtain ⟨hsum, hbound⟩ :=
    LegendreCoefficientTail.normalizedPlainLegendre_coefficient_tsum_tail_le
      (a * z) m hq
  let base : ℕ → ℝ := fun n ↦
    ‖LegendrePlaneWave.polyFourierIntegral
      (LegendreOrthogonality.normalizedPlainLegendre (m + n))
        (a * z) (-1) 1‖ ^ 2
  have hcoeff : ∀ n : ℕ,
      ‖LegendrePlaneWave.polyFourierIntegral
        (scaledNormalizedPlainLegendre a (m + n)) z (-a) a‖ ^ 2 =
        a * base n := by
    intro n
    simpa [base] using
      norm_polyFourierIntegral_scaled_eq_scale_mul a ha (m + n) z
  have hsum' : Summable (fun n ↦ a * base n) := by
    apply hsum.mul_left a
  refine ⟨?_, ?_⟩
  · simpa only [hcoeff] using hsum'
  · rw [show (∑' n : ℕ,
        ‖LegendrePlaneWave.polyFourierIntegral
          (scaledNormalizedPlainLegendre a (m + n)) z (-a) a‖ ^ 2) =
        ∑' n : ℕ, a * base n by
      apply tsum_congr
      exact hcoeff]
    rw [tsum_mul_left]
    have hscaled := mul_le_mul_of_nonneg_left hbound ha.le
    simpa [base, mul_assoc, mul_left_comm, mul_comm] using hscaled

end LegendreScaled
