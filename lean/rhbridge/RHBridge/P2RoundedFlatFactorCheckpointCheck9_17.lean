import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel9FlatEven17 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven17 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel9FlatComponentChunk17

end RHP2Bridge
