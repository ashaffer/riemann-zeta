import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel0FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel0FlatComponentChunk34

end RHP2Bridge
