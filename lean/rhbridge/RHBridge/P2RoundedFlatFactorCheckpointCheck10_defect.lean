import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel10FlatDefect =
      P2RoundedFactorCheckpointData.panel10DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
