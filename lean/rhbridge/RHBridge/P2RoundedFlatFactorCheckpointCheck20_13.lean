import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel20FlatEven13 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven13 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel20FlatComponentChunk13

end RHP2Bridge
