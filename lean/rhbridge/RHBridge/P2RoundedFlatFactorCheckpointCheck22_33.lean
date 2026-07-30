import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel22FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel22FlatComponentChunk33

end RHP2Bridge
