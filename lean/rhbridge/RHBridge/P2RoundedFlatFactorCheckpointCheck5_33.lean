import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel5FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel5FlatComponentChunk33

end RHP2Bridge
