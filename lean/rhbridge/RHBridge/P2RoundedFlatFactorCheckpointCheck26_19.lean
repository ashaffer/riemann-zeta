import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk19 :
    P2RoundedFactorCheckpointData.panel26FlatEven19 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel26FlatEven19_eq :
    P2RoundedFactorCheckpointData.panel26FlatEven19 =
      (P2RoundedFactorCheckpointData.panel26TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  exact panel26FlatComponentChunk19

end RHP2Bridge
