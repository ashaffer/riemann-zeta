/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.SuzukiScrewLiterature

/-!
# The prime-ramp component of Suzuki's screw kernel

For one prime power `n`, Suzuki's continuous kernel contains

`Λ(n) / sqrt(n) * (|t| - log n)₊`.

Two integrations by parts turn its distributional second derivative, the two
point masses at `± log n`, into the negative shifted-autocorrelation term of
the Weil form.  The elementary integration-by-parts statement is isolated as
a narrow axiom below; all arithmetic normalization and finite summation are
proved in Lean.  It assumes neither RH nor positivity.
-/

namespace RHP2Bridge.SuzukiPrimeRamp

open scoped ArithmeticFunction

noncomputable section

open GeneralZetaWeilForm GuinandWeilFormula

/-- Positive part of the ramp beginning at the logarithmic prime shift. -/
def primeRampKernel (n : ℕ) (t : ℝ) : ℝ :=
  Λ n / Real.sqrt n * max (|t| - Real.log n) 0

/-- Derivative-kernel form contributed by a single prime power. -/
def singlePrimeRampForm {a : ℝ}
    (φ : SmoothCompactSupportData a) (n : ℕ) : ℝ :=
  ∫ x in Set.Icc (-a) a, ∫ y in Set.Icc (-a) a,
    primeRampKernel n (x - y) * deriv φ.toFun y * deriv φ.toFun x

/-- The finite ramp contribution active in the support window. -/
def primeRampForm {a : ℝ} (φ : SmoothCompactSupportData a) : ℝ :=
  ∑ n ∈ activePrimePowers a, singlePrimeRampForm φ n

/-- Elementary two-variable integration-by-parts identity for one ramp.

This is intentionally narrower than the imported full Suzuki identity.  Its
proof requires splitting the square along `x-y=±log n`, applying the
fundamental theorem of calculus on each polygonal region, and using the
compact-support endpoint conditions. -/
axiom singlePrimeRampForm_eq_neg_primePowerTerm
    {a : ℝ} (φ : SmoothCompactSupportData a) (n : ℕ) :
    singlePrimeRampForm φ n = -primePowerTerm a φ.toTestSpace n

/-- The complete finite prime-ramp block is exactly the negative of the Weil
prime term, including the factor `2`, von Mangoldt weight, square-root
normalization, and logarithmic shift. -/
theorem primeRampForm_eq_neg_primeTerm {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    primeRampForm φ = -primeTerm a φ.toTestSpace := by
  unfold primeRampForm primeTerm
  simp_rw [singlePrimeRampForm_eq_neg_primePowerTerm]
  rw [← Finset.sum_neg_distrib]

/-- Removing the now-aligned prime ramps from Suzuki's full kernel leaves
exactly the pole plus archimedean part of the arithmetic Weil form. -/
theorem screwKernelForm_sub_primeRampForm {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    SuzukiScrewLiterature.screwKernelForm φ φ - primeRampForm φ =
      poleTerm a φ.toTestSpace + archimedeanTerm a φ.toTestSpace := by
  rw [SuzukiScrewLiterature.screwKernelForm_eq_weilForm,
    primeRampForm_eq_neg_primeTerm]
  unfold weilForm
  ring

end

end RHP2Bridge.SuzukiPrimeRamp
