import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel27FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel27FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel27FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel27TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel27FlatComponentChunk46

end RHP2Bridge
