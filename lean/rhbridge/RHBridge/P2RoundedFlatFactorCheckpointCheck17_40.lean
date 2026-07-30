import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel17FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel17FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel17FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel17TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel17FlatComponentChunk40

end RHP2Bridge
