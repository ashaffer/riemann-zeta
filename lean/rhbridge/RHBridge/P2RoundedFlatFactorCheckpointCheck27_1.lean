import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel27FlatEven1 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven1 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel27FlatComponentChunk1

end RHP2Bridge
