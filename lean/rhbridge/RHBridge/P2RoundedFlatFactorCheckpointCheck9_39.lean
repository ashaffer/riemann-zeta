import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel9FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel9FlatComponentChunk39

end RHP2Bridge
