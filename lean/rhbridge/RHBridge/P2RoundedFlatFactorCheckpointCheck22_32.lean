import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel22FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel22FlatComponentChunk32

end RHP2Bridge
