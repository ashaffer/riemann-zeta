import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel17FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel17FlatComponentChunk39

end RHP2Bridge
