import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel17FlatEven22 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven22 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel17FlatComponentChunk22

end RHP2Bridge
