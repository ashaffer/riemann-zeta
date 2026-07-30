import RHBridge.P2RoundedFlatFactorCheckpointData10

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel10FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel10FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel10FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel10TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel10FlatComponentChunk32

end RHP2Bridge
