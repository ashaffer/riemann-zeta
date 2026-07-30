import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel9FlatEven23 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven23 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel9FlatComponentChunk23

end RHP2Bridge
