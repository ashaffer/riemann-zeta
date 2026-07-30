import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel30FlatDefect =
      P2RoundedFactorCheckpointData.panel30DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
