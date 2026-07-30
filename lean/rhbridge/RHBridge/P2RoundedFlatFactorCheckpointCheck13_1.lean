import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel13FlatEven1 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel13FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel13FlatEven1 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel13FlatComponentChunk1

end RHP2Bridge
