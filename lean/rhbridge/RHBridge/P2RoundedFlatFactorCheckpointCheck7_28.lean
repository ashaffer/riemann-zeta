import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel7FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel7FlatComponentChunk28

end RHP2Bridge
