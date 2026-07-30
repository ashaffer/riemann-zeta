import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel17FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel17FlatComponentChunk30

end RHP2Bridge
