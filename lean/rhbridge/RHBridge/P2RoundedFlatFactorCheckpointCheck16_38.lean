import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel16FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel16FlatComponentChunk38

end RHP2Bridge
