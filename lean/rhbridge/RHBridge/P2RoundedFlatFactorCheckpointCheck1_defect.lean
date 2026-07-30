import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel1FlatDefect =
      P2RoundedFactorCheckpointData.panel1DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
