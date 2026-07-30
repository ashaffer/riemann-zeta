import RHBridge.P2RoundedFlatFactorCheckpointData3

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel3FlatEven10 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel3FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel3FlatEven10 =
      (P2RoundedFactorCheckpointData.panel3TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel3FlatComponentChunk10

end RHP2Bridge
