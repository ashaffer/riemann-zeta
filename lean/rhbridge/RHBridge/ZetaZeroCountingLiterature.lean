/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilFormula

/-!
# Classical zero-counting consequence

We record the summable weight needed for Stage 4.  It is a direct consequence
of the unconditional Riemann--von Mangoldt zero-counting formula, with zeros
counted according to analytic multiplicity.  It contains no RH assertion.
-/

namespace RHP2Bridge.ZetaZeroCountingLiterature

open GuinandWeilFormula

/-- The height weight arising from one zero-free-region logarithm and two
integrations by parts on a fixed smooth compact test. -/
noncomputable def residualHeightWeight (ρ : NontrivialZetaZero) : ℝ :=
  zeroMultiplicity ρ *
    (Real.log (2 + |ρ.val.im|) / (1 + |ρ.val.im|) ^ 2)

/-- Unconditional Riemann--von Mangoldt summability consequence. -/
axiom summable_residualHeightWeight : Summable residualHeightWeight

/-- Stronger square-sampling weight used for the full form-domain CCM
residual.  Its summability is another immediate Riemann--von Mangoldt
consequence. -/
noncomputable def squareSampleHeightWeight (ρ : NontrivialZetaZero) : ℝ :=
  zeroMultiplicity ρ *
    (Real.log (2 + |ρ.val.im|) ^ 2 / (1 + |ρ.val.im|) ^ 2)

axiom summable_squareSampleHeightWeight : Summable squareSampleHeightWeight

end RHP2Bridge.ZetaZeroCountingLiterature
