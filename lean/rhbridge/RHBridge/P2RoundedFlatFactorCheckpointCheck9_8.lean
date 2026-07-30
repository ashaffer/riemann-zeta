import RHBridge.P2RoundedFlatFactorCheckpointData9

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel9FlatEven8 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel9FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel9FlatEven8 =
      (P2RoundedFactorCheckpointData.panel9TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel9FlatComponentChunk8

end RHP2Bridge
