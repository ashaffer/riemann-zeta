import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel21FlatEven10 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven10 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel21FlatComponentChunk10

end RHP2Bridge
