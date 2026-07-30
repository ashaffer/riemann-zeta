import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel27FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel27FlatComponentChunk28

end RHP2Bridge
