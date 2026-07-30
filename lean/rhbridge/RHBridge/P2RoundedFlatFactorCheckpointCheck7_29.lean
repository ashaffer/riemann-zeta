import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel7FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel7FlatComponentChunk29

end RHP2Bridge
