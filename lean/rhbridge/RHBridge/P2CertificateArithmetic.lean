/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PoleScaleCenters
import RHBridge.P2CanonicalRational
import RHBridge.P2EntryTable

/-!
# Exact rational arithmetic target for canonical `p = 2` containment

Every analytic estimate has been discharged before this file.  The sole
remaining proposition is a finite comparison in `ℚ`: the exact rational
32-panel center (including the finite pole center) must be within `10⁻¹³`
of the stored matrix center.  A generated executable backend can prove that
proposition without introducing any numerical axiom.
-/

namespace RHP2Bridge

open scoped BigOperators

noncomputable def p2EntryPanelSumQ (e : P2EntryIndex) : ℚ :=
  ∑ k ∈ Finset.range 32,
    RatPoly.exactIntegral
      (RatPoly.p2ScaleCenteredPanelIntegrandPolynomialQ
        (p2EntrySelectedKind e.block) e.row e.col
        (p2PanelCenterQ k) 32)
      (-p2PanelHalfWidthQ k) (p2PanelHalfWidthQ k)

theorem p2EntryPanelSum_eq_cast (e : P2EntryIndex) :
    p2EntryPanelSum e = (p2EntryPanelSumQ e : ℝ) := by
  unfold p2EntryPanelSum p2EntryPanelSumQ
  push_cast
  apply Finset.sum_congr rfl
  intro k hk
  simpa [p2PanelCenter, p2PanelHalfWidth] using
    RatPoly.p2ScaleCenteredPanel_exactIntegral_eq_cast
      (p2EntrySelectedKind e.block) e.row e.col
      (p2PanelCenterQ k) (p2PanelHalfWidthQ k) 32

noncomputable def p2PoleTaylorCoeffScaleCenterQ (n : Fin 48) : ℚ :=
  p2ScaleCenterQ n.val / 2 * RatPoly.p2PoleTaylorRationalCoreQ n.val

noncomputable def p2EntryTaylorPoleCenterQ (e : P2EntryIndex) : ℚ :=
  2 * p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.col) *
    p2PoleTaylorCoeffScaleCenterQ
      (p2EntryPoleMode e.block e.row)

theorem p2PoleTaylorCoeffScaleCenter_eq_cast (n : Fin 48) :
    p2PoleTaylorCoeffScaleCenter n =
      (p2PoleTaylorCoeffScaleCenterQ n : ℝ) := by
  unfold p2PoleTaylorCoeffScaleCenter p2PoleTaylorCoeffScaleCenterQ
  rw [RatPoly.p2PoleTaylorRationalCore_eq_cast]
  push_cast
  rfl

theorem p2EntryTaylorPoleCenter_eq_cast (e : P2EntryIndex) :
    p2EntryTaylorPoleCenter e = (p2EntryTaylorPoleCenterQ e : ℝ) := by
  unfold p2EntryTaylorPoleCenter p2EntryTaylorPoleCenterQ
  rw [p2PoleTaylorCoeffScaleCenter_eq_cast,
    p2PoleTaylorCoeffScaleCenter_eq_cast]
  push_cast
  rfl

def p2AlphaCenterQ : ℚ := 10938711277167 / 10 ^ 13

def p2InvTwoPiCenterQ : ℚ := 15915494309189533576 / 10 ^ 20

def p2EntryDiagonalIndicatorQ (e : P2EntryIndex) : ℚ :=
  if e.row = e.col then 1 else 0

def p2EntryPoleSignQ (block : P2EntryBlock) : ℚ :=
  match block with
  | .even => 1
  | .odd => -1

def p2StoredCenterQ (e : P2EntryIndex) : ℚ :=
  (p2StoredCenterNumerator e : ℚ) / 10 ^ 18 +
    if e.row = e.col then 227 / 10 ^ 7 else 0

noncomputable def p2EntryApproxCenterQ (e : P2EntryIndex) : ℚ :=
  p2AlphaCenterQ * p2EntryDiagonalIndicatorQ e +
    p2InvTwoPiCenterQ * (2 * p2EntryPanelSumQ e) +
    p2EntryPoleSignQ e.block * p2EntryTaylorPoleCenterQ e

@[simp] theorem p2AlphaCenterQ_cast :
    (p2AlphaCenterQ : ℝ) = p2AlphaCenter := by
  norm_num [p2AlphaCenterQ, p2AlphaCenter]

