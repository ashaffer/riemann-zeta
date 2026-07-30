import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel7FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel7FlatComponentChunk26

end RHP2Bridge
