import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel20FlatDefect =
      P2RoundedFactorCheckpointData.panel20DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
