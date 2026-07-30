import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel25FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel25FlatComponentChunk33

end RHP2Bridge
