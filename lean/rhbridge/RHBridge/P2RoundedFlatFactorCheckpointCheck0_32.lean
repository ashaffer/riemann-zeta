import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel0FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel0FlatComponentChunk32

end RHP2Bridge
