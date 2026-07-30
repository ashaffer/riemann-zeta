import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel4FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel4FlatComponentChunk32

end RHP2Bridge
