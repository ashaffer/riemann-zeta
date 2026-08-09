/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# A bare relative factor is not a propagation mechanism

Once the source value is positive, existence of an unspecified positive factor
`theta` with `theta * source ≤ target` is equivalent to positivity of the
target. A useful support-transfer theorem must therefore construct or bound
its factor from independent analytic data; it cannot merely quantify over one.
-/

namespace RHP2Bridge.RelativeFactorObstruction

/-- With a positive source, an unspecified positive relative lower-bound factor
exists exactly when the target is already positive. -/
theorem exists_pos_factor_mul_le_iff
    {source target : ℝ} (hsource : 0 < source) :
    (∃ theta : ℝ, 0 < theta ∧ theta * source ≤ target) ↔ 0 < target := by
  constructor
  · rintro ⟨theta, htheta, hle⟩
    exact lt_of_lt_of_le (mul_pos htheta hsource) hle
  · intro htarget
    have hsource_ne : source ≠ 0 := ne_of_gt hsource
    refine ⟨target / source, div_pos htarget hsource, ?_⟩
    rw [div_mul_cancel₀ target hsource_ne]

/-- The equality formulation makes the same logical point: after target
positivity is known, the factor can be chosen as the target/source ratio. -/
theorem exists_pos_factor_mul_eq_iff
    {source target : ℝ} (hsource : 0 < source) :
    (∃ theta : ℝ, 0 < theta ∧ theta * source = target) ↔ 0 < target := by
  constructor
  · rintro ⟨theta, htheta, rfl⟩
    exact mul_pos htheta hsource
  · intro htarget
    have hsource_ne : source ≠ 0 := ne_of_gt hsource
    refine ⟨target / source, div_pos htarget hsource, ?_⟩
    exact div_mul_cancel₀ target hsource_ne

end RHP2Bridge.RelativeFactorObstruction
