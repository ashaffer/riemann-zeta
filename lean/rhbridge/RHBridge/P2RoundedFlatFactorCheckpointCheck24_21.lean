import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel24FlatEven21 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven21 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel24FlatComponentChunk21

end RHP2Bridge
