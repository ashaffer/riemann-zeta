import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel27FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel27FlatComponentChunk36

end RHP2Bridge
