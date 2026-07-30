import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel22FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel22FlatComponentChunk34

end RHP2Bridge
