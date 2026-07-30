import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel21FlatEven17 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven17 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel21FlatComponentChunk17

end RHP2Bridge
