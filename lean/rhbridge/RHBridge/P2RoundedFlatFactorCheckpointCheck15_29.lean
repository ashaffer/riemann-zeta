import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel15FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel15FlatComponentChunk29

end RHP2Bridge
