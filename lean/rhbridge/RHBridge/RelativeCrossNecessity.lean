/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ScaleUniformLeakage

/-!
# Necessity of the relative old--collar cross bound

The Schur determinant condition is not merely a convenient sufficient
estimate.  For two nonnegative diagonal energies it is equivalent to
nonnegativity of the quadratic form on their entire mixed plane.  Thus a
uniform proof of the relative contraction must use arithmetic information
strong enough to prove the corresponding mixed positivity; support leakage
alone cannot imply it.
-/

namespace RHP2Bridge.RelativeCrossNecessity

noncomputable section

/-- Nonnegativity of a scalar quadratic polynomial forces its discriminant
to be nonpositive.  The positive `D` case is proved by evaluating at the
minimizer `-C/D`; the zero case follows by testing an explicit direction. -/
theorem cross_sq_le_of_quadratic_nonneg {A C D : ℝ}
    (hA : 0 ≤ A) (hD : 0 ≤ D)
    (hline : ∀ t : ℝ, 0 ≤ A + 2 * t * C + t ^ 2 * D) :
    C ^ 2 ≤ A * D := by
  rcases hD.eq_or_lt with rfl | hDpos
  · by_cases hC : C = 0
    · simp [hC]
    · have hp := hline (-(A + 1) / C)
      have hcancel : 2 * (-(A + 1) / C) * C = -2 * (A + 1) := by
        field_simp [hC]
      rw [hcancel] at hp
      norm_num at hp
      nlinarith
  · have h := hline (-C / D)
    have hDne : D ≠ 0 := ne_of_gt hDpos
    field_simp [hDne] at h
    nlinarith

/-- Exact scalar Schur equivalence. -/
theorem quadratic_nonneg_iff_cross_sq_le {A C D : ℝ}
    (hA : 0 ≤ A) (hD : 0 ≤ D) :
    (∀ t : ℝ, 0 ≤ A + 2 * t * C + t ^ 2 * D) ↔ C ^ 2 ≤ A * D := by
  constructor
  · exact cross_sq_le_of_quadratic_nonneg hA hD
  · intro hdet t
    have hscaled : (t * C) ^ 2 ≤ A * (t ^ 2 * D) := by
      have hm := mul_le_mul_of_nonneg_left hdet (sq_nonneg t)
      nlinarith
    have hdiag : 0 ≤ t ^ 2 * D := mul_nonneg (sq_nonneg t) hD
    have := SupportDecomposition.add_two_mul_nonneg_of_cross_sq_le
      hA hdiag hscaled
    nlinarith

/-- The same equivalence with a named quadratic-plane predicate, convenient
for operator block arguments. -/
def MixedPlaneNonnegative (A C D : ℝ) : Prop :=
  ∀ t : ℝ, 0 ≤ A + 2 * t * C + t ^ 2 * D

theorem mixedPlaneNonnegative_iff {A C D : ℝ}
    (hA : 0 ≤ A) (hD : 0 ≤ D) :
    MixedPlaneNonnegative A C D ↔ C ^ 2 ≤ A * D :=
  quadratic_nonneg_iff_cross_sq_le hA hD

end

end RHP2Bridge.RelativeCrossNecessity
