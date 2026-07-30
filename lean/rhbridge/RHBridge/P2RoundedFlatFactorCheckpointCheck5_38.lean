import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel5FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel5FlatComponentChunk38

end RHP2Bridge
