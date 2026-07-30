import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel22FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel22FlatComponentChunk24

end RHP2Bridge
