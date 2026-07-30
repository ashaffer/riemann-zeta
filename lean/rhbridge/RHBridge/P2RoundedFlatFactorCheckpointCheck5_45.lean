import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel5FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel5FlatComponentChunk45

end RHP2Bridge
