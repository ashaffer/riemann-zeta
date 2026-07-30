import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel20FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel20FlatComponentChunk37

end RHP2Bridge
