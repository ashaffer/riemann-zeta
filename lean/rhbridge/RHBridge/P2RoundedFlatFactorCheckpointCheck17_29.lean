import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel17FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel17FlatComponentChunk29

end RHP2Bridge
