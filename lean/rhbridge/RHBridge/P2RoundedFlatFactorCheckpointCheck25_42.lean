import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel25FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel25FlatComponentChunk42

end RHP2Bridge
