import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel24FlatEven7 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven7 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel24FlatComponentChunk7

end RHP2Bridge
