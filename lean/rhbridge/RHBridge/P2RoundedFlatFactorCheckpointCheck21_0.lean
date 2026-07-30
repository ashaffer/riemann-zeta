import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel21FlatEven0 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven0 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel21FlatComponentChunk0

end RHP2Bridge
