import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel7FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel7FlatComponentChunk27

end RHP2Bridge
