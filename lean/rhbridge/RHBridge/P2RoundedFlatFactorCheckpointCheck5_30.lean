import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel5FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel5FlatComponentChunk30

end RHP2Bridge
