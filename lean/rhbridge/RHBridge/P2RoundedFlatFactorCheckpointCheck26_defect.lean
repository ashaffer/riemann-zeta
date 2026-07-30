import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel26FlatDefect =
      P2RoundedFactorCheckpointData.panel26DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
