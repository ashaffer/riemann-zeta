import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel27FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel27FlatComponentChunk34

end RHP2Bridge
