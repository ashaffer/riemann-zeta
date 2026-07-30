import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel20FlatEven4 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven4 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel20FlatComponentChunk4

end RHP2Bridge
