/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.WeilCriterionLiterature
import RHBridge.SupportDecomposition

/-!
# From local support propagation to RH

This module records a deliberately non-circular interface for the remaining
support-uniform argument.  It does not assume positivity at every support.
Instead it assumes an initial interval, a cofinal sequence of support scales,
and a local implication propagating positivity across each adjacent slab.
-/

namespace RHP2Bridge.UniformPropagationToRH

noncomputable section

open GeneralZetaWeilForm WeilCriterionLiterature SupportDecomposition

/-- Nonnegativity of the complete logarithmic Weil form at one support. -/
def PositiveAt (a : ℝ) : Prop :=
  ∀ f : LogarithmicFormDomain a, 0 ≤ logarithmicWeilForm a f

/-- A pointwise block criterion for one local support enlargement.  This is
the sharp relative-energy formulation suggested by the old/collar split; it
does not require a support-independent spectral gap. -/
theorem positiveAt_of_relative_block_bounds {a b : ℝ} (hab : a ≤ b)
    (hold : ∀ f : LogarithmicFormDomain b,
      0 ≤ weilForm b (oldPart a b hab f.val))
    (hcollar : ∀ f : LogarithmicFormDomain b,
      0 ≤ weilForm b (collarPart a b hab f.val))
    (hcross : ∀ f : LogarithmicFormDomain b,
      (weilCross b (oldPart a b hab f.val) (collarPart a b hab f.val)) ^ 2 ≤
        weilForm b (oldPart a b hab f.val) *
          weilForm b (collarPart a b hab f.val)) :
    PositiveAt b := by
  intro f
  exact weilForm_nonneg_of_relative_cross_bound a b hab f.val
    (hold f) (hcollar f) (hcross f)

/-- The exact package a successful support-uniform propagation argument must
provide.  `step` is local; cofinality and induction turn it into an all-support
statement. -/
structure PropagationPackage where
  base : ℝ
  scale : ℕ → ℝ
  base_nonneg : 0 ≤ base
  scale_zero : scale 0 = base
  scale_mono : Monotone scale
  cover : ∀ b, base ≤ b → ∃ n, scale n ≤ b ∧ b ≤ scale (n + 1)
  initial : ∀ a, 0 ≤ a → a ≤ base → PositiveAt a
  step : ∀ n, PositiveAt (scale n) →
    ∀ b, scale n ≤ b → b ≤ scale (n + 1) → PositiveAt b

theorem positiveAt_scale (P : PropagationPackage) :
    ∀ n, PositiveAt (P.scale n) := by
  intro n
  induction n with
  | zero =>
      rw [P.scale_zero]
      exact P.initial P.base P.base_nonneg le_rfl
  | succ n ih =>
      exact P.step n ih (P.scale (n + 1))
        (P.scale_mono (Nat.le_succ n)) le_rfl

theorem globalWeilPositivity_of_propagationPackage
    (P : PropagationPackage) : GlobalWeilPositivity := by
  intro a ha f
  by_cases hbase : a ≤ P.base
  · exact P.initial a ha hbase f
  · have hba : P.base ≤ a := le_of_lt (lt_of_not_ge hbase)
    obtain ⟨n, hleft, hright⟩ := P.cover a hba
    exact P.step n (positiveAt_scale P n) a hleft hright f

/-- Once a genuine local propagation package has been proved, the accepted
classical Weil criterion closes the argument to RH with no further analytic
remainder. -/
theorem riemannHypothesis_of_propagationPackage
    (P : PropagationPackage) : RiemannHypothesis :=
  globalWeilPositivity_implies_riemannHypothesis
    (globalWeilPositivity_of_propagationPackage P)

end

end RHP2Bridge.UniformPropagationToRH
