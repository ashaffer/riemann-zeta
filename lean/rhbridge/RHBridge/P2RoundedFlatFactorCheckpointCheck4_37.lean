import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel4FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel4FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel4FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel4TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel4FlatComponentChunk37

end RHP2Bridge
