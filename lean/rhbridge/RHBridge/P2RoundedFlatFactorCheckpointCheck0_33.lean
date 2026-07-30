import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel0FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel0FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel0FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel0TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel0FlatComponentChunk33

end RHP2Bridge
