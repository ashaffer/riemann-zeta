import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel16FlatEven14 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven14 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel16FlatComponentChunk14

end RHP2Bridge
