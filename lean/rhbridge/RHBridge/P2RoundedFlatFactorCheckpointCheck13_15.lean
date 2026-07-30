import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel13FlatEven15 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel13FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel13FlatEven15 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel13FlatComponentChunk15

end RHP2Bridge
