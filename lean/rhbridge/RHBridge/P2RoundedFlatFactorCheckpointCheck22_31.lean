import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel22FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel22FlatComponentChunk31

end RHP2Bridge
