import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel5FlatDefect =
      P2RoundedFactorCheckpointData.panel5DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
