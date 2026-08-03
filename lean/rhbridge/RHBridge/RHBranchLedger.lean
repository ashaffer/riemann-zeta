/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.WeilCriterionLiterature

/-!
# Explicit RH / not-RH assumption ledger

These theorems deliberately label the two contradiction branches.  They are
qualitative consequences of the accepted classical Weil criterion; neither
branch is an unconditional proof of its hypothesis.
-/

namespace RHP2Bridge.RHBranchLedger

noncomputable section

open GeneralZetaWeilForm WeilCriterionLiterature

/-- **RH branch.** Assuming RH, every finite-support logarithmic Weil form is
nonnegative.  A zero-frame factorization sought under this hypothesis must
eventually reproduce this conclusion without retaining the hypothesis. -/
theorem rh_implies_every_window_nonnegative
    (hRH : RiemannHypothesis) :
    ∀ (a : ℝ), 0 ≤ a → ∀ f : LogarithmicFormDomain a,
      0 ≤ logarithmicWeilForm a f :=
  riemannHypothesis_implies_globalWeilPositivity hRH

/-- **Not-RH branch.** Assuming RH is false, Weil's converse supplies a
negative witness at some finite support.  The quantitative converse-Weil
program asks for explicit bounds on this `a` from an off-line zero's height
and horizontal displacement. -/
theorem not_rh_implies_exists_negative_window
    (hnot : ¬ RiemannHypothesis) :
    ∃ (a : ℝ), 0 ≤ a ∧ ∃ f : LogarithmicFormDomain a,
      logarithmicWeilForm a f < 0 := by
  have hnotGlobal : ¬ GlobalWeilPositivity := by
    intro hglobal
    exact hnot (globalWeilPositivity_implies_riemannHypothesis hglobal)
  simp only [GlobalWeilPositivity] at hnotGlobal
  push Not at hnotGlobal
  exact hnotGlobal

/-- The qualitative dichotomy.  Its right branch is existential; obtaining a
computable support bound is additional analytic content, not propositional
logic. -/
theorem rh_or_negative_window :
    RiemannHypothesis ∨
      ∃ (a : ℝ), 0 ≤ a ∧ ∃ f : LogarithmicFormDomain a,
        logarithmicWeilForm a f < 0 := by
  by_cases hRH : RiemannHypothesis
  · exact Or.inl hRH
  · exact Or.inr (not_rh_implies_exists_negative_window hRH)

end

end RHP2Bridge.RHBranchLedger
