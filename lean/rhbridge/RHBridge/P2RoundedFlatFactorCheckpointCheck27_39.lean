import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel27FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel27FlatComponentChunk39

end RHP2Bridge
