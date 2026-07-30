import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel20FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel20FlatComponentChunk33

end RHP2Bridge
