import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel4FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel4FlatComponentChunk24

end RHP2Bridge
