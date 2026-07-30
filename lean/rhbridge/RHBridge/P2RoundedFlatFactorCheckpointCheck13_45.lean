import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel13FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel13FlatComponentChunk45

end RHP2Bridge
