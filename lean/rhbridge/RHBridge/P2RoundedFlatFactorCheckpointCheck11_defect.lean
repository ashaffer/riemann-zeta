import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel11FlatDefect =
      P2RoundedFactorCheckpointData.panel11DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
