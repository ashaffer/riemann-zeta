import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel25FlatEven8 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven8 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel25FlatComponentChunk8

end RHP2Bridge
