import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel22FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel22FlatComponentChunk29

end RHP2Bridge
