/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ContinuousDelayObstruction

/-!
# Compression is not a global multiplier equation

The localized Euler--Lagrange equation says that the operator output is
orthogonal to the old support subspace.  It does not say that the full output
vanishes.  This elementary obstruction persists after Fourier transform and
prevents a direct entire-function argument of the form `Omega * F = 0`.
-/

namespace RHP2Bridge.LocalizedFourierObstruction

/-- A two-dimensional symmetric block model: `A(x,y)=(y,x)`, the old subspace
is the first coordinate, and `u=(1,0)`.  Every old test annihilates `A u`, but
`A u` is nonzero. -/
theorem compressed_equation_does_not_imply_global_equation :
    (∀ v₁ v₂ : ℝ, v₂ = 0 → 0 * v₁ + 1 * v₂ = 0) ∧
      ¬ (0 = 0 ∧ (1 : ℝ) = 0) := by
  constructor
  · intro v₁ v₂ hv
    simp [hv]
  · norm_num

/-- Scalar form of the same fact: orthogonality to a proper coordinate
subspace leaves an arbitrary complementary residual. -/
theorem arbitrary_complement_residual (r : ℝ) :
    (∀ v : ℝ, r * 0 * v = 0) ∧ (r = 0 ↔ r * 1 = 0) := by
  simp

end RHP2Bridge.LocalizedFourierObstruction
