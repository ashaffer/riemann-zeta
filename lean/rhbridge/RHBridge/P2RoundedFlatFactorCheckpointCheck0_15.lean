import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel0FlatEven15 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven15 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel0FlatComponentChunk15

end RHP2Bridge
