import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel6FlatEven22 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel6FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel6FlatEven22 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel6FlatComponentChunk22

end RHP2Bridge
