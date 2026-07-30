import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel0FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel0FlatComponentChunk39

end RHP2Bridge
