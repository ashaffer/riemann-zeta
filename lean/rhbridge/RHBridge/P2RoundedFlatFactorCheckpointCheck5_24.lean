import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel5FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel5FlatComponentChunk24

end RHP2Bridge
