import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel4FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel4FlatComponentChunk47

end RHP2Bridge
