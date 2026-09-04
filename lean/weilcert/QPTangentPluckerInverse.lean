/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Bilinear Pluecker and tangent-ruling identities

This file mechanically certifies the exact algebra used to distinguish a
fixed-secant conic from a tangent ruling in the QP four-cycle problem.  It
does not assert the open global zero-mode restriction estimate.
-/

namespace QPTangentPluckerInverse

def det2 (a b c d : ℤ) : ℤ := a * d - b * c

def bilinear
    (k11 k12 k21 k22 x1 x2 y1 y2 : ℤ) : ℤ :=
  x1 * (k11 * y1 + k12 * y2) + x2 * (k21 * y1 + k22 * y2)

def pair4
    (k11 k12 k21 k22 e11 e12 e21 e22 : ℤ) : ℤ :=
  k11 * e11 + k12 * e12 + k21 * e21 + k22 * e22

def detPolar
    (e11 e12 e21 e22 v11 v12 v21 v22 : ℤ) : ℤ :=
  e11 * v22 + v11 * e22 - e12 * v21 - v12 * e21

/-- The two-by-two bilinear Pluecker identity. -/
theorem bilinear_plucker
    (k11 k12 k21 k22 a1 a2 A1 A2 b1 b2 B1 B2 : ℤ) :
    bilinear k11 k12 k21 k22 a1 a2 b1 b2
          * bilinear k11 k12 k21 k22 A1 A2 B1 B2
      - bilinear k11 k12 k21 k22 a1 a2 B1 B2
          * bilinear k11 k12 k21 k22 A1 A2 b1 b2
      = det2 k11 k12 k21 k22
          * det2 a1 A1 a2 A2 * det2 b1 B1 b2 B2 := by
  simp [bilinear, det2]
  ring

/-- The determinant of a difference of two rank-one product matrices. -/
theorem rank_one_difference_determinant
    (a1 a2 A1 A2 b1 b2 B1 B2 : ℤ) :
    det2 (a1 * b1 - A1 * B1) (a1 * b2 - A1 * B2)
        (a2 * b1 - A2 * B1) (a2 * b2 - A2 * B2)
      = -(det2 a1 A1 a2 A2 * det2 b1 B1 b2 B2) := by
  simp [det2]
  ring

/-- On an equal bilinear level, the two cross levels multiply to the full
fixed-secant conic parameter `L^2 + det(K)det(E)`. -/
theorem equal_level_cross_factor
    (k11 k12 k21 k22 a1 a2 A1 A2 b1 b2 B1 B2 L : ℤ)
    (hfirst : bilinear k11 k12 k21 k22 a1 a2 b1 b2 = L)
    (hsecond : bilinear k11 k12 k21 k22 A1 A2 B1 B2 = L) :
    bilinear k11 k12 k21 k22 a1 a2 B1 B2
          * bilinear k11 k12 k21 k22 A1 A2 b1 b2
      = L ^ 2 + det2 k11 k12 k21 k22
          * det2 (a1 * b1 - A1 * B1) (a1 * b2 - A1 * B2)
              (a2 * b1 - A2 * B1) (a2 * b2 - A2 * B2) := by
  rw [rank_one_difference_determinant]
  have hp := bilinear_plucker
    k11 k12 k21 k22 a1 a2 A1 A2 b1 b2 B1 B2
  rw [hfirst, hsecond] at hp
  nlinarith

/-- Exact determinant polynomial along a matrix line. -/
theorem determinant_line
    (e11 e12 e21 e22 v11 v12 v21 v22 t : ℤ) :
    det2 (e11 + t * v11) (e12 + t * v12)
        (e21 + t * v21) (e22 + t * v22)
      = det2 e11 e12 e21 e22
        + t * detPolar e11 e12 e21 e22 v11 v12 v21 v22
        + t ^ 2 * det2 v11 v12 v21 v22 := by
  simp [det2, detPolar]
  ring

