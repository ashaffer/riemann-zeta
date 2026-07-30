import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel27FlatEven12 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven12 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel27FlatComponentChunk12

end RHP2Bridge
