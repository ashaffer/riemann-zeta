import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk5 :
    P2RoundedFactorCheckpointData.panel25FlatEven5 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven5_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven5 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  exact panel25FlatComponentChunk5

end RHP2Bridge
