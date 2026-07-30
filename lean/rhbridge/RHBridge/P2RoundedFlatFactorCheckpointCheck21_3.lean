import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel21FlatEven3 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven3 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel21FlatComponentChunk3

end RHP2Bridge
