import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel6FlatEven3 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel6FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel6FlatEven3 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel6FlatComponentChunk3

end RHP2Bridge
