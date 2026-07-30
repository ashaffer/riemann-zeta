import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel25FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel25FlatComponentChunk43

end RHP2Bridge
