import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel27FlatEven16 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven16 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel27FlatComponentChunk16

end RHP2Bridge
