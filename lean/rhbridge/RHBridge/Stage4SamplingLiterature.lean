/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ZetaZeroCountingLiterature
import RHBridge.NestedSupport
import RHBridge.SupportDecomposition

/-!
# Upper zero-sampling bound on the logarithmic form domain

This is the unconditional upper (Bessel) estimate obtained from local zeta
zero counting and the local Plancherel--Polya inequality.  It is not a lower
frame bound and contains no RH assertion.
-/

namespace RHP2Bridge.Stage4SamplingLiterature

open GuinandWeilFormula GeneralZetaWeilForm

/-- Positive graph quantity defining the logarithmic form topology. -/
noncomputable def logarithmicGraphNormSq (a : ℝ) (f : TestSpace a) : ℝ :=
  ‖f‖ ^ 2 +
    ∫ xi, Real.log (1 + (2 * Real.pi * xi) ^ 2) * fourierEnergy a f xi

/-- The two complementary samples occurring in the polarized Weil sum. -/
noncomputable def zeroSampleEnergy (a : ℝ) (f : TestSpace a) : ℝ :=
  ∑' ρ : NontrivialZetaZero, (zeroMultiplicity ρ : ℝ) *
    (‖bilateralLaplace a f (ρ.val - 1 / 2)‖ ^ 2 +
      ‖bilateralLaplace a f (1 / 2 - ρ.val)‖ ^ 2)

/-- Multiplicity-weighted Plancherel--Polya upper sampling inequality.  The
constant depends only on the fixed time support. -/
axiom zeroSampleEnergy_le_logarithmicGraphNormSq
    (a : ℝ) : ∃ C : ℝ, 0 ≤ C ∧
      ∀ f : LogarithmicFormDomain a,
        0 ≤ zeroSampleEnergy a f.val ∧
        zeroSampleEnergy a f.val ≤ C * logarithmicGraphNormSq a f.val

/-- Polarized Guinand--Weil plus infinite-series Cauchy--Schwarz. -/
axiom weilCross_abs_le_zeroSampleEnergy
    {a : ℝ} (f g : LogarithmicFormDomain a) :
    |SupportDecomposition.weilCross a f.val g.val| ≤
      Real.sqrt (zeroSampleEnergy a f.val) *
        Real.sqrt (zeroSampleEnergy a g.val)

/-- The sample energy is intrinsic to the full-line zero extension, hence is
unchanged when a fixed test is represented in a larger support interval. -/
axiom zeroSampleEnergy_nestedLogarithmicSupport
    {a b : ℝ} (hab : a ≤ b) (f : LogarithmicFormDomain a) :
    zeroSampleEnergy b (NestedSupport.nestedLogarithmicSupport hab f).val =
      zeroSampleEnergy a f.val

end RHP2Bridge.Stage4SamplingLiterature
