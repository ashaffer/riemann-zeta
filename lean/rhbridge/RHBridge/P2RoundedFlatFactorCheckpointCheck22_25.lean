import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel22FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel22FlatComponentChunk25

end RHP2Bridge
