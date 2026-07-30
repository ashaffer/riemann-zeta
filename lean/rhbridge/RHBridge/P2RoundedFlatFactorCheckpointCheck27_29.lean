import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel27FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel27FlatComponentChunk29

end RHP2Bridge
