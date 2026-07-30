import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel15FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel15FlatComponentChunk27

end RHP2Bridge
