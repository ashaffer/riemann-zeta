import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel17FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel17FlatComponentChunk25

end RHP2Bridge
