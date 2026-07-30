import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk20 :
    P2RoundedFactorCheckpointData.panel4FlatEven20 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven20_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven20 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  exact panel4FlatComponentChunk20

end RHP2Bridge
