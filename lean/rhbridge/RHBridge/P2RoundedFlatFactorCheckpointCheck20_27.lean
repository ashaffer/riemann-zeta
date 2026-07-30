import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel20FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel20FlatComponentChunk27

end RHP2Bridge
