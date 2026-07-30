import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel22FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel22FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel22FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel22TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel22FlatComponentChunk40

end RHP2Bridge
