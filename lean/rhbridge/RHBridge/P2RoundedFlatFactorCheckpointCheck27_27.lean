import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel27FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel27FlatComponentChunk27

end RHP2Bridge
