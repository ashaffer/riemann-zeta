import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel5FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel5FlatComponentChunk32

end RHP2Bridge
