/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRational
import RHBridge.P2PoleScaleCenters

/-!
# Exact rational source of the canonical `p = 2` pole center

The analytic pole enclosure uses the stored spherical scale centers and the
finite Taylor cores.  Both inputs have exact rational sources, so the center
passed to the final entry arithmetic is itself the cast of one rational.
-/

namespace RHP2Bridge

namespace RatPoly

/-- Rational source of one scale-centered finite pole coefficient. -/
noncomputable def p2PoleTaylorCoeffScaleCenterQ (n : Fin 48) : ℚ :=
  p2ScaleCenterQ n.val / 2 * p2PoleTaylorRationalCoreQ n.val

theorem p2PoleTaylorCoeffScaleCenter_eq_cast (n : Fin 48) :
    p2PoleTaylorCoeffScaleCenter n =
      (p2PoleTaylorCoeffScaleCenterQ n : ℝ) := by
  unfold p2PoleTaylorCoeffScaleCenter
    p2PoleTaylorCoeffScaleCenterQ
  rw [p2PoleTaylorRationalCore_eq_cast]
  push_cast
  norm_num

/-- Entire unsigned pole-product center as an exact rational. -/
noncomputable def p2EntryTaylorPoleCenterQ (e : P2EntryIndex) : ℚ :=
  2 * p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.col) *
    p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.row)

theorem p2EntryTaylorPoleCenter_eq_cast (e : P2EntryIndex) :
    p2EntryTaylorPoleCenter e =
      (p2EntryTaylorPoleCenterQ e : ℝ) := by
  unfold p2EntryTaylorPoleCenter p2EntryTaylorPoleCenterQ
  rw [p2PoleTaylorCoeffScaleCenter_eq_cast,
    p2PoleTaylorCoeffScaleCenter_eq_cast]
  push_cast
  norm_num

end RatPoly

end RHP2Bridge
