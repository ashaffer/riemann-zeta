import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel5FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel5FlatComponentChunk39

end RHP2Bridge
