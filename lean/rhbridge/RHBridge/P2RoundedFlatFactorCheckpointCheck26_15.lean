import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel26FlatEven15 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven15 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel26FlatComponentChunk15

end RHP2Bridge
