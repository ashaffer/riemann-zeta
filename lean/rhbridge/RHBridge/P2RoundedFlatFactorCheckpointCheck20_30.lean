import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel20FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel20FlatComponentChunk30

end RHP2Bridge
