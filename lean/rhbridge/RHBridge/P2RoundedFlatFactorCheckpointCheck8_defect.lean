import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel8FlatDefect =
      P2RoundedFactorCheckpointData.panel8DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
