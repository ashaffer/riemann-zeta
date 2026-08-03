/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ActivationCancellation
import RHBridge.RelativeIncidenceComplex

/-!
# Exact transport of the completed incidence excess

After completing prime adjacencies to translation-defect squares, the positive
incidence energy differs from the Weil form by a scalar degree deficit (on the
two-moment relative subspace).  A vector supported in a smaller window gains
exactly the new scalar degree when the ambient support grows, because every
newly active translation has zero overlap.  Hence incidence energy minus its
degree threshold is exactly invariant under nested support.
-/

namespace RHP2Bridge.SharpIncidenceTransport

open scoped ArithmeticFunction
open GeneralZetaWeilForm

noncomputable section

/-- The scalar threshold left by completing all active prime adjacencies to
difference squares and normalizing the archimedean symbol at frequency zero. -/
def degreeDeficit (a : ℝ) : ℝ :=
  2 * ∑ n ∈ activePrimePowers a, Λ n / Real.sqrt n -
    (GlideKernel.quarterDigammaReal 0 - Real.log Real.pi)

/-- The renormalized incidence ledger.  On the relative moment subspace this
is the continuum-plus-prime defect energy. -/
def incidenceLedger (a : ℝ) (f : LogarithmicFormDomain a) : ℝ :=
  logarithmicWeilForm a f + degreeDeficit a * ‖f.val‖ ^ 2

/-- Its excess above the exact scalar threshold is just the Weil form. -/
theorem incidenceLedger_sub_degree (a : ℝ)
    (f : LogarithmicFormDomain a) :
    incidenceLedger a f - degreeDeficit a * ‖f.val‖ ^ 2 =
      logarithmicWeilForm a f := by
  unfold incidenceLedger
  ring

/-- The two relative moment constraints survive zero extension to every
larger support window. -/
theorem relativeMoments_nestedSupport {a b : ℝ} (hab : a ≤ b)
    {f : LogarithmicFormDomain a}
    (hf : RelativeIncidenceComplex.InRelativeMomentSubspace a f.val) :
    RelativeIncidenceComplex.InRelativeMomentSubspace b
      (NestedSupport.nestedLogarithmicSupport hab f).val := by
  unfold RelativeIncidenceComplex.InRelativeMomentSubspace at hf ⊢
  change
    inner ℝ (NestedSupport.nestedSupport a b f.val)
        (PoleProjection.polePlusL2 b) = 0 ∧
      inner ℝ (NestedSupport.nestedSupport a b f.val)
        (PoleProjection.poleMinusL2 b) = 0
  unfold PoleProjection.polePlusL2 PoleProjection.poleMinusL2
  rw [NestedSupport.inner_nestedSupport_poleL2 hab,
    NestedSupport.inner_nestedSupport_poleL2 hab]
  exact hf

/-- Exact sharpness identity: enlarging the ambient support adds the same
amount to incidence energy and to its degree threshold. -/
theorem incidenceExcess_nestedSupport {a b : ℝ} (hab : a ≤ b)
    (f : LogarithmicFormDomain a) :
    incidenceLedger b (NestedSupport.nestedLogarithmicSupport hab f) -
        degreeDeficit b *
          ‖(NestedSupport.nestedLogarithmicSupport hab f).val‖ ^ 2 =
      incidenceLedger a f - degreeDeficit a * ‖f.val‖ ^ 2 := by
  rw [incidenceLedger_sub_degree, incidenceLedger_sub_degree]
  change weilForm b (NestedSupport.nestedSupport a b f.val) =
    logarithmicWeilForm a f
  exact ActivationCancellation.weilForm_nestedSupport_eq hab f

end

end RHP2Bridge.SharpIncidenceTransport
