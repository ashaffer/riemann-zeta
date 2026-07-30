import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel0FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel0FlatComponentChunk31

end RHP2Bridge
