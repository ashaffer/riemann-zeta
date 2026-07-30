import RHBridge.P2RoundedFlatFactorCheckpointData4

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel4FlatEven6 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel4FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel4FlatEven6 =
      (P2RoundedFactorCheckpointData.panel4TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel4FlatComponentChunk6

end RHP2Bridge
