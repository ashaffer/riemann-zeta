import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel16FlatEven13 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven13 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel16FlatComponentChunk13

end RHP2Bridge
