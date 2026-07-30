import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel8FlatEven23 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel8FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel8FlatEven23 =
      (P2RoundedFactorCheckpointData.panel8TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel8FlatComponentChunk23

end RHP2Bridge
