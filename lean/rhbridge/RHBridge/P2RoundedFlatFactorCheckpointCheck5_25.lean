import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel5FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel5FlatComponentChunk25

end RHP2Bridge
