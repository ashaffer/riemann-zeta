import Mathlib

/-!
# Affine four-completion Hessian identities

These certify the local stationary-product algebra, not the global inverse
theorem which would be needed to place arbitrary actual-prime cells in such
a chart.
-/

namespace QPAffineFourCompletionHessian

theorem stationary_cubic_identity (A B : ℚ) :
    (1 - A - B) * (1 + A) * (1 + B) - 1 =
      -(A^2 + A * B + B^2) - A * B * (A + B) := by
  ring

theorem hexagonal_norm_lower_bound (A B : ℚ) :
    (A^2 + B^2) / 2 ≤ A^2 + A * B + B^2 := by
  nlinarith [sq_nonneg (A + B)]

theorem hessian_determinant (x p z : ℚ) :
    4 * x^2 * (p^2 * z^2) - x^2 * (p * z)^2 =
      3 * x^2 * p^2 * z^2 := by
  ring

theorem simultaneous_coordinate_degeneracy
    (p P z Z : ℤ) (hU : p ≠ 0 ∨ P ≠ 0) (hZ : z ≠ 0 ∨ Z ≠ 0)
    (h1 : p * z = 0) (h2 : P * Z = 0) :
    (p = 0 ∧ Z = 0 ∧ P ≠ 0 ∧ z ≠ 0) ∨
      (P = 0 ∧ z = 0 ∧ p ≠ 0 ∧ Z ≠ 0) := by
  rcases mul_eq_zero.mp h1 with hp | hz
  · rcases mul_eq_zero.mp h2 with hP | hZ0 <;> aesop
  · rcases mul_eq_zero.mp h2 with hP | hZ0 <;> aesop

theorem coordinate_degeneracy_is_signed_tangent
    (p P z Z : ℤ)
    (h : (p = 0 ∧ Z = 0) ∨ (P = 0 ∧ z = 0)) :
    p * z - P * Z = 0 := by
  rcases h with h | h
  · rcases h with ⟨rfl, rfl⟩
    ring
  · rcases h with ⟨rfl, rfl⟩
    ring

/-- Signed tangency need not make either product Hessian degenerate. -/
theorem tangent_converse_fails :
    (1 : ℤ) * 1 - 1 * 1 = 0 ∧ (1 : ℤ) * 1 ≠ 0 := by
  norm_num

/-- The determinant polynomial on an affine Cartesian token chart. -/
theorem affine_determinant_expansion
    (P₀ P₁ R₀ R₁ V₀ V₁ W₀ W₁ r s : ℤ) :
    (P₀ + r * V₀) * (R₁ + s * W₁) -
        (P₁ + r * V₁) * (R₀ + s * W₀) =
      (P₀ * R₁ - P₁ * R₀) +
      r * (V₀ * R₁ - V₁ * R₀) +
      s * (P₀ * W₁ - P₁ * W₀) +
      r * s * (V₀ * W₁ - V₁ * W₀) := by
  ring

/-- Factorisation behind the transverse harmonic-slope count. -/
theorem affine_bilinear_factorisation
    (A B C E r s : ℤ) :
    (E * r + C) * (E * s + B) =
      E * (A + B * r + C * s + E * r * s) + (B * C - E * A) := by
  ring

/-- Parallel token directions lift to the signed tangent equation. -/
theorem parallel_token_is_signed_tangent
    (c C u v V₀ V₁ W₀ W₁ : ℤ)
    (hparallel : V₀ * W₁ - V₁ * W₀ = 0) :
    (u * V₀ - C * V₁) * (-v * W₀ + c * W₁) -
      (v * V₀ - c * V₁) * (-u * W₀ + C * W₁) = 0 := by
  calc
    (u * V₀ - C * V₁) * (-v * W₀ + c * W₁) -
        (v * V₀ - c * V₁) * (-u * W₀ + C * W₁) =
      (c * u - C * v) * (V₀ * W₁ - V₁ * W₀) := by ring
    _ = 0 := by rw [hparallel]; ring

/-- The radial null condition is the coordinate-product null condition. -/
theorem token_direction_norm
    (c C u v V₀ V₁ : ℤ) :
    -2 * u * v * V₀^2 + 2 * (c * u + C * v) * V₀ * V₁ -
        2 * c * C * V₁^2 =
      -2 * (u * V₀ - C * V₁) * (v * V₀ - c * V₁) := by
  ring

end QPAffineFourCompletionHessian
