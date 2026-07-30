import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel16FlatEven10 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven10 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel16FlatComponentChunk10

end RHP2Bridge
