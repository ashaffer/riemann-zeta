import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel5FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel5FlatComponentChunk27

end RHP2Bridge
