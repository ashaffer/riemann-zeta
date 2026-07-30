import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel26FlatEven23 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven23 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel26FlatComponentChunk23

end RHP2Bridge
