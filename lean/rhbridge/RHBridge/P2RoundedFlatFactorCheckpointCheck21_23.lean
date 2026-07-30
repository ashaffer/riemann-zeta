import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel21FlatEven23 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven23 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel21FlatComponentChunk23

end RHP2Bridge
