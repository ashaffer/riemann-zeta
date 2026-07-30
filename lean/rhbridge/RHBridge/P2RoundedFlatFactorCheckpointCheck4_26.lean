import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel4FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel4FlatComponentChunk26

end RHP2Bridge
