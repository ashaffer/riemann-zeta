import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel13FlatEven6 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel13FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel13FlatEven6 =
      (P2RoundedFactorCheckpointData.panel13TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel13FlatComponentChunk6

end RHP2Bridge
