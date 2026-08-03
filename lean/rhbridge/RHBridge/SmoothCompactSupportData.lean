/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import LegendreScaledL2

/-!
# Smooth compact-support representatives

This small data layer stores an actual globally smooth real function together
with its compact-interval support bound.  It is separated from the zeta-zero
and explicit-formula theory so constructions on test representatives do not
inherit that theory's large dependency graph.
-/

namespace RHP2Bridge.GuinandWeilFormula

/-- A globally smooth representative supported in `[-a,a]`. -/
structure SmoothCompactSupportData (a : ℝ) where
  toFun : ℝ → ℝ
  smooth : ContDiff ℝ (⊤ : ℕ∞) toFun
  support_subset : Function.support toFun ⊆ LegendreScaledL2.Interval a

namespace SmoothCompactSupportData

instance (a : ℝ) : CoeFun (SmoothCompactSupportData a) (fun _ ↦ ℝ → ℝ) :=
  ⟨toFun⟩

end SmoothCompactSupportData

end RHP2Bridge.GuinandWeilFormula
