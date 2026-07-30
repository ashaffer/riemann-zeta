import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel15FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel15FlatComponentChunk43

end RHP2Bridge
