import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel17FlatEven0 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven0 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel17FlatComponentChunk0

end RHP2Bridge
