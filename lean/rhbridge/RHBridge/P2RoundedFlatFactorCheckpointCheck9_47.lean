import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel9FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel9FlatComponentChunk47

end RHP2Bridge
