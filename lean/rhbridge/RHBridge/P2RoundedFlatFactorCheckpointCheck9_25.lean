import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel9FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel9FlatComponentChunk25

end RHP2Bridge
