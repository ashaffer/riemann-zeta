import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel0FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel0FlatComponentChunk43

end RHP2Bridge
