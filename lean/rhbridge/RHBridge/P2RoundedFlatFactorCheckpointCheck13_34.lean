import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel13FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel13FlatComponentChunk34

end RHP2Bridge
