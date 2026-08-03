/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreOrthogonality

/-!
Exact normalized Legendre plane-wave coefficients and their geometric tail.
-/

namespace LegendreCoefficientTail

/-- Exact plane-wave coefficient for the unit-normalized Legendre polynomial
on `[-1,1]`. -/
theorem polyFourierIntegral_normalizedPlainLegendre
    (n : ℕ) (z : ℝ) :
    LegendrePlaneWave.polyFourierIntegral
        (LegendreOrthogonality.normalizedPlainLegendre n) z (-1) 1 =
      ((Real.sqrt ((2 * (n : ℝ) + 1) / 2) : ℝ) : ℂ) *
        (2 * (-Complex.I) ^ n *
          LegendreTail.sphericalJIntegralModel n z) := by
  rw [LegendreOrthogonality.normalizedPlainLegendre,
    LegendrePlaneWave.polyFourierIntegral_C_mul,
    LegendreRodrigues.polyFourierIntegral_plainLegendre_eq_sphericalJIntegralModel]

/-- Squared modulus of the normalized coefficient, in the energy weighting
used by the geometric tail theorem. -/
theorem norm_polyFourierIntegral_normalizedPlainLegendre_sq
    (n : ℕ) (z : ℝ) :
    ‖LegendrePlaneWave.polyFourierIntegral
        (LegendreOrthogonality.normalizedPlainLegendre n) z (-1) 1‖ ^ 2 =
      2 * (2 * (n : ℝ) + 1) *
        ‖LegendreTail.sphericalJIntegralModel n z‖ ^ 2 := by
  rw [polyFourierIntegral_normalizedPlainLegendre, norm_mul, norm_mul,
    norm_mul, norm_pow]
  have hnonneg : 0 ≤ (2 * (n : ℝ) + 1) / 2 := by positivity
  rw [Complex.norm_real, Real.norm_eq_abs,
    abs_of_nonneg (Real.sqrt_nonneg _)]
  simp only [Complex.norm_ofNat, norm_neg, Complex.norm_I, one_pow, mul_one]
  rw [mul_pow, Real.sq_sqrt hnonneg]
  ring

/-- Complete geometric upper bound for the squared normalized plane-wave
coefficient tail.  This is a coefficient theorem; identifying the sum with
an orthogonal-projection residual still requires the L²/Parseval bridge. -/
theorem normalizedPlainLegendre_coefficient_tsum_tail_le
    (z : ℝ) (m : ℕ)
    (hq : z ^ 2 /
      ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)) < 1) :
    Summable (fun n ↦
      ‖LegendrePlaneWave.polyFourierIntegral
        (LegendreOrthogonality.normalizedPlainLegendre (m + n))
          z (-1) 1‖ ^ 2) ∧
      ∑' n : ℕ,
          ‖LegendrePlaneWave.polyFourierIntegral
            (LegendreOrthogonality.normalizedPlainLegendre (m + n))
              z (-1) 1‖ ^ 2 ≤
        2 * (LegendreTail.doubleFactorialMajorant z m /
          (1 - z ^ 2 /
            ((2 * (m : ℝ) + 1) * (2 * (m : ℝ) + 3)))) := by
  obtain ⟨hsum, hbound⟩ :=
    LegendreTail.sphericalJIntegralModel_tsum_tail_le z m hq
  let energy : ℕ → ℝ := fun n ↦
    (2 * ((m + n : ℕ) : ℝ) + 1) *
      ‖LegendreTail.sphericalJIntegralModel (m + n) z‖ ^ 2
  have hcoeff : ∀ n : ℕ,
      ‖LegendrePlaneWave.polyFourierIntegral
        (LegendreOrthogonality.normalizedPlainLegendre (m + n))
          z (-1) 1‖ ^ 2 = 2 * energy n := by
    intro n
    rw [norm_polyFourierIntegral_normalizedPlainLegendre_sq]
    dsimp [energy]
    ring
  have hsum' : Summable (fun n ↦ 2 * energy n) := hsum.mul_left 2
  refine ⟨?_, ?_⟩
  · simpa only [hcoeff] using hsum'
  · rw [show (∑' n : ℕ,
        ‖LegendrePlaneWave.polyFourierIntegral
          (LegendreOrthogonality.normalizedPlainLegendre (m + n))
            z (-1) 1‖ ^ 2) = ∑' n : ℕ, 2 * energy n by
      apply tsum_congr
      exact hcoeff]
    rw [tsum_mul_left]
    exact mul_le_mul_of_nonneg_left hbound (by norm_num)

end LegendreCoefficientTail
