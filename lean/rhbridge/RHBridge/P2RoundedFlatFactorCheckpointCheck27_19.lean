import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk19 :
    P2RoundedFactorCheckpointData.panel27FlatEven19 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven19_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven19 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨19, by decide⟩ := by
  exact panel27FlatComponentChunk19

end RHP2Bridge
