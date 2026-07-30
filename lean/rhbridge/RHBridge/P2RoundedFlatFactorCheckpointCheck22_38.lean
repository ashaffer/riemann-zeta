import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel22FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel22FlatComponentChunk38

end RHP2Bridge
