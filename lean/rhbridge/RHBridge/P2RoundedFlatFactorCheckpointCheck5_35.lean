import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel5FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel5FlatComponentChunk35

end RHP2Bridge
