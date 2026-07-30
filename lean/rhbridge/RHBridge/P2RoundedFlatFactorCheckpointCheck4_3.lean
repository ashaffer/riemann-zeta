import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel4FlatEven3 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven3 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel4FlatComponentChunk3

end RHP2Bridge
