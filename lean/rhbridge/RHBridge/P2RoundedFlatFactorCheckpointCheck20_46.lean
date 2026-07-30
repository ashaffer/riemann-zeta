import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel20FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel20FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel20FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel20TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel20FlatComponentChunk46

end RHP2Bridge
