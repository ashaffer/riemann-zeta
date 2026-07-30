import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel25FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel25FlatComponentChunk37

end RHP2Bridge
