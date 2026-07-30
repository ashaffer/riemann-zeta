import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel15FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel15FlatComponentChunk39

end RHP2Bridge
