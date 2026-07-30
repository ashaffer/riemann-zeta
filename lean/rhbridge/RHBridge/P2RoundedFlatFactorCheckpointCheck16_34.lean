import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel16FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel16FlatComponentChunk34

end RHP2Bridge
