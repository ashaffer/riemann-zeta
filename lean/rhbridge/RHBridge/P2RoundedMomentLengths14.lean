import RHBridge.P2RoundedMomentCheckpointData14
import RHBridge.P2RoundedBoundedTriple
import RHBridge.P2RoundedPanelTargetDataAll

namespace RHP2Bridge

open P2RoundedSharedEvaluator

theorem panel14ComponentLengthLe
    (kind : P2SelectedKind) (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel14FlatCache.component
      kind i).coeffs.length ≤ 149 := by
  cases kind <;> fin_cases i <;> decide +kernel

def panel14BoundedRefinementAt (r : Fin 600) : Prop :=
  let e := P2RoundedSharedEvaluator.generatedEntryAt r
  (P2RoundedBoundedTriple.boundedMomentEntryBall
    P2RoundedFactorCheckpointData.panel14MomentData
    P2RoundedFactorCheckpointData.panel14FlatCache
    ⟨14, by decide⟩
    (p2EntrySelectedKind e.block) e.row e.col
    (panel14ComponentLengthLe _ _)).Refines
      (P2RoundedPanelRefinement.coarsePanelBall
        ⟨14, by decide⟩ r)

end RHP2Bridge
