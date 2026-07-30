import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel16FlatEven0 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel16FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel16FlatEven0 =
      (P2RoundedFactorCheckpointData.panel16TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel16FlatComponentChunk0

end RHP2Bridge
