/-
An analysis-facing all-degree Legendre family obtained from mathlib's
integer shifted Legendre polynomials, together with its unshifted Rodrigues
formula.
-/
import LegendrePlaneWave

namespace LegendreRodrigues

open Polynomial

/-- Iterated chain rule for composition with an affine polynomial. -/
theorem iterate_derivative_comp_affine (p : ℝ[X]) (a b : ℝ) (n : ℕ) :
    (Polynomial.derivative^[n])
        (p.comp (C a * X + C b)) =
      C (a ^ n) *
        ((Polynomial.derivative^[n]) p).comp (C a * X + C b) := by
  induction n generalizing p with
  | zero => simp
  | succ n ih =>
      rw [Function.iterate_succ_apply']
      rw [ih]
      simp only [Polynomial.derivative_mul, Polynomial.derivative_C,
        zero_mul, zero_add, Polynomial.derivative_comp]
      rw [Function.iterate_succ_apply']
      simp
      ring

/-- Mathlib's shifted Legendre polynomial, with coefficients mapped to
`ℝ`. -/
noncomputable def shiftedLegendreReal (n : ℕ) : ℝ[X] :=
  (Polynomial.shiftedLegendre n).map (Int.castRingHom ℝ)

/-- The analysis-facing unshifted Legendre polynomial
`Pₙ(X) = shiftedLegendre n ((1-X)/2)`. -/
noncomputable def plainLegendre (n : ℕ) : ℝ[X] :=
  (shiftedLegendreReal n).comp
    (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ))

/-- Rodrigues' formula for the real-coefficient shifted family. -/
theorem factorial_mul_shiftedLegendreReal_eq (n : ℕ) :
    C (n.factorial : ℝ) * shiftedLegendreReal n =
      (Polynomial.derivative^[n])
        (X ^ n * (1 - (X : ℝ[X])) ^ n) := by
  have h := congrArg (Polynomial.map (Int.castRingHom ℝ))
    (Polynomial.factorial_mul_shiftedLegendre_eq n)
  rw [← Polynomial.iterate_derivative_map] at h
  simpa [shiftedLegendreReal] using h

/-- The shifted Rodrigues weight becomes a constant multiple of
`(1-X²)^n` under the affine unshifting map. -/
theorem shiftedWeight_comp_unshift (n : ℕ) :
    (X ^ n * (1 - (X : ℝ[X])) ^ n).comp
        (C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)) =
      C ((1 / 4 : ℝ) ^ n) * LegendrePlaneWave.rodriguesWeight n := by
  simp only [Polynomial.mul_comp, Polynomial.pow_comp, Polynomial.X_comp,
    Polynomial.sub_comp, Polynomial.one_comp]
  rw [← mul_pow]
  simp only [LegendrePlaneWave.rodriguesWeight, Polynomial.C_pow]
  rw [← mul_pow]
  congr 1
  have hneg : C (-(1 / 2 : ℝ)) = -C (1 / 2 : ℝ) := by
    rw [map_neg]
  have hsq : C (1 / 2 : ℝ) ^ 2 = C (1 / 4 : ℝ) := by
    rw [← Polynomial.C_pow]
    norm_num
  have hlinear : C (1 / 2 : ℝ) =
      2 * C (1 / 2 : ℝ) ^ 2 := by
    rw [hsq]
    rw [← Polynomial.C_ofNat (R := ℝ) 2, ← Polynomial.C_mul]
    norm_num
  rw [hneg]
  calc
    _ = C (1 / 2 : ℝ) ^ 2 * (1 - X ^ 2) := by
      linear_combination (1 - X) * hlinear
    _ = _ := by rw [hsq]

