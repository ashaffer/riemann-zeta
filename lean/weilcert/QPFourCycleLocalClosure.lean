/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact local ledgers for the QP four-cycle attack

This file certifies the algebraic identities used by the lossless Fejer/Airy
local closure and by the reduction from mixed reciprocal-strip restriction to
self restriction.  It deliberately does not assert the open hereditary
reciprocal-strip estimate or the global mask-sensitive assembly theorem.
-/

namespace QPFourCycleLocalClosure

/-! ## Critical rational exponents -/

/-- The harmonic and completion savings in the proposed (nonautomatic) split
add to the gap-closing threshold. -/
theorem proposed_split_ledger : (1 : ℚ) / 12 + 1 / 16 = 7 / 48 := by
  norm_num

/-- Two comparable Fejer factors at harmonic threshold `D^(-1/12)` give the
exact allowed physical cluster exponent. -/
theorem two_fejer_cluster_ledger :
    (33 : ℚ) / 16 - 17 / 16 + ((1 : ℚ) / 12) / 4 = 49 / 48 := by
  norm_num

/-- A full `q^(1/3)` completion block moves the regular Fejer height by only
`D^(-5/16)`. -/
theorem regular_fejer_drift_ledger :
    (17 : ℚ) / 16 + 11 / 16 - 33 / 16 = -(5 / 16 : ℚ) := by
  norm_num

/-- The scaled Airy coordinate moves by `D^(1/48)` per completion and by
`D^(17/24)` over a full block. -/
theorem airy_motion_ledger :
    (2 * ((17 : ℚ) / 16) / 3 - ((33 : ℚ) / 16) / 3 = 1 / 48) ∧
      (1 / 48 + 11 / 16 = 17 / 24) := by
  constructor <;> norm_num

/-- Vector Plancherel recovers the complete Airy Fourier-spread loss. -/
theorem airy_vector_closure_ledger :
    (49 : ℚ) / 48 - 25 / 48 = 1 / 2 := by
  norm_num

/-! ## Self restriction is sufficient after Fejer summation -/

/-- Starting from the mixed constant obtained by Fourier Cauchy, adjoining
the two cardinality powers, taking the convolution norm, and inserting the
two height-one Fejer weights gives
`D^(5/4) U^(-11/8) V^(-11/8)`. -/
theorem self_to_mixed_weighted_fejer_ledger (u v : ℚ) :
    (((1 / 2 : ℚ) + (u + v) / 4 + (1 + u) + (1 + v)) / 2
        - 2 * u - 2 * v)
      = 5 / 4 - (11 / 8) * (u + v) := by
  ring

/-- Relative to sharp `min(U,V)` RSR, the symmetric Fourier-Cauchy route
loses only one eighth of the width imbalance in the convolution norm. -/
theorem symmetric_over_sharp_gap (m M : ℚ) :
    (5 / 4 - (11 / 8) * (m + M))
        - (5 / 4 - (5 / 4) * m - (3 / 2) * M)
      = (M - m) / 8 := by
  ring

/-! ## Exact shifted-product normal form -/

/-- Two nearby products with horizontal separation `h` and quotient
separation `k` satisfy the first completed-square identity. -/
theorem shifted_product_discriminant_left
    (a n h k C : ℤ) :
    let e := a * (n + k) - C
    let f := (a + h) * n - C
    let g := e - f
    let Y := a * k + h * n + h * k
    Y ^ 2 - (g - h * k) ^ 2 = 4 * h * k * (C + e) := by
  dsimp
  ring

/-- The companion completed-square identity for the translated product. -/
theorem shifted_product_discriminant_right
    (a n h k C : ℤ) :
    let e := a * (n + k) - C
    let f := (a + h) * n - C
    let g := e - f
    let Y := a * k + h * n + h * k
    Y ^ 2 - (g + h * k) ^ 2 = 4 * h * k * (C + f) := by
  dsimp
  ring

/-- In odd midpoint coordinates, the two physical products become a thin
split-complex product: one coordinate is the product sum and the other is
the chord determinant. -/
theorem shifted_product_midpoint_normal_form
    (a n h k C : ℤ) :
    let e := a * (n + k) - C
    let f := (a + h) * n - C
    let A := 2 * a + h
    let B := 2 * n + k
    (A * B - h * k = 4 * C + 2 * (e + f)) ∧
      (A * k - B * h = 2 * (e - f)) := by
  dsimp
  constructor <;> ring

end QPFourCycleLocalClosure
