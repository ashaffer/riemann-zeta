/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Order.OrderClosed
import Mathlib.Tactic

/-!
# Cofinal vanishing shifts already force global positivity

Let `floor a` be the bottom of a quadratic form on the window of support `a`.
Canonical nesting makes this function antitone.  If a cofinal exhaustion has
strictly admissible shifts

`shift n < floor (support n)`

and those shifts tend to zero, then `floor a ≥ 0` at every fixed support.
Conversely, global nonnegativity admits the explicit strictly negative shifts
`-1/(n+1)`, which tend to zero.  Thus the existence of a cofinal admissible
vanishing-shift sequence is exactly as strong as global nonnegativity of an
antitone family of spectral floors.

For completed zeta Weil forms, identifying global nonnegativity with RH is a
separate instance of the Weil criterion; no zeta-specific fact or RH
assumption occurs in this file.
-/

namespace RHBridge.CofinalShiftPositivity

open Filter
open scoped Topology

noncomputable section

/-- A canonical sequence of strictly negative shifts approaching zero. -/
def canonicalNegativeShift (n : ℕ) : ℝ :=
  -(1 / ((n : ℝ) + 1))

theorem canonicalNegativeShift_neg (n : ℕ) :
    canonicalNegativeShift n < 0 := by
  unfold canonicalNegativeShift
  apply neg_lt_zero.mpr
  exact one_div_pos.mpr (by positivity)

theorem canonicalNegativeShift_tendsto_zero :
    Tendsto canonicalNegativeShift atTop (𝓝 0) := by
  change Tendsto (fun n : ℕ ↦ -(1 / ((n : ℝ) + 1))) atTop (𝓝 0)
  simpa only [neg_zero] using
    (tendsto_one_div_add_atTop_nhds_zero_nat (𝕜 := ℝ)).neg

/-- The decisive direction: cofinal admissibility plus convergence of the
shifts to zero forces every fixed spectral floor to be nonnegative. -/
theorem nonnegative_of_cofinal_admissible_vanishing
    (floor : ℝ → ℝ) (support : ℕ → ℝ) (shift : ℕ → ℝ)
    (hfloor : Antitone floor)
    (hsupport : Tendsto support atTop atTop)
    (hshift : Tendsto shift atTop (𝓝 0))
    (hadmissible : ∀ n, shift n < floor (support n)) :
    ∀ a, 0 ≤ floor a := by
  intro a
  apply le_of_tendsto hshift
  filter_upwards [hsupport.eventually (eventually_ge_atTop a)] with n hn
  exact (hadmissible n).le.trans (hfloor hn)

/-- The converse requires no quantitative lower margin: if every floor is
nonnegative, the canonical negative shifts are strictly admissible. -/
theorem exists_cofinal_admissible_vanishing_of_nonnegative
    (floor : ℝ → ℝ) (support : ℕ → ℝ)
    (hfloor : ∀ a, 0 ≤ floor a) :
    ∃ shift : ℕ → ℝ,
      Tendsto shift atTop (𝓝 0) ∧
        ∀ n, shift n < floor (support n) := by
  refine ⟨canonicalNegativeShift, canonicalNegativeShift_tendsto_zero, ?_⟩
  intro n
  exact (canonicalNegativeShift_neg n).trans_le (hfloor (support n))

/-- For an antitone spectral-floor family and a cofinal exhaustion, existence
of any strictly admissible shift sequence tending to zero is equivalent to
global nonnegativity. -/
theorem exists_cofinal_admissible_vanishing_iff_nonnegative
    (floor : ℝ → ℝ) (support : ℕ → ℝ)
    (hfloor : Antitone floor)
    (hsupport : Tendsto support atTop atTop) :
    (∃ shift : ℕ → ℝ,
      Tendsto shift atTop (𝓝 0) ∧
        ∀ n, shift n < floor (support n)) ↔
      ∀ a, 0 ≤ floor a := by
  constructor
  · rintro ⟨shift, hshift, hadmissible⟩
    exact nonnegative_of_cofinal_admissible_vanishing
      floor support shift hfloor hsupport hshift hadmissible
  · exact exists_cofinal_admissible_vanishing_of_nonnegative floor support

end

end RHBridge.CofinalShiftPositivity
