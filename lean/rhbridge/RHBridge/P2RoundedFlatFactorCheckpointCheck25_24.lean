import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel25FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel25FlatComponentChunk24

end RHP2Bridge
