import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel27FlatDefect =
      P2RoundedFactorCheckpointData.panel27DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
