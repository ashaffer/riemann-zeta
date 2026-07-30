import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel17FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel17FlatComponentChunk33

end RHP2Bridge
