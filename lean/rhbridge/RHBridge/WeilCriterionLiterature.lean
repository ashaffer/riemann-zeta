/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.GuinandWeilLiterature

/-!
# Weil's positivity criterion for the Riemann hypothesis

This file states the final classical literature bridge separately from the
normalization-matched Guinand--Weil formula.  The target is nonnegativity at
each finite support, not a support-independent positive spectral gap.

The equivalence below is the classical Weil criterion.  Its use with the
specific low-regularity domain in this project also relies on the closure
input isolated in `GuinandWeilLiterature`.
-/

namespace RHP2Bridge.WeilCriterionLiterature

noncomputable section

open GeneralZetaWeilForm

/-- Positivity of the normalization-matched zeta Weil form at every finite
logarithmic support.  This is the exact all-support target needed for RH. -/
def GlobalWeilPositivity : Prop :=
  ∀ (a : ℝ), 0 ≤ a → ∀ f : LogarithmicFormDomain a,
    0 ≤ logarithmicWeilForm a f

/-- Equivalent arithmetic-side formulation: the prime-power term is dominated
by the pole and archimedean terms at every finite support. -/
def GlobalPrimeDomination : Prop :=
  ∀ (a : ℝ), 0 ≤ a → ∀ f : LogarithmicFormDomain a,
    primeTerm a f.val ≤ poleTerm a f.val + archimedeanTerm a f.val

theorem globalWeilPositivity_iff_globalPrimeDomination :
    GlobalWeilPositivity ↔ GlobalPrimeDomination := by
  simp only [GlobalWeilPositivity, GlobalPrimeDomination,
    logarithmicWeilForm, weilForm]
  constructor <;> intro h a ha f
  · linarith [h a ha f]
  · linarith [h a ha f]

/-- Classical Weil positivity criterion, expressed in the precise
normalization and logarithmic form domain used by this project. -/
axiom riemannHypothesis_iff_globalWeilPositivity :
  RiemannHypothesis ↔ GlobalWeilPositivity

theorem globalWeilPositivity_implies_riemannHypothesis
    (h : GlobalWeilPositivity) : RiemannHypothesis :=
  riemannHypothesis_iff_globalWeilPositivity.mpr h

theorem riemannHypothesis_implies_globalWeilPositivity
    (h : RiemannHypothesis) : GlobalWeilPositivity :=
  riemannHypothesis_iff_globalWeilPositivity.mp h

/-- The decisive remaining theorem can be attacked entirely on the arithmetic
side: support-by-support domination of the finite prime-power sum proves RH. -/
theorem riemannHypothesis_of_uniform_primeDomination
    (h : ∀ (a : ℝ), 0 ≤ a → ∀ f : LogarithmicFormDomain a,
      primeTerm a f.val ≤ poleTerm a f.val + archimedeanTerm a f.val) :
    RiemannHypothesis := by
  apply globalWeilPositivity_implies_riemannHypothesis
  exact globalWeilPositivity_iff_globalPrimeDomination.mpr h

/-- Conversely, the item-5 inequality is not merely sufficient: under the
classical Weil criterion it is equivalent to RH. -/
theorem uniform_primeDomination_of_riemannHypothesis
    (h : RiemannHypothesis) (a : ℝ) (ha : 0 ≤ a)
    (f : LogarithmicFormDomain a) :
    primeTerm a f.val ≤ poleTerm a f.val + archimedeanTerm a f.val := by
  exact (globalWeilPositivity_iff_globalPrimeDomination.mp
    (riemannHypothesis_implies_globalWeilPositivity h)) a ha f

/-- The fixed-window certificate is strict on every nonzero vector in the
full logarithmic form domain, rather than merely on a finite-dimensional
trial space. -/
theorem seven_sixteenths_strictlyPositive
    (f : LogarithmicFormDomain (7 / 16)) (hf : f.val ≠ 0) :
    0 < logarithmicWeilForm (7 / 16) f := by
  have hbound := weilForm_seven_sixteenths_strict_lower_bound
    f.val hf f.property
  have hnorm : 0 < ‖f.val‖ ^ 2 := sq_pos_of_pos (norm_pos_iff.mpr hf)
  have hcoeff : (0 : ℝ) < 22699 / 10 ^ 9 := by norm_num
  exact lt_trans (mul_pos hcoeff hnorm) hbound

end

end RHP2Bridge.WeilCriterionLiterature
