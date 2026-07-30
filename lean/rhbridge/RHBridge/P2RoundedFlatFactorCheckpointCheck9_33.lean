import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel9FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel9FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel9TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel9FlatComponentChunk33

end RHP2Bridge
