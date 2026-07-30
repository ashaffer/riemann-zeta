import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel28FlatDefect =
      P2RoundedFactorCheckpointData.panel28DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
