import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel18FlatDefect =
      P2RoundedFactorCheckpointData.panel18DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
