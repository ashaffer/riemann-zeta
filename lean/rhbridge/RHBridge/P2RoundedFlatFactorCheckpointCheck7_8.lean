import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel7FlatEven8 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel7FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel7FlatEven8 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel7FlatComponentChunk8

end RHP2Bridge
