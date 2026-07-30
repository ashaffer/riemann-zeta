import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel25FlatEven17 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven17 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel25FlatComponentChunk17

end RHP2Bridge
