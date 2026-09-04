/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# Exact algebra for the rank-one H tangent/residual split

This file certifies only the polynomial identities used in the tangent and
affine-packet arguments.  It deliberately does not assert the open uniform
residual degree-product theorem.
-/

namespace QPRankOneHTangentResidual

/-- The reduced-ratio tangent parametrization is exactly determinant zero. -/
theorem tangent_parametrization
    (g u v d : ℤ) :
    (g * u) * (v * d) = (g * v) * (u * d) := by
  ring

/-- A linear row/color packet has a genuinely quadratic product drift. -/
theorem affine_packet_product
    (a c r p t : ℤ) :
    (a + r * t) * (c - p * t)
      = a * c + (r * c - a * p) * t - r * p * t ^ 2 := by
  ring

/-- The mixed second difference of the corner determinant factors into the
two coordinate gaps. -/
theorem determinant_mixed_difference
    (b B c C u U p P : ℤ) :
    (b * c - B * C)
      - (b * (c - p) - B * (C - P))
      - ((b - u) * c - (B - U) * C)
      + ((b - u) * (c - p) - (B - U) * (C - P))
      = u * p - U * P := by
  ring

/-- Exact error ledger behind the two-sided affine-gap comparison. -/
theorem affine_gap_determinant_ledger
    (b B c C r s x y p P u U L1 L2 R1 R2 : ℤ)
    (hp : x * p = c * r - L1)
    (hP : x * P = C * r - L2)
    (hu : y * u = b * s - R1)
    (hU : y * U = B * s - R2) :
    x * y * (u * p - U * P)
      = (b * c - B * C) * r * s
        - c * r * R1 - b * s * L1 + L1 * R1
        + C * r * R2 + B * s * L2 - L2 * R2 := by
  calc
    x * y * (u * p - U * P)
        = (x * p) * (y * u) - (x * P) * (y * U) := by ring
    _ = (b * c - B * C) * r * s
          - c * r * R1 - b * s * L1 + L1 * R1
          + C * r * R2 + B * s * L2 - L2 * R2 := by
      rw [hp, hP, hu, hU]
      ring

/-- Exact Cramer/Pluecker identity for all left-by-right pairs around one
residual transition edge.  The orientation is
`p=(b,B), q=(C,c), u=(D,d), v=(e,E)`. -/
theorem shared_edge_pluecker
    (b B c C d D e E : ℤ) :
    (b * c - B * C) * (D * E - d * e)
      = (c * D - C * d) * (b * E - B * e)
        - (b * d - B * D) * (e * c - E * C) := by
  ring

/-- The left vector is recovered exactly from its two determinant
coordinates in the base `(p,q)`. -/
theorem shared_edge_left_cramer
    (b B c C d D : ℤ) :
    let delta := b * c - B * C
    let k := b * d - B * D
    let r := c * D - C * d
    delta * D = r * b + k * C ∧ delta * d = r * B + k * c := by
  dsimp
  constructor <;> ring

/-- The right vector is recovered exactly from its two determinant
coordinates in the same base. -/
theorem shared_edge_right_cramer
    (b B c C e E : ℤ) :
    let delta := b * c - B * C
    let ell := e * c - E * C
    let t := b * E - B * e
    delta * e = ell * b + t * C ∧ delta * E = ell * B + t * c := by
  dsimp
  constructor <;> ring

/-- Polynomial error ledger which proves that every left-by-right cross
determinant is `O(D)` once all six physical product errors are `O(qD)`. -/
theorem shared_edge_product_error_ledger
    (a b B c C x d D y e E L1 L2 R1 R2 : ℤ)
    (hL1 : x * d = a * c + L1)
    (hL2 : x * D = a * C + L2)
    (hR1 : y * e = a * b + R1)
    (hR2 : y * E = a * B + R2) :
    x * y * (d * e - D * E)
      = a ^ 2 * (b * c - B * C)
        + a * c * R1 + a * b * L1 + L1 * R1
        - a * C * R2 - a * B * L2 - L2 * R2 := by
  calc
    x * y * (d * e - D * E)
        = (x * d) * (y * e) - (x * D) * (y * E) := by ring
    _ = a ^ 2 * (b * c - B * C)
          + a * c * R1 + a * b * L1 + L1 * R1
          - a * C * R2 - a * B * L2 - L2 * R2 := by
      rw [hL1, hL2, hR1, hR2]
      ring

/-- If `g*U+1=m*b`, multiplication by the base determinant transports the
center-gap inverse step to the opposite physical color modulo `b`. -/
theorem center_inverse_step_transference
    (b B c C g U m : ℤ)
    (hg : g = B - b)
    (hU : g * U + 1 = m * b) :
    (b * c - B * C) * U
      = C + b * ((c - C) * U - m * C) := by
  rw [hg] at hU
  linear_combination -C * hU

/-- The symmetric color-gap inverse step transports to `-b` modulo `C`. -/
theorem color_inverse_step_transference
    (b B c C h V n : ℤ)
    (hh : h = c - C)
    (hV : h * V + 1 = n * C) :
    (b * c - B * C) * V
      = -b + C * (b * n - (B - b) * V) := by
  rw [hh] at hV
  linear_combination b * hV

/-- Eliminating the two opposite physical endpoints from the transported
inverse steps gives the exact shared-edge lift coupling. -/
theorem inverse_lift_coupling
    (b C delta U V R S : ℤ)
    (hU : delta * U = C + b * R)
    (hV : delta * V = -b + C * S) :
    b * (1 + R * S) = delta * (S * U - V) ∧
      C * (1 + R * S) = delta * (U + R * V) := by
  constructor
  · linear_combination -S * hU + hV
  · linear_combination -hU - R * hV

end QPRankOneHTangentResidual
