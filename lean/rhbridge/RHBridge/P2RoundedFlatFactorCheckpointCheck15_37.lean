import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel15FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel15FlatComponentChunk37

end RHP2Bridge
