import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel17FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel17FlatComponentChunk26

end RHP2Bridge
