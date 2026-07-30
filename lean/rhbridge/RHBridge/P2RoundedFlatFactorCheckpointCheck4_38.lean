import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel4FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel4FlatComponentChunk38

end RHP2Bridge
