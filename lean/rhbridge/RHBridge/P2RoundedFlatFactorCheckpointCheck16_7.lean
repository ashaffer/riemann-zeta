import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel16FlatEven7 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven7 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel16FlatComponentChunk7

end RHP2Bridge
