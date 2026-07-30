import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel2FlatDefect =
      P2RoundedFactorCheckpointData.panel2DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
