import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel0FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel0FlatComponentChunk42

end RHP2Bridge
