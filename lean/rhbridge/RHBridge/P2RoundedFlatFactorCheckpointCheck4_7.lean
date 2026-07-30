import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel4FlatEven7 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven7 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel4FlatComponentChunk7

end RHP2Bridge
