import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel9FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel9FlatComponentChunk31

end RHP2Bridge
