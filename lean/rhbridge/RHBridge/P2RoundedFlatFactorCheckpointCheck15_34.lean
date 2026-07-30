import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel15FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel15FlatComponentChunk34

end RHP2Bridge
