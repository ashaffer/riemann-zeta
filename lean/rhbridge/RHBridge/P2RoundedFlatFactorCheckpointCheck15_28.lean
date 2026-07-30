import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel15FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel15FlatComponentChunk28

end RHP2Bridge
