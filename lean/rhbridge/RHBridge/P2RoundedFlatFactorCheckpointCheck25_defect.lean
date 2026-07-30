import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel25FlatDefect =
      P2RoundedFactorCheckpointData.panel25DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
