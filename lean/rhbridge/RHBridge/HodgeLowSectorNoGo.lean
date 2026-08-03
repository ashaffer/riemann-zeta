/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Low-sector Dirichlet-to-Neumann reduction and no-go model

After every already-controlled direction has been Schur-eliminated, a single
old mode of energy `lambda`, its exterior residual `r`, and a positive exterior
block of energy `d` form a two-by-two quadratic.  Completing the square shows
that the remaining pivot is exactly `lambda - r^2 / d`.

The rank-one model in the second part is the scalar reduction of the even
translation-invariant form

`Q_J(f) = ||f||^2 - alpha * |integral_J f|^2`.

Its nonlocal kernel is constant, hence entire.  Nevertheless, the compression
to an old interval and the compression to its exterior can both be positive
while the exterior response exceeds the old gap.  Analytic continuation,
convolution structure, and separate block positivity therefore do not imply
the desired low-sector contraction.
-/

namespace RHP2Bridge.HodgeLowSectorNoGo

noncomputable section

/-- The scalar Dirichlet-to-Neumann response of a residual `r` through a
positive exterior direction of energy `d`. -/
def scalarDtNResponse (r d : ℝ) : ℝ := r ^ 2 / d

/-- The scalar pivot left after the exterior direction is minimized out. -/
def scalarDtNPivot (lambda r d : ℝ) : ℝ :=
  lambda - scalarDtNResponse r d

/-- Exact harmonic-extension identity.  The minimizing exterior coefficient
is `w = -t*r/d`, and its energy is `t^2 * scalarDtNPivot lambda r d`. -/
theorem scalar_harmonic_extension_identity
    {lambda r d t w : ℝ} (hd : d ≠ 0) :
    lambda * t ^ 2 + 2 * r * t * w + d * w ^ 2 =
      d * (w + t * r / d) ^ 2 +
        t ^ 2 * scalarDtNPivot lambda r d := by
  unfold scalarDtNPivot scalarDtNResponse
  field_simp [hd]
  ring

/-- If the exterior response is larger than the old energy, the harmonic
extension is an explicit negative direction. -/
theorem negative_harmonic_extension_of_response_gt
    {lambda r d : ℝ} (hd : 0 < d)
    (hresponse : lambda < scalarDtNResponse r d) :
    lambda + 2 * r * (-r / d) + d * (-r / d) ^ 2 < 0 := by
  have hd0 : d ≠ 0 := ne_of_gt hd
  have hid :
      lambda + 2 * r * (-r / d) + d * (-r / d) ^ 2 =
        scalarDtNPivot lambda r d := by
    unfold scalarDtNPivot scalarDtNResponse
    field_simp [hd0]
    ring
  rw [hid]
  exact sub_neg.mpr hresponse

/-! ## Constant-convolution countermodel -/

/-- Old constant-mode eigenvalue for `I - alpha * 1 ⊗ 1` on a set of
measure `m`. -/
def rankOneOldGap (alpha m : ℝ) : ℝ := 1 - alpha * m

/-- Exterior constant-mode eigenvalue on a disjoint set of measure `n`. -/
def rankOneExteriorGap (alpha n : ℝ) : ℝ := 1 - alpha * n

/-- Squared normalized old/exterior residual in the constant directions. -/
def rankOneResidualSq (alpha m n : ℝ) : ℝ := alpha ^ 2 * m * n

/-- Exterior response of the constant old mode after the exterior block is
inverted. -/
def rankOneResponse (alpha m n : ℝ) : ℝ :=
  rankOneResidualSq alpha m n / rankOneExteriorGap alpha n

/-- Exact difference between the exterior response and the positive old gap.
The numerator is the eigenvalue crossing on the union, with the opposite
sign. -/
theorem rankOneResponse_sub_oldGap
    {alpha m n : ℝ} (hExterior : rankOneExteriorGap alpha n ≠ 0) :
    rankOneResponse alpha m n - rankOneOldGap alpha m =
      (alpha * (m + n) - 1) / rankOneExteriorGap alpha n := by
  unfold rankOneResponse rankOneResidualSq rankOneOldGap
  unfold rankOneExteriorGap at hExterior ⊢
  field_simp [hExterior]
  ring

