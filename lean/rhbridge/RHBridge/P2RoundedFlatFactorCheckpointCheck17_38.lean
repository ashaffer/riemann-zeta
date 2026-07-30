import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel17FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel17FlatComponentChunk38

end RHP2Bridge
