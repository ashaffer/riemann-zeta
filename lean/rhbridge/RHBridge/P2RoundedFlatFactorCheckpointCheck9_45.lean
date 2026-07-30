import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel9FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel9FlatComponentChunk45

end RHP2Bridge
