import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel20FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel20FlatComponentChunk24

end RHP2Bridge
