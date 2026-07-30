import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel3FlatEven8 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel3FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel3FlatEven8 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel3FlatComponentChunk8

end RHP2Bridge
