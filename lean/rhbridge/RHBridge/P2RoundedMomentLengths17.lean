import RHBridge.P2RoundedMomentCheckpointData17
import RHBridge.P2RoundedBoundedTriple
import RHBridge.P2RoundedPanelTargetDataAll

namespace RHP2Bridge

open P2RoundedSharedEvaluator

theorem panel17ComponentLengthLe
    (kind : P2SelectedKind) (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel17FlatCache.component
      kind i).coeffs.length ≤ 149 := by
  cases kind <;> fin_cases i <;> decide +kernel

def panel17BoundedRefinementAt (r : Fin 600) : Prop :=
  let e := P2RoundedSharedEvaluator.generatedEntryAt r
  (P2RoundedBoundedTriple.boundedMomentEntryBall
    P2RoundedFactorCheckpointData.panel17MomentData
    P2RoundedFactorCheckpointData.panel17FlatCache
    ⟨17, by decide⟩
    (p2EntrySelectedKind e.block) e.row e.col
    (panel17ComponentLengthLe _ _)).Refines
      (P2RoundedPanelRefinement.coarsePanelBall
        ⟨17, by decide⟩ r)

end RHP2Bridge
