import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel25FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel25FlatComponentChunk32

end RHP2Bridge
