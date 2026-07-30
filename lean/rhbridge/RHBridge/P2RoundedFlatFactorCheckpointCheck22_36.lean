import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel22FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel22FlatComponentChunk36

end RHP2Bridge
