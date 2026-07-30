import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel17FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel17FlatComponentChunk36

end RHP2Bridge
