import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel26FlatEven0 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven0 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel26FlatComponentChunk0

end RHP2Bridge
