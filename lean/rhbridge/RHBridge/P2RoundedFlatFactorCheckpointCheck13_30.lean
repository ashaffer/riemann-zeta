import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel13FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel13FlatComponentChunk30

end RHP2Bridge
