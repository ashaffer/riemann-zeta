/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact reciprocal-translate midpoint and tangent identities

This file mechanically certifies the polynomial identities used in the
reciprocal translate-intersection reduction.  It deliberately does not assert
the open varying-direction near-square counting estimate.
-/

namespace QPReciprocalTranslateNormalForm

/-- The two product errors become radial and tangent midpoint coordinates. -/
theorem midpoint_identities (a n m h M : ℤ) :
    let e := a * n - M
    let f := (a + h) * m - M
    let k := n - m
    let X := 2 * a + h
    let Y := n + m
    (X * k - Y * h = 2 * (e - f)) ∧
      (X * Y - h * k - 4 * M = 2 * (e + f)) := by
  dsimp
  constructor <;> ring

/-- The midpoint coordinates invert to the original two products. -/
theorem midpoint_reconstruction (X Y h k M : ℤ) :
    let a2 := X - h
    let n2 := Y + k
    let m2 := Y - k
    (a2 * n2 - 4 * M =
        (X * Y - h * k - 4 * M) + (X * k - Y * h)) ∧
      ((X + h) * m2 - 4 * M =
        (X * Y - h * k - 4 * M) - (X * k - Y * h)) := by
  dsimp
  constructor <;> ring

/-- After `h=g*s`, `k=g*r`, the tangent coordinate is exactly the error
difference and the split-square coordinate is exactly the error sum. -/
theorem primitive_tangent_identities
    (a n m g r s M : ℤ) :
    let h := g * s
    let k := g * r
    let e := a * n - M
    let f := (a + h) * m - M
    let X := 2 * a + h
    let Y := n + m
    let T := r * X + s * Y
    let Z := r * X - s * Y
    n - m = k →
      (g * Z = 2 * (e - f)) ∧
      (T ^ 2 - Z ^ 2 - 4 * r * s * (4 * M + g ^ 2 * r * s)
        = 8 * r * s * (e + f)) := by
  dsimp
  intro hnm
  have hm : m = n - g * r := by
    linear_combination -hnm
  rw [hm]
  constructor
  · ring
  · ring

/-- The primitive CRT masks recover the original midpoint coordinates. -/
theorem primitive_mask_reconstruction (X Y r s : ℤ) :
    let T := r * X + s * Y
    let Z := r * X - s * Y
    (T + Z = 2 * r * X) ∧ (T - Z = 2 * s * Y) := by
  dsimp
  constructor <;> ring

/-- The exact-center discriminant factors into four integral factors.  The
analytic use additionally cancels the nonzero factor `4*r*s`. -/
theorem exact_center_factorization (M g r s d : ℤ) :
    (2 * r * s * d) ^ 2 - 4 * r * s * (4 * M + g ^ 2 * r * s)
      = 4 * r * s * (r * s * (d - g) * (d + g) - 4 * M) := by
  ring

/-- The square target has a literal tangent-parabola family. -/
theorem square_target_tangent_family (Q t h : ℤ) :
    ((Q + t) * (Q - t) - Q ^ 2 = -(t ^ 2)) ∧
      ((Q + t + h) * (Q - t - h) - Q ^ 2 = -((t + h) ^ 2)) := by
  constructor <;> ring

end QPReciprocalTranslateNormalForm
