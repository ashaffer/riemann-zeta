import RHBridge.P2RoundedFlatFactorCheckpointData7

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FlatComponentChunk20 :
    P2RoundedFactorCheckpointData.panel7FlatEven20 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel7FlatEven20_eq :
    P2RoundedFactorCheckpointData.panel7FlatEven20 =
      (P2RoundedFactorCheckpointData.panel7TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  exact panel7FlatComponentChunk20

end RHP2Bridge
