import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel22FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel22FlatComponentChunk39

end RHP2Bridge
