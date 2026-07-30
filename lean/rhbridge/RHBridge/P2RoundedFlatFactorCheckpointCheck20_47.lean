import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel20FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel20FlatComponentChunk47

end RHP2Bridge
