import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel6FlatEven10 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel6FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel6FlatEven10 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel6FlatComponentChunk10

end RHP2Bridge
