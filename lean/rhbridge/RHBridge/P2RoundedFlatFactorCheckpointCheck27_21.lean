import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel27FlatEven21 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven21 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel27FlatComponentChunk21

end RHP2Bridge
