import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel13FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel13FlatComponentChunk29

end RHP2Bridge
