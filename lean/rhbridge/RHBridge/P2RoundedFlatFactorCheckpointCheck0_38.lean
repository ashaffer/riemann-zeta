import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel0FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel0FlatComponentChunk38

end RHP2Bridge
