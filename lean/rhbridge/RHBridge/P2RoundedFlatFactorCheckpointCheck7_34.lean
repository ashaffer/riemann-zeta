import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel7FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel7FlatComponentChunk34

end RHP2Bridge
