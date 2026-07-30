import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel9FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel9FlatComponentChunk34

end RHP2Bridge
