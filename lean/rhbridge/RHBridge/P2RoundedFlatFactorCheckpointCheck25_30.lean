import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel25FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel25FlatComponentChunk30

end RHP2Bridge
