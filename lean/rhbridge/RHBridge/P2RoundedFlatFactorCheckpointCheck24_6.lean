import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel24FlatEven6 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven6 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel24FlatComponentChunk6

end RHP2Bridge
