import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel0FlatEven22 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven22 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel0FlatComponentChunk22

end RHP2Bridge
