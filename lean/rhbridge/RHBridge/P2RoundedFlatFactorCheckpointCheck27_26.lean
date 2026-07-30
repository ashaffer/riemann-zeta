import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel27FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel27FlatComponentChunk26

end RHP2Bridge
