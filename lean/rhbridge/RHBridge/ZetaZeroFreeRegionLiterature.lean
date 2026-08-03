/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilFormula

/-!
# Unconditional critical-strip edge distance

The logarithmic reciprocal bound is the classical de la Vallee Poussin
zero-free region, reflected by the zeta functional equation.  It assumes
neither RH nor a zero-density conjecture.
-/

namespace RHP2Bridge.ZetaZeroFreeRegionLiterature

open GuinandWeilFormula

/-- Distance of a nontrivial zero from the nearest vertical edge of the open
critical strip. -/
def centeredEdgeDistance (ρ : NontrivialZetaZero) : ℝ :=
  min ρ.val.re (1 - ρ.val.re)

theorem centeredEdgeDistance_pos (ρ : NontrivialZetaZero) :
    0 < centeredEdgeDistance ρ := by
  exact lt_min ρ.property.2.1 (sub_pos.mpr ρ.property.2.2)

/-- Symmetric de la Vallee Poussin zero-free-region consequence, with the
finite low-zero range absorbed into the constant. -/
axiom exists_recip_centeredEdgeDistance_le_log :
  ∃ C : ℝ, 0 ≤ C ∧ ∀ ρ : NontrivialZetaZero,
    (centeredEdgeDistance ρ)⁻¹ ≤ C * Real.log (2 + |ρ.val.im|)

end RHP2Bridge.ZetaZeroFreeRegionLiterature
