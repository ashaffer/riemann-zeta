import RHBridge.P2RoundedMomentCheckpointData30
import RHBridge.P2RoundedBoundedTriple
import RHBridge.P2RoundedPanelTargetDataAll

namespace RHP2Bridge

open P2RoundedSharedEvaluator

theorem panel30ComponentLengthLe
    (kind : P2SelectedKind) (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel30FlatCache.component
      kind i).coeffs.length ≤ 149 := by
  cases kind <;> fin_cases i <;> decide +kernel

def panel30BoundedRefinementAt (r : Fin 600) : Prop :=
  let e := P2RoundedSharedEvaluator.generatedEntryAt r
  (P2RoundedBoundedTriple.boundedMomentEntryBall
    P2RoundedFactorCheckpointData.panel30MomentData
    P2RoundedFactorCheckpointData.panel30FlatCache
    ⟨30, by decide⟩
    (p2EntrySelectedKind e.block) e.row e.col
    (panel30ComponentLengthLe _ _)).Refines
      (P2RoundedPanelRefinement.coarsePanelBall
        ⟨30, by decide⟩ r)

end RHP2Bridge
