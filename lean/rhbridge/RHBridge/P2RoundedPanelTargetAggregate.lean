/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2RoundedPanelTargetDataAll
import RHBridge.P2RoundedSharedEvaluator
import RHBridge.P2PanelCertificateAggregate

/-!
# Aggregate boundary for the generated `p = 2` panel targets

The 32 panel targets use the same `10^-40` grid as the independently
generated band-integral table.  This file isolates their inexpensive table
identity from the analytic rounded-polynomial checks.
-/

namespace RHP2Bridge

namespace P2RoundedPanelTargetAggregate

open P2PanelCertificateAggregate
open P2RoundedPanelTargetData
open P2RoundedSharedEvaluator

/-- Coarse target ball used after a panel's rounded-polynomial calculation
has refined to the generated `10^-40` center. -/
def panelTargetBall (k : Fin 32) (r : Fin 600) : QBall :=
  ⟨panelTargetQ k r, panelAllowanceQ⟩

/-- The inexpensive 32-panel aggregate, independent of all polynomial
evaluation. -/
def bandTargetBall (r : Fin 600) : QBall :=
  QBall.finSum fun k : Fin 32 => panelTargetBall k r

@[simp] theorem bandTargetBall_center (r : Fin 600) :
    (bandTargetBall r).center = ∑ k : Fin 32, panelTargetQ k r := rfl

@[simp] theorem bandTargetBall_radius (r : Fin 600) :
    (bandTargetBall r).radius = 32 / 10 ^ 18 := by
  simp [bandTargetBall, panelTargetBall, panelAllowanceQ]
  norm_num

/-- Small closed predicate for one generated-table coordinate. -/
def CenterMatchesAt (r : Fin 600) : Prop :=
  (bandTargetBall r).center =
    generatedBandIntegralQ (p2UpperEntryAt r).val

/-- Executable form of the complete target-table identity.  It contains no
analytic statement: both sides are explicit rational tables. -/
def AllCentersMatch : Prop :=
  ∀ r : Fin 600, CenterMatchesAt r

/-- The final panel center is an exact residual, so the target-table identity
is a symbolic rational identity for arbitrary `r`; it needs no 600-row
generated equality certificate. -/
theorem sum_panelTargetQ_eq_generated (r : Fin 600) :
    (∑ k : Fin 32, panelTargetQ k r) =
      generatedBandIntegralQ (p2UpperEntryAt r).val := by
  simp [Fin.sum_univ_succ, panelTargetQ, first31PanelTargetSumQ]
  ring

theorem allCentersMatch : AllCentersMatch := by
  intro r
  unfold CenterMatchesAt
  rw [bandTargetBall_center]
  exact sum_panelTargetQ_eq_generated r

theorem bandTargetBall_center_eq_generated
    (h : AllCentersMatch) (r : Fin 600) :
    (bandTargetBall r).center =
      generatedBandIntegralQ (p2UpperEntryAt r).val :=
  h r

/-- Once the table identity is checked, the target aggregate fits in the
existing `10^-15` band allowance with a large exact-rational margin. -/
theorem bandTargetBall_fits_generated
    (h : AllCentersMatch) (r : Fin 600) :
    |(bandTargetBall r).center -
        generatedBandIntegralQ (p2UpperEntryAt r).val| +
      (bandTargetBall r).radius ≤
        P2PanelCertificateData.bandIntegralRoundingRadius := by
  rw [bandTargetBall_center_eq_generated h r,
    bandTargetBall_radius]
  norm_num [P2PanelCertificateData.bandIntegralRoundingRadius]

/-- Analytic factor enclosures and 32 local refinement checks combine with
the cheap target-table identity.  This is the semantic handoff required by
the aggregate band certificate; no polynomial expression is reduced here. -/
theorem abs_panelSum_sub_generated_le
    (h : AllCentersMatch) (r : Fin 600)
    (cache : Fin 32 → PanelCache)
    (hcache : ∀ k, (cache k).EnclosesCanonical k)
    (hrefines : ∀ k,
      ((panelBallsFromCache k (cache k)).get r).Refines
        (panelTargetBall k r)) :
    |DenseRatPoly.p2EntryPanelSumQ (p2UpperEntryAt r).val -
        generatedBandIntegralQ (p2UpperEntryAt r).val| ≤
      32 / 10 ^ 18 := by
  have hsum :=
    abs_p2EntryPanelSumQ_sub_coarseFinSumCenter_le_of_enclosesCanonical
      r cache (fun k => panelTargetBall k r) hcache hrefines
  change
    |DenseRatPoly.p2EntryPanelSumQ (p2UpperEntryAt r).val -
        (bandTargetBall r).center| ≤
      (bandTargetBall r).radius at hsum
  rw [bandTargetBall_center_eq_generated h r,
    bandTargetBall_radius] at hsum
  exact hsum

end P2RoundedPanelTargetAggregate

end RHP2Bridge
