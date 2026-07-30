import RHBridge.P2RoundedFlatFactorCheckpointData16

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel16FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel16FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel16FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel16TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel16FlatComponentChunk45

end RHP2Bridge
