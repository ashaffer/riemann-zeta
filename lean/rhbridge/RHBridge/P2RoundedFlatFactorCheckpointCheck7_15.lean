import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel7FlatEven15 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel7FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel7FlatEven15 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel7FlatComponentChunk15

end RHP2Bridge
