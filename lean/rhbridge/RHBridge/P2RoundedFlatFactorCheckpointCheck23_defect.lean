import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel23FlatDefect =
      P2RoundedFactorCheckpointData.panel23DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
