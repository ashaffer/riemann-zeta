import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel7FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel7FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel7FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel7TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel7FlatComponentChunk32

end RHP2Bridge
