import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel0FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel0FlatComponentChunk29

end RHP2Bridge
