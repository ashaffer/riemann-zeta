import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel27FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel27FlatComponentChunk30

end RHP2Bridge
