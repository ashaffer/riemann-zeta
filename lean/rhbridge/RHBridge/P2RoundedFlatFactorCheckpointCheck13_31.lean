import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel13FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel13FlatComponentChunk31

end RHP2Bridge
