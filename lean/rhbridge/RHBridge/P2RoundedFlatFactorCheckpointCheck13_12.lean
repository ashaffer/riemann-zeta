import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel13FlatEven12 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel13FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel13FlatEven12 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel13FlatComponentChunk12

end RHP2Bridge
