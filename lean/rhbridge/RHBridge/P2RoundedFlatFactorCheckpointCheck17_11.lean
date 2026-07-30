import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel17FlatEven11 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven11 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel17FlatComponentChunk11

end RHP2Bridge
