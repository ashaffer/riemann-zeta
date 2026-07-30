import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel4FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel4FlatComponentChunk29

end RHP2Bridge
