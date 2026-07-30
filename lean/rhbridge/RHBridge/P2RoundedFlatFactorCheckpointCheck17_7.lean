import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel17FlatEven7 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven7 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel17FlatComponentChunk7

end RHP2Bridge
