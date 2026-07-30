import RHBridge.P2RoundedMomentCheckpointData21
import RHBridge.P2RoundedBoundedTriple
import RHBridge.P2RoundedPanelTargetDataAll

namespace RHP2Bridge

open P2RoundedSharedEvaluator

theorem panel21ComponentLengthLe
    (kind : P2SelectedKind) (i : Fin 24) :
    (P2RoundedFactorCheckpointData.panel21FlatCache.component
      kind i).coeffs.length ≤ 149 := by
  cases kind <;> fin_cases i <;> decide +kernel

def panel21BoundedRefinementAt (r : Fin 600) : Prop :=
  let e := P2RoundedSharedEvaluator.generatedEntryAt r
  (P2RoundedBoundedTriple.boundedMomentEntryBall
    P2RoundedFactorCheckpointData.panel21MomentData
    P2RoundedFactorCheckpointData.panel21FlatCache
    ⟨21, by decide⟩
    (p2EntrySelectedKind e.block) e.row e.col
    (panel21ComponentLengthLe _ _)).Refines
      (P2RoundedPanelRefinement.coarsePanelBall
        ⟨21, by decide⟩ r)

end RHP2Bridge
