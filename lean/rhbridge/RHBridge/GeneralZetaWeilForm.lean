/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ZetaWeilForm
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Analysis.Complex.ExponentialBounds

/-!
# The compact-support zeta Weil quadratic form

This file defines the pole, archimedean, and prime-power sides of the zeta
Weil quadratic form on the zero extension of `L²[-a,a]`.  The prime sum is
finite because only `log n < 2a` can meet the autocorrelation support.

This is the arithmetic side of the Guinand--Weil explicit formula.  Mathlib
does not presently contain the theorem identifying it with a sum over the
nontrivial zeros of `riemannZeta`; no such identity is assumed here.
-/

namespace RHP2Bridge.GeneralZetaWeilForm

open scoped ENNReal InnerProductSpace RealInnerProductSpace ArithmeticFunction

noncomputable section

/-- Compact-support test space, represented on its minimal symmetric interval. -/
abbrev TestSpace (a : ℝ) := LegendreScaledL2.IntervalL2 a

/-- Squared ordinary-frequency Fourier density of the zero extension. -/
def fourierEnergy (a : ℝ) (f : TestSpace a) (xi : ℝ) : ℝ :=
  ‖(IntervalZeroExtension.fourierZeroExtensionL2 a f : ℝ → ℂ) xi‖ ^ 2

/-- Intrinsic form domain for the compact-support Weil quadratic form. -/
def InLogarithmicDomain (a : ℝ) (f : TestSpace a) : Prop :=
  MeasureTheory.Integrable
    (fun xi ↦ Real.log (1 + (2 * Real.pi * xi) ^ 2) *
      fourierEnergy a f xi)
    (MeasureTheory.volume : MeasureTheory.Measure ℝ)

