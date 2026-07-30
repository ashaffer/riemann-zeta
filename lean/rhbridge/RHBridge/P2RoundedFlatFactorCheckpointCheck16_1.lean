import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel16FlatEven1 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven1 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel16FlatComponentChunk1

end RHP2Bridge
