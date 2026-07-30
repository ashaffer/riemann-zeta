import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel7FlatEven3 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel7FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel7FlatEven3 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel7FlatComponentChunk3

end RHP2Bridge
