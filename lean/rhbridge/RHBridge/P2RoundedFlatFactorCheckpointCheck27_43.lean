import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel27FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel27FlatComponentChunk43

end RHP2Bridge
