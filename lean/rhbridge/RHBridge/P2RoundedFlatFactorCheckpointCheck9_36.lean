import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel9FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel9FlatComponentChunk36

end RHP2Bridge