/-- Three points in one affine arithmetic progression, on one determinant
layer and one linear level, force a rank-one tangent direction. -/
theorem three_term_ruling_inverse
    (k11 k12 k21 k22 e11 e12 e21 e22 v11 v12 v21 v22 : ℤ)
    (hlevel0 : pair4 k11 k12 k21 k22 e11 e12 e21 e22 = 0)
    (hlevel1 : pair4 k11 k12 k21 k22
      (e11 + v11) (e12 + v12) (e21 + v21) (e22 + v22) = 0)
    (hdet1 : det2 (e11 + v11) (e12 + v12) (e21 + v21) (e22 + v22)
      = det2 e11 e12 e21 e22)
    (hdet2 : det2 (e11 + 2 * v11) (e12 + 2 * v12)
        (e21 + 2 * v21) (e22 + 2 * v22)
      = det2 e11 e12 e21 e22) :
    pair4 k11 k12 k21 k22 v11 v12 v21 v22 = 0 ∧
      det2 v11 v12 v21 v22 = 0 ∧
      detPolar e11 e12 e21 e22 v11 v12 v21 v22 = 0 := by
  constructor
  · simp [pair4] at hlevel0 hlevel1 ⊢
    linear_combination hlevel1 - hlevel0
  · have hline1 := determinant_line
      e11 e12 e21 e22 v11 v12 v21 v22 1
    have hline2 := determinant_line
      e11 e12 e21 e22 v11 v12 v21 v22 2
    simp only [one_mul, one_pow] at hline1
    norm_num at hline2
    constructor <;> simp [det2, detPolar] at hdet1 hdet2 hline1 hline2 ⊢ <;>
      nlinarith

/-- If `E` and `E+V` lie on one determinant layer and one linear level,
then the doubled midpoint `Y=2E+V` is polar-orthogonal to `V` and satisfies
the exact binary-norm equation `det Y=4 det E-det V`. -/
theorem secant_midpoint_normal_form
    (k11 k12 k21 k22 e11 e12 e21 e22 v11 v12 v21 v22 : ℤ)
    (hlevelE : pair4 k11 k12 k21 k22 e11 e12 e21 e22 = 0)
    (hlevelV : pair4 k11 k12 k21 k22 v11 v12 v21 v22 = 0)
    (hdet : det2 (e11 + v11) (e12 + v12) (e21 + v21) (e22 + v22)
      = det2 e11 e12 e21 e22) :
    pair4 k11 k12 k21 k22
        (2 * e11 + v11) (2 * e12 + v12)
        (2 * e21 + v21) (2 * e22 + v22) = 0 ∧
      detPolar (2 * e11 + v11) (2 * e12 + v12)
        (2 * e21 + v21) (2 * e22 + v22) v11 v12 v21 v22 = 0 ∧
      det2 (2 * e11 + v11) (2 * e12 + v12)
        (2 * e21 + v21) (2 * e22 + v22)
        = 4 * det2 e11 e12 e21 e22 - det2 v11 v12 v21 v22 := by
  constructor
  · simp [pair4] at hlevelE hlevelV ⊢
    linear_combination 2 * hlevelE + hlevelV
  · constructor <;> simp [det2, detPolar] at hdet ⊢ <;> nlinarith

/-- Three physical transitions around a shared edge force the determinant
of every Cartesian cross-neighbor pair through an exact six-product
identity. -/
theorem shared_edge_six_product_identity
    (a x y b B c C d D e E : ℤ) :
    (8 * x * b * d) * (8 * y * e * c) * (8 * a * B * C)
      - (8 * x * B * D) * (8 * y * E * C) * (8 * a * b * c)
      = 512 * a * x * y * b * B * c * C * (d * e - D * E) := by
  ring

/-- Pluecker for the Cartesian cross-determinant table.  Vanishing of a
two-by-two table minor forces one of the two arm determinants to vanish. -/
theorem cross_determinant_plucker
    (d1 D1 d2 D2 e1 E1 e2 E2 : ℤ) :
    (d1 * e1 - D1 * E1) * (d2 * e2 - D2 * E2)
      - (d1 * e2 - D1 * E2) * (d2 * e1 - D2 * E1)
      = -(det2 d1 d2 D1 D2 * det2 e1 e2 E1 E2) := by
  simp [det2]
  ring

/-! ## Fixed-row-pair level audit -/

/-- The row determinant is controlled by the two short cross defects through
the exact identity `d Delta = a V-A v`. -/
theorem fixed_row_determinant_defect_identity
    (a m A M c d : ℤ) :
    d * (a * M - m * A)
      = a * (M * d - A * c) - A * (m * d - a * c) := by
  ring

/-- Denominator-cleared form of the exact pinned-level expansion used in
the fixed-row-pair codegree theorem.  Here `Q` denotes `q^3`, the two
product errors are `8abc-Q` and `8ABc-Q`, and
`J=b(md-ac)-B(Md-Ac)`. -/
theorem fixed_row_pinned_level_expansion
    (Q a m A M b B c d : ℤ) :
    8 * a * A * c *
        (b * (m * d - a * c) - B * (M * d - A * c))
      = -Q * d * (a * M - m * A)
        + A * (8 * a * b * c - Q) * (m * d - a * c)
        - a * (8 * A * B * c - Q) * (M * d - A * c) := by
  ring

/-- Exact residual determinant in the physical affine RDP-saturation grid. -/
theorem affine_transition_grid_determinant (m i j : ℤ) :
    (m + 2 * i) * (m + 2 * j + 2)
      - (m + 2 * i + 1) * (m + 2 * j + 1)
      = 2 * (i - j) - 1 := by
  ring

