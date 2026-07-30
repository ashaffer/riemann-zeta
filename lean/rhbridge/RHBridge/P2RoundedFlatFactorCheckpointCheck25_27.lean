import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel25FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel25FlatComponentChunk27

end RHP2Bridge
