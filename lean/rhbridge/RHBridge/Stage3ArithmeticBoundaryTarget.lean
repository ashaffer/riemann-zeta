/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.Stage3SupportSaturation

/-!
# The irreducible Stage-3 arithmetic boundary target

The finite-dimensional no-go model shows that Hilbert-space collar size alone
cannot exclude a radical.  This file records the strictly stronger statement
that would do so: a support-saturating first-crossing vector must be detected
by at least one arithmetic/archimedean boundary variation.
-/

namespace RHP2Bridge.Stage3ArithmeticBoundaryTarget

open GeneralZetaWeilForm SuzukiClosedDomainLiterature
open Stage2DefectCharacterization Stage3SupportSaturation

/-- A genuinely zeta-specific boundary separation principle.  Unlike a norm
lower bound, it asserts that some admissible variation detects a mismatch
between the prime and pole--archimedean cross kernels. -/
def ArithmeticBoundarySeparation : Prop :=
  ∀ (a : ℝ), 0 < a → ∀ crossing : FirstCrossingWithHistory a,
    (∀ (b : ℝ) (_hb : 0 ≤ b) (hba : b < a),
      SupportDecomposition.collarPart b a hba.le crossing.vector.val ≠ 0) →
    ∃ g : LogarithmicFormDomain a,
      WeilCrossKernel.poleCross a crossing.vector.val g.val +
          WeilCrossKernel.archimedeanCross a crossing.vector.val g.val ≠
        WeilCrossKernel.primeCross a crossing.vector.val g.val

/-- The proposed separation condition is not yet a simplification: using the
already-proved radical identity and support saturation, it is exactly the
nonexistence of a positive-support first crossing. -/
theorem arithmeticBoundarySeparation_iff_noFirstCrossing :
    ArithmeticBoundarySeparation ↔
      ∀ (a : ℝ), 0 < a → IsEmpty (FirstCrossingWithHistory a) := by
  constructor
  · intro hsep a ha
    refine ⟨?_⟩
    intro crossing
    obtain ⟨g, hg⟩ := hsep a ha crossing (fun b hb hba ↦
      collarPart_ne_zero crossing hb hba)
    exact hg (firstCrossing_arithmetic_balance
      crossing.toFirstCrossingZeroMode g)
  · intro hno a ha crossing _
    exact False.elim ((hno a ha).false crossing)

/-- The arithmetic boundary separation principle rules out the first crossing
and therefore implies RH. -/
theorem riemannHypothesis_of_arithmeticBoundarySeparation
    (hsep : ArithmeticBoundarySeparation) : RiemannHypothesis := by
  by_contra hnot
  obtain ⟨a, ha, ⟨crossing⟩⟩ :=
    exists_firstCrossingWithHistory_of_not_rh hnot
  obtain ⟨g, hg⟩ := hsep a ha crossing (fun b hb hba ↦
    collarPart_ne_zero crossing hb hba)
  exact hg (firstCrossing_arithmetic_balance crossing.toFirstCrossingZeroMode g)

/-- Parsimonious form of the same reduction, exposing that all remaining
content is the exclusion of the first-crossing object itself. -/
theorem riemannHypothesis_of_no_firstCrossingWithHistory
    (hno : ∀ (a : ℝ), 0 < a → IsEmpty (FirstCrossingWithHistory a)) :
    RiemannHypothesis := by
  exact riemannHypothesis_of_arithmeticBoundarySeparation
    (arithmeticBoundarySeparation_iff_noFirstCrossing.mpr hno)

end RHP2Bridge.Stage3ArithmeticBoundaryTarget
