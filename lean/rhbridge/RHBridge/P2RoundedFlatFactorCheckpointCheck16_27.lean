import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel16FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel16FlatComponentChunk27

end RHP2Bridge
