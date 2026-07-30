import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel7FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel7FlatComponentChunk31

end RHP2Bridge
