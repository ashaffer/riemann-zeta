import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel20FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel20FlatComponentChunk34

end RHP2Bridge
