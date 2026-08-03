/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Algebraic normalization of the CCM Poisson identity

For even functions, Poisson summation is a relation between the value at zero
and twice the positive-index sum.  Once both zero moments vanish, multiplying
by the CCM square-root factor gives exactly `E(F h)(u⁻¹) = E(h)(u)`.
-/

namespace RHP2Bridge.Stage4PoissonReduction

/-- The scalar algebra underlying the positive-half Poisson formula.  `Sh`
and `SF` stand for the positive-index sums of `h(nu)` and
`Fourier(h)(n/u)`, respectively. -/
theorem sqrt_mul_positiveSum_eq
    {u Sh SF : ℝ} (hu : 0 < u)
    (hPoisson : 2 * Sh = u⁻¹ * (2 * SF)) :
    Real.sqrt u * Sh = Real.sqrt (u⁻¹) * SF := by
  have hu0 : u ≠ 0 := hu.ne'
  have hs : Sh = u⁻¹ * SF := by linarith
  rw [hs, Real.sqrt_inv]
  have hsqrt : Real.sqrt u ≠ 0 := (Real.sqrt_pos.2 hu).ne'
  field_simp
  rw [Real.sq_sqrt hu.le]

/-- With vanishing values at zero, the usual even full-lattice Poisson
identity has exactly the hypothesis used by `sqrt_mul_positiveSum_eq`. -/
theorem sqrt_mul_positiveSum_eq_of_fullPoisson
    {u h0 F0 Sh SF : ℝ} (hu : 0 < u)
    (hh0 : h0 = 0) (hF0 : F0 = 0)
    (hPoisson : h0 + 2 * Sh = u⁻¹ * (F0 + 2 * SF)) :
    Real.sqrt u * Sh = Real.sqrt (u⁻¹) * SF := by
  apply sqrt_mul_positiveSum_eq hu
  simpa [hh0, hF0] using hPoisson

end RHP2Bridge.Stage4PoissonReduction
