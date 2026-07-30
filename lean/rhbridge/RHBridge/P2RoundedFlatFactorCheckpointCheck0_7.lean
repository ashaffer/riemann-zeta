import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel0FlatEven7 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven7 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel0FlatComponentChunk7

end RHP2Bridge
