import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel21FlatEven12 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven12 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel21FlatComponentChunk12

end RHP2Bridge
