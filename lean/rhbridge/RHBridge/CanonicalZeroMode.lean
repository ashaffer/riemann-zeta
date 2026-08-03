/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LocalizedFourierObstruction

/-!
# The zero-parameter canonical-system uniqueness mechanism

At spectral parameter zero, a canonical system `J Y' = z H Y` has constant
solutions.  Two independent separated endpoint conditions therefore force
the solution to vanish.  This file isolates the finite-dimensional endpoint
algebra; connecting it to Suzuki's localized zero mode is the remaining
analytic realization problem.
-/

namespace RHP2Bridge.CanonicalZeroMode

/-- Two independent real endpoint covectors have trivial common kernel. -/
theorem eq_zero_of_independent_endpoint_conditions
    {a₁ a₂ b₁ b₂ x y : ℝ}
    (hleft : a₁ * x + a₂ * y = 0)
    (hright : b₁ * x + b₂ * y = 0)
    (hindependent : a₁ * b₂ - a₂ * b₁ ≠ 0) :
    x = 0 ∧ y = 0 := by
  have hxdet : (a₁ * b₂ - a₂ * b₁) * x = 0 := by
    calc
      (a₁ * b₂ - a₂ * b₁) * x =
          b₂ * (a₁ * x + a₂ * y) - a₂ * (b₁ * x + b₂ * y) := by ring
      _ = 0 := by rw [hleft, hright]; ring
  have hydet : (a₁ * b₂ - a₂ * b₁) * y = 0 := by
    calc
      (a₁ * b₂ - a₂ * b₁) * y =
          a₁ * (b₁ * x + b₂ * y) - b₁ * (a₁ * x + a₂ * y) := by ring
      _ = 0 := by rw [hleft, hright]; ring
  exact ⟨(mul_eq_zero.mp hxdet).resolve_left hindependent,
    (mul_eq_zero.mp hydet).resolve_left hindependent⟩

/-- Equivalent determinant formulation convenient for transfer matrices. -/
theorem endpoint_determinant_ne_zero_excludes_nonzero_constant
    {a₁ a₂ b₁ b₂ x y : ℝ}
    (hindependent : a₁ * b₂ - a₂ * b₁ ≠ 0)
    (hconditions : a₁ * x + a₂ * y = 0 ∧
      b₁ * x + b₂ * y = 0) :
    ¬ (x ≠ 0 ∨ y ≠ 0) := by
  obtain ⟨hx, hy⟩ := eq_zero_of_independent_endpoint_conditions
    hconditions.1 hconditions.2 hindependent
  simp [hx, hy]

end RHP2Bridge.CanonicalZeroMode
