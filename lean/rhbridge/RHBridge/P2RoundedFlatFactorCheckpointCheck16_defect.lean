import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatDefect_eq :
    P2RoundedFactorCheckpointData.panel16FlatDefect =
      P2RoundedFactorCheckpointData.panel16DefectPieces.assemble := by
  decide +kernel

end RHP2Bridge
