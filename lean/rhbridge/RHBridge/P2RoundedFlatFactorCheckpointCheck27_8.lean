import RHBridge.P2RoundedFlatFactorCheckpointData27

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel27FlatEven8 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel27FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel27FlatEven8 =
      (P2RoundedFactorCheckpointData.panel27TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel27FlatComponentChunk8

end RHP2Bridge
