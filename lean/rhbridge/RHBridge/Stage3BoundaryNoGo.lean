/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.InnerProductSpace.PiL2

/-!
# Stage 3 boundary-size no-go model

Support saturation, even with a uniform quantitative collar lower bound, does
not exclude a first-crossing radical.  This two-dimensional model isolates the
logical obstruction: the missing theorem must couple the boundary coordinate
to the special zeta kernel, rather than merely control its Hilbert norm.
-/

namespace RHP2Bridge.Stage3BoundaryNoGo

/-- The old one-dimensional sector embedded in the enlarged two-dimensional
space. -/
def oldEmbed (x : ℝ) : ℝ × ℝ := (x, 0)

/-- A nonnegative crossing form whose radical is precisely the new collar
coordinate. -/
def crossingForm (x : ℝ × ℝ) : ℝ := x.1 ^ 2

/-- Its associated symmetric cross form. -/
def crossingCross (x y : ℝ × ℝ) : ℝ := x.1 * y.1

/-- The saturated boundary vector. -/
def boundaryMode : ℝ × ℝ := (0, 1)

theorem old_form_strictlyPositive (x : ℝ) (hx : x ≠ 0) :
    0 < crossingForm (oldEmbed x) := by
  simp only [crossingForm, oldEmbed]
  exact sq_pos_of_ne_zero hx

theorem boundaryMode_nonzero : boundaryMode ≠ 0 := by
  intro h
  have := congrArg Prod.snd h
  norm_num [boundaryMode] at this

theorem boundaryMode_zeroEnergy : crossingForm boundaryMode = 0 := by
  norm_num [crossingForm, boundaryMode]

theorem boundaryMode_radical (y : ℝ × ℝ) :
    crossingCross boundaryMode y = 0 := by
  simp [crossingCross, boundaryMode]

theorem boundaryMode_not_old (x : ℝ) : oldEmbed x ≠ boundaryMode := by
  intro h
  have := congrArg Prod.snd h
  norm_num [oldEmbed, boundaryMode] at this

/-- The collar coordinate has the strongest possible fixed lower bound, yet
the vector remains a nonzero radical vector. -/
theorem boundaryMode_uniformCollarLowerBound :
    1 ≤ |boundaryMode.2| := by
  norm_num [boundaryMode]

/-- Kernel-checked countermodel to the proposed inference from positivity on
the old sector plus quantitative support saturation to nondegeneracy. -/
theorem quantitative_collar_size_does_not_exclude_radical :
    (∀ x : ℝ, x ≠ 0 → 0 < crossingForm (oldEmbed x)) ∧
    boundaryMode ≠ 0 ∧
    crossingForm boundaryMode = 0 ∧
    (∀ y : ℝ × ℝ, crossingCross boundaryMode y = 0) ∧
    (∀ x : ℝ, oldEmbed x ≠ boundaryMode) ∧
    1 ≤ |boundaryMode.2| := by
  exact ⟨old_form_strictlyPositive, boundaryMode_nonzero,
    boundaryMode_zeroEnergy, boundaryMode_radical, boundaryMode_not_old,
    boundaryMode_uniformCollarLowerBound⟩

end RHP2Bridge.Stage3BoundaryNoGo
