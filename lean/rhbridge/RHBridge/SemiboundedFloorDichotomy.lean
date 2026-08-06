/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Order.Filter.AtTopBot.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# The abstract semibounded spectral-floor dichotomy

For a nested family of finite-window quadratic forms, its bottom spectral
value is antitone in the window size.  This file records the order-theoretic
part of the resulting global dichotomy.

A floor family is uniformly bounded below exactly when one fixed strict shift
lies below every floor.  If an antitone family has no such bound, then its
floors tend to `-∞` as the support tends to `+∞`.

The arguments are completely abstract.  In particular, this file contains no
zeta-specific input and makes no claim that a particular Weil floor is (or is
not) uniformly bounded below.
-/

namespace RHBridge.SemiboundedFloorDichotomy

open Filter

/-- A family of real spectral floors admits one support-independent lower
bound.  Writing the bound as `-C` matches the quadratic-form convention
`Q(f) ≥ -C ‖f‖²`; no sign restriction on `C` is needed. -/
def UniformlyLowerBounded (floor : ℝ → ℝ) : Prop :=
  ∃ C : ℝ, ∀ a : ℝ, -C ≤ floor a

/-- There is one strict shift that lies below every finite-window floor. -/
def HasStrictGlobalShift (floor : ℝ → ℝ) : Prop :=
  ∃ σ : ℝ, ∀ a : ℝ, σ < floor a

/-- Extend a floor family that is physically relevant only above `a₀` to the
whole real line by freezing it below `a₀`. -/
def truncateBelow (floor : ℝ → ℝ) (a₀ a : ℝ) : ℝ :=
  floor (max a a₀)

@[simp] theorem truncateBelow_eq_of_le (floor : ℝ → ℝ) {a₀ a : ℝ}
    (h : a₀ ≤ a) :
    truncateBelow floor a₀ a = floor a := by
  simp [truncateBelow, h]

/-- Freezing below the first physical support preserves antitonicity. -/
theorem truncateBelow_antitone (floor : ℝ → ℝ) (a₀ : ℝ)
    (hfloor : Antitone floor) :
    Antitone (truncateBelow floor a₀) := by
  intro a b hab
  exact hfloor (max_le_max hab le_rfl)

/-- A common lower bound for the frozen extension is exactly a common lower
bound on the physical tail `a₀ ≤ a`. -/
theorem truncateBelow_uniformlyLowerBounded_iff
    (floor : ℝ → ℝ) (a₀ : ℝ) :
    UniformlyLowerBounded (truncateBelow floor a₀) ↔
      ∃ C : ℝ, ∀ a : ℝ, a₀ ≤ a → -C ≤ floor a := by
  constructor
  · rintro ⟨C, hC⟩
    refine ⟨C, ?_⟩
    intro a ha
    simpa [truncateBelow, ha] using hC a
  · rintro ⟨C, hC⟩
    refine ⟨C, ?_⟩
    intro a
    exact hC (max a a₀) (le_max_right a a₀)

/-- A uniform lower bound can always be made strict, and conversely a strict
global shift is in particular a uniform lower bound. -/
theorem uniformlyLowerBounded_iff_hasStrictGlobalShift (floor : ℝ → ℝ) :
    UniformlyLowerBounded floor ↔ HasStrictGlobalShift floor := by
  constructor
  · rintro ⟨C, hC⟩
    refine ⟨-C - 1, ?_⟩
    intro a
    linarith [hC a]
  · rintro ⟨σ, hσ⟩
    refine ⟨-σ, ?_⟩
    intro a
    simpa using (hσ a).le

/-- Failure of support-uniform semiboundedness forces an antitone floor family
to diverge to `-∞` along increasing supports. -/
theorem tendsto_atBot_of_antitone_of_not_uniformlyLowerBounded
    (floor : ℝ → ℝ) (hfloor : Antitone floor)
    (hunbounded : ¬ UniformlyLowerBounded floor) :
    Tendsto floor atTop atBot := by
  rw [tendsto_atTop_atBot_iff_of_antitone hfloor]
  intro b
  by_contra hbelow
  apply hunbounded
  rw [uniformlyLowerBounded_iff_hasStrictGlobalShift]
  refine ⟨b, ?_⟩
  intro a
  exact lt_of_not_ge (not_exists.mp hbelow a)

/-- For an antitone real floor, tending to `-∞` is exactly the failure of a
support-independent lower bound. -/
theorem tendsto_atBot_iff_not_uniformlyLowerBounded
    (floor : ℝ → ℝ) (hfloor : Antitone floor) :
    Tendsto floor atTop atBot ↔ ¬ UniformlyLowerBounded floor := by
  constructor
  · intro htend hbounded
    rcases hbounded with ⟨C, hC⟩
    rcases (tendsto_atTop_atBot.mp htend) (-C - 1) with ⟨A, hA⟩
    linarith [hC A, hA A le_rfl]
  · exact tendsto_atBot_of_antitone_of_not_uniformlyLowerBounded floor hfloor

/-- Every antitone real floor is either uniformly bounded below or diverges to
`-∞`.  The preceding equivalence shows that these alternatives are mutually
exclusive. -/
theorem uniformlyLowerBounded_or_tendsto_atBot
    (floor : ℝ → ℝ) (hfloor : Antitone floor) :
    UniformlyLowerBounded floor ∨ Tendsto floor atTop atBot := by
  by_cases hbounded : UniformlyLowerBounded floor
  · exact Or.inl hbounded
  · exact Or.inr
      (tendsto_atBot_of_antitone_of_not_uniformlyLowerBounded floor hfloor hbounded)

/-- Global nonnegativity is one (strong) source of a uniform lower bound. -/
theorem uniformlyLowerBounded_of_nonnegative
    (floor : ℝ → ℝ) (hfloor : ∀ a : ℝ, 0 ≤ floor a) :
    UniformlyLowerBounded floor := by
  exact ⟨0, by simpa using hfloor⟩

end RHBridge.SemiboundedFloorDichotomy
