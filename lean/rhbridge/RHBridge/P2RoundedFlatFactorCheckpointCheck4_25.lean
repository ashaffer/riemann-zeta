import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel4FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel4FlatComponentChunk25

end RHP2Bridge
