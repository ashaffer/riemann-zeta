import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel21FlatDefect =
      P2RoundedFactorCheckpointData.panel21DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
