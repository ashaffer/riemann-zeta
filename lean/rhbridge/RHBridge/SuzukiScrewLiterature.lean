/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilLiterature

/-!
# Suzuki's screw-kernel realization of the Weil form

This module records the normalization-matched, unconditional identity from
M. Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096,
equation (2.9).  The identity is isolated as a literature axiom because its
proof requires the distributional second derivative of the explicit screw
function and a substantial finite-part integration argument.

No positivity property of the screw kernel is assumed.  Global positive
definiteness of this particular kernel is RH-equivalent in Suzuki's earlier
work, so importing it here would be circular.
-/

namespace RHP2Bridge.SuzukiScrewLiterature

open scoped ArithmeticFunction

noncomputable section

open GeneralZetaWeilForm GuinandWeilFormula

/-- The real Hurwitz--Lerch series `Φ(q,2,c)` needed in Suzuki's explicit
screw function. -/
def realLerchTwo (q c : ℝ) : ℝ :=
  ∑' n : ℕ, q ^ n / (n + c) ^ 2

/-- Suzuki's explicit continuous even function associated with zeta,
equation (1.3), in the same logarithmic coordinate used by RHBridge. -/
def zetaScrewFunction (t : ℝ) : ℝ :=
  -4 * (Real.exp (t / 2) + Real.exp (-t / 2) - 2) +
    (∑ n ∈ Finset.Icc 1 ⌊Real.exp |t|⌋₊,
      Λ n / Real.sqrt n * (|t| - Real.log n)) -
    |t| / 2 * (GlideKernel.quarterDigammaReal 0 - Real.log Real.pi) -
    1 / 4 *
      (realLerchTwo 1 (1 / 4) -
        Real.exp (-|t| / 2) * realLerchTwo (Real.exp (-2 * |t|)) (1 / 4))

/-- The explicit kernel is even, unconditionally and before any positivity
question is posed. -/
theorem zetaScrewFunction_neg (t : ℝ) :
    zetaScrewFunction (-t) = zetaScrewFunction t := by
  simp only [zetaScrewFunction, abs_neg, neg_div, neg_neg]
  ring

/-- The polarized derivative-kernel form on explicit smooth real test data.
Suzuki writes the complex conjugate in the second factor; it is invisible for
the real-valued core used by RHBridge. -/
def screwKernelForm {a : ℝ}
    (φ ψ : SmoothCompactSupportData a) : ℝ :=
  ∫ x in Set.Icc (-a) a, ∫ y in Set.Icc (-a) a,
    zetaScrewFunction (x - y) * deriv φ.toFun y * deriv ψ.toFun x

/-- **Unconditional literature input.**  On the smooth compact-support core,
Suzuki's continuous derivative-kernel form is exactly the arithmetic Weil
form used in this repository.  This is an identity, not a positivity axiom. -/
axiom screwKernelForm_eq_weilForm {a : ℝ}
    (φ : SmoothCompactSupportData a) :
    screwKernelForm φ φ = weilForm a φ.toTestSpace

/-- Positivity of the localized derivative-kernel form, deliberately defined
as a target rather than assumed. -/
def ScrewKernelPositiveAt (a : ℝ) : Prop :=
  ∀ φ : SmoothCompactSupportData a, 0 ≤ screwKernelForm φ φ

/-- The unconditional alignment transfers any future screw-kernel positivity
proof to smooth-core Weil positivity at the same window. -/
theorem smooth_weil_nonneg_of_screwKernelPositiveAt
    {a : ℝ} (h : ScrewKernelPositiveAt a)
    (φ : SmoothCompactSupportData a) :
    0 ≤ weilForm a φ.toTestSpace := by
  rw [← screwKernelForm_eq_weilForm]
  exact h φ

/-- Conversely, positivity on the smooth arithmetic Weil core is precisely
positivity of the aligned localized kernel form. -/
theorem screwKernelPositiveAt_iff_smoothWeilPositive (a : ℝ) :
    ScrewKernelPositiveAt a ↔
      ∀ φ : SmoothCompactSupportData a, 0 ≤ weilForm a φ.toTestSpace := by
  constructor
  · exact smooth_weil_nonneg_of_screwKernelPositiveAt
  · intro h φ
    rw [screwKernelForm_eq_weilForm]
    exact h φ

end

end RHP2Bridge.SuzukiScrewLiterature
