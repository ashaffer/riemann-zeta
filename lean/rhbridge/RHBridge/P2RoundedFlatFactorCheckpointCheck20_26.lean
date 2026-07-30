import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel20FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel20FlatComponentChunk26

end RHP2Bridge
