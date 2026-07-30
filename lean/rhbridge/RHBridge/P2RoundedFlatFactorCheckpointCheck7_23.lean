import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel7FlatEven23 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel7FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel7FlatEven23 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel7FlatComponentChunk23

end RHP2Bridge
