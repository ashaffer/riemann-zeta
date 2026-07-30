import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel7FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel7FlatComponentChunk30

end RHP2Bridge
