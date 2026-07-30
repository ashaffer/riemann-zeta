import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel7FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel7FlatComponentChunk36

end RHP2Bridge
