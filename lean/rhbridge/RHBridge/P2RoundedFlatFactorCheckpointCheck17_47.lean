import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel17FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel17FlatComponentChunk47

end RHP2Bridge
