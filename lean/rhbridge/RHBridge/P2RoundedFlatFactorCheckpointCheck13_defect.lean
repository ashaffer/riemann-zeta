import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel13FlatDefect =
      P2RoundedFactorCheckpointData.panel13DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
