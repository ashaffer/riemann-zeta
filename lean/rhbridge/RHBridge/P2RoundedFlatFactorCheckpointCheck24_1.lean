import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel24FlatEven1 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven1 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel24FlatComponentChunk1

end RHP2Bridge
