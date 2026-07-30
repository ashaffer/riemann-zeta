import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel24FlatEven17 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven17 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel24FlatComponentChunk17

end RHP2Bridge
