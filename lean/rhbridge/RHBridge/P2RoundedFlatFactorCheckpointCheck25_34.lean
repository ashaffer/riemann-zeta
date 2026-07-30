import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel25FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel25FlatComponentChunk34

end RHP2Bridge
