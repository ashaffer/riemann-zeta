import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel30FlatEven2 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel30FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel30FlatEven2 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel30FlatComponentChunk2

end RHP2Bridge
