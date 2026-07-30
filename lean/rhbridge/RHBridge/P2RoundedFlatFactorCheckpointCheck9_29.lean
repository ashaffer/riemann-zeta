import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel9FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel9FlatComponentChunk29

end RHP2Bridge
