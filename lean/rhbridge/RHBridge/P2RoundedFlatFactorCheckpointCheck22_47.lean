import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel22FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel22FlatComponentChunk47

end RHP2Bridge
