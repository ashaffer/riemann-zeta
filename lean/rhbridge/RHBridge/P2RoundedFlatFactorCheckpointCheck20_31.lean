import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel20FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel20FlatComponentChunk31

end RHP2Bridge
