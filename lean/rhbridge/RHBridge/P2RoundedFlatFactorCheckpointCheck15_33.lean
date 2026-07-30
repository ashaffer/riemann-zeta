import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel15FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel15FlatComponentChunk33

end RHP2Bridge
