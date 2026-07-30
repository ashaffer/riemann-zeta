import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel17FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel17FlatComponentChunk34

end RHP2Bridge
