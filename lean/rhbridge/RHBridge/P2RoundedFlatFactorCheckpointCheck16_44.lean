import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel16FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel16FlatComponentChunk44

end RHP2Bridge
