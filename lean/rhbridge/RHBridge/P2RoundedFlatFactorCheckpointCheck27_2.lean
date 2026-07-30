import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel27FlatEven2 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven2 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel27FlatComponentChunk2

end RHP2Bridge
