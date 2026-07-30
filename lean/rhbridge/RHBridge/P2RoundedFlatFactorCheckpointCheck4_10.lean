import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel4FlatEven10 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven10 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel4FlatComponentChunk10

end RHP2Bridge
