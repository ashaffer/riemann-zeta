import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel20FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel20FlatComponentChunk43

end RHP2Bridge
