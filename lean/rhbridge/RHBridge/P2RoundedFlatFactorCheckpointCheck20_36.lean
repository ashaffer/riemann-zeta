import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel20FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel20FlatComponentChunk36

end RHP2Bridge
