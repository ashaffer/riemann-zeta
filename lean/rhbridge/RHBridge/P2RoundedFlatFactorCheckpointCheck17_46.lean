import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel17FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel17FlatComponentChunk46

end RHP2Bridge
