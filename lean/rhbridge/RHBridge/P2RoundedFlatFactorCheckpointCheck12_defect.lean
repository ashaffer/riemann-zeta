import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel12FlatDefect =
      P2RoundedFactorCheckpointData.panel12DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
