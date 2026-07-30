import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel17FlatEven21 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven21 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel17FlatComponentChunk21

end RHP2Bridge
