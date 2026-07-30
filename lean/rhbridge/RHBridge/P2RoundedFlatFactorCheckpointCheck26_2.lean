import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel26FlatEven2 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven2 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel26FlatComponentChunk2

end RHP2Bridge
