import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel15FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel15FlatComponentChunk42

end RHP2Bridge
