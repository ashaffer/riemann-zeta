/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.UniformPropagationToRH

/-!
# Form-domain-safe support propagation

The orthogonal projection onto a sharply truncated support interval is natural
in `L²`, but it need not preserve the logarithmic Weil form domain.  This file
therefore states the block argument for an arbitrary decomposition whose two
pieces are separately known to lie in that domain.

It also isolates the discrete loss caused by prime powers activated between
two support scales.  This loss is distinct from the continuous boundary-collar
problem and must be paid for by an explicit reserve in the old diagonal block.
-/

namespace RHP2Bridge.SmoothSupportPropagation

noncomputable section

open GeneralZetaWeilForm NestedSupport SupportDecomposition
  UniformPropagationToRH

/-- A decomposition of a form-domain vector into two form-domain pieces.
In applications these should be produced by a smooth partition of unity,
rather than a sharp support projection. -/
def AdmissibleSplit {a : ℝ} (f u v : TestSpace a) : Prop :=
  InLogarithmicDomain a f ∧ InLogarithmicDomain a u ∧
    InLogarithmicDomain a v ∧ u + v = f

/-- The exact prime-power loss on an old vector when support grows from `a`
to `b`. -/
def activationLoss {a b : ℝ} (f : LogarithmicFormDomain a) : ℝ :=
  ∑ n ∈ activePrimePowers b \ activePrimePowers a,
    primePowerTerm a f.val n

/-- Fixed-window positivity survives on an embedded old vector precisely when
the newly activated prime shell does not exhaust its existing energy reserve.
No sign of an individual autocorrelation is assumed. -/
theorem nestedSupport_nonneg_of_activationLoss_le
    {a b : ℝ} (hab : a ≤ b)
    (f : LogarithmicFormDomain a)
    (hloss : activationLoss (b := b) f ≤ logarithmicWeilForm a f) :
    0 ≤ weilForm b (nestedSupport a b f.val) := by
  rw [weilForm_nestedSupport hab]
  exact sub_nonneg.mpr hloss

/-- Between activation thresholds the reserve condition is automatic: the
old diagonal block is exactly the previous-support form. -/
theorem nestedSupport_nonneg_of_no_activation
    {a b : ℝ} (hab : a ≤ b) (hpositive : PositiveAt a)
    (hactive : activePrimePowers b = activePrimePowers a)
    (f : LogarithmicFormDomain a) :
    0 ≤ weilForm b (nestedSupport a b f.val) := by
  rw [weilForm_nestedSupport_of_active_eq hab hactive]
  exact hpositive f

/-- A form-domain-safe two-block positivity theorem.  Unlike the sharp
projection formulation, every invocation records that both pieces remain in
the logarithmic domain. -/
theorem weilForm_nonneg_of_admissible_relative_bounds
    {a : ℝ} {f u v : TestSpace a}
    (hsplit : AdmissibleSplit f u v)
    (hu : 0 ≤ weilForm a u) (hv : 0 ≤ weilForm a v)
    (hcross : (weilCross a u v) ^ 2 ≤ weilForm a u * weilForm a v) :
    0 ≤ weilForm a f := by
  obtain ⟨_, _, _, huv⟩ := hsplit
  rw [← huv, weilForm_add]
  exact add_two_mul_nonneg_of_cross_sq_le hu hv hcross

/-- The genuinely local obligations for one smooth enlargement from `a` to
`b`.  The old piece must come from the smaller form domain; the remainder
must remain in the larger form domain; the newly activated prime shell must
fit inside the old energy reserve; and the two enlarged-support blocks must
satisfy the sharp Schur bound. -/
def SmoothStepCertificate (a b : ℝ) : Prop :=
  ∀ f : LogarithmicFormDomain b,
    ∃ w : LogarithmicFormDomain a, ∃ v : TestSpace b,
      InLogarithmicDomain b v ∧ nestedSupport a b w.val + v = f.val ∧
      activationLoss (b := b) w ≤ logarithmicWeilForm a w ∧
      0 ≤ weilForm b v ∧
      (weilCross b (nestedSupport a b w.val) v) ^ 2 ≤
        weilForm b (nestedSupport a b w.val) * weilForm b v

/-- A smooth step certificate propagates positivity without ever applying a
sharp cutoff to a form-domain vector. -/
theorem positiveAt_of_smoothStepCertificate {a b : ℝ} (hab : a ≤ b)
    (h : SmoothStepCertificate a b) : PositiveAt b := by
  intro f
  obtain ⟨w, v, hvDomain, hsum, hloss, hv, hcross⟩ := h f
  have hu : 0 ≤ weilForm b (nestedSupport a b w.val) :=
    nestedSupport_nonneg_of_activationLoss_le hab w hloss
  have hsplit : AdmissibleSplit f.val (nestedSupport a b w.val) v := by
    exact ⟨f.property,
      (inLogarithmicDomain_nestedSupport_iff hab w.val).2 w.property,
      hvDomain, hsum⟩
  exact weilForm_nonneg_of_admissible_relative_bounds
    hsplit hu hv hcross

end

end RHP2Bridge.SmoothSupportPropagation
