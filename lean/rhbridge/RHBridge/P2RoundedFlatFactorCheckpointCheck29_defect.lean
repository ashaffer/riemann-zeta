import RHBridge.P2RoundedFlatFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel29FlatDefect =
      P2RoundedFactorCheckpointData.panel29DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
