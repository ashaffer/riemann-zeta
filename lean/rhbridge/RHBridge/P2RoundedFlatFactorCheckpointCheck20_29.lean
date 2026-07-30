import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel20FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel20FlatComponentChunk29

end RHP2Bridge
