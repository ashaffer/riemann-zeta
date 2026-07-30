import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel24FlatEven14 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven14 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel24FlatComponentChunk14

end RHP2Bridge
