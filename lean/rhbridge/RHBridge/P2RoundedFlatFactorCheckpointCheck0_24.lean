import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel0FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel0FlatComponentChunk24

end RHP2Bridge
