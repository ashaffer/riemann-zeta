import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel20FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel20FlatComponentChunk42

end RHP2Bridge
