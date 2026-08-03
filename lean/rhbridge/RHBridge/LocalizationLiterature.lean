/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ExplicitSmoothCutoff

/-!
# Standard localization inputs and the prime-shell bound

This module isolates two routine literature inputs that are not worth
rebuilding inside Mathlib for the RH program:

* autocorrelation is bounded above by squared `L²` norm (Cauchy--Schwarz and
  translation unitarity);
* multiplication by the explicit Lipschitz-smooth cutoff preserves the
  logarithmic Fourier form domain, with the usual first-Sobolev cost.

Neither input contains arithmetic positivity, Weil positivity, or RH.  From
the first, the complete newly activated prime shell is bounded in Lean by an
explicit finite von Mangoldt weight.
-/

namespace RHP2Bridge.LocalizationLiterature

open scoped ArithmeticFunction

noncomputable section

open GeneralZetaWeilForm GuinandWeilFormula
  SmoothSupportPropagation ExplicitSmoothCutoff

/-- Standard Cauchy--Schwarz bound for a unitary translate. -/
axiom intervalAutocorrelation_le_norm_sq (a u : ℝ) (f : TestSpace a) :
  AutocorrelationPlancherel.intervalAutocorrelation a u f ≤ ‖f‖ ^ 2

/-- Physical first-Sobolev energy of an explicit smooth representative. -/
def smoothH1Energy {a : ℝ} (φ : SmoothCompactSupportData a) : ℝ :=
  ∫ x : ℝ, |φ x| ^ 2 + |deriv φ.toFun x| ^ 2

/-- Logarithmically weighted Fourier energy before passage to the form
domain subtype. -/
def logarithmicFourierEnergy (a : ℝ) (f : TestSpace a) : ℝ :=
  ∫ ξ : ℝ, Real.log (1 + (2 * Real.pi * ξ) ^ 2) * fourierEnergy a f ξ

/-- **Standard smooth-multiplier literature input.**  The explicit old piece
belongs to the logarithmic domain and its logarithmic Fourier energy is
controlled at first-Sobolev order.  The coefficient displays the full
transition-width dependence proved for the cutoff derivative.

This is a conventional Plancherel/product-rule estimate, not an RH-related
assumption. -/
axiom explicitOld_logarithmicLocalization
    {b r a : ℝ} (φ : SmoothCompactSupportData b)
    (hr : 0 < r) (hra : r < a) :
    InLogarithmicDomain a (explicitOldSmoothData φ r a hr hra).toTestSpace ∧
      logarithmicFourierEnergy a
          (explicitOldSmoothData φ r a hr hra).toTestSpace ≤
        (2 + 8 * transitionSlopeBound ^ 2 / (a - r) ^ 2) *
          smoothH1Energy φ

/-- Explicit total weight of prime powers activated from `a` to `b`. -/
def activationShellWeight (a b : ℝ) : ℝ :=
  ∑ n ∈ activePrimePowers b \ activePrimePowers a,
    2 * Λ n / Real.sqrt n

theorem activationShellWeight_nonneg (a b : ℝ) :
    0 ≤ activationShellWeight a b := by
  unfold activationShellWeight
  exact Finset.sum_nonneg fun n _ =>
    div_nonneg (mul_nonneg (by norm_num) ArithmeticFunction.vonMangoldt_nonneg)
      (Real.sqrt_nonneg _)

theorem activationShellWeight_eq_zero_of_active_eq {a b : ℝ}
    (hactive : activePrimePowers b = activePrimePowers a) :
    activationShellWeight a b = 0 := by
  simp [activationShellWeight, hactive]

theorem primePowerTerm_le_weight_mul_norm_sq
    (a : ℝ) (f : TestSpace a) (n : ℕ) :
    primePowerTerm a f n ≤
      (2 * Λ n / Real.sqrt n) * ‖f‖ ^ 2 := by
  unfold primePowerTerm
  have hc : 0 ≤ 2 * Λ n / Real.sqrt n :=
    div_nonneg (mul_nonneg (by norm_num) ArithmeticFunction.vonMangoldt_nonneg)
      (Real.sqrt_nonneg _)
  exact mul_le_mul_of_nonneg_left
    (intervalAutocorrelation_le_norm_sq a (Real.log n) f) hc

/-- Every newly activated prime shell is bounded by its explicit arithmetic
weight times squared old-vector mass.  All summation and normalization are
proved here; only the standard single-shift Cauchy--Schwarz inequality is
imported. -/
theorem activationLoss_le_shellWeight_mul_norm_sq
    {a b : ℝ} (f : LogarithmicFormDomain a) :
    activationLoss (b := b) f ≤
      activationShellWeight a b * ‖f.val‖ ^ 2 := by
  unfold activationLoss activationShellWeight
  calc
    (∑ n ∈ activePrimePowers b \ activePrimePowers a,
        primePowerTerm a f.val n) ≤
      ∑ n ∈ activePrimePowers b \ activePrimePowers a,
        (2 * Λ n / Real.sqrt n) * ‖f.val‖ ^ 2 := by
          exact Finset.sum_le_sum fun n _ =>
            primePowerTerm_le_weight_mul_norm_sq a f.val n
    _ = (∑ n ∈ activePrimePowers b \ activePrimePowers a,
          2 * Λ n / Real.sqrt n) * ‖f.val‖ ^ 2 := by
      rw [Finset.sum_mul]

/-- A concrete sufficient reserve condition: it is enough for the old Weil
energy to dominate the explicit shell weight times `L²` mass. -/
theorem activationLoss_le_of_shellWeight_reserve
    {a b : ℝ} (f : LogarithmicFormDomain a)
    (hreserve : activationShellWeight a b * ‖f.val‖ ^ 2 ≤
      logarithmicWeilForm a f) :
    activationLoss (b := b) f ≤ logarithmicWeilForm a f :=
  (activationLoss_le_shellWeight_mul_norm_sq f).trans hreserve

/-- The explicit shell reserve is sufficient for nonnegativity of the old
block after embedding into the larger support window. -/
theorem nestedSupport_nonneg_of_shellWeight_reserve
    {a b : ℝ} (hab : a ≤ b) (f : LogarithmicFormDomain a)
    (hreserve : activationShellWeight a b * ‖f.val‖ ^ 2 ≤
      logarithmicWeilForm a f) :
    0 ≤ weilForm b (NestedSupport.nestedSupport a b f.val) :=
  nestedSupport_nonneg_of_activationLoss_le hab f
    (activationLoss_le_of_shellWeight_reserve f hreserve)

end

end RHP2Bridge.LocalizationLiterature
