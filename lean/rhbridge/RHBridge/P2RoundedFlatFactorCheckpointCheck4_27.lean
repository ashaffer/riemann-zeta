import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel4FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel4FlatComponentChunk27

end RHP2Bridge
