import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel7FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel7FlatComponentChunk43

end RHP2Bridge
