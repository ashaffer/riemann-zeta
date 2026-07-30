import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel4FlatEven22 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven22 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel4FlatComponentChunk22

end RHP2Bridge
