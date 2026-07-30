import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel22FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel22FlatComponentChunk45

end RHP2Bridge
