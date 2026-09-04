import Mathlib

/-!
# Canonical tower embedding of the aligned cubic chart

This file certifies the exact algebra behind the critical canonical-tower
fixture.  It shows that the aligned `S = R + 1` completed-strip phase occurs
inside a self-orbit chart.  It does not assert the open cubic incidence or
dyadic reciprocal large-sieve estimates.
-/

namespace QPSelfOrbitTowerCubicSurvival

/-- The long aligned direction and the short diagonal complement form a
unimodular basis. -/
theorem aligned_basis_unimodular (R : ℤ) :
    R * (-1) - (R + 1) * (-1) = 1 := by
  ring

/-- The reflected anchor in the critical family is `F d + e`. -/
theorem reflected_anchor_decomposition (F R : ℤ) :
    (F * R - 1, F * (R + 1) - 1) =
      (F * R + (-1), F * (R + 1) + (-1)) := by
  rfl

/-- On the embedded rectangle the determinant label is exactly `m-F*n`. -/
theorem critical_tower_label (F R m n : ℤ) :
    let C := F * R - 1
    let c := F * (R + 1) - 1
    let b := R * m - n
    let B := (R + 1) * m - n
    c * b - C * B = m - F * n := by
  dsimp
  ring

/-- The product in one ordered lane pair has three exact base-`R`
coefficients.  This is the carry-sensitive normal form used to classify
equal products in the balanced rectangle. -/
theorem ordered_lane_product_expansion (a b R n n' : ℤ) :
    (a * R - n) * (b * (R + 1) - n') =
      R^2 * (a * b) + R * (a * b - a * n' - b * n) + n * (n' - b) := by
  ring

/-- Swapping the two lanes and their internal coordinates changes the
product by the exact rank-one defect `a*n' - b*n`.  Thus transposed packets
can be close without being exact aliases. -/
theorem transposed_lane_product_defect (a b R n n' : ℤ) :
    (a * R - n) * (b * (R + 1) - n') -
        (b * R - n') * (a * (R + 1) - n) =
      a * n' - b * n := by
  ring

/-- Over the rationals, the three base-`R` coefficients are equivalently
the lane product and the unordered pair of normalized offsets. -/
theorem normalized_lane_product
    (a b R n n' : ℚ) (ha : a ≠ 0) (hb : b ≠ 0) :
    (a * R - n) * (b * (R + 1) - n') =
      (a * b) * (R - n / a) * (R - (n' / b - 1)) := by
  field_simp
  ring

/-- In the scaled lane coordinates the carrier is an integral lane multiple
of either leading linear frequency.  Therefore simultaneous integrality of
the two linear characters imposes no third carrier congruence. -/
theorem carrier_from_linear_frequencies
    (F R alpha beta : ℚ) (ha : alpha ≠ 0) (hb : beta ≠ 0) :
    F * (R - 1) / (alpha * beta) =
        (alpha * F) * (R - 1) * (1 / (alpha^2 * beta)) ∧
      F * (R - 1) / (alpha * beta) =
        (beta * F) * (R - 1) * (1 / (alpha * beta^2)) := by
  constructor <;> field_simp

/-- The two leading linear frequencies have zero cross determinant before
rounding.  Consequently the determinant of simultaneous nearest integers is
controlled entirely by their two rounding errors. -/
theorem leading_frequency_cross_cancellation
    (F h a b : ℚ) (ha : a ≠ 0) (hb : b ≠ 0) :
    a * (h * F^3 / (a^2 * b)) - b * (h * F^3 / (a * b^2)) = 0 := by
  field_simp
  ring

/-- On the zero-determinant branch `a=g*A`, `b=g*B`, `r=B*t`, the first
near-integral frequency is exactly `B` times one common scalar frequency.
The companion identity is obtained by interchanging `A` and `B`. -/
theorem zero_defect_common_frequency
    (F h g A B t : ℚ) (hg : g ≠ 0) (hA : A ≠ 0) (hB : B ≠ 0) :
    h * F^3 / (g^3 * A^2 * B) - B * t =
      B * (h * F^3 / (g^3 * A^2 * B^2) - t) := by
  field_simp

/-- Clearing the scalar diagonal frequency gives the shifted-cube
numerator with no loss or additional congruence. -/
theorem diagonal_scalar_near_cube
    (F h u t : ℚ) (hu : u ≠ 0) :
    h * F^3 / u^3 - t = (h * F^3 - t * u^3) / u^3 := by
  field_simp

/-- Two shifted-cube solutions over the same input satisfy the exact
cross-determinant identity used to prove primitive-ray uniqueness. -/
theorem same_input_cross_determinant
    (P u A₁ A₂ B₁ B₂ Δ₁ Δ₂ : ℤ)
    (h₁ : A₁ * u^3 - B₁ * P^3 = Δ₁)
    (h₂ : A₂ * u^3 - B₂ * P^3 = Δ₂) :
    P^3 * (A₁ * B₂ - A₂ * B₁) = A₂ * Δ₁ - A₁ * Δ₂ := by
  calc
    P^3 * (A₁ * B₂ - A₂ * B₁) =
        A₂ * (A₁ * u^3 - B₁ * P^3) -
          A₁ * (A₂ * u^3 - B₂ * P^3) := by ring
    _ = A₂ * Δ₁ - A₁ * Δ₂ := by rw [h₁, h₂]

/-- For distinct inputs, the coefficient determinant is the cubic secant
plus the two residual errors. -/
theorem ordered_input_cross_determinant
    (P u₁ u₂ A₁ A₂ B₁ B₂ Δ₁ Δ₂ : ℤ)
    (h₁ : A₁ * u₁^3 - B₁ * P^3 = Δ₁)
    (h₂ : A₂ * u₂^3 - B₂ * P^3 = Δ₂) :
    P^3 * (A₁ * B₂ - A₂ * B₁) =
      A₁ * A₂ * (u₂^3 - u₁^3) + A₂ * Δ₁ - A₁ * Δ₂ := by
  calc
    P^3 * (A₁ * B₂ - A₂ * B₁) =
        A₁ * A₂ * (u₂^3 - u₁^3) +
          A₂ * (A₁ * u₁^3 - B₁ * P^3) -
          A₁ * (A₂ * u₂^3 - B₂ * P^3) := by ring
    _ = A₁ * A₂ * (u₂^3 - u₁^3) + A₂ * Δ₁ - A₁ * Δ₂ := by
      rw [h₁, h₂]

/-- Eliminating a shared coefficient reproduces a shifted-cube equation at
the same scale; this is the exact determinant-iteration obstruction. -/
theorem same_coefficient_shifted_cube
    (P A u₁ u₂ B₁ B₂ Δ₁ Δ₂ : ℤ)
    (h₁ : A * u₁^3 - B₁ * P^3 = Δ₁)
    (h₂ : A * u₂^3 - B₂ * P^3 = Δ₂) :
    P^3 * (B₁ * u₂^3 - B₂ * u₁^3) = Δ₂ * u₁^3 - Δ₁ * u₂^3 := by
  calc
    P^3 * (B₁ * u₂^3 - B₂ * u₁^3) =
        (A * u₁^3 - Δ₁) * u₂^3 -
          (A * u₂^3 - Δ₂) * u₁^3 := by
      rw [← h₁, ← h₂]
      ring
    _ = Δ₂ * u₁^3 - Δ₁ * u₂^3 := by ring

/-- More generally, Euclidean division `C=rR+s` gives the tower label
`-r*n-s*m`; the Euclidean remainder does not alter the aligned kernel. -/
theorem euclidean_tower_label (r R s m n : ℤ) :
    let C := r * R + s
    let c := r * (R + 1) + s
    let b := R * m - n
    let B := (R + 1) * m - n
    c * b - C * B = -r * n - s * m := by
  dsimp
  ring

/-- With `q=2FR`, the diagonal B-process cubic frequency is exactly the
aligned pure cube multiplied by `(R+1)/R`. -/
theorem aligned_cubic_frequency
    (F R u : ℚ) (hF : F ≠ 0) (hR : R ≠ 0) :
    8 * R^2 * (R + 1) * u^3 / (2 * F * R)^3 =
      ((R + 1) / R) * (u / F)^3 := by
  field_simp
  ring

/-- Clearing the aligned cubic approximation introduces no extra factor or
congruence beyond its standard near-cube numerator. -/
theorem aligned_near_cube_clearing
    (F R u a b : ℚ) (hF : F ≠ 0) (hR : R ≠ 0) :
    a * (((R + 1) / R) * (u / F)^3) - b =
      (a * (R + 1) * u^3 - b * R * F^3) / (R * F^3) := by
  field_simp

end QPSelfOrbitTowerCubicSurvival
