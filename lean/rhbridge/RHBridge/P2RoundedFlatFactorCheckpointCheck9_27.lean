import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel9FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel9FlatComponentChunk27

end RHP2Bridge
