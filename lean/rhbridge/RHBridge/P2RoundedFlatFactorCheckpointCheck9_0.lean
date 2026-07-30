import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel9FlatEven0 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven0 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel9FlatComponentChunk0

end RHP2Bridge
