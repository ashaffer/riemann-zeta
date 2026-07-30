import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel26FlatEven10 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven10 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel26FlatComponentChunk10

end RHP2Bridge
