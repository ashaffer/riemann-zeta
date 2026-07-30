import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel4FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel4FlatComponentChunk45

end RHP2Bridge
