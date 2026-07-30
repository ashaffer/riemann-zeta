import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel0FlatEven16 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven16 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel0FlatComponentChunk16

end RHP2Bridge
