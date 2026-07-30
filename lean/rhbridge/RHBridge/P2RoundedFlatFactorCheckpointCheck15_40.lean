import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel15FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel15FlatComponentChunk40

end RHP2Bridge
