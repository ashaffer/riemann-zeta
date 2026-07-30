import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel24FlatDefect =
      P2RoundedFactorCheckpointData.panel24DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
