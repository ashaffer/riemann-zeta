import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel17FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel17FlatComponentChunk31

end RHP2Bridge
