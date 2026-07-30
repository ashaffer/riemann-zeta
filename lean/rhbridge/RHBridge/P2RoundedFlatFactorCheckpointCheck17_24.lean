import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel17FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel17FlatComponentChunk24

end RHP2Bridge
