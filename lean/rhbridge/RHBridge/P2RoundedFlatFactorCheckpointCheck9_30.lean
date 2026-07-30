import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel9FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel9FlatComponentChunk30

end RHP2Bridge
