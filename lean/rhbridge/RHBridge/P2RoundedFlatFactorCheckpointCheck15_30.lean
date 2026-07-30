import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel15FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel15FlatComponentChunk30

end RHP2Bridge
