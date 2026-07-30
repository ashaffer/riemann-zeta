/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedTripleMoment
import RHBridge.P2RoundedPanelRefinement

/-!
# Generated-data boundary for staged `p = 2` moment refinements

This module keeps generated dispatch abstract.  For each panel, generated
leaves may supply one 297-entry defect-moment vector and 48 149-entry
component matvecs.  Pointwise correctness of those values identifies the
resulting staged QBall with the direct triple-factor QBall, whose analytic
error bound was already proved in `P2RoundedSharedEvaluator`.
-/

namespace RHP2Bridge

namespace P2RoundedMomentRefinement

open P2RoundedPanelRefinement
open P2RoundedSharedEvaluator
open P2RoundedTripleMoment

/-- Pure generated data for one panel.  No correctness claim is bundled into
the values, so their finite checks can be split across arbitrary leaves. -/
structure PanelMomentData where
  moments : Vector ℚ 297
  matvecs : P2SelectedKind → Fin 24 → Vector ℚ 149

/-- Small semantic interface for one panel's supplied moments and matvecs.
The final field is pointwise so generated row checks need not construct one
large vector equality proof. -/
structure PanelMomentData.CorrectFor
    (data : PanelMomentData) (cache : PanelCache) : Prop where
  moments_correct :
    DefectMomentsCorrect cache.defect.coeffs data.moments
  component_length_le : ∀ (kind : P2SelectedKind) (i : Fin 24),
    (cache.component kind i).coeffs.length ≤ 149
  matvec_get_eq : ∀ (kind : P2SelectedKind) (i : Fin 24)
      (row : Fin 149),
    (data.matvecs kind i).get row =
      (hankelMatVecFromMoments data.moments
        (cache.component kind i).coeffs).get row

/-- Correct supplied moments and a pointwise matvec checkpoint imply the
direct mathematical Hankel-row specification. -/
theorem PanelMomentData.CorrectFor.matvec_correct
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache)
    (kind : P2SelectedKind) (i : Fin 24) :
    HankelMatVecCorrect cache.defect.coeffs
      (cache.component kind i).coeffs (data.matvecs kind i) := by
  intro row
  rw [hdata.matvec_get_eq kind i row]
  exact hankelMatVecFromMoments_correct
    hdata.moments_correct (cache.component kind i).coeffs
      (hdata.component_length_le kind i) row

/-- One supplied-matvec entry ball.  Its radius is literally the direct
three-factor analytic ledger; only its exact rational center is staged. -/
def stagedEntryBall
    (data : PanelMomentData) (cache : PanelCache) (k : Fin 32)
    (kind : P2SelectedKind) (i j : Fin 24)
    (hrows : (cache.component kind j).coeffs.length ≤ 149) : QBall :=
  ⟨p2PanelHalfWidthQ k.val *
      hankelDotFromVector (cache.component kind j).coeffs
        (data.matvecs kind i) hrows,
    2 * p2PanelHalfWidthQ k.val *
      tripleFactorError cache.defect
        (cache.component kind j) (cache.component kind i)⟩

/-- The staged entry ball is definitionally the same analytic enclosure once
the supplied moments and matvec are proved correct. -/
theorem stagedEntryBall_eq_tripleFactorEntryBall
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache)
    (k : Fin 32) (kind : P2SelectedKind) (i j : Fin 24) :
    stagedEntryBall data cache k kind i j
        (hdata.component_length_le kind j) =
      tripleFactorEntryBall k cache kind i j := by
  have hdot := hankelDotFromVector_eq_hankelBilinear
    cache.defect.coeffs (cache.component kind j).coeffs
    (cache.component kind i).coeffs (data.matvecs kind i)
    (hdata.component_length_le kind j)
    (hdata.matvec_correct kind i)
  simp [stagedEntryBall, tripleFactorEntryBall,
    tripleFactorIntegralBall,
    exactIntegral_triple_eq_hankelBilinear, hdot]

/-- Generated-entry wrapper around `stagedEntryBall`. -/
def stagedPanelBall
    (data : PanelMomentData) (cache : PanelCache) (k : Fin 32)
    (hdata : data.CorrectFor cache) (r : Fin 600) : QBall :=
  let e := generatedEntryAt r
  stagedEntryBall data cache k
    (p2EntrySelectedKind e.block) e.row e.col
    (hdata.component_length_le (p2EntrySelectedKind e.block) e.col)

/-- The generated-entry staged ball is the direct analytic panel ball used
by `P2RoundedPanelRefinement`. -/
theorem stagedPanelBall_eq_tripleFactorPanelBall
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache) (k : Fin 32) (r : Fin 600) :
    stagedPanelBall data cache k hdata r =
      tripleFactorPanelBall cache k r := by
  unfold stagedPanelBall tripleFactorPanelBall
  dsimp only
  exact stagedEntryBall_eq_tripleFactorEntryBall hdata k
    (p2EntrySelectedKind (generatedEntryAt r).block)
    (generatedEntryAt r).row (generatedEntryAt r).col

/-- Canonical analytic enclosure stated directly for the staged panel ball. -/
theorem abs_p2PanelIntegralQ_sub_stagedPanelBallCenter_le
    {data : PanelMomentData} {cache : PanelCache}
    (hdata : data.CorrectFor cache) {k : Fin 32}
    (hcache : cache.EnclosesCanonical k) (r : Fin 600) :
    let e := generatedEntryAt r
    |DenseRatPoly.p2PanelIntegralQ
          (p2EntrySelectedKind e.block) e.row e.col k.val -
        (stagedPanelBall data cache k hdata r).center| ≤
      (stagedPanelBall data cache k hdata r).radius := by
  dsimp only
  rw [stagedPanelBall_eq_tripleFactorPanelBall hdata]
  simpa [tripleFactorPanelBall, generatedEntryAt] using
    abs_p2PanelIntegralQ_sub_tripleFactorEntryBallCenter_le
      hcache
      (p2EntrySelectedKind (generatedEntryAt r).block)
      (generatedEntryAt r).row (generatedEntryAt r).col

/-- Finite target-refinement predicate for abstract generated dispatch. -/
def StagedPanelTargetRefinements
    (cache : Fin 32 → PanelCache)
    (data : Fin 32 → PanelMomentData)
    (hdata : ∀ k, (data k).CorrectFor (cache k)) : Prop :=
  ∀ (k : Fin 32) (r : Fin 600),
    (stagedPanelBall (data k) (cache k) k (hdata k) r).Refines
      (coarsePanelBall k r)

/-- The staged finite checks discharge exactly the existing panel-target
interface; downstream aggregation and containment proofs are unchanged. -/
theorem panelTargetRefinements_of_staged
    (cache : Fin 32 → PanelCache)
    (data : Fin 32 → PanelMomentData)
    (hdata : ∀ k, (data k).CorrectFor (cache k))
    (hrefines : StagedPanelTargetRefinements cache data hdata) :
    PanelTargetRefinements cache := by
  intro k r
  rw [← stagedPanelBall_eq_tripleFactorPanelBall (hdata k)]
  exact hrefines k r

end P2RoundedMomentRefinement

end RHP2Bridge
