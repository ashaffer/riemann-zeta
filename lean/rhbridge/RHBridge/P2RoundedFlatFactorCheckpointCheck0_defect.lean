import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel0FlatDefect =
      P2RoundedFactorCheckpointData.panel0DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
