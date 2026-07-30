import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel27FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel27FlatComponentChunk31

end RHP2Bridge
