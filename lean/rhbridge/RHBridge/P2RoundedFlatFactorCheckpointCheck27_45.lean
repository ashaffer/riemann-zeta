import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel27FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel27FlatComponentChunk45

end RHP2Bridge
