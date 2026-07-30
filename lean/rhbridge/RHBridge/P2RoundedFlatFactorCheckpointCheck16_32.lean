import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel16FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel16FlatComponentChunk32

end RHP2Bridge
