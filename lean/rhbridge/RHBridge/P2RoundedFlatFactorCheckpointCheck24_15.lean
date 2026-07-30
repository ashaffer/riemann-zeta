import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel24FlatEven15 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven15 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel24FlatComponentChunk15

end RHP2Bridge
