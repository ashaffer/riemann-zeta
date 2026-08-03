/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.LocalizationLiterature

/-!
# Cancellation-sensitive prime activation

The crude prime-shell bound discards the exact Hilbert identity

`2 ⟪f,T_h f⟫ = 2 ‖f‖² - ‖f-T_h f‖²`.

This file retains the nonnegative shift-defect term.  The complete activation
loss is therefore the shell mass bound minus a weighted nonlocal Dirichlet
energy.  This is an exact identity, not an inequality or positivity premise.
-/

namespace RHP2Bridge.ActivationCancellation

open scoped ArithmeticFunction

noncomputable section

open GeneralZetaWeilForm SmoothSupportPropagation LocalizationLiterature

/-- Squared full-line distance between the zero extension and its translate. -/
def intervalShiftDefect (a u : ℝ) (f : TestSpace a) : ℝ :=
  ‖AutocorrelationPlancherel.toFullLineL2
      (IntervalZeroExtension.zeroExtensionFn a f)
      (IntervalZeroExtension.zeroExtensionFn_memLp a f) -
    AutocorrelationPlancherel.translateL2 u
      (IntervalZeroExtension.zeroExtensionFn a f)
      (IntervalZeroExtension.zeroExtensionFn_memLp a f)‖ ^ 2

theorem intervalShiftDefect_nonneg (a u : ℝ) (f : TestSpace a) :
    0 ≤ intervalShiftDefect a u f := sq_nonneg _

/-- Standard compact-support fact: a translate by at least the diameter of
`[-a,a]` has zero autocorrelation (endpoint overlap is null). -/
axiom intervalAutocorrelation_eq_zero_of_two_mul_le
    {a u : ℝ} (f : TestSpace a) (h : 2 * a ≤ |u|) :
    AutocorrelationPlancherel.intervalAutocorrelation a u f = 0

/-- **Standard Hilbert-space literature input.** Translation is unitary, so
expanding the squared distance gives twice mass minus twice autocorrelation.
This contains no zeta-specific or positivity information. -/
axiom two_intervalAutocorrelation_eq_two_norm_sq_sub_shiftDefect
    (a u : ℝ) (f : TestSpace a) :
    2 * AutocorrelationPlancherel.intervalAutocorrelation a u f =
      2 * ‖f‖ ^ 2 - intervalShiftDefect a u f

/-- Weighted nonlocal Dirichlet energy of all prime powers newly activated
between two support scales. -/
def activationShellDefect (a b : ℝ) (f : TestSpace a) : ℝ :=
  ∑ n ∈ activePrimePowers b \ activePrimePowers a,
    Λ n / Real.sqrt n * intervalShiftDefect a (Real.log n) f

/-- Fourier multiplier of the weighted prime-shift defect energy. -/
def activationDefectSymbol (a b ξ : ℝ) : ℝ :=
  ∑ n ∈ activePrimePowers b \ activePrimePowers a,
    2 * (Λ n / Real.sqrt n) *
      (1 - Real.cos (2 * Real.pi * Real.log n * ξ))

/-- **Standard Plancherel literature input.** The nonlocal shift-defect energy
is the Fourier energy weighted by its explicit nonnegative symbol. -/
axiom activationShellDefect_eq_fourier (a b : ℝ) (f : TestSpace a) :
    activationShellDefect a b f =
      ∫ ξ : ℝ, activationDefectSymbol a b ξ * fourierEnergy a f ξ

theorem activationDefectSymbol_nonneg (a b ξ : ℝ) :
    0 ≤ activationDefectSymbol a b ξ := by
  unfold activationDefectSymbol
  apply Finset.sum_nonneg
  intro n _
  have hw : 0 ≤ Λ n / Real.sqrt n :=
    div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _)
  have hc : 0 ≤ 1 - Real.cos (2 * Real.pi * Real.log n * ξ) := by
    linarith [Real.neg_one_le_cos (2 * Real.pi * Real.log n * ξ),
      Real.cos_le_one (2 * Real.pi * Real.log n * ξ)]
  positivity

/-- The defect symbol necessarily vanishes at zero frequency.  Therefore no
positive pointwise `L²` spectral gap can come from prime-shift cancellation
alone; the pole/archimedean low-frequency energy must participate. -/
@[simp] theorem activationDefectSymbol_zero (a b : ℝ) :
    activationDefectSymbol a b 0 = 0 := by
  simp [activationDefectSymbol]

theorem no_positive_uniform_symbol_floor (a b δ : ℝ) (hδ : 0 < δ) :
    ¬ ∀ ξ : ℝ, δ ≤ activationDefectSymbol a b ξ := by
  intro h
  have := h 0
  simp only [activationDefectSymbol_zero] at this
  linarith

theorem activationShellDefect_nonneg (a b : ℝ) (f : TestSpace a) :
    0 ≤ activationShellDefect a b f := by
  unfold activationShellDefect
  apply Finset.sum_nonneg
  intro n _
  exact mul_nonneg
    (div_nonneg ArithmeticFunction.vonMangoldt_nonneg (Real.sqrt_nonneg _))
    (intervalShiftDefect_nonneg a (Real.log n) f)

