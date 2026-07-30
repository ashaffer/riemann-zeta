import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel7FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel7FlatComponentChunk24

end RHP2Bridge
