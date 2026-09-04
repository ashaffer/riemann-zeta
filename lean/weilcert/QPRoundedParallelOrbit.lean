import Mathlib

/-!
# Rounded parallel-orbit identities

These certify the exact algebra behind the one-orbit parallel normal form
and the four-corner reciprocal-curvature identity.  They do not assert the
open rectangle-packing estimate.
-/

namespace QPRoundedParallelOrbit

/-- Parallel physical orbit lines have no mixed term in their determinant. -/
theorem parallel_cross_determinant
    (b₀ B₀ b₁ B₁ p P r s : ℤ) :
    (b₀ + p * r) * (B₁ + P * s) -
        (B₀ + P * r) * (b₁ + p * s) =
      (b₀ * B₁ - B₀ * b₁) +
        (p * B₁ - P * b₁) * r -
        (p * B₀ - P * b₀) * s := by
  ring

/-- Exact four-corner mixed difference of the reciprocal product row. -/
theorem reciprocal_four_corner
    (Q b₀ b₁ d₀ d₁ : ℚ)
    (hb₀ : b₀ ≠ 0) (hb₁ : b₁ ≠ 0)
    (hd₀ : d₀ ≠ 0) (hd₁ : d₁ ≠ 0) :
    Q / (b₁ * d₁) - Q / (b₁ * d₀) -
        Q / (b₀ * d₁) + Q / (b₀ * d₀) =
      Q * (1 / b₁ - 1 / b₀) * (1 / d₁ - 1 / d₀) := by
  field_simp
  ring

/-- The physical direction reconstructed from a token direction has the
declared determinant label. -/
theorem token_direction_roundtrip
    (c C u v v₀ v₁ : ℤ) (hbez : c * u - C * v = 1) :
    c * (u * v₀ - C * v₁) - C * (v * v₀ - c * v₁) = v₀ := by
  linear_combination v₀ * hbez

end QPRoundedParallelOrbit
