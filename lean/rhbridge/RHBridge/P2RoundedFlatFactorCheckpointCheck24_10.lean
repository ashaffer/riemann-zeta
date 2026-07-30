import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel24FlatEven10 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven10 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel24FlatComponentChunk10

end RHP2Bridge
