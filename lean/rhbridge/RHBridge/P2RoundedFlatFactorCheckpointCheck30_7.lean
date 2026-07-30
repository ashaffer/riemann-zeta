import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel30FlatEven7 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel30FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel30FlatEven7 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel30FlatComponentChunk7

end RHP2Bridge
