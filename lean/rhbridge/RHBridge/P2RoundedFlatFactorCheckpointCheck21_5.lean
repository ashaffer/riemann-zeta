import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk5 :
    P2RoundedFactorCheckpointData.panel21FlatEven5 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel21FlatEven5_eq :
    P2RoundedFactorCheckpointData.panel21FlatEven5 =
      (P2RoundedFactorCheckpointData.panel21TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  exact panel21FlatComponentChunk5

end RHP2Bridge
