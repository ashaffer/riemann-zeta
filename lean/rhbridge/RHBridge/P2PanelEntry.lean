/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2PanelPartition
import RHBridge.P2EntryError

/-!
# Entry-indexed form of the canonical `p = 2` panel enclosure

This small adapter identifies the parity-tagged entry interface with the
selected real/imaginary component interface used by the 32-panel proof.
-/

namespace RHP2Bridge

open scoped BigOperators

def p2EntrySelectedKind : P2EntryBlock → P2SelectedKind
  | .even => .even
  | .odd => .odd

noncomputable def p2EntryPanelSum (e : P2EntryIndex) : ℝ :=
  ∑ k ∈ Finset.range 32,
    PolyEnclosure.exactIntegral
      (p2ScaleCenteredPanelIntegrandPolynomial
        (p2EntrySelectedKind e.block) e.row e.col
        (p2PanelCenter k) 32)
      (-p2PanelHalfWidth k) (p2PanelHalfWidth k)

theorem p2PositiveHalfBandIntegral_eq_selected (e : P2EntryIndex) :
    p2PositiveHalfBandIntegral e =
      ∫ r in (0 : ℝ)..50,
        p2SelectedBandIntegrand (p2EntrySelectedKind e.block)
          e.row.val e.col.val r := by
  rcases e with ⟨block, i, j⟩
  cases block <;>
    simp [p2PositiveHalfBandIntegral, p2EntrySelectedKind,
      p2SelectedBandIntegrand_even, p2SelectedBandIntegrand_odd]

theorem abs_p2PositiveHalfBandIntegral_sub_entryPanelSum_le
    (e : P2EntryIndex) :
    |p2PositiveHalfBandIntegral e - p2EntryPanelSum e| ≤
      p2PositiveHalfBandErrorBound := by
  rw [p2PositiveHalfBandIntegral_eq_selected]
  exact integral_p2SelectedBandIntegrand_sub_panelSum_le
    (p2EntrySelectedKind e.block) e.row e.col

theorem abs_p2EntryPanelSum_le (e : P2EntryIndex) :
    |p2EntryPanelSum e| ≤ 373 := by
  exact abs_p2SelectedBandPanelSum_le
    (p2EntrySelectedKind e.block) e.row e.col

/-- Close one entry once finite rational arithmetic has supplied a pole
center and checked the displayed approximation against the stored center.
All analytic errors have already been reduced to fixed rational constants. -/
theorem abs_p2ScalarEntry_sub_storedCenter_le_of_panelCertificate
    (e : P2EntryIndex) (qPole : ℝ)
    (hpole : |p2TaylorPoleContribution e - qPole| ≤ 1 / 10 ^ 17)
    (hround :
      |p2AlphaCenter * p2EntryDiagonalIndicator e +
          p2InvTwoPiCenter * (2 * p2EntryPanelSum e) +
          p2EntryPoleSign e.block * qPole - p2StoredCenter e| ≤
        1 / 10 ^ 13) :
    |p2ScalarEntry e - p2StoredCenter e| ≤ p2StoredRadius := by
  apply abs_p2ScalarEntry_sub_storedCenter_le_of_positiveHalf_taylorPole
    (e := e) (R := p2EntryPanelSum e)
    (eBand := p2PositiveHalfBandErrorBound) (B := 373)
    (qPole := qPole) (ePole := 1 / 10 ^ 17)
    (eRound := 1 / 10 ^ 13)
  · norm_num [p2PositiveHalfBandErrorBound]
  · norm_num
  · exact abs_p2PositiveHalfBandIntegral_sub_entryPanelSum_le e
  · exact abs_p2EntryPanelSum_le e
  · exact hpole
  · exact hround
  · rw [p2StoredRadius_eq]
    norm_num [p2PositiveHalfBandErrorBound]

end RHP2Bridge
