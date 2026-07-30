import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel8FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel8FlatComponentChunk37

end RHP2Bridge