/-- Exact cancellation-sensitive formula for the newly activated prime shell.
The previous mass-only upper bound is recovered by dropping the final
nonnegative term. -/
theorem activationLoss_eq_shellWeight_mul_norm_sq_sub_defect
    {a b : ℝ} (f : LogarithmicFormDomain a) :
    activationLoss (b := b) f =
      activationShellWeight a b * ‖f.val‖ ^ 2 -
        activationShellDefect a b f.val := by
  unfold activationLoss activationShellWeight activationShellDefect
  rw [Finset.sum_mul, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro n hn
  unfold primePowerTerm
  rw [show 2 * Λ n / Real.sqrt n *
      AutocorrelationPlancherel.intervalAutocorrelation a (Real.log n) f.val =
      (Λ n / Real.sqrt n) *
        (2 * AutocorrelationPlancherel.intervalAutocorrelation
          a (Real.log n) f.val) by ring]
  rw [two_intervalAutocorrelation_eq_two_norm_sq_sub_shiftDefect]
  ring

/-- A prime power newly activated after support `a` has shift at least the
diameter `2a` of the old window. -/
theorem two_mul_le_log_of_mem_activationShell
    {a b : ℝ} {n : ℕ}
    (hn : n ∈ activePrimePowers b \ activePrimePowers a) :
    2 * a ≤ Real.log n := by
  have hnB := (Finset.mem_sdiff.mp hn).1
  have hnA := (Finset.mem_sdiff.mp hn).2
  simp only [activePrimePowers, Finset.mem_filter, Finset.mem_Ioc] at hnB
  obtain ⟨⟨hnpos, _hnfloorB⟩, hnpp, _hnlogB⟩ := hnB
  by_contra h
  have hnlogA : Real.log n < 2 * a := lt_of_not_ge h
  have hncast : (0 : ℝ) < n := by exact_mod_cast hnpos
  have hnexp : (n : ℝ) ≤ Real.exp (2 * a) := by
    apply le_of_lt
    rw [← Real.exp_log hncast]
    exact Real.exp_lt_exp.mpr hnlogA
  apply hnA
  simp only [activePrimePowers, Finset.mem_filter, Finset.mem_Ioc]
  exact ⟨⟨hnpos, Nat.le_floor hnexp⟩, hnpp, hnlogA⟩

/-- Decisive event-driven simplification: every newly activated prime term is
exactly zero on the embedded old support.  Hence the old block suffers no
activation loss at all; only collar and cross interactions remain. -/
theorem activationLoss_eq_zero {a b : ℝ}
    (f : LogarithmicFormDomain a) :
    activationLoss (b := b) f = 0 := by
  unfold activationLoss
  apply Finset.sum_eq_zero
  intro n hn
  unfold primePowerTerm
  rw [intervalAutocorrelation_eq_zero_of_two_mul_le f.val]
  · ring
  · exact (two_mul_le_log_of_mem_activationShell hn).trans
      (le_abs_self (Real.log n))

theorem weilForm_nestedSupport_eq {a b : ℝ} (hab : a ≤ b)
    (f : LogarithmicFormDomain a) :
    weilForm b (NestedSupport.nestedSupport a b f.val) =
      logarithmicWeilForm a f := by
  rw [NestedSupport.weilForm_nestedSupport hab]
  change logarithmicWeilForm a f - activationLoss (b := b) f = _
  rw [activationLoss_eq_zero, sub_zero]

theorem nestedSupport_nonneg_of_positiveAt {a b : ℝ} (hab : a ≤ b)
    (hpositive : UniformPropagationToRH.PositiveAt a)
    (f : LogarithmicFormDomain a) :
    0 ≤ weilForm b (NestedSupport.nestedSupport a b f.val) := by
  rw [weilForm_nestedSupport_eq hab]
  exact hpositive f

/-- Cancellation-sensitive reserve condition for the old block.  Unlike the
crude criterion, a large shell coefficient is harmless when the corresponding
prime translations have large defect energy. -/
def HasActivationReserve {a b : ℝ} (f : LogarithmicFormDomain a) : Prop :=
  activationShellWeight a b * ‖f.val‖ ^ 2 -
      activationShellDefect a b f.val ≤ logarithmicWeilForm a f

theorem activationLoss_le_of_hasActivationReserve
    {a b : ℝ} (f : LogarithmicFormDomain a)
    (h : HasActivationReserve (b := b) f) :
    activationLoss (b := b) f ≤ logarithmicWeilForm a f := by
  rw [activationLoss_eq_shellWeight_mul_norm_sq_sub_defect]
  exact h

theorem nestedSupport_nonneg_of_hasActivationReserve
    {a b : ℝ} (hab : a ≤ b) (f : LogarithmicFormDomain a)
    (h : HasActivationReserve (b := b) f) :
    0 ≤ weilForm b (NestedSupport.nestedSupport a b f.val) :=
  nestedSupport_nonneg_of_activationLoss_le hab f
    (activationLoss_le_of_hasActivationReserve f h)

/-- The cancellation-sensitive condition is genuinely weaker than the crude
mass reserve: dropping a nonnegative defect recovers it. -/
theorem hasActivationReserve_of_crude_reserve
    {a b : ℝ} (f : LogarithmicFormDomain a)
    (h : activationShellWeight a b * ‖f.val‖ ^ 2 ≤
      logarithmicWeilForm a f) :
    HasActivationReserve (b := b) f := by
  unfold HasActivationReserve
  linarith [activationShellDefect_nonneg a b f.val]

end

end RHP2Bridge.ActivationCancellation
