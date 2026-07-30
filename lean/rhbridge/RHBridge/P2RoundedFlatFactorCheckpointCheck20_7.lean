import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel20FlatEven7 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven7 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel20FlatComponentChunk7

end RHP2Bridge
