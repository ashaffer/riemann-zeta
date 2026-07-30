import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel26FlatEven12 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven12 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel26FlatComponentChunk12

end RHP2Bridge