/-- The two grid triples both lie on the affine plane with coordinate sum
`3m`; this is the exact first-order cancellation behind the quadratic
hard-window cost. -/
theorem affine_transition_grid_sums (m i j : ℤ) :
    let a := m - 2 * i - 2 * j - 2
    let b := m + 2 * i
    let B := m + 2 * i + 1
    let c := m + 2 * j + 2
    let C := m + 2 * j + 1
    (a + b + c = 3 * m) ∧ (a + B + C = 3 * m) := by
  dsimp
  constructor <;> ring

/-- The full-integer tangent witness has determinant `-2h^2`. -/
theorem tangent_color_determinant (m h : ℤ) :
    det2 m (-(m - 2 * h)) (-(m - h)) (m - 3 * h) = -2 * h ^ 2 := by
  simp [det2]
  ring

/-- Its affine carrier parameter has a literally constant bilinear level. -/
theorem tangent_level_constant (m h t : ℤ) :
    bilinear m (-(m - 2 * h)) (-(m - h)) (m - 3 * h)
      (m + h + t) (m + 2 * h + t) (m - h - t) (m + h - t)
      = -2 * h ^ 2 * (m + 3 * h) := by
  simp [bilinear]
  ring

/-- The tangent carrier directions satisfy the exact bilinear equation
`p^T K q=0`. -/
theorem tangent_direction_equation (m h : ℤ) :
    bilinear m (-(m - 2 * h)) (-(m - h)) (m - 3 * h)
      1 1 (-1) (-1) = 0 := by
  simp [bilinear]
  ring

/-- A fixed-gap tangent secant has determinant `2h^2 d^2`. -/
theorem tangent_secant_determinant (m h t d : ℤ) :
    let a1 := m + h + t
    let a2 := m + 2 * h + t
    let b1 := m - h - t
    let b2 := m + h - t
    let A1 := m + h + t + d
    let A2 := m + 2 * h + t + d
    let B1 := m - h - t - d
    let B2 := m + h - t - d
    det2 (a1 * b1 - A1 * B1) (a1 * b2 - A1 * B2)
        (a2 * b1 - A2 * B1) (a2 * b2 - A2 * B2)
      = 2 * h ^ 2 * d ^ 2 := by
  dsimp
  simp [det2]
  ring

/-! ## A residual algebraic model -/

/-- The model secants lie on one trace-zero, determinant-one quadric. -/
theorem residual_secant_invariants (t : ℤ) :
    det2 t 1 (-(t ^ 2) - 1) (-t) = 1 ∧ t + (-t) = 0 := by
  constructor
  · simp [det2]
    ring
  · ring

/-- Distinct model secants have a full-rank chord, so no tangent ruling
contains two of them. -/
theorem residual_secant_chord (s t : ℤ) :
    det2 (t - s) 0 ((-(t ^ 2) - 1) - (-(s ^ 2) - 1)) ((-t) - (-s))
      = -(t - s) ^ 2 := by
  simp [det2]
  ring

/-- Each residual secant is nevertheless a difference of two rank-one
integer matrices on one fixed trace level. -/
theorem residual_rank_one_realization (L t : ℤ) :
    let m11 := t
    let m12 := 1
    let m21 := t * (L - t)
    let m22 := L - t
    let n11 := 0
    let n12 := 0
    let n21 := t * L + 1
    let n22 := L
    (det2 m11 m12 m21 m22 = 0) ∧
      (det2 n11 n12 n21 n22 = 0) ∧
      (m11 + m22 = L) ∧ (n11 + n22 = L) ∧
      (m11 - n11 = t) ∧ (m12 - n12 = 1) ∧
      (m21 - n21 = -(t ^ 2) - 1) ∧ (m22 - n22 = -t) := by
  dsimp
  simp [det2]
  ring

/-- The exceptional full-rank displacement `det V=4 Delta` really has a
tangent-line fiber. -/
theorem antipodal_tangent_fiber (t : ℤ) :
    let e11 := -1
    let e12 := t
    let e21 := 0
    let e22 := -1
    let v11 := 2
    let v12 := 0
    let v21 := 0
    let v22 := 2
    (e11 - e22 = 0) ∧
      ((e11 + v11) - (e22 + v22) = 0) ∧
      (det2 e11 e12 e21 e22 = 1) ∧
      (det2 (e11 + v11) (e12 + v12) (e21 + v21) (e22 + v22) = 1) ∧
      (det2 v11 v12 v21 v22 = 4) := by
  dsimp
  simp [det2]

end QPTangentPluckerInverse
