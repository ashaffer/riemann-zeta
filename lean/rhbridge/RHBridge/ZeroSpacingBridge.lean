/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import Mathlib

/-!
# What ordinate rigidity can prove

This file records the elementary logical core of a proposed zero-spacing
route.  If a set of complex points is closed under reflection across the
critical line and the imaginary-part map is injective on that set, then every
point lies on the critical line.

For the nontrivial zeta zeros, reflection closure is supplied by the
functional equation.  Consequently, *pointwise* ordinate injectivity is not
an independent GUE-style input: it is already an equivalent reformulation of
RH (for distinct zero locations).  Asymptotic pair correlation is much weaker
and does not supply the injectivity hypothesis used below.
-/

namespace RHP2Bridge.ZeroSpacingBridge

open scoped ComplexConjugate

/-- Distinct points of `Z` never have the same ordinate. -/
def OrdinateInjective (Z : Set ℂ) : Prop :=
  ∀ ⦃z w : ℂ⦄, z ∈ Z → w ∈ Z → z.im = w.im → z = w

/-- `Z` is closed under the horizontal critical-line reflection
`z ↦ 1 - conj z`, which preserves the ordinate. -/
def CriticalReflectionClosed (Z : Set ℂ) : Prop :=
  ∀ ⦃z : ℂ⦄, z ∈ Z → (1 - conj z) ∈ Z

/-- Reflection closure plus ordinate injectivity puts every point on
`re z = 1/2`.  This is the precise reason a pointwise zero-spacing condition
would prove RH, and also why that condition is essentially RH in disguise. -/
theorem criticalLine_of_ordinateInjective
    (Z : Set ℂ) (hreflect : CriticalReflectionClosed Z)
    (hinj : OrdinateInjective Z) ⦃z : ℂ⦄ (hz : z ∈ Z) :
    z.re = 1 / 2 := by
  have hmem : (1 - conj z) ∈ Z := hreflect hz
  have him : (1 - conj z).im = z.im := by simp
  have heq : 1 - conj z = z := hinj hmem hz him
  have hre := congrArg Complex.re heq
  simp at hre
  linarith

/-- Conversely, a set contained in the critical line has injective ordinate
map on its distinct locations.  Multiplicity is deliberately not represented
by a `Set`; an occurrence-level version would additionally assert simplicity. -/
theorem ordinateInjective_of_criticalLine
    (Z : Set ℂ) (hline : ∀ ⦃z : ℂ⦄, z ∈ Z → z.re = 1 / 2) :
    OrdinateInjective Z := by
  intro z w hz hw him
  apply Complex.ext
  · rw [hline hz, hline hw]
  · exact him

end RHP2Bridge.ZeroSpacingBridge
