import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel0FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel0FlatComponentChunk47

end RHP2Bridge