/-- Separate positivity of the old and exterior compressions is compatible
with failure of the low-sector contraction as soon as the constant mode on
their union has crossed zero. -/
theorem analytic_rankOne_convolution_breaks_contraction
    {alpha m n : ℝ}
    (hOld : alpha * m < 1) (hExterior : alpha * n < 1)
    (hUnion : 1 < alpha * (m + n)) :
    0 < rankOneOldGap alpha m ∧
      0 < rankOneExteriorGap alpha n ∧
      rankOneOldGap alpha m < rankOneResponse alpha m n := by
  have hOldGap : 0 < rankOneOldGap alpha m := by
    exact sub_pos.mpr hOld
  have hExteriorGap : 0 < rankOneExteriorGap alpha n := by
    exact sub_pos.mpr hExterior
  have hExteriorNe : rankOneExteriorGap alpha n ≠ 0 := ne_of_gt hExteriorGap
  have hDifference :
      0 < rankOneResponse alpha m n - rankOneOldGap alpha m := by
    rw [rankOneResponse_sub_oldGap hExteriorNe]
    exact div_pos (sub_pos.mpr hUnion) hExteriorGap
  exact ⟨hOldGap, hExteriorGap, sub_pos.mp hDifference⟩

/-- A fully rational instance of the analytic constant-convolution no-go.
Both diagonal gaps are `1/4`, but the Dirichlet-to-Neumann response is `9/4`
and the harmonic extension `(1,3)` has energy `-2`. -/
theorem rational_analytic_rankOne_countermodel :
    rankOneOldGap (3 / 4 : ℝ) 1 = 1 / 4 ∧
      rankOneExteriorGap (3 / 4 : ℝ) 1 = 1 / 4 ∧
      rankOneResponse (3 / 4 : ℝ) 1 1 = 9 / 4 ∧
      rankOneOldGap (3 / 4 : ℝ) 1 * 1 ^ 2 +
          2 * (-3 / 4 : ℝ) * 1 * 3 +
          rankOneExteriorGap (3 / 4 : ℝ) 1 * 3 ^ 2 = -2 := by
  norm_num [rankOneOldGap, rankOneExteriorGap, rankOneResponse,
    rankOneResidualSq]

/-! ## The exact final pivot in the two-mode odd sector -/

/-- After the first low mode is eliminated, this is the exact remaining
pivot.  The off-diagonal response cannot in general be omitted. -/
def twoModeFinalPivot
    (lambda1 lambda3 h11 h13 h33 : ℝ) : ℝ :=
  lambda3 - h33 - h13 ^ 2 / (lambda1 - h11)

/-- Completing the square in the two-mode response matrix exhibits the
`h13^2 / (lambda1-h11)` correction to the last pivot. -/
theorem twoMode_completion_identity
    {lambda1 lambda3 h11 h13 h33 x y : ℝ}
    (hfirst : lambda1 - h11 ≠ 0) :
    (lambda1 - h11) * x ^ 2 - 2 * h13 * x * y +
        (lambda3 - h33) * y ^ 2 =
      (lambda1 - h11) *
          (x - h13 / (lambda1 - h11) * y) ^ 2 +
        twoModeFinalPivot lambda1 lambda3 h11 h13 h33 * y ^ 2 := by
  unfold twoModeFinalPivot
  field_simp [hfirst]
  ring

/-- Under positivity of the first pivot, positivity of the determinant is
equivalent to positivity of the exact final pivot. -/
theorem twoMode_determinant_pos_iff_finalPivot_pos
    {lambda1 lambda3 h11 h13 h33 : ℝ}
    (hfirst : 0 < lambda1 - h11) :
    0 < (lambda1 - h11) * (lambda3 - h33) - h13 ^ 2 ↔
      0 < twoModeFinalPivot lambda1 lambda3 h11 h13 h33 := by
  have hfirstNe : lambda1 - h11 ≠ 0 := ne_of_gt hfirst
  have hid :
      (lambda1 - h11) *
          twoModeFinalPivot lambda1 lambda3 h11 h13 h33 =
        (lambda1 - h11) * (lambda3 - h33) - h13 ^ 2 := by
    unfold twoModeFinalPivot
    field_simp [hfirstNe]
  rw [← hid]
  exact mul_pos_iff_of_pos_left hfirst

end

end RHP2Bridge.HodgeLowSectorNoGo
