import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel4FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel4FlatComponentChunk31

end RHP2Bridge
