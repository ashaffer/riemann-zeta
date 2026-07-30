import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel7FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel7FlatComponentChunk25

end RHP2Bridge
