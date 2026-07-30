import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel15FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel15FlatComponentChunk36

end RHP2Bridge
