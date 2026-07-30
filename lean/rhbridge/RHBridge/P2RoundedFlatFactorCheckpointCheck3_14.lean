import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel3FlatEven14 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel3FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel3FlatEven14 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel3FlatComponentChunk14

end RHP2Bridge
