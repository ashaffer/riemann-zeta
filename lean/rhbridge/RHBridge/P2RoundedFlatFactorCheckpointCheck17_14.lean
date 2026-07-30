import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel17FlatEven14 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven14 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel17FlatComponentChunk14

end RHP2Bridge
