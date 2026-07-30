import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel21FlatEven7 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven7 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel21FlatComponentChunk7

end RHP2Bridge
