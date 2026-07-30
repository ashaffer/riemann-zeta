import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel0FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel0FlatComponentChunk25

end RHP2Bridge
