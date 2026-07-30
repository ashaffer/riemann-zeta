import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel9FlatDefect =
      P2RoundedFactorCheckpointData.panel9DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
