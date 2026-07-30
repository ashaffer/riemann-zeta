import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel15FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel15FlatComponentChunk47

end RHP2Bridge
