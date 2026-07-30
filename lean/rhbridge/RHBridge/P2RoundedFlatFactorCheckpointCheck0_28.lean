import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel0FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel0FlatComponentChunk28

end RHP2Bridge
