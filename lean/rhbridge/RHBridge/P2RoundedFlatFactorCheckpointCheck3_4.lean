import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel3FlatEven4 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel3FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel3FlatEven4 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel3FlatComponentChunk4

end RHP2Bridge
