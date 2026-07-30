import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel25FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel25FlatComponentChunk28

end RHP2Bridge
