import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel9FlatEven16 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven16 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel9FlatComponentChunk16

end RHP2Bridge
