import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel5FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel5FlatComponentChunk40

end RHP2Bridge
