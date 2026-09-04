/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Finite algebra for the compact completed-source derivative bridge

The analytic audit uses a compact profile `h` and the prime source

`S_h(t) = sum_n Lambda(n)/n * h'(t-log n)`.

This file checks only the pointwise algebra after the relevant derivatives
and Laplace multipliers have been identified.  It does not formalize the
von Mangoldt series, differentiation under that sum, the Landau theorem, a
zero-free strip, or RH.
-/

namespace RHBridge.CompactSourceDerivativeBridge

/-- Algebra behind
`S_h = exp(-t/2) * (d/dt - 1/2) D_W`.
Here `e` stands for `exp(t/2)`, `x` for the centered compact prime sum, and
`dx` for its derivative `S_h`. -/
theorem r71_source_derivative_algebra
    (e x dx D dD : ℝ) (he : e ≠ 0)
    (hD : D = e * x) (hdD : dD = e * (x / 2 + dx)) :
    e⁻¹ * (dD - D / 2) = dx := by
  rw [hD, hdD]
  field_simp
  ring

/-- Algebra behind
`(d/dt-delta) G_delta = exp(delta*t) S_h`. -/
theorem shifted_source_derivative_algebra
    (delta e source G dG : ℝ)
    (hdG : dG = delta * G + e * source) :
    dG - delta * G = e * source := by
  rw [hdG]
  ring

/-- Cancellation of the two causal differential multipliers in the
pole-killed ramp bridge.  Boundary/collar terms and transform conventions
remain analytic obligations outside this theorem. -/
theorem pole_killed_ramp_multiplier_algebra
    (q r delta V F : ℂ) (hq : q ≠ 0) (hqr : q + r ≠ 0) :
    V * (q * (q + r)) * (((q - delta) / (q * (q + r))) * F) =
      V * (q - delta) * F := by
  field_simp [hq, hqr]

/-- In the standard causal distribution convention, the completed source
has multiplier `V * (1 + core)`, while the differentiated pole-killed ramp
has multiplier `V * core`.  Their difference is the fixed initial-collar
term `V`, with the displayed sign. -/
theorem causal_ramp_boundary_correction
    (V core completedSource : ℂ)
    (hsource : completedSource = V * (1 + core)) :
    V * core = completedSource - V := by
  rw [hsource]
  ring

/-- Any two-sided absolute estimate supplies either globally fixed signed
lower estimate.  This is only an order-theoretic bookkeeping fact. -/
theorem fixed_sign_lower_of_abs
    (epsilon source bound : ℝ) (hepsilon : |epsilon| = 1)
    (hbound : |source| ≤ bound) :
    -bound ≤ epsilon * source := by
  have habs : |epsilon * source| ≤ bound := by
    simpa [abs_mul, hepsilon] using hbound
  exact (neg_le_of_abs_le habs)

end RHBridge.CompactSourceDerivativeBridge
