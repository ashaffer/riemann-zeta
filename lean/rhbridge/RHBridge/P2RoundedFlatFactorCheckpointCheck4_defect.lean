import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel4FlatDefect =
      P2RoundedFactorCheckpointData.panel4DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
