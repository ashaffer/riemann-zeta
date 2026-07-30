import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel6FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel6FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel6FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel6TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel6FlatComponentChunk32

end RHP2Bridge
