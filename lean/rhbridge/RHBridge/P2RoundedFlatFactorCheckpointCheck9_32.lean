import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel9FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel9FlatComponentChunk32

end RHP2Bridge
