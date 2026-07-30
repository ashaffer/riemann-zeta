import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel27FlatEven23 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven23 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel27FlatComponentChunk23

end RHP2Bridge
