import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel8FlatEven16 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel8FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel8FlatEven16 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel8FlatComponentChunk16

end RHP2Bridge
