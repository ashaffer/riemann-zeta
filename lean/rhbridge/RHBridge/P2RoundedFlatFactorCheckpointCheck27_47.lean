import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel27FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel27FlatComponentChunk47

end RHP2Bridge
