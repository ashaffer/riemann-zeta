import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel5FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel5FlatComponentChunk36

end RHP2Bridge
