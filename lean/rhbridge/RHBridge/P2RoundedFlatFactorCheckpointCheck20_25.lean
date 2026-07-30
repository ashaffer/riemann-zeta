import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel20FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel20FlatComponentChunk25

end RHP2Bridge
