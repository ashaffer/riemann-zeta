import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel27FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel27FlatComponentChunk38

end RHP2Bridge
