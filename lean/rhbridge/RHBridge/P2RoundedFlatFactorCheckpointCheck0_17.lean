import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel0FlatEven17 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven17 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel0FlatComponentChunk17

end RHP2Bridge