/-- The actual form domain of the zeta Weil quadratic form.  It is a dense
subspace of compactly supported `L²`, but the form is not an everywhere
bounded quadratic form for the plain `L²` norm because its Fourier multiplier
has logarithmic growth. -/
def LogarithmicFormDomain (a : ℝ) :=
  {f : TestSpace a // InLogarithmicDomain a f}

instance (a : ℝ) : Coe (LogarithmicFormDomain a) (TestSpace a) :=
  ⟨Subtype.val⟩

@[simp] theorem logarithmicFormDomain_mem (a : ℝ)
    (f : LogarithmicFormDomain a) : InLogarithmicDomain a f.val :=
  f.property

/-- The finite set of prime powers whose shifts can meet `[-a,a]`. -/
def activePrimePowers (a : ℝ) : Finset ℕ :=
  ((Finset.Ioc 0 ⌊Real.exp (2 * a)⌋₊).filter
    fun n ↦ IsPrimePow n ∧ Real.log n < 2 * a)

/-- Increasing the support can only activate additional prime powers. -/
theorem activePrimePowers_mono {a b : ℝ} (hab : a ≤ b) :
    activePrimePowers a ⊆ activePrimePowers b := by
  intro n hn
  simp only [activePrimePowers, Finset.mem_filter, Finset.mem_Ioc] at hn ⊢
  obtain ⟨⟨hnpos, hnfloor⟩, hnpp, hnlog⟩ := hn
  have hexp : Real.exp (2 * a) ≤ Real.exp (2 * b) := by
    exact Real.exp_le_exp.mpr (by linarith)
  exact ⟨⟨hnpos, hnfloor.trans (Nat.floor_mono hexp)⟩, hnpp,
    hnlog.trans_le (by linarith)⟩

/-- Exact bookkeeping identity for the new prime powers appearing between two
support scales.  No sign is assigned to the new contribution. -/
theorem sum_activePrimePowers_eq_add_increment {M : Type*}
    [AddCommMonoid M] {a b : ℝ} (hab : a ≤ b) (term : ℕ → M) :
    (∑ n ∈ activePrimePowers b, term n) =
      (∑ n ∈ activePrimePowers a, term n) +
        ∑ n ∈ activePrimePowers b \ activePrimePowers a, term n := by
  rw [add_comm]
  exact (Finset.sum_sdiff (activePrimePowers_mono hab)).symm

/-- Rank-two pole contribution. -/
def poleTerm (a : ℝ) (f : TestSpace a) : ℝ :=
  inner ℝ f (PoleProjection.polePlusL2 a) *
      inner ℝ f (PoleProjection.poleMinusL2 a) +
    inner ℝ f (PoleProjection.poleMinusL2 a) *
      inner ℝ f (PoleProjection.polePlusL2 a)

/-- Archimedean contribution in Mathlib's ordinary Fourier frequency. -/
def archimedeanTerm (a : ℝ) (f : TestSpace a) : ℝ :=
  ∫ xi, (GlideKernel.quarterDigammaReal (2 * Real.pi * xi) -
      Real.log Real.pi) * fourierEnergy a f xi

/-- One prime-power summand, in the time-domain normalization of `THEOREMS.md`. -/
def primePowerTerm (a : ℝ) (f : TestSpace a) (n : ℕ) : ℝ :=
  2 * Λ n / Real.sqrt n *
    AutocorrelationPlancherel.intervalAutocorrelation a (Real.log n) f

/-- The finite prime-power contribution for support in `[-a,a]`. -/
def primeTerm (a : ℝ) (f : TestSpace a) : ℝ :=
  ∑ n ∈ activePrimePowers a, primePowerTerm a f n

/-- At a larger support, the prime contribution splits into the terms already
active at the smaller support and the newly activated finite shell.  The
vector remains in the larger interval space; identifying the first sum with
the smaller-support form requires the nested-support isometry. -/
theorem primeTerm_eq_old_add_new {a b : ℝ} (hab : a ≤ b)
    (f : TestSpace b) :
    primeTerm b f =
      (∑ n ∈ activePrimePowers a, primePowerTerm b f n) +
        ∑ n ∈ activePrimePowers b \ activePrimePowers a,
          primePowerTerm b f n := by
  exact sum_activePrimePowers_eq_add_increment hab (primePowerTerm b f)

/-- The arithmetic side of the compact-support zeta Weil quadratic form. -/
def weilForm (a : ℝ) (f : TestSpace a) : ℝ :=
  poleTerm a f + archimedeanTerm a f - primeTerm a f

/-- The Weil form restricted to its mathematically correct logarithmic form
domain. -/
def logarithmicWeilForm (a : ℝ) (f : LogarithmicFormDomain a) : ℝ :=
  weilForm a f.val

theorem activePrimePowers_seven_sixteenths :
    activePrimePowers (7 / 16) = {2} := by
  have hlog2 : Real.log 2 < (7 / 8 : ℝ) :=
    Real.log_two_lt_d9.trans (by norm_num)
  have hlog3 : (7 / 8 : ℝ) < Real.log 3 :=
    (by norm_num : (7 / 8 : ℝ) < 1.0986122885).trans Real.log_three_gt_d9
  have hexpLower : (2 : ℝ) < Real.exp (7 / 8 : ℝ) := by
    rw [← Real.exp_log (by norm_num : (0 : ℝ) < 2)]
    exact Real.exp_lt_exp.mpr hlog2
  have hexpUpper : Real.exp (7 / 8 : ℝ) < 3 := by
    exact (Real.exp_lt_exp.mpr (by norm_num : (7 / 8 : ℝ) < 1)).trans
      Real.exp_one_lt_three
  have hfloor : ⌊Real.exp (7 / 8 : ℝ)⌋₊ = 2 := by
    exact (Nat.floor_eq_iff (Real.exp_pos _).le).mpr
      ⟨hexpLower.le, by norm_num at hexpUpper ⊢; exact hexpUpper⟩
  ext n
  simp only [activePrimePowers, show 2 * (7 / 16 : ℝ) = 7 / 8 by norm_num,
    hfloor, Finset.mem_filter, Finset.mem_Ioc, Finset.mem_singleton]
  constructor
  · rintro ⟨⟨_, hn2⟩, hpp, _⟩
    exact Nat.le_antisymm hn2 hpp.two_le
  · rintro rfl
    exact ⟨⟨by norm_num, by norm_num⟩, Nat.prime_two.isPrimePow, hlog2⟩

theorem primePowerTerm_two_eq_p2TimePrimeTwoTerm
    (f : ZetaWeilForm.P2Space) :
    primePowerTerm (7 / 16) f 2 = ZetaWeilForm.p2TimePrimeTwoTerm f := by
  unfold primePowerTerm ZetaWeilForm.p2TimePrimeTwoTerm
  rw [ArithmeticFunction.vonMangoldt_apply_prime Nat.prime_two]
  have hsqrt : Real.sqrt (2 : ℝ) * Real.sqrt 2 = 2 := by norm_num
  have hsqrtPos : 0 < Real.sqrt (2 : ℝ) := Real.sqrt_pos.2 (by norm_num)
  have hcoeff : 2 * Real.log (2 : ℝ) / Real.sqrt 2 =
      GlideKernel.p2PrimeAmplitude := by
    apply (div_eq_iff hsqrtPos.ne').2
    unfold GlideKernel.p2PrimeAmplitude
    calc
      2 * Real.log 2 = Real.log 2 * (Real.sqrt 2 * Real.sqrt 2) := by
        rw [hsqrt]
        ring
      _ = Real.sqrt 2 * (Real.log 2 * Real.sqrt 2) :=
        mul_left_comm _ _ _
      _ = (Real.sqrt 2 * Real.log 2) * Real.sqrt 2 :=
        (mul_assoc _ _ _).symm
  norm_num only [Nat.cast_ofNat]
  rw [hcoeff]

theorem primeTerm_seven_sixteenths (f : ZetaWeilForm.P2Space) :
    primeTerm (7 / 16) f = ZetaWeilForm.p2TimePrimeTwoTerm f := by
  rw [primeTerm, activePrimePowers_seven_sixteenths]
  simp only [Finset.sum_singleton]
  exact primePowerTerm_two_eq_p2TimePrimeTwoTerm f

/-- The previously certified fixed-window form is exactly the specialization
of the general compact-support zeta Weil form at `a = 7/16` (`L = 7/4`). -/
theorem weilForm_seven_sixteenths (f : ZetaWeilForm.P2Space) :
    weilForm (7 / 16) f = ZetaWeilForm.p2TimeDomainWeilForm f := by
  unfold weilForm poleTerm archimedeanTerm ZetaWeilForm.p2TimeDomainWeilForm
    ZetaWeilForm.p2PoleTerm ZetaWeilForm.p2ArchimedeanTerm
  rw [primeTerm_seven_sixteenths]
  rfl

theorem inLogarithmicDomain_seven_sixteenths
    (f : ZetaWeilForm.P2Space) :
    InLogarithmicDomain (7 / 16) f ↔
      ZetaWeilForm.InLogarithmicDomain f := by
  rfl

/-- The fixed-window kernel certificate, transported through the exact
specialization of the general compact-support zeta Weil form. -/
theorem weilForm_seven_sixteenths_strict_lower_bound
    (f : ZetaWeilForm.P2Space) (hf : f ≠ 0)
    (hlog : InLogarithmicDomain (7 / 16) f) :
    (22699 / 10 ^ 9 : ℝ) * ‖f‖ ^ 2 < weilForm (7 / 16) f := by
  rw [weilForm_seven_sixteenths]
  exact ZetaWeilForm.p2TimeDomainWeilForm_strict_lower_bound_on_logarithmicDomain
    f hf (inLogarithmicDomain_seven_sixteenths f |>.mp hlog)

end

end RHP2Bridge.GeneralZetaWeilForm
