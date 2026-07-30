import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel0FlatEven0 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven0 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel0FlatComponentChunk0

end RHP2Bridge
