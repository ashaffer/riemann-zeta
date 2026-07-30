import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel15FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel15FlatComponentChunk45

end RHP2Bridge
