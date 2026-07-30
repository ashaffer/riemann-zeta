import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel30FlatEven12 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel30FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel30FlatEven12 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel30FlatComponentChunk12

end RHP2Bridge
