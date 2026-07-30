import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel20FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel20FlatComponentChunk28

end RHP2Bridge
