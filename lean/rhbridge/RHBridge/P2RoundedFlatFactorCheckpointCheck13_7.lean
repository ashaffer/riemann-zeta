import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel13FlatEven7 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel13FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel13FlatEven7 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel13FlatComponentChunk7

end RHP2Bridge
