import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel20FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel20FlatComponentChunk41

end RHP2Bridge
