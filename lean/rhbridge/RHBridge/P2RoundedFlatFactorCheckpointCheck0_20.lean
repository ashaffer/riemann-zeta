import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk20 :
    P2RoundedFactorCheckpointData.panel0FlatEven20 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven20_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven20 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  exact panel0FlatComponentChunk20

end RHP2Bridge
