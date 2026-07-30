import RHBridge.P2RoundedFlatFactorCheckpointData24

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel24FlatEven9 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel24FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel24FlatEven9 =
      (P2RoundedFactorCheckpointData.panel24TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel24FlatComponentChunk9

end RHP2Bridge
