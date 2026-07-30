import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel5FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel5FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel5FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel5TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel5FlatComponentChunk41

end RHP2Bridge
