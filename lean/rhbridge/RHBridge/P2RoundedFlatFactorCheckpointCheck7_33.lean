import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel7FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel7FlatComponentChunk33

end RHP2Bridge
