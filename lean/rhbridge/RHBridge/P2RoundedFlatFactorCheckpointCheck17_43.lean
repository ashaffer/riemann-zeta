import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel17FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel17FlatComponentChunk43

end RHP2Bridge
