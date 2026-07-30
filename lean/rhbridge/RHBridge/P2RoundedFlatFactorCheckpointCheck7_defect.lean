import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel7FlatDefect =
      P2RoundedFactorCheckpointData.panel7DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
