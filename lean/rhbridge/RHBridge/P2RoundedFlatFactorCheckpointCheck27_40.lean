import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel27FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel27FlatComponentChunk40

end RHP2Bridge
