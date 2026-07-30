import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel20FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel20FlatComponentChunk45

end RHP2Bridge
