import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel4FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel4FlatComponentChunk42

end RHP2Bridge
