import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel15FlatDefect =
      P2RoundedFactorCheckpointData.panel15DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
