/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.ActivationCancellation

/-!
# Event-driven propagation reduced to collar and cross control

New prime shifts have zero autocorrelation on the embedded old window, so its
Weil energy is preserved exactly.  An event step therefore needs only a
form-domain-safe old/collar decomposition, collar nonnegativity, and the sharp
relative cross bound.
-/

namespace RHP2Bridge.EventCollarPropagation

noncomputable section

open GeneralZetaWeilForm NestedSupport SupportDecomposition
  SmoothSupportPropagation UniformPropagationToRH ActivationCancellation

/-- The two genuinely remaining estimates for an event-driven enlargement.
The old vector is stored in the smaller logarithmic domain, while the collar
is explicitly required to remain in the larger one. -/
def EventCollarCertificate (a b : ℝ) : Prop :=
  ∀ f : LogarithmicFormDomain b,
    ∃ w : LogarithmicFormDomain a, ∃ v : TestSpace b,
      InLogarithmicDomain b v ∧
      nestedSupport a b w.val + v = f.val ∧
      0 ≤ weilForm b v ∧
      (weilCross b (nestedSupport a b w.val) v) ^ 2 ≤
        weilForm b (nestedSupport a b w.val) * weilForm b v

/-- Old positivity plus collar/cross control propagates positivity to the
larger event window.  There is no activation-reserve hypothesis. -/
theorem positiveAt_of_eventCollarCertificate
    {a b : ℝ} (hab : a ≤ b) (hpositive : PositiveAt a)
    (hcert : EventCollarCertificate a b) : PositiveAt b := by
  intro f
  obtain ⟨w, v, hvDomain, hsum, hv, hcross⟩ := hcert f
  have hu : 0 ≤ weilForm b (nestedSupport a b w.val) :=
    nestedSupport_nonneg_of_positiveAt hab hpositive w
  have hsplit : AdmissibleSplit f.val (nestedSupport a b w.val) v := by
    exact ⟨f.property,
      (inLogarithmicDomain_nestedSupport_iff hab w.val).2 w.property,
      hvDomain, hsum⟩
  exact weilForm_nonneg_of_admissible_relative_bounds
    hsplit hu hv hcross

/-- Pointwise version convenient for constructing a certificate from separate
collar and cross estimates. -/
theorem event_step_pointwise
    {a b : ℝ} (hab : a ≤ b) (hpositive : PositiveAt a)
    {f : LogarithmicFormDomain b} {w : LogarithmicFormDomain a}
    {v : TestSpace b} (hvDomain : InLogarithmicDomain b v)
    (hsum : nestedSupport a b w.val + v = f.val)
    (hcollar : 0 ≤ weilForm b v)
    (hcross : (weilCross b (nestedSupport a b w.val) v) ^ 2 ≤
      weilForm b (nestedSupport a b w.val) * weilForm b v) :
    0 ≤ logarithmicWeilForm b f := by
  have hu := nestedSupport_nonneg_of_positiveAt hab hpositive w
  apply weilForm_nonneg_of_admissible_relative_bounds
    (f := f.val) (u := nestedSupport a b w.val) (v := v)
  · exact ⟨f.property,
      (inLogarithmicDomain_nestedSupport_iff hab w.val).2 w.property,
      hvDomain, hsum⟩
  · exact hu
  · exact hcollar
  · exact hcross

end

end RHP2Bridge.EventCollarPropagation
