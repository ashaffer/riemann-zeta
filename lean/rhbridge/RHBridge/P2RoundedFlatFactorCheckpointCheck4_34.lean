import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel4FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel4FlatComponentChunk34

end RHP2Bridge
