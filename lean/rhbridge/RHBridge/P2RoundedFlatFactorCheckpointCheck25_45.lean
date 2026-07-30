import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel25FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel25FlatComponentChunk45

end RHP2Bridge
