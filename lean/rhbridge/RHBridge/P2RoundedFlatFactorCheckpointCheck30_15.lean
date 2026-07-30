import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel30FlatEven15 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel30FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel30FlatEven15 =
      (P2RoundedFactorCheckpointData.panel30TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel30FlatComponentChunk15

end RHP2Bridge
