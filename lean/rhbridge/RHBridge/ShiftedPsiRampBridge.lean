/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Scalar certificates for the shifted-Psi / bounded-ramp bridge

The analytic Laplace-transform argument is recorded in the companion report.
This module kernel-checks the rational multiplier identities and positivity of
the inverse Green kernel.  It does not formalize Suzuki's theorem or Landau's
Tauberian theorem.
-/

namespace RHP2Bridge.ShiftedPsiRampBridge

/-- The shifted bounded-ramp multiplier and its Green multiplier compose to
double integration. -/
theorem bridge_multiplier_product (q κ : ℝ)
    (hq : q ≠ 0) (hminus : q - κ ≠ 0) (hplus : q + κ ≠ 0) :
    ((q - κ) / (q * (q + κ))) * ((q + κ) / (q * (q - κ))) = 1 / q ^ 2 := by
  field_simp [hq, hminus, hplus]

/-- The same bridge identity for an arbitrary positive-decay parameter `r`. -/
theorem general_bridge_multiplier_product (q κ r : ℝ)
    (hq : q ≠ 0) (hminus : q - κ ≠ 0) (hplus : q + r ≠ 0) :
    ((q - κ) / (q * (q + r))) * ((q + r) / (q * (q - κ))) =
      1 / q ^ 2 := by
  field_simp [hq, hminus, hplus]

/-- Exact partial fractions for the deformation from the `κ = 0` weighted
Mertens endpoint to a positive shift `κ`. -/
theorem mertens_deformation_partial_fractions (q κ : ℝ)
    (hq : q ≠ 0) (hplus : q + κ ≠ 0) :
    (q - κ) ^ 2 / (q * (q + κ)) =
      1 + κ / q - 4 * κ / (q + κ) := by
  field_simp [hq, hplus]
  ring

/-- The coefficients of the normalized two-power pole-killing kernel are
forced.  The second hypothesis is the denominator-cleared condition that its
Laplace multiplier vanish at `q = κ`. -/
theorem two_scale_pole_killer_unique (a b κ r : ℝ) (hr : r ≠ 0)
    (hnorm : a + b = 1) (hkill : a * κ + b * (κ + r) = 0) :
    a = (r + κ) / r ∧ b = -κ / r := by
  have hnormκ : (a + b) * κ = κ := by rw [hnorm]; ring
  have hnormr : (a + b) * r = r := by rw [hnorm]; ring
  have hbr : b * r = -κ := by nlinarith [hkill, hnormκ]
  have har : a * r = r + κ := by nlinarith [hnormr, hbr]
  constructor
  · exact (eq_div_iff hr).2 har
  · exact (eq_div_iff hr).2 hbr

/-- Exact partial fractions for a general positive decay `r`; the symmetric
deformation above is `r = κ`. -/
theorem general_mertens_deformation_partial_fractions (q κ r : ℝ)
    (hq : q ≠ 0) (hr : r ≠ 0) (hplus : q + r ≠ 0) :
    (q - κ) ^ 2 / (q * (q + r)) =
      1 + κ ^ 2 / (r * q) - (r + κ) ^ 2 / (r * (q + r)) := by
  field_simp [hq, hr, hplus]
  ring

/-- The inverse bridge kernel `2 exp(κt)-1` is strictly positive on the
forward time cone. -/
theorem inverse_bridge_kernel_pos {κ t : ℝ} (hκ : 0 < κ) (ht : 0 ≤ t) :
    0 < 2 * Real.exp (κ * t) - 1 := by
  have harg : 0 ≤ κ * t := mul_nonneg (le_of_lt hκ) ht
  have hexp : 1 ≤ Real.exp (κ * t) := Real.one_le_exp harg
  linarith

/-- Positivity of the general inverse bridge kernel
`((r + κ) exp (κ t) - r) / κ`. -/
theorem general_inverse_bridge_kernel_pos {κ r t : ℝ}
    (hκ : 0 < κ) (hr : 0 < r) (ht : 0 ≤ t) :
    0 < ((r + κ) * Real.exp (κ * t) - r) / κ := by
  have harg : 0 ≤ κ * t := mul_nonneg (le_of_lt hκ) ht
  have hexp : 1 ≤ Real.exp (κ * t) := Real.one_le_exp harg
  have hsum : 0 ≤ r + κ := by positivity
  have hscaled := mul_le_mul_of_nonneg_left hexp hsum
  have hnum : 0 < (r + κ) * Real.exp (κ * t) - r := by linarith
  exact div_pos hnum hκ

/-- At a nonzero pole frequency the multiplier has a nonzero denominator and
vanishes.  The denominator clause avoids relying analytically on Lean's
totalized division at `κ = 0`. -/
theorem pole_killing_zero (κ : ℝ) (hκ : κ ≠ 0) :
    κ * (κ + κ) ≠ 0 ∧ (κ - κ) / (κ * (κ + κ)) = 0 := by
  have htwice : κ + κ ≠ 0 := by
    intro h
    apply hκ
    linarith
  exact ⟨mul_ne_zero hκ htwice, by simp⟩

end RHP2Bridge.ShiftedPsiRampBridge
