import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel27FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel27FlatComponentChunk41

end RHP2Bridge
