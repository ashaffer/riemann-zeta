import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk19 :
    P2RoundedFactorCheckpointData.panel25FlatEven19 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven19_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven19 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  exact panel25FlatComponentChunk19

end RHP2Bridge
