import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel27FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel27FlatComponentChunk25

end RHP2Bridge
