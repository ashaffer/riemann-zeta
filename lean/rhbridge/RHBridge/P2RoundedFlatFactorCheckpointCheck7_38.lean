import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel7FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel7FlatComponentChunk38

end RHP2Bridge
