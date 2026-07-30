import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel20FlatEven22 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven22 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel20FlatComponentChunk22

end RHP2Bridge
