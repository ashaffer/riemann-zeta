import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel26FlatEven21 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven21 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel26FlatComponentChunk21

end RHP2Bridge
