import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel4FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel4FlatComponentChunk33

end RHP2Bridge
