import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel15FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel15FlatComponentChunk26

end RHP2Bridge
