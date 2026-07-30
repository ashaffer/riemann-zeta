import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel17FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel17FlatComponentChunk42

end RHP2Bridge
