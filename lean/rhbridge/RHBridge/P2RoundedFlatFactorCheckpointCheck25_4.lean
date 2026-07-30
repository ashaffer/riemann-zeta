import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel25FlatEven4 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven4 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel25FlatComponentChunk4

end RHP2Bridge
