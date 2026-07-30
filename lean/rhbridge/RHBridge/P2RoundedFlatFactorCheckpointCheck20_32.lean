import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel20FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel20FlatComponentChunk32

end RHP2Bridge
