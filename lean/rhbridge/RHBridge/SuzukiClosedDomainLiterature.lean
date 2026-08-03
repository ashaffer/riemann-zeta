/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.CompressedKernelSynthesis

/-!
# Closed-domain Suzuki zero-mode dictionary

This module isolates the finite-interval operator-domain theorem used in
Stage 1.  The completed target space depends on a shift below the bottom of
the localized Weil spectrum.  At a nonnegative zero crossing every negative
shift is admissible.

The two analytic assertions below are imported from the closed-form/Friedrichs
extension and completed derivative construction in Suzuki's finite-interval
framework.  They are deliberately not presented as smooth-core facts.
-/

namespace RHP2Bridge.SuzukiClosedDomainLiterature

open GeneralZetaWeilForm

noncomputable section

/-- The shifted completion carrying the continuous-kernel realization.  It
is opaque here because the repository has not constructed this completion. -/
axiom CompletedSuzukiSpace (a shift : ℝ) : Type

axiom completedSuzukiAddCommGroup (a shift : ℝ) :
  AddCommGroup (CompletedSuzukiSpace a shift)

attribute [instance] completedSuzukiAddCommGroup

axiom completedSuzukiModule (a shift : ℝ) :
  Module ℝ (CompletedSuzukiSpace a shift)

attribute [instance] completedSuzukiModule

/-- The continuous screw-kernel operator extended to the shifted completion. -/
axiom completedSuzukiOperator (a shift : ℝ) :
  CompletedSuzukiSpace a shift →ₗ[ℝ] CompletedSuzukiSpace a shift

/-- The closed extension of the Dirichlet derivative coordinate map. -/
axiom closedDerivative (a shift : ℝ) :
  LogarithmicFormDomain a → CompletedSuzukiSpace a shift

/-- **Literature input: injectivity of the completed derivative coordinate.** -/
axiom closedDerivative_ne_zero
    {a shift : ℝ} {f : LogarithmicFormDomain a}
    (hf : f.val ≠ 0) :
    closedDerivative a shift f ≠ 0

/-- **Literature input: zero-eigenvalue intertwining on the closed domain.**
If the localized Weil form is nonnegative and `f` has zero energy, a negative
shift is below its spectral bottom and the completed derivative lies in the
kernel of the extended continuous-kernel operator. -/
axiom completedSuzukiOperator_closedDerivative_eq_zero
    {a shift : ℝ} {f : LogarithmicFormDomain a}
    (hshift : shift < 0)
    (hnonneg : ∀ g : LogarithmicFormDomain a,
      0 ≤ logarithmicWeilForm a g)
    (hzero : logarithmicWeilForm a f = 0) :
    completedSuzukiOperator a shift (closedDerivative a shift f) = 0

/-- Data of a genuine zero-energy vector at a nonnegative window. -/
structure FirstCrossingZeroMode (a : ℝ) where
  vector : LogarithmicFormDomain a
  nonzero : vector.val ≠ 0
  window_nonnegative : ∀ g : LogarithmicFormDomain a,
    0 ≤ logarithmicWeilForm a g
  zero_energy : logarithmicWeilForm a vector = 0

/-- The correctly completed Suzuki-kernel witness. -/
structure CompletedSuzukiZeroMode (a shift : ℝ) where
  vector : CompletedSuzukiSpace a shift
  nonzero : vector ≠ 0
  kernel : completedSuzukiOperator a shift vector = 0

/-- **Literature input: existence of a first zero crossing if RH fails.**
This packages Weil's criterion, positivity for sufficiently small support,
continuity of the lowest localized eigenvalue, attainment at zero, and the
closed-form representation theorem. -/
axiom exists_firstCrossingZeroMode_of_not_rh
    (hnot : ¬ RiemannHypothesis) :
    ∃ a : ℝ, 0 < a ∧ Nonempty (FirstCrossingZeroMode a)

/-- Stage 1 composition: an actual first-crossing form-domain mode transfers
to a nonzero kernel vector in Suzuki's shifted completed space. -/
noncomputable def firstCrossing_to_completedSuzukiZeroMode
    {a shift : ℝ} (hshift : shift < 0)
    (mode : FirstCrossingZeroMode a) :
    CompletedSuzukiZeroMode a shift where
  vector := closedDerivative a shift mode.vector
  nonzero := closedDerivative_ne_zero mode.nonzero
  kernel := completedSuzukiOperator_closedDerivative_eq_zero hshift
    mode.window_nonnegative mode.zero_energy

/-- In particular the completed Suzuki operator cannot have trivial kernel at
a first crossing. -/
theorem not_injective_completedSuzukiOperator
    {a shift : ℝ} (hshift : shift < 0)
    (mode : FirstCrossingZeroMode a) :
    ¬ Function.Injective (completedSuzukiOperator a shift) := by
  intro hinjective
  let witness := firstCrossing_to_completedSuzukiZeroMode hshift mode
  apply witness.nonzero
  apply hinjective
  simpa [witness.kernel]

/-- Failure of RH forces noninjectivity of every negatively shifted completed
Suzuki realization at some positive finite support. -/
theorem not_rh_implies_completedSuzuki_noninjective
    (hnot : ¬ RiemannHypothesis) :
    ∃ a : ℝ, 0 < a ∧ ∀ shift : ℝ, shift < 0 →
      ¬ Function.Injective (completedSuzukiOperator a shift) := by
  obtain ⟨a, ha, ⟨mode⟩⟩ := exists_firstCrossingZeroMode_of_not_rh hnot
  exact ⟨a, ha, fun shift hshift ↦
    not_injective_completedSuzukiOperator hshift mode⟩

/-- Stage-1 reduction to RH: uniform injectivity of the correctly completed
finite-window Suzuki operators rules out the first crossing. -/
theorem riemannHypothesis_of_completedSuzuki_injective
    (hinjective : ∀ a : ℝ, 0 < a → ∀ shift : ℝ, shift < 0 →
      Function.Injective (completedSuzukiOperator a shift)) :
    RiemannHypothesis := by
  by_contra hnot
  obtain ⟨a, ha, hnoninjective⟩ :=
    not_rh_implies_completedSuzuki_noninjective hnot
  exact hnoninjective (-1) (by norm_num) (hinjective a ha (-1) (by norm_num))

end

end RHP2Bridge.SuzukiClosedDomainLiterature
