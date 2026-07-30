import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel26FlatEven7 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven7 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel26FlatComponentChunk7

end RHP2Bridge
