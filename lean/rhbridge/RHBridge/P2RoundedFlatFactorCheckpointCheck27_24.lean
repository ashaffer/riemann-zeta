import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel27FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel27FlatComponentChunk24

end RHP2Bridge
