import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel25FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel25FlatComponentChunk47

end RHP2Bridge
