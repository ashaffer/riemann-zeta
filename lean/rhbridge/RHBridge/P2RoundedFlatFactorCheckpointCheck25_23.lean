import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel25FlatEven23 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven23 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel25FlatComponentChunk23

end RHP2Bridge
