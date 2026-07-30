import RHBridge.P2RoundedFlatFactorCheckpointData0
import RHBridge.P2RoundedPanelTargetData0

namespace RHP2Bridge

open P2RoundedFactorCheckpointData
open P2RoundedPanelTargetData
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0TripleFactorRefines599 :
    (tripleFactorEntryBall ⟨0, by decide⟩ panel0FlatCache .odd
        ⟨23, by decide⟩ ⟨23, by decide⟩).Refines
      ⟨panel0TargetQ ⟨599, by decide⟩, panelAllowanceQ⟩ := by
  unfold QBall.Refines
  decide +kernel

end RHP2Bridge
