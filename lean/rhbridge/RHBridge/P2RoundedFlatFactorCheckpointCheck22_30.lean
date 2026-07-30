import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel22FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel22FlatComponentChunk30

end RHP2Bridge
