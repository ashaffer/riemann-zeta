import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel0FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel0FlatComponentChunk30

end RHP2Bridge
