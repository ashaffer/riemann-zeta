import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel27FlatEven3 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven3 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel27FlatComponentChunk3

end RHP2Bridge
