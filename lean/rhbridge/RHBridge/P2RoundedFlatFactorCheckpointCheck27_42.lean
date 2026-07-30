import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel27FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel27FlatComponentChunk42

end RHP2Bridge
