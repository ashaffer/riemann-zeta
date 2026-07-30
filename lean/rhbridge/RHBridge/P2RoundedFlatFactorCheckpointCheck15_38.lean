import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel15FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel15FlatComponentChunk38

end RHP2Bridge
