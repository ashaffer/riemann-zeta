import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel17FlatEven16 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven16 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel17FlatComponentChunk16

end RHP2Bridge
