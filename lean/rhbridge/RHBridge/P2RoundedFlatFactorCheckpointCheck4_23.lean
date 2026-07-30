import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel4FlatEven23 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven23 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel4FlatComponentChunk23

end RHP2Bridge
