import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel9FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel9FlatComponentChunk37

end RHP2Bridge
