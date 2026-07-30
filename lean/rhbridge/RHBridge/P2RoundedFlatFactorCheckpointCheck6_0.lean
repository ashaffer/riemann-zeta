import RHBridge.P2RoundedFlatFactorCheckpointData6

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel6FlatEven0 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel6FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel6FlatEven0 =
      (P2RoundedFactorCheckpointData.panel6TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel6FlatComponentChunk0

end RHP2Bridge
