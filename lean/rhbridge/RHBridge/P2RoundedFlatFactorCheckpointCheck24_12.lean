import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel24FlatEven12 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven12 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel24FlatComponentChunk12

end RHP2Bridge