/-- The direct output of combining shifted Rodrigues with the affine chain
rule.  The next theorem clears the harmless powers of two. -/
theorem scaled_rodrigues_plainLegendre (n : ℕ) :
    C ((1 / 4 : ℝ) ^ n) *
        (Polynomial.derivative^[n])
          (LegendrePlaneWave.rodriguesWeight n) =
      C ((-(1 / 2 : ℝ)) ^ n) *
        (C (n.factorial : ℝ) * plainLegendre n) := by
  let q : ℝ[X] := C (-(1 / 2 : ℝ)) * X + C (1 / 2 : ℝ)
  let f : ℝ[X] := X ^ n * (1 - X) ^ n
  have hcomp := congrArg (fun p : ℝ[X] ↦ p.comp q)
    (factorial_mul_shiftedLegendreReal_eq n)
  have hcomp' :
      C (n.factorial : ℝ) * plainLegendre n =
        ((Polynomial.derivative^[n]) f).comp q := by
    simpa [q, f, plainLegendre] using hcomp
  have hchain := iterate_derivative_comp_affine f
    (-(1 / 2 : ℝ)) (1 / 2 : ℝ) n
  rw [show f.comp q =
      C ((1 / 4 : ℝ) ^ n) *
        LegendrePlaneWave.rodriguesWeight n by
        simpa [f, q] using shiftedWeight_comp_unshift n,
      Polynomial.iterate_derivative_C_mul, ← hcomp'] at hchain
  exact hchain

/-- The standard unshifted Rodrigues identity, valid in every degree for the
analysis-facing Legendre family derived from mathlib's independent integer
polynomials. -/
theorem rodrigues_plainLegendre (n : ℕ) :
    C ((2 : ℝ) ^ n * (n.factorial : ℝ)) * plainLegendre n =
      C ((-1 : ℝ) ^ n) *
        (Polynomial.derivative^[n])
          (LegendrePlaneWave.rodriguesWeight n) := by
  let D : ℝ[X] :=
    (Polynomial.derivative^[n])
      (LegendrePlaneWave.rodriguesWeight n)
  let P : ℝ[X] := plainLegendre n
  have h := scaled_rodrigues_plainLegendre n
  change C ((1 / 4 : ℝ) ^ n) * D =
    C ((-(1 / 2 : ℝ)) ^ n) *
      (C (n.factorial : ℝ) * P) at h
  have hA : (4 : ℝ) ^ n * (1 / 4 : ℝ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  have hB : (4 : ℝ) ^ n * (-(1 / 2 : ℝ)) ^ n = (-2 : ℝ) ^ n := by
    rw [← mul_pow]
    norm_num
  have hD : D =
      C ((-2 : ℝ) ^ n) * (C (n.factorial : ℝ) * P) := by
    calc
      D = C ((4 : ℝ) ^ n * (1 / 4 : ℝ) ^ n) * D := by
        rw [hA]
        simp
      _ = C ((4 : ℝ) ^ n) * (C ((1 / 4 : ℝ) ^ n) * D) := by
        rw [Polynomial.C_mul]
        ring
      _ = C ((4 : ℝ) ^ n) *
          (C ((-(1 / 2 : ℝ)) ^ n) *
            (C (n.factorial : ℝ) * P)) := by rw [h]
      _ = C ((4 : ℝ) ^ n * (-(1 / 2 : ℝ)) ^ n) *
          (C (n.factorial : ℝ) * P) := by
        rw [Polynomial.C_mul]
        ring
      _ = _ := by rw [hB]
  have hsign : (-1 : ℝ) ^ n * (-2 : ℝ) ^ n = 2 ^ n := by
    rw [← mul_pow]
    norm_num
  change C ((2 : ℝ) ^ n * (n.factorial : ℝ)) * P =
    C ((-1 : ℝ) ^ n) * D
  calc
    C ((2 : ℝ) ^ n * (n.factorial : ℝ)) * P =
        C (((-1 : ℝ) ^ n * (-2 : ℝ) ^ n) *
          (n.factorial : ℝ)) * P := by rw [hsign]
    _ = C ((-1 : ℝ) ^ n) *
        (C ((-2 : ℝ) ^ n) * (C (n.factorial : ℝ) * P)) := by
      simp only [Polynomial.C_mul]
      ring
    _ = C ((-1 : ℝ) ^ n) * D := by rw [← hD]

/-! ## Plane-wave coefficient for the analysis-facing family -/

/-- Rodrigues plus the iterated integration-by-parts theorem, before
normalizing the nonzero real scalar `2^n n!`. -/
theorem plainLegendre_fourier_scaled (n : ℕ) (z : ℝ) :
    (((2 : ℝ) ^ n * (n.factorial : ℝ) : ℝ) : ℂ) *
        LegendrePlaneWave.polyFourierIntegral
          (plainLegendre n) z (-1) 1 =
      (((-1 : ℝ) ^ n : ℝ) : ℂ) *
        ((((z : ℂ) * Complex.I) ^ n) *
          LegendrePlaneWave.polyFourierIntegral
            (LegendrePlaneWave.rodriguesWeight n) z (-1) 1) := by
  have h := congrArg
    (fun p : ℝ[X] ↦
      LegendrePlaneWave.polyFourierIntegral p z (-1) 1)
    (rodrigues_plainLegendre n)
  rw [LegendrePlaneWave.polyFourierIntegral_C_mul,
    LegendrePlaneWave.polyFourierIntegral_C_mul,
    LegendrePlaneWave.rodriguesWeight_iterate_derivative_fourier] at h
  exact h

/-- Exact plane-wave coefficient identity for the all-degree Legendre family.
It is division-free in `z`, so it also holds at `z = 0`. -/
theorem polyFourierIntegral_plainLegendre_eq_sphericalJIntegralModel
    (n : ℕ) (z : ℝ) :
    LegendrePlaneWave.polyFourierIntegral
        (plainLegendre n) z (-1) 1 =
      2 * (-Complex.I) ^ n *
        LegendreTail.sphericalJIntegralModel n z := by
  have hA :
      ((((2 : ℝ) ^ n * (n.factorial : ℝ) : ℝ) : ℂ)) ≠ 0 := by
    exact_mod_cast mul_ne_zero (pow_ne_zero n (by norm_num : (2 : ℝ) ≠ 0))
      (by positivity : (n.factorial : ℝ) ≠ 0)
  have hcoef :
      ((((2 : ℝ) ^ n * (n.factorial : ℝ) : ℝ) : ℂ)) *
          (2 * (-Complex.I) ^ n *
            (((z ^ n /
              (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ))) =
        ((((-1 : ℝ) ^ n : ℝ) : ℂ)) *
          (((z : ℂ) * Complex.I) ^ n) := by
    have hf : (n.factorial : ℂ) ≠ 0 := by
      exact_mod_cast Nat.factorial_ne_zero n
    push_cast
    rw [mul_pow, neg_pow, pow_succ]
    field_simp [hf]
  apply (mul_left_cancel₀ hA)
  rw [plainLegendre_fourier_scaled,
    LegendrePlaneWave.sphericalJIntegralModel_eq_mul_polyFourierIntegral]
  let W : ℂ := LegendrePlaneWave.polyFourierIntegral
    (LegendrePlaneWave.rodriguesWeight n) z (-1) 1
  change ((((-1 : ℝ) ^ n : ℝ) : ℂ)) *
      ((((z : ℂ) * Complex.I) ^ n) * W) =
    ((((2 : ℝ) ^ n * (n.factorial : ℝ) : ℝ) : ℂ)) *
      ((2 * (-Complex.I) ^ n) *
        ((((z ^ n / (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ)) * W))
  calc
    ((((-1 : ℝ) ^ n : ℝ) : ℂ)) *
        ((((z : ℂ) * Complex.I) ^ n) * W) =
      (((((-1 : ℝ) ^ n : ℝ) : ℂ)) *
        (((z : ℂ) * Complex.I) ^ n)) * W := by ring
    _ = (((((2 : ℝ) ^ n * (n.factorial : ℝ) : ℝ) : ℂ)) *
        (2 * (-Complex.I) ^ n *
          (((z ^ n /
            (2 ^ (n + 1) * (n.factorial : ℝ)) : ℝ) : ℂ)))) * W := by
      rw [← hcoef]
    _ = _ := by ring

end LegendreRodrigues
