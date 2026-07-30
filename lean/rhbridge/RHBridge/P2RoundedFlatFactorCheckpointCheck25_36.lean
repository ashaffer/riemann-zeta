import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel25FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel25FlatComponentChunk36

end RHP2Bridge
