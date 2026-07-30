import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel4FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel4FlatComponentChunk39

end RHP2Bridge
