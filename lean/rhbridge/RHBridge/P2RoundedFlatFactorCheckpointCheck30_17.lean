import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel30FlatEven17 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel30FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel30FlatEven17 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel30FlatComponentChunk17

end RHP2Bridge
