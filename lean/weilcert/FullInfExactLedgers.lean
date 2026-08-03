/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import FullInfTransfer

/-!
# Project-specific exact `FULLINF` ledgers

This application module instantiates the generic two-block inequalities from
`CertFramework` and `FullInfTransfer` at the exact rational constants used by
three Riemann-zeta certificate windows.  It deliberately remains separate
from those reusable algebra modules.

The declarations retain their original namespaces so downstream project files
can keep the established fully qualified names after importing this module.
Nothing here identifies the block hypotheses with the zeta Weil form; those
analytic and finite-matrix obligations are discharged elsewhere.
-/

namespace CertFramework

/-! ## Scalar ledgers -/

/-- The strict two-block estimate for the `p = 2`, `L = 7/4` ledger. -/
theorem fullinf_p2_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (22699 / 10 ^ 9) * (x ^ 2 + y ^ 2)
      < (227 / 10 ^ 7) * x ^ 2 + (1093 / 1000) * y ^ 2
        - 2 * (212 / 10 ^ 12) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

/-- The strict two-block estimate for the `p = 3`, `L = 497/200` ledger. -/
theorem fullinf_p3_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (999 / 10 ^ 13) * (x ^ 2 + y ^ 2)
      < (1 / 10 ^ 10) * x ^ 2 + (161 / 1000) * y ^ 2
        - 2 * (721 / 10 ^ 13) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

/-- The strict two-block estimate for the `n = 4`, `L = 749/250` ledger. -/
theorem fullinf_n4_block_lower_bound (x y : ℝ) (hxy : (x, y) ≠ (0, 0)) :
    (99 / 10 ^ 17) * (x ^ 2 + y ^ 2)
      < (1 / 10 ^ 15) * x ^ 2 + (289 / 1000) * y ^ 2
        - 2 * (106 / 10 ^ 11) * x * y := by
  apply two_by_two_strict_lower_bound
  · norm_num
  · norm_num
  · norm_num
  · exact hxy

end CertFramework

namespace FullInfTransfer

open scoped RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-! ## Projection-level ledgers -/

/-- The `L = 7/4` ledger lifted to an arbitrary orthogonal projection. -/
theorem fullinf_p2_projection_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, (227 / 10 ^ 7) * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, (1093 / 1000) * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ (212 / 10 ^ 12) * ‖u‖ * ‖w‖)
    {f : E} (hf : f ≠ 0) :
    (22699 / 10 ^ 9) * ‖f‖ ^ 2 < B f f := by
  apply starProjection_strict_lower_bound B U
    (227 / 10 ^ 7) (1093 / 1000) (212 / 10 ^ 12) (22699 / 10 ^ 9)
    hsymm hfinite hcomplement hcross
  · norm_num
  · norm_num
  · norm_num
  · exact hf

/-- The `L = 497/200` ledger lifted to an arbitrary orthogonal projection. -/
theorem fullinf_p3_projection_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, (1 / 10 ^ 10) * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, (161 / 1000) * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ (721 / 10 ^ 13) * ‖u‖ * ‖w‖)
    {f : E} (hf : f ≠ 0) :
    (999 / 10 ^ 13) * ‖f‖ ^ 2 < B f f := by
  apply starProjection_strict_lower_bound B U
    (1 / 10 ^ 10) (161 / 1000) (721 / 10 ^ 13) (999 / 10 ^ 13)
    hsymm hfinite hcomplement hcross
  · norm_num
  · norm_num
  · norm_num
  · exact hf

/-- The `L = 749/250` ledger lifted to an arbitrary orthogonal projection. -/
theorem fullinf_n4_projection_lower_bound
    (B : E →ₗ[ℝ] E →ₗ[ℝ] ℝ) (U : Submodule ℝ E)
    [U.HasOrthogonalProjection]
    (hsymm : ∀ x y, B x y = B y x)
    (hfinite : ∀ u ∈ U, (1 / 10 ^ 15) * ‖u‖ ^ 2 ≤ B u u)
    (hcomplement : ∀ w ∈ Uᗮ, (289 / 1000) * ‖w‖ ^ 2 ≤ B w w)
    (hcross : ∀ u ∈ U, ∀ w ∈ Uᗮ,
      |B u w| ≤ (106 / 10 ^ 11) * ‖u‖ * ‖w‖)
    {f : E} (hf : f ≠ 0) :
    (99 / 10 ^ 17) * ‖f‖ ^ 2 < B f f := by
  apply starProjection_strict_lower_bound B U
    (1 / 10 ^ 15) (289 / 1000) (106 / 10 ^ 11) (99 / 10 ^ 17)
    hsymm hfinite hcomplement hcross
  · norm_num
  · norm_num
  · norm_num
  · exact hf

end FullInfTransfer
