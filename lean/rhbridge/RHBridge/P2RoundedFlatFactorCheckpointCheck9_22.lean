import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel9FlatEven22 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven22 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel9FlatComponentChunk22

end RHP2Bridge
