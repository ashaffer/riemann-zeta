import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel4FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel4FlatComponentChunk36

end RHP2Bridge
