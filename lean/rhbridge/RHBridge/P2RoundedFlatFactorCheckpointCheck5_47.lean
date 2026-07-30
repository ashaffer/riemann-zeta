import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel5FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel5FlatComponentChunk47

end RHP2Bridge
