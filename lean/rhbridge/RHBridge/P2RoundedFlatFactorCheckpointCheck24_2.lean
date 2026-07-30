import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel24FlatEven2 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven2 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel24FlatComponentChunk2

end RHP2Bridge
