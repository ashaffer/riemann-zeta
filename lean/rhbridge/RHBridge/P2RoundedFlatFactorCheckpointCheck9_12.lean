import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel9FlatEven12 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven12 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel9FlatComponentChunk12

end RHP2Bridge
