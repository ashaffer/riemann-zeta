import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel17FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel17FlatComponentChunk35

end RHP2Bridge
