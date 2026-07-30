import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel0FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel0FlatComponentChunk27

end RHP2Bridge
