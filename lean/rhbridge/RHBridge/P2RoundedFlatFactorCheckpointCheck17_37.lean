import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel17FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel17FlatComponentChunk37

end RHP2Bridge
