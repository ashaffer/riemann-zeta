import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel5FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel5FlatComponentChunk34

end RHP2Bridge
