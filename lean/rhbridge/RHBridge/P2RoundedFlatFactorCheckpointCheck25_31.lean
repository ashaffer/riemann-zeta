import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel25FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel25FlatComponentChunk31

end RHP2Bridge
