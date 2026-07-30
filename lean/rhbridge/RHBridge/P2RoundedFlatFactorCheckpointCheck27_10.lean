import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel27FlatEven10 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven10 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel27FlatComponentChunk10

end RHP2Bridge
