import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel9FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel9FlatComponentChunk24

end RHP2Bridge
