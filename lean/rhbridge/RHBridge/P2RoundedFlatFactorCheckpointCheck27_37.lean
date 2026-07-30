import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel27FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel27FlatComponentChunk37

end RHP2Bridge
