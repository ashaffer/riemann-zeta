import Mathlib

/-!
Exact polynomial identities behind the lossless four-completion Bezout-token
normal form.  This file certifies the coordinate algebra and the principal
quadratic chart; it does not assert the open global occupied-cell estimate.
-/

namespace QPFourCompletionBezoutToken

theorem center_roundtrip
    (c C u v delta n : ℤ) (hbez : c * u - C * v = 1) :
    c * (u * delta - C * n) - C * (v * delta - c * n) = delta := by
  linear_combination delta * hbez

theorem endpoint_roundtrip
    (c C u v h m : ℤ) (hbez : c * u - C * v = 1) :
    C * (-v * h + c * m) - c * (-u * h + C * m) = h := by
  linear_combination h * hbez

/-- The endpoint orbit is the coordinate-swap of the centre orbit at the
opposite determinant label.  In token coordinates this is simply negation. -/
theorem endpoint_is_negated_center_orbit
    (c C u v h n : ℤ) :
    let b := u * (-h) - C * n
    let B := v * (-h) - c * n
    (-v * h + c * (-n), -u * h + C * (-n)) = (B, b) := by
  dsimp
  apply Prod.ext <;> simp <;> ring

/-- Consequently a middle transition is made from the two cross-products of
two points on the same centre orbit. -/
theorem one_orbit_cross_products
    (c C u v delta n h m : ℤ) :
    let b₁ := u * delta - C * n
    let B₁ := v * delta - c * n
    let b₂ := u * (-h) - C * m
    let B₂ := v * (-h) - c * m
    b₁ * (-v * h + c * (-m)) = b₁ * B₂ ∧
      B₁ * (-u * h + C * (-m)) = B₁ * b₂ := by
  dsimp
  constructor <;> ring

/-- Exact rational-strip identity for every physical centre token. -/
theorem center_digital_strip_identity
    (C u delta n : ℤ) :
    C * n - u * delta = -(u * delta - C * n) := by
  ring

theorem middle_determinant_is_token_area
    (c C u v delta n h m : ℤ) (hbez : c * u - C * v = 1) :
    (u * delta - C * n) * (-v * h + c * m)
      - (v * delta - c * n) * (-u * h + C * m)
      = delta * m - n * h := by
  linear_combination (delta * m - n * h) * hbez

theorem product_sum_form
    (c C u v delta n h m : ℤ) :
    (u * delta - C * n) * (-v * h + c * m)
      + (v * delta - c * n) * (-u * h + C * m)
      = (-2 * u * v) * delta * h
        + (c * u + C * v) * (delta * m + n * h)
        - (2 * c * C) * n * m := by
  ring

theorem token_form_determinant
    (c C u v : ℤ) (hbez : c * u - C * v = 1) :
    (-2 * u * v) * (-2 * c * C) - (c * u + C * v)^2 = -1 := by
  nlinarith [sq_nonneg (c * u - C * v - 1)]

theorem max_abs_add_sub_int (A B : ℤ) :
    max |A + B| |A - B| = |A| + |B| := by
  rcases le_total 0 A with hA | hA
  · rcases le_total 0 B with hB | hB
    · have hsum : 0 ≤ A + B := add_nonneg hA hB
      have hbound : |A - B| ≤ |A| + |B| := abs_sub A B
      rw [abs_of_nonneg hA, abs_of_nonneg hB] at hbound ⊢
      rw [abs_of_nonneg hsum, max_eq_left hbound]
    · have hdiff : 0 ≤ A - B := sub_nonneg.mpr (le_trans hB hA)
      have hbound : |A + B| ≤ |A| + |B| := by
        simpa [sub_neg_eq_add] using (abs_sub A (-B))
      rw [abs_of_nonneg hA, abs_of_nonpos hB] at hbound ⊢
      rw [abs_of_nonneg hdiff, max_eq_right (by linarith : |A + B| ≤ A - B)]
      ring
  · rcases le_total 0 B with hB | hB
    · have hdiff : A - B ≤ 0 := sub_nonpos.mpr (le_trans hA hB)
      have hbound : |A + B| ≤ |A| + |B| := by
        simpa [sub_neg_eq_add] using (abs_sub A (-B))
      rw [abs_of_nonpos hA, abs_of_nonneg hB] at hbound ⊢
      rw [abs_of_nonpos hdiff,
        max_eq_right (by linarith : |A + B| ≤ -(A - B))]
      ring
    · have hsum : A + B ≤ 0 := add_nonpos hA hB
      have hbound : |A - B| ≤ |A| + |B| := abs_sub A B
      rw [abs_of_nonpos hA, abs_of_nonpos hB] at hbound ⊢
      rw [abs_of_nonpos hsum,
        max_eq_left (by linarith : |A - B| ≤ -(A + B))]
      ring

theorem hard_pair_diamond (q y s k : ℤ) :
    max |4 * y * (s + k) - q^3| |4 * y * (s - k) - q^3|
      = |4 * y * s - q^3| + 4 * |y| * |k| := by
  calc
    _ = max |(4 * y * s - q^3) + 4 * y * k|
        |(4 * y * s - q^3) - 4 * y * k| := by
          congr 2 <;> ring
    _ = |4 * y * s - q^3| + |4 * y * k| :=
      max_abs_add_sub_int (4 * y * s - q^3) (4 * y * k)
    _ = _ := by simp [abs_mul]

theorem symmetric_gram_determinant_minus_one
    (a b d p1 p2 q1 q2 : ℤ)
    (hdet : a * d - b^2 = -1) :
    let pp := a * p1^2 + 2 * b * p1 * p2 + d * p2^2
    let qq := a * q1^2 + 2 * b * q1 * q2 + d * q2^2
    let pq := a * p1 * q1 + b * (p1 * q2 + p2 * q1) + d * p2 * q2
    pq^2 - pp * qq = (p1 * q2 - p2 * q1)^2 := by
  dsimp
  calc
    _ = -(a * d - b^2) * (p1 * q2 - p2 * q1)^2 := by ring
    _ = _ := by rw [hdet]; ring

theorem physical_gram_factorisation (b B d E : ℤ) :
    (b * d + B * E)^2 - (-2 * b * B) * (-2 * d * E)
      = (b * d - B * E)^2 := by
  ring

theorem principal_middle_residual
    (M A s : ℤ) :
    (M + A - s) * (M - A) * (M + s) - M^3
      = -M * (A^2 - A * s + s^2) + A * s * (s - A) := by
  ring

theorem principal_quadratic_positive (A s : ℝ) :
    (A^2 + s^2) / 2 ≤ A^2 - A * s + s^2 := by
  nlinarith [sq_nonneg (A - s)]

end QPFourCompletionBezoutToken
