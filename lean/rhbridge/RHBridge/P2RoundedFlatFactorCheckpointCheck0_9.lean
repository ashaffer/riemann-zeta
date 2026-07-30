import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel0FlatEven9 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven9 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel0FlatComponentChunk9

end RHP2Bridge
