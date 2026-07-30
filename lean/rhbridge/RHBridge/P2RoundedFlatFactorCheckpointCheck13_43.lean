import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel13FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel13FlatComponentChunk43

end RHP2Bridge
