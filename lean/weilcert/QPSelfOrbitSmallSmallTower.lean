import Mathlib

/-!
# Small-step/small-remainder self-orbit tower rigidity

This file certifies the exact integral identities behind the unique hard
direction and parallel-line separation.  It does not assert the open signed
translate-Bessel or dyadic reciprocal large-sieve estimate.
-/

namespace QPSelfOrbitSmallSmallTower

/-- Two anchor remainders recover the determinant of their directions. -/
theorem two_direction_determinant_identities
    (c C p P s S : ℤ) :
    C * (p * S - P * s) =
        (c * p - C * P) * s - (c * s - C * S) * p ∧
      c * (p * S - P * s) =
        (c * p - C * P) * S - (c * s - C * S) * P := by
  constructor <;> ring

/-- If the cleared determinant is strictly smaller than its positive anchor
scale, integrality forces the two directions to be parallel. -/
theorem direction_parallel_of_small_remainder_expression
    (c C p P s S : ℤ) (hC : 0 < C)
    (hsmall :
      |(c * p - C * P) * s - (c * s - C * S) * p| < C) :
    p * S - P * s = 0 := by
  have hid :
      C * (p * S - P * s) =
        (c * p - C * P) * s - (c * s - C * S) * p := by
    ring
  rw [← hid] at hsmall
  by_contra hdet
  have hone : 1 ≤ |p * S - P * s| := Int.one_le_abs hdet
  have habs : |C * (p * S - P * s)| = C * |p * S - P * s| := by
    rw [abs_mul, abs_of_pos hC]
  rw [habs] at hsmall
  nlinarith [abs_nonneg (p * S - P * s)]

/-- Exact tower coordinates: `t` is the anchor label and `s` the affine
line index `det(U,z)`. -/
theorem tower_coordinate_identities
    (c C p P b B : ℤ) :
    let r := c * p - C * P
    let t := c * b - C * B
    let s := p * B - P * b
    r * b = p * t + C * s ∧ r * B = P * t + c * s := by
  dsimp
  constructor <;> ring

/-- Subtracting two tower coordinates gives the exact numerators used in
the macroscopic interline gap. -/
theorem subtracted_tower_identities
    (c C p P b₁ B₁ b₂ B₂ : ℤ) :
    let r := c * p - C * P
    let t₁ := c * b₁ - C * B₁
    let t₂ := c * b₂ - C * B₂
    let s₁ := p * B₁ - P * b₁
    let s₂ := p * B₂ - P * b₂
    r * (b₂ - b₁) = p * (t₂ - t₁) + C * (s₂ - s₁) ∧
      r * (B₂ - B₁) = P * (t₂ - t₁) + c * (s₂ - s₁) := by
  dsimp
  constructor <;> ring

/-- The centered reciprocal phase has the same Hessian as the reciprocal
phase, with strictly positive determinant away from the axes. -/
theorem centered_reciprocal_hessian_determinant
    (T x y : ℚ) (hx : x ≠ 0) (hy : y ≠ 0) :
    (2 * T / (x ^ 3 * y)) * (2 * T / (x * y ^ 3)) -
        (T / (x ^ 2 * y ^ 2)) ^ 2 =
      3 * T ^ 2 / (x ^ 4 * y ^ 4) := by
  field_simp
  ring

/-- At a two-dimensional reciprocal stationary point the Legendre action is
three times the original phase, and its cube depends only on the product of
the two Poisson frequencies.  This is the exact product-action collapse
which remains after stationary-frequency images have been separated. -/
theorem reciprocal_stationary_product_action
    (A x y m n : ℚ) (hx : x ≠ 0) (hy : y ≠ 0)
    (hm : m = A / (x ^ 2 * y))
    (hn : n = A / (x * y ^ 2)) :
    let f := A / (x * y)
    f + m * x + n * y = 3 * f ∧ f ^ 3 = A * m * n := by
  subst m
  subst n
  dsimp
  constructor
  · field_simp
    ring
  · field_simp

end QPSelfOrbitSmallSmallTower