@[simp] theorem p2InvTwoPiCenterQ_cast :
    (p2InvTwoPiCenterQ : ℝ) = p2InvTwoPiCenter := by
  norm_num [p2InvTwoPiCenterQ, p2InvTwoPiCenter]

@[simp] theorem p2EntryDiagonalIndicatorQ_cast (e : P2EntryIndex) :
    (p2EntryDiagonalIndicatorQ e : ℝ) =
      p2EntryDiagonalIndicator e := by
  unfold p2EntryDiagonalIndicatorQ p2EntryDiagonalIndicator
  split <;> simp

@[simp] theorem p2EntryPoleSignQ_cast (block : P2EntryBlock) :
    (p2EntryPoleSignQ block : ℝ) = p2EntryPoleSign block := by
  cases block <;> simp [p2EntryPoleSignQ, p2EntryPoleSign]

theorem p2StoredCenter_eq_cast (e : P2EntryIndex) :
    p2StoredCenter e = (p2StoredCenterQ e : ℝ) := by
  rw [p2StoredCenter_eq_integer_table]
  unfold p2StoredCenterQ
  push_cast
  split <;> simp_all <;> norm_num

theorem p2EntryApproxCenter_eq_cast (e : P2EntryIndex) :
    p2AlphaCenter * p2EntryDiagonalIndicator e +
        p2InvTwoPiCenter * (2 * p2EntryPanelSum e) +
        p2EntryPoleSign e.block * p2EntryTaylorPoleCenter e =
      (p2EntryApproxCenterQ e : ℝ) := by
  unfold p2EntryApproxCenterQ
  push_cast
  rw [p2EntryPanelSum_eq_cast, p2EntryTaylorPoleCenter_eq_cast]
  simp

/-- The demonstrably finite final arithmetic obligation. -/
def P2RationalCenterFits : Prop :=
  ∀ e : P2UpperEntryIndex,
    |p2EntryApproxCenterQ e.val - p2StoredCenterQ e.val| ≤ 1 / 10 ^ 13

/-- Row-major form consumed by a generated 600-row executable table. -/
def P2GeneratedRationalCenterFits : Prop :=
  ∀ k : Fin 600,
    |p2EntryApproxCenterQ (p2UpperEntryAt k).val -
      p2StoredCenterQ (p2UpperEntryAt k).val| ≤ 1 / 10 ^ 13

theorem p2RationalCenterFits_of_generated
    (h : P2GeneratedRationalCenterFits) : P2RationalCenterFits := by
  intro e
  have hk := h (p2UpperEntryEquiv.symm e)
  have hidx : p2UpperEntryAt (p2UpperEntryEquiv.symm e) = e :=
    p2UpperEntryEquiv.apply_symm_apply e
  rwa [hidx] at hk

theorem p2UpperEntryCenterCertificate_of_rationalCenterFits
    (h : P2RationalCenterFits) : P2UpperEntryCenterCertificate := by
  intro e
  apply abs_p2ScalarEntry_sub_storedCenter_le_of_rationalCenter
  rw [p2EntryApproxCenter_eq_cast, p2StoredCenter_eq_cast]
  rw [← Rat.cast_sub, ← Rat.cast_abs]
  have he :
      ((|p2EntryApproxCenterQ e.val - p2StoredCenterQ e.val| : ℚ) : ℝ) ≤
        (((1 / 10 ^ 13 : ℚ) : ℚ) : ℝ) := by
    exact_mod_cast h e
  convert he using 1 <;> norm_num

theorem p2_matrix_containment_of_rationalCenterFits
    (h : P2RationalCenterFits) :
    (∀ i j,
      FullInfClipped48Real.evenLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2EvenMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.evenUpperReal i j) ∧
    (∀ i j,
      FullInfClipped48Real.oddLowerReal i j ≤
          FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ∧
        FullInfP2CanonicalEndpoint.p2OddMatrix p2ClippedForm i j ≤
          FullInfClipped48Real.oddUpperReal i j) := by
  exact p2_matrix_containment_of_upper_entry_enclosures
    (p2UpperEntryEnclosures_of_centerCertificate
      (p2UpperEntryCenterCertificate_of_rationalCenterFits h))

end RHP2Bridge
