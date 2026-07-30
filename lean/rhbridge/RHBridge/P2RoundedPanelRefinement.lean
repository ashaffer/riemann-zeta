/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedBandCertificate
import RHBridge.P2RoundedPanelTargetAggregate

/-!
# Semantic boundary for the rounded `p = 2` panel certificates

The generated leaves prove two independent facts about each panel cache:

* its rounded factors enclose the exact canonical factors;
* each of its 600 computed entry balls refines the small generated target ball.

This file contains no large computation.  It assembles those facts into the
exact 32-panel enclosure consumed by `P2RoundedBandCertificate`.
-/

namespace RHP2Bridge

open scoped BigOperators

namespace P2RoundedPanelRefinement

open P2RoundedBandCertificate
open P2RoundedPanelTargetData
open P2RoundedPanelTargetAggregate
open P2RoundedSharedEvaluator

/-- The small generated checkpoint ball for entry `r` of panel `k`. -/
def coarsePanelBall (k : Fin 32) (r : Fin 600) : QBall :=
  ⟨panelTargetQ k r, panelAllowanceQ⟩

/-- The entrywise sum of all 32 generated panel checkpoint balls. -/
def coarseAggregateBall (r : Fin 600) : QBall :=
  QBall.finSum fun k : Fin 32 => coarsePanelBall k r

@[simp] theorem coarsePanelBall_center (k : Fin 32) (r : Fin 600) :
    (coarsePanelBall k r).center = panelTargetQ k r := rfl

@[simp] theorem coarsePanelBall_radius (k : Fin 32) (r : Fin 600) :
    (coarsePanelBall k r).radius = panelAllowanceQ := rfl

@[simp] theorem coarseAggregateBall_center (r : Fin 600) :
    (coarseAggregateBall r).center = ∑ k : Fin 32, panelTargetQ k r := rfl

@[simp] theorem coarseAggregateBall_radius (r : Fin 600) :
    (coarseAggregateBall r).radius = ∑ _k : Fin 32, panelAllowanceQ := rfl

/-- Direct unrounded triple-factor ball for generated entry `r` in one cache.
This avoids materializing a rounded product polynomial. -/
def tripleFactorPanelBall
    (cache : PanelCache) (k : Fin 32) (r : Fin 600) : QBall :=
  let e := generatedEntryAt r
  tripleFactorEntryBall k cache
    (p2EntrySelectedKind e.block) e.row e.col

/-- Compact proposition discharged by the split finite panel leaves. -/
def PanelTargetRefinements (cache : Fin 32 → PanelCache) : Prop :=
  ∀ (k : Fin 32) (r : Fin 600),
    (tripleFactorPanelBall (cache k) k r).Refines
      (coarsePanelBall k r)

/-- Analytic enclosure of the exact canonical 32-panel integral sum, obtained
from semantic factor enclosures and the finite rational refinements. -/
theorem abs_p2EntryPanelSumQ_sub_coarseAggregateCenter_le
    (cache : Fin 32 → PanelCache)
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : PanelTargetRefinements cache)
    (r : Fin 600) :
    |DenseRatPoly.p2EntryPanelSumQ (p2UpperEntryAt r).val -
        (coarseAggregateBall r).center| ≤
      (coarseAggregateBall r).radius := by
  unfold coarseAggregateBall
  unfold DenseRatPoly.p2EntryPanelSumQ
  rw [← Fin.sum_univ_eq_sum_range]
  apply QBall.abs_sum_sub_finSum_center_le
  intro k
  exact QBall.abs_sub_center_le_of_refines
    (by
      simpa [tripleFactorPanelBall, generatedEntryAt] using
        abs_p2PanelIntegralQ_sub_tripleFactorEntryBallCenter_le
          (hcache k)
          (p2EntrySelectedKind (generatedEntryAt r).block)
          (generatedEntryAt r).row (generatedEntryAt r).col)
    (hrefines k r)

/-- Final generic handoff: once the small aggregate checkpoint ball fits the
published generated band, the canonical analytic band certificates follow. -/
theorem bandSumCertificates_of_panelTargetRefinements
    (cache : Fin 32 → PanelCache)
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : PanelTargetRefinements cache)
    (hfits : FitsGeneratedBandTable
      (fun r => (coarseAggregateBall r).center)
      (fun r => (coarseAggregateBall r).radius)) :
    P2PanelCertificateAggregate.BandSumCertificates := by
  apply bandSumCertificates_of_fitsGeneratedBandTable
    (fun r => (coarseAggregateBall r).center)
    (fun r => (coarseAggregateBall r).radius)
  · exact abs_p2EntryPanelSumQ_sub_coarseAggregateCenter_le
      cache hcache hrefines
  · exact hfits

/-- The independently generated aggregate-target identity supplies the finite
band-fit premise without touching any polynomial computation. -/
theorem fitsGeneratedBandTable_of_allCentersMatch
    (hcenters : AllCentersMatch) :
    FitsGeneratedBandTable
      (fun r => (coarseAggregateBall r).center)
      (fun r => (coarseAggregateBall r).radius) := by
  intro r
  simpa [coarseAggregateBall, coarsePanelBall,
    bandTargetBall, panelTargetBall] using
      bandTargetBall_fits_generated hcenters r

/-- Complete generic handoff from the three independently checkable finite
interfaces: cache semantics, local target refinements, and target-table
aggregation. -/
theorem bandSumCertificates_of_panelTargetRefinements_and_centers
    (cache : Fin 32 → PanelCache)
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : PanelTargetRefinements cache) :
    P2PanelCertificateAggregate.BandSumCertificates :=
  bandSumCertificates_of_panelTargetRefinements
    cache hcache hrefines
      (fitsGeneratedBandTable_of_allCentersMatch allCentersMatch)

end P2RoundedPanelRefinement

end RHP2Bridge
