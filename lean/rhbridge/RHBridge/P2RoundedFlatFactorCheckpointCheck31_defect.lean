import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel31FlatDefect =
      P2RoundedFactorCheckpointData.panel31DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
