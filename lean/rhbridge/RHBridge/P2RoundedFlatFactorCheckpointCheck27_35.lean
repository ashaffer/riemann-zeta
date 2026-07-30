import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk35 :
    P2RoundedFactorCheckpointData.panel27FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd11_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd11 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨11, by decide⟩ := by
  exact panel27FlatComponentChunk35

end RHP2Bridge
