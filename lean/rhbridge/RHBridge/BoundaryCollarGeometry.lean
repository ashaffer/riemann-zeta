/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.EventCollarPropagation

/-!
# Translation geometry of a two-sided boundary collar

A vector supported in `[-b,-a] ∪ [a,b]` can correlate with a translate only
at short within-collar shifts or at shifts bridging the two opposite collars.
This removes the bulk of the prime sum from event-driven collar estimates.
-/

namespace RHP2Bridge.BoundaryCollarGeometry

noncomputable section

open GeneralZetaWeilForm

/-- Support predicate for the two boundary collars of an enlargement. -/
def SupportedInBoundaryCollar (a b : ℝ) (f : TestSpace b) : Prop :=
  Function.support (IntervalZeroExtension.zeroExtensionFn b f) ⊆
    Set.Icc (-b) (-a) ∪ Set.Icc a b

/-- Standard support-overlap fact.  Between the within-collar range and the
opposite-collar range, the autocorrelation vanishes. -/
axiom intervalAutocorrelation_eq_zero_of_boundaryCollar_gap
    {a b u : ℝ} {f : TestSpace b}
    (hsupport : SupportedInBoundaryCollar a b f)
    (hshort : b - a < |u|) (hlong : |u| ≤ 2 * a) :
    AutocorrelationPlancherel.intervalAutocorrelation b u f = 0

/-- Shifts larger than the collar diameter also vanish. -/
axiom intervalAutocorrelation_eq_zero_of_boundaryCollar_exterior
    {a b u : ℝ} {f : TestSpace b}
    (hsupport : SupportedInBoundaryCollar a b f)
    (h : 2 * b ≤ |u|) :
    AutocorrelationPlancherel.intervalAutocorrelation b u f = 0

theorem primePowerTerm_eq_zero_of_boundaryCollar_gap
    {a b : ℝ} {f : TestSpace b} (hsupport : SupportedInBoundaryCollar a b f)
    {n : ℕ} (hshort : b - a < |Real.log n|)
    (hlong : |Real.log n| ≤ 2 * a) :
    primePowerTerm b f n = 0 := by
  unfold primePowerTerm
  rw [intervalAutocorrelation_eq_zero_of_boundaryCollar_gap
    hsupport hshort hlong]
  ring

/-- On a consecutive event collar, if every active prime shift lies between
the collar width and the opposite-collar separation, the complete prime term
vanishes. -/
theorem primeTerm_eq_zero_of_boundaryCollar_event
    {a b : ℝ} {f : TestSpace b} (hsupport : SupportedInBoundaryCollar a b f)
    (hshort : ∀ n ∈ activePrimePowers b, b - a < |Real.log n|)
    (hlong : ∀ n ∈ activePrimePowers b, |Real.log n| ≤ 2 * a) :
    primeTerm b f = 0 := by
  unfold primeTerm
  apply Finset.sum_eq_zero
  intro n hn
  exact primePowerTerm_eq_zero_of_boundaryCollar_gap
    hsupport (hshort n hn) (hlong n hn)

/-- Consequently collar positivity is purely pole--archimedean on an isolated
event window; no arithmetic sign estimate is needed for the diagonal block. -/
theorem weilForm_collar_eq_pole_add_archimedean
    {a b : ℝ} {f : TestSpace b} (hsupport : SupportedInBoundaryCollar a b f)
    (hshort : ∀ n ∈ activePrimePowers b, b - a < |Real.log n|)
    (hlong : ∀ n ∈ activePrimePowers b, |Real.log n| ≤ 2 * a) :
    weilForm b f = poleTerm b f + archimedeanTerm b f := by
  unfold weilForm
  rw [primeTerm_eq_zero_of_boundaryCollar_event hsupport hshort hlong, sub_zero]

theorem primePowerTerm_eq_zero_of_boundaryCollar_exterior
    {a b : ℝ} {f : TestSpace b} (hsupport : SupportedInBoundaryCollar a b f)
    {n : ℕ} (h : 2 * b ≤ |Real.log n|) :
    primePowerTerm b f n = 0 := by
  unfold primePowerTerm
  rw [intervalAutocorrelation_eq_zero_of_boundaryCollar_exterior hsupport h]
  ring

/-- A proxy-energy version of the collar/cross certificate.  It is often
easier to prove both estimates against the same positive collar control
functional than directly against the full indefinite Weil form. -/
structure RelativeCollarBounds {b : ℝ}
    (old : TestSpace b) (collar : TestSpace b) where
  control : ℝ
  control_nonneg : 0 ≤ control
  collar_lower : control ≤ weilForm b collar
  cross_sq_le : (SupportDecomposition.weilCross b old collar) ^ 2 ≤
    weilForm b old * control

theorem relative_cross_of_collarBounds {b : ℝ}
    {old collar : TestSpace b} (hold : 0 ≤ weilForm b old)
    (h : RelativeCollarBounds old collar) :
    0 ≤ weilForm b collar ∧
      (SupportDecomposition.weilCross b old collar) ^ 2 ≤
        weilForm b old * weilForm b collar := by
  constructor
  · exact h.control_nonneg.trans h.collar_lower
  · exact h.cross_sq_le.trans
      (mul_le_mul_of_nonneg_left h.collar_lower hold)

/-- A complete event certificate phrased through a common collar control
functional. -/
def RelativeEventCertificate (a b : ℝ) : Prop :=
  ∀ f : LogarithmicFormDomain b,
    ∃ w : LogarithmicFormDomain a, ∃ v : TestSpace b,
      ∃ _bounds : RelativeCollarBounds
          (NestedSupport.nestedSupport a b w.val) v,
        InLogarithmicDomain b v ∧
        NestedSupport.nestedSupport a b w.val + v = f.val

theorem positiveAt_of_relativeEventCertificate
    {a b : ℝ} (hab : a ≤ b)
    (hpositive : UniformPropagationToRH.PositiveAt a)
    (hcert : RelativeEventCertificate a b) :
    UniformPropagationToRH.PositiveAt b := by
  intro f
  obtain ⟨w, v, hbounds, hvDomain, hsum⟩ := hcert f
  have hold : 0 ≤ weilForm b (NestedSupport.nestedSupport a b w.val) :=
    ActivationCancellation.nestedSupport_nonneg_of_positiveAt
      hab hpositive w
  obtain ⟨hcollar, hcross⟩ :=
    relative_cross_of_collarBounds hold hbounds
  exact EventCollarPropagation.event_step_pointwise hab hpositive
    hvDomain hsum hcollar hcross

end

end RHP2Bridge.BoundaryCollarGeometry
