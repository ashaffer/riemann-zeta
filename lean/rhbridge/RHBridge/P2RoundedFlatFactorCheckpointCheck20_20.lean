import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk20 :
    P2RoundedFactorCheckpointData.panel20FlatEven20 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven20_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven20 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  exact panel20FlatComponentChunk20

end RHP2Bridge
