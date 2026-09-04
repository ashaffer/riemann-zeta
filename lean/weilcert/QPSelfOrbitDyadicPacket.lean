import Mathlib

/-!
# Exact self-orbit dyadic-packet identities

This file certifies the integral algebra behind the natural-scale affine
packet theorem and the common-shift reciprocal collision normal form.  It
does not assert the open signed dyadic reciprocal large-sieve estimate.
-/

namespace QPSelfOrbitDyadicPacket

/-- Determinant labels convert affine area into a two-by-two label minor. -/
theorem label_area_identity
    (c C b₁ B₁ b₂ B₂ b₃ B₃ t₁ t₂ t₃ : ℤ)
    (h₁ : t₁ = c * b₁ - C * B₁)
    (h₂ : t₂ = c * b₂ - C * B₂)
    (h₃ : t₃ = c * b₃ - C * B₃) :
    C * ((b₂ - b₁) * (B₃ - B₁) - (B₂ - B₁) * (b₃ - b₁)) =
      (t₂ - t₁) * (b₃ - b₁) - (b₂ - b₁) * (t₃ - t₁) := by
  subst t₁
  subst t₂
  subst t₃
  ring

/-- An integral affine area vanishes when its nonzero scale multiple is
strictly smaller than that scale. -/
theorem integral_area_zero
    (C A : ℤ) (hC : 0 < C) (hsmall : |C * A| < C) : A = 0 := by
  by_contra hA
  have hAabs : 1 ≤ |A| := Int.one_le_abs hA
  have hscale : C ≤ C * |A| := by
    nlinarith [abs_nonneg A]
  have habs : |C * A| = C * |A| := by
    rw [abs_mul, abs_of_pos hC]
  rw [habs] at hsmall
  omega

/-- The two-point cross determinant is the corresponding label minor. -/
theorem cross_determinant_from_labels
    (c C b₁ B₁ b₂ B₂ t₁ t₂ : ℤ)
    (h₁ : t₁ = c * b₁ - C * B₁)
    (h₂ : t₂ = c * b₂ - C * B₂) :
    C * (b₁ * B₂ - B₁ * b₂) = t₁ * b₂ - t₂ * b₁ := by
  subst t₁
  subst t₂
  ring

/-- Exact coordinates in the index-`r` parallel-tower chart.  Here `t` is
the anchor determinant label and `s` is the transverse line index. -/
theorem tower_coordinate_identities
    (c C p P b B : ℤ) :
    let r := c * p - C * P
    let t := c * b - C * B
    let s := p * B - P * b
    r * b = p * t + C * s ∧ r * B = P * t + c * s := by
  dsimp
  constructor <;> ring

/-- Exact difference between the two reciprocal cross charts. -/
theorem reciprocal_chart_difference
    (Q b B d D : ℚ)
    (hb : b ≠ 0) (hB : B ≠ 0) (hd : d ≠ 0) (hD : D ≠ 0) :
    Q / (b * D) - Q / (B * d) =
      -Q * (b * D - B * d) / (b * D * B * d) := by
  field_simp
  ring

/-- Clearing denominators leaves a single integral/rational Möbius shift. -/
theorem cleared_reciprocal_collision
    (Q n n' r : ℚ) (hn : n ≠ 0) (hn' : n' ≠ 0) :
    Q / n - Q / n' - r =
      (Q * (n' - n) - r * n * n') / (n * n') := by
  field_simp

end QPSelfOrbitDyadicPacket
