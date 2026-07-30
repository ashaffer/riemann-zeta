import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk19 :
    P2RoundedFactorCheckpointData.panel0FlatEven19 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven19_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven19 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  exact panel0FlatComponentChunk19

end RHP2Bridge
